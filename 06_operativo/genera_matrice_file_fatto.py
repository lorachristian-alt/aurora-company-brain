# -*- coding: utf-8 -*-
"""genera_matrice_file_fatto — la mappatura (file x fatto) di metodo_03 §9.3.

Una riga per **coppia grezzo-nota**: un grezzo che alimenta tre note ha tre righe.
Colonne: `file` · `fatto` · `cartella_prevista` · `nota_padrona_prevista` · `lotto` ·
`stato`, come prescritto dal manuale.

⚠️ Non si compila a mano e non si compila in blocco per tutti i 160 grezzi: si
rigenera **lotto per lotto** alla chiusura di ciascuno, leggendo le note che
esistono davvero. Le righe degli altri lotti restano dov'erano: questo script
sostituisce solo quelle del lotto che gli si passa.

Il campo `fatto` non e' inventato dallo script: e' il `summary` della nota, che e'
gia' per costruzione l'enunciato del fatto (metodo_03 §2.1). Il campo `stato` vale
`fatta` per ogni riga che nasce da una nota esistente.

Uso:
    python genera_matrice_file_fatto.py --lotto 1a --elenco qa/lotti/lotto_01a_linea1_turno_ccp.txt
    python genera_matrice_file_fatto.py --controlla        # solo diagnostica
"""
import argparse, csv, io, os, sys

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(QUI, "qa"))
import qa_comune as Q

CSV = os.path.join(QUI, "matrice_corpus_v1.csv")
COLONNE = ["file", "fatto", "cartella_prevista", "nota_padrona_prevista", "lotto", "stato"]


def leggi_elenco(percorso):
    if not os.path.isabs(percorso) and not os.path.isfile(percorso):
        percorso = os.path.join(QUI, percorso)
    return [r.strip() for r in io.open(percorso, encoding="utf-8")
            if r.strip() and not r.strip().startswith("#")]


def righe_esistenti():
    if not os.path.isfile(CSV):
        return []
    with io.open(CSV, encoding="utf-8", newline="") as f:
        return [r for r in csv.DictReader(f, delimiter=";")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lotto")
    ap.add_argument("--elenco")
    ap.add_argument("--controlla", action="store_true")
    args = ap.parse_args()

    vecchie = righe_esistenti()
    if args.controlla or not args.lotto:
        per_lotto = {}
        for r in vecchie:
            per_lotto[r["lotto"]] = per_lotto.get(r["lotto"], 0) + 1
        print("righe totali nel CSV: %d" % len(vecchie))
        for k in sorted(per_lotto):
            print("   lotto %-6s %4d righe · %3d grezzi distinti"
                  % (k, per_lotto[k], len({r["file"] for r in vecchie if r["lotto"] == k})))
        return

    grezzi = set(leggi_elenco(args.elenco))
    note = Q.tutte_le_note()
    nuove = []
    for n in sorted(note, key=lambda x: (x.cartella, x.slug)):
        for f in n.fonti:
            f = str(f)
            if f not in grezzi:
                continue
            nuove.append({
                "file": f,
                "fatto": (n.fm or {}).get("summary", "").strip(),
                "cartella_prevista": n.cartella,
                "nota_padrona_prevista": n.slug,
                "lotto": args.lotto,
                "stato": "fatta",
            })

    # i grezzi del lotto che nessuna nota cita: riga con stato esplicito
    citati = {r["file"] for r in nuove}
    for g in sorted(grezzi - citati):
        nuove.append({"file": g, "fatto": "", "cartella_prevista": "",
                      "nota_padrona_prevista": "", "lotto": args.lotto,
                      "stato": "da fare"})

    tenute = [r for r in vecchie if r["lotto"] != args.lotto]
    tutte = tenute + nuove
    with io.open(CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLONNE, delimiter=";")
        w.writeheader()
        for r in tutte:
            w.writerow(r)

    print("lotto %s: %d righe (%d grezzi, %d note distinte)"
          % (args.lotto, len(nuove), len(citati),
             len({r["nota_padrona_prevista"] for r in nuove if r["nota_padrona_prevista"]})))
    print("righe conservate dagli altri lotti: %d" % len(tenute))
    print("CSV: %s — %d righe in tutto" % (CSV, len(tutte)))
    scoperti = sorted(grezzi - citati)
    if scoperti:
        print("⚠ grezzi del lotto senza nessuna nota:")
        for g in scoperti:
            print("   ", g)


if __name__ == "__main__":
    main()
