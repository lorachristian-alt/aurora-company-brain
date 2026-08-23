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

E DICHIARA, perche' e' l'unico che lo sa: **quanti lotti sono CHIUSI**.

⚠️ Adempimento del gate del lotto 3B (23/08/2026). Il numero dei lotti chiusi era
l'ultimo del progetto che il coordinatore componeva **a mano**, dentro i prompt e nella
§3 del passaggio di consegne — ed e' uscito sbagliato: «undici» dove i marcatori
`# CHIUSO` erano dieci. **E' la malattia che il progetto cura con gli script, ricomparsa
al livello che dovrebbe controllarla** (§4.47: una copia di stato dentro uno strumento si
disallinea in silenzio, e lo fa sempre).

Da qui in poi **il numero si legge da qui e si INCOLLA**, come il blocco di
`conta_stato.py`. Il padrone e' il marcatore `# CHIUSO` in testa all'elenco, che il metodo
gia' impone alla chiusura di ogni lotto (§2 del prompt dei lotti).

⚠️ **La fetta pilota non porta il marcatore e non e' un elenco della matrice**: e'
anteriore alla matrice, e questo script la tratta come chiusa per il controllo 4 senza
contarla fra i lotti chiusi. Si dichiara a parte, in chiaro, perche' la differenza fra
dieci e undici e' esattamente quella e non deve tornare a essere l'aritmetica di qualcuno.

Uso:
    python verifica_matrice_lotti.py
Esce 0 se la matrice e' completa e disgiunta, 1 altrimenti.
"""
import os, re, sys

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(QUI, "qa"))
import qa_comune as Q

DIR_LOTTI = os.path.join(QUI, "qa", "lotti")
PILOTA = os.path.join(QUI, "qa", "fetta_l26130.txt")

# I DUE MARCATORI, RICONOSCIUTI COME MARCATORI E NON COME PREFISSI DI PROSA.
#
# ⚠️ Il primo riconoscimento, scritto lo stesso giorno, faceva `startswith` sulla parola:
# l'elenco del lotto **1B** — un lotto di canonizzazione — risultava di MANUTENZIONE per via
# di una riga di commento che va a capo su «manutenzione mai firmato». **Un conteggio nato
# per togliere l'aritmetica dalle mani di qualcuno sbagliava alla prima misura**, ed era la
# stessa specie che stava riparando: un riscontro DEBOLE preso per forte (E56).
#
# La forma del marcatore la impone il metodo, e questi due la pretendono:
#   §2 del prompt dei lotti ... `# CHIUSO <data>` in testa all'elenco;
#   §3-bis (E35) .............. `# MANUTENZIONE` in testa, da solo.
RX_CHIUSO = re.compile(r"^CHIUSO\b\s*(IL\s+)?\d")
RX_MANUTENZIONE = re.compile(r"^MANUTENZIONE\s*([—–-].*)?$")


def leggi(percorso):
    """Righe utili dell'elenco, piu' i flag CHIUSO e MANUTENZIONE.

    Un elenco che porta `# CHIUSO` fra i commenti di testa e' un lotto gia'
    canonizzato: i suoi grezzi sono citati dalle note **per costruzione**, e il
    controllo 4 non si applica — esattamente come per la fetta pilota. Senza
    questo flag la verifica diventa rossa a ogni lotto che si chiude, cioe'
    proprio quando dovrebbe restare verde.
    """
    fuori, chiuso, manutenzione = [], False, False
    for riga in open(percorso, encoding="utf-8"):
        riga = riga.strip()
        if riga.startswith("#"):
            testa = riga.lstrip("# ").upper()
            if RX_CHIUSO.match(testa):
                chiuso = True
            if RX_MANUTENZIONE.match(testa):
                manutenzione = True
        elif riga:
            fuori.append(riga)
    return fuori, chiuso, manutenzione


def main():
    sources = os.path.join(Q.VAULT, "sources")
    su_disco = sorted(n for n in os.listdir(sources)
                      if os.path.isfile(os.path.join(sources, n)) and not n.lower().endswith(".md"))

    voci_pilota, _c, _m = leggi(PILOTA)
    # Il pilota entra col flag `chiuso` alzato SOLO per esentarlo dal controllo 4 (i suoi
    # grezzi sono citati per costruzione). Non e' un elenco della matrice e NON entra nel
    # conteggio dei lotti chiusi: il quinto campo, `della_matrice`, tiene i due fatti
    # separati invece di lasciarli confondere da chi legge.
    elenchi = [("fetta_l26130 (pilota, S2)", voci_pilota, True, False, False)]
    for n in sorted(os.listdir(DIR_LOTTI)):
        # E32: accanto all'elenco dei grezzi vive `<lotto>_note.txt`, che elenca le NOTE
        # modificate dal lotto. Non e' un elenco di grezzi e qui non si legge.
        if n.lower().endswith("_note.txt"):
            continue
        if n.lower().endswith(".txt"):
            voci, chiuso, manut = leggi(os.path.join(DIR_LOTTI, n))
            elenchi.append((n[:-4], voci, chiuso, manut, True))

    citati = set()
    for nota in Q.tutte_le_note(Q.VAULT):
        for f in nota.fonti:
            if f:
                citati.add(str(f))

    guasti = []
    proprietario = {}
    print("| Elenco | Grezzi |")
    print("|---|---|")
    for nome, voci, chiuso, manut, _della_matrice in elenchi:
        marca = " *(chiuso)*" if chiuso else ""
        if manut:
            marca += " *(manutenzione)*"
        print("| %s | %d |%s" % (nome, len(voci), marca))
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

    totale = sum(len(v) for _n, v, _c, _m, _d in elenchi)
    print("| **totale righe** | **%d** |" % totale)
    print("")
    print("grezzi su disco ............ %d" % len(su_disco))
    print("nomi distinti nella matrice  %d" % len(proprietario))
    print("scoperti ................... %d" % len(scoperti))

    # ---- IL NUMERO CHE DA QUI IN POI SI INCOLLA E NON SI CONTA ----------------------
    chiusi = [e for e in elenchi if e[2] and e[4]]
    canonizzazione = [e for e in chiusi if not e[3]]
    manutenzione = [e for e in chiusi if e[3]]
    aperti = [e for e in elenchi if not e[2] and e[4]]
    print("")
    print("lotti chiusi: %d" % len(chiusi))
    print("   di cui di canonizzazione ... %d (%s)"
          % (len(canonizzazione), ", ".join(e[0] for e in canonizzazione)))
    print("   di cui di manutenzione ..... %d (%s)"
          % (len(manutenzione), ", ".join(e[0] for e in manutenzione) or "nessuno"))
    print("   elenchi ancora aperti ...... %d" % len(aperti))
    print("   FUORI dal conteggio: la fetta pilota (%d grezzi), anteriore alla matrice e"
          % len(voci_pilota))
    print("                        senza marcatore `# CHIUSO`. Canonizzata in S2.")
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
