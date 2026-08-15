# 05_rag_produzione — la pipeline che il cliente compra (config C)

Oggi questa cartella è vuota: si riempie nella Sessione 3 della scaletta, seguendo
`01_metodo/metodo_04_rag_produzione.md` (architettura, passi di costruzione, runbook).

Struttura prevista a regime:
- `config.yaml` — TUTTI i parametri, congelati (chunking, RRF, reranker, prompt, seed).
- `requirements.txt` — versioni pinnate.
- `ingestione/` — watcher della inbox, estrazione testo/OCR, chunking, metadati.
- `indice/` — gestione Qdrant (collezioni, snapshot, manifest dell'indice).
- `servizio/` — catena di interrogazione (ibrido → RRF → rerank → LLM) e UI minimale.
- `registro/` — il log delle interrogazioni (jsonl): il documento per l'auditor.

Principio: Chroma è il metro (config B, non si tocca), Qdrant è il motore (config C).
Tutto gira in locale; il cloud (es. Notion) è solo una fonte in entrata.
