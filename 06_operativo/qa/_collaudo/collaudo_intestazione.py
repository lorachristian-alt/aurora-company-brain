# -*- coding: utf-8 -*-
r"""collaudo_intestazione — un'affermazione inventata nel `title` o nel `summary` deve scattare.

=====================================================================================
PERCHE' QUESTO COLLAUDO ESISTE
=====================================================================================
Fino al 23/08/2026 lo strato deterministico di `qa_provenance.py` estraeva le affermazioni
verificabili dal SOLO `corpo_senza_fonti`. ⚠️ **Il `title` e il `summary` vivono nel
frontmatter e restavano fuori**: un numero, una data o un codice inventati li' passavano la
QA a **verde**.

⚠️ **E' la superficie su cui questo progetto trova piu' difetti di ogni altra**, e la si
lasciava alla sola diligenza:

| Emendamento | Che cosa dice dell'intestazione |
|---|---|
| **E18** | se la nota stabilisce una regola decisionale, **il `summary` la enuncia** |
| **E30** | `title` e `summary` si rileggono **come note a se'**, a OGNI giro — nel lotto 1C, al terzo giro, **sei rilievi su sette** stavano li' col corpo gia' corretto |
| **E39 · E42** | la cautela si propaga a `summary`, `title`, celle di tabella, glosse |
| **E51** | una nota non puo' essere smentita dalla propria intestazione |
| **E61** | la frase NUOVA scritta correggendo si verifica come una di prima stesura |

**Cinque emendamenti sulla stessa superficie, e nessuno strato deterministico dietro.**

⚠️ **Il buco non era teorico**: alla prima misura il vault portava **quattordici**
affermazioni che vivono solo nell'intestazione e che nessuna fonte citata sorregge — quasi
tutte **date scritte con l'anno dove la fonte non lo scrive** (`05/05/2026` in nota, `5/5`
nel quaderno OCR). Sono E24 ed E50 sulla superficie che nessuno controllava.

=====================================================================================
IL DIFETTO PIANTATO, E IL SUO ROVESCIO
=====================================================================================
Il fix **aggiunge agganci** (§4.9): non avrebbe bisogno del difetto piantato, e ce l'ha lo
stesso perche' «chi lo applica pianta anche il difetto nel collaudo, o il buco si riapre in
silenzio» (§4 del prompt dei lotti).

⚠️ **Il collaudo chiama `qa_provenance.controlla`, cioe' la VIA CHE LA PRODUZIONE USA**, non
una copia della sua logica: e' §4.29, che nasce dal pacchetto del giudizio tagliato in fette
per una via equivalente e mai esercitata.

| # | Caso | Atteso |
|---|---|---|
| 1 | numero inventato **solo nel `summary`**, nota nata sotto la regola — **IL DIFETTO PIANTATO** | **ERRORE** |
| 2 | numero inventato **solo nel campo `title`** (H1 pulito), nota nata sotto la regola | **ERRORE** |
| 3 | data inventata **solo nel `summary`** | **ERRORE** |
| 4 | stesso difetto, ma nota **anteriore al 23/08/2026** | **AVVISO** col debito (§4.35), mai errore |
| 5 | intestazione con numeri **tutti riscontrati nella fonte** | **tace** |
| 6 | numero inventato **nel corpo** *(il controllo di sempre)* | **ERRORE** |
| 7 | lo stesso numero inventato **nel corpo E nell'intestazione** | **un rilievo solo**, non due |
| 8 | valore **derivato e marcato** nel `summary` (E23) | **tace** |

Uso:
    python collaudo_intestazione.py
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

import qa_comune as Q            # noqa: E402
import estrazione_cantiere as EC  # noqa: E402
import qa_provenance as P        # noqa: E402


NOTA = """---
title: "%(title)s"
summary: "%(summary)s"
type: atomica
area: qualita
tags: [areas, qualita]
fonti:
  - x.csv
stato: risolto
aliases: []
data_nota: %(data)s
related: "[[_index-areas]]"
---

# %(h1)s

%(corpo)s

## Fonti

- [[x.csv]] - riga 2.
"""

# La fonte finta porta 250 pezzi e la data 07/07/2026: tutto il resto e' inventato.
FONTE = "voce;valore;quando\npezzi;250;07/07/2026\n"

OGGI = "2026-08-23"       # nata SOTTO la regola
IERI = "2026-08-18"       # nata PRIMA della regola

SANO = {"title": "Nota di collaudo", "h1": "Nota di collaudo",
        "summary": "Una frase sola, senza cifre inventate.",
        "corpo": "Il corpo dichiara 250 pezzi, che la fonte porta.", "data": OGGI}

# (nome, dati, errori attesi, avvisi attesi) - contati sulle SOLE voci che citano il token
CASI = [
    ("difetto piantato: numero inventato solo nel `summary`",
     dict(SANO, summary="Il valore dichiarato e' 91919 pezzi."), 1, 0),
    ("numero inventato solo nel campo `title`, con l'H1 pulito",
     dict(SANO, title="I 91919 pezzi del collaudo"), 1, 0),
    ("data inventata solo nel `summary`",
     dict(SANO, summary="Deciso il 14/03/2026, e altrove non compare."), 1, 0),
    ("lo stesso difetto su una nota ANTERIORE al 23/08/2026",
     dict(SANO, summary="Il valore dichiarato e' 91919 pezzi.", data=IERI), 0, 1),
    ("intestazione con i numeri tutti riscontrati nella fonte",
     dict(SANO, summary="La fonte porta 250 pezzi il 07/07/2026."), 0, 0),
    ("numero inventato nel corpo (il controllo di sempre)",
     dict(SANO, corpo="Il corpo dichiara 91919 pezzi."), 1, 0),
    ("lo stesso numero nel corpo E nell'intestazione: un rilievo solo",
     dict(SANO, corpo="Il corpo dichiara 91919 pezzi.",
          summary="Anche il summary dichiara 91919 pezzi."), 1, 0),
    ("valore derivato e marcato nel `summary` (E23)",
     dict(SANO, summary="In tutto 500 pezzi (calcolato: 250 + 250)."), 0, 0),
]

TOKEN = ("91919", "91.919", "14/03/2026", "500")


def cita_il_token(messaggio):
    return any(t in messaggio for t in TOKEN)


def main():
    tmp = tempfile.mkdtemp(prefix="collaudo_intestazione_")
    esiti = []
    sources_vero, sources_ec = Q.SOURCES, EC.Q.SOURCES
    try:
        os.makedirs(os.path.join(tmp, "areas"))
        os.makedirs(os.path.join(tmp, "sources"))
        with io.open(os.path.join(tmp, "sources", "x.csv"), "w", encoding="utf-8") as f:
            f.write(FONTE)
        Q.SOURCES = os.path.join(tmp, "sources")
        EC.Q.SOURCES = Q.SOURCES

        for i, (_nome, dati, _e, _a) in enumerate(CASI, 1):
            p = os.path.join(tmp, "areas", "caso-%d.md" % i)
            with io.open(p, "w", encoding="utf-8") as f:
                f.write(NOTA % dati)

        for i, (nome, _dati, att_err, att_avv) in enumerate(CASI, 1):
            n = Q.Nota(os.path.join(tmp, "areas", "caso-%d.md" % i))
            rep = Q.Report("collaudo")
            P.controlla(n, rep, {})
            err = len([v for v in rep.errori if cita_il_token(v[4])])
            avv = len([v for v in rep.avvisi if cita_il_token(v[4])])
            ok = (err == att_err) and (avv == att_avv)
            esiti.append((i, nome, att_err, att_avv, err, avv, ok))
    finally:
        Q.SOURCES, EC.Q.SOURCES = sources_vero, sources_ec
        shutil.rmtree(tmp, ignore_errors=True)

    print("=" * 82)
    print("COLLAUDO - l'affermazione inventata in `title`/`summary` deve scattare")
    print("=" * 82)
    print("| # | Caso | Attesi E/A | Avuti E/A | Esito |")
    print("|---|---|---|---|---|")
    for i, nome, ae, aa, e, a, ok in esiti:
        print("| %d | %s | %d/%d | %d/%d | %s |"
              % (i, nome, ae, aa, e, a, "OK" if ok else "FALLITO"))
    falliti = [x for x in esiti if not x[6]]
    if falliti:
        print("\nCOLLAUDO FALLITO - %d casi su %d" % (len(falliti), len(esiti)))
        return 1
    print("\nCOLLAUDO SUPERATO - %d casi su %d, nei due versi." % (len(esiti), len(esiti)))
    print("Il caso 1 e' il difetto piantato; il 5 e l'8 provano che il controllo non e'")
    print("diventato un generatore di rumore, e il 4 che il pregresso resta debito (§4.35).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
