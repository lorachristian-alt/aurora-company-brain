# metodo_04 — RAG di produzione (Configurazione C)

> **Cos'è** · L'architettura e la costruzione passo-passo della pipeline di
> interrogazione che il cliente compra: un RAG Advanced ibrido, interamente locale.
> **Quando si usa** · Nella Sessione 3 della scaletta (costruzione + baseline C sul
> corpus grezzo) e poi in produzione sul vault canonizzato.
> **Cosa non toccare** · Dalla baseline C in poi, la configurazione è CONGELATA come
> quelle di A e B, e il padrone dei valori è **`05_rag_produzione/config_c.json`**: qui
> si spiega il perché, lì si legge il quanto. In Sessione 6 si cambia solo la cartella
> del corpus, da riga di comando.
> **Data di congelamento** · 17/08/2026. Impronta del config e hash del commit nel
> verbale della baseline C.

---

## 1. Perché questa architettura — il caso per il titolare

**Il problema che risolve.** Quando l'ispettore ATS o l'auditor BRCGS chiede «mi
ricostruisca il lotto L26130», la risposta oggi costa ore di tre persone. Con questa
pipeline costa secondi, e arriva con la catena delle fonti allegata: quale registro,
quale bolla, quale log, riga per riga. La richiesta BRCGS di rintracciabilità
(mass balance entro 4 ore) si chiude in minuti, con evidenze citate.

**Perché una catena di montaggio e non un agente.** Un agente decide da solo come
cercare: è più intelligente (la nostra misura A lo dimostra) ma ogni volta può
prendere una strada diversa. Questa pipeline fa SEMPRE la stessa strada, negli stessi
passaggi, con gli stessi parametri: come una linea di confezionamento, si può
validare una volta e ispezionare sempre.

**Cosa si garantisce, detto con precisione** (le parole contano, davanti a un auditor):

- il RECUPERO è deterministico: stessa domanda + stesso indice + parametri congelati
  → stessi passaggi recuperati, nello stesso ordine, riproducibili — e la traccia di
  audit lo dimostra, perché contiene i punteggi dei due rami, l'esito della fusione e
  l'ordine dopo il reranker;
- la RISPOSTA è vincolata ai passaggi recuperati e generata a temperatura 0: la
  garanzia che si vende è la **tracciabilità** (ogni affermazione → passaggio → file),
  non l'identità carattere per carattere del testo. Promettere «risponde sempre con le
  stesse parole» è una promessa che un auditor può smontare; «ogni risposta è
  riproducibile e documentata nel registro delle interrogazioni» è una promessa che
  regge.

**GDPR e segreto industriale.** Tutto ciò che elabora, indicizza e risponde gira
dentro le mura: nessun documento, nessun frammento, nessuna domanda esce verso un
cloud. Le fonti cloud già in uso in azienda (es. Notion) sono trattate SOLO in
entrata: la pipeline le legge e le porta dentro, mai il contrario.

**Nota terminologica.** In letteratura «Modular RAG» indica un'architettura
componibile, non «improvvisazione»: il contrasto corretto da usare col cliente è
**pipeline deterministica** (questa) contro **retrieval agentico** (la nostra
configurazione A) — più accurato sulle domande difficili, ma non ispezionabile passo
per passo e con costi per interrogazione.

---

## 2. La catena di montaggio

```
INGESTIONE  →  INDICE  →  INTERROGAZIONE  →  RISPOSTA  →  REGISTRO
```

1. **Ingestione** (Python, locale): cartella-inbox sorvegliata → estrazione testo
   (§5, regole per tutti gli 11 formati) → cache su disco con chiave = SHA-256 del file
   → chunking consapevole della struttura → metadati per chunk **ricavati dal corpus**.
   Sul vault canonizzato il chunking è naturale: **una nota atomica = un chunk**, col
   frontmatter che diventa metadato filtrabile.
2. **Indice** (Qdrant): vettori densi `bge-m3` + vettori sparsi BM25 nella stessa
   collezione; payload = metadati; telemetria disattivata; snapshot periodici. Dettaglio
   critico: il tokenizzatore sparso NON deve spezzare i codici (`L26130-L1-T2`,
   `MV26-0429A`, `AF-SN-0450`) — tokenizzazione custom che emette il composto intero
   **e** le sue parti.
3. **Interrogazione**: query → top-k densi + top-k sparsi → **RRF** → **cross-encoder**
   multilingue → top-n finale.
4. **Risposta**: LLM locale via Ollama, temperatura 0, prompt fisso con le stesse
   regole della misura B: rispondi SOLO dai passaggi; cita i file; se il dato non c'è
   dichiara «non presente»; se i passaggi divergono riporta il conflitto.
5. **Registro**: ogni interrogazione in `registro/AAAA-MM.jsonl` — timestamp, domanda,
   passaggi con punteggi, risposta, fonti. È il documento che si apre davanti
   all'auditor: l'orchestrazione è Python deterministico, l'LLM interviene solo
   all'ultimo passo e solo sul materiale recuperato. In sede di misura il registro
   prende la forma di una traccia per domanda in `tracce/`.

**Dove la fusione RRF viene calcolata, e perché.** In Python, non lato Qdrant. Serve
avere in mano le due classifiche separate, coi loro punteggi, per scriverle nella
traccia: la tracciabilità è l'argomento di vendita, la riga di codice in meno no.

---

## 3. Componenti e ruoli

| Componente | Ruolo | Nota |
|---|---|---|
| Qdrant | Motore di produzione (config C) | ibrido denso+sparso nativo, filtri sui payload, snapshot |
| Chroma | **Metro** (config B, congelata) | non si tocca e non si migra: serve al confronto prima/dopo |
| `BAAI/bge-m3` | Embedding densi | **la stessa copia congelata su disco** della config B, apposta: il confronto B/C isola l'architettura |
| BM25 (sparse) | Ricerca lessicale su codici e keyword | scritto a mano, tokenizzazione custom, pesi esportati come vettori sparsi |
| RRF | Fusione delle due classifiche | deterministico, senza pesi da tarare |
| `BAAI/bge-reranker-v2-m3` | Selezione finale dei passaggi | cross-encoder multilingue, self-hosted |
| Ollama + LLM locale | Generazione della risposta | temperatura 0, prompt fisso, `num_ctx` allineato al budget |
| Tesseract (`ita`) | OCR delle scansioni | undicesimo formato; soglia dichiarata, output in cache |
| UI minima | Open WebUI in LAN, oppure CLI | niente account esterni |
| Notion API (sola lettura) | Fonte inbound | i dati entrano, mai escono (§10) |

⚠️ **Sostituzione del reranker rispetto alla versione del 15/08/2026.** Il documento
diceva `BAAI/bge-reranker-large`: **si sostituisce con `BAAI/bge-reranker-v2-m3`**, e il
motivo è la copertura linguistica. Il `large` è addestrato su inglese e cinese; su un
archivio italiano è lo strumento sbagliato, e il reranker è proprio il pezzo che deve far
vincere C su B. La `v2-m3` è multilingue e appartiene alla stessa famiglia
dell'embedding `bge-m3`: le due fasi guardano il testo con lo stesso vocabolario.

---

## 4. Due livelli, e non si confondono mai

Il generatore è **l'unico parametro dichiarato dipendente dall'hardware**. Tutto il resto
della pipeline — estrazione, chunking, embedding, BM25, RRF, reranker, prompt, tracce —
è identico nei due livelli.

| | Livello **RIFERIMENTO** (produzione) | Livello **MISURATO** (baseline C) |
|---|---|---|
| Hardware | 16-32 GB RAM, GPU consumer 8-12 GB | 8 GB RAM, CPU 4 core, nessuna GPU |
| Generatore | classe 8B (es. `llama3.1:8b`) | classe 3B (valore esatto in `config_c.json`) |
| Misurato? | **NO** | **SÌ**, sulle 282 domande |

**Come si citano i numeri di C, sempre, senza eccezioni: «pavimento, non tetto —
misurato sull'hardware minimo».** La macchina di misura sta *sotto* la fascia minima che
questo stesso documento dichiara al §8, e il generatore è più piccolo di quello di
riferimento. Un numero di C non va mai presentato come il massimo che l'architettura può
dare: è il minimo garantito da un portatile.

**E il livello di riferimento non si racconta come misurato.** Finché non gira su una
macchina con 16 GB e una GPU, del livello di riferimento si dice che è la
configurazione consigliata, non che rende di più: nessuno l'ha contata.

---

## 5. Estrazione, formato per formato

Il corpus v1 ha **11 formati** (conteggio dal manifest: 51 `.txt`, 30 `.csv`, 27 `.pdf`,
15 `.xlsx`, 12 `.eml`, 11 `.docx`, 4 `.jpg`, 4 `.pptx`, 3 `.log`, 2 `.xml`, 1 `.p7m`).

**Regola generale: sui dieci formati non-immagine, C legge gli stessi byte di B, con la
stessa funzione.** È la `text_of` del §5-bis di metodo_01, copiata alla lettera. Se
l'estrattore cambiasse, la differenza fra B e C smetterebbe di essere l'architettura.

| Formato | Come si estrae | Nota |
|---|---|---|
| `.txt` `.csv` `.log` `.xml` `.p7m` | byte grezzi, decodifica utf-8 → cp1252 → latin-1 | il `.p7m` è un contenitore, non una firma valida: si legge come testo, e ciò che si trova è quello |
| `.pdf` | `pypdf`, `extract_text()` pagina per pagina | **sonda del 17/08/2026: tutti i 27 PDF danno testo, nessuno sotto i 200 caratteri alfanumerici.** Non ci sono scansioni cieche fra i PDF, quindi il ramo OCR per i PDF non esiste: sarebbe codice non esercitato |
| `.docx` | `python-docx`: paragrafi **più** celle di tabella | senza le celle, mezzo documento sparisce |
| `.xlsx` | `openpyxl` con `data_only=True`, tutti i fogli, riga per riga | le formule non calcolate tornano `None` e vengono saltate: è un limite noto del corpus, non della pipeline |
| `.pptx` | `python-pptx`: testo delle forme, tabelle **e note del relatore** | le note contengono spesso il fatto vero |
| `.eml` | `BytesParser`: intestazioni, corpo (plain, poi html), **nomi degli allegati** | è il ramo che si dimentica sempre |
| `.jpg` | **OCR tesseract, lingua `ita`** | l'unica differenza di estrazione fra B e C — vedi sotto |

### 5.1 L'OCR, e la soglia che separa una scansione da una fotografia

**Perché l'OCR è attivo.** Una pipeline che non legge una non conformità scansionata non
è vendibile a un'azienda alimentare: la scansione è il formato che in produzione arriva
più spesso. E metodo_02 registra che la cecità di B sui 4 `.jpg` gonfia il delta A-B.

**Il rischio, però, è opposto e va gestito**: l'OCR produce testo utile su un modulo
scansionato e produce rumore su una fotografia di un frammento. Il rumore in un indice
costa due volte — occupa un posto nel top-k e porta il generatore fuori strada.

Quindi si dichiara una **soglia di testo utile** (valori esatti in `config_c.json`):
sopra soglia il testo entra nell'indice; **sotto soglia il file entra con la sola scheda
di metadati** — nome, formato e perché non c'è testo — e il verbale della misura elenca
quali file ci sono finiti. La soglia guarda due cose insieme, i caratteri alfanumerici
estratti e la confidenza media di tesseract: un modulo A4 scansionato produce migliaia di
caratteri sopra 70 di confidenza, la foto di un frammento qualche decina di token a 30-40.

**La cache dell'estrazione non è un'ottimizzazione, è determinismo.** Ogni estrazione
finisce su disco con chiave = SHA-256 del file grezzo, in `_locale_non_su_github/`.
**La Sessione 6 riusa la stessa cache**: lo stesso file non si ri-estrae mai con una
versione diversa dello strumento. Senza, un aggiornamento di tesseract fra agosto e
ottobre cambierebbe il corpus in silenzio, e i due lati del confronto misurerebbero testi
diversi. La versione di tesseract va a verbale.

**I chunk nati dall'OCR portano `origine: ocr` nel payload e nella traccia**, così ogni
risposta che ne dipende è riconoscibile a colpo d'occhio.

### 5.2 Nessun file resta invisibile

Un file che non produce testo utile — scansione sotto soglia, o il lock file di Word che
è rumore realistico e va lasciato dov'è — **entra comunque nell'indice con una scheda**:
nome, formato, e perché il contenuto non è leggibile. La scheda non afferma nulla sul
contenuto. Serve a un principio solo: un file che sparisce dall'indice non è
raggiungibile da nessuna domanda, nemmeno da quella che chiede cosa contiene l'archivio.

### 5.3 Due scostamenti dalla versione del 15/08, con il motivo

- **Il dedup con hash NON si applica.** Il documento lo prevedeva. Su questo corpus i
  duplicati sono **contenuto** (metodo_01 §11 e regola d'oro 1: le anomalie
  dell'archivio sono contenuto), e fonderli cancellerebbe dall'indice le prove che le
  domande sull'inventario cercano. Il payload porta comunque `testo_sha256`: chi vuole
  deduplica al momento della risposta, non dentro l'indice.
- **Il canone e la tabella alias NON entrano nei metadati.** Il documento prevedeva
  «lotti ed entità riconosciute via canone» e la tabella alias per le varianti OCR.
  Iniettare nell'indice fatti che il corpus grezzo non contiene misurerebbe un archivio
  già in parte organizzato — cioè esattamente ciò che la Sessione 6 deve misurare
  *dopo*. I metadati della baseline C si ricavano **solo dal testo**: codici e date per
  espressione regolare. Nel vault, `tipo` e `area` arriveranno dal frontmatter delle
  note, che è il posto giusto. La tabella alias resta un punto di estensione dichiarato,
  da valutare in Sessione 6 come variabile a sé.

---

## 6. La specifica di determinismo

1. Versioni pinnate in `requirements.txt`; modelli scaricati una volta e **congelati su
   disco**, non ri-risolti da un nome remoto a ogni avvio.
2. **`config_c.json` unico e congelato**: chunking, k dei due rami, parametro della RRF,
   top-in e top-out del reranker, prompt di generazione, temperatura 0, seed, thread e
   batch. Sì, anche thread e batch: cambiano l'ordine delle somme in virgola mobile.
3. **Impronta del config** (SHA-256 su tutte le chiavi tranne `meta` e `misura`): finisce
   nel manifest dell'indice e in ogni traccia. Se qualcuno tocca un valore, l'indice
   esistente non si aggiorna in silenzio — il codice si ferma e lo dice.
4. **Manifest dell'indice**: hash del config, corpus di provenienza, conteggi per formato
   e per origine, modelli, data. Un indice senza manifest non è misurabile: non si sa più
   su cosa.
5. **Cache dell'estrazione con chiave = SHA-256 del grezzo** (§5.1).
6. Ogni modifica è una NUOVA versione dichiarata nel decision log; mai cambiare nulla
   a metà di un confronto.
7. Ogni interrogazione lascia una traccia. Nessuna risposta senza fonti.

**Il runner della misura gira a DUE PASSATE, ed è una conseguenza dell'hardware.**
Passata 1: recupero, fusione e rerank per tutte le domande, tracce su disco. Passata 2:
sola generazione, con embedder e reranker scaricati dalla memoria e solo Ollama
residente. Su 8 GB i tre modelli non convivono — 2,3 + 2,3 + 2,0 GB più Qdrant e Python
— e una macchina che pagina moltiplica i tempi. **Il risultato per domanda è identico a
quello di una pipeline che gira tutta d'un fiato: cambia l'ordine in cui si pagano i
passi, non cosa viene calcolato.** Entrambe le passate sono riprendibili riga per riga,
con `fsync` a ogni scrittura: un'interruzione costa al massimo la domanda in corso.

---

## 7. Costruzione passo-passo (Sessione 3)

- **S3.1 Ambiente** · Python + `requirements.txt` pinnate; Ollama (installer Windows) e
  `ollama pull` del modello del config; tesseract con pacchetto lingua `ita`; bge-m3
  **riusando la copia congelata** in `04_misurazioni\_locale_non_su_github\modelli\bge-m3`;
  reranker congelato in `05_rag_produzione\_locale_non_su_github\modelli\`. Qdrant in
  modalità locale su file per la misura, `docker-compose.yml` per la produzione.
- **S3.2 Verifica del corpus** · `pipeline\verifica_corpus.py`: 160/160 contro
  `manifest_corpus_v1.1.json`, o non si indicizza. Nessun numero senza manifest.
- **S3.3 Ingestione** · `pipeline\ingestione.py`: estrazione con cache, chunking,
  metadati, `chunk.jsonl` più il rapporto coi conteggi per formato e per origine.
- **S3.4 Indicizzazione** · `pipeline\indicizza.py`: BM25 su tutto il corpus, embedding
  densi, upsert in Qdrant, manifest dell'indice. Riprendibile: l'embedding è il passo caro.
- **S3.5 Collaudo** · `pipeline\collaudo.py`: 10 domande scritte a mano leggendo il
  corpus, **mai dall'eval set**. Verifica che i pezzi girino e che ogni formato sia
  raggiungibile. ⚠️ Un difetto si corregge; un parametro NON si tocca (§12).
- **S3.6 Sonda dei tempi** · le stesse 10 domande cronometrate end-to-end → stima onesta
  per 282, e la decisione se lanciare il run.
- **S3.7 BASELINE C ufficiale** · `pipeline\runner_misura.py`, due passate, sulle 282 di
  `03_valutazione\domande_solo.jsonl`. Protocollo di metodo_02, addendum C. PRIMA della
  canonizzazione: è l'ultima finestra utile. La valutazione la fa una sessione diversa,
  con P3 e `misura = C`.
- **S3.8 Notion inbound** · documentato come punto di estensione (§10), non costruito:
  nel corpus v1 non c'è contenuto Notion da misurare.

---

## 8. Hardware, senza favole

| Fascia | Cosa serve | Cosa aspettarsi |
|---|---|---|
| **Misura (17/08/2026)** | 8 GB RAM, i7-1065G7 4 core, nessuna GPU | tutto funziona a due passate; generatore di classe 3B; ore, non secondi |
| Minima consigliata | 16 GB RAM, CPU 8 core | generatore di classe 8B; reranking e generazione lenti (decine di secondi) |
| Consigliata | GPU consumer 8-12 GB (es. RTX 4060/4070) | risposte in pochi secondi; macchina completa 1.500-2.500 € una tantum |

La macchina della baseline C **sta sotto la fascia minima**, ed è per questo che i numeri
di C si citano come pavimento (§4). Non è un difetto della misura: è un'informazione che
va detta, perché un cliente che compra la fascia consigliata ottiene di più, non di meno.

---

## 9. Runbook per le 1-2 figure IT

Scritto per chi tiene in piedi la rete e i backup, non per uno specialista di AI.
Nessun passo qui sotto richiede di capire come funziona un embedding.

**Settimanale** (15 minuti)
- Spazio disco sulla partizione dell'indice: sotto il 15% libero, si allarga.
- Snapshot Qdrant: `curl -X POST http://127.0.0.1:6333/collections/<collezione>/snapshots`
  con l'header della chiave API; lo snapshot finisce nel volume `qdrant_snapshot`.
  Si copia fuori macchina come qualunque altro backup.
- Rotazione del registro delle interrogazioni: il file del mese chiuso si archivia.

**Mensile** (mezz'ora)
- Ingestione incrementale della inbox: si lancia l'ingestione, che rilegge solo i file
  nuovi (la cache tiene il resto) e reindicizza.
- **Prova di ripristino**: si ripristina uno snapshot su una collezione di prova e si
  fanno tre domande di controllo. Un backup mai ripristinato non è un backup.

**Trimestrale** (mezza giornata)
- Aggiornamento delle versioni pinnate **prima su macchina di prova**, poi in produzione.
- Rilancio del collaudo: le 10 domande devono continuare a tornare gli stessi file.
- Nuova voce nel decision log, con la data e cosa è cambiato.

**Sempre**
- Il servizio è esposto **solo in LAN** (in `docker-compose.yml` le porte sono legate a
  `127.0.0.1`: per aprirlo alla rete interna si mette l'IP del server, **mai** `0.0.0.0`).
- Chiave API di Qdrant in un file `.env` accanto al compose, mai dentro il compose e mai
  su git.
- Telemetrie disattivate; nessun dato verso l'esterno.

**Checklist della notte, quando gira un run lungo**
1. Riavvio della macchina.
2. Browser, IDE ed editor chiusi: su 8 GB ogni finestra aperta è RAM tolta al modello.
3. Alimentazione collegata.
4. Sospensione e ibernazione disattivate (`powercfg /change standby-timeout-ac 0`).
5. OneDrive in pausa e aggiornamenti di Windows rimandati: un riavvio automatico a metà
   run costa la notte.
6. Il runner scrive in append con `fsync`: se qualcosa va storto si riprende, non si
   ricomincia.

---

## 10. Notion: fonte inbound, e nient'altro

**Cosa significa «inbound».** La pipeline legge Notion in **sola lettura** e ne porta il
contenuto dentro l'indice. Non scrive su Notion, non ci manda domande, non ci manda
risposte, non ci manda frammenti di documenti. È il pattern coerente col pitch GDPR: i
dati entrano, non escono.

**Dove si aggancia.** All'ingestione (§2, punto 1), come una qualsiasi altra sorgente:
un lettore che scarica le pagine, le converte in testo e le deposita nella cartella di
lavoro **prima** del passo di estrazione. Da lì in poi seguono la stessa strada di ogni
altro documento — chunking, metadati, indice — e portano nel payload la pagina di
origine invece del nome file.

**Perché non si costruisce ora.** Nel corpus v1 non c'è contenuto Notion da misurare, e
aggiungerne uno significherebbe aggiungere fatti nuovi a un corpus congelato. Fatti nuovi
solo da corpus v2 (decisione del 15/08/2026). Costruire un lettore che non ha niente da
leggere sarebbe codice non esercitato — lo stesso motivo per cui non esiste il ramo OCR
per i PDF.

---

## 11. Onestà commerciale: cosa si promette e cosa no

**Sul determinismo.**

| Si promette | Non si promette |
|---|---|
| Il recupero è deterministico e la traccia lo dimostra: stessi passaggi, stesso ordine, stessi punteggi | Che la risposta sia identica carattere per carattere |
| La risposta è vincolata ai passaggi recuperati, e ogni affermazione risale a un file | Che il modello non sbagli mai a leggere un passaggio |
| A temperatura 0 e seed fisso la generazione è stabile | Il bit-per-bit: cambiano libreria, driver o versione del modello e il testo può cambiare |

La frase da usare davanti a un auditor è: **«ogni risposta è riproducibile e documentata
nel registro delle interrogazioni»**. Quella da non usare è «risponde sempre allo stesso
modo».

**Sui costi.** «Costo di esercizio trascurabile» è difendibile. **«Costo zero» no.**

| Voce | Cosa costa davvero |
|---|---|
| Licenze e token | zero: modelli aperti, tutto in locale |
| Hardware | una tantum, 1.500-2.500 € per la fascia consigliata |
| Energia | una macchina accesa, con reranker e LLM che usano la CPU o la GPU sotto carico |
| Manutenzione | mezza giornata IT a trimestre, più i 15 minuti settimanali del runbook |
| Il primo indice | ore di calcolo, una volta sola (sulla macchina di misura: vedi verbale) |

**Sulla misura.** I numeri di C sono un pavimento (§4). Il confronto A/B/C mette a
paragone **tre strumenti diversi**, non tre versioni dello stesso: A è un agente che apre
i file, B è un RAG a embedding senza rerank su Chroma, C è una pipeline ibrida con
reranker su Qdrant e un generatore locale piccolo. Le asimmetrie note si elencano nel
verbale, senza addolcirle.

**Sulle fonti citate, una regola che costa a C e si tiene lo stesso.** Il runner scrive
nel file di risposte **tutti** i nomi che il modello ha citato, compresi quelli che non
erano fra i passaggi consegnati e quelli che non esistono. Filtrarli sarebbe tecnicamente
facile e metodologicamente disonesto: in A e in B il giudice vede le fonti come il
modello le ha scritte, e P3 classifica come `allucinata` proprio la fonte citata che non
contiene il dato. Ripulire quelle di C le darebbe meno allucinazioni per costruzione, e i
tre numeri smetterebbero di parlarsi. I nomi fuori contesto vengono comunque contati e
finiscono nella traccia e nel verbale, come diagnostica.

---

## 12. Cosa non fare, mai

- Rispondere senza fonti, o fuori dai passaggi recuperati.
- Cambiare un parametro fra una misura e l'altra.
- **Regolare un parametro guardando i risultati del collaudo.** Il collaudo trova
  difetti — crash, formati non letti, fusione rotta — e i difetti si correggono. Se fa
  venire voglia di spostare un `k`, la risposta è no: si segnala al gate.
- Migrare la config B su Qdrant «per pulizia»: è il metro, non il motore.
- Esporre il servizio fuori dalla LAN o attivare telemetrie.
- Indicizzare `03_valutazione\` (le risposte del test): mai, in nessun indice.
- Committare pesi, indici o cache: stanno in `_locale_non_su_github\`, che è gitignorata.
- Presentare il livello di riferimento come se fosse stato misurato.

---

## Configurazione C — dove stanno i parametri

⚠️ **La tabella dei valori non è più qui.** Il padrone è
**`05_rag_produzione/config_c.json`**, congelato il **17/08/2026**: un fatto ha un
padrone solo, e un numero ricopiato in due posti diventa due numeri diversi nel giro di
un mese. Questo documento tiene i *perché*; il config tiene i *quanto*, con il perché di
ciascun valore accanto, nella chiave `_perche`.

Si legge così:

```
python 05_rag_produzione\pipeline\impronta.py      # l'hash di congelamento
type   05_rag_produzione\config_c.json             # i valori, col perché accanto
```

**Struttura del config**, per sapere dove guardare:

| Sezione | Cosa tiene |
|---|---|
| `esecuzione` | device, thread, batch — fissati perché cambiano le somme in virgola mobile |
| `estrazione` | regole per gli 11 formati, OCR e soglia, cache, scheda, dedup disattivato |
| `chunking` | caratteri, overlap, taglio (identici a B) |
| `embedding_denso` | modello, percorso della copia congelata, dimensioni, troncamento |
| `ricerca_sparsa` | BM25: `k1`, `b`, tokenizzazione |
| `indice` | motore, modalità, collezione, nomi dei due vettori, payload |
| `recupero` | k del ramo denso, k del ramo sparso, k della RRF |
| `reranker` | modello, top-in, top-out, `max_length`, batch |
| `generazione` | modello Ollama col tag esatto, temperatura, seed, `num_ctx`, `keep_alive`, budget di contesto, template del prompt |
| `tracce` | cosa finisce nella traccia di audit |
| `misura` | cartella e nome del file di risposte — **le sole chiavi che la Sessione 6 cambia**, ed escluse dall'impronta |
