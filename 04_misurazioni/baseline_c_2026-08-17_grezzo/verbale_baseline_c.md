# Verbale — Baseline C sul corpus grezzo (RAG Advanced ibrido di produzione)

> **Stato: APERTO.** Il giudizio delle 282 risposte non è ancora stato eseguito: si fa in
> una sessione separata con `06_operativo/prompt/prompt_s3_giudice_c.txt`. Questo verbale
> si chiude — e da quel momento non si modifica più — solo dopo il giudizio e
> l'approvazione al gate.
> **Cosa contiene già** · le condizioni della misura, la costruzione della pipeline, il
> collaudo e l'esito del run, tutti ricontati da script.
> **Cosa manca** · i quattro esiti per le 282 domande, la tabella A/B/C, la riga del README.

---

## 1. Oggetto

Misura della **configurazione C** — RAG Advanced ibrido, interamente locale — sulle stesse
282 domande di `03_valutazione/domande_solo.jsonl` già usate per le baseline A e B del
14/08/2026, e sullo **stesso corpus grezzo di 160 file**.

È l'ultima finestra utile: la baseline C doveva precedere la canonizzazione integrale
(decisione del 15/08/2026, scaletta Sessione 3).

⚠️ **A, B e C sono tre strumenti diversi, non tre versioni dello stesso.** Le asimmetrie
sono elencate al §8 e non vanno addolcite in nessuna lettura dei numeri.

---

## 2. Condizioni della misura

### 2.1 Macchina

| | |
|---|---|
| CPU | Intel Core i7-1065G7, 4 core fisici / 8 logici |
| RAM | 7,8 GB (7.987 MB) |
| GPU | nessuna NVIDIA — Intel Iris Plus integrata, non usata |
| Disco | 86 GB liberi |
| Sistema | Windows 11 Home 10.0.26200 |
| Python | 3.14.7 |

⚠️ **La macchina sta SOTTO la fascia minima dichiarata da `metodo_04` §8 (16 GB).** È il
motivo per cui il generatore è di classe 3B e non 8B, ed è il motivo per cui i numeri di C
si citano sempre come **pavimento, non tetto**.

### 2.2 Componenti e versioni esatte

| Componente | Versione | Checksum SHA-256 |
|---|---|---|
| Embedding denso | `BAAI/bge-m3` — **la stessa copia congelata della config B** | `993b2248881724788dcab8c644a91dfd63584b6e5604ff2037cb5541e1e38e7e` |
| Reranker | `BAAI/bge-reranker-v2-m3` | `d9e3e081faff1eefb84019509b2f5558fd74c1a05a2c7db22f74174fcedb5286` |
| Generatore | `llama3.2:3b-instruct-q4_K_M` via Ollama | digest `a80c4f17acd55265feec403c7aef86be0c25983ab279d83f3bcd3abbcb5b8b72`, 2.019.393.189 byte |
| OCR | tesseract `5.5.3.20260724`, lingua `ita` | percorso assoluto nel config |
| Vector store | Qdrant via `qdrant-client 1.19.0`, modalità locale su file | — |

Librerie pinnate in `05_rag_produzione/requirements.txt`: `torch 2.13.0`,
`transformers 5.15.0`, `sentence-transformers 5.7.0`, `pypdf 6.15.0`,
`python-docx 1.2.0`, `openpyxl 3.1.5`, `python-pptx 1.0.2`, `pillow 12.3.0`,
`pytesseract 0.3.13`.

### 2.3 Configurazione congelata

| | |
|---|---|
| File | `05_rag_produzione/config_c.json` |
| Impronta (SHA-256 su tutte le chiavi tranne `meta` e `misura`) | `afb5893936f27a8a6c0a276e34206a9d87b9052b21ba59f8f8f8e3817e61b0e8` |
| Commit di congelamento | **`d36d7ce`** |
| Pushato sul remote privato | **prima di costruire l'indice** |

**La pre-registrazione è il punto.** La configurazione è stata scritta, committata e
pushata *prima* di indicizzare e *prima* di vedere un solo risultato. L'impronta è
registrata nel manifest dell'indice e in ognuna delle 282 tracce: se un parametro fosse
stato toccato in corsa, l'indice si sarebbe rifiutato di riprendere.

⚠️ **Un tentativo di modifica, intercettato dal meccanismo stesso.** Durante la
costruzione dell'indice si stava per aggiungere al config un'avvertenza sulla ricerca
esatta. Sarebbe stato un ritocco di solo commento, ma ogni byte del file entra
nell'impronta: l'indice in costruzione avrebbe smesso di corrispondere al config che
dichiarava di averlo prodotto. La modifica è stata revocata (`git diff` a zero,
impronta invariata e coincidente con quella scritta nello stato dell'indice) e
l'avvertenza è finita in `metodo_04` §11, che è prosa. Da quell'episodio nasce la regola
scritta in testa a `metodo_04`: **la prosa si corregge, il config no.**

---

## 3. Corpus e indice

### 3.1 Verifica del corpus

`pipeline/verifica_corpus.py` contro `06_operativo/manifest_corpus_v1.1.json`:
**160/160 file verificati**, zero mancanti, zero intrusi, zero divergenti.

### 3.2 Ingestione

| | |
|---|---|
| File letti | 160 |
| Chunk prodotti | **1.902** |
| Caratteri totali | 2.104.242 |
| Chunk duplicati **non** fusi | 26 |

**Chunk per formato** (tutti e 11):

| txt | csv | log | pdf | docx | xlsx | eml | pptx | xml | p7m | jpg |
|---|---|---|---|---|---|---|---|---|---|---|
| 514 | 435 | 390 | 236 | 123 | 80 | 69 | 35 | 10 | 6 | 4 |

**Chunk per origine:** `nativa` **1.897** · `ocr` 2 · `scheda` 3.

⚠️ **I 1.897 chunk `nativa` sono esattamente i 1.897 chunk della configurazione B.**
Non è una coincidenza ed è la verifica più importante di tutto il verbale: estrazione e
chunking di C sono identici a B file per file, quindi la differenza fra le due misure è
l'architettura di recupero e non l'estrattore. Le uniche differenze sono i 2 chunk da OCR
e le 3 schede.

**File senza testo utile (3), che entrano con la sola scheda di metadati:**

| file | perché |
|---|---|
| `IMG-20260510-WA0007.jpg` | OCR sotto soglia: 11 parole, 48 caratteri alfanumerici, confidenza 67,4 |
| `IMG_20260514_152241_frammento_REC-2026-011.jpg` | OCR sotto soglia: 8 parole, 42 caratteri, confidenza 93,0 |
| `~$ttera_risposta_Tosano_reclamo_BOZZA_v3.docx` | lock file di Word, `PackageNotFoundError` — rumore realistico, non un guasto |

### 3.3 L'OCR è stato davvero eseguito — verifica su tre livelli

La soglia (200 caratteri alfanumerici **e** 60 di confidenza media) era dichiarata nel
config *prima* di vedere i risultati. L'esito:

| file | caratteri alfanum. | confidenza | esito |
|---|---|---|---|
| `MOD-QA-07_10-05-26_L1_T2_scansione.jpg` | 437 | 73,6 | **ocr** |
| `SKM_C224e26050408520.jpg` | 476 | 84,4 | **ocr** |
| `IMG-20260510-WA0007.jpg` | 48 | 67,4 | scheda |
| `IMG_..._frammento_REC-2026-011.jpg` | 42 | 93,0 | scheda |

Le due scansioni di documento stanno a 437-476 caratteri, le due fotografie a 42-48: la
soglia a 200 cade in mezzo a un vuoto di un fattore 9. **La confidenza 93,0 sulla foto del
frammento dimostra che l'OCR ha letto benissimo il poco che c'era**: è il conteggio dei
caratteri a discriminare, non la qualità del riconoscimento.

Verificato che tesseract sia stato **eseguito** e non saltato in silenzio:

1. versione `5.5.3.20260724` registrata nel manifest dell'indice **e** nel rapporto di ingestione;
2. la cache di estrazione di **tutti e quattro** i `.jpg` — compresi i due sotto soglia —
   porta `strumento: tesseract 5.5.3.20260724`;
3. nella collezione Qdrant i due chunk `origine=ocr` contengono testo reale
   (`AURORA FOOD GROUP S.r.l. … MOD-QA-07 rev.5 VERIFICA ORARIA METAL DETECTOR`;
   `MOLINO VENETO S.p.A. … P.IVA 00298440231`).

Se tesseract non fosse stato raggiungibile il codice avrebbe sollevato un errore invece di
cachare un file cieco: è scritto in `comune.estrai` apposta, perché un file cieco messo in
cache resterebbe cieco per sempre.

### 3.4 Indice

| | |
|---|---|
| Collezione | `aurora_corpus_v1`, punti **1.902** |
| Ramo denso | `bge-m3`, 1024 dimensioni, coseno |
| Ramo sparso | BM25 scritto a mano, **25.541 termini**, avgdl 239,69 token, k1 1,2, b 0,75 |
| Durata della costruzione | ~2 ore, a ~2,2-2,5 s per chunk |

Il ritmo di indicizzazione (2,2-2,5 s/chunk) coincide con quello misurato per la
configurazione B sulla stessa macchina (2,47 s/chunk): un'ulteriore conferma indipendente
che il ramo denso di C e quello di B sono lo stesso strumento.

⚠️ **La costruzione dell'indice è stata interrotta due volte e ripresa due volte senza
perdere lavoro** (a 496 e a 632 chunk). La ripartibilità non è una promessa del documento:
è stata esercitata.

---

## 4. Collaudo di funzionamento

Dieci domande tecniche **scritte a mano leggendo `02_corpus/`**. Nessuna viene dall'eval
set, che questa sessione non ha mai aperto. Servivano a verificare che i pezzi girino, non
a giudicare la qualità.

| | |
|---|---|
| Documento atteso fra i 4 passaggi consegnati | **8 su 9** |
| Documento atteso presente nella fusione RRF | **9 su 9** |
| Formati toccati dai passaggi consegnati | csv, docx, eml, jpg, log, pdf, txt, xlsx |
| Origini toccate | `nativa` **e** `ocr` |
| Passaggi scartati per budget di contesto | 0 |

Verifica separata dei tre formati che il collaudo non aveva toccato: **`p7m`, `pptx` e
`xml` sono tutti raggiungibili** dal ramo denso, `pptx` e `xml` anche dallo sparso.
**Nessuno degli 11 formati è cieco.**

L'unico atteso non consegnato (domanda 2) era presente nella fusione e il reranker gli ha
preferito un altro documento: è qualità, non funzionamento. ⚠️ **Non è stato toccato
alcun parametro**, come prescrive `metodo_04` §12.

**Un difetto vero trovato dal collaudo e corretto.** L'indicizzatore usava il `cid` del
chunk come posizione nella lista dei pesi BM25: funzionava solo su un file di chunk
completo e in ordine, e su uno filtrato avrebbe assegnato **i pesi sbagliati in silenzio**.
Corretto prima del congelamento.

---

## 5. Il run

### 5.1 Architettura dell'esecuzione, e perché

Il runner gira a **fasi separate**, ed è una conseguenza diretta degli 8 GB di RAM: i tre
modelli pesano 2,3 + 2,3 + 2,0 GB e non convivono.

| Fase | Cosa gira | In memoria |
|---|---|---|
| 1a | vettori densi delle domande, **uno per volta** | solo `bge-m3` |
| 1b | ricerca densa e sparsa, RRF, rerank, tracce | solo il reranker |
| 2 | generazione | solo Ollama |

Il risultato per domanda è identico a quello di una pipeline che gira tutta d'un fiato:
cambia l'ordine in cui si pagano i passi, non cosa viene calcolato. Ogni domanda è
codificata in un batch di uno, perché il batch cambierebbe il riempimento e con esso
l'ultima cifra del vettore.

### 5.2 Tempi

| Passata | Domande | Durata | Per domanda |
|---|---|---|---|
| 1 — recupero, fusione, rerank | 282/282 | **3h 48m** (228,4 min) | 48,2 s (min 35,4 · max 110,6) |
| 2 — generazione | 282/282 | **5h 13m** (313,3 min) | 66,6 s (min 27,7 · max 185,7) |
| **totale** | | **9h 01m** | |

Dentro lo stop-loss delle 24 ore, con margine.

**Sonde eseguite prima del run, sulle domande di collaudo:**

- reranker, a modello caldo e macchina libera: top-in 16 = 27,1 s · 20 = 33,0 s ·
  **24 = 36,2-38,5 s** · 32 = 51,1 s per domanda. Batch: 2 = 40,8 s · **4 = 38,5 s** ·
  8 = 40,7 s · 16 = 47,2 s su 24 coppie. Da qui il top-in 24 e il batch 4 del config.
- generazione, con **solo Ollama in memoria**: 56,3 s medi → 4,41 h stimate sulle 282.

⚠️ **Il run reale è andato più lento della sonda (66,6 s contro 56,3), e il motivo è
misurato, non ipotizzato:** a metà passata 2 la macchina aveva **160 MB di RAM libera su
7.987** e 29,9 GB di commit su 31,3, con browser ed editor aperti accanto al runner. È
pressione di memoria, non un costo della pipeline. Su una macchina dedicata il numero
onesto da aspettarsi è quello della sonda.

### 5.3 Interruzione della shell durante la passata 2 — e continuità dimostrata

**Cosa è successo.** La finestra del terminale che sorvegliava il run si è chiusa per
errore mentre la passata 2 era in corso. Il runner era stato lanciato **staccato dalla
shell** (`Start-Process`, output rediretto su file), scelta presa a metà sessione dopo
aver constatato che i processi tracciati dalla shell venivano terminati alla chiusura di
questa: **il processo è sopravvissuto e ha portato a termine il run da solo.**

**Come si dimostra che il run è stato continuo**, e non spezzato e rilanciato:

| Prova | Esito |
|---|---|
| Intestazioni di avvio nel log della passata 2 | **1 sola**, e dice «282 da fare, 0 già risposte» |
| Righe di rapporto per la passata `generazione` | **1 sola** |
| Fine dichiarata dal runner | `2026-08-18 00:09:46` |
| Durata dichiarata | 313,3 minuti |
| Inizio implicito (fine − durata) | `2026-08-17 18:56:28` |
| Lancio effettivo registrato nel log | `2026-08-17 18:56:49` |
| **Scarto** | **21 secondi** — l'avvio di Python, l'apertura dei file e il controllo di Ollama |

Un rilancio avrebbe lasciato **due** intestazioni, con un numero diverso di «già
risposte», e **due** righe di rapporto con durate spezzate. Ce n'è una sola per ciascuna, e
la durata copre l'intervallo dal lancio alla fine senza buchi.

**Che cosa insegna.** La riprendibilità riga per riga con `fsync` a ogni scrittura e
l'esecuzione staccata dalla shell erano state progettate contro un rischio teorico — un
riavvio, un aggiornamento di Windows a metà notte. Il rischio si è presentato in forma
diversa da quella prevista e la difesa ha retto **senza che nessuno intervenisse**. Vale
come collaudo sul campo della resilienza, ed è un argomento vendibile: la pipeline che il
cliente compra sopravvive alla chiusura della sessione di chi l'ha avviata.

⚠️ Nessun rilancio è stato eseguito dopo l'episodio: il run era già completo.

### 5.4 Integrità del run, ricontata da script

`04_misurazioni/verifica_run_c.py`, che riapre i file prodotti invece di fidarsi del
rapporto che il runner ha scritto di sé:

| | |
|---|---|
| Righe in `misuraC_risposte.jsonl` | **282** |
| Righe in `contesti_c.jsonl` | 282 |
| File di traccia in `tracce/` | 282 |
| id duplicati · mancanti · estranei | **0 · 0 · 0** |
| Risposte senza la propria traccia | 0 |
| Ordine identico a `domande_solo.jsonl` | sì |
| Errori del runner | **nessuno** |
| **Esito** | **INTEGRO** |

---

## 6. Diagnostica formale delle risposte

⚠️ **Non è un giudizio.** Sono conteggi meccanici sul formato, prodotti prima che il
giudice veda alcunché. Il giudizio lo fa una sessione separata.

| | |
|---|---|
| Risposte vuote | 1 su 282 |
| Risposte senza alcuna fonte citata | 12 su 282 |
| **Risposte che citano almeno un file non presente fra i passaggi consegnati** | **76 su 282 (27,0%)** |
| Confidenza dichiarata | `bassa` 212 · `alta` 70 · `media` 0 |

**Sui 76 casi, e sul perché non sono stati ripuliti.** Il runner scrive nel file di
risposte **tutti** i nomi che il modello ha citato, compresi quelli che non erano nel
contesto. Filtrarli sarebbe stato tecnicamente banale e metodologicamente disonesto: in A
e in B il giudice vede le fonti come il modello le ha scritte, e P3 classifica come
`allucinata` proprio la fonte citata che non contiene il dato. Ripulire quelle di C le
avrebbe dato meno allucinazioni **per costruzione**, e i tre numeri avrebbero smesso di
parlarsi. Il 27% è un dato scomodo per C e sta qui perché è vero.

**Sulla confidenza.** Il generatore da 3B non usa la scala: nessun `media` in 282
risposte. Il campo esiste per compatibilità di formato con A e B e **non va fatto pesare
sul giudizio**; l'istruzione è scritta nel prompt del giudice.

---

## 7. Da quale ramo vengono i passaggi — il dato che giustifica l'ibrido

Sui **1.128 passaggi** effettivamente consegnati al generatore (282 × 4), ricontati dalle
tracce:

| Provenienza | Passaggi | Quota |
|---|---|---|
| solo ramo denso | 342 | 30,3% |
| **solo ramo sparso (BM25)** | **255** | **22,6%** |
| trovati da entrambi | 531 | 47,1% |

**Quasi un quarto dei passaggi che il generatore ha visto non sarebbe mai stato trovato
dalla ricerca semantica.** È la giustificazione quantitativa della ricerca ibrida, ed è
misurata su questo archivio, non citata dalla letteratura.

**Copertura dell'archivio:** 130 file distinti su 160 compaiono almeno una volta fra i
passaggi consegnati.

**Formati nei 1.128 passaggi:** txt 460 · csv 186 · pdf 166 · docx 105 · eml 80 ·
xlsx 63 · pptx 37 · log 27 · p7m 2 · jpg 2.

⚠️ **Un risultato contro il progetto, e va scritto per primo: l'OCR non ha inciso sulla
baseline.** Nessuna delle 282 domande ha ricevuto un chunk `origine=ocr` fra i quattro
passaggi finali; le due comparse `.jpg` sono le *schede* dei file senza testo. La capacità
di leggere le scansioni esiste ed è dimostrata dal collaudo, ma **su questa misura non ha
spostato nulla**. L'asimmetria B/C sull'OCR, dichiarata in anticipo come rischio, nei
fatti vale zero.

---

## 8. Le asimmetrie fra A, B e C — senza addolcirle

**Sono tre strumenti diversi.** Chi legge la tabella dei risultati deve avere questo
elenco sotto gli occhi.

1. **Il generatore.** A e B scrivono le risposte con `claude-opus-5`; C con un
   `llama3.2:3b` locale quantizzato a 4 bit. È la differenza più grande di tutte, ed è
   voluta: C misura **il sistema che il cliente compra e che gira dentro le sue mura**,
   non il miglior testo ottenibile.
2. **L'hardware.** La macchina di misura sta sotto la fascia minima dichiarata da
   `metodo_04` §8. I numeri di C sono un **pavimento**.
3. **L'architettura di recupero.** B: Chroma, solo denso, nessun rerank, **8 passaggi**.
   C: Qdrant denso+sparso, RRF, cross-encoder, **4 passaggi**. Che 4 passaggi filtrati
   valgano più di 8 non filtrati è l'ipotesi che la misura mette alla prova, non un
   assunto.
4. **L'estrazione.** C legge i `.jpg` via OCR, B no — ma vedi §7: nei fatti non ha inciso.
5. **Le schede.** C indicizza una scheda di metadati per i 3 file senza testo utile; A e B
   non li vedono affatto.
6. **La ricerca densa esatta.** Qdrant in modalità locale confronta la query con **tutti**
   i vettori; il container di produzione userebbe HNSW, approssimato. **Su questo lato
   specifico il numero di C è un tetto, non un pavimento**, ed è l'unico parametro in cui
   la misura è più favorevole della produzione.
7. **Le fonti non ripulite.** Vedi §6: scelta che costa a C e che si tiene.
8. **Il modello del giudice.** Se il giudice della misura C non fosse `claude-opus-5` con
   fast mode off, come per A e B, il confronto ne risentirebbe e andrebbe annotato qui.

---

## 9. Scostamenti da `metodo_04` decisi in questa sessione

Tutti decisi **prima** del congelamento, con il motivo scritto accanto al valore nel
config.

| Scostamento | Motivo |
|---|---|
| Reranker `bge-reranker-large` → **`bge-reranker-v2-m3`** | il `large` è addestrato su inglese e cinese; su un archivio italiano il reranker è proprio il pezzo che deve far vincere C su B |
| **Dedup dei chunk disattivato** | i duplicati sono contenuto (`metodo_01` §11, regola d'oro 1); fonderli cancellerebbe dall'indice le prove che le domande sull'inventario cercano. Il payload porta `testo_sha256` per chi voglia deduplicare al momento della risposta |
| **Canone e tabella alias fuori dai metadati** | iniettare nell'indice fatti che il corpus grezzo non contiene misurerebbe un archivio già in parte organizzato, cioè ciò che la Sessione 6 deve misurare *dopo* |
| **Niente ramo OCR per i PDF** | sonda su tutti e 27: nessuno scende sotto i 200 caratteri estratti da `pypdf`. Sarebbe stato codice non esercitato |
| **Generatore 3B invece di 8B** | hardware; dichiarato come livello *misurato* contro il livello di *riferimento*, che resta non misurato e non si racconta come tale |

---

## 10. Contrasto fra il prompt di sessione e `metodo_02`, e come è stato risolto

Il prompt della Sessione 3 indicava il file delle risposte come `risposte_c.jsonl`;
l'**Addendum — Configurazione C** di `metodo_02` dice `misuraC_risposte.jsonl`. Vince
`metodo_02`, come prescrive il prompt stesso, e il file si chiama
**`misuraC_risposte.jsonl`**.

Stesso addendum: «le risposte si producono a blocchi da 30 in append». Per una pipeline
automatica il blocco da 30 non ha significato — non c'è una sessione da ricaricare — ma
**la semantica che il blocco proteggeva è rispettata e rafforzata**: scrittura in append
con `fsync` a ogni riga e ripresa riga per riga, non a blocchi. Segnalato al gate.

---

## 11. Cosa manca per chiudere questo verbale

1. Giudizio delle 282 risposte, in sessione separata, con
   `06_operativo/prompt/prompt_s3_giudice_c.txt` → `valutazione_c.jsonl`.
2. Riconteggio con `04_misurazioni/conta_esiti_abc.py` e tabella A / B / C sugli stessi
   282 id.
3. Riga della configurazione C nella tabella dei risultati del `README.md`.
4. Approvazione al gate. **Solo allora questo verbale si chiude e non si modifica più.**

---

## Artefatti prodotti

| Percorso | Cosa |
|---|---|
| `04_misurazioni/baseline_c_2026-08-17_grezzo/misuraC_risposte.jsonl` | le 282 risposte |
| `04_misurazioni/baseline_c_2026-08-17_grezzo/contesti_c.jsonl` | i passaggi consegnati, in forma compatta |
| `04_misurazioni/baseline_c_2026-08-17_grezzo/tracce/` | 282 tracce di audit complete |
| `04_misurazioni/baseline_c_2026-08-17_grezzo/rapporto_run.jsonl` | i rapporti delle due passate |
| `04_misurazioni/verifica_run_c.py` · `conta_passata1.py` · `conta_esiti_abc.py` | gli script che ricontano |
| `05_rag_produzione/` | pipeline, config congelata, `docker-compose.yml`, requirements |
| `05_rag_produzione/collaudo/` | rapporti e tracce del collaudo |

**Cosa contiene una traccia:** domanda, candidati del ramo denso con i punteggi, candidati
del ramo sparso con i punteggi, esito della fusione RRF con i ranghi dei due rami, ordine
completo dopo il reranker con i voti, i passaggi consegnati al modello, il testo grezzo
della generazione, le fonti citate e quelle fuori contesto, i tempi per fase e l'impronta
della configurazione. È il documento che si apre davanti a un auditor.
