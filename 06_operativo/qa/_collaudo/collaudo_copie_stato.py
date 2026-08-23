# -*- coding: utf-8 -*-
r"""collaudo_copie_stato — la copia che diverge dal padrone deve scattare, e il padrone deve leggersi.

=====================================================================================
PERCHE' QUESTO COLLAUDO ESISTE
=====================================================================================
`verifica_copie_stato.py` e' un controllo di CONFRONTO, e i controlli di confronto hanno un
modo tutto loro di morire: **il padrone smette di leggersi** — un titolo riformattato, un
blocco recintato spostato — e il confronto contro l'insieme vuoto **assolve tutto**. ⚠️ E'
esattamente il difetto MUTO di `verifica_dominio.py`, dove `\b` scartava in silenzio ogni
sigla del corpus e restavano solo i riscontri deboli: **uno script che tace non e' uno script
che assolve** (E56).

Quindi il collaudo pianta il difetto **nei due versi**:
  - la copia che **diverge** dal padrone deve scattare;
  - il padrone che **non si legge** deve scattare, e non passare per «tutto in ordine».

=====================================================================================
I CASI
=====================================================================================
| # | Caso | Atteso |
|---|---|---|
| 1 | il censimento vero, com'e' oggi | **tutto concorde** |
| 2 | **DIFETTO PIANTATO**: alla copia delle aree si **aggiunge** un valore che il manuale non ha | **scatta** |
| 3 | **DIFETTO PIANTATO**: dalla copia delle aree si **toglie** un valore che il manuale ha | **scatta** |
| 4 | **DIFETTO PIANTATO**: il padrone non si legge (sezione introvabile) | **scatta**, e non assolve |
| 5 | i quattro padroni si leggono davvero, e nessuno e' vuoto | **quattro elenchi non vuoti** |

Uso:
    python collaudo_copie_stato.py
Esce 0 se tutti i casi passano, 1 altrimenti.
"""
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(QUI, os.pardir, os.pardir))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "qa"))

import qa_comune as Q          # noqa: E402
import verifica_copie_stato as C  # noqa: E402


def divergenze(voci):
    """Le voci del censimento in cui copia e padrone non coincidono, o il padrone e' vuoto."""
    return [v for v in voci if not v[3] or set(v[1]) != set(v[3])]


def main():
    esiti = []
    vere_aree = set(Q.AREE)

    # 1. com'e' oggi
    esiti.append((1, "il censimento vero, com'e' oggi", 0, len(divergenze(C.censimento()))))

    # 2. una voce di troppo nella copia
    try:
        Q.AREE = vere_aree | {"area-inventata-dal-collaudo"}
        esiti.append((2, "difetto piantato: una voce IN PIU' nella copia", 1,
                      len(divergenze(C.censimento()))))
        # 3. una voce di meno
        Q.AREE = vere_aree - {sorted(vere_aree)[0]}
        esiti.append((3, "difetto piantato: una voce IN MENO nella copia", 1,
                      len(divergenze(C.censimento()))))
    finally:
        Q.AREE = vere_aree

    # 4. il padrone che non si legge
    vero_lettore = C.aree_dal_manuale
    try:
        C.aree_dal_manuale = lambda _manuale: set()
        esiti.append((4, "difetto piantato: il padrone non si legge (non deve assolvere)", 1,
                      len(divergenze(C.censimento()))))
    finally:
        C.aree_dal_manuale = vero_lettore

    # 5. nessun padrone vuoto
    vuoti = [v[4] for v in C.censimento() if not v[3]]
    esiti.append((5, "i quattro padroni si leggono, nessuno vuoto", 0, len(vuoti)))

    print("=" * 84)
    print("COLLAUDO - la copia che diverge deve scattare, e il padrone deve leggersi")
    print("=" * 84)
    print("| # | Caso | Divergenze attese | Avute | Esito |")
    print("|---|---|---|---|---|")
    for i, nome, atteso, avuto in esiti:
        print("| %d | %s | %d | %d | %s |"
              % (i, nome, atteso, avuto, "OK" if atteso == avuto else "FALLITO"))
    falliti = [e for e in esiti if e[2] != e[3]]
    if falliti:
        print("\nCOLLAUDO FALLITO - %d casi su %d" % (len(falliti), len(esiti)))
        return 1
    print("\nCOLLAUDO SUPERATO - %d casi su %d, nei due versi." % (len(esiti), len(esiti)))
    print("Il caso 4 e' quello che conta: un confronto contro l'insieme vuoto assolverebbe")
    print("sempre, ed e' il modo in cui un controllo di confronto muore senza rompersi.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
