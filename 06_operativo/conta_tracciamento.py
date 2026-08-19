# -*- coding: utf-8 -*-
"""conta_tracciamento — le righe della tabella di tracciamento, contate da script.

`matrice_lotti_corpus_v1.md` §«La tabella di tracciamento viva» e' la prova con cui, al
gate finale, si dichiarano i conflitti chiusi, aperti dichiarati, riconciliati e ancora
tracciati. Fino al 19/08/2026 il numero delle sue righe era **l'ultimo numero del progetto
dichiarato senza script**, e come tutti quelli prima di lui e' gia' uscito sbagliato una
volta: lo stato dichiarava «41 righe» quando erano 54.

Da qui in poi il numero delle righe non si legge piu' a occhio: si incolla da qui, nello
stato e nei rapporti di lotto, come si fa col blocco di `conta_stato.py`.

Controlla, e sono controlli non conteggi:
  1. la numerazione e' continua da T1 e senza buchi ne' doppioni. L'ORDINE FISICO NON
     CONTA (§4.26: i numeri sono permanenti, l'ordine e' di servizio) - T34 sta in fondo
     alla tabella e va benissimo cosi';
  2. ogni riga ha esattamente cinque celle: una riga con un `|` di troppo dentro il testo
     sposta silenziosamente la colonna dello stato, e lo stato e' proprio cio' che si conta;
  3. ogni riga esce con UNO dei quattro esiti previsti. Una riga senza esito riconoscibile
     e' un errore, non un valore mancante: al gate finale sarebbe un conflitto che non
     risulta ne' chiuso ne' aperto.

⚠️ L'esito si legge nella SOLA quinta cella. La quarta - «Gamba mancante attesa in» -
contiene formule come «chiusa in **1A**», che parlano del lotto in cui la gamba e' arrivata
e non dell'esito della questione: leggere la riga intera farebbe contare due volte.

Uso:
    python conta_tracciamento.py                  # blocco markdown sullo standard output
    python conta_tracciamento.py --matrice <path>

Esce 0 se la tabella e' integra, 1 altrimenti.
"""
import argparse, io, os, re, sys
from datetime import date

QUI = os.path.dirname(os.path.abspath(__file__))
MATRICE = os.path.join(QUI, "matrice_lotti_corpus_v1.md")

# I quattro esiti, nell'ordine in cui si provano. L'ordine e' sostanziale: lo stato di una
# riga riconciliata racconta spesso anche come e' stata chiusa, e quello di una chiusa cita
# la questione che ha aperto. Vince il piu' specifico, che si prova per primo.
ESITI = [
    ("riconciliata",     r"\briconciliat[ao]\b"),
    ("aperta dichiarata", r"\baperta dichiarata\b"),
    ("chiusa",           r"\bchiusa\b"),
    ("tracciata",        r"\btracciata\b"),
]


def righe_della_tabella(testo):
    """Le righe `| T<n> | ... |` della tabella di tracciamento, con le loro celle."""
    fuori = []
    for numero_riga, riga in enumerate(testo.split("\n"), 1):
        s = riga.strip()
        if not re.match(r"^\|\s*T\d+\s*\|", s):
            continue
        celle = [c.strip() for c in s.strip("|").split("|")]
        n = int(re.match(r"^T(\d+)$", celle[0]).group(1))
        fuori.append((n, celle, numero_riga))
    return fuori


def esito_di(cella):
    for nome, rx in ESITI:
        if re.search(rx, cella, re.I):
            return nome
    return None


def main():
    ap = argparse.ArgumentParser(description="Conta le righe della tabella di tracciamento.")
    ap.add_argument("--matrice", default=MATRICE)
    args = ap.parse_args()

    with io.open(args.matrice, encoding="utf-8") as f:
        testo = f.read()
    righe = righe_della_tabella(testo)
    errori = []

    if not righe:
        errori.append("nessuna riga di tracciamento trovata: la tabella e' cambiata di forma")

    # ---- 1. numerazione continua, senza buchi ne' doppioni ----------------------
    numeri = [n for n, _c, _r in righe]
    doppi = sorted({n for n in numeri if numeri.count(n) > 1})
    if doppi:
        errori.append("righe duplicate: %s" % ", ".join("T%d" % n for n in doppi))
    if numeri:
        mancanti = sorted(set(range(1, max(numeri) + 1)) - set(numeri))
        if mancanti:
            errori.append("numerazione con buchi: manca %s"
                          % ", ".join("T%d" % n for n in mancanti))

    # ---- 2. cinque celle per riga -----------------------------------------------
    for n, celle, riga_file in righe:
        if len(celle) != 5:
            errori.append("T%d (riga %d del file): %d celle invece di 5 - un `|` dentro il "
                          "testo sposta la colonna dello stato" % (n, riga_file, len(celle)))

    # ---- 3. ogni riga esce con uno dei quattro esiti ------------------------------
    per_esito = {nome: [] for nome, _rx in ESITI}
    senza = []
    for n, celle, riga_file in righe:
        e = esito_di(celle[4]) if len(celle) == 5 else None
        if e is None:
            senza.append(n)
        else:
            per_esito[e].append(n)
    for n in senza:
        errori.append("T%d: nessuno dei quattro esiti previsti nella cella «Stato»" % n)

    # ---- il blocco da incollare -------------------------------------------------
    print("<!-- TABELLA DI TRACCIAMENTO - generata da `06_operativo\\conta_tracciamento.py`")
    print("     il %s. Si incolla VERBATIM: il numero delle righe non si legge a occhio. -->"
          % date.today().isoformat())
    print("")
    print("| Esito | Righe | Quali |")
    print("|---|---|---|")
    for nome, _rx in ESITI:
        n = per_esito[nome]
        print("| %s | **%d** | %s |"
              % (nome, len(n), ", ".join("T%d" % x for x in sorted(n)) or "—"))
    print("| **totale righe** | **%d** | da T1 a T%d, nessuna mancante e nessuna duplicata |"
          % (len(righe), max(numeri) if numeri else 0))

    if errori:
        print("\nERRORI: %d" % len(errori))
        for e in errori:
            print("  - " + e)
        return 1
    print("\nTabella integra: %d righe, numerazione continua da T1 a T%d, quattro esiti."
          % (len(righe), max(numeri)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
