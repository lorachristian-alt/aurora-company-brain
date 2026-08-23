# -*- coding: utf-8 -*-
"""ricalibra_budget — la densita' misurata sui lotti chiusi, LETTA e non ricopiata.

⚠️ RISCRITTO IL 23/08/2026, AL GATE DEL LOTTO 3B, DAL CENSIMENTO DELLE COPIE DI STATO
(§4.49 del passaggio di consegne). Questo script era il caso piu' grave del censimento:
teneva **due liste scritte a mano** — i lotti chiusi coi loro consuntivi e i lotti restanti
con le loro fasce — e le teneva ferme al **19/08/2026**. Cinque lotti dopo, la prima tabella
diceva che i lotti chiusi erano quattro; il resto del progetto ne contava dieci.

⚠️ **Nessuno se n'era accorto perche' nessuno lo lanciava**, ed e' la forma peggiore della
malattia di §4.47: uno strumento che non mente mai a voce alta perche' non parla mai, e che
al primo rilancio avrebbe dato numeri di cinque lotti fa con l'aria di darli di oggi.

DA DOVE LEGGE, ADESSO. Niente qui dentro e' scritto a mano:
  - i **lotti** e i loro grezzi ........ dagli elenchi in `qa\\lotti\\` e dalla fetta pilota;
  - **chiuso / manutenzione** .......... dai marcatori, via `verifica_matrice_lotti.leggi`;
  - le **note** di ogni lotto .......... dal vault, incrociando `fonti` coi grezzi del lotto;
  - la **capacita'** ................... da E31: 25-35 note di contenuto, tetto 40 (E28).

⚠️ CHE COSA MISURA, DETTO COL SUO NOME (E46). «Note del lotto» qui significa **note di
contenuto che citano almeno un grezzo di quel lotto**, non «note che quel lotto ha prodotto»:
una nota estesa da un lotto successivo (E32) cita grezzi di due lotti e viene contata in
**entrambi**. Lo scarto si dichiara in coda, nota per nota, e non si aggiusta: e' il numero
che le fonti sanno dare, e un numero che si aggiusta a mano e' il difetto che questo file e'
stato riscritto per togliere.

⚠️ LE FASCE DEI LOTTI 2-10 NON ESISTONO PIU' (E31), e non sono state sostituite da altre
fasce: al loro posto vale la **capacita'**. La proiezione qui sotto e' quindi sulla capacita',
non su una densita' per grezzo — che i consuntivi hanno gia' mostrato essere un artefatto.

Uso:
    python ricalibra_budget.py
    python ricalibra_budget.py --vault <percorso>
Esce 0 sempre: e' un consuntivo, non un controllo.
"""
from __future__ import division

import argparse
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(QUI, "qa"))
import qa_comune as Q                    # noqa: E402
import verifica_matrice_lotti as V       # noqa: E402

DIR_LOTTI = os.path.join(QUI, "qa", "lotti")
PILOTA = os.path.join(QUI, "qa", "fetta_l26130.txt")

# E31 + E28: la capacita' e la soglia, che sono l'unico budget in vigore.
CAPACITA = (25, 35)
TETTO_E28 = 40
BERSAGLIO = 30


def elenchi():
    """(nome, grezzi, chiuso, manutenzione, della_matrice) per ogni elenco, pilota compreso."""
    voci, _c, _m = V.leggi(PILOTA)
    fuori = [("pilota L26130", voci, True, False, False)]
    for n in sorted(os.listdir(DIR_LOTTI)):
        if n.lower().endswith("_note.txt") or not n.lower().endswith(".txt"):
            continue
        voci, chiuso, manut = V.leggi(os.path.join(DIR_LOTTI, n))
        fuori.append((n[:-4], voci, chiuso, manut, True))
    return fuori


def note_di_contenuto(vault):
    """Le note di contenuto del vault, con l'insieme dei grezzi che ciascuna cita.

    Stessa definizione di `conta_stato.py`, e non una seconda: fuori gli `_index`, le
    note-strumento del progetto (E20) e le note di diario."""
    fuori = []
    for n in Q.tutte_le_note(vault):
        if n.type == "index" or Q.e_nota_strumento(n) or n.type in ("sessione", "daily"):
            continue
        fuori.append((n.slug, {str(f) for f in n.fonti if f}))
    return fuori


def main():
    ap = argparse.ArgumentParser(description="Densita' misurata e capacita' dei lotti restanti.")
    ap.add_argument("--vault", default=Q.VAULT)
    args = ap.parse_args()

    tutti = elenchi()
    note = note_di_contenuto(args.vault)

    chiusi = [e for e in tutti if e[2]]
    aperti = [e for e in tutti if not e[2] and e[4]]

    # a quanti lotti chiusi appartiene ogni nota: e' lo scarto da dichiarare
    per_nota = {}
    conteggio = {}
    for nome, grezzi, _c, _m, _d in chiusi:
        g = set(grezzi)
        dentro = [slug for slug, fonti in note if fonti & g]
        conteggio[nome] = dentro
        for slug in dentro:
            per_nota.setdefault(slug, []).append(nome)
    condivise = {s: l for s, l in per_nota.items() if len(l) > 1}

    print("=" * 84)
    print("I LOTTI CHIUSI, LETTI DAI MARCATORI - e le loro note, lette dal vault")
    print("=" * 84)
    print("| Lotto | Grezzi | Note di contenuto che li citano | Note/grezzo | Specie |")
    print("|---|---|---|---|---|")
    canon = []
    for nome, grezzi, _c, manut, della_matrice in chiusi:
        n_g, n_n = len(grezzi), len(conteggio[nome])
        specie = "manutenzione" if manut else ("pilota" if not della_matrice else "canonizzazione")
        dens = "-" if not n_g else "%.1f" % (n_n / n_g)
        print("| %s | %d | %d | %s | %s |" % (nome, n_g, n_n, dens, specie))
        if not manut:
            canon.append((nome, n_g, n_n))
    print("")
    print("lotti chiusi ............... %d   (di cui manutenzione: %d, fuori dalla serie per E38)"
          % (len(chiusi) - 1, sum(1 for e in chiusi if e[3])))
    print("   ⚠ il pilota e' contato a parte: non ha marcatore e non e' della matrice")

    print("")
    print("=" * 84)
    print("LO SCARTO, DICHIARATO: le note che appartengono a PIU' DI UN LOTTO")
    print("=" * 84)
    print("note contate in due o piu' lotti ... %d su %d"
          % (len(condivise), sum(len(v) for v in conteggio.values())))
    for slug in sorted(condivise)[:20]:
        print("   %-58s %s" % (slug, " + ".join(condivise[slug])))
    if len(condivise) > 20:
        print("   ... e altre %d" % (len(condivise) - 20))
    print("⚠ Sono le note che un lotto successivo ha ESTESO (E32): il conteggio le vede in")
    print("  entrambi i lotti, e questo numero e' la misura di quanto la somma ecceda il vero.")

    print("")
    print("=" * 84)
    print("IL CONTROLLO CHE SMONTA IL MODELLO LINEARE (lotto 1C, ancora vero)")
    print("=" * 84)
    if canon:
        n_note = [n for _n, _g, n in canon]
        dens = [n / g for _n, g, n in canon if g]
        media = sum(n_note) / len(n_note)
        print("  note per lotto di canonizzazione: min %d, max %d, scarto %d su una media di %.0f (%.0f%%)"
              % (min(n_note), max(n_note), max(n_note) - min(n_note), media,
                 100 * (max(n_note) - min(n_note)) / media))
        if dens:
            m_d = sum(dens) / len(dens)
            print("  densita' note/grezzo ...........: min %.1f, max %.1f, scarto %.1f su una media di %.1f (%.0f%%)"
                  % (min(dens), max(dens), max(dens) - min(dens), m_d,
                     100 * (max(dens) - min(dens)) / m_d))
    print("  Cio' che si mantiene costante e' il LOTTO, non la densita': moltiplicare una")
    print("  densita' misurata su lotti da 2-7 grezzi per lotti da 12-18 e' un artefatto,")
    print("  ed e' esattamente la ragione per cui E31 ha sostituito le fasce con la capacita'.")

    print("")
    print("=" * 84)
    print("GLI ELENCHI ANCORA APERTI, E LA CAPACITA' DI E31 (%d-%d note, tetto %d)"
          % (CAPACITA[0], CAPACITA[1], TETTO_E28))
    print("=" * 84)
    print("| Elenco | Grezzi | Pezzi da ~%d note attesi |" % BERSAGLIO)
    print("|---|---|---|")
    tot_g = 0
    for nome, grezzi, _c, _m, _d in aperti:
        tot_g += len(grezzi)
        print("| %s | %d | %s |"
              % (nome, len(grezzi),
                 "si ripacchettizza in apertura (E31)" if len(grezzi) > 5 else "1"))
    print("| **totale** | **%d** | |" % tot_g)
    print("")
    print("⚠ Quanti pezzi servano NON si proietta qui: E31 dice che i grezzi di un lotto si")
    print("  decidono in APERTURA contando i fatti (E21), non moltiplicando una densita'.")
    print("  Questo script misura il consuntivo; la proiezione la fa l'apertura del lotto.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
