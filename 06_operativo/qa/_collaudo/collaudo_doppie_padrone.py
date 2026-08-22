# -*- coding: utf-8 -*-
"""collaudo_doppie_padrone — il controllo scatta sul fatto condiviso, non sui decimali comuni.

⚠️ **PERIMETRO CHIUSO.** Non guarda il vault vero: costruisce note finte in una cartella
temporanea e verifica il solo predicato che decide se due note siano doppie padrone.

PERCHE' ESISTE.
Il gate del lotto 2A lascio' rosso un rilievo di doppia padrona «finche' non avra' il suo
turno». Col lotto 3A e' passato da **1 a 4**, tutti contro la stessa nota — una tabella di
dieci indicatori per cinque mesi, che porta **cinquanta decimali piccoli in una nota sola**
— e i valori «in comune» erano `0,8 · 0,9 · 1,1 · 1,4 · 6,1`, numeri di sfondo di questo
archivio.

⚠️ **E' il primo caso in cui canonizzare un lotto AUMENTA il debito dichiarato**, e un
controllo il cui rosso cresce col lavoro fatto bene e' un controllo che verra' ignorato
(§4.35, stessa logica).

IL FIX ALLENTA, quindi §4.9 alla lettera: perimetro chiuso e difetti piantati **nei due
versi**. Le due condizioni aggiunte sono entrambe necessarie:

  1. **fonte condivisa** — due note sono padrone dello stesso fatto solo se il fatto viene
     dallo stesso grezzo;
  2. **valori identificanti** — almeno tre cifre significative: `0,9` non identifica nulla.

⚠️ **Nessuna delle due basta da sola**, e i casi qui sotto lo esercitano: senza la prima
scattano due note dello stesso lotto che condividono tre decimali di sfondo (il caso
frequente); senza la seconda scattano due note di lotti diversi che nominano lo stesso
importo per ragioni scollegate.

Uso:
    python collaudo_doppie_padrone.py
Esce 0 se tutti i casi passano, 1 altrimenti.
"""
import io, os, shutil, subprocess, sys, tempfile

QUI = os.path.dirname(os.path.abspath(__file__))
QA = os.path.dirname(QUI)
sys.path.insert(0, QA)

NOTA = """\
---
title: "%s"
summary: "Nota di collaudo del controllo sulle doppie padrone, con i valori indicati nel proprio nome."
type: atomica
area: qualita
tags: [areas, qualita, collaudo]
fonti:
%s
stato: risolto
aliases: []
data_nota: 2026-08-22
related: "[[area-qualita]]"
---

# %s

I valori che questa nota afferma sono %s.

## Fonti
%s
"""

HUB = """\
---
title: "Qualita' — hub di collaudo"
summary: "Hub minimo per il collaudo del controllo sulle doppie padrone."
type: hub
area: qualita
tags: [areas, qualita]
stato: risolto
aliases: []
data_nota: 2026-08-22
related: "[[_index-areas]]"
---

# Qualita'

Hub di collaudo.
"""

INDEX = """\
---
title: "Indice di areas"
summary: "Indice di collaudo."
type: index
area: qualita
tags: [areas]
data_nota: 2026-08-22
related: "[[area-qualita]]"
---

# Indice

- [[area-qualita]]
"""


def scrivi(cartella, slug, titolo, valori, fonti):
    p = os.path.join(cartella, "areas", slug + ".md")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    elenco = "\n".join("  - " + f for f in fonti)
    blocco = "\n".join("- [[%s]] — riferimento di collaudo." % f for f in fonti)
    with io.open(p, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(NOTA % (titolo, elenco, titolo, ", ".join(valori), blocco))


LOG = "log_temperature_pastorizzatore_linea1_10_05_26.log"
OEE = "calcolo_sfrido_efficienza_OEE_linea_bakery.csv"

CASI = [
    ("DOPPIA PADRONA VERA: stessa fonte, tre valori identificanti, nessun link",
     [("collaudo-dp-uno", ["68,9", "5.580", "5.250"], [LOG]),
      ("collaudo-dp-due", ["68,9", "5.580", "5.250"], [LOG])],
     True),
    ("decimali di sfondo condivisi, stessa fonte: NON deve scattare",
     [("collaudo-dp-tre", ["0,8", "0,9", "1,1", "1,4"], [LOG]),
      ("collaudo-dp-quattro", ["0,8", "0,9", "1,1", "1,4"], [LOG])],
     False),
    ("tre valori identificanti ma FONTI DISGIUNTE: non deve scattare",
     [("collaudo-dp-cinque", ["68,9", "5.580", "5.250"], [LOG]),
      ("collaudo-dp-sei", ["68,9", "5.580", "5.250"], [OEE])],
     False),
]


def gira(cartella):
    """Lancia qa_copertura sul vault finto e ritorna le righe di doppia padrona."""
    out = subprocess.run(
        [sys.executable, os.path.join(QA, "qa_copertura.py"), "--perimetro", "vault",
         "--vault", cartella],
        capture_output=True, text=True, encoding="utf-8", cwd=QA).stdout
    return [r for r in out.splitlines() if "doppia padrona" in r]


def main():
    print("=" * 74)
    print("IL CONTROLLO SCATTA SUL FATTO CONDIVISO, NON SUI DECIMALI COMUNI")
    print("=" * 74)
    esiti = []
    for etichetta, note, atteso in CASI:
        tmp = tempfile.mkdtemp(prefix="collaudo_dp_")
        try:
            os.makedirs(os.path.join(tmp, "areas"), exist_ok=True)
            io.open(os.path.join(tmp, "areas", "area-qualita.md"), "w",
                    encoding="utf-8", newline="\n").write(HUB)
            io.open(os.path.join(tmp, "areas", "_index-areas.md"), "w",
                    encoding="utf-8", newline="\n").write(INDEX)
            for slug, valori, fonti in note:
                scrivi(tmp, slug, slug, valori, fonti)
            righe = gira(tmp)
            scattato = bool(righe)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        ok = (scattato == atteso)
        esiti.append(ok)
        print("%-62s %-9s %s"
              % (etichetta[:62], "scatta" if scattato else "tace",
                 "ok" if ok else "*** FALLITO"))

    print()
    if all(esiti):
        print("COLLAUDO SUPERATO — %d casi su %d, nei due versi." % (len(esiti), len(esiti)))
        print("Il controllo vede la doppia padrona vera e non i decimali di sfondo.")
        return 0
    print("COLLAUDO FALLITO: il fix ha allentato piu' di quanto doveva, o meno.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
