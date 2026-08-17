# -*- coding: utf-8 -*-
"""
verifica_run_c.py — l'integrita' del run della baseline C, ricontata da zero.

Non si fida del rapporto che il runner ha scritto di se stesso: riapre i file prodotti e
li conta. Controlla che ci siano tutte e sole le 282 domande, che nessun id sia doppio o
mancante, che ogni risposta abbia la sua traccia, e che la continuita' del run sia
leggibile nei timestamp.

⚠️ Non apre `03_valutazione\\eval_set.jsonl` e non stampa il testo delle domande ne'
delle risposte: qui si contano righe, non si giudica.

Uso:
    python verifica_run_c.py [--cartella baseline_c_2026-08-17_grezzo]
"""

import argparse
import collections
import json
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent
RADICE = BASE.parent
DOMANDE = RADICE / "03_valutazione" / "domande_solo.jsonl"


def righe(p):
    if not Path(p).exists():
        return []
    fuori, rotte = [], 0
    for r in Path(p).read_text(encoding="utf-8").splitlines():
        r = r.strip()
        if not r:
            continue
        try:
            fuori.append(json.loads(r))
        except json.JSONDecodeError:
            rotte += 1
    if rotte:
        print("  ⚠ %d righe illeggibili in %s" % (rotte, Path(p).name))
    return fuori


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cartella", default="baseline_c_2026-08-17_grezzo")
    a = ap.parse_args()
    d = BASE / a.cartella
    esito_ok = True

    # --- l'elenco atteso viene dalle domande, non da cio' che il runner ha prodotto
    attesi = [v["id"] for v in righe(DOMANDE)]
    print("domande attese (domande_solo.jsonl) : %d" % len(attesi))
    if len(set(attesi)) != len(attesi):
        print("  ⚠ il file delle domande ha id duplicati")
        esito_ok = False

    ris = righe(d / "misuraC_risposte.jsonl")
    ctx = righe(d / "contesti_c.jsonl")
    tracce = sorted((d / "tracce").glob("*.json"))
    ids_ris = [v["id"] for v in ris]

    print("\n--- conteggi ---")
    print("righe in misuraC_risposte.jsonl     : %d" % len(ris))
    print("righe in contesti_c.jsonl           : %d" % len(ctx))
    print("file di traccia                     : %d" % len(tracce))

    print("\n--- copertura e unicita' ---")
    dup = [k for k, v in collections.Counter(ids_ris).items() if v > 1]
    mancanti = [i for i in attesi if i not in set(ids_ris)]
    estranei = [i for i in ids_ris if i not in set(attesi)]
    for etichetta, elenco in (("id duplicati", dup), ("id mancanti", mancanti),
                              ("id estranei", estranei)):
        print("%-36s: %d%s" % (etichetta, len(elenco),
                               ("  -> " + ", ".join(elenco[:10])) if elenco else ""))
        if elenco:
            esito_ok = False
    senza_traccia = [i for i in ids_ris if not (d / "tracce" / ("%s.json" % i)).exists()]
    print("%-36s: %d" % ("risposte senza traccia", len(senza_traccia)))
    if senza_traccia:
        esito_ok = False

    # --- ORDINE: le risposte devono seguire l'ordine delle domande, o il file e' stato
    # ricomposto a mano invece che scritto in append
    print("%-36s: %s" % ("ordine identico a domande_solo",
                         "si" if ids_ris == attesi else "NO"))

    print("\n--- qualita' formale delle risposte (non e' un giudizio) ---")
    print("%-36s: %d" % ("risposte vuote", sum(1 for v in ris if not v["risposta"].strip())))
    print("%-36s: %d" % ("risposte senza fonti", sum(1 for v in ris if not v["fonti"])))
    conf = collections.Counter(v["confidenza"] for v in ris)
    print("%-36s: %s" % ("confidenza dichiarata", dict(conf)))

    # --- fonti citate che NON erano fra i passaggi consegnati: si legge dalle tracce
    fuori_ctx = 0
    for t in tracce:
        g = json.loads(t.read_text(encoding="utf-8")).get("generazione") or {}
        if g.get("fonti_fuori_contesto"):
            fuori_ctx += 1
    print("%-36s: %d" % ("risposte con fonti fuori contesto", fuori_ctx))

    # --- errori del runner
    err = d / "errori_runner.jsonl"
    print("%-36s: %s" % ("errori del runner",
                         "nessuno" if not err.exists() else "%d" % len(righe(err))))
    if err.exists():
        esito_ok = False

    # --- CONTINUITA': i timestamp delle tracce raccontano se il run si e' interrotto
    print("\n--- continuita' del run (timestamp scritti dal runner nelle tracce) ---")
    momenti = []
    for t in tracce:
        tr = json.loads(t.read_text(encoding="utf-8"))
        g = tr.get("generazione")
        if g and tr.get("quando"):
            momenti.append((tr["id"], tr["quando"]))
    if momenti:
        print("prima traccia scritta               : %s" % min(m[1] for m in momenti))
        print("ultima traccia scritta              : %s" % max(m[1] for m in momenti))

    # i tempi di generazione, ricontati dalle tracce e non dal rapporto del runner
    tempi = []
    for t in tracce:
        g = json.loads(t.read_text(encoding="utf-8")).get("generazione") or {}
        if g.get("secondi"):
            tempi.append(g["secondi"])
    if tempi:
        print("generazioni con tempo registrato    : %d" % len(tempi))
        print("secondi per risposta                : medio %.1f, min %.1f, max %.1f"
              % (sum(tempi) / len(tempi), min(tempi), max(tempi)))
        print("somma dei tempi di generazione      : %.1f h" % (sum(tempi) / 3600))

    print("\n--- rapporto scritto dal runner (per confronto) ---")
    for r in righe(d / "rapporto_run.jsonl"):
        print("  %s: fatte %s/%s, %.1f min, medi %.1fs"
              % (r.get("passata"), r.get("fatte"), r.get("totali"),
                 r.get("minuti", 0), r.get("secondi_medi") or 0))

    print("\nESITO: %s" % ("INTEGRO" if esito_ok else "PROBLEMI, vedi sopra"))
    return 0 if esito_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
