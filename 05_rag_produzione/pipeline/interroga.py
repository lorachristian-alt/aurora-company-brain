# -*- coding: utf-8 -*-
"""
interroga.py — la catena di interrogazione della configurazione C.

    domanda -> [denso k1 | sparso k2] -> RRF -> reranker cross-encoder -> passaggi -> LLM

Due classi, e sono separate apposta:

  `Recupero`   tiene embedder + BM25 + Qdrant + reranker. E' la PASSATA 1.
  `Generatore` parla con Ollama e non tocca nessun modello locale. E' la PASSATA 2.

Sono separate perche' su una macchina da 8 GB non ci stanno insieme: bge-m3 (2,3 GB),
il reranker (2,3 GB) e il modello di Ollama (2,0 GB) piu' Qdrant e Python sfondano la
RAM e la macchina inizia a paginare, che significa tempi moltiplicati. Il risultato per
singola domanda e' identico a quello di una pipeline che gira tutta d'un fiato — cambia
solo l'ordine in cui si pagano i passi.

La FUSIONE RRF e' fatta in Python e non lato Qdrant di proposito: serve avere in mano le
due classifiche separate coi loro punteggi per poterle scrivere nella traccia di audit.
E' la traccia l'argomento di vendita, non la riga di codice in meno.
"""

import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pipeline import comune                                        # noqa: E402
from pipeline.bm25 import IndiceBM25                               # noqa: E402


# ==================================================================== PASSATA 1

class Recupero:
    """Recupero ibrido + fusione + rerank. Carica i modelli solo al primo uso."""

    def __init__(self, cfg):
        self.cfg = cfg
        comune.fissa_thread(cfg)
        from qdrant_client import QdrantClient, models
        self.models = models
        self.client = QdrantClient(path=str(comune.INDICE))
        self.collezione = cfg["indice"]["collezione"]
        self.bm25 = IndiceBM25.carica(comune.INDICE.parent / "vocabolario_bm25.json")
        self._emb = None
        self._rer = None

    # ---------------------------------------------------------------- modelli

    def embedder(self):
        if self._emb is None:
            from sentence_transformers import SentenceTransformer
            d = self.cfg["embedding_denso"]
            self._emb = SentenceTransformer(str(comune.RADICE / d["percorso_locale"]),
                                            device=self.cfg["esecuzione"]["device"])
            self._emb.max_seq_length = d["max_seq_length"]
        return self._emb

    def reranker(self):
        if self._rer is None:
            from sentence_transformers import CrossEncoder
            r = self.cfg["reranker"]
            self._rer = CrossEncoder(str(comune.RADICE / r["percorso_locale"]),
                                     device=self.cfg["esecuzione"]["device"],
                                     max_length=r["max_length"])
        return self._rer

    # ---------------------------------------------------------------- rami

    def vettore_domanda(self, domanda):
        """Un vettore per volta, batch di 1. Il batch NON e' un parametro libero qui:
        cambiarlo cambia il riempimento e quindi l'ultima cifra del vettore. Uno per
        volta e' l'unica scelta che da' lo stesso numero comunque si esegua il run."""
        return self.embedder().encode([domanda], normalize_embeddings=True,
                                      convert_to_numpy=True)[0].tolist()

    def _ramo_denso(self, domanda, k, vettore=None):
        v = vettore if vettore is not None else self.vettore_domanda(domanda)
        r = self.client.query_points(self.collezione, query=v,
                                     using=self.cfg["indice"]["vettore_denso"],
                                     limit=k, with_payload=True).points
        return [{"cid": p.id, "punteggio": float(p.score), "file": p.payload["file"],
                 "idx": p.payload["idx"], "origine": p.payload["origine"]} for p in r]

    def _ramo_sparso(self, domanda, k):
        ind, val = self.bm25.vettore_domanda(domanda)
        if not ind:
            return []
        r = self.client.query_points(
            self.collezione,
            query=self.models.SparseVector(indices=ind, values=val),
            using=self.cfg["indice"]["vettore_sparso"], limit=k, with_payload=True).points
        return [{"cid": p.id, "punteggio": float(p.score), "file": p.payload["file"],
                 "idx": p.payload["idx"], "origine": p.payload["origine"]} for p in r]

    # ---------------------------------------------------------------- fusione

    def _rrf(self, denso, sparso, k_rrf, quanti):
        """Reciprocal Rank Fusion: 1/(k + rango), ranghi a partire da 1.

        Non ha pesi da tarare — ed e' il motivo per cui e' stata scelta: un peso fra
        denso e sparso andrebbe deciso guardando i risultati, che qui e' vietato.
        Parita' rotta sul `cid`, cosi' due esecuzioni danno lo stesso ordine sempre.
        """
        punti = {}
        for elenco, ramo in ((denso, "denso"), (sparso, "sparso")):
            for rango, c in enumerate(elenco, 1):
                v = punti.setdefault(c["cid"], {"cid": c["cid"], "file": c["file"],
                                                "idx": c["idx"], "origine": c["origine"],
                                                "rrf": 0.0, "rango_denso": None,
                                                "rango_sparso": None})
                v["rrf"] += 1.0 / (k_rrf + rango)
                v["rango_%s" % ramo] = rango
        ordinati = sorted(punti.values(), key=lambda x: (-x["rrf"], x["cid"]))
        return ordinati[:quanti]

    # ---------------------------------------------------------------- testi

    def _testi(self, cid):
        r = self.client.retrieve(self.collezione, ids=list(cid), with_payload=True)
        return {p.id: p.payload for p in r}

    # ---------------------------------------------------------------- interrogazione

    def recupera(self, domanda, vettore=None):
        """Restituisce la traccia completa di un'interrogazione, generazione esclusa.

        `vettore` permette di passare l'embedding gia' calcolato: e' cosi' che il runner
        evita di tenere embedder e reranker in memoria nello stesso momento.
        """
        c = self.cfg["recupero"]
        t0 = time.time()
        denso = self._ramo_denso(domanda, c["k_denso"], vettore)
        t_denso = time.time() - t0

        t0 = time.time()
        sparso = self._ramo_sparso(domanda, c["k_sparso"])
        t_sparso = time.time() - t0

        fusi = self._rrf(denso, sparso, c["k_rrf"], self.cfg["reranker"]["top_in"])
        payload = self._testi([x["cid"] for x in fusi])

        t0 = time.time()
        coppie = [(domanda, payload[x["cid"]]["testo"]) for x in fusi]
        voti = self.reranker().predict(
            coppie, batch_size=self.cfg["reranker"]["batch"],
            show_progress_bar=False) if coppie else []
        t_rerank = time.time() - t0

        for x, v in zip(fusi, voti):
            x["rerank"] = float(v)
        riordinati = sorted(fusi, key=lambda x: (-x["rerank"], x["cid"]))
        finali = riordinati[:self.cfg["reranker"]["top_out"]]

        # Budget di contesto: si taglia in coda, mai a meta' di un passaggio scelto.
        budget = self.cfg["generazione"]["budget_contesto_caratteri"]
        passaggi, usati, scartati = [], 0, []
        for x in finali:
            testo = payload[x["cid"]]["testo"]
            if usati + len(testo) > budget and passaggi:
                scartati.append(x["cid"])
                continue
            usati += len(testo)
            passaggi.append({"cid": x["cid"], "file": payload[x["cid"]]["file"],
                             "origine": payload[x["cid"]]["origine"],
                             "rerank": x["rerank"], "testo": testo})

        return {
            "domanda": domanda,
            "candidati_densi": denso,
            "candidati_sparsi": sparso,
            "fusione_rrf": [{k: v for k, v in x.items() if k != "rerank"} for x in fusi],
            "ordine_post_rerank": [{"cid": x["cid"], "file": x["file"],
                                    "rerank": x["rerank"]} for x in riordinati],
            "passaggi_consegnati": passaggi,
            "scartati_per_budget": scartati,
            "caratteri_contesto": usati,
            "tempi": {"denso": round(t_denso, 2), "sparso": round(t_sparso, 2),
                      "rerank": round(t_rerank, 2)},
        }

    def chiudi(self):
        self.client.close()

    def libera_modelli(self):
        """Lascia andare embedder e reranker. Su una macchina da 8 GB non e' igiene: e'
        la differenza fra un run di tre ore e uno che pagina."""
        import gc
        self._emb = None
        self._rer = None
        gc.collect()


# ==================================================================== il prompt

def costruisci_prompt(domanda, passaggi, cfg):
    """Le regole sono quelle della misura B (metodo_02, P2.1), tradotte per un modello
    locale che risponde a UNA domanda con i passaggi gia' davanti. Le regole non si
    ammorbidiscono: se cambiassero, C smetterebbe di essere confrontabile con B."""
    blocchi = []
    for n, p in enumerate(passaggi, 1):
        blocchi.append("[%d] file: %s\n%s" % (n, p["file"], p["testo"]))
    return cfg["generazione"]["template"].format(
        passaggi="\n\n".join(blocchi), domanda=domanda)


def estrai_campi(testo_risposta, passaggi):
    """Da testo libero ai campi del formato di misura.

    Restituisce (risposta, fonti, confidenza, fonti_fuori_contesto).

    Il parsing e' tollerante di proposito: un 3B non rispetta un formato rigido il 100%
    delle volte, e un errore di formattazione non deve diventare una risposta persa. Se
    le righe di coda mancano, `fonti` resta vuoto e `confidenza` diventa «bassa»: e' cio'
    che il modello ha davvero dichiarato, e riempirlo d'ufficio sarebbe inventare.

    ⚠️ `fonti` contiene TUTTI i nomi che il modello ha citato, anche quelli che non erano
    fra i passaggi consegnati. Filtrarli sarebbe ripulire la misura a favore di C: in A e
    in B il giudice vede le fonti come il modello le ha scritte, e P3 classifica come
    `allucinata` proprio la fonte citata che non contiene il dato. Togliere gli inventati
    darebbe a C meno allucinazioni per costruzione, e i tre numeri smetterebbero di
    parlarsi.

    `fonti_fuori_contesto` e' la stessa informazione a uso diagnostico: finisce nella
    traccia e nel verbale, non nel file di risposte.
    """
    righe = [r.strip() for r in (testo_risposta or "").splitlines()]
    fonti, fuori, confidenza, corpo = [], [], None, []
    nomi_validi = {p["file"] for p in passaggi}
    for r in righe:
        alta = r.upper()
        if alta.startswith("FONTI:"):
            grezze = [x.strip().strip("[]`\"' ") for x in r.split(":", 1)[1].split(",")]
            for g in grezze:
                if not g or g.lower() in ("nessuna", "nessuno", "-", "n/a"):
                    continue
                if g not in fonti:
                    fonti.append(g)
                if g not in nomi_validi and g not in fuori:
                    fuori.append(g)
        elif alta.startswith("CONFIDENZA:"):
            v = r.split(":", 1)[1].strip().lower()
            confidenza = v if v in ("alta", "media", "bassa") else None
        else:
            corpo.append(r)
    return ("\n".join(corpo).strip(), fonti, confidenza or "bassa", fuori)


# ==================================================================== PASSATA 2

class Generatore:
    """Il solo pezzo che parla con Ollama. Nessun modello locale caricato qui dentro."""

    def __init__(self, cfg):
        self.cfg = cfg
        g = cfg["generazione"]
        self.url = g["endpoint"]
        self.corpo_base = {
            "model": g["modello"],
            "stream": False,
            "keep_alive": g["keep_alive"],
            "options": {
                "temperature": g["temperature"],
                "seed": g["seed"],
                "num_ctx": g["num_ctx"],
                "num_predict": g["num_predict"],
                "top_k": g["top_k"],
                "top_p": g["top_p"],
                "repeat_penalty": g["repeat_penalty"],
            },
        }

    def disponibile(self):
        try:
            with urllib.request.urlopen(self.url.replace("/api/generate", "/api/tags"),
                                        timeout=5) as r:
                modelli = {m["name"] for m in json.loads(r.read())["models"]}
            return self.cfg["generazione"]["modello"] in modelli, sorted(modelli)
        except Exception as exc:                                   # noqa: BLE001
            return False, "Ollama non raggiungibile: %s" % exc

    def genera(self, prompt):
        corpo = dict(self.corpo_base, prompt=prompt)
        req = urllib.request.Request(
            self.url, data=json.dumps(corpo).encode("utf-8"),
            headers={"Content-Type": "application/json"})
        t0 = time.time()
        with urllib.request.urlopen(req, timeout=self.cfg["generazione"]["timeout_s"]) as r:
            d = json.loads(r.read())
        return {
            "testo": d.get("response", ""),
            "secondi": round(time.time() - t0, 2),
            "token_prompt": d.get("prompt_eval_count"),
            "token_risposta": d.get("eval_count"),
            "modello": d.get("model"),
        }


# ==================================================================== uso a mano

def main():
    """Interrogazione singola da riga di comando: serve al collaudo e alle demo.

        python pipeline\\interroga.py "una ricerca sul lotto L26130 recupera il mass balance?"
    """
    sys.stdout.reconfigure(line_buffering=True)
    solo_recupero = "--solo-recupero" in sys.argv
    liberi = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not liberi:
        sys.exit('uso: python pipeline\\interroga.py "la domanda" [--solo-recupero]')
    domanda = liberi[0]

    cfg = comune.carica_config()
    rec = Recupero(cfg)
    tr = rec.recupera(domanda)
    print("\n--- passaggi consegnati (%d) ---" % len(tr["passaggi_consegnati"]))
    for n, p in enumerate(tr["passaggi_consegnati"], 1):
        print("[%d] %-55s rerank %+.3f  origine %s" % (n, p["file"], p["rerank"],
                                                       p["origine"]))
    print("tempi: %s" % tr["tempi"])
    rec.chiudi()

    if solo_recupero:
        return
    gen = Generatore(cfg)
    ok, info = gen.disponibile()
    if not ok:
        sys.exit("modello non disponibile in Ollama: %s" % (info,))
    out = gen.genera(costruisci_prompt(domanda, tr["passaggi_consegnati"], cfg))
    risposta, fonti, conf, fuori = estrai_campi(out["testo"], tr["passaggi_consegnati"])
    print("\n--- risposta (%.1fs, %s token prompt, %s token risposta) ---"
          % (out["secondi"], out["token_prompt"], out["token_risposta"]))
    print(risposta)
    print("fonti: %s | confidenza: %s" % (fonti, conf))
    if fuori:
        print("⚠️ fonti citate che NON erano fra i passaggi consegnati: %s" % fuori)


if __name__ == "__main__":
    main()
