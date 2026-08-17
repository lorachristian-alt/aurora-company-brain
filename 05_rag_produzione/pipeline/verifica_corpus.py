# -*- coding: utf-8 -*-
"""
verifica_corpus.py — vincola l'indice a un corpus verificabile.

Ricalcola lo SHA-256 di ogni file di `02_corpus\\` e lo confronta con
`06_operativo\\manifest_corpus_v1.1.json`. Se anche un solo file diverge, o manca, o
ne compare uno di troppo, esce con codice 1 e NON si indicizza: il principio P1 della
scaletta dice che nessun numero esiste senza un manifest che lo regga.

Uso:
    python pipeline\\verifica_corpus.py            # stampa il riepilogo
    python pipeline\\verifica_corpus.py --json     # riepilogo in json (per i verbali)

Non scrive niente: e' un controllo, non una manutenzione.
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

RADICE = Path(__file__).resolve().parents[2]
CORPUS = RADICE / "02_corpus"
MANIFEST = RADICE / "06_operativo" / "manifest_corpus_v1.1.json"


def sha256(percorso, blocco=1 << 20):
    h = hashlib.sha256()
    with open(percorso, "rb") as f:
        while True:
            b = f.read(blocco)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def verifica():
    """Restituisce (esito_ok, riepilogo). Non solleva: il chiamante decide."""
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    attesi = {e["nome"]: e for e in manifest["file"]}
    presenti = {p.name: p for p in sorted(CORPUS.iterdir()) if p.is_file()}

    mancanti = sorted(set(attesi) - set(presenti))
    intrusi = sorted(set(presenti) - set(attesi))
    divergenti = []
    verificati = 0

    for nome in sorted(set(attesi) & set(presenti)):
        p = presenti[nome]
        atteso = attesi[nome]
        h = sha256(p)
        if h != atteso["sha256"] or p.stat().st_size != atteso["bytes"]:
            divergenti.append({"nome": nome, "sha256_atteso": atteso["sha256"],
                               "sha256_trovato": h,
                               "bytes_attesi": atteso["bytes"],
                               "bytes_trovati": p.stat().st_size})
        else:
            verificati += 1

    riepilogo = {
        "manifest": MANIFEST.name,
        "versione_corpus": manifest.get("versione_corpus"),
        "attesi": len(attesi),
        "presenti": len(presenti),
        "verificati": verificati,
        "mancanti": mancanti,
        "intrusi": intrusi,
        "divergenti": divergenti,
        "hash_globale_manifest": manifest.get("hash_globale_sha256"),
    }
    ok = not mancanti and not intrusi and not divergenti and verificati == len(attesi)
    return ok, riepilogo


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="riepilogo in json")
    a = ap.parse_args()

    ok, r = verifica()
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=1))
    else:
        print("corpus:   %s" % CORPUS)
        print("manifest: %s (%s)" % (r["manifest"], r["versione_corpus"]))
        print("verificati %d/%d file" % (r["verificati"], r["attesi"]))
        for etichetta, elenco in (("mancanti", r["mancanti"]), ("intrusi", r["intrusi"])):
            if elenco:
                print("  %s: %d -> %s" % (etichetta, len(elenco), ", ".join(elenco)))
        for d in r["divergenti"]:
            print("  DIVERGENTE: %s (atteso %s..., trovato %s...)"
                  % (d["nome"], d["sha256_atteso"][:12], d["sha256_trovato"][:12]))
        print("ESITO: %s" % ("OK" if ok else "FALLITO"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
