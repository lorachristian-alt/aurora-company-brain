# -*- coding: utf-8 -*-
r"""collaudo_lotti_chiusi — «lotti chiusi: N» si legge dal marcatore, e il marcatore non e' un prefisso.

=====================================================================================
PERCHE' QUESTO COLLAUDO ESISTE
=====================================================================================
Il numero dei lotti chiusi era **l'ultimo del progetto composto a mano**: viveva nei prompt
del coordinatore e nella §3 del passaggio di consegne, e il 23/08/2026 e' uscito sbagliato —
«undici» dove i marcatori `# CHIUSO` erano **dieci**. ⚠️ **La malattia che il progetto cura
con gli script, ricomparsa al livello che dovrebbe controllarla** (§4.47).

Il gate del lotto 3B ha deciso la risposta strutturale: il numero lo stampa
`verifica_matrice_lotti.py`, e da li' si **incolla**.

⚠️ **E IL PRIMO RICONOSCIMENTO DEL MARCATORE ERA GIA' SBAGLIATO, SCRITTO LO STESSO GIORNO.**
Faceva `startswith("MANUTENZIONE")` sulla riga di commento ripulita, e l'elenco del lotto
**1B** — un lotto di **canonizzazione** — risultava di manutenzione per via di una riga che va
a capo su «*manutenzione* mai firmato». **Un conteggio nato per togliere l'aritmetica dalle
mani di qualcuno sbagliava alla prima misura**, ed era la stessa specie che stava riparando:
un riscontro **debole** preso per forte (E56, le due classi di forza).

**Da qui l'esistenza di questo collaudo:** il marcatore e' un marcatore, non una parola che
capita a inizio riga.

=====================================================================================
LA FORMA DEI DUE MARCATORI, E CHI LA IMPONE
=====================================================================================
| Marcatore | Chi lo impone | Forma ammessa |
|---|---|---|
| `# CHIUSO <data>` | §2 del prompt dei lotti, adempimento di chiusura | `CHIUSO il 23/08/2026 - …` · `CHIUSO 2026-08-19` |
| `# MANUTENZIONE` | §3-bis (E35), in testa e **da solo** | `MANUTENZIONE` · `MANUTENZIONE — nota di coda` |

=====================================================================================
I CASI
=====================================================================================
| # | Caso | Atteso |
|---|---|---|
| 1 | `# CHIUSO il 23/08/2026 - lotto canonizzato` | **chiuso** |
| 2 | `# CHIUSO 2026-08-19` *(l'altra grafia in uso)* | **chiuso** |
| 3 | **IL DIFETTO PIANTATO**: una riga di prosa che va a capo su «manutenzione mai firmato» | **NON** manutenzione |
| 4 | **IL DIFETTO PIANTATO, secondo verso**: prosa che va a capo su «chiuso il contratto» | **NON** chiuso |
| 5 | `# MANUTENZIONE` da solo | **manutenzione** |
| 6 | `# MANUTENZIONE — riverifica del barrato (E35)` | **manutenzione** |
| 7 | elenco senza marcatori | **ne' chiuso ne' manutenzione** |
| 8 | il conteggio sugli elenchi VERI: `lotti chiusi` = elenchi col marcatore, **pilota escluso** | **coincide** |

Uso:
    python collaudo_lotti_chiusi.py
Esce 0 se tutti i casi passano, 1 altrimenti.
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile

QUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(QUI, os.pardir, os.pardir))
sys.path.insert(0, REPO)

import verifica_matrice_lotti as V  # noqa: E402


TESTA = [
    ("`# CHIUSO <data>` nella grafia lunga",
     "# CHIUSO il 23/08/2026 - lotto canonizzato: i suoi grezzi sono citati dalle note\n"
     "# Lotto finto per il collaudo.\ngrezzo_finto.txt\n",
     True, False),
    ("`# CHIUSO <data>` nella grafia corta",
     "# CHIUSO 2026-08-19\n# MANUTENZIONE\n",
     True, True),
    ("difetto piantato: prosa che va a capo su «manutenzione mai firmato»",
     "# CHIUSO il 19/08/2026 - lotto canonizzato\n"
     "# Il contratto di\n# manutenzione mai firmato sono lo stesso fatto.\ngrezzo_finto.txt\n",
     True, False),
    ("difetto piantato, secondo verso: prosa che va a capo su «chiuso il contratto»",
     "# Lotto finto, ancora aperto.\n# Nel 2025 hanno\n# chiuso il contratto con il fornitore.\n"
     "grezzo_finto.txt\n",
     False, False),
    ("`# MANUTENZIONE` da solo",
     "# CHIUSO 2026-08-19\n# MANUTENZIONE\n# Perimetro di sole note.\n",
     True, True),
    ("`# MANUTENZIONE` con la coda dopo il trattino lungo",
     "# MANUTENZIONE — riverifica del barrato (E35): il perimetro sono le note\n",
     False, True),
    ("elenco senza marcatori",
     "# Lotto finto, ancora da aprire.\ngrezzo_finto.txt\n",
     False, False),
]


def main():
    esiti = []
    tmp = tempfile.mkdtemp(prefix="collaudo_lotti_chiusi_")
    try:
        for i, (nome, testo, att_chiuso, att_manut) in enumerate(TESTA, 1):
            p = os.path.join(tmp, "caso-%d.txt" % i)
            with io.open(p, "w", encoding="utf-8") as f:
                f.write(testo)
            _voci, chiuso, manut = V.leggi(p)
            ok = (chiuso == att_chiuso) and (manut == att_manut)
            esiti.append((i, nome, att_chiuso, att_manut, chiuso, manut, ok))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # --- caso 8: il conteggio vero, contro gli elenchi veri --------------------------
    # ⚠️ Si lancia lo SCRIPT, non se ne rifa' la logica: e' §4.29 — il collaudo esercita la
    # via che la produzione usa. Chi legge «lotti chiusi: N» legge questa riga, non un'altra.
    uscita = subprocess.run([sys.executable, os.path.join(REPO, "verifica_matrice_lotti.py")],
                            capture_output=True, text=True, encoding="utf-8", errors="replace")
    riga = [r for r in (uscita.stdout or "").splitlines() if r.startswith("lotti chiusi:")]
    stampato = int(riga[0].split(":")[1]) if riga else -1

    dir_lotti = os.path.join(REPO, "qa", "lotti")
    atteso = 0
    for n in sorted(os.listdir(dir_lotti)):
        if not n.lower().endswith(".txt") or n.lower().endswith("_note.txt"):
            continue
        _v, chiuso, _m = V.leggi(os.path.join(dir_lotti, n))
        if chiuso:
            atteso += 1
    ok8 = (stampato == atteso) and stampato > 0
    esiti.append((8, "il conteggio stampato coincide con gli elenchi marcati, pilota escluso",
                  atteso, "-", stampato, "-", ok8))

    print("=" * 84)
    print("COLLAUDO - «lotti chiusi: N» si legge dal marcatore, e il marcatore non e' un prefisso")
    print("=" * 84)
    print("| # | Caso | Atteso chiuso/manut | Avuto chiuso/manut | Esito |")
    print("|---|---|---|---|---|")
    for i, nome, ac, am, c, m, ok in esiti:
        print("| %d | %s | %s/%s | %s/%s | %s |"
              % (i, nome, ac, am, c, m, "OK" if ok else "FALLITO"))
    falliti = [e for e in esiti if not e[6]]
    if falliti:
        print("\nCOLLAUDO FALLITO - %d casi su %d" % (len(falliti), len(esiti)))
        return 1
    print("\nCOLLAUDO SUPERATO - %d casi su %d, nei due versi." % (len(esiti), len(esiti)))
    print("I casi 3 e 4 sono i difetti piantati: senza di loro gli altri proverebbero solo")
    print("che il marcatore si trova quando c'e', non che NON si trova quando non c'e'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
