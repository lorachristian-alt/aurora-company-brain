# -*- coding: utf-8 -*-
"""
conta_esiti_abc.py — riconta A, B e C sugli stessi id. Nessun numero a mano.

Regola d'oro 5: nessun numero dichiarato senza uno script che l'ha ricontato. Questo e'
quello script per la tabella del verbale e del README.

Legge:
  baseline_2026-08-14_grezzo\\valutazione.jsonl      (misure A e B, 564 righe)
  baseline_c_<data>_grezzo\\valutazione_c.jsonl      (misura C)
  baseline_c_<data>_grezzo\\misuraC_risposte.jsonl   (per i buchi del runner)

⚠️ PERIMETRO. Con `--tipi` legge anche `03_valutazione\\eval_set.jsonl`, e ne estrae
SOLO la coppia id→tipo: nessuna risposta attesa viene letta, stampata o salvata. Si lancia
**dopo** che il run e' concluso e la configurazione e' congelata e committata: a quel
punto non esiste piu' niente che quella lettura possa influenzare. Prima del run, non si
lancia con questa opzione.

Uso:
    python conta_esiti_abc.py
    python conta_esiti_abc.py --tipi
    python conta_esiti_abc.py --json
"""

import argparse
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
RADICE = BASE.parent
BASELINE_AB = BASE / "baseline_2026-08-14_grezzo" / "valutazione.jsonl"
EVAL_SET = RADICE / "03_valutazione" / "eval_set.jsonl"
ESITI = ("corretta", "parziale", "sbagliata", "allucinata")


def righe(percorso):
    out = []
    if not Path(percorso).exists():
        return out
    with open(percorso, encoding="utf-8") as f:
        for r in f:
            r = r.strip()
            if r:
                try:
                    out.append(json.loads(r))
                except json.JSONDecodeError:
                    pass
    return out


def per_misura(voci):
    """Ultima riga per (misura, id): se una voce e' stata rigiudicata, vince l'ultima."""
    d = {}
    for v in voci:
        d[(v.get("misura"), v.get("id"))] = v
    fuori = {}
    for (m, i), v in d.items():
        fuori.setdefault(m, {})[i] = v
    return fuori


def conta(voci_per_id, ids=None):
    ids = set(ids) if ids else set(voci_per_id)
    sel = [v for i, v in voci_per_id.items() if i in ids]
    c = {e: sum(1 for v in sel if v.get("esito") == e) for e in ESITI}
    c["totale"] = len(sel)
    c["fonti_corrette"] = sum(1 for v in sel if v.get("fonti_corrette") is True)
    return c


def pct(n, tot):
    return (100.0 * n / tot) if tot else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cartella-c", default="baseline_c_2026-08-17_grezzo")
    ap.add_argument("--tipi", action="store_true",
                    help="aggiunge la ripartizione per tipo (legge SOLO id->tipo)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    cart_c = BASE / a.cartella_c
    voci = righe(BASELINE_AB) + righe(cart_c / "valutazione_c.jsonl")
    mis = per_misura(voci)
    if not mis:
        sys.exit("nessuna valutazione trovata: controlla i percorsi")

    # id comuni a tutte le misure presenti: la tabella si fa sugli STESSI id, sempre
    presenti = [m for m in ("A", "B", "C") if m in mis]
    comuni = set.intersection(*[set(mis[m]) for m in presenti]) if presenti else set()

    risultato = {"misure_presenti": presenti, "id_comuni": len(comuni), "totali": {},
                 "su_id_comuni": {}}
    for m in presenti:
        risultato["totali"][m] = conta(mis[m])
        risultato["su_id_comuni"][m] = conta(mis[m], comuni)

    # buchi del runner: id attesi ma senza riga di risposta o senza riga di giudizio
    risposte = {r["id"] for r in righe(cart_c / "misuraC_risposte.jsonl")}
    if risposte:
        risultato["misuraC"] = {
            "righe_risposte": len(risposte),
            "id_giudicati": len(mis.get("C", {})),
            "risposte_senza_giudizio": sorted(risposte - set(mis.get("C", {}))),
            "giudizi_senza_risposta": sorted(set(mis.get("C", {})) - risposte),
        }

    if a.tipi:
        tipi = {}
        for r in righe(EVAL_SET):
            if "id" in r and "tipo" in r:
                tipi[r["id"]] = r["tipo"]        # solo questi due campi, niente altro
        risultato["per_tipo"] = {}
        for m in presenti:
            d = {}
            for i, v in mis[m].items():
                t = tipi.get(i, "?")
                d.setdefault(t, {e: 0 for e in ESITI})
                d[t][v.get("esito", "?")] = d[t].get(v.get("esito", "?"), 0) + 1
            risultato["per_tipo"][m] = {k: d[k] for k in sorted(d)}

    if a.json:
        print(json.dumps(risultato, ensure_ascii=False, indent=1))
        return

    print("id comuni alle misure %s: %d\n" % ("/".join(presenti), len(comuni)))
    print("%-16s %s" % ("", "  ".join("%13s" % m for m in presenti)))
    for e in ESITI:
        print("%-16s %s" % (e, "  ".join(
            "%5d (%4.1f%%)" % (risultato["su_id_comuni"][m][e],
                               pct(risultato["su_id_comuni"][m][e],
                                   risultato["su_id_comuni"][m]["totale"]))
            for m in presenti)))
    print("%-16s %s" % ("fonti corrette", "  ".join(
        "%5d (%4.1f%%)" % (risultato["su_id_comuni"][m]["fonti_corrette"],
                           pct(risultato["su_id_comuni"][m]["fonti_corrette"],
                               risultato["su_id_comuni"][m]["totale"]))
        for m in presenti)))
    print("%-16s %s" % ("totale", "  ".join(
        "%13d" % risultato["su_id_comuni"][m]["totale"] for m in presenti)))

    if "misuraC" in risultato:
        c = risultato["misuraC"]
        print("\nmisura C: %d risposte, %d giudizi" % (c["righe_risposte"],
                                                       c["id_giudicati"]))
        for k in ("risposte_senza_giudizio", "giudizi_senza_risposta"):
            if c[k]:
                print("  %s (%d): %s" % (k, len(c[k]), ", ".join(c[k][:20])))

    if a.tipi:
        print("\nper tipo (corrette/parziali/sbagliate/allucinate)")
        tutti = sorted({t for m in presenti for t in risultato["per_tipo"][m]})
        print("%-18s %s" % ("", "  ".join("%18s" % m for m in presenti)))
        for t in tutti:
            celle = []
            for m in presenti:
                d = risultato["per_tipo"][m].get(t, {e: 0 for e in ESITI})
                celle.append("%18s" % ("%d / %d / %d / %d" % (d["corretta"], d["parziale"],
                                                             d["sbagliata"],
                                                             d["allucinata"])))
            print("%-18s %s" % (t, "  ".join(celle)))


if __name__ == "__main__":
    main()
