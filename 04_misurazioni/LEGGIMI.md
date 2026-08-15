# 04_misurazioni — i numeri, una cartella per misura

Regola dei nomi: `<fase>_<data>_<oggetto>` (es. `baseline_2026-08-14_grezzo`,
`dopo_2026-xx-xx_vault`). I file dentro una cartella di misura sono il VERBALE di
quella misura: non si modificano mai, nemmeno per «pulizia».

- `baseline_2026-08-14_grezzo/` — la baseline A e B sul corpus grezzo: risposte,
  valutazione, metriche, configurazioni congelate (`Config_test_13-08-26/`).
  `misuraA.1_risposte.jsonl` è il file di ripartenza del giro 9-10 della misura A
  (il file principale si era appesantito: episodio documentato in metodo_02).
- `rag_retrieval.py` — lo strumento della configurazione B. Per una nuova misura vanno
  adattate SOLO le costanti di percorso in testa (SOURCES, DOMANDE, OUT, MODEL_DIR,
  INDEX): il modello congelato sta in `_locale_non_su_github/modelli/bge-m3`, le domande
  in `03_valutazione/domande_solo.jsonl`. Chunking e parametri NON si toccano.
- `_locale_non_su_github/` — modello di embedding (2,2 GB) e indice Chroma della
  baseline: restano su questa macchina, esclusi da git (vedi `.gitignore`).

La baseline C (RAG di produzione) e le misure «dopo» aggiungeranno qui le loro cartelle.
