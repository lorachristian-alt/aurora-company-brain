# -*- coding: utf-8 -*-
"""Verifica la copia dei grezzi in aurora-cervello\\sources contro il manifest v1.1.

metodo_03 §9.2. Riporta TUTTI gli scarti prima di fermarsi: in una sessione non
interattiva il traceback si mangerebbe l'output utile.

Uso:  python verifica_copia_sources.py
Esce 0 se la copia corrisponde al manifest, 1 altrimenti.
"""
import hashlib, json, os, sys

MAN = r"C:\Users\buulo\Desktop\.eval_do_not_index\Aurora_Food_Group_SRL\06_operativo\manifest_corpus_v1.1.json"
DST = r"C:\Users\buulo\Desktop\aurora-cervello\sources"
AMMESSI = {"_index-sources.md"}          # l'unico markdown consentito in sources\ (§3.6)

man = json.load(open(MAN, encoding="utf-8"))
assert len(man["file"]) == 160, "Manifest inatteso: %d voci invece di 160" % len(man["file"])

scarti = []
for e in man["file"]:
    p = os.path.join(DST, e["nome"])
    if not os.path.isfile(p):
        scarti.append(("MANCANTE", e["nome"])); continue
    if hashlib.sha256(open(p, "rb").read()).hexdigest() != e["sha256"]:
        scarti.append(("HASH", e["nome"]))
    if int(os.stat(p).st_mtime * 1000) != e["mtime_ms"]:
        scarti.append(("MTIME", e["nome"]))

presenti = {n for n in os.listdir(DST) if os.path.isfile(os.path.join(DST, n))}
sottocartelle = {n for n in os.listdir(DST) if os.path.isdir(os.path.join(DST, n))}
extra = presenti - {e["nome"] for e in man["file"]} - AMMESSI

for s in scarti:        print("SCARTO      ", *s)
for n in sorted(extra): print("ESTRANEO    ", n)
for n in sorted(sottocartelle): print("SOTTOCARTELLA", n)
print("file verificati: %d | scarti: %d | estranei: %d | sottocartelle: %d"
      % (len(man["file"]), len(scarti), len(extra), len(sottocartelle)))

if scarti or extra or sottocartelle:
    print("\nLa copia non corrisponde al manifest: non si canonizza.")
    sys.exit(1)
print("\nCopia verificata: si puo' canonizzare.")
sys.exit(0)
