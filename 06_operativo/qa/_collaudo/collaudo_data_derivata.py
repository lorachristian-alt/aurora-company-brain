# -*- coding: utf-8 -*-
r"""collaudo_data_derivata — il derivato e' derivato qualunque sia il genere (E50 esteso).

=====================================================================================
PERCHE' QUESTO COLLAUDO ESISTE — IL BUCO TROVATO DAL LOTTO 3F
=====================================================================================
E50 dice che **un numero che la fonte non enuncia e' un valore derivato anche quando si
ottiene contando**, e che si scrive con la marca del modo — `(contate)`, `(calcolato)`. Lo
strato deterministico aveva preso la regola alla lettera: l'esenzione di `qa_provenance`
valeva per il solo `genere == "numero"`.

⚠️ **Una DATA derivata non aveva nessuna esenzione, e veniva respinta ANCHE MARCATA.**

⚠️ **Il caso**: la riunione di preparazione del lotto 3F e' convocata per «Domani mattina» in
una mail del **25/05/2026**. Il **26/05/2026** e' un derivato esatto, marcabile, e la nota ha
dovuto **togliere la data dal corpo** — con lo slug rinominato di conseguenza.

⚠️ **E la via d'uscita facile era un trucco**: scrivere «il ventisei maggio» in lettere passa
il controllo e dice la stessa cosa. **Il costo vero non era la precisione persa: era che chi
scrive imparava ad aggirare un controllo invece di soddisfarlo.**

=====================================================================================
CHE COSA IL FIX CAMBIA, E CHE COSA NO
=====================================================================================
⚠️ **Cambia il PERIMETRO del controllo, non il requisito** (§4). La marca resta OBBLIGATORIA e
continua a dichiarare che il valore va ricontato; la finestra resta stretta — sessanta
caratteri prima della marca, come per i numeri. **Cambia solo che ora la marca si puo' apporre
a una data.**

⚠️ **I due generi non si travasano**: un numero marcato non esenta una data, e viceversa. E'
il caso 7, ed e' quello che impedisce al fix di diventare un condono.

=====================================================================================
I CASI
=====================================================================================
| # | Caso | Atteso |
|---|---|---|
| 1 | **LA PREMESSA**: la fonte finta NON contiene la data derivata | non c'e' |
| 2 | **DIFETTO PIANTATO, verso 1**: data derivata **marcata** | **tace** (prima del fix scattava) |
| 3 | **DIFETTO PIANTATO, verso 2**: stessa data **senza marca**, assente dalla fonte | **SCATTA** |
| 4 | **NON-SCATTO DI REGRESSIONE**: numero derivato **marcato** | tace, come prima del fix |
| 5 | regressione, verso opposto: numero **senza marca**, assente dalla fonte | **SCATTA** |
| 6 | **il perimetro resta stretto**: marca a piu' di sessanta caratteri dalla data | **SCATTA** |
| 7 | **i generi non si travasano**: marca su un NUMERO, data non marcata accanto | **SCATTA** |
| 8 | la data che la fonte ENUNCIA, senza marca | tace |

⚠️ **Il caso 1 e' quello che rende gli altri qualcosa di piu' di una tautologia**: se la fonte
finta cominciasse a contenere il 26/05/2026, i casi 3, 6 e 7 tacerebbero per il motivo
sbagliato e nessuno se ne accorgerebbe.

Uso:
    python collaudo_data_derivata.py
Esce 0 se tutti i casi passano, 1 altrimenti.
"""
import io
import os
import shutil
import sys
import tempfile

QUI = os.path.dirname(os.path.abspath(__file__))
QA = os.path.normpath(os.path.join(QUI, os.pardir))
sys.path.insert(0, QA)

import qa_comune as Q          # noqa: E402
import qa_provenance as P      # noqa: E402

FONTE = u"mail_di_collaudo.txt"

# ⚠️ La fonte NON contiene il 26/05/2026 ne' il 217: e' esattamente il punto.
# Porta il 25/05/2026 e il 1.240, che le note citano per avere un aggancio vero —
# senza, la fonte risulterebbe «rumore nel payload» e il collaudo misurerebbe altro.
TESTO_FONTE = (
    u"Da: elena.marchetti@aurorafood.it\n"
    u"Data: 25/05/2026 14:38\n"
    u"Oggetto: preparativi\n\n"
    u"Domani mattina alle 9 in sala riunioni, ci vediamo tutti.\n"
    u"Il preventivo aperto e' di 1.240 euro.\n"
)

NOTA = u"""---
title: "Nota di collaudo"
summary: "Una frase sola."
type: atomica
area: qualita
tags: [areas, qualita]
fonti:
  - %(fonte)s
stato: risolto
aliases: []
data_nota: 2026-08-25
related: "[[_index-areas]]"
---

# Nota di collaudo

La mail e' del 25/05/2026 e apre un preventivo di 1.240 euro.

%(corpo)s

## Fonti

- [[%(fonte)s]] - §intestazione.
"""

# (nome, corpo, errori attesi)
CASI = [
    (u"DIFETTO PIANTATO, verso 1: data derivata MARCATA",
     u"La riunione cade quindi il 26/05/2026 *(derivato dalla data della mail)*.", 0),

    (u"DIFETTO PIANTATO, verso 2: stessa data SENZA marca",
     u"La riunione cade quindi il 26/05/2026.", 1),

    (u"REGRESSIONE: numero derivato MARCATO",
     u"Restano quindi 217 euro *(calcolato)* di scostamento.", 0),

    (u"regressione, verso opposto: numero SENZA marca",
     u"Restano quindi 217 euro di scostamento.", 1),

    (u"il perimetro resta stretto: marca oltre i sessanta caratteri",
     u"La riunione cade il 26/05/2026, e questa riga esiste solo per allontanare la marca "
     u"dalla data di piu' di sessanta caratteri *(derivato)*.", 1),

    (u"i generi non si travasano: marca su un NUMERO, data non marcata",
     u"Restano 217 euro *(calcolato)* e la riunione cade il 26/05/2026.", 1),

    (u"la data che la fonte ENUNCIA, senza marca",
     u"La mail porta la data del 25/05/2026 in intestazione.", 0),
]


def main():
    tmp = tempfile.mkdtemp(prefix="collaudo_data_der_")
    testo_vero = P.EC.testo_cantiere
    esiti = []
    try:
        P.EC.testo_cantiere = lambda nome: TESTO_FONTE if nome == FONTE else u""

        # --- 1. LA PREMESSA ---------------------------------------------------------
        ok1 = (u"26/05/2026" not in TESTO_FONTE) and (u"217" not in TESTO_FONTE)
        esiti.append((1, u"LA PREMESSA: la fonte finta non contiene ne' la data ne' il numero",
                      u"non c'e'", u"c'e'" if not ok1 else u"non c'e'", ok1))

        cartella = os.path.join(tmp, "areas")
        os.makedirs(cartella)
        for i, (nome, corpo, attesi) in enumerate(CASI, 2):
            p = os.path.join(cartella, "caso-%d.md" % i)
            with io.open(p, "w", encoding="utf-8") as f:
                f.write(NOTA % {"fonte": FONTE, "corpo": corpo})
            n = Q.Nota(p)
            rep = Q.Report("collaudo")
            P.controlla(n, rep, {})
            avuti = len(rep.errori)
            esiti.append((i, nome, u"%d errori" % attesi, u"%d errori" % avuti,
                          avuti == attesi))
    finally:
        P.EC.testo_cantiere = testo_vero
        shutil.rmtree(tmp, ignore_errors=True)

    print("=" * 92)
    print("COLLAUDO - il derivato e' derivato qualunque sia il genere (E50 esteso, gate 3F, 31/08/2026)")
    print("=" * 92)
    print("| # | Caso | Atteso | Avuto | Esito |")
    print("|---|---|---|---|---|")
    for i, nome, att, avu, ok in esiti:
        print("| %d | %s | %s | %s | %s |" % (i, nome, att, avu, "OK" if ok else "FALLITO"))
    falliti = [x for x in esiti if not x[4]]
    if falliti:
        print("\nCOLLAUDO FALLITO - %d casi su %d" % (len(falliti), len(esiti)))
        return 1
    print("\nCOLLAUDO SUPERATO - %d casi su %d." % (len(esiti), len(esiti)))
    print("Il caso 1 e' la premessa; i casi 2 e 3 sono il difetto piantato nei due versi;")
    print("i casi 4 e 5 provano che il ramo del numero non si e' mosso; i casi 6, 7 e 8")
    print("provano che il fix NON e' un condono - la finestra resta stretta, i generi non si")
    print("travasano, e una data che la fonte enuncia non ha mai avuto bisogno di marca.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
