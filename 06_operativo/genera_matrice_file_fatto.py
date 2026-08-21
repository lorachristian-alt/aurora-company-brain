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
import argparse, csv, datetime, io, os, sys

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


# ⚠️ E44 — IL CSV ENTRA NELLE MISURE DI CHIUSURA, E LE SUE GUARDIE SONO DUE.
# Il 21/08/2026 questo script e' andato in errore A META' SCRITTURA e ha lasciato il file
# a 184 righe delle 293 che aveva: tre righe portavano SETTE campi invece di sei, per un
# punto e virgola non protetto dentro il campo `fatto`. Il danno era reversibile perche' il
# file sta in git; la prossima volta potrebbe non esserlo.
#
# ⚠️ E il difetto era VISIBILE da un lotto: nel censimento quelle tre righe comparivano
# come tre lotti fantasma col nome di una nota, perche' lo slittamento dei campi spostava
# la nota nella colonna del lotto. **Nessuno le aveva guardate.**
#
# Le due guardie, e la prima conta piu' della seconda:
#   1. IN SCRITTURA si rifiuta la riga malformata PRIMA di aprire il file. Un campo che
#      contiene il separatore, un ritorno a capo o una virgoletta e' un campo che va
#      protetto: `csv` lo fa da se', ma solo se il valore passa da qui. Se una riga non
#      supera il controllo, NON si scrive niente: meglio un file vecchio e integro che uno
#      nuovo e mezzo.
#   2. IN LETTURA una riga con campi in piu' non si ingoia in silenzio: si dice.
def righe_esistenti():
    if not os.path.isfile(CSV):
        return []
    with io.open(CSV, encoding="utf-8", newline="") as f:
        righe, malformate = [], []
        for i, r in enumerate(csv.DictReader(f, delimiter=";"), start=2):
            if None in r or any(v is None for v in r.values()):
                malformate.append(i)
            righe.append(r)
    if malformate:
        print("⚠ ATTENZIONE: %d righe del CSV hanno un numero di campi sbagliato "
              "(righe %s). Non si riscrive finche' non sono riparate."
              % (len(malformate), ", ".join(str(i) for i in malformate[:10])))
        raise SystemExit(2)
    return righe


def controlla_riga(r, dove):
    """Nessun campo puo' contenere il separatore, un a capo o una virgoletta nuda."""
    guasti = []
    for col in COLONNE:
        v = "" if r.get(col) is None else str(r[col])
        for cattivo, nome in ((";", "separatore"), ("\n", "a capo"),
                              ("\r", "ritorno carrello"), ('"', "virgoletta")):
            if cattivo in v:
                guasti.append("%s: il campo `%s` contiene un %s" % (dove, col, nome))
    return guasti


def conta_campi(percorso):
    """Righe e campi per riga, letti a mano dal file scritto. E' la misura di chiusura."""
    with io.open(percorso, encoding="utf-8", newline="") as f:
        lette = list(csv.reader(f, delimiter=";"))
    distinti = sorted({len(r) for r in lette})
    return len(lette) - 1, distinti


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
        n, campi = conta_campi(CSV)
        print("righe totali nel CSV: %d" % len(vecchie))
        print("MISURA DI CHIUSURA (E44), %s: %d righe di dati, campi per riga: %s"
              % (datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), n,
                 " / ".join(str(c) for c in campi)))
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

    # ⚠️ guardia 1: si controlla PRIMA di aprire il file in scrittura
    guasti = []
    for i, r in enumerate(tutte, start=1):
        guasti += controlla_riga(r, "riga %d" % i)
    if guasti:
        print("SCRITTURA RIFIUTATA: %d campi non protetti." % len(guasti))
        for g in guasti[:10]:
            print("   ", g)
        print("Il CSV NON e' stato toccato: resta quello di prima, integro.")
        raise SystemExit(2)

    with io.open(CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLONNE, delimiter=";")
        w.writeheader()
        for r in tutte:
            w.writerow(r)

    print("lotto %s: %d righe (%d grezzi, %d note distinte)"
          % (args.lotto, len(nuove), len(citati),
             len({r["nota_padrona_prevista"] for r in nuove if r["nota_padrona_prevista"]})))
    print("righe conservate dagli altri lotti: %d" % len(tenute))
    n, campi = conta_campi(CSV)
    print("CSV: %s — %d righe in tutto" % (CSV, len(tutte)))
    print("MISURA DI CHIUSURA (E44), %s: %d righe di dati, campi per riga: %s"
          % (datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), n,
             " / ".join(str(c) for c in campi)))
    if campi != [len(COLONNE)]:
        print("⚠ ATTENZIONE: non tutte le righe hanno %d campi." % len(COLONNE))
    scoperti = sorted(grezzi - citati)
    if scoperti:
        print("⚠ grezzi del lotto senza nessuna nota:")
        for g in scoperti:
            print("   ", g)


if __name__ == "__main__":
    main()
