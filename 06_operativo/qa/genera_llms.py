# -*- coding: utf-8 -*-
"""genera_llms — rigenera `aurora-cervello\\llms.txt` dal frontmatter delle note.

metodo_03 §8.1. E' l'unico derivato che vive DENTRO il vault, perche' serve alla
navigazione ed e' parte del sistema misurato. Un derivato si rigenera, non si
modifica: se una riga e' brutta, si riscrive il `summary` della nota e si rilancia.

Il testo di ogni riga e' il `summary` della nota, copiato senza riscriverlo.

Uso:
    python genera_llms.py            # scrive il file
    python genera_llms.py --stdout   # lo stampa soltanto (serve alla QA)
"""
import argparse, io, os, sys

import qa_comune as Q

INTESTAZIONE = (
    "# aurora-cervello — il cervello aziendale di Aurora Food Group S.r.l.\n"
    "# Mappa generata dal frontmatter delle note: undici cartelle, una porta `_index` "
    "per ciascuna, gli hub dei temi e le questioni che l'archivio lascia aperte.\n"
)


def componi(vault=Q.VAULT):
    note = Q.tutte_le_note(vault)
    r = [INTESTAZIONE]

    r.append("## Le porte delle cartelle\n")
    for c in Q.CARTELLE:
        for n in note:
            if n.cartella == c and n.type == "index":
                r.append("- [%s](%s/%s): %s" % (n.slug, c, n.nome, _sum(n)))
    r.append("")

    r.append("## Gli hub dei temi\n")
    for c in Q.CARTELLE:
        hub = sorted([n for n in note if n.cartella == c and n.type == "hub"],
                     key=lambda x: x.slug)
        if not hub:
            continue
        r.append("### %s" % c)
        for n in hub:
            r.append("- [%s](%s/%s): %s" % (n.slug, c, n.nome, _sum(n)))
        r.append("")

    aperte = sorted([n for n in note if n.type == "conflitto"], key=lambda x: x.slug)
    r.append("## Le questioni che l'archivio non chiude\n")
    if aperte:
        for n in aperte:
            r.append("- [%s](%s/%s): %s" % (n.slug, n.cartella, n.nome, _sum(n)))
    else:
        r.append("*(nessuna questione aperta registrata)*")
    r.append("")
    return "\n".join(r)


def _sum(n):
    return str((n.fm or {}).get("summary") or "").strip()


def main():
    ap = argparse.ArgumentParser(description="Rigenera llms.txt dal frontmatter.")
    ap.add_argument("--vault", default=Q.VAULT)
    ap.add_argument("--stdout", action="store_true")
    args = ap.parse_args()
    testo = componi(args.vault)
    if args.stdout:
        sys.stdout.write(testo)
        return
    p = os.path.join(args.vault, "llms.txt")
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(testo)
    print("llms.txt rigenerato: %s (%d righe)" % (p, testo.count("\n")))


if __name__ == "__main__":
    main()
