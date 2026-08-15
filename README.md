# Aurora Food Group — archivio documentale simulato e banco di prova misurato

*Company-brain case study: a fully synthetic, deliberately messy document archive of a
fictional Italian food SME (159 files, 11 formats), a 282-question verified eval set,
frozen retrieval configurations, and before/after measurements of how much
organization improves retrieval. Everything runs locally. Start from
`00_INIZIA_QUI.md` (Italian).*

> ## ⚠️ Questo archivio è interamente inventato
>
> **Aurora Food Group S.r.l. non esiste.** Non è mai esistita. Ogni documento contenuto in
> questo repository è stato generato artificialmente per una simulazione dimostrativa.
>
> Persone, fornitori, prodotti, lotti, importi, non conformità, reclami, contestazioni e
> ispezioni **sono invenzioni**. Nessuno degli eventi descritti è mai accaduto.
>
> Alcuni documenti sono redatti **in forma di atti provenienti da organizzazioni realmente
> esistenti** — rapporti di audit, verbali ispettivi, estratti conto, fatture, certificati.
> Tutti i numeri di certificato, protocollo, pratica, conto e matricola in essi contenuti sono
> inventati, così come tutte le persone indicate come dipendenti, funzionari, auditor o
> ispettori di quelle organizzazioni: **nessuna di esse esiste, e nessuna di quelle
> organizzazioni ha redatto, firmato o ricevuto alcuno di questi documenti.**
>
> Sono nominate **aziende, enti e istituzioni realmente esistenti** — una catena
> della distribuzione organizzata, un ente di certificazione, banche, istituti pubblici,
> un'azienda sanitaria locale. Compaiono come sfondo per rendere verosimile lo scenario:
> **nessun comportamento, dichiarazione, atto o documento qui contenuto è mai stato posto in
> essere da quei soggetti, né è a loro riconducibile.** Ogni condotta descritta è attribuita
> a un'azienda che non esiste, all'interno di una vicenda che non è mai avvenuta.
>
> Codici fiscali, partite IVA, IBAN, codici a barre e numeri di telefono sono generati in
> modo da risultare formalmente corretti — cioè da superare i rispettivi algoritmi di
> controllo — **perché il realismo tecnico è l'oggetto stesso dell'esercizio**. Non
> corrispondono ad alcun soggetto, conto corrente o prodotto reale, e **non devono essere
> utilizzati per alcuno scopo.**
>
> Il progetto non ha finalità commerciali, denigratorie o di altro tipo verso
> alcuno. Chiunque ritenga che un contenuto lo riguardi può segnalarlo: sarà rimosso.

---

## Che cos'è

Il "caos documentale" di una PMI alimentare italiana, ricostruito da zero: **159
documenti, 6,2 MB, 11 formati diversi**, come li si troverebbe nella cartella condivisa
di un'azienda da 50 dipendenti a cui è stato chiesto di consegnare *tutto quello che ha*.

Serve come **banco di prova per pipeline di ingest documentale e sistemi RAG**, e come
caso studio completo: dall'archivio grezzo al «cervello aziendale» organizzato, con la
misura di quanto l'organizzazione migliora le risposte. Un archivio pulito non dice
niente su come si comporterà un sistema nel mondo reale; questo è costruito apposta per
essere difficile nei modi in cui la realtà è difficile.

### Perché un archivio finto

Costruire un sistema che risponde sui documenti di un'azienda è diventato facile: gli
strumenti ci sono e i tutorial pure. Quello che resta difficile è **dire quanto bene
funziona**.

Su un archivio vero non si può misurare: nessuno conosce tutte le risposte giuste, e
nessuno può dire con certezza che un dato *non* è presente da nessuna parte. Su un
archivio costruito da zero sì — ogni risposta è nota, ogni contraddizione è stata messa
lì apposta, e le domande a cui i documenti non rispondono sono state verificate cercando
il dato in tutti i file.

Per questo l'archivio non è il prodotto: è **lo strumento di misura**. Serve a
rispondere alla domanda che conta — non «funziona?», ma *quanto* funziona, dove
sbaglia, e quante volte inventa invece di ammettere che il dato non c'è.

---

## Com'è organizzato il repository

| Cartella | Contenuto |
|---|---|
| `00_INIZIA_QUI.md` | La guida d'orientamento: mappa, stato, regole, glossario |
| `01_metodo/` | I documenti che governano il progetto: generazione dell'archivio, protocollo di misura (con la baseline già verbalizzata), pipeline RAG di produzione, canone della simulazione |
| `02_corpus/` | I 160 file grezzi (159 documenti + avvertenza di finzione), **congelati** e vincolati a un manifest SHA-256 |
| `03_valutazione/` | Le 282 domande, le risposte verificate, l'eval set in JSONL — da **non** indicizzare mai |
| `04_misurazioni/` | I risultati, una cartella per misura (la baseline del 14/08/2026 è la prima) |
| `05_rag_produzione/` | La pipeline RAG Advanced locale (Qdrant, ibrido BM25+denso, RRF, reranker, LLM locale) |
| `06_operativo/` | Scaletta delle sessioni, decision log, manifest del corpus, prompt operativi |

Il corpus (`02_corpus/`):
`.txt` 50 · `.csv` 30 · `.pdf` 27 · `.xlsx` 15 · `.eml` 12 (8 con allegati in base64) ·
`.docx` 11 · `.jpg` 4 · `.pptx` 4 · `.log` 3 · `.xml` 2 (FatturaPA) · `.p7m` 1.

## Perché è difficile

L'archivio riproduce di proposito gli ostacoli che un sistema incontra sul campo:

- **Encoding misto** — sei file di testo in cp1252 con CRLF, il resto UTF-8.
- **OCR degradato** — 5 documenti scansionati con `0`↔`O`, accenti rotti, righe storte
  (ma i codici, decodificati, tornano validi).
- **Date in tre formati** nello stesso file: `10/05/26`, `2026-05-10`, `10-mag-26`.
- **CSV malformati** — separatori incoerenti, decimali con la virgola, header ripetuti,
  righe di totale in mezzo ai dati, celle `#DIV/0!` e `#RIF!`.
- **Contraddizioni deliberate** — due listini, due previsionali, registri che non
  quadrano coi verbali. La risposta giusta non è scegliere un valore: è accorgersi del
  conflitto. Sono tutte registrate, una per una, nel canone.
- **Rumore di fondo** — una ventina di file (menù, cancelleria, condominio, palestra)
  che non c'entra nulla con la vicenda principale.
- **Una storia da ricostruire** — un guasto, una riparazione fatta male, un reclamo:
  la sequenza esiste solo mettendo in fila una decina di documenti scritti da reparti
  che non si parlano.

## Come è stato costruito

Ogni documento è coerente con gli altri: nomi, ruoli, codici, lotti, importi e date
compongono un unico mondo che regge al controllo incrociato. La coerenza non è affidata
alla rilettura ma a **una suite di 89 controlli automatici** su dieci prospettive, e il
corpus è **congelato con un manifest SHA-256** (`06_operativo/manifest_corpus_v1.json`):
ogni misura dichiara su quale impronta esatta dell'archivio è stata fatta.

Le 282 domande non sono state scritte a memoria: per ognuna, uno script estrae i fatti
dalla risposta — numeri, date, codici, nomi — e li cerca nel documento citato. Se il
riscontro non c'è, la domanda viene scartata. Per le domande la cui risposta corretta è
*«il dato non è in archivio»*, il controllo è invertito: il dato viene cercato in tutti
i 159 file e la domanda sopravvive solo se davvero non esiste. Su 361 domande generate,
**35 sono state scartate**.

## Come si misura

Tre configurazioni, tutte congelate, sugli stessi 282 quesiti (protocollo completo in
`01_metodo/metodo_02_misurazione.md`):

- **A — retrieval agentico**: un agente con accesso in lettura ai file. Il più
  intelligente, il meno ispezionabile.
- **B — RAG a embedding semplice** (Chroma + bge-m3, top-8, nessun re-ranking): il
  riferimento confrontabile con la letteratura. È **il metro**: non si tocca.
- **C — RAG Advanced ibrido di produzione** (Qdrant, BM25+denso, RRF, cross-encoder,
  LLM locale a temperatura 0): **il motore** che un'azienda installerebbe davvero,
  interamente dentro le proprie mura (architettura in
  `01_metodo/metodo_04_rag_produzione.md`).

Tre sessioni separate: chi risponde non vede mai le risposte attese; chi valuta non è
chi ha risposto. Tra il «prima» (archivio grezzo) e il «dopo» (vault organizzato in
note atomiche collegate) cambia **una sola variabile**: la forma dell'archivio.

| Metrica | Su quante domande | Perché conta |
|---|---|---|
| Tasso di allucinazione | 31 non rispondibili | misura se il sistema sa dire «non c'è»: è la più dura |
| Riconoscimento dei conflitti | 14 contraddizioni | segnala la divergenza o sceglie a caso? |
| Divario ricerca ↔ attraversamento | 86 vs 74 | misura quanto l'archivio è *navigabile* |
| Precisione delle fonti | tutte | i file citati contengono davvero il dato? |

### Risultati

| Misura | Data | Allucinazione | Conflitti | Ricerca diretta | Attraversamento | Fonti |
|---|---|---|---|---|---|---|
| Baseline — grezzo, agentico (A) | 14/08/2026 | 3.2% | 50.0% | 82.6% | 52.7% | 91.8% |
| Baseline — grezzo, RAG semplice (B) | 14/08/2026 | 0.0% | 57.1% | 61.6% | 31.1% | 80.5% |
| Baseline — grezzo, RAG Advanced (C) | *da misurare* | | | | | |
| Dopo l'organizzazione, A | | | | | | |
| Dopo l'organizzazione, B | | | | | | |
| Dopo l'organizzazione, C | | | | | | |

Zero allucinazioni su 564 valutazioni A+B: entrambe le configurazioni sanno dire «non
c'è». Il divario vero è altrove — sulle domande che attraversano più documenti
(multi-hop: −30 punti rispetto alla ricerca diretta, in **entrambe** le
configurazioni) e su quelle che richiedono di leggere una tabella intera
(aggregazioni: A 19 corrette, B 3). È esattamente ciò che l'organizzazione in note
deve migliorare, ed è ciò che le misure «dopo» dovranno dimostrare.

Il campo `tipo` di ogni domanda dice cosa si sta misurando, e serve a capire *dove* si
rompe il sistema:

| Se sbaglia… | Il problema è… |
|---|---|
| le ricerche dirette | il recupero: indicizzazione o segmentazione |
| gli attraversamenti multi-documento | recupera un documento solo e non sa collegare |
| le trappole (risponde con sicurezza) | inventa: soglie troppo basse, nessun rifiuto |
| i conflitti (sceglie a caso) | non distingue le versioni: mancano data e revisione nel contesto |

## Come usarlo

1. Indicizzare `02_corpus/` con la propria pipeline. **Non indicizzare
   `03_valutazione/`**: contiene le risposte e falserebbe qualunque misura.
2. Sottoporre le domande di `03_valutazione/domande_solo.jsonl` — contiene solo `id` e
   testo, ed è l'unico file che deve entrare nella sessione di test.
3. Confrontare con `03_valutazione/eval_set.jsonl`, usando `note_valutazione` come
   rubrica.

Nota di trasparenza: dal momento in cui questo repository è pubblico, modelli futuri
potrebbero aver visto domande e risposte. Le misure qui riportate sono state eseguite
prima della pubblicazione; chi usa l'archivio come benchmark ne tenga conto.

---

*Archivio generato per scopi dimostrativi e didattici. Nessun dato reale, nessun
soggetto reale.*
