# Verbale — Baseline C sul corpus grezzo (RAG Advanced ibrido di produzione)

> **Stato: CHIUSO** il 18/08/2026, a giudizio concluso. **Da questo momento non si
> modifica più**: se emergesse un errore si scrive una nota separata e datata, non si
> corregge il verbale.
> **Cosa contiene** · condizioni della misura, costruzione della pipeline, collaudo,
> esito del run, risultati del giudizio e diagnosi. Ogni numero è stato **ricontato da
> script dai file jsonl**; nessuno è stato trascritto dal rapporto del giudice.
> **Giudizio** · eseguito il 18/08/2026 in sessione separata, `claude-opus-5` fast mode
> OFF — lo stesso modello e le stesse condizioni della valutazione A/B del 14/08/2026.
> Rapporto discorsivo del giudice: `giudice_rapporto_c.md`, esito riga per riga in
> `valutazione_c.jsonl`.

---

## 0. Il risultato, e va letto con due numeri insieme

> ## **14,5% corrette sulle 282 · 7,6% sulle 251 rispondibili**
>
> **Le due percentuali non si citano mai una senza l'altra.**

| | corrette | su | |
|---|---:|---:|---|
| Tutte le domande | 41 | 282 | **14,5%** |
| Solo le domande **rispondibili** | 19 | 251 | **7,6%** |
| Solo le `non_rispondibile` | 22 | 31 | 71,0% |

**Perché il solo dato complessivo è fuorviante — la spiegazione è del giudice e si
riporta com'è.** Delle 41 risposte corrette, **22 vengono da domande la cui risposta
giusta è «il dato non è in archivio»**, e il modello ci arriva

> «**perché si astiene sempre**, non perché sappia distinguere ciò che c'è da ciò che
> manca. È lo stesso comportamento che altrove produce decine di astensioni false.»

Il 71,0% sulle `non_rispondibile` **non misura prudenza**: misura una costante. Lo stesso
riflesso che fa passare le esche fa fallire le domande a cui una risposta esisteva —
Q089, Q170, Q209 e decine di altre, dove il sistema si astiene **citando il file che
contiene il dato**. Contare quelle 22 come merito e non contare le astensioni false come
colpa sarebbe misurare due volte lo stesso comportamento, una volta in positivo.

⚠️ **Chiunque riporti il 14,5% senza il 7,6% sta raccontando una capacità che il sistema
non ha.** Vale per il README, per il rapporto di gate e per qualunque uso commerciale.

---
## 1. Oggetto

Misura della **configurazione C** — RAG Advanced ibrido, interamente locale — sulle stesse
282 domande di `03_valutazione/domande_solo.jsonl` già usate per le baseline A e B del
14/08/2026, e sullo **stesso corpus grezzo di 160 file**.

È l'ultima finestra utile: la baseline C doveva precedere la canonizzazione integrale
(decisione del 15/08/2026, scaletta Sessione 3).

⚠️ **A, B e C sono tre strumenti diversi, non tre versioni dello stesso.** Le asimmetrie
sono elencate al §14 e non vanno addolcite in nessuna lettura dei numeri.

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

⚠️ **Come è finita.** Il giudice, che non ha ricevuto questo numero apposta (avrebbe
saputo quante allucinazioni «doveva» trovare), ha classificato `allucinata` **25 risposte
su 282**, non 76. Le due misure non coincidono e non devono: 76 conta le **citazioni fuori
contesto**, cioè un difetto di formato; 25 conta le **affermazioni false**, cioè un
difetto di contenuto. Molte delle 76 sono rumore in coda a una risposta per il resto
onesta, e il giudice ha dichiarato di non farle degradare il campo (§9).

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

## 8. Risultati del giudizio — A, B e C sugli stessi 282

Tutti i numeri di questa sezione escono da `04_misurazioni/conta_esiti_abc.py` e
`04_misurazioni/metriche_abc.py`, che rileggono i jsonl delle valutazioni. **Nessun
numero è stato trascritto dal rapporto del giudice**; i due conteggi coincidono.

### 8.1 I quattro esiti

| Esito | A — agentico | B — RAG semplice | C — RAG produzione |
|---|---:|---:|---:|
| `corretta` | **199 (70,6%)** | **126 (44,7%)** | **41 (14,5%)** |
| `parziale` | 50 (17,7%) | 77 (27,3%) | 75 (26,6%) |
| `sbagliata` | 33 (11,7%) | 79 (28,0%) | 141 (50,0%) |
| `allucinata` | 0 (0,0%) | 0 (0,0%) | 25 (8,9%) |
| fonti corrette | 259 (91,8%) | 227 (80,5%) | 198 (70,2%) |
| corrette **sulle 251 rispondibili** | 68,9% | 40,2% | **7,6%** |
| corrette + parziali | 88,3% | 72,0% | 41,1% |

**C è ultima su ogni riga, e di molto.** Non è un esito da addolcire: sulle domande a cui
una risposta esisteva, C ne prende bene una su tredici, contro due su tre di A.

### 8.2 Per tipo di domanda (corrette / parziali / sbagliate / allucinate)

| Tipo | n | A | B | C | C — % corrette |
|---|---:|---|---|---|---:|
| `non_rispondibile` | 31 | 26/4/1/0 | 25/6/0/0 | 22/3/4/2 | 71,0% |
| `lookup` | 86 | 71/9/6/0 | 53/15/18/0 | 15/30/31/10 | 17,4% |
| `calcolo` | 24 | 19/3/2/0 | 9/9/6/0 | 2/7/13/2 | 8,3% |
| `multi_hop` | 74 | 39/21/14/0 | 23/28/23/0 | 2/19/48/5 | 2,7% |
| `aggregazione` | 28 | 19/4/5/0 | 3/4/21/0 | 0/1/25/2 | **0%** |
| `temporale` | 18 | 15/3/0/0 | 5/9/4/0 | 0/4/11/3 | **0%** |
| `contraddizione` | 14 | 7/4/3/0 | 8/3/3/0 | 0/11/3/0 | **0%** |
| `metadato` | 7 | 3/2/2/0 | 0/3/4/0 | 0/0/6/1 | **0%** |

**Quattro tipi su otto chiudono a zero per C.** Su `aggregazione` la caduta è totale e
non è nuova — anche B fa 3 su 28 — ma C non prende nemmeno quelle.

### 8.3 Le quattro metriche di P4

| Metrica | A | B | C |
|---|---:|---:|---:|
| Tasso di allucinazione (su `non_rispondibile`) | 3,2% | 0,0% | **19,4%** |
| Riconoscimento dei conflitti | 50,0% | 57,1% | **0,0%** |
| Ricerca diretta (`lookup`) | 82,6% | 61,6% | 17,4% |
| Attraversamento (`multi_hop`) | 52,7% | 31,1% | 2,7% |
| Precisione delle fonti | 91,8% | 80,5% | 70,2% |

⚠️ **Come è definito il tasso di allucinazione, e perché così.** P4 lo definisce come
percentuale di esiti `allucinata` sulle sole `non_rispondibile`. Nella valutazione A/B
del 14/08 **il campo `allucinata` non fu mai usato** — zero righe su 564 — e il giudice
di allora ripiegò su `sbagliata`, dichiarandolo. Nella misura C il campo è usato davvero.
Per non avere una colonna che confronta due definizioni diverse, qui si usa
**`allucinata` + `sbagliata` su `non_rispondibile`**, che dove il campo `allucinata` è
vuoto **coincide esattamente col ripiego del 14/08**: le righe A e B non cambiano di una
cifra. Con la definizione alla lettera di P4, C farebbe 6,5% (2 allucinate su 31) — un
numero più lusinghiero e meno confrontabile, e per questo non è quello in tabella.

⚠️ **Un numero che sembra un merito e non lo è.** Il divario fra `lookup` e `multi_hop`
è 29,9 punti in A, 30,5 in B e **14,7 in C**. Non significa che C attraversi meglio:
significa che parte da 17,4% e non ha spazio per cadere. È effetto pavimento, e
presentarlo come un vantaggio sarebbe disonesto.

### 8.4 La riga per il README

```
| Baseline — grezzo, RAG Advanced (C) | 17/08/2026 | 19.4% | 0.0% | 17.4% | 2.7% | 70.2% |
```

---

## 9. Come è stato compilato `fonti_corrette`, e perché non è confrontabile fra le tre misure

La regola è del giudice ed è **citata alla lettera**, perché il campo sia ricalcolabile da
chiunque:

> **`true` se e solo se:**
> 1. fra le fonti citate compare **almeno una delle fonti attese** dall'`eval_set`, **e**
> 2. nessuna citazione punta a un **documento inesistente** (nome inventato, storpiato o troncato).
>
> **Non degradano il campo:**
> - le fonti reali ma non pertinenti aggiunte in coda — rumore frequentissimo in C, presente in quasi tutte le risposte;
> - i frammenti che non sono nomi di file ma **intestazioni di sezione, numeri di pagina o righe del documento giusto** (`"CONTO ECONOMICO"`, `"pag. 2"`, `"Art. 5.1"`): sono rumore di formattazione, non citazioni false.
>
> **Separazione dei due campi.** `esito` misura il contenuto, `fonti_corrette` misura la citazione. Sono tenuti distinti apposta, per non contare due volte lo stesso difetto: esistono risposte `corretta` con `fonti_corrette: false` (Q020, Q033, Q121) e risposte `allucinata` con `fonti_corrette: true` (Q016, Q045, Q101).

E l'eccezione, anch'essa alla lettera:

> **⚠️ Eccezione sulle `non_rispondibile`.** Per le 31 domande di tipo `non_rispondibile` **le fonti attese sono vuote**, quindi la regola sopra non si applica e **il campo non è confrontabile con quello degli altri blocchi**. Lì `fonti_corrette` è `false` solo dove una citazione viene usata per **sostenere un'affermazione errata** (Q248 con l'AUA, Q265 col report costi fissi, Q272 con la bozza di lettera).

⚠️ **Conseguenza, e va detta prima che qualcuno metta i tre numeri in fila.** Il confronto
`fonti_corrette` fra A, B e C **non è omogeneo**, per tre motivi cumulativi:

1. la regola sopra è stata **dichiarata e applicata dal giudice di C**; i giudici di A e B
   del 14/08 non hanno lasciato una regola scritta altrettanto esplicita, quindi non si sa
   se abbiano trattato allo stesso modo il rumore in coda e i nomi storpiati;
2. **il materiale è diverso**: in C il campo `fonti` contiene rumore massiccio — frammenti
   di righe CSV, nomi di persone, numeri di pagina — che in A e B non esiste, perché lì
   scriveva un modello di frontiera che rispettava il formato;
3. sulle 31 `non_rispondibile` il campo misura una cosa diversa in tutte e tre le misure.

**Quindi 91,8% / 80,5% / 70,2% si leggono come ordine di grandezza, non come misura fine.**
Il numero di C che regge da solo, perché ricontato sullo stesso metro, è il **70,2%
confrontato con l'esito**: vedi §10.

---
## 10. La diagnosi: il collo di bottiglia è il generatore, non il recupero

**È il risultato più utile di tutta la misura, e nasce dal confronto di due numeri
prodotti dallo stesso giudizio:**

| | |
|---|---:|
| Risposte che citano il documento giusto (`fonti_corrette`) | **198 / 282 = 70,2%** |
| Risposte corrette | **41 / 282 = 14,5%** |
| **Scarto** | **55,7 punti** |

**Nel 70% dei casi il sistema aveva il documento giusto in mano e ha sbagliato lo stesso.**
E non «non ha trovato»: in decine di casi **la risposta nega un dato che sta nel file che
la risposta stessa sta citando**. Le parole del giudice:

> «Non è un problema di recupero: è che un LLM da 3B non estrae dal passaggio che ha in
> mano, non conta righe, non somma, non incrocia.»

I tre casi che lo mostrano meglio:

| id | Cosa è successo |
|---|---|
| **Q089** | Dichiara «non determinabile» un conteggio che il registro scrive **in chiaro in fondo al file**: `TOTALE SCADUTI: 17`. |
| **Q170** | Alla domanda se qualcuno guidi il muletto senza abilitazione risponde che non è determinabile, **citando il registro che riporta testualmente** «NON ABILITATO ALLA GUIDA fino a rinnovo» accanto a Preda Radu. |
| **Q209** | Rifiuta di rispondere **perché il dato nel documento è espresso come «circa»**: ha trovato il passaggio, l'ha letto, e l'ha scartato per approssimazione. |

Stesso schema in Q012 (scrive «non è possibile determinare la pratica» e mette
«Pratica n. 28714» dentro il campo `fonti` della stessa riga), Q087, Q097, Q106, Q112,
Q115. Sulle `aggregazione` è totale: 28 domande, zero corrette, e le quattro volte in cui
ha provato a contare ha sbagliato di molto (Q099: 1 invece di 3 · Q104: 1 invece di 5 ·
Q109: 19 invece di 8 · Q113: 4 invece di ~49, avendo contato gli *eventi* invece dei
*campioni*).

### 10.1 Il richiamo che rende leggibile questo numero: è un pavimento dichiarato

**Il generatore misurato è un `llama3.2:3b` quantizzato a 4 bit, scelto perché la macchina
ha 7,8 GB di RAM e nessuna GPU** — sotto la fascia minima che `metodo_04` §8 dichiara per
sé stesso (16 GB). Questo era **scritto e committato prima di misurare**, non è una
spiegazione trovata dopo aver visto i numeri: sta in `config_c.json`
(`generazione._perche_modello`) e in `metodo_04` §4, nel commit di congelamento
`d36d7ce` del 17/08/2026 alle 12:44 — **prima** che l'indice esistesse.

La configurazione di **riferimento** — classe 8B su 16-32 GB, resto della pipeline
identico — è documentata in `metodo_04` §4 e **non è mai stata misurata**. La regola resta
in vigore: **non si racconta come se lo fosse.** Di essa si dice che è la configurazione
consigliata, mai che rende di più, finché qualcuno non la conta.

⚠️ **Conseguenza operativa, ed è l'unica azione che questi numeri autorizzano:**
sostituire il generatore lasciando invariata la pipeline è l'unico intervento che può
spostare il risultato. Il recupero, su questa misura, **non è il fattore limitante** — e
il dato del §7 lo conferma dall'altro lato: il 22,6% dei passaggi consegnati veniva solo
dal ramo BM25, cioè l'ibrido stava lavorando.

### 10.2 Un difetto di recupero però esiste, ed è isolabile

Quando il corpus contiene un **documento-padrone e un suo derivato** — mail di inoltro,
copia di cortesia, contratto che cita il listino — il recupero pesca il derivato:

- **Q033** — condizioni Molino corrette ma attribuite alla mail di aumento invece che al listino;
- **Q052** — cita l'inoltro `.eml` e restituisce il claim commerciale «−22% rispetto al TS-01» al posto dei 0,072 kWh/kg del preventivo;
- **Q049** — fattura di cortesia invece degli XML SDI, e infatti perde il codice destinatario in entrata;
- **Q020**, **Q048**, **Q066**, **Q070** — stesso schema.

È il difetto di recupero più chiaro emerso, ed è **materiale per la Sessione 6**: nel
vault canonizzato il documento-padrone e il derivato diventano due note distinte con
`fonti` esplicite, ed è esattamente il caso che la canonizzazione dovrebbe risolvere.
⚠️ Nessuna correzione ora: vedi §13.

---

## 11. Il rischio dominante non sono le allucinazioni: sono le 75 `parziale`

**È il punto che un'azienda alimentare deve leggere per primo.**

Le 25 allucinazioni (8,9%) sono il difetto che tutti si aspettano da un sistema AI. Non
sono il difetto peggiore di questa misura. **La forma dominante è il sì o il no giusto,
nudo:**

> «Sì, in parte a rifiuto» (Q183) · «Sì, era già stato contestato» (Q210) · «No, non aveva
> la formazione HACCP» (Q191) · «Sì, c'è un problema con il lievito» (Q224) · «La lista
> buyer contiene duplicati» (Q095)

Sono risposte **vere e inutilizzabili**: nessuna data, nessun codice, nessun importo,
nessun FIR, nessuna NC. Chi legge **non ha modo di distinguerle da un'ipotesi e non ha
nulla da verificare**. Il giudice le qualifica come

> «la modalità di fallimento più insidiosa della misura C, perché **si comporta come una
> risposta**.»

Il conto è questo: **75 risposte su 282 — più di una su quattro — sono vere e non
verificabili.** Sono il triplo delle allucinazioni.

### 11.1 E sulle contraddizioni il difetto diventa sistematico

**14 domande di tipo `contraddizione`. Zero corrette. Undici `parziale`.**

Il modello dà quasi sempre il valore giusto e **non si accorge mai che nell'archivio ne
esiste un altro**:

| id | Cosa dà | Cosa nasconde |
|---|---|---|
| **Q235** | «2» NC dell'audit, come dichiara l'intestazione | la sezione di chiusura dello **stesso file** parla di NC 1-7 |
| **Q240 / Q234** | un numero d'offerta Criotech | ne circolano **tre** |
| **Q236** | il protocollo giusto della PEC | il verbale ispettivo ne richiama un altro |
| **Q238** | 68,6 | non distingue la sonda di camera da quella **al cuore**, l'unica rilevante per il CCP2 |
| **Q241** | le dimensioni del tunnel dall'offerta | che con quell'altezza **l'impianto non passa sotto la trave**: un rischio di progetto da 290.000 € |

⚠️ **Il giudizio del giudice su questo punto, e lo si sottoscrive:**

> «Un sistema documentale che risponde così è **più pericoloso di uno che si astiene**:
> consegna un numero verificabile e nasconde che il dato è contestato.»

**Perché è il difetto peggiore proprio in un'azienda alimentare.** Il valore di questa
pipeline, davanti a un auditor BRCGS o a un ispettore ATS, è consegnare un dato **con la
catena delle fonti**. Una risposta che dà il numero giusto e tace che ne esiste un secondo
in conflitto non è un'informazione incompleta: **è un'informazione che chiude un'indagine
che andava aperta.** L'archivio contiene contraddizioni volute — è l'oggetto del test — e
riconoscerle era metà del punto della misura. A ne riconosce metà (50,0%), B poco più
(57,1%), **C nessuna**.

Va detto che il metro qui è severo e coerente: le 11 `parziale` non sono errori, sono
risposte vere a metà. Ma su questo tipo di domanda **metà non basta**, ed è lo stesso
criterio con cui sono state giudicate A e B.

---

## 12. Le allucinazioni: poche, ma concentrate dove fanno danno

25 su 282 (8,9%). Non è il difetto quantitativamente dominante, ma la distribuzione è
sfavorevole: cadono su **sicurezza alimentare, igiene, adempimenti e denaro**.

| id | Cosa afferma | Perché pesa |
|---|---|---|
| **Q078** | dà per riuscito un lavaggio CIP finito in `ESITO=ABORT` per conducibilità bassa in fase soda | evento di sicurezza alimentare dichiarato conforme |
| **Q190** | «la situazione igienica non è rientrata» dopo il ricambio originale | i tamponi del 25/05 danno 24 e 2 UFC/cm², **conformi** |
| **Q094** | nega cinque rotture di stock registrate | tocca l'OTIF, quindi le penali contrattuali |
| **Q144** | «nessun corso è scaduto da più di un mese» | un preposto è scaduto dal 15/09/2025, un'addetta primo soccorso dall'08/02/2026 |
| **Q272** | attribuisce al laboratorio una conferma sull'origine del frammento | il rapporto dichiara che l'attribuzione esula dalle sue competenze |
| **Q116** | «290.000,00 + 304.500,00 = 594.500,00» | IVA al 105%; le due milestone successive sono invece copiate esatte |
| **Q281** | «non esistono documenti in doppia copia» | l'archivio ne contiene **quattro coppie** |

### 12.1 ⚠️ L'allucinazione persistente — il rischio-tipo per l'audit

> **Q193 e Q265: una fattura Pakmatic da 4.912 €. Il numero non esiste in nessun
> documento, ed è lo stesso in due punti diversi del giro.**

**È l'unico difetto di questa misura che va segnalato come rischio-tipo e non come caso
singolo**, e il motivo è la sua *forma*, non la sua gravità:

- **è riproducibile** — non è un errore casuale che a un secondo tentativo sparisce: è una
  costante del modello a temperatura 0 su quel contesto, e rifare l'interrogazione dà lo
  stesso numero;
- **è plausibile** — 4.912 € è un importo credibile per quella fornitura, e nulla nella
  risposta segnala un'invenzione;
- **è coerente con sé stesso** — due domande indipendenti, lo stesso importo. Un revisore
  che incrociasse le due risposte troverebbe una **conferma**, e la coerenza fra fonti
  diverse è esattamente il segnale che si usa per fidarsi di un dato.

**Davanti a un auditor è lo scenario peggiore possibile**, peggiore di un errore
grossolano: un errore evidente si scarta, un numero inventato coerente e ripetuto entra
nel verbale. È il caso che giustifica da solo la regola commerciale di `metodo_04` §11 —
**si vende la tracciabilità, non la correttezza**: ogni affermazione risale a un passaggio
e a un file, e **chi firma verifica sul file**. La pipeline riduce il tempo di ricerca;
non solleva nessuno dalla verifica.

⚠️ Che la traccia di Q193 e Q265 esista e contenga i passaggi consegnati è ciò che rende
questo difetto **diagnosticabile in trenta secondi** invece che invisibile: si apre la
traccia e si vede che 4.912 non c'è. È l'argomento della tracciabilità, provato sul suo
caso peggiore.

### 12.2 Due errori di sostanza non allucinati, ma altrettanto gravi

- **Q203** — alla domanda se l'investimento stia dentro a quanto approvato dal CdA
  risponde «è stato approvato dal Consiglio di Amministrazione», lasciando intendere di
  sì. Il tetto deliberato è 319.000 €, il quadro economico 413.316: **serve una nuova
  delibera, e la risposta la nasconde.**
- **Q248 / Q251** — costruzione sintattica difettosa: «Non è ricavabile dai documenti
  forniti se non che Aurora ha la certificazione ISO 14001». Letta alla lettera, la frase
  **afferma** ciò che il modello voleva negare — su una certificazione e su un fatto
  patrimoniale.

### 12.3 Dove il sistema tiene, e va registrato

Sulle `non_rispondibile` **resiste alle esche**, che erano costruite bene: non spaccia il
consuntivo gestionale per bilancio 2026 (Q245), non deduce il vincitore ERP dal confronto
fra le due offerte (Q253), non attribuisce a nessuno il ruolo di referente privacy
lasciato «da nominare» (Q254), non fornisce una ragione sociale per il concorrente
pugliese di cui esiste solo un'iniziale (Q264), non scambia il codice operatore
`IT BIO 006` per il certificato ICEA dell'azienda (Q267).

⚠️ Con la riserva del §0: **è astensione costante, non discernimento.**

---

## 13. I guasti di formato sono DIFETTI NOTI DELLO STRUMENTO CONGELATO

Registrati per l'audit. **Non hanno pesato sul giudizio**, che è sempre sul contenuto.

### 13.1 Le tre anomalie preannunciate, tutte confermate

| Difetto | Dove |
|---|---|
| Una risposta **vuota** | Q204 (costo complessivo del reclamo) |
| Dodici risposte **senza fonti**, in diversi casi coi nomi dei file riversati nel corpo | Q046, Q084, Q100, Q110, Q134, Q140, Q142, Q197, Q204, Q208, Q217, Q244 |
| Scala `confidenza` a due soli valori (`alta`/`bassa`, mai `media`) | tutte le 282 |

### 13.2 Quattro difetti non preannunciati

| Difetto | Dove |
|---|---|
| **Segnaposto letterale restituito come risposta** | Q205 (`<la risposta></la risposta>`) e Q282 (`<la risposta>CONFIDEZZA: bassa</la risposta>`, col campo storpiato) |
| **Degenerazione in loop** | Q208 ripete 23 volte la stessa frase fino al troncamento; Q268 cinque volte; Q278 sei; Q148 e Q156 ripetono ciclicamente gli elementi di una lista |
| **Campo `fonti` che esplode in frammenti** | Q183 contiene 18 voci che sono pezzi di una riga CSV di una NC estranea (`"T salita a -15"`, `"320"`, `"00"`); casi minori in Q003, Q184, Q092, Q162, Q163 (nomi di **persone** citati come fonti), Q263 |
| **Nomi di file inesistenti o storpiati** | Q193 (`Fattura_Elettronica_SDI_Inbound_Q2.txt`, singolare), Q156 (`log_lavaggio_CIP_line`, troncato), Q205 e Q282 (XML inventati) |

Più due **documenti-esca pescati dal retrieval**: Q096 cita
`Newsletter_Fiere_alimentari_2026_NON_LEGGERE.eml`, Q253 cita
`confronto_ERP_v3_DEFINITIVO_ok2.txt`.

### 13.3 ⚠️ Nessuna correzione prima della Sessione 6, e non è pigrizia

Ognuno di questi difetti sarebbe **facile da correggere**: un controllo sul segnaposto,
un tetto alle ripetizioni, un filtro sul campo `fonti`, un `stop` sul template. **Non si
tocca nulla.**

Il motivo è il principio 2 della scaletta e la regola d'oro 2: **fra il «prima» e il
«dopo» cambia una sola variabile, la forma dell'archivio.** Lo strumento resta identico —
**i suoi bug compresi**. Un runner che nella misura «dopo» filtrasse le fonti esplose o
troncasse i loop produrrebbe un delta che mescola due cause: l'archivio organizzato e lo
strumento migliorato. Sarebbe impossibile dire quale dei due ha spostato il numero, e il
lavoro di tutte le sessioni precedenti perderebbe valore.

**Dove finiscono queste correzioni.** Sono **materiale per la configurazione di
riferimento**, quella di classe 8B, e si applicano **dopo la Sessione 6** — quando il
ciclo prima/dopo è chiuso e i numeri sono al sicuro. Vanno scritte ora, mentre sono
fresche, e non applicate: questa sezione è la lista di lavoro di quel momento.

⚠️ Vale identico per il difetto di recupero del §10.2 (padrone contro derivato): si
osserva, si registra, **non si tocca il config**.

---
## 14. Le asimmetrie fra A, B e C — senza addolcirle

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
8. **Il modello del giudice — verificato, e questa asimmetria NON c'e'.** Il giudizio di C
   e' stato eseguito con `claude-opus-5`, fast mode off, in sessione separata, gli stessi
   del 14/08. Su questo asse le tre misure sono confrontabili.
9. **La regola di `fonti_corrette`.** Dichiarata ed esplicita per C, non altrettanto per
   A e B: il confronto su quel campo e' un ordine di grandezza, non una misura fine.
   Vedi §9.

---

## 15. Scostamenti da `metodo_04` decisi in questa sessione

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

## 16. Contrasto fra il prompt di sessione e `metodo_02`, e come è stato risolto

Il prompt della Sessione 3 indicava il file delle risposte come `risposte_c.jsonl`;
l'**Addendum — Configurazione C** di `metodo_02` dice `misuraC_risposte.jsonl`. Vince
`metodo_02`, come prescrive il prompt stesso, e il file si chiama
**`misuraC_risposte.jsonl`**.

Stesso addendum: «le risposte si producono a blocchi da 30 in append». Per una pipeline
automatica il blocco da 30 non ha significato — non c'è una sessione da ricaricare — ma
**la semantica che il blocco proteggeva è rispettata e rafforzata**: scrittura in append
con `fsync` a ogni riga e ripresa riga per riga, non a blocchi. Segnalato al gate.

---
---

## 17. Cosa questa misura ha insegnato, e cosa autorizza

**Tre conclusioni che i numeri reggono:**

1. **Il generatore è il collo di bottiglia, non il recupero.** 70,2% di fonti giuste
   contro 14,5% di risposte giuste: 55,7 punti di scarto. L'unico intervento che può
   spostare il risultato è sostituire il generatore lasciando la pipeline invariata.
2. **La ricerca ibrida lavora, ed è misurato.** Il 22,6% dei passaggi consegnati veniva
   solo dal ramo BM25: quasi un quarto di ciò che il generatore ha visto era invisibile
   alla ricerca semantica. Il valore della fusione non è un'affermazione di letteratura.
3. **Il difetto più pericoloso non è quello atteso.** Non le 25 allucinazioni, ma le 75
   risposte vere e non verificabili e le 11 contraddizioni nascoste su 14.

**Due conclusioni che i numeri NON reggono, e che non vanno tratte:**

- ❌ «Il RAG di produzione è peggiore del RAG semplice.» C ha un generatore da 3B e B da
  frontiera: il confronto misura i generatori, non le architetture. Per confrontare le
  architetture servirebbe C con lo stesso modello di B, e **non è stato fatto**.
- ❌ «C attraversa meglio di A e B» per via del divario `lookup`/`multi_hop` più stretto
  (14,7 punti contro ~30). È effetto pavimento: vedi §8.3.

### Proposte per la Sessione 6 — da decidere al gate, non qui

| Proposta | Perché |
|---|---|
| **C «dopo» gira su questo config, byte per byte** | è il vincolo del metodo. `AURORA_LOCALE` dà l'indice nuovo senza toccare quello della baseline; cambia solo `--corpus` |
| Riusare la **cache di estrazione** | garantisce che il testo dei grezzi copiati nel vault sia identico a quello della baseline, anche se tesseract nel frattempo cambia |
| Attendersi il guadagno maggiore su **`contraddizione` e `multi_hop`** | sono i tipi che la canonizzazione tocca direttamente: la nota-conflitto rende esplicita la divergenza che C non vede mai, e i wikilink accorciano l'attraversamento. Da scrivere in `predizioni.md` **prima** di misurare |
| Attendersi **poco o nulla** su `aggregazione` e `calcolo` | dipendono dal saper contare e sommare, che è il generatore. Se migliorassero molto, sarebbe un segnale da indagare, non da festeggiare |
| Verificare se il difetto **padrone/derivato** (§10.2) sparisce | è la previsione più netta e più falsificabile che questa misura consegna alla Sessione 6 |
| ⚠️ Decidere **prima** come conta `fonti_corrette` quando la risposta cita una nota del vault | questione già aperta nel decision log il 16/08 e ancora non decisa. Con il vault come perimetro il caso sarà frequente; **proposta: la fonte che conta resta il grezzo, la nota è navigazione** |
| ⚠️ Fissare **prima** la regola per il tasso di allucinazione | §8.3: se il giudice della «dopo» usa `allucinata` mentre quello del 14/08 non l'ha usato, la colonna non si parla. Si dichiari la definizione `allucinata + sbagliata su non_rispondibile` come quella ufficiale |

### Cosa NON si fa prima della Sessione 6

- Non si tocca `config_c.json`, il codice della pipeline né il template del prompt.
- Non si correggono i difetti di formato del §13, per quanto banali.
- Non si cambia il generatore: la configurazione di riferimento a 8B si misura **dopo**,
  e finché non è misurata non si dice che rende di più.

---

## 18. Artefatti prodotti

| Percorso | Cosa |
|---|---|
| `misuraC_risposte.jsonl` | le 282 risposte |
| `valutazione_c.jsonl` | i 282 giudizi |
| `giudice_rapporto_c.md` | il rapporto discorsivo del giudice |
| `contesti_c.jsonl` | i passaggi consegnati, in forma compatta |
| `tracce/` | 282 tracce di audit complete |
| `rapporto_run.jsonl` | i rapporti delle due passate |
| `verbale_baseline_c.md` | questo documento |
| `../verifica_run_c.py` · `../conta_passata1.py` · `../conta_esiti_abc.py` · `../metriche_abc.py` | gli script che ricontano |
| `../../05_rag_produzione/` | pipeline, config congelata, `docker-compose.yml`, requirements |
| `../../05_rag_produzione/collaudo/` | rapporti e tracce del collaudo |

**Cosa contiene una traccia:** domanda, candidati del ramo denso con i punteggi, candidati
del ramo sparso con i punteggi, esito della fusione RRF con i ranghi dei due rami, ordine
completo dopo il reranker con i voti, i passaggi consegnati al modello, il testo grezzo
della generazione, le fonti citate e quelle fuori contesto, i tempi per fase e l'impronta
della configurazione. **È il documento che si apre davanti a un auditor** — ed è ciò che
rende diagnosticabile in trenta secondi anche il caso peggiore di questa misura (§12.1).

---

## 19. Chiusura

Verbale **chiuso il 18/08/2026**. Da questo momento non si modifica: un errore che
emergesse si scrive in una nota separata e datata, accanto a questo file.

| | |
|---|---|
| Corpus | 160/160 contro `manifest_corpus_v1.1.json` |
| Config congelata | `afb5893936f27a8a6c0a276e34206a9d87b9052b21ba59f8f8f8e3817e61b0e8`, commit `d36d7ce`, pushata prima di indicizzare |
| Run | 282/282, integro, 9h 01m |
| Giudizio | 282/282, sessione separata, `claude-opus-5` fast mode OFF |
| Risultato | **14,5% sulle 282 · 7,6% sulle 251 rispondibili** |
