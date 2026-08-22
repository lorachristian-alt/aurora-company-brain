# -*- coding: utf-8 -*-
"""collaudo_locator_eml — la grammatica dei locator .eml conosce la CATENA, e non si e' aperta.

⚠️ **PERIMETRO CHIUSO.** Non guarda il vault vero: costruisce note finte in una cartella
temporanea e verifica il solo controllo di grammatica del locator.

PERCHE' ESISTE.
E55 (22/08/2026, lotto 3C) allarga la grammatica del `.eml`: un file puo' essere una CATENA
di messaggi quotati uno dentro l'altro, e allora «corpo, punto 1)» indica quattro punti
diversi nello stesso file. La forma lunga nomina prima QUALE messaggio, con la sua data.

⚠️ **E' un fix che ALLENTA un controllo**, quindi §4.9 alla lettera: perimetro chiuso e
difetti piantati **nei due versi**. Allentare senza collaudo e' il modo in cui una grammatica
chiusa diventa, un emendamento alla volta, una grammatica che accetta tutto — e a quel punto
il controllo non dice piu' niente e nessuno se ne accorge, perche' tace.

I TRE CASI, e ciascuno guarda un verso diverso:

  1. la forma NUOVA su una catena ................ non deve scattare (e' cio' che E55 ammette)
  2. la forma BREVE, di sempre .................... non deve scattare (E55 non la revoca)
  3. una forma FUORI da entrambe .................. **deve** scattare

⚠️ Il terzo e' il difetto piantato, ed e' quello che conta: dice che la grammatica e' ancora
chiusa DOPO l'allargamento. Senza di lui i primi due proverebbero soltanto che il controllo
e' stato spento.

Uso:
    python collaudo_locator_eml.py
Esce 0 se tutti i casi passano, 1 altrimenti.
"""
import io, os, shutil, subprocess, sys, tempfile

QUI = os.path.dirname(os.path.abspath(__file__))
QA = os.path.dirname(QUI)
sys.path.insert(0, QA)

EML = "R_R_R_scadenza_certificato_BRCGS_e_audit_di_rinnovo.eml"

NOTA = """\
---
title: "Nota di collaudo della grammatica dei locator .eml"
summary: "Nota costruita per il collaudo del controllo di grammatica sul locator di un file .eml a catena."
type: atomica
area: qualita
tags: [areas, qualita, collaudo]
fonti:
  - %s
stato: risolto
aliases: []
data_nota: 2026-08-22
related: "[[area-qualita]]"
---

# Nota di collaudo

Il corpo non conta per questo controllo: conta la forma del locator qui sotto.

## Fonti

- [[%s]] — %s
"""

HUB = """\
---
title: "Qualita' — hub di collaudo"
summary: "Hub minimo per il collaudo della grammatica dei locator."
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

CASI = [
    ("E55: 'corpo del messaggio del 07/04, ...' su una catena",
     "corpo del messaggio del 07/04, «Cordiali saluti».", False),
    ("la forma breve di sempre: 'corpo, punto 1)'",
     "corpo, punto 1) «Cordiali saluti».", False),
    ("fuori da entrambe: 'messaggio del 7 aprile'",
     "messaggio del 7 aprile, «Cordiali saluti».", True),
]


def gira(cartella):
    """Lancia qa_frontmatter sul vault finto e ritorna le righe di grammatica del locator."""
    out = subprocess.run(
        [sys.executable, os.path.join(QA, "qa_frontmatter.py"), "--perimetro", "vault",
         "--vault", cartella],
        capture_output=True, text=True, encoding="utf-8", cwd=QA).stdout
    return [r for r in out.splitlines() if "locator fuori grammatica" in r]


def main():
    print("=" * 74)
    print("LA GRAMMATICA DEI LOCATOR .eml CONOSCE LA CATENA, E NON SI E' APERTA")
    print("=" * 74)
    esiti = []
    for etichetta, locator, atteso in CASI:
        tmp = tempfile.mkdtemp(prefix="collaudo_eml_")
        try:
            os.makedirs(os.path.join(tmp, "areas"), exist_ok=True)
            io.open(os.path.join(tmp, "areas", "area-qualita.md"), "w",
                    encoding="utf-8", newline="\n").write(HUB)
            io.open(os.path.join(tmp, "areas", "_index-areas.md"), "w",
                    encoding="utf-8", newline="\n").write(INDEX)
            io.open(os.path.join(tmp, "areas", "collaudo-eml.md"), "w",
                    encoding="utf-8", newline="\n").write(NOTA % (EML, EML, locator))
            scattato = bool(gira(tmp))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        ok = (scattato == atteso)
        esiti.append(ok)
        print("%-58s %-9s %s"
              % (etichetta[:58], "scatta" if scattato else "tace",
                 "ok" if ok else "*** FALLITO"))

    print()
    if all(esiti):
        print("COLLAUDO SUPERATO - %d casi su %d, nei due versi." % (len(esiti), len(esiti)))
        print("La grammatica ha imparato la catena e non ha smesso di rifiutare il resto.")
        return 0
    print("COLLAUDO FALLITO: la grammatica si e' aperta piu' del dovuto, o meno.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
