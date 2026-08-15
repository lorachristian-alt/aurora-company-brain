# Sessione 0 — Estensione mtime + verifica hash del corpus v1.
# Legge manifest_corpus_v1.json, riverifica lo SHA-256 di ogni file su disco,
# aggiunge mtime_ms e scrive manifest_corpus_v1.1.json.
# Il manifest v1.1 si scrive SOLO se tutti i file tornano: un manifest parziale
# varrebbe meno di nessun manifest.
# Eseguire da 06_operativo\.

import hashlib
import json
import os
import sys

SRC = r"C:\Users\buulo\Desktop\sources"
IN = "manifest_corpus_v1.json"
OUT = "manifest_corpus_v1.1.json"

with open(IN, encoding="utf-8") as f:
    base = json.load(f)

mancanti = []
divergenti = []

for e in base["file"]:
    p = os.path.join(SRC, e["nome"])
    if not os.path.isfile(p):
        mancanti.append(e["nome"])
        continue
    with open(p, "rb") as f:
        b = f.read()
    calcolato = hashlib.sha256(b).hexdigest()
    if calcolato != e["sha256"]:
        divergenti.append((e["nome"], e["sha256"], calcolato))
        continue
    e["mtime_ms"] = int(os.stat(p).st_mtime * 1000)

totale = len(base["file"])
verificati = sum(1 for e in base["file"] if "mtime_ms" in e)

if mancanti or divergenti:
    print("VERIFICA FALLITA: manifest v1.1 NON scritto.")
    for n in mancanti:
        print("  MANCANTE: " + n)
    for n, atteso, trovato in divergenti:
        print("  HASH DIVERSO: " + n)
        print("    atteso:  " + atteso)
        print("    trovato: " + trovato)
    print("%d/%d file verificati." % (verificati, totale))
    sys.exit(1)

base["artefatto"] = "manifest_corpus_v1.1"
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(base, f, ensure_ascii=False, indent=1)

print("OK: %d file verificati, mtime aggiunti -> %s" % (verificati, OUT))
