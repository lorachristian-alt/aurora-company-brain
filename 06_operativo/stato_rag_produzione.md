# Stato della pipeline RAG di produzione (configurazione C)

> **Cos'è** · Lo stato di oggi della configurazione C: cosa esiste, cosa è congelato,
> cosa è stato misurato e cosa resta. Solo stato, mai una regola: le regole stanno in
> `01_metodo\metodo_04_rag_produzione.md`, i valori in `05_rag_produzione\config_c.json`,
> le decisioni in `06_operativo\decision_log.md`.
> **Aggiornato al** · 18/08/2026, chiusura della Sessione 3 dopo il gate.

---

## Dove siamo

| | |
|---|---|
| Pipeline | **costruita, collaudata, misurata** |
| Configurazione | **CONGELATA** il 17/08/2026 — impronta `afb58939…`, commit `d36d7ce`, pushato prima di indicizzare |
| Baseline C sul grezzo | **eseguita e giudicata**, verbale **chiuso** |
| Risultato | **14,5% corrette sulle 282 · 7,6% sulle 251 rispondibili** |
| Verbale | `04_misurazioni\baseline_c_2026-08-17_grezzo\verbale_baseline_c.md` |
| Rapporto di gate | `06_operativo\rapporto_gate_s3.md` — approvato dal coordinatore |
| **Prossimo uso** | **Sessione 6**, misura «dopo» sul vault, con QUESTO config byte per byte |

⚠️ **Il risultato si cita sempre con due numeri.** Delle 41 corrette, 22 vengono da
domande la cui risposta giusta è «il dato non c'è», e il sistema ci arriva perché si
astiene sempre. Il 14,5% da solo racconta una capacità che il sistema non ha.

## Che cosa esiste, in concreto

| | |
|---|---|
| Codice | `05_rag_produzione\pipeline\` — 9 moduli, eseguibili da riga di comando |
| Configurazione | `config_c.json`, ogni valore col suo `_perche` accanto |
| Produzione | `docker-compose.yml` (Qdrant in container) + runbook in `metodo_04` §9 |
| Versioni | `requirements.txt` pinnate a quelle della misura |
| Indice | 1.902 punti, in `_locale_non_su_github\` (gitignorata, rigenerabile) |
| Tracce di audit | 282, una per domanda, complete |
| Script che ricontano | `verifica_corpus.py`, `verifica_run_c.py`, `conta_passata1.py`, `conta_esiti_abc.py`, `metriche_abc.py` |

## I numeri della costruzione, tutti da script

| | |
|---|---|
| Corpus verificato | 160/160 contro `manifest_corpus_v1.1.json` |
| Chunk | 1.902 — di cui **1.897 `nativa`, esattamente i 1.897 della config B** |
| | 2 da OCR, 3 schede di file senza testo utile |
| BM25 | 25.541 termini, avgdl 239,69 token |
| Collaudo | atteso consegnato 8/9, presente nella fusione 9/9; tutti gli 11 formati raggiungibili |
| Passata 1 (recupero + rerank) | 282/282 in 3h 48m — 48,2 s a domanda |
| Passata 2 (generazione) | 282/282 in 5h 13m — 66,6 s a domanda |
| Integrità del run | **INTEGRO**: 0 duplicati, 0 mancanti, 0 estranei, 0 errori |

## Il dato che giustifica l'architettura ibrida

Sui 1.128 passaggi consegnati al generatore: **22,6% viene solo dal ramo BM25**, 30,3%
solo dal denso, 47,1% da entrambi. Quasi un quarto di ciò che il generatore ha visto era
invisibile alla ricerca semantica.

## La diagnosi, e cosa autorizza

**Il collo di bottiglia è il generatore, non il recupero.** 70,2% di fonti giuste contro
14,5% di risposte giuste: 55,7 punti di scarto. Nel 70% dei casi il sistema aveva il
documento in mano e ha sbagliato lo stesso.

**Autorizza una sola azione:** sostituire il generatore lasciando la pipeline invariata.
⚠️ E non ora: prima la Sessione 6 (una variabile alla volta).

## Difetti noti, e perché restano

Registrati nel §13 del verbale e **non corretti di proposito**: risposta vuota,
segnaposto letterale restituito come risposta, degenerazione in loop, campo `fonti` che
esplode in frammenti, e il difetto di recupero padrone/derivato.

⚠️ **Fra il «prima» e il «dopo» cambia solo la forma dell'archivio, i bug dello strumento
compresi.** Un runner migliorato produrrebbe un delta che mescola due cause. Le
correzioni sono materiale per la configurazione di **riferimento**, e si applicano **dopo
la Sessione 6**.

## Cosa resta

- **Sessione 6** — misura «dopo» sul vault: `--corpus <vault>` e `AURORA_LOCALE` per
  l'indice nuovo. Il config **non si tocca**. Prima: `predizioni.md` committato.
- **Configurazione di riferimento (8B)** — lavoro post-ciclo **candidato, non impegno**:
  serve hardware che qui non c'è, e va misurata solo dopo che il ciclo prima/dopo è chiuso.
- **Connettore Notion** — documentato come punto di estensione in `metodo_04` §10, non
  costruito: nel corpus v1 non c'è contenuto Notion da misurare.
- **Registro delle interrogazioni** `registro/AAAA-MM.jsonl` — la forma di produzione
  delle tracce, da attivare quando la pipeline gira per un cliente e non per una misura.
