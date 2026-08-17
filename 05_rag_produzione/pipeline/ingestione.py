# -*- coding: utf-8 -*-
"""
ingestione.py — dal corpus ai chunk, con i metadati.

Legge tutti i file del corpus, ne estrae il testo (cache su disco, chiave = SHA-256 del
grezzo), lo spezza secondo il config e produce `chunk.jsonl` piu' un rapporto di
ingestione con i conteggi. Non tocca Qdrant: separare l'ingestione dall'indicizzazione
serve a poter guardare i pezzi prima di pagare l'embedding, e a rifare l'indice senza
ri-estrarre niente.

Uso:
    python pipeline\\ingestione.py                       # corpus v1, verificato col manifest
    python pipeline\\ingestione.py --corpus <cartella>   # Sessione 6: il vault
    python pipeline\\ingestione.py --senza-verifica      # solo per corpus fuori manifest

E' il punto di estensione dell'ingestione: una inbox sorvegliata o una fonte Notion in
sola lettura si agganciano qui, scrivendo altri file nella stessa cartella di lavoro
prima di questo passo. Nel corpus v1 non c'e' contenuto Notion da misurare, quindi la
fonte inbound resta documentata e non costruita (decisione del 15/08/2026).
"""

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pipeline import comune                                       # noqa: E402
from pipeline.verifica_corpus import verifica                      # noqa: E402


def scheda(voce):
    """La scheda di un file senza testo utile: nome, formato e perche' non c'e' testo.

    Serve a un principio solo: nessun file del corpus e' invisibile all'indice. Un file
    che non produce testo sparirebbe del tutto, e una domanda sull'inventario
    dell'archivio non avrebbe modo di raggiungerlo. La scheda dichiara cio' che e', e non
    afferma nulla sul contenuto.
    """
    d = voce.get("ocr") or {}
    if voce["origine"] == "illeggibile":
        perche = "file non apribile dall'estrattore (%s)" % d.get("errore", "errore")
    elif d.get("motivo"):
        perche = d["motivo"]
    elif "sopra_soglia" in d:
        perche = ("OCR sotto soglia: %d parole, confidenza media %.1f, %d caratteri "
                  "alfanumerici" % (d.get("parole", 0), d.get("confidenza_media", 0.0),
                                    d.get("caratteri_alfanumerici", 0)))
    else:
        perche = "nessun testo estraibile"
    return ("[scheda documento] File: %s — formato %s. Nessun contenuto testuale "
            "disponibile per questo file (%s). Il file esiste nell'archivio; il suo "
            "contenuto non e' leggibile dalla pipeline."
            % (voce["nome"], voce["formato"], perche))


# Cartelle che non sono contenuto: configurazione dello strumento, non archivio.
# `.obsidian\` e' esclusa dal perimetro della misura «dopo» da metodo_02 (addendum),
# e va esclusa QUI, non a mano il giorno della Sessione 6.
CARTELLE_ESCLUSE = (".obsidian", ".git", ".claude", "__pycache__", ".venv")


def ingerisci(corpus, cfg, verifica_manifest=True, uscita=None, escluse=None):
    corpus = Path(corpus)
    escluse = set(escluse if escluse is not None else CARTELLE_ESCLUSE)
    uscita = Path(uscita or (comune.LOCALE / "chunk.jsonl"))
    uscita.parent.mkdir(parents=True, exist_ok=True)

    if verifica_manifest:
        ok, r = verifica()
        if not ok:
            sys.exit("MANIFEST FALLITO: %d/%d verificati, %d mancanti, %d intrusi, "
                     "%d divergenti. Non indicizzo un corpus non verificabile."
                     % (r["verificati"], r["attesi"], len(r["mancanti"]),
                        len(r["intrusi"]), len(r["divergenti"])))
        print("manifest: %d/%d file verificati" % (r["verificati"], r["attesi"]))

    file = sorted(p for p in corpus.rglob("*")
                  if p.is_file() and not (escluse & set(p.relative_to(corpus).parts)))
    print("ingestione di %d file da %s (cartelle escluse: %s)"
          % (len(file), corpus, ", ".join(sorted(escluse)) or "nessuna"))

    per_formato, per_origine, schede, righe = {}, {}, [], []
    cid = 0
    t0 = time.time()
    for n, p in enumerate(file, 1):
        voce = comune.estrai(p, cfg)
        testo = voce.get("testo") or ""
        origine = voce["origine"]
        if testo.strip():
            pezzi = comune.spezza(testo, cfg)
        else:
            pezzi = [scheda(voce)]
            origine = "scheda"
            schede.append({"nome": voce["nome"], "formato": voce["formato"],
                           "diagnostica": voce.get("ocr")})
        for i, pezzo in enumerate(pezzi):
            md = comune.metadati_chunk(pezzo)
            righe.append({
                "cid": cid,
                "file": p.name,
                "percorso_relativo": str(p.relative_to(corpus)).replace("\\", "/"),
                "sha256_file": voce["sha256"],
                "formato": voce["formato"],
                "origine": origine,
                "idx": i,
                "n_chunk_file": len(pezzi),
                "caratteri": len(pezzo),
                "testo_sha256": hashlib.sha256(pezzo.encode("utf-8")).hexdigest(),
                "codici": md["codici"],
                "date": md["date"],
                "testo": pezzo,
            })
            cid += 1
        per_formato[voce["formato"]] = per_formato.get(voce["formato"], 0) + len(pezzi)
        per_origine[origine] = per_origine.get(origine, 0) + len(pezzi)
        if n % 25 == 0 or n == len(file):
            print("  %3d/%d file  ->  %d chunk  (%.0fs)" % (n, len(file), cid,
                                                            time.time() - t0))

    with open(uscita, "w", encoding="utf-8") as f:
        for r in righe:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # I duplicati NON si fondono: sono contenuto (metodo_01 §11, regola d'oro 1). Si
    # contano, e il payload porta l'hash del pezzo perche' chi vuole possa deduplicare
    # al momento della risposta invece che dentro l'indice.
    visti, dup = set(), 0
    for r in righe:
        if r["testo_sha256"] in visti:
            dup += 1
        visti.add(r["testo_sha256"])

    rapporto = {
        "corpus": str(corpus),
        "cartelle_escluse": sorted(escluse),
        "file_letti": len(file),
        "chunk_totali": len(righe),
        "chunk_per_formato": dict(sorted(per_formato.items())),
        "chunk_per_origine": dict(sorted(per_origine.items())),
        "chunk_duplicati_non_fusi": dup,
        "file_senza_testo_utile": schede,
        "caratteri_totali": sum(r["caratteri"] for r in righe),
        "secondi": round(time.time() - t0, 1),
        "config": {"chunking": cfg["chunking"], "estrazione": cfg["estrazione"]},
        "tesseract": comune.versione_tesseract(cfg),
    }
    (uscita.with_name("rapporto_ingestione.json")).write_text(
        json.dumps(rapporto, ensure_ascii=False, indent=1), encoding="utf-8")

    print("\nchunk: %d da %d file in %.1f min" % (len(righe), len(file),
                                                  rapporto["secondi"] / 60))
    print("per formato: %s" % rapporto["chunk_per_formato"])
    print("per origine: %s" % rapporto["chunk_per_origine"])
    if schede:
        print("file senza testo utile (%d): %s"
              % (len(schede), ", ".join(s["nome"] for s in schede)))
    print("scritto %s" % uscita)
    return rapporto


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", default=str(comune.RADICE / "02_corpus"))
    ap.add_argument("--senza-verifica", action="store_true",
                    help="salta il controllo col manifest (corpus diversi dal v1)")
    ap.add_argument("--uscita", default=None)
    ap.add_argument("--escludi", default=",".join(CARTELLE_ESCLUSE),
                    help="cartelle da saltare, separate da virgola")
    a = ap.parse_args()
    sys.stdout.reconfigure(line_buffering=True)
    cfg = comune.carica_config()
    comune.fissa_thread(cfg)
    ingerisci(a.corpus, cfg, verifica_manifest=not a.senza_verifica, uscita=a.uscita,
              escluse=[x for x in a.escludi.split(",") if x])


if __name__ == "__main__":
    main()
