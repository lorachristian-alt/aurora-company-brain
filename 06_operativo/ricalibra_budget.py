# -*- coding: utf-8 -*-
"""ricalibra_budget — i budget dei lotti restanti, ricalcolati sui consuntivi veri.

Le fasce della matrice sono state costruite in fase di pianificazione sulla densita'
del pilota — 2,1 note di contenuto per grezzo. I lotti chiusi dopo il pilota misurano
6,0 · 9,5 · 13,5: con le stime vecchie il controllo di apertura (E21/E28) scatterebbe a
ogni lotto, e una regola che scatta sempre viene scavalcata per prassi.

Questo script fa due cose, entrambe da script e non a mano (regola d'oro 5):
  1. calcola la densita' misurata, lotto per lotto e aggregata;
  2. proietta le note dei lotti restanti e dice quali superano il tetto di 40 note di
     E28 — cioe' quali vanno spezzati PRIMA di aprirli — e in quanti pezzi.

Uso:
    python ricalibra_budget.py
"""
from __future__ import division

# --- consuntivi: note di CONTENUTO prodotte, da conta_stato.py a ogni chiusura -------
CHIUSI = [
    # (lotto, grezzi, note di contenuto prodotte)
    ("pilota L26130", 22, 46),
    ("1A", 7, 42),
    ("1B", 4, 38),
    ("1C", 2, 27),
]

# --- i lotti restanti, come stanno oggi nella matrice --------------------------------
# classe: 'contenuto'  = documenti operativi densi, riconciliabili col vault
#         'normativo'  = documenti lunghi ma monotematici (DVR, CPI, AUA, polizze)
#         'rumore'     = fondo d'archivio: nota corta e pochi link (metodo_03 §1.3 es. 23)
RESTANTI = [
    (2,  "Igiene, sanificazione, autocontrollo, MOCA",        12, (20, 30), "contenuto"),
    (3,  "Sistema qualita', certificazioni, audit, crisi",    13, (22, 32), "contenuto"),
    (4,  "Filiera in entrata, fornitori, logistica",          14, (26, 36), "contenuto"),
    (5,  "Commerciale: cliente, listini, marginalita'",       15, (28, 38), "contenuto"),
    (6,  "Amministrazione, bilancio, cassa",                  15, (28, 40), "contenuto"),
    (7,  "Persone: lavoro, organico, sindacato",              15, (24, 34), "contenuto"),
    (8,  "Sicurezza sul lavoro, ambiente, assicurazioni",     11, (16, 24), "normativo"),
    (9,  "R&D, nuovi prodotti, investimenti, visione",        12, (22, 30), "contenuto"),
    (10, "Rumore di fondo e forma dell'archivio",             18, (14, 22), "rumore"),
]

TETTO_E28 = 40          # oltre questa soglia il lotto si spezza sempre
BERSAGLIO = 30          # dimensione a cui si punta spezzando: sotto la soglia doppia


def main():
    print("=" * 78)
    print("DENSITA' MISURATA SUI LOTTI CHIUSI")
    print("=" * 78)
    tot_g = tot_n = 0
    for nome, g, n in CHIUSI:
        print("  %-14s %2d grezzi -> %3d note di contenuto   densita' %5.1f" % (nome, g, n, n / g))
        tot_g += g; tot_n += n
    print("  %-14s %2d grezzi -> %3d note                    densita' %5.1f  (media pesata)"
          % ("TOTALE", tot_g, tot_n, tot_n / tot_g))

    dopo = [(g, n) for nome, g, n in CHIUSI if nome != "pilota L26130"]
    dg = sum(g for g, _ in dopo); dn = sum(n for _, n in dopo)
    d_recente = dn / dg
    print("  %-14s %2d grezzi -> %3d note                    densita' %5.1f  <-- riferimento"
          % ("dopo il pilota", dg, dn, d_recente))

    # densita' attesa per classe: si parte dal riferimento misurato e si corregge
    # verso il basso per le classi che il pilota ha mostrato meno dense.
    DENSITA = {
        "contenuto": d_recente,
        "normativo": d_recente * 0.75,
        "rumore":    d_recente * 0.30,
    }
    print("\n  densita' attesa per classe:")
    for k in ("contenuto", "normativo", "rumore"):
        print("    %-10s %5.1f note/grezzo" % (k, DENSITA[k]))

    print("\n" + "=" * 78)
    print("PROIEZIONE DEI LOTTI RESTANTI, E CHI VA SPEZZATO PRIMA DI APRIRLO")
    print("=" * 78)
    print("| # | Tema | Grezzi | Budget vecchio | Proiezione | Budget nuovo | Verdetto |")
    print("|---|---|---|---|---|---|---|")
    tot_proj = 0
    tot_pezzi = 0
    for num, tema, grezzi, (bmin, bmax), classe in RESTANTI:
        d = DENSITA[classe]
        proj = grezzi * d
        tot_proj += proj
        pezzi = max(1, int(proj / BERSAGLIO) + (1 if proj % BERSAGLIO else 0))
        tot_pezzi += pezzi
        per_pezzo = proj / pezzi
        nuovo = (int(proj * 0.85), int(proj * 1.15))
        if proj > TETTO_E28:
            verdetto = "**SPEZZARE in %d** (~%d grezzi, ~%d note per pezzo)" % (
                pezzi, round(grezzi / pezzi), round(per_pezzo))
        elif proj > bmax:
            verdetto = "budget alzato, non si spezza"
        else:
            verdetto = "invariato"
        print("| %d | %s | %d | %d-%d | **%d** | %d-%d | %s |"
              % (num, tema, grezzi, bmin, bmax, round(proj), nuovo[0], nuovo[1], verdetto))
    print("| | **totale** | **%d** | 200-286 | **%d** | | **%d lotti invece di 9** |"
          % (sum(r[2] for r in RESTANTI), round(tot_proj), tot_pezzi))

    print(chr(10) + "=" * 78)
    print("IL CONTROLLO CHE SMONTA IL MODELLO LINEARE")
    print("=" * 78)
    print("  Le NOTE PER LOTTO sono molto piu' stabili del rapporto note/grezzo:")
    for nome, g, n_ in CHIUSI:
        print("    %-14s %2d grezzi -> %3d note" % (nome, g, n_))
    note_lotto = [n_ for _, _, n_ in CHIUSI]
    media = sum(note_lotto) / len(note_lotto)
    scarto_n = max(note_lotto) - min(note_lotto)
    dens = [n_ / g for _, g, n_ in CHIUSI]
    print("    note per lotto: min %d, max %d, scarto %d su una media di %.0f (%.0f%%)"
          % (min(note_lotto), max(note_lotto), scarto_n, media, 100 * scarto_n / media))
    print("    densita':       min %.1f, max %.1f, scarto %.1f su una media di %.1f (%.0f%%)"
          % (min(dens), max(dens), max(dens) - min(dens), sum(dens) / len(dens),
             100 * (max(dens) - min(dens)) / (sum(dens) / len(dens))))
    print("  ATTENZIONE: i grezzi per lotto sono passati da 22 a 2 mentre le note restavano")
    print("  fra 46 e 27. Cio' che si mantiene costante e' il LOTTO, non la densita': moltiplicare")
    print("  una densita' misurata su lotti da 2-7 grezzi per lotti da 12-18 e' un artefatto.")

    print("\n" + "=" * 78)
    print("REGOLA CHE NE DISCENDE")
    print("=" * 78)
    print("  Con densita' attesa %.1f note/grezzo e tetto di %d note (E28):" % (d_recente, TETTO_E28))
    print("    massimo %d grezzi per lotto di CONTENUTO" % int(TETTO_E28 / DENSITA["contenuto"]))
    print("    massimo %d grezzi per lotto NORMATIVO" % int(TETTO_E28 / DENSITA["normativo"]))
    print("    massimo %d grezzi per lotto di RUMORE" % int(TETTO_E28 / DENSITA["rumore"]))
    print("\n  Note totali proiettate a fine corsa: %d di contenuto sui %d grezzi restanti,"
          % (round(tot_proj), sum(r[2] for r in RESTANTI)))
    print("  piu' le %d gia' scritte = **%d note di contenuto** nel vault finale."
          % (tot_n, round(tot_proj) + tot_n))


if __name__ == "__main__":
    main()
