# -*- coding: utf-8 -*-
r"""collaudo_assenza_fuori_formula — un'assenza dichiarata SENZA la formula deve scattare (E43).

=====================================================================================
PERCHE' QUESTO COLLAUDO ESISTE
=====================================================================================
Fino al 24/08/2026 il controllo di E43 in `qa_frontmatter.py` cercava LA FORMULA di
attestazione — «assenza verificata su tutto `sources\`» — e da li' risaliva all'artefatto
della ricerca. ⚠️ **Un'assenza scritta in prosa, dentro un elenco di «cosa servirebbe per
chiuderla», non la vedeva nessuno.**

⚠️ **Il caso, ed e' E3 pagato per la QUINTA volta in sette lotti**:
`questione-data-apertura-rec-2026-011`, scritta il 19/08, elencava fra le cose che sarebbero
servite per chiuderla «la mail automatica di notifica della segnalazione, **che l'archivio non
contiene**». **L'archivio la contiene, ed e' il primo grezzo del lotto 3D** (T161).

**LA SUPERFICIE IN CUI UN'ASSENZA SI NASCONDE E' PIU' LARGA DELLA FORMULA CHE LA DICHIARA.**
Il controllo ha quindi acquistato, al gate del lotto 3D, il **riconoscitore della classe
`assenza`** che `qa_comune` definisce e che `censimento_superlativi.py` usa per contare la
classe in T142: quantificatore piu' termine di perimetro dentro la finestra, in esistenziale
negativo. **Una definizione sola, due chiamanti** — se il controllo ne avesse una propria, il
progetto conterebbe una classe e ne fermerebbe un'altra.

=====================================================================================
CHE COSA IL FIX CAMBIA, E CHE COSA NO
=====================================================================================
⚠️ **Cambia l'AGGANCIO, non il requisito.** Il requisito resta quello di E43 — chi dichiara
un'assenza lascia l'artefatto della ricerca — e adesso l'assenza si riconosce per due vie che
non si sostituiscono: la formula, e la classe. E' un fix che **AGGIUNGE agganci** (§4.9), e
per questo il caso 3 e i casi 6-10 contano quanto il difetto piantato: un aggancio nuovo che
scatta anche dove non deve e' rumore, e **un controllo che fa rumore viene disattivato**.

⚠️ **Il pregresso resta debito e non diventa rosso** (§4.35, come per E43 il 20/08 e per la
superficie dell'intestazione il 23/08): ERRORE per le note nate dal **24/08/2026**, AVVISO
dichiarato per le altre. Il conteggio del pregresso sta nella sua riga di tracciamento.

⚠️ **Il collaudo chiama `qa_frontmatter.controlla_artefatto_assenza`, cioe' LA VIA CHE LA
PRODUZIONE USA** — la funzione che `controlla` invoca su ogni nota — non una copia della sua
logica: e' §4.29.

=====================================================================================
I CASI, NEI DUE VERSI
=====================================================================================
| # | Caso | Atteso |
|---|---|---|
| 1 | assenza in prosa, **fuori dalla formula**, nota nata sotto la regola, nessun artefatto — **IL DIFETTO PIANTATO** | **ERRORE** |
| 2 | la stessa assenza in una nota **anteriore** al 24/08/2026 | **AVVISO** col debito (§4.35), mai errore |
| 3 | assenza fuori dalla formula, ma con **rimando a un artefatto che esiste** | **tace** |
| 4 | assenza fuori dalla formula, con rimando a un artefatto che **non esiste** | **ERRORE** |
| 5 | **la formula** di E3 senza artefatto — il controllo di sempre, che non deve essersi rotto | **ERRORE** |
| 6 | **superlativo affermativo** sull'archivio: e' la classe di E57, non questa | **tace** |
| 7 | perimetro **ristretto per iscritto** («in nessun altro documento di questo lotto») | **tace** |
| 8 | omonimia: l'**archivio cartaceo** di Aurora, che col vault non c'entra | **tace** |
| 9 | **nota-strumento** del progetto (E20): parla degli attrezzi, non di Aurora | **tace** |
| 10 | nota pulita, nessuna assenza | **tace** |

Uso:
    python collaudo_assenza_fuori_formula.py
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
import qa_frontmatter as F     # noqa: E402

NOTA = """---
title: "Nota di collaudo"
summary: "Una frase sola, senza assenze dichiarate."
type: %(type)s
area: qualita
tags: [areas, qualita]
fonti:
  - x.csv
stato: aperto
aliases: []
data_nota: %(data)s
related: "[[_index-areas]]"
---

# Nota di collaudo

%(corpo)s

## Fonti

- [[x.csv]] - riga 2.
"""

OGGI = "2026-08-24"       # nata SOTTO la regola
IERI = "2026-08-21"       # nata PRIMA della regola

ARTEFATTO_VERO = "prova-di-collaudo_2026-08-24.md"
ARTEFATTO_FINTO = "questo-artefatto-non-esiste_2026-08-24.md"

# ⚠️ Le frasi sono scritte per esercitare il riconoscitore di `qa_comune`, non per somigliare
# a una nota vera: quantificatore e termine di perimetro devono stare nella stessa finestra.
ASSENZA = ("Il termine non compare da nessuna parte: **nessun documento dell'archivio** lo\n"
           "riporta, e la pratica resta aperta.")

CASI = [
    ("difetto piantato: assenza in prosa, fuori dalla formula, senza artefatto",
     dict(corpo=ASSENZA, data=OGGI, type="atomica", cartella="areas"), 1, 0),
    ("la stessa assenza in una nota ANTERIORE al 24/08/2026",
     dict(corpo=ASSENZA, data=IERI, type="atomica", cartella="areas"), 0, 1),
    ("assenza fuori dalla formula, con rimando a un artefatto che ESISTE",
     dict(corpo=ASSENZA + "\n\nRicerca depositata in\n`06_operativo\\ricerche_assenza\\"
          + ARTEFATTO_VERO + "`.", data=OGGI, type="atomica", cartella="areas"), 0, 0),
    ("assenza fuori dalla formula, con rimando a un artefatto che NON esiste",
     dict(corpo=ASSENZA + "\n\nRicerca depositata in\n`06_operativo\\ricerche_assenza\\"
          + ARTEFATTO_FINTO + "`.", data=OGGI, type="atomica", cartella="areas"), 1, 0),
    ("la FORMULA di E3 senza artefatto: il controllo di sempre",
     dict(corpo="Il dato non c'e': **assenza verificata** su tutto sources, manifest v1.1.",
          data=OGGI, type="atomica", cartella="areas"), 1, 0),
    ("superlativo AFFERMATIVO sull'archivio: e' la classe di E57, non questa",
     dict(corpo="E' l'unica registrazione continua di quel valore nell'archivio.",
          data=OGGI, type="atomica", cartella="areas"), 0, 0),
    ("perimetro RISTRETTO per iscritto: «di questo lotto»",
     dict(corpo="Il codice non compare in nessun altro documento di questo lotto.",
          data=OGGI, type="atomica", cartella="areas"), 0, 0),
    ("omonimia: l'archivio CARTACEO di Aurora, che col vault non c'entra",
     dict(corpo="Nessun documento dell'archivio cartaceo di stabilimento lo riporta.",
          data=OGGI, type="atomica", cartella="areas"), 0, 0),
    ("nota-strumento del progetto (E20): parla degli attrezzi, non di Aurora",
     dict(corpo=ASSENZA, data=OGGI, type="atomica", cartella="code"), 0, 0),
    ("nota pulita, nessuna assenza dichiarata",
     dict(corpo="La fonte porta 250 pezzi il 07/07/2026, e la nota si ferma li'.",
          data=OGGI, type="atomica", cartella="areas"), 0, 0),
]


def main():
    tmp = tempfile.mkdtemp(prefix="collaudo_assenza_")
    dir_vera = F.DIR_RICERCHE
    esiti = []
    try:
        ricerche = os.path.join(tmp, "ricerche_assenza")
        os.makedirs(ricerche)
        with io.open(os.path.join(ricerche, ARTEFATTO_VERO), "w", encoding="utf-8") as f:
            f.write("# artefatto di collaudo\n")
        F.DIR_RICERCHE = ricerche

        for i, (_nome, dati, _e, _a) in enumerate(CASI, 1):
            # ⚠️ La nota-strumento e' definita dal PREFISSO `script-` DENTRO `code\` (E20):
            # servono tutti e due, ed e' per questo che il caso 9 cambia anche cartella.
            cartella = os.path.join(tmp, dati["cartella"])
            if not os.path.isdir(cartella):
                os.makedirs(cartella)
            prefisso = "script-" if dati["cartella"] == "code" else "caso-"
            p = os.path.join(cartella, "%scaso-%d.md" % (prefisso, i))
            with io.open(p, "w", encoding="utf-8") as f:
                f.write(NOTA % dati)
            dati["percorso"] = p

        for i, (nome, dati, att_err, att_avv) in enumerate(CASI, 1):
            n = Q.Nota(dati["percorso"])
            rep = Q.Report("collaudo")
            F.controlla_artefatto_assenza(n, rep)
            esiti.append((i, nome, att_err, att_avv, len(rep.errori), len(rep.avvisi),
                          len(rep.errori) == att_err and len(rep.avvisi) == att_avv))
    finally:
        F.DIR_RICERCHE = dir_vera
        shutil.rmtree(tmp, ignore_errors=True)

    print("=" * 88)
    print("COLLAUDO - l'assenza dichiarata FUORI dalla formula di attestazione deve scattare")
    print("=" * 88)
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
    print("Il caso 1 e' il difetto piantato e il 4 il suo gemello; il 2 prova che il pregresso")
    print("resta debito (§4.35); il 5 che l'aggancio vecchio non si e' rotto; i casi 6-10 che")
    print("l'aggancio nuovo NON scatta dove non deve - ed e' la meta' che decide se un")
    print("controllo sopravvive, perche' un controllo che fa rumore viene disattivato.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
