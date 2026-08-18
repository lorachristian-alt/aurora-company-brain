# -*- coding: utf-8 -*-
"""
metriche_abc.py — le quattro metriche di P4 (metodo_02) per A, B e C, ricontate.

⚠️ Il «tasso di allucinazione» NON e' omogeneo fra le tre misure, e lo script lo dice
invece di nasconderlo. P4 lo definisce come percentuale di esiti `allucinata` sulle sole
`non_rispondibile`. Nella valutazione A/B del 14/08 il campo `allucinata` non fu mai
usato (zero righe su 564) e il giudice di allora ripiego' su `sbagliata`; nella misura C
il campo e' usato davvero. Qui si calcolano ENTRAMBE le definizioni per tutte e tre.

Uso:  python metriche_abc.py
"""
import collections, json
from pathlib import Path

BASE = Path(__file__).resolve().parent
EVAL = BASE.parent / "03_valutazione" / "eval_set.jsonl"

def righe(p):
    return [json.loads(r) for r in Path(p).read_text(encoding="utf-8").splitlines() if r.strip()]

tipi = {v["id"]: v["tipo"] for v in righe(EVAL) if "tipo" in v}   # solo id -> tipo
voci = righe(BASE / "baseline_2026-08-14_grezzo" / "valutazione.jsonl") + \
       righe(BASE / "baseline_c_2026-08-17_grezzo" / "valutazione_c.jsonl")
mis = collections.defaultdict(dict)
for v in voci:
    mis[v["misura"]][v["id"]] = v

def q(d, tipo=None, esito=None):
    s = [v for i, v in d.items() if tipo is None or tipi.get(i) == tipo]
    if esito is None:
        return len(s)
    return sum(1 for v in s if v["esito"] == esito)

print("%-46s %8s %8s %8s" % ("", "A", "B", "C"))
def riga(et, f):
    print("%-46s %8s %8s %8s" % (et, f("A"), f("B"), f("C")))

def pc(n, d):
    return "-" if not d else "%.1f%%" % (100.0 * n / d)

riga("1a. allucinate su non_rispondibile (P4 lettera)",
     lambda m: pc(q(mis[m], "non_rispondibile", "allucinata"), q(mis[m], "non_rispondibile")))
riga("1b. sbagliate su non_rispondibile (ripiego 14/08)",
     lambda m: pc(q(mis[m], "non_rispondibile", "sbagliata"), q(mis[m], "non_rispondibile")))
riga("1c. allucinate+sbagliate su non_rispondibile",
     lambda m: pc(q(mis[m], "non_rispondibile", "allucinata") + q(mis[m], "non_rispondibile", "sbagliata"),
                  q(mis[m], "non_rispondibile")))
riga("2. conflitti riconosciuti (corrette/contraddizione)",
     lambda m: pc(q(mis[m], "contraddizione", "corretta"), q(mis[m], "contraddizione")))
riga("3a. lookup corrette",
     lambda m: pc(q(mis[m], "lookup", "corretta"), q(mis[m], "lookup")))
riga("3b. multi_hop corrette",
     lambda m: pc(q(mis[m], "multi_hop", "corretta"), q(mis[m], "multi_hop")))
riga("3c. divario lookup - multi_hop (punti)",
     lambda m: "%.1f" % (100.0*q(mis[m],"lookup","corretta")/q(mis[m],"lookup")
                         - 100.0*q(mis[m],"multi_hop","corretta")/q(mis[m],"multi_hop")))
riga("4. fonti corrette",
     lambda m: pc(sum(1 for v in mis[m].values() if v.get("fonti_corrette") is True), len(mis[m])))
print()
riga("corrette, TUTTE le 282",
     lambda m: pc(q(mis[m], None, "corretta"), q(mis[m])))
riga("corrette, SOLO le 251 rispondibili",
     lambda m: pc(sum(1 for i, v in mis[m].items() if tipi.get(i) != "non_rispondibile" and v["esito"] == "corretta"),
                  sum(1 for i in mis[m] if tipi.get(i) != "non_rispondibile")))
riga("corrette+parziali, tutte",
     lambda m: pc(q(mis[m], None, "corretta") + q(mis[m], None, "parziale"), q(mis[m])))
print()
print("righe README (allucinazione con la definizione 1a, alla lettera di P4):")
for m in ("A", "B", "C"):
    d = mis[m]
    print("| %s | %s | %s | %s | %s | %s | %s |" % (
        m, "14/08/2026" if m in "AB" else "17/08/2026",
        pc(q(d, "non_rispondibile", "allucinata"), q(d, "non_rispondibile")),
        pc(q(d, "contraddizione", "corretta"), q(d, "contraddizione")),
        pc(q(d, "lookup", "corretta"), q(d, "lookup")),
        pc(q(d, "multi_hop", "corretta"), q(d, "multi_hop")),
        pc(sum(1 for v in d.values() if v.get("fonti_corrette") is True), len(d))))
