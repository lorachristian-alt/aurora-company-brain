# -*- coding: utf-8 -*-
r"""collaudo_dominio_canonizzati — il fix di `verifica_dominio.CANONIZZATI`, nei due versi.

=====================================================================================
PERCHE' QUESTO COLLAUDO ESISTE
=====================================================================================
Fino al 23/08/2026 l'insieme dei lotti canonizzati era una **lista di nomi scritta a mano**
dentro `verifica_dominio.py`: una copia di un fatto il cui padrone e' altrove. Si e'
disallineata in silenzio, come ogni copia, e all'apertura del lotto 3B portava

- **un nome morto**, `lotto_02b_autocontrollo_igiene`, che dal 20/08 non corrisponde a nessun
  elenco: quando il lotto 2B si spezzo' in apertura, il file fu rinominato in `..._analitico`;
- e **non portava** `lotto_02b_autocontrollo_analitico`, `lotto_03c_certificazione_audit` ne'
  `r1_riconciliazione_verticale`, **tutti e tre CHIUSI**.

⚠️ **Il costo, se non fosse stato visto**: in apertura di 3B lo script dichiarava
`Certificato_BRCGS_Food_Issue9_Aurora_2026.pdf` NON CITABILE, il giorno dopo che 3C lo aveva
canonizzato. **Una fonte governante tenuta fuori dalla dichiarazione del dominio e' il verso
«troppo stretto» di E56**, che in 2B-bis e' costato un 9,1 % gonfiato.

Il fix legge l'insieme dal **marcatore `# CHIUSO`** in testa all'elenco del lotto: lo stesso
dato che `verifica_matrice_lotti.py` gia' pretende, che non puo' invecchiare separatamente.

=====================================================================================
PERCHE' SERVE UN DIFETTO PIANTATO, E QUAL E'
=====================================================================================
⚠️ **Il fix ALLENTA un controllo**: rende CITABILI fonti che prima erano rifiutate. Per
§4.9 del prompt dei lotti un fix cosi' si accetta **solo** con perimetro chiuso e un difetto
piantato NUOVO che dimostri che il buco non si apre.

**Il difetto piantato e' il caso 2**: un lotto **senza** `# CHIUSO` deve continuare a essere
rifiutato. Senza di lui, i casi 1 e 3 proverebbero soltanto che il controllo e' stato spento.

| # | Caso | Atteso |
|---|---|---|
| 1 | elenco **con** `# CHIUSO` in testa | **riconosciuto** come canonizzato |
| 2 | elenco **senza** `# CHIUSO` — **IL DIFETTO PIANTATO** | **rifiutato** |
| 3 | elenco `..._note.txt`, che non e' un lotto | **ignorato** |
| 4 | il **pilota**, che elenco non ne ha | **riconosciuto** per nome |
| 5 | `# CHIUSO` scritto in minuscolo o con spazi davanti | **riconosciuto** — il marcatore e' un fatto, non una calligrafia |

Uso:
    python collaudo_dominio_canonizzati.py
Esce 0 se tutti i casi passano, 1 altrimenti.
"""
import io
import os
import shutil
import sys
import tempfile

QUI = os.path.dirname(os.path.abspath(__file__))
OPERATIVO = os.path.normpath(os.path.join(QUI, os.pardir, os.pardir))
sys.path.insert(0, OPERATIVO)

import verifica_dominio as VD  # noqa: E402


CASI = [
    # (nome del file, prima riga, atteso, che cosa prova)
    ("lotto_zz_chiuso.txt",
     "# CHIUSO il 01/01/2026 - lotto canonizzato: i suoi grezzi sono citati dalle note\n",
     True,
     "un elenco chiuso viene riconosciuto"),
    ("lotto_zz_aperto.txt",
     "# Lotto ZZ - non ancora aperto: i suoi grezzi non stanno in nessuna nota\n",
     False,
     "DIFETTO PIANTATO: un lotto NON chiuso resta NON CITABILE"),
    ("lotto_zz_chiuso_note.txt",
     "# CHIUSO il 01/01/2026 - questo e' un elenco di NOTE, non di grezzi\n",
     None,
     "un `_note.txt` non e' un lotto e non entra nell'insieme"),
    ("lotto_zz_minuscolo.txt",
     "   # chiuso il 01/01/2026 - marcatore in minuscolo e rientrato\n",
     True,
     "il marcatore e' un fatto, non una calligrafia"),
]


def prova():
    """Costruisce una cartella di elenchi FINTA e ci fa girare la lettura del marcatore."""
    esiti = []
    tmp = tempfile.mkdtemp(prefix="collaudo_dominio_")
    vero = VD.DIR_LOTTI
    try:
        for nome, testa, _atteso, _perche in CASI:
            with io.open(os.path.join(tmp, nome), "w", encoding="utf-8") as fh:
                fh.write(testa)
                fh.write("un_grezzo_qualsiasi.txt\n")
        VD.DIR_LOTTI = tmp
        letti = VD.lotti_canonizzati()
    finally:
        VD.DIR_LOTTI = vero
        shutil.rmtree(tmp, ignore_errors=True)

    for nome, _testa, atteso, perche in CASI:
        etichetta = nome[:-4]
        dentro = etichetta in letti
        if atteso is None:
            ok = not dentro
            atteso_txt = "ignorato"
        else:
            ok = (dentro == atteso)
            atteso_txt = "riconosciuto" if atteso else "rifiutato"
        esiti.append((etichetta, atteso_txt, "dentro" if dentro else "fuori", ok, perche))

    # caso 5: il pilota, che un elenco non ce l'ha e sta nell'insieme per nome
    pilota = "pilota (fetta L26130)" in letti
    esiti.append(("pilota (fetta L26130)", "riconosciuto",
                  "dentro" if pilota else "fuori", pilota,
                  "il pilota e' anteriore alla matrice e non ha elenco"))
    return esiti


def prova_sul_vero():
    """Il controllo di realta': l'insieme letto dal disco vero non deve contenere nomi morti."""
    letti = VD.lotti_canonizzati()
    morti = []
    for x in letti:
        if x == "pilota (fetta L26130)":
            continue
        if not os.path.isfile(os.path.join(VD.DIR_LOTTI, x + ".txt")):
            morti.append(x)
    return morti


def main():
    print("=" * 74)
    print("COLLAUDO - `verifica_dominio.lotti_canonizzati()`, nei due versi")
    print("=" * 74)
    esiti = prova()
    print("| Caso | Atteso | Trovato | Esito | Che cosa prova |")
    print("|---|---|---|---|---|")
    for nome, atteso, trovato, ok, perche in esiti:
        print("| `%s` | %s | %s | %s | %s |"
              % (nome, atteso, trovato, "OK" if ok else "FALLITO", perche))

    morti = prova_sul_vero()
    print("")
    print("Controllo di realta' sugli elenchi VERI: nomi nell'insieme senza un file "
          "corrispondente: %d %s" % (len(morti), morti or ""))

    falliti = [e for e in esiti if not e[3]]
    if falliti or morti:
        print("\nCOLLAUDO FALLITO - %d casi su %d, piu' %d nomi morti"
              % (len(falliti), len(esiti), len(morti)))
        return 1
    print("\nCOLLAUDO SUPERATO - %d casi su %d, nei due versi." % (len(esiti), len(esiti)))
    print("Il difetto piantato e' il caso 2: senza di lui gli altri proverebbero solo")
    print("che il controllo e' stato spento.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
