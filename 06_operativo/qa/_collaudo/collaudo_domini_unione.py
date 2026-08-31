# -*- coding: utf-8 -*-
r"""collaudo_domini_unione — il perimetro di piu' domini e' la loro UNIONE, non l'ultimo.

=====================================================================================
PERCHE' QUESTO COLLAUDO ESISTE — IL GUASTO TROVATO ALL'APERTURA DI R2
=====================================================================================
`R2` e' il lotto di manutenzione che copre DUE domini, `reclami` e `ritiro`, e il suo elenco
prescriveva di rigenerare il perimetro con **due invocazioni successive sullo stesso `--lotto`**:

    python candidate_r1.py --dominio reclami --lotto r2_reclami_verticale
    python candidate_r1.py --dominio ritiro  --lotto r2_reclami_verticale

⛔ **`candidate_r1.py` scrive l'elenco con `"w"`: la seconda invocazione CANCELLA la prima.**
Il perimetro risultante sarebbe stato quello del **solo `ritiro`** — 31 note invece delle 102
dell'unione — e **il file sarebbe apparso perfettamente corretto**: intestazione giusta,
criterio giusto, note vere. Un dominio intero sparito in silenzio.

⚠️ **E' la specie di §4.47**: una procedura che *sembra* comporre e invece sovrascrive. Non
c'e' errore, non c'e' avviso, e a valle nessuno puo' accorgersene — perche' 31 note sono un
perimetro plausibile quanto 102.

=====================================================================================
CHE COSA IL FIX CAMBIA, E CHE COSA NO
=====================================================================================
`--dominio` accetta ora **piu' valori in una invocazione sola**, e il perimetro e' l'**unione**:
una nota entra se e' **scoperta per almeno uno** dei domini. ⚠️ **Le due condizioni di E37+E36
valgono dominio per dominio e non si mescolano**: una nota che parla di `reclami` citando
`PRO-QA-08` e parla anche di `ritiro` senza citare `PRO-QA-14` **e' scoperta**, e nel perimetro
ci sta — per il secondo dominio, non per il primo.

⚠️ **Con un dominio solo il comportamento e' identico a prima**, ed e' il caso 4.

=====================================================================================
I CASI
=====================================================================================
| # | Caso | Atteso |
|---|---|---|
| 1 | **LA PREMESSA**: i due domini hanno perimetri diversi, e nessuno contiene l'altro | diversi |
| 2 | **IL DIFETTO PIANTATO**: due invocazioni successive sullo stesso `--lotto` | resta **solo il secondo** |
| 3 | l'invocazione unica coi due domini | l'**UNIONE** |
| 4 | **non-scatto di regressione**: un dominio solo | il perimetro di quel dominio, invariato |
| 5 | l'unione **non e' la somma**: `|A∪B| = |A|+|B|-|A∩B|`, con intersezione non vuota | l'identita' regge |

⚠️ **Il caso 1 e' quello che rende gli altri qualcosa di piu' di una tautologia**: se un
dominio fosse contenuto nell'altro, il caso 2 passerebbe per il motivo sbagliato — il difetto
non si vedrebbe, perche' sovrascrivere darebbe lo stesso insieme dell'unione.

Uso:
    python collaudo_domini_unione.py
Esce 0 se tutti i casi passano, 1 altrimenti.
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile

QUI = os.path.dirname(os.path.abspath(__file__))
QA = os.path.normpath(os.path.join(QUI, os.pardir))
OPERATIVO = os.path.normpath(os.path.join(QA, os.pardir))
SCRIPT = os.path.join(OPERATIVO, "candidate_r1.py")
DIR_LOTTI = os.path.join(QA, "lotti")

A, B = "reclami", "ritiro"
PREFISSO = "_collaudo_unione"


def genera(slug, domini):
    """Chiama la via DI PRODUZIONE. Nessuna logica di selezione e' reimplementata qui."""
    cmd = [sys.executable, SCRIPT, "--lotto", slug, "--dominio"] + list(domini)
    subprocess.run(cmd, cwd=OPERATIVO, capture_output=True)
    return leggi(slug)


def leggi(slug):
    p = os.path.join(DIR_LOTTI, slug + "_note.txt")
    if not os.path.isfile(p):
        return set()
    return {r.strip() for r in io.open(p, encoding="utf-8")
            if r.strip() and not r.strip().startswith("#")}


def pulisci():
    for f in os.listdir(DIR_LOTTI):
        if f.startswith(PREFISSO):
            os.remove(os.path.join(DIR_LOTTI, f))


def main():
    esiti = []
    try:
        sa = genera(PREFISSO + "_a", [A])
        sb = genera(PREFISSO + "_b", [B])

        # --- 1. LA PREMESSA ---------------------------------------------------------
        ok1 = bool(sa) and bool(sb) and not (sa <= sb) and not (sb <= sa)
        esiti.append((1, u"LA PREMESSA: i due domini hanno perimetri diversi, nessuno contiene l'altro",
                      u"diversi", u"%s (%d e %d, comuni %d)"
                      % ("diversi" if ok1 else "contenuti", len(sa), len(sb), len(sa & sb)), ok1))

        # --- 2. IL DIFETTO PIANTATO: due invocazioni sullo stesso lotto -------------
        genera(PREFISSO + "_seq", [A])
        seq = genera(PREFISSO + "_seq", [B])
        ok2 = (seq == sb) and (seq != (sa | sb))
        esiti.append((2, u"IL DIFETTO PIANTATO: due invocazioni successive sullo stesso --lotto",
                      u"resta solo il secondo (%d)" % len(sb), u"%d note" % len(seq), ok2))

        # --- 3. l'invocazione unica ------------------------------------------------
        uni = genera(PREFISSO + "_uni", [A, B])
        ok3 = uni == (sa | sb)
        esiti.append((3, u"l'invocazione unica coi due domini da' l'UNIONE",
                      u"%d note" % len(sa | sb), u"%d note" % len(uni), ok3))

        # --- 4. non-scatto di regressione ------------------------------------------
        rig = genera(PREFISSO + "_reg", [A])
        ok4 = rig == sa
        esiti.append((4, u"non-scatto di regressione: un dominio solo, perimetro invariato",
                      u"%d note" % len(sa), u"%d note" % len(rig), ok4))

        # --- 5. l'unione non e' la somma -------------------------------------------
        comuni = len(sa & sb)
        ok5 = comuni > 0 and len(uni) == len(sa) + len(sb) - comuni
        esiti.append((5, u"l'unione non e' la somma: |A u B| = |A|+|B|-|A n B|",
                      u"%d = %d+%d-%d" % (len(sa) + len(sb) - comuni, len(sa), len(sb), comuni),
                      u"%d" % len(uni), ok5))
    finally:
        pulisci()

    print("=" * 96)
    print("COLLAUDO - il perimetro di piu' domini e' la loro UNIONE, non l'ultimo scritto")
    print("=" * 96)
    print("| # | Caso | Atteso | Avuto | Esito |")
    print("|---|---|---|---|---|")
    for i, nome, att, avu, ok in esiti:
        print("| %d | %s | %s | %s | %s |" % (i, nome, att, avu, "OK" if ok else "FALLITO"))
    falliti = [x for x in esiti if not x[4]]
    if falliti:
        print("\nCOLLAUDO FALLITO - %d casi su %d" % (len(falliti), len(esiti)))
        return 1
    print("\nCOLLAUDO SUPERATO - %d casi su %d." % (len(esiti), len(esiti)))
    print("Il caso 1 e' la premessa senza la quale il 2 passerebbe per il motivo sbagliato;")
    print("il 2 e' il difetto piantato - la via vecchia, che sovrascrive; il 4 prova che un")
    print("dominio solo non si e' mosso, e il 5 che l'unione e' un'unione e non una somma.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
