# -*- coding: utf-8 -*-
"""conta_fumo — riconta gli esiti della mini-misura di fumo e li confronta con la baseline A.

I numeri della fumo NON sono ufficiali e non entrano nel README, ma la regola d'oro 5
non fa eccezioni: nessun numero si dichiara senza che uno script l'abbia ricontato.
Questo script legge i due `.jsonl` e stampa i conteggi, il confronto sugli STESSI id e
l'elenco di migliorati e peggiorati.

Uso:
    python conta_fumo.py
"""
import argparse, collections, io, json, os, sys

QUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(QUI))
FUMO = os.path.join(REPO, "04_misurazioni", "fumo_s2_2026-08-16")
BASE = os.path.join(REPO, "04_misurazioni", "baseline_2026-08-14_grezzo")

ESITI = ["corretta", "parziale", "sbagliata", "allucinata"]
# scala di merito, per dire cosa e' «migliorato» e cosa «peggiorato»
RANGO = {"allucinata": 0, "sbagliata": 1, "parziale": 2, "corretta": 3}


def carica(percorso, filtro_misura=None):
    voci = {}
    for riga in io.open(percorso, encoding="utf-8"):
        riga = riga.strip()
        if not riga:
            continue
        v = json.loads(riga)
        if filtro_misura and str(v.get("misura", "")).upper() != filtro_misura.upper():
            continue
        voci[str(v["id"])] = v
    return voci


def tabella(nome, voci):
    c = collections.Counter(v["esito"] for v in voci.values())
    tot = sum(c.values())
    print("\n%s — %d voci" % (nome, tot))
    for e in ESITI:
        n = c.get(e, 0)
        pct = (100.0 * n / tot) if tot else 0.0
        print("  %-11s %3d  %5.1f%%" % (e, n, pct))
    fc = sum(1 for v in voci.values() if v.get("fonti_corrette") is True)
    print("  %-11s %3d/%d" % ("fonti ok", fc, tot))
    return c, tot, fc


def main():
    ap = argparse.ArgumentParser(description="Riconta la misura di fumo e la confronta con la baseline A.")
    ap.add_argument("--fumo", default=os.path.join(FUMO, "fumo_valutazione.jsonl"))
    ap.add_argument("--risposte", default=os.path.join(FUMO, "fumo_risposte.jsonl"))
    ap.add_argument("--baseline", default=os.path.join(BASE, "valutazione.jsonl"))
    args = ap.parse_args()

    fumo = carica(args.fumo)
    risposte = carica(args.risposte)

    print("=" * 62)
    print("MINI-MISURA DI FUMO — Sessione 2, fetta pilota L26130")
    print("NUMERI NON UFFICIALI: non entrano nel README e non sostituiscono la misura «dopo».")
    print("=" * 62)
    print("\nrisposte prodotte: %d | voci valutate: %d" % (len(risposte), len(fumo)))
    mancanti = set(risposte) - set(fumo)
    sovrapiu = set(fumo) - set(risposte)
    if mancanti:
        print("⚠️ risposte senza valutazione: %s" % ", ".join(sorted(mancanti)))
    if sovrapiu:
        print("⚠️ valutazioni senza risposta: %s" % ", ".join(sorted(sovrapiu)))

    cf, totf, fcf = tabella("FUMO (vault canonizzato)", fumo)

    # --- baseline A sugli STESSI id ------------------------------------------
    baseA = carica(args.baseline, filtro_misura="A")
    comuni = sorted(set(fumo) & set(baseA))
    assenti = sorted(set(fumo) - set(baseA))
    print("\nid della fumo presenti anche nella baseline A: %d su %d" % (len(comuni), len(fumo)))
    if assenti:
        print("  esclusi dal confronto (assenti in baseline A): %s" % ", ".join(assenti))

    sotto = {i: baseA[i] for i in comuni}
    cb, totb, fcb = tabella("BASELINE A (corpus grezzo), stessi id", sotto)

    print("\n" + "-" * 62)
    print("CONFRONTO sugli stessi %d id" % len(comuni))
    print("-" * 62)
    print("  %-11s %>8s %>8s %>8s".replace(">", "") % ("esito", "fumo", "baseA", "delta"))
    for e in ESITI:
        a, b = cf.get(e, 0), cb.get(e, 0)
        print("  %-11s %8d %8d %+8d" % (e, a, b, a - b))
    print("  %-11s %8d %8d %+8d" % ("fonti ok", fcf, fcb, fcf - fcb))

    migliorati, peggiorati, invariati = [], [], []
    for i in comuni:
        a, b = fumo[i]["esito"], baseA[i]["esito"]
        if RANGO[a] > RANGO[b]:
            migliorati.append((i, b, a))
        elif RANGO[a] < RANGO[b]:
            peggiorati.append((i, b, a))
        else:
            invariati.append(i)

    print("\nmigliorati: %d | peggiorati: %d | invariati: %d"
          % (len(migliorati), len(peggiorati), len(invariati)))
    for etichetta, elenco in (("MIGLIORATI", migliorati), ("PEGGIORATI", peggiorati)):
        if not elenco:
            continue
        print("\n%s" % etichetta)
        for i, b, a in elenco:
            print("  %-6s %-10s -> %-10s | %s" % (i, b, a, fumo[i]["motivazione"][:88]))

    print("\n" + "=" * 62)
    print("Su %d domande la differenza di due o tre esiti non e' significativa:" % len(comuni))
    print("questo campione dice se il design regge, non quanto rende.")
    print("=" * 62)


if __name__ == "__main__":
    main()
