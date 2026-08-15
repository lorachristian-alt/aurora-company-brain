# INIZIA QUI — la mappa del progetto

Questa guida serve a tre persone: te fra un anno, un collega che entra ora, e un
lettore non tecnico che vuole capire cosa sta guardando. Dieci minuti di lettura.

---

## Il progetto in 60 secondi

Le PMI hanno migliaia di documenti e nessuno trova niente. Gli strumenti AI che
«rispondono sui documenti» sono facili da montare e difficili da giudicare: alla
domanda del titolare — *funziona?* — quasi tutti rispondono con una demo.
Questo progetto risponde con un numero.

Qui dentro c'è: un'azienda alimentare **simulata** (Aurora Food Group S.r.l., non
esiste) con **159 documenti** realistici e volutamente caotici; **282 domande
d'esame** con risposte verificate una per una; le **misure del prima** (archivio
grezzo); il metodo per organizzare tutto in un «cervello aziendale» in Obsidian e
**rimisurare il dopo**; e una **pipeline RAG di produzione** che gira interamente in
locale.

La frase da ricordare: **l'archivio non è il prodotto — è lo strumento di misura.**

---

## Come si lavora (il modello operativo)

- **La chat Cowork è il cervello**: strategia, decisioni, revisione dei piani,
  scrittura dei prompt. Non esegue le sessioni operative.
- **Il terminale (Claude Code) è le mani**: ogni sessione si apre in una cartella
  precisa e incolla un prompt preciso. La cartella in cui apri il terminale È il
  perimetro: da lì il modello vede solo ciò che deve vedere.
- **Antigravity è la plancia**: l'IDE si apre sulla cartella giusta per la sessione
  (il repository per metodo e misure; il vault per la canonizzazione). Claude Code
  gira nel terminale integrato, e il perimetro lo decide la cartella del TERMINALE
  (`cd` prima di `claude`), non quella dell'IDE. L'agente nativo dell'IDE resta
  spettatore: può leggere, non scrive mai su repo o vault — le mani sono solo le
  sessioni Claude Code col loro prompt.
- Igiene dell'editor: formattazione automatica al salvataggio DISATTIVATA nel
  workspace (`editor.formatOnSave`, `files.trimTrailingWhitespace`,
  `files.insertFinalNewline` a false) e mai salvare dall'editor i file di
  `02_corpus/` o dei verbali di misura: un trim di spazi rompe gli hash del manifest.
- Ogni sessione chiude con tre gesti: stato aggiornato, voce nel
  `06_operativo/decision_log.md`, commit git.

Il piano delle sessioni, con l'ordine e gli stop-loss, sta in
`06_operativo/scaletta_end_to_end.md`. **È il primo file da riaprire dopo una pausa.**

---

## La mappa delle cartelle

| Cartella | Cosa contiene | Regola d'oro |
|---|---|---|
| `README.md` | La porta pubblica: disclaimer, progetto, risultati | i numeri solo ricontati da script |
| `00_INIZIA_QUI.md` | Questa guida | — |
| `01_metodo/` | I documenti che governano tutto: generazione (01), misurazione (02), canonizzazione (03, nascerà), RAG di produzione (04), canone | si cambia il sorgente, si rigenera il derivato |
| `02_corpus/` | I 160 file grezzi simulati (159 + avvertenza) | **INTOCCABILI**: sono il corpus congelato |
| `03_valutazione/` | Le 282 domande, le risposte, l'eval set | **MAI aprire** in sessioni che generano o rispondono |
| `04_misurazioni/` | I numeri, una cartella per misura | i verbali di misura non si modificano |
| `05_rag_produzione/` | La pipeline Qdrant (config C), dalla Sessione 3 | tutto locale, tutto nel registro |
| `06_operativo/` | Scaletta, decision log, manifest, prompt pronti | il quaderno di bordo |

Il **vault Obsidian** (`Desktop\aurora-cervello`, 11 cartelle) e il **corpus
originale di lavoro** (`Desktop\sources`) vivono FUORI dal repository. `02_corpus/`
è la copia identica del corpus, vincolata all'hash del manifest.

---

## I nomi storici (per leggere i documenti più vecchi)

| Nome storico | Oggi |
|---|---|
| `docs_PMI_blueprint.md` | `01_metodo/metodo_01_generazione_archivio.md` |
| `docs_PMI_misura.md` | `01_metodo/metodo_02_misurazione.md` |
| `CANONE_AURORA.md` | `01_metodo/canone_aurora.md` |
| `DOMANDE_RAG.md` / `RISPOSTE_RAG.md` | `03_valutazione/domande_282.md` / `risposte_282.md` |
| `file_grezzi/` | `02_corpus/` |
| `misure_aurora/` e `Desktop\misure_aurora\` | `04_misurazioni/` (baseline in `baseline_2026-08-14_grezzo/`) |
| `PROMPT_FASE1_espansione_sources.txt` | `06_operativo/prompt/prompt_corpus_v2_espansione.txt` |
| `SCALETTA_END_TO_END_corpus_v1.md` | `06_operativo/scaletta_end_to_end.md` |
| `tassonomia_vault_aurora.png` | `06_operativo/tassonomia_vault.png` |

---

## Dove siamo adesso (15/08/2026)

**Fatto:** corpus v1 congelato con manifest SHA-256; baseline A (agentico: 70,6%
corrette, 0 allucinazioni) e B (RAG semplice: 44,7%) misurate il 14/08 sul grezzo;
repository riorganizzato in questa struttura; git attivo con remote PRIVATO
`github.com/lorachristian-alt/aurora-company-brain` (pubblico solo in Sessione 7).

**Deciso** (dettagli e motivi nel decision log): l'espansione dell'archivio slitta a
corpus v2; prima si chiude il ciclo end-to-end sui 159; Chroma resta il metro della
misura B, Qdrant sarà il motore della config C; Notion entra solo come fonte inbound;
la baseline C si misura sul grezzo prima di canonizzare.

**Prossimo passo:** completare la Sessione 0 della scaletta (git, estensione mtime del
manifest, verifica del perimetro della misura «dopo»), poi Sessione 1: il manuale di
canonizzazione.

---

## Le 6 regole d'oro

1. Corpus (`02_corpus/`, `Desktop\sources`) e valutazione (`03_valutazione/`) sono
   intoccabili: le anomalie dell'archivio sono contenuto, le risposte sono l'esame.
2. Una variabile alla volta: tra un «prima» e un «dopo» cambia solo la forma
   dell'archivio, mai lo strumento.
3. Chi genera, canonizza o risponde non apre MAI `03_valutazione/`; chi valuta è
   sempre una sessione diversa da chi ha risposto.
4. I prompt congelati si copiano alla lettera: si adattano solo i percorsi.
5. Nessun numero dichiarato senza uno script che l'ha ricontato.
6. Ogni sessione chiude con stato + decision log + commit.

---

## Glossario minimo

- **Corpus** · l'insieme dei documenti grezzi simulati (160 file, 11 formati).
- **Canone** · il documento che fissa la verità della simulazione: chi è chi, cosa è
  successo, quali contraddizioni sono volute.
- **Baseline** · la misura fatta sull'archivio grezzo, prima di organizzarlo: il
  termine di paragone.
- **Eval set** · le 282 domande d'esame con risposte verificate e fonti.
- **Canonizzazione** · trasformare i documenti grezzi in note atomiche collegate
  dentro Obsidian («un fatto, un padrone»).
- **Nota atomica / hub** · una nota = una sola idea; gli hub sono le note-mappa che
  collegano le altre.
- **_index** · la nota-porta presente in OGNI cartella del vault: elenca gli hub e
  le note della cartella, così ogni documento è raggiungibile navigando i link
  (llms.txt → _index → hub → nota) e non esistono note orfane.
- **RAG** · Retrieval-Augmented Generation: il sistema recupera i passaggi rilevanti
  dai documenti e l'AI risponde SOLO su quelli.
- **Embedding** · la trasformazione del testo in numeri che ne rappresentano il
  significato, per la ricerca semantica.
- **BM25** · la ricerca «classica» per parole chiave e codici esatti.
- **RRF / reranker** · i due passaggi che fondono e raffinano i risultati delle due
  ricerche, sempre nello stesso modo.
- **Manifest** · l'impronta digitale (hash) del corpus: prova che le misure sono
  state fatte esattamente su quei file.
- **Configurazione congelata** · parametri scritti, datati e mai più toccati: è ciò
  che rende i numeri confrontabili.
