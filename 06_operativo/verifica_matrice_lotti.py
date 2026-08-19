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
    """Righe utili dell'elenco, piu' il flag CHIUSO.

    Un elenco che porta `# CHIUSO` fra i commenti di testa e' un lotto gia'
    canonizzato: i suoi grezzi sono citati dalle note **per costruzione**, e il
    controllo 4 non si applica — esattamente come per la fetta pilota. Senza
    questo flag la verifica diventa rossa a ogni lotto che si chiude, cioe'
    proprio quando dovrebbe restare verde.
    """
    fuori, chiuso = [], False
    for riga in open(percorso, encoding="utf-8"):
        riga = riga.strip()
        if riga.startswith("#"):
            if riga.lstrip("# ").upper().startswith("CHIUSO"):
                chiuso = True
        elif riga:
            fuori.append(riga)
    return fuori, chiuso


def main():
    sources = os.path.join(Q.VAULT, "sources")
    su_disco = sorted(n for n in os.listdir(sources)
                      if os.path.isfile(os.path.join(sources, n)) and not n.lower().endswith(".md"))

    voci_pilota, _ = leggi(PILOTA)
    elenchi = [("fetta_l26130 (pilota, S2)", voci_pilota, True)]
    for n in sorted(os.listdir(DIR_LOTTI)):
        # E32: accanto all'elenco dei grezzi vive `<lotto>_note.txt`, che elenca le NOTE
        # modificate dal lotto. Non e' un elenco di grezzi e qui non si legge.
        if n.lower().endswith("_note.txt"):
            continue
        if n.lower().endswith(".txt"):
            voci, chiuso = leggi(os.path.join(DIR_LOTTI, n))
            elenchi.append((n[:-4], voci, chiuso))

    citati = set()
    for nota in Q.tutte_le_note(Q.VAULT):
        for f in nota.fonti:
            if f:
                citati.add(str(f))

    guasti = []
    proprietario = {}
    print("| Elenco | Grezzi |")
    print("|---|---|")
    for nome, voci, chiuso in elenchi:
        print("| %s | %d |%s" % (nome, len(voci), " *(chiuso)*" if chiuso else ""))
        for v in voci:
            if v in proprietario:
                guasti.append("DOPPIO      %s — in %s e in %s" % (v, proprietario[v], nome))
            else:
                proprietario[v] = nome
            if v not in su_disco:
                guasti.append("INESISTENTE %s — nominato da %s" % (v, nome))
            if not chiuso and v in citati:
                guasti.append("GIA' COPERTO %s — in %s ma gia' citato da una nota" % (v, nome))

    scoperti = [n for n in su_disco if n not in proprietario]
    for n in scoperti:
        guasti.append("SCOPERTO    %s — in nessun elenco" % n)

    totale = sum(len(v) for _, v, _c in elenchi)
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
