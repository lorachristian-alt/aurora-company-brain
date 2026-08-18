# -*- coding: utf-8 -*-
"""verifica_matrice_lotti — la matrice copre i 160 grezzi, ognuno una volta sola.

metodo_03 §9.3: la matrice e' un piano, non un vincolo, ma deve essere COMPLETA e
DISGIUNTA prima di eseguirla — «il pilota ha insegnato: i conteggi a mano sbagliano
di uno». Questo script e' l'unico che dichiara i numeri della matrice.

Controlla:
  1. ogni grezzo di `sources\\` sta in esattamente un elenco (fetta pilota compresa);
  2. nessun file compare in due lotti;
  3. nessun elenco nomina un file che non esiste in `sources\\`;
  4. nessun lotto contiene un grezzo gia' citato da una nota (salvo la fetta pilota).

Uso:
    python verifica_matrice_lotti.py
Esce 0 se la matrice e' completa e disgiunta, 1 altrimenti.
"""
import os, sys

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(QUI, "qa"))
import qa_comune as Q

DIR_LOTTI = os.path.join(QUI, "qa", "lotti")
PILOTA = os.path.join(QUI, "qa", "fetta_l26130.txt")


def leggi(percorso):
    fuori = []
    for riga in open(percorso, encoding="utf-8"):
        riga = riga.strip()
        if riga and not riga.startswith("#"):
            fuori.append(riga)
    return fuori


def main():
    sources = os.path.join(Q.VAULT, "sources")
    su_disco = sorted(n for n in os.listdir(sources)
                      if os.path.isfile(os.path.join(sources, n)) and not n.lower().endswith(".md"))

    elenchi = [("fetta_l26130 (pilota, S2)", leggi(PILOTA))]
    for n in sorted(os.listdir(DIR_LOTTI)):
        if n.lower().endswith(".txt"):
            elenchi.append((n[:-4], leggi(os.path.join(DIR_LOTTI, n))))

    citati = set()
    for nota in Q.tutte_le_note(Q.VAULT):
        for f in nota.fonti:
            if f:
                citati.add(str(f))

    guasti = []
    proprietario = {}
    print("| Elenco | Grezzi |")
    print("|---|---|")
    for nome, voci in elenchi:
        print("| %s | %d |" % (nome, len(voci)))
        for v in voci:
            if v in proprietario:
                guasti.append("DOPPIO      %s — in %s e in %s" % (v, proprietario[v], nome))
            else:
                proprietario[v] = nome
            if v not in su_disco:
                guasti.append("INESISTENTE %s — nominato da %s" % (v, nome))
            if nome != "fetta_l26130 (pilota, S2)" and v in citati:
                guasti.append("GIA' COPERTO %s — in %s ma gia' citato da una nota" % (v, nome))

    scoperti = [n for n in su_disco if n not in proprietario]
    for n in scoperti:
        guasti.append("SCOPERTO    %s — in nessun elenco" % n)

    totale = sum(len(v) for _, v in elenchi)
    print("| **totale righe** | **%d** |" % totale)
    print("")
    print("grezzi su disco ............ %d" % len(su_disco))
    print("nomi distinti nella matrice  %d" % len(proprietario))
    print("scoperti ................... %d" % len(scoperti))
    print("guasti ..................... %d" % len(guasti))
    for g in guasti:
        print("   %s" % g)

    if guasti:
        print("\nLA MATRICE NON E' COMPLETA E DISGIUNTA: non si esegue.")
        sys.exit(1)
    print("\nMatrice completa e disgiunta: %d grezzi, %d elenchi." % (len(su_disco), len(elenchi)))
    sys.exit(0)


if __name__ == "__main__":
    main()
