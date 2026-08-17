# -*- coding: utf-8 -*-
"""
indicizza.py — da `chunk.jsonl` alla collezione Qdrant, densa e sparsa.

Una collezione sola con due vettori nominati: `denso` (bge-m3, coseno) e `sparso`
(BM25 pesato a mano, prodotto scalare). Il payload porta i metadati filtrabili.
Alla fine scrive il MANIFEST DELL'INDICE: hash del config, hash del corpus, conteggi,
modelli e data. Un indice senza manifest non e' misurabile — non si sa piu' su cosa.

Riprendibile: l'embedding e' il passo caro (ore su CPU), quindi lo stato dice fin dove si
e' arrivati e un rilancio riparte da li'.

Uso:
    python pipeline\\indicizza.py                 # costruisce o riprende
    python pipeline\\indicizza.py --da-zero       # butta l'indice e ricomincia
"""

import argparse
import hashlib
import json
import sys
import time
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pipeline import comune                                        # noqa: E402
from pipeline.bm25 import IndiceBM25                               # noqa: E402
from pipeline.impronta import impronta_config                      # noqa: E402


def leggi_chunk(percorso):
    righe = []
    with open(percorso, encoding="utf-8-sig") as f:      # tollera il BOM di un editor
        for r in f:
            r = r.strip()
            if r:
                righe.append(json.loads(r))
    return righe


def carica_embedder(cfg):
    from sentence_transformers import SentenceTransformer
    d = cfg["embedding_denso"]
    percorso = comune.RADICE / d["percorso_locale"]
    if not percorso.exists():
        sys.exit("manca il modello di embedding congelato: %s" % percorso)
    m = SentenceTransformer(str(percorso), device=cfg["esecuzione"]["device"])
    m.max_seq_length = d["max_seq_length"]
    return m


def apri_qdrant(cfg, da_zero=False):
    from qdrant_client import QdrantClient, models
    percorso = comune.INDICE
    if da_zero and percorso.exists():
        import shutil
        shutil.rmtree(percorso, ignore_errors=True)
    percorso.mkdir(parents=True, exist_ok=True)
    c = QdrantClient(path=str(percorso))
    nome = cfg["indice"]["collezione"]
    if nome not in {x.name for x in c.get_collections().collections}:
        c.create_collection(
            nome,
            vectors_config={cfg["indice"]["vettore_denso"]: models.VectorParams(
                size=cfg["embedding_denso"]["dimensioni"],
                distance=models.Distance.COSINE)},
            sparse_vectors_config={cfg["indice"]["vettore_sparso"]:
                                   models.SparseVectorParams()},
        )
    return c, models


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--da-zero", action="store_true")
    ap.add_argument("--chunk", default=None)
    a = ap.parse_args()
    sys.stdout.reconfigure(line_buffering=True)

    cfg = comune.carica_config()
    comune.fissa_thread(cfg)
    percorso_chunk = Path(a.chunk or (comune.LOCALE / "chunk.jsonl"))
    if not percorso_chunk.exists():
        sys.exit("manca %s: lancia prima pipeline\\ingestione.py" % percorso_chunk)

    chunk = leggi_chunk(percorso_chunk)
    print("chunk da indicizzare: %d" % len(chunk))

    # ---------------------------------------------------------------- ramo sparso
    # Si costruisce sempre per intero: e' questione di secondi e dipende dall'INSIEME dei
    # documenti (df e lunghezza media), quindi non e' incrementale per natura.
    t0 = time.time()
    sp = cfg["ricerca_sparsa"]
    idx_bm25, conteggi, lunghezze = IndiceBM25.costruisci(
        [c["testo"] for c in chunk], sp["k1"], sp["b"])
    idx_bm25.salva(comune.INDICE.parent / "vocabolario_bm25.json")
    print("BM25: %d termini, avgdl %.1f token, %.1fs"
          % (len(idx_bm25.vocabolario), idx_bm25.avgdl, time.time() - t0))

    # ---------------------------------------------------------------- Qdrant
    client, models = apri_qdrant(cfg, da_zero=a.da_zero)
    nome = cfg["indice"]["collezione"]
    stato_file = comune.INDICE.parent / "stato_indice_c.json"
    impronta = impronta_config(cfg)

    stato = {}
    if stato_file.exists() and not a.da_zero:
        stato = json.loads(stato_file.read_text(encoding="utf-8"))
        if stato.get("impronta_config") != impronta:
            sys.exit("il config e' cambiato rispetto all'indice esistente: rifallo con "
                     "--da-zero, oppure ripristina il config congelato. Un indice a meta'"
                     " fra due configurazioni non e' misurabile.")
    fatti = int(stato.get("chunk_indicizzati", 0))
    if fatti and fatti < len(chunk):
        print("riprendo dal chunk %d" % fatti)
    elif fatti >= len(chunk):
        print("indice gia' completo: %d punti" % client.count(nome).count)

    if fatti < len(chunk):
        embedder = carica_embedder(cfg)
        lotto = cfg["esecuzione"]["batch_embedding"]
        t0 = time.time()
        i = fatti
        while i < len(chunk):
            gruppo = chunk[i:i + lotto]
            vettori = embedder.encode([c["testo"] for c in gruppo],
                                      batch_size=lotto, normalize_embeddings=True,
                                      show_progress_bar=False, convert_to_numpy=True)
            punti = []
            # `conteggi` e `lunghezze` sono paralleli alla LISTA dei chunk, non ai `cid`:
            # si indicizzano per posizione. Usare il `cid` funzionerebbe solo finche' il
            # file dei chunk e' completo e in ordine — e smetterebbe di funzionare, in
            # silenzio e con i pesi sbagliati, su un file filtrato.
            for j, (c, v) in enumerate(zip(gruppo, vettori)):
                pos = i + j
                ind, val = idx_bm25.vettore_documento(conteggi[pos], lunghezze[pos])
                punti.append(models.PointStruct(
                    id=c["cid"],
                    vector={cfg["indice"]["vettore_denso"]: v.tolist(),
                            cfg["indice"]["vettore_sparso"]:
                                models.SparseVector(indices=ind, values=val)},
                    payload={k: c[k] for k in ("file", "percorso_relativo", "sha256_file",
                                               "formato", "origine", "idx", "n_chunk_file",
                                               "caratteri", "testo_sha256", "codici",
                                               "date", "testo")},
                ))
            client.upsert(nome, points=punti)
            i += len(gruppo)
            stato_file.write_text(json.dumps(
                {"impronta_config": impronta, "chunk_indicizzati": i,
                 "chunk_totali": len(chunk)}, ensure_ascii=False), encoding="utf-8")
            el = time.time() - t0
            fatti_ora = i - fatti
            print("  %5d/%d  %6.0fs  stima rimanente %5.1f min"
                  % (i, len(chunk), el, (el / fatti_ora) * (len(chunk) - i) / 60))
        print("indicizzazione finita in %.1f min" % ((time.time() - t0) / 60))

    # ---------------------------------------------------------------- manifest
    rapporto = json.loads((comune.LOCALE / "rapporto_ingestione.json")
                          .read_text(encoding="utf-8"))
    manifest = {
        "artefatto": "manifest_indice_c",
        "data": date.today().isoformat(),
        "impronta_config_c": impronta,
        "collezione": nome,
        "punti": client.count(nome).count,
        "chunk_totali": len(chunk),
        "chunk_per_formato": rapporto["chunk_per_formato"],
        "chunk_per_origine": rapporto["chunk_per_origine"],
        "file_letti": rapporto["file_letti"],
        "corpus": rapporto["corpus"],
        "manifest_corpus": "manifest_corpus_v1.1.json",
        "bm25": {"termini": len(idx_bm25.vocabolario), "avgdl": idx_bm25.avgdl,
                 "n_doc": idx_bm25.n_doc, "k1": idx_bm25.k1, "b": idx_bm25.b},
        "embedding": cfg["embedding_denso"],
        "tesseract": rapporto.get("tesseract"),
    }
    (comune.INDICE.parent / "manifest_indice_c.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    client.close()
    print("\npunti nella collezione: %d" % manifest["punti"])
    print("manifest dell'indice scritto in %s"
          % (comune.INDICE.parent / "manifest_indice_c.json"))


if __name__ == "__main__":
    main()
