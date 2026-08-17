# 05_rag_produzione — la pipeline che il cliente compra (config C)

Un RAG Advanced ibrido, interamente locale: ricerca densa + ricerca lessicale, fusione
RRF, reranker cross-encoder, generazione con un LLM locale a temperatura 0, e una traccia
di audit per ogni interrogazione.

**Le regole e i perché stanno in `01_metodo/metodo_04_rag_produzione.md`.**
**I valori stanno in `config_c.json`, congelato il 17/08/2026.** Questo file dice solo
dove sono le cose e come si lanciano.

---

## La cartella

| | |
|---|---|
| `config_c.json` | **La configurazione congelata.** Ogni parametro col suo perché accanto, nella chiave `_perche`. Dopo il commit di congelamento non si tocca |
| `requirements.txt` | Versioni pinnate: quelle con cui la baseline C è stata misurata, non le più recenti |
| `docker-compose.yml` | Qdrant di produzione, in container. **Non serve alla misura**, che gira su Qdrant in modalità locale |
| `pipeline/` | Il codice, eseguibile da riga di comando |
| `collaudo/` | Rapporto e tracce del collaudo di funzionamento |
| `_locale_non_su_github/` | Pesi dei modelli, indice Qdrant, cache dell'estrazione. **Gitignorata** |

## Il codice, in ordine di esecuzione

| File | Cosa fa |
|---|---|
| `pipeline/verifica_corpus.py` | 160/160 contro il manifest, o non si indicizza |
| `pipeline/comune.py` | Percorsi, config, estrazione con cache, chunking, tokenizzazione |
| `pipeline/bm25.py` | Il ramo lessicale, scritto a mano, esportabile come vettore sparso |
| `pipeline/ingestione.py` | Corpus → `chunk.jsonl` + rapporto coi conteggi |
| `pipeline/indicizza.py` | Chunk → collezione Qdrant (densa + sparsa) + manifest dell'indice |
| `pipeline/interroga.py` | La catena di interrogazione, e una domanda singola da riga di comando |
| `pipeline/collaudo.py` | 10 domande scritte a mano leggendo il corpus: collaudo di funzionamento |
| `pipeline/runner_misura.py` | La baseline C sulle 282, a due passate, riprendibile |
| `pipeline/impronta.py` | L'hash di congelamento del config |

## I comandi

Dalla cartella `05_rag_produzione\`:

```
python pipeline\verifica_corpus.py
python pipeline\ingestione.py
python pipeline\indicizza.py
python pipeline\collaudo.py --solo-recupero
python pipeline\collaudo.py
python pipeline\interroga.py "quanti chili riporta il mass balance del lotto L26130?"

python pipeline\runner_misura.py --passata retrieval   --limite 5 --sonda
python pipeline\runner_misura.py --passata generazione --limite 5 --sonda
python pipeline\runner_misura.py --passata retrieval
python pipeline\runner_misura.py --passata generazione
```

Per la Sessione 6, il corpus cambia da riga di comando e **il config non si tocca**:

```
python pipeline\ingestione.py --corpus <radice del vault> --senza-verifica
python pipeline\indicizza.py --da-zero
```

## Le tre cose da sapere prima di metterci le mani

1. **Chroma è il metro (config B), Qdrant è il motore (config C).** Non si migra B su
   Qdrant «per pulizia»: cambierebbe lo strumento a metà esperimento.
2. **Il runner gira a due passate** — prima tutto il recupero, poi tutta la generazione —
   perché su 8 GB di RAM embedder, reranker e LLM non convivono. Il risultato per domanda
   è identico: cambia l'ordine in cui si pagano i passi.
3. **La configurazione è congelata.** Se il collaudo fa venire voglia di spostare un `k`,
   la risposta è no: si segnala al gate. Un parametro mosso guardando dei risultati è
   ciò che rende una misura non credibile.
