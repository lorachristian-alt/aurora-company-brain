# metodo_04 — RAG di produzione (Configurazione C)

> **Cos'è** · L'architettura e la costruzione passo-passo della pipeline di
> interrogazione che il cliente compra: un RAG Advanced ibrido, interamente locale.
> **Quando si usa** · Nella Sessione 3 della scaletta (costruzione + baseline C sul
> corpus grezzo) e poi in produzione sul vault canonizzato.
> **Cosa non toccare** · Dopo la baseline C, la tabella dei parametri in fondo è
> CONGELATA come quelle di A e B: si adatta solo il percorso del corpus.

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
  → stessi passaggi recuperati, nello stesso ordine, riproducibili;
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

**Costi, detti onestamente.** Zero costi per token e licenze; hardware una tantum
(fascia in §6); manutenzione compatibile con 1-2 figure IT (runbook in §7).
«Costo di esercizio trascurabile» è difendibile; «costo zero» no: c'è corrente,
backup e mezza giornata IT a trimestre.

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

1. **Ingestione** (Python, locale): cartella-inbox sorvegliata → estrazione testo con
   `text_of` (metodo_01 §5-bis) → OCR locale (tesseract) per le scansioni →
   chunking consapevole della struttura → dedup con hash (stessa logica del manifest)
   → metadati per chunk: file di origine, tipo, area, data, lotti ed entità
   riconosciute via canone. Sul vault canonizzato il chunking è naturale:
   **una nota atomica = un chunk**, col frontmatter che diventa metadato filtrabile.
2. **Indice** (Qdrant self-hosted): vettori densi `bge-m3` + vettori sparsi BM25
   nella stessa collezione; payload = metadati; telemetria disattivata; snapshot
   periodici. Dettaglio critico: il tokenizzatore sparso NON deve spezzare i codici
   (`L26130-L1-T2`, `MV26-0429A`, `AF-SN-0450`) — pattern di tokenizzazione custom,
   più la tabella alias del canone per le varianti OCR (`O39847lOZ3O` → `03984710230`).
3. **Interrogazione**: query → top-20 densi + top-20 sparsi → **RRF** (k=60) → top-8 →
   **cross-encoder** `BAAI/bge-reranker-large` (self-hosted) → top-4.
4. **Risposta**: `Llama-3.1-8B` via Ollama, temperatura 0, prompt fisso con le stesse
   regole della misura B: rispondi SOLO dai passaggi; cita i file; se il dato non c'è
   dichiara «non presente»; se i passaggi divergono riporta il conflitto.
5. **Registro**: ogni interrogazione in `registro/AAAA-MM.jsonl` — timestamp, domanda,
   passaggi con punteggi, risposta, fonti. È il documento che si apre davanti
   all'auditor: l'orchestrazione è Python deterministico, l'LLM interviene solo
   all'ultimo passo e solo sul materiale recuperato.

---

## 3. Componenti e ruoli

| Componente | Ruolo | Nota |
|---|---|---|
| Qdrant (self-hosted) | Motore di produzione (config C) | ibrido denso+sparso nativo, filtri sui payload, snapshot |
| Chroma | **Metro** (config B, congelata) | non si tocca e non si migra: serve al confronto prima/dopo |
| `BAAI/bge-m3` | Embedding densi | lo stesso di B, apposta: il confronto B/C isola l'architettura |
| BM25 (sparse) | Ricerca lessicale su codici e keyword | tokenizzazione custom per i codici |
| RRF (k=60) | Fusione delle due classifiche | deterministico, senza pesi da tarare |
| `bge-reranker-large` | Selezione finale dei passaggi | cross-encoder self-hosted |
| Ollama + `Llama-3.1-8B` | Generazione della risposta | temperatura 0, prompt fisso |
| UI minima | Open WebUI in LAN, oppure CLI | niente account esterni |
| Notion API (sola lettura) | Fonte inbound simulata | i dati entrano, mai escono |

---

## 4. La specifica di determinismo

1. Versioni pinnate in `requirements.txt` (lock); modelli scaricati una volta,
   congelati su disco, con checksum registrati.
2. `config.yaml` unico e congelato: chunking, k, parametri RRF, top-n del reranker,
   prompt di generazione, temperatura 0, seed.
3. Indice con manifest: hash dei contenuti indicizzati + data di costruzione.
4. Ogni modifica è una NUOVA versione dichiarata nel decision log; mai cambiare nulla
   a metà di un confronto.
5. Ogni interrogazione lascia una riga nel registro. Nessuna risposta senza fonti.

---

## 5. Costruzione passo-passo (Sessione 3 — dal terminale, in `05_rag_produzione\`)

- **S3.1 Ambiente** · venv Python + `requirements.txt`; Qdrant (Docker o binario);
  `ollama pull llama3.1:8b`; download di bge-m3 (riusare la copia congelata in
  `04_misurazioni\_locale_non_su_github\modelli\bge-m3`) e del reranker; checksum di
  tutto nel decision log.
- **S3.2 Ingestione** · script inbox → chunk → metadati (riusa `text_of`; OCR per le
  scansioni; dedup con hash).
- **S3.3 Indicizzazione del corpus v1** · il corpus congelato (verificato contro il
  manifest) entra nella collezione Qdrant; snapshot e manifest dell'indice.
- **S3.4 Catena di interrogazione** · ibrido → RRF → rerank → generazione → registro.
- **S3.5 Fumo** · 10 domande a mano, verifica della catena delle fonti passaggio per
  passaggio.
- **S3.6 BASELINE C ufficiale** · protocollo di metodo_02 (blocchi da 30, append,
  perimetri, valutazione P3 con `misura = C`) — PRIMA della canonizzazione: è l'ultima
  finestra utile. La tabella qui sotto si data e si congela quel giorno.
- **S3.7 Demo Notion inbound** · 2-3 pagine simulate con COPIE di documenti non
  sensibili già nel corpus (listini, presentazione commerciale), ingerite via API in
  sola lettura: dimostra il pattern senza aggiungere fatti nuovi. Fatti nuovi solo da
  corpus v2.

---

## 6. Hardware, senza favole

| Fascia | Cosa serve | Cosa aspettarsi |
|---|---|---|
| Minima | 16 GB RAM, CPU 8 core | tutto funziona; reranking e generazione lenti (decine di secondi) |
| Consigliata | GPU consumer 8-12 GB (es. RTX 4060/4070) | risposte in pochi secondi; macchina completa 1.500-2.500 € una tantum |

Esercizio: corrente, backup, mezza giornata IT a trimestre per gli aggiornamenti
pinnati. Nessun canone, nessun costo per token.

---

## 7. Runbook per le 1-2 figure IT

- **Settimanale** · spazio disco; snapshot Qdrant; rotazione del registro.
- **Mensile** · ingestione incrementale della inbox; prova di ripristino di un backup.
- **Trimestrale** · aggiornamento delle versioni pinnate PRIMA su macchina di prova,
  poi in produzione; nuova voce nel decision log.
- **Sempre** · servizio esposto solo in LAN; telemetrie disattivate; nessun dato verso
  l'esterno.

---

## 8. Cosa non fare, mai

- Rispondere senza fonti, o fuori dai passaggi recuperati.
- Cambiare un parametro fra una misura e l'altra.
- Migrare la config B su Qdrant «per pulizia»: è il metro, non il motore.
- Esporre il servizio fuori dalla LAN o attivare telemetrie.
- Indicizzare `03_valutazione\` (le risposte del test): mai, in nessun indice.

---

## Configurazione C — tabella dei parametri (si congela il giorno della baseline C)

| Parametro | Valore |
|---|---|
| Vector store | Qdrant self-hosted, collezione unica densa+sparsa |
| Embedding denso | `BAAI/bge-m3`, locale (stessa copia congelata della config B) |
| Ricerca sparsa | BM25, tokenizzazione custom che preserva i codici |
| Chunking (grezzi) | 1.200 caratteri, overlap 200, taglio su confine di riga (identico a B) |
| Chunking (vault) | 1 nota atomica = 1 chunk, frontmatter nei payload |
| Fusione | RRF con k=60, top-20 denso + top-20 sparso → top-8 |
| Re-ranking | `BAAI/bge-reranker-large` → top-4 |
| Generazione | `Llama-3.1-8B` via Ollama, temperatura 0, prompt della misura B (metodo_02, P2.1) |
| Metadati per chunk | file, tipo, area, data, lotti/entità dal canone |
| Registro | una riga jsonl per interrogazione, con passaggi e punteggi |
| Data di congelamento | — (si scrive alla baseline C) |
