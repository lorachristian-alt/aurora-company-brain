# -*- coding: utf-8 -*-
"""conta_stato — il blocco standard dei conteggi del vault, da incollare VERBATIM.

Nasce al gate del lotto 1B, come fix di PROCESSO: in due lotti su due i totali
ricomposti a mano in prosa sono usciti sbagliati — «46 note di contenuto» contro
32 nel rapporto 1A, e «105 note, 88 di contenuto» nello stato quando `qa_all.py`
ne contava 106 e 89. Nessuno dei due era un errore di canonizzazione: erano due
sottrazioni fatte a mano su numeri veri.

**Da qui in poi lo stato e i rapporti di lotto incollano questo blocco cosi' com'e'**,
e non ricompongono piu' i totali in prosa. Se un numero non e' qui dentro, o lo
produce un altro script, oppure non si dichiara.

Regola d'oro 5, applicata a se stessa: anche i conteggi del vault sono un numero, e
un numero non si dichiara senza che uno script l'abbia contato.

Uso:
    python conta_stato.py                 # blocco markdown sullo standard output
    python conta_stato.py --vault <path>  # su un vault diverso da quello di default
"""
import argparse, os, sys
from datetime import date

import qa_comune as Q


def conta(vault):
    note = list(Q.tutte_le_note(vault))
    per_cartella, per_type = {}, {}
    strumento = diario = index = 0
    for n in note:
        per_cartella[n.cartella] = per_cartella.get(n.cartella, 0) + 1
        per_type[n.type or "?"] = per_type.get(n.type or "?", 0) + 1
        if n.type == "index":
            index += 1
        elif Q.e_nota_strumento(n):
            strumento += 1
        elif n.type in ("sessione", "daily"):
            diario += 1

    sources = os.path.join(vault, "sources")
    grezzi = sorted(f for f in os.listdir(sources)
                    if os.path.isfile(os.path.join(sources, f)) and not f.lower().endswith(".md"))
    citati = set()
    for n in note:
        for f in n.fonti:
            if f:
                citati.add(str(f))
    citati &= set(grezzi)

    aperte = sum(1 for n in note if n.type == "conflitto")
    return {
        "note": len(note), "index": index, "strumento": strumento, "diario": diario,
        "contenuto": len(note) - index - strumento - diario,
        "per_cartella": per_cartella, "per_type": per_type,
        "grezzi": len(grezzi), "citati": len(citati), "restanti": len(grezzi) - len(citati),
        "aperte": aperte,
    }


def riga(d, chiave, sep=" · "):
    return sep.join("%s %d" % (k, v) for k, v in sorted(d[chiave].items(), key=lambda x: -x[1]))


def main():
    ap = argparse.ArgumentParser(description="Il blocco standard dei conteggi del vault.")
    ap.add_argument("--vault", default=Q.VAULT)
    a = ap.parse_args()
    d = conta(a.vault)

    print("<!-- CONTEGGI DEL VAULT — generati da `06_operativo\\qa\\conta_stato.py` il %s."
          % date.today().isoformat())
    print("     Si incollano VERBATIM: non si ricompongono a mano, non si riscrivono in prosa. -->")
    print("")
    print("| Grandezza | Valore |")
    print("|---|---|")
    print("| Note nel vault | **%d** |" % d["note"])
    print("| di cui `_index` | %d |" % d["index"])
    print("| di cui note-strumento del progetto | %d |" % d["strumento"])
    print("| di cui note di diario (`sessione`, `daily`) | %d |" % d["diario"])
    print("| **di cui note di contenuto** | **%d** |" % d["contenuto"])
    print("| Note per cartella | %s |" % riga(d, "per_cartella"))
    print("| Note per `type` | %s |" % riga(d, "per_type"))
    print("| Questioni aperte (`type: conflitto`) | %d |" % d["aperte"])
    print("| Grezzi in `sources\\` | %d |" % d["grezzi"])
    print("| Grezzi citati da almeno una nota | **%d** |" % d["citati"])
    print("| Grezzi restanti | **%d** |" % d["restanti"])
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
