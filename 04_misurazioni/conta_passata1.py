# -*- coding: utf-8 -*-
"""
conta_passata1.py — riconta l'esito della passata 1 (retrieval) della baseline C.

Regola d'oro 5: nessun numero dichiarato senza uno script che l'ha ricontato. Questo
legge il file dei contesti e le tracce, e riporta soltanto conteggi: non apre le
risposte attese, non giudica, non stampa il testo delle domande.

Uso:
    python conta_passata1.py [--cartella baseline_c_2026-08-17_grezzo]
"""

import argparse
import collections
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cartella", default="baseline_c_2026-08-17_grezzo")
    a = ap.parse_args()
    d = BASE / a.cartella

    ctx = [json.loads(r) for r in
           (d / "contesti_c.jsonl").read_text(encoding="utf-8").splitlines() if r.strip()]
    tracce = sorted((d / "tracce").glob("*.json"))

    print("righe in contesti_c.jsonl : %d" % len(ctx))
    print("id distinti               : %d" % len({c["id"] for c in ctx}))
    print("file di traccia           : %d" % len(tracce))
    err = d / "errori_runner.jsonl"
    print("errori del runner         : %s"
          % ("nessuno" if not err.exists()
             else "%d righe" % len(err.read_text(encoding="utf-8").splitlines())))

    npass = [len(c["passaggi"]) for c in ctx]
    print("passaggi per domanda      : min %d, max %d (attesi %d)"
          % (min(npass), max(npass), 4))
    car = [c["caratteri_contesto"] for c in ctx]
    print("caratteri di contesto     : min %d, medio %d, max %d"
          % (min(car), sum(car) // len(car), max(car)))

    ocr = sum(1 for c in ctx if any(p["origine"] == "ocr" for p in c["passaggi"]))
    sch = sum(1 for c in ctx if any(p["origine"] == "scheda" for p in c["passaggi"]))
    print("domande con un chunk OCR  : %d" % ocr)
    print("domande con una scheda    : %d" % sch)

    f = collections.Counter(p["file"].rsplit(".", 1)[-1].lower()
                            for c in ctx for p in c["passaggi"])
    print("\nformati nei passaggi consegnati (%d passaggi in tutto):" % sum(f.values()))
    for k, v in f.most_common():
        print("   %-5s %4d" % (k, v))

    doc = collections.Counter(p["file"] for c in ctx for p in c["passaggi"])
    print("\nfile distinti che compaiono almeno una volta: %d su 160" % len(doc))
    print("i dieci piu' recuperati:")
    for k, v in doc.most_common(10):
        print("   %4d  %s" % (v, k))

    # quanto pesa ciascun ramo nella selezione finale: si legge dalle tracce
    solo_d = solo_s = entrambi = 0
    for t in tracce:
        tr = json.loads(t.read_text(encoding="utf-8"))
        finali = {p["cid"] for p in tr["passaggi_consegnati"]}
        for x in tr["fusione_rrf"]:
            if x["cid"] not in finali:
                continue
            if x["rango_denso"] is not None and x["rango_sparso"] is not None:
                entrambi += 1
            elif x["rango_denso"] is not None:
                solo_d += 1
            else:
                solo_s += 1
    tot = solo_d + solo_s + entrambi
    print("\nda quale ramo vengono i passaggi consegnati (%d):" % tot)
    print("   solo denso   %4d  (%.1f%%)" % (solo_d, 100.0 * solo_d / tot))
    print("   solo sparso  %4d  (%.1f%%)" % (solo_s, 100.0 * solo_s / tot))
    print("   da entrambi  %4d  (%.1f%%)" % (entrambi, 100.0 * entrambi / tot))


if __name__ == "__main__":
    main()
