# -*- coding: utf-8 -*-
"""
runner_misura.py — il runner della baseline C, a DUE PASSATE.

    passata 1 (retrieval)    denso + sparso -> RRF -> rerank -> traccia su disco
    passata 2 (generazione)  traccia -> prompt -> Ollama -> riga di risposta

Perche' due passate e non una. Su 8 GB di RAM i tre modelli non convivono: bge-m3 e il
reranker pesano 2,3 GB l'uno, il modello di Ollama 2,0 GB. Tenendoli insieme la macchina
pagina, e un run che dura sei ore ne dura venti. Separando le passate, in memoria c'e'
sempre un solo protagonista. Il risultato per domanda e' identico: cambia l'ordine in cui
si pagano i passi, non cosa viene calcolato.

Entrambe le passate sono RIPRENDIBILI riga per riga: si guarda cosa c'e' gia' su disco e
si riparte da li'. Un'interruzione costa al massimo la domanda in corso.

⚠️ PERIMETRO. Questo script legge `03_valutazione\\domande_solo.jsonl` — id e testo delle
domande, senza risposte. E' l'unica eccezione strumentale prevista dalla scaletta, ed e'
concessa a uno SCRIPT, non a una sessione. Per questo il runner non stampa mai il testo di
una domanda ne' di una risposta: a schermo escono solo id, conteggi e tempi.

Uso:
    python pipeline\\runner_misura.py --passata retrieval
    python pipeline\\runner_misura.py --passata generazione
    python pipeline\\runner_misura.py --passata retrieval --limite 5 --sonda
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pipeline import comune                                        # noqa: E402
from pipeline.interroga import (Generatore, Recupero, costruisci_prompt,  # noqa: E402
                                estrai_campi)

DOMANDE = comune.RADICE / "03_valutazione" / "domande_solo.jsonl"


# ------------------------------------------------------------------ utilita'

def cartella_misura(cfg, nome=None):
    d = comune.RADICE / "04_misurazioni" / (nome or cfg["misura"]["cartella"])
    (d / "tracce").mkdir(parents=True, exist_ok=True)
    return d


def leggi_domande():
    if not DOMANDE.exists():
        sys.exit("manca %s" % DOMANDE)
    out = []
    with open(DOMANDE, encoding="utf-8") as f:
        for r in f:
            r = r.strip()
            if r:
                d = json.loads(r)
                out.append((d["id"], d["domanda"]))
    return out


def id_gia_fatti(percorso):
    fatti = set()
    if not Path(percorso).exists():
        return fatti
    with open(percorso, encoding="utf-8") as f:
        for r in f:
            r = r.strip()
            if not r:
                continue
            try:
                fatti.add(json.loads(r)["id"])
            except Exception:                                      # noqa: BLE001
                pass          # riga troncata da un'interruzione: si rifa' quella domanda
    return fatti


def appendi(percorso, riga):
    """Append con fsync: se la macchina si spegne a meta' notte, cio' che e' scritto e'
    scritto davvero e la ripresa non perde nulla."""
    with open(percorso, "a", encoding="utf-8") as f:
        f.write(json.dumps(riga, ensure_ascii=False) + "\n")
        f.flush()
        os.fsync(f.fileno())


# ------------------------------------------------------------------ passata 1

def passata_retrieval(cfg, cartella, limite=None, sonda=False):
    contesti = cartella / "contesti_c.jsonl"
    tracce = cartella / "tracce"
    tutte = leggi_domande()
    fatti = id_gia_fatti(contesti)
    restanti = [(i, d) for i, d in tutte if i not in fatti]
    if limite:
        restanti = restanti[:limite]
    print("passata 1 (retrieval): %d da fare su %d totali (%d gia' presenti)"
          % (len(restanti), len(tutte), len(fatti)))
    if not restanti:
        return {"fatte": 0, "totali": len(tutte)}

    rec = Recupero(cfg)
    impronta = cfg.get("_impronta")
    tempi = []
    t_inizio = time.time()
    try:
        for n, (qid, testo) in enumerate(restanti, 1):
            t0 = time.time()
            tr = rec.recupera(testo)
            dt = time.time() - t0
            tempi.append(dt)
            tr.update(id=qid, config_c=impronta, quando=datetime.now().isoformat(timespec="seconds"),
                      secondi=round(dt, 2))
            (tracce / ("%s.json" % qid)).write_text(
                json.dumps(tr, ensure_ascii=False, indent=1), encoding="utf-8")
            appendi(contesti, {
                "id": qid,
                "passaggi": [{"cid": p["cid"], "file": p["file"], "origine": p["origine"],
                              "rerank": round(p["rerank"], 4)}
                             for p in tr["passaggi_consegnati"]],
                "caratteri_contesto": tr["caratteri_contesto"],
                "secondi": round(dt, 2),
            })
            medio = sum(tempi) / len(tempi)
            print("  %3d/%d  %s  %5.1fs  (medio %5.1fs, rimanenti ~%.1f h)"
                  % (n, len(restanti), qid, dt, medio,
                     medio * (len(restanti) - n) / 3600))
    finally:
        rec.chiudi()

    r = {"fatte": len(tempi), "totali": len(tutte),
         "secondi_totali": round(time.time() - t_inizio, 1),
         "secondi_medi": round(sum(tempi) / len(tempi), 2) if tempi else None,
         "secondi_min": round(min(tempi), 2) if tempi else None,
         "secondi_max": round(max(tempi), 2) if tempi else None}
    if sonda:
        print("\nSONDA retrieval: %.1fs medi -> %.1f h sulle %d domande"
              % (r["secondi_medi"], r["secondi_medi"] * len(tutte) / 3600, len(tutte)))
    return r


# ------------------------------------------------------------------ passata 2

def passata_generazione(cfg, cartella, limite=None, sonda=False):
    risposte = cartella / cfg["misura"]["file_risposte"]
    tracce = cartella / "tracce"
    contesti = cartella / "contesti_c.jsonl"

    if not contesti.exists():
        sys.exit("manca %s: la passata 1 (retrieval) non e' mai stata eseguita.\n"
                 "  python pipeline\\runner_misura.py --passata retrieval" % contesti.name)
    pronti = [v["id"] for v in map(json.loads,
                                   [r for r in contesti.read_text(encoding="utf-8")
                                    .splitlines() if r.strip()])]
    fatti = id_gia_fatti(risposte)
    restanti = [i for i in pronti if i not in fatti]
    if limite:
        restanti = restanti[:limite]
    print("passata 2 (generazione): %d da fare su %d con contesto (%d gia' risposte)"
          % (len(restanti), len(pronti), len(fatti)))
    if not restanti:
        return {"fatte": 0, "totali": len(pronti)}

    gen = Generatore(cfg)
    ok, info = gen.disponibile()
    if not ok:
        sys.exit("Ollama: %s" % (info,))
    print("Ollama: modello %s disponibile" % cfg["generazione"]["modello"])

    tempi, senza_fonti, vuote, con_fuori = [], 0, 0, 0
    t_inizio = time.time()
    for n, qid in enumerate(restanti, 1):
        tr = json.loads((tracce / ("%s.json" % qid)).read_text(encoding="utf-8"))
        passaggi = tr["passaggi_consegnati"]
        prompt = costruisci_prompt(tr["domanda"], passaggi, cfg)
        try:
            out = gen.genera(prompt)
        except Exception as exc:                                   # noqa: BLE001
            print("  %3d/%d  %s  ERRORE DEL RUNNER: %s" % (n, len(restanti), qid,
                                                           type(exc).__name__))
            appendi(cartella / "errori_runner.jsonl",
                    {"id": qid, "passata": "generazione", "errore": repr(exc)})
            continue
        risposta, fonti, conf, fuori = estrai_campi(out["testo"], passaggi)
        if not fonti:
            senza_fonti += 1
        if not risposta:
            vuote += 1
        if fuori:
            con_fuori += 1
        appendi(risposte, {"id": qid, "risposta": risposta, "fonti": fonti,
                           "confidenza": conf})
        tr["generazione"] = {
            "modello": out["modello"], "secondi": out["secondi"],
            "token_prompt": out["token_prompt"], "token_risposta": out["token_risposta"],
            "testo_grezzo": out["testo"], "fonti_citate": fonti,
            "fonti_fuori_contesto": fuori, "confidenza": conf,
        }
        (tracce / ("%s.json" % qid)).write_text(
            json.dumps(tr, ensure_ascii=False, indent=1), encoding="utf-8")
        tempi.append(out["secondi"])
        medio = sum(tempi) / len(tempi)
        print("  %3d/%d  %s  %6.1fs  (medio %5.1fs, rimanenti ~%.1f h)"
              % (n, len(restanti), qid, out["secondi"], medio,
                 medio * (len(restanti) - n) / 3600))

    r = {"fatte": len(tempi), "totali": len(pronti),
         "secondi_totali": round(time.time() - t_inizio, 1),
         "secondi_medi": round(sum(tempi) / len(tempi), 2) if tempi else None,
         "risposte_senza_fonti": senza_fonti, "risposte_vuote": vuote,
         "risposte_con_fonti_fuori_contesto": con_fuori}
    if sonda:
        print("\nSONDA generazione: %.1fs medi -> %.1f h sulle %d domande"
              % (r["secondi_medi"], r["secondi_medi"] * len(pronti) / 3600, len(pronti)))
    return r


# ------------------------------------------------------------------ main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--passata", choices=("retrieval", "generazione"), required=True)
    ap.add_argument("--limite", type=int, default=None,
                    help="lavora solo sulle prime N domande non ancora fatte")
    ap.add_argument("--sonda", action="store_true", help="stampa la stima sulle 282")
    ap.add_argument("--cartella", default=None)
    a = ap.parse_args()
    sys.stdout.reconfigure(line_buffering=True)

    cfg = comune.carica_config()
    from pipeline.impronta import impronta_config
    cfg["_impronta"] = impronta_config(cfg)
    comune.fissa_thread(cfg)
    cartella = cartella_misura(cfg, a.cartella)
    print("cartella della misura: %s" % cartella)

    t0 = time.time()
    if a.passata == "retrieval":
        r = passata_retrieval(cfg, cartella, a.limite, a.sonda)
    else:
        r = passata_generazione(cfg, cartella, a.limite, a.sonda)
    r.update(passata=a.passata, quando=datetime.now().isoformat(timespec="seconds"),
             minuti=round((time.time() - t0) / 60, 1))
    appendi(cartella / "rapporto_run.jsonl", r)
    print("\n%s" % json.dumps(r, ensure_ascii=False))


if __name__ == "__main__":
    main()
