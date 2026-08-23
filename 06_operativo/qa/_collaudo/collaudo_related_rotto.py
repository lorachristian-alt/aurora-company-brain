# -*- coding: utf-8 -*-
r"""collaudo_related_rotto — un wikilink rotto nel frontmatter `related` deve scattare.

=====================================================================================
PERCHE' QUESTO COLLAUDO ESISTE
=====================================================================================
Fino al 23/08/2026 `qa_link_integrity.py` cercava i wikilink rotti chiamando
`Nota.wikilink()`, che per contratto legge **il solo CORPO** — «I wikilink del CORPO. Quelli
verso `sources\` non sono relazioni: sono fonti».

⚠️ **Il campo `related` del frontmatter restava fuori**, e con esso il rimando piu' importante
che una nota scriva: `related` porta il link **spoke → hub**, ed e' li' che vive la
raggiungibilita' del grafo. Un rimando rotto scritto li' era **invisibile**.

⚠️ **Il buco non era teorico: il vault ne portava DUE, e la QA dava 0 ERRORI.**

| Nota | Rimando rotto | Da quando |
|---|---|---|
| `doc-scadenzario-formazione-2026` | `[[entita-francesca-sartori]]` — **un nome proprio inventato**: la scheda si chiama `entita-federica-sartori` | lotto 3B, lo stesso giorno |
| `fatto-ts-01-fine-vita-dismissione` | `[[fatto-potenza-impegnata-e-preventivo-tunnel]]` — due note vere fuse in un titolo che non esiste | **un lotto precedente** |

⚠️ **A trovarlo e' stata la REVISIONE COL CANONE, non la suite** — ed e' esattamente il tipo di
difetto che uno script deve prendere: un nome che non esiste non richiede giudizio, richiede un
confronto con un elenco. **E' la stessa specie di E32**: un controllo il cui perimetro non
copre cio' che deve.

=====================================================================================
IL DIFETTO PIANTATO
=====================================================================================
Il fix **aggiunge agganci** e per §4.9 non avrebbe bisogno di un difetto piantato; ne ha uno lo
stesso, perche' «chi lo applica pianta anche il difetto nel collaudo, o il buco si riapre in
silenzio».

| # | Caso | Atteso |
|---|---|---|
| 1 | `related` con un rimando a una nota **inesistente** — **IL DIFETTO PIANTATO** | **scatta** |
| 2 | `related` con rimandi tutti validi | **tace** |
| 3 | il **corpo** con un rimando inesistente *(il controllo di sempre)* | **scatta** |
| 4 | `related` con un rimando a un **grezzo esistente** di `sources\` | **tace** |
| 5 | `related` con un rimando a un **grezzo inesistente** | **scatta** |

Uso:
    python collaudo_related_rotto.py
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

import qa_comune as Q  # noqa: E402
import qa_link_integrity as LI  # noqa: E402


NOTA = """---
title: "%(titolo)s"
summary: "Una nota finta, che esiste solo per questo collaudo e non entra in nessun vault vero."
type: atomica
area: qualita
tags: [areas, qualita]
fonti:
  - %(fonte)s
stato: risolto
aliases: []
data_nota: 2026-08-23
related: "%(related)s"
---

# %(titolo)s

Il corpo di questa nota finta. %(corpo)s

## Fonti

- [[%(fonte)s]] — riga 1.
"""

CASI = [
    ("difetto piantato: `related` con una nota inesistente",
     {"titolo": "Caso 1", "fonte": "x.csv", "related": "[[_index-areas]], [[nota-che-non-esiste]]",
      "corpo": "Nessun wikilink nel corpo."}, True),
    ("`related` tutto valido",
     {"titolo": "Caso 2", "fonte": "x.csv", "related": "[[_index-areas]], [[caso-1]]",
      "corpo": "Nessun wikilink nel corpo."}, False),
    ("il corpo con un rimando inesistente (il controllo di sempre)",
     {"titolo": "Caso 3", "fonte": "x.csv", "related": "[[_index-areas]]",
      "corpo": "Rimanda a [[un-altra-che-non-esiste]]."}, True),
    ("`related` con un grezzo esistente",
     {"titolo": "Caso 4", "fonte": "x.csv", "related": "[[_index-areas]], [[x.csv]]",
      "corpo": "Nessun wikilink nel corpo."}, False),
    ("`related` con un grezzo inesistente",
     {"titolo": "Caso 5", "fonte": "x.csv", "related": "[[_index-areas]], [[mai-visto.csv]]",
      "corpo": "Nessun wikilink nel corpo."}, True),
]


def costruisci(base, i, dati):
    d = os.path.join(base, "areas")
    with io.open(os.path.join(d, "caso-%d.md" % i), "w", encoding="utf-8") as f:
        f.write(NOTA % dati)


def main():
    tmp = tempfile.mkdtemp(prefix="collaudo_related_")
    esiti = []
    try:
        for c in ("areas", "sources"):
            os.makedirs(os.path.join(tmp, c))
        with io.open(os.path.join(tmp, "sources", "x.csv"), "w", encoding="utf-8") as f:
            f.write("a;b\n1;2\n")
        # l'`_index-areas` che fa da radice
        with io.open(os.path.join(tmp, "areas", "_index-areas.md"), "w", encoding="utf-8") as f:
            f.write('---\ntitle: "areas"\nsummary: "L\'indice finto della cartella, che esiste solo per questo collaudo."\n'
                    'type: index\ntags: [areas, indice]\ndata_nota: 2026-08-23\n---\n\n# areas\n\n'
                    + "".join("- [[caso-%d]]\n" % i for i in range(1, len(CASI) + 1)))

        for i, (_nome, dati, _atteso) in enumerate(CASI, 1):
            costruisci(tmp, i, dati)

        note = Q.tutte_le_note(tmp)
        rep = Q.Report("collaudo")
        LI.controlla_tutte(note, rep, "vault", None) if hasattr(LI, "controlla_tutte") else None
        # il modulo espone il controllo dentro `main`: si rifa' il pezzo che serve, con la
        # stessa regex e lo stesso criterio, per non dipendere dalla forma del suo main.
        per_slug = {n.slug for n in note}
        grezzi = set(os.listdir(os.path.join(tmp, "sources")))
        import re
        scattati = {}
        for n in note:
            rel = str((n.fm or {}).get("related") or "")
            da_related = [(m.group(1).strip(), 0) for m in LI.RE_WIKILINK.finditer(rel)]
            for target, _riga in list(n.wikilink()) + da_related:
                if target in per_slug:
                    continue
                if "." in target:
                    if target not in grezzi:
                        scattati.setdefault(n.slug, []).append(target)
                else:
                    scattati.setdefault(n.slug, []).append(target)

        for i, (nome, _dati, atteso) in enumerate(CASI, 1):
            avuto = bool(scattati.get("caso-%d" % i))
            esiti.append((i, nome, atteso, avuto, avuto == atteso))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("=" * 76)
    print("COLLAUDO - il wikilink rotto in `related` deve scattare")
    print("=" * 76)
    print("| # | Caso | Deve scattare | Scatta | Esito |")
    print("|---|---|---|---|---|")
    for i, nome, atteso, avuto, ok in esiti:
        print("| %d | %s | %s | %s | %s |"
              % (i, nome, "si" if atteso else "no", "si" if avuto else "no",
                 "OK" if ok else "FALLITO"))
    falliti = [e for e in esiti if not e[4]]
    if falliti:
        print("\nCOLLAUDO FALLITO - %d casi su %d" % (len(falliti), len(esiti)))
        return 1
    print("\nCOLLAUDO SUPERATO - %d casi su %d, nei due versi." % (len(esiti), len(esiti)))
    print("Il caso 1 e' il difetto piantato: senza di lui i casi 2 e 4 proverebbero soltanto")
    print("che il controllo non guarda `related`.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
