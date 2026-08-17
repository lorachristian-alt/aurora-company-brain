# -*- coding: utf-8 -*-
"""
impronta.py — l'hash della configurazione congelata.

Serve a una cosa sola: ogni indice e ogni traccia portano scritto CON QUALI PARAMETRI
sono nati. Se qualcuno tocca un valore, l'indice esistente non si aggiorna in silenzio:
il codice si ferma e lo dice.

Sono escluse dall'impronta due sezioni, e solo quelle:
  `meta`    prosa e date, non cambiano un risultato;
  `misura`  nome della cartella e del file di risposte — la Sessione 6 li cambia per
            forza, e bloccarla su quelli significherebbe rifare l'indice per un nome.

Uso:
    python pipeline\\impronta.py
"""

import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pipeline import comune                                        # noqa: E402

ESCLUSE = ("meta", "misura")


def impronta_config(cfg):
    d = {k: v for k, v in cfg.items()
         if k not in ESCLUSE and not k.startswith("_")}
    testo = json.dumps(d, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(testo.encode("utf-8")).hexdigest()


if __name__ == "__main__":
    cfg = comune.carica_config()
    print("config:   %s" % comune.CONFIG)
    print("escluse:  %s" % ", ".join(ESCLUSE))
    print("impronta: %s" % impronta_config(cfg))
