# -*- coding: utf-8 -*-
"""collaudo_due_tassi — il tasso di produzione conta scoperta una nota, e solo quella giusta.

⚠️ **PERIMETRO CHIUSO.** Questo collaudo non guarda il vault vero: costruisce due note
finte, con fonti scelte a mano, e verifica il SOLO predicato che decide il tasso di
difetto di produzione — «la nota parla del dominio e non ha fra le sue fonti nessuna
delle fonti che quel dominio lo governano».

PERCHE' ESISTE, e perche' proprio adesso.
Il gate del 21/08/2026 ha aggiunto una **seconda fonte governante** al dominio
`allergeni`: il materiale di formazione, accanto alla scheda PRPo1. E' un cambiamento
che puo' solo ABBASSARE il tasso — ogni nota che prima era scoperta e ora cita la
seconda fonte diventa coperta — e un fix che allenta si approva **solo** se il collaudo
prova che non ha aperto un buco. Da qui i due versi, che sono due e non uno:

  1. ALLENTAMENTO — una nota che parla del dominio e cita **solo la seconda** fonte
     deve risultare COPERTA. Prima del cambiamento risultava scoperta, e le tre note
     della formazione del lotto 2B-bis sono esattamente questo caso.

  2. STRETTA — una nota che parla del dominio e non cita **nessuna** delle due deve
     restare SCOPERTA. Se cadesse anche questa, il tasso non misurerebbe piu' niente:
     darebbe zero sempre, ed e' il modo in cui una misura smette di essere una misura
     senza che nessuno se ne accorga.

⚠️ **Il numero gia' pubblicato non si tocca**: il 9,1 % del lotto 2B-bis e' stato
misurato con lo strumento di allora e resta scritto cosi' (E46). Questo collaudo
verifica lo strumento di adesso, non riscrive la serie.

Uso:
    python collaudo_due_tassi.py
Esce 0 se entrambi i versi passano, 1 altrimenti.
"""
import io, os, shutil, sys, tempfile

QUI = os.path.dirname(os.path.abspath(__file__))
QA = os.path.dirname(QUI)
OPERATIVO = os.path.dirname(QA)
sys.path.insert(0, QA)
sys.path.insert(0, OPERATIVO)
import qa_comune as Q
import candidate_r1 as C1

DOMINIO = "allergeni"
SCHEDA = "scheda_allergeni_matrice_cross_contamination.docx"
AULA = "formazione_allergeni_operatori_2026.pptx"
ESTRANEA = "manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt"

NOTA = """\
---
title: "%s"
summary: "Nota di collaudo del predicato di copertura: parla di allergeni e di rework, e cita le fonti indicate nel proprio nome."
type: atomica
area: qualita
tags: [areas, qualita, collaudo, allergeni]
fonti:
%s
stato: risolto
aliases: []
data_nota: 2026-08-21
related: "[[area-qualita]]"
---

# %s

La sequenza di produzione tiene conto degli **allergeni** e il **rework** e' ammesso solo
entro il turno: la nota parla del dominio, e sul punto non ci sono dubbi.

## Fonti
%s
"""


def scrivi_nota(cartella, slug, titolo, fonti):
    p = os.path.join(cartella, "areas", slug + ".md")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    elenco = "\n".join("  - " + f for f in fonti)
    blocco = "\n".join("- [[%s]] — riferimento di collaudo." % f for f in fonti)
    with io.open(p, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(NOTA % (titolo, elenco, titolo, blocco))
    return p


def scoperta(nota, dom):
    """Il predicato vero e proprio, copiato da `misura_due_tassi.stato`."""
    if not any(rx.search(C1.testo_della_nota(nota)) for rx in dom["rx"]):
        return None                      # non parla del dominio: fuori dal denominatore
    return not ({str(f) for f in nota.fonti} & dom["fonti"])


def main():
    dom = C1.DOMINI[DOMINIO]
    print("dominio «%s» — fonti governanti dichiarate: %d" % (DOMINIO, len(dom["fonti"])))
    for f in sorted(dom["fonti"]):
        print("   ·", f)
    print()

    tmp = tempfile.mkdtemp(prefix="collaudo_tassi_")
    try:
        casi = [
            ("ALLENTAMENTO: cita SOLO la seconda fonte governante",
             "collaudo-tassi-solo-aula", [AULA], False),
            ("STRETTA: non cita nessuna delle due",
             "collaudo-tassi-nessuna", [ESTRANEA], True),
            ("controprova: cita la prima fonte governante",
             "collaudo-tassi-solo-scheda", [SCHEDA], False),
        ]
        esiti = []
        for etichetta, slug, fonti, atteso in casi:
            p = scrivi_nota(tmp, slug, slug, fonti)
            n = Q.Nota(p)
            avuto = scoperta(n, dom)
            ok = (avuto == atteso)
            esiti.append(ok)
            print("%-52s attesa=%-9s avuta=%-9s %s"
                  % (etichetta, "scoperta" if atteso else "coperta",
                     "scoperta" if avuto else "coperta",
                     "ok" if ok else "*** FALLITO"))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print()
    if all(esiti):
        print("COLLAUDO SUPERATO — %d casi su %d, nei due versi." % (len(esiti), len(esiti)))
        print("Il fix ABBASSA il tasso dove deve e NON lo abbassa dove non deve.")
        return 0
    print("COLLAUDO FALLITO: il predicato di copertura non fa quello che dichiara.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
