# Scaletta — primo deliverable end-to-end sul corpus v1 (159 file)

> Il corpus v1 è **CONGELATO** (`06_operativo/manifest_corpus_v1.json`). L'espansione
> dell'archivio slitta a corpus v2: il prompt è pronto in
> `06_operativo/prompt/prompt_corpus_v2_espansione.txt` e NON va usato prima della
> fine di questo ciclo. Ogni sessione operativa gira **nel terminale** (Claude Code),
> aperta nella cartella indicata; la chat Cowork è il cervello: decisioni, piani,
> prompt. Aggiornata al 15/08/2026 (riorganizzazione + configurazione C).

---

## I sette princìpi del workflow

1. **Corpus congelato + manifest.** Ogni misura è vincolata a un hash verificabile del
   corpus e a una versione del dataset di domande. Nessun numero senza manifest.
2. **Una variabile alla volta.** Tra «prima» e «dopo» cambia solo la forma
   dell'archivio: stessi 282 quesiti, configurazioni congelate (A, B e C), stesso
   modello per configurazione.
3. **Verticale prima di orizzontale.** Ogni fase nuova si prova su una fetta piccola
   end-to-end prima di industrializzarla.
4. **Ogni fase ha la sua suite di controlli rieseguibili.** Generazione ✓ (89
   controlli), misura ✓ (protocollo congelato), canonizzazione ← nasce in Sessione 1,
   produzione ← specifica di determinismo in metodo_04.
5. **Stato su disco, decision log, passaggio di consegne, git.** Ogni sessione lascia
   CINQUE gesti: stato aggiornato, decisione datata, **passaggio di consegne del
   coordinatore aggiornato**, un commit e un `git push` — il lavoro non resta mai
   su un solo disco a fine sessione. La storia del repo È la prova del metodo.

   ⚠️ **Il quinto gesto è nato tardi e per questo si scrive qui.**
   `06_operativo\passaggio_di_consegne_coordinatore.md` è l'unica casa della
   *giurisprudenza* — il modo in cui si decide ai gate — e un passaggio di consegne che
   invecchia è peggio di nessun passaggio di consegne. La regola in vigore sta nella §8 di
   quel file: **§3 «dove siamo» si riscrive sempre**, coi numeri incollati da
   `conta_stato.py`; **§4, §5 e §6 prendono una riga datata** solo se la sessione ha fissato
   un criterio nuovo, versionato uno strumento, ratificato una prassi o pagato un errore
   nuovo. Il gesto operativo per i lotti sta in `metodo_03` §9.5, passo 8.
6. **Perimetri fisici anti-contaminazione.** Chi genera, canonizza o risponde non apre
   mai `03_valutazione/`; chi valuta non è chi ha risposto; i blocchi di domande li
   prepara uno script.
7. **Tutto locale.** Retrieval e generazione dentro le mura; il cloud (Notion) è solo
   una fonte in entrata.

---

## Sessione 0 — Fondazioni (≈ 30 minuti) · Terminale: radice del repository

- [x] Manifest dei contenuti (`06_operativo/manifest_corpus_v1.json`, 15/08) — hash
      SHA-256 dei 160 file; conferma indipendente dei conteggi del README.
- [x] Decision log avviato (`06_operativo/decision_log.md`).
- [x] `.gitignore` pronto in radice.
- [x] **Estensione mtime + verifica hash in locale** (15/08) → `manifest_corpus_v1.1.json`:
      160/160 file riverificati contro gli SHA-256 del v1, zero divergenze, mtime
      aggiunti. Script: `06_operativo/estendi_manifest_mtime.py` (riporta tutti gli
      scarti e non scrive nulla se anche uno solo non torna). Eseguire in
      `06_operativo\`:

      ```python
      import hashlib, json, os
      SRC = r"C:\Users\buulo\Desktop\sources"
      base = json.load(open("manifest_corpus_v1.json", encoding="utf-8"))
      for e in base["file"]:
          p = os.path.join(SRC, e["nome"]); b = open(p, "rb").read()
          assert hashlib.sha256(b).hexdigest() == e["sha256"], "HASH DIVERSO: " + e["nome"]
          e["mtime_ms"] = int(os.stat(p).st_mtime * 1000)
      base["artefatto"] = "manifest_corpus_v1.1"
      json.dump(base, open("manifest_corpus_v1.1.json", "w", encoding="utf-8"),
                ensure_ascii=False, indent=1)
      print("OK: 160 file verificati, mtime aggiunti")
      ```
- [x] **git init** nella radice del repository + primo commit
      («riorganizzazione + congelamento corpus v1») + tag `corpus-v1-baseline`
      (15/08, `12c3023`, 193 file, branch `main`). Aggiunto `.gitattributes` con
      `* -text`: senza, `core.autocrlf=true` avrebbe riscritto i line ending dei
      grezzi al checkout, invalidando gli hash del manifest.
- [x] **Perimetro della misura «dopo»** — FISSATO il 15/08: addendum dedicato in
      `01_metodo/metodo_02_misurazione.md` (si misura l'intero vault esclusa
      `.obsidian\`, grezzi copiati compresi; indice B nuovo; stesse 282 domande).

---

## Sessione 1 — Il manuale di canonizzazione · Terminale: radice del repository

- [x] **FATTA il 16/08/2026 — manuale approvato al gate.** Nati
      `01_metodo/metodo_03_canonizzazione.md` (10 sezioni: spareggio con albero a 12
      passi e 27 esempi limite da file veri, metabolismo delle note, frontmatter con
      vocabolari chiusi, 6 template con esempi compilati, naming e link, «un fatto un
      padrone» con i valori derivati, entity resolution, suite QA, derivati, processo a
      lotti, 40 divieti) e l'allegato `01_metodo/alias_entita.md`. Revisione indipendente
      eseguita prima del gate: corretti due numeri falsi negli esempi, la definizione
      doppia di orfano, la QA di provenance insoddisfacibile e un bug nello snippet di
      verifica della copia. Divergenza di categoria B trovata e registrata nel canone
      (sezione datata 16/08). **Nessuna nota scritta: il vault non è stato toccato.**

Nasce `01_metodo/metodo_03_canonizzazione.md`, il terzo documento di metodo: regole di
spareggio fra le 11 cartelle del vault; frontmatter come verità macchina (type, area,
fonti, stato risolto/aperto, aliases, date); template dei 6 tipi di nota (atomica ≈
≤300 parole = chunk naturale per il RAG, hub, scheda entità, nota conflitto, nota
concetto, più la nota `_index` di cartella); naming e wikilink (spoke→hub,
«Detect all file extensions» ON); un **`_index` in OGNI cartella del vault** — la
porta della cartella, con frontmatter proprio (`type: index`, summary) e l'elenco
di hub e note della cartella: nessuna nota deve essere irraggiungibile lungo il
percorso llms.txt → `_index` → hub → nota; gli `_index` sono esentati dalla regola
degli orfani e non contano nel minimo di wikilink delle altre note;
«un fatto, un padrone» operativo (contraddizione con vincitore → nota padrona col
valore canonico e le fonti divergenti linkate; conflitto aperto → nota «questione
aperta»; le fonti non si correggono MAI); entity resolution con tabella alias;
la suite QA delle note (provenance: ogni fatto ha riscontro nella fonte citata —
si riusa la tecnica di verifica delle 282 risposte; link integrity: zero link
rotti e zero orfani, cioè ogni nota raggiungibile dall'`_index` della sua cartella,
direttamente o via hub; validazione frontmatter; copertura); artefatti derivati (llms.txt rigenerato dal frontmatter
— unico derivato che vive DENTRO il vault; showcase in `06_operativo/showcase/`, FUORI
dal vault, perché le 11 cartelle restano 11 e il perimetro della misura non si tocca;
skill journal — il minimo di wikilink è un avviso, non un errore bloccante);
decisione logistica: i grezzi si COPIANO in `aurora-cervello\sources`, l'originale
congelato resta fuori.

Il prompt della sessione si prepara in Cowork e si salva in
`06_operativo/prompt/prompt_s1_canonizzazione.txt`. Gate: tua approvazione del
documento prima di toccare una sola nota.

---

## Sessione 2 — Fetta pilota verticale · Terminale: radice del repository

- [x] **FATTA il 16-17/08/2026 — design validato al gate.** 22 grezzi del caso L26130 →
      **63 note** (46 di contenuto, 11 `_index`, 6 note-strumento), con 11 questioni aperte.
      Suite QA implementata e **collaudata** (5 difetti piantati su 5 trovati, 0 falsi
      positivi), QA di lotto **verde**, copertura 22/22. Strato di giudizio della provenance
      su tutte le 46 note candidate (42 pulite); revisione indipendente col canone: 13 A ·
      5 B · 10 C, tutte chiuse, le 5 B registrate nel canone in sezione datata. Mini-misura
      di fumo su 30 domande, **numeri non ufficiali**: 28/30 corrette contro 23/30 della
      baseline A sugli stessi id, fonti 30/30 contro 27/30, **zero peggioramenti**.
      **19 emendamenti a metodo_03** approvati e applicati; prompt di giudizio congelato in
      `qa_provenance.py`. Rapporto di gate: `06_operativo/rapporto_gate_s2.md`.

15-20 file del caso L26130 (NC, reclamo REC-2026-011, log pastorizzatore, mass
balance, MOD-QA, lettere al cliente, audit, ispezione) → 20-30 note nel vault, con
hub, almeno una nota conflitto e una questione aperta. Suite QA completa + revisore
indipendente col canone (una nota che «corregge» una trappola è un errore, categoria
A). Mini-misura di fumo, solo config A, sul sottoinsieme di domande con fonti nella
fetta (gli ID li estrae uno script di preparazione da `03_valutazione/eval_set.jsonl`
in una sessione separata; chi risponde riceve solo gli ID e `domande_solo.jsonl`).
I numeri del pilota NON sono ufficiali. Gate: il design regge? Si aggiorna
metodo_03 e SOLO POI si industrializza.

---

## Sessione 3 — Pipeline RAG di produzione + baseline C · Terminale: `05_rag_produzione\`

- [x] **FATTA il 17-18/08/2026 — gate approvato dal coordinatore.** Pipeline costruita e
      congelata (`config_c.json`, impronta `afb58939…`, commit `d36d7ce` **pushato prima
      di indicizzare**); corpus 160/160; 1.902 chunk di cui **1.897 `nativa`, esattamente
      i 1.897 della config B**; indice Qdrant 1.902 punti; collaudo 8/9 attesi consegnati
      e tutti gli 11 formati raggiungibili; run 282/282 in 9h 01m, verificato **INTEGRO**.
      Giudizio in sessione separata: **14,5% corrette sulle 282 · 7,6% sulle 251
      rispondibili** — i due numeri non si citano mai separati. Diagnosi: **il collo di
      bottiglia è il generatore, non il recupero** (70,2% di fonti giuste contro 14,5% di
      risposte giuste). Verbale chiuso in
      `04_misurazioni/baseline_c_2026-08-17_grezzo/verbale_baseline_c.md`, rapporto di
      gate in `06_operativo/rapporto_gate_s3.md`.

Guida: `01_metodo/metodo_04_rag_produzione.md`, passi S3.1-S3.7 — ambiente (Qdrant,
Ollama, modelli congelati con checksum), ingestione, indicizzazione del corpus v1
verificato contro il manifest, catena ibrida (BM25+denso → RRF → reranker → Llama a
temperatura 0), smoke test, **BASELINE C ufficiale sul grezzo** (protocollo di
metodo_02, addendum C — ultima finestra utile prima della canonizzazione), demo
Notion inbound con copie non sensibili. La tabella dei parametri C si data e si
congela; riga C della tabella risultati nel README.

*(Le Sessioni 2 e 3 sono indipendenti: si possono invertire. L'unico vincolo duro è
che la baseline C preceda la Sessione 4.)*

---

## Sessioni 4-5 — Canonizzazione integrale · Terminale: radice + vault

Input: mappatura a matrice dei 159 (quali cartelle alimenta ogni file, con quali
fatti) usata come piano di lavoro. Lotti per area tematica; ogni lotto: note → suite
QA → revisore indipendente → correzioni propagate → QA di nuovo. Pass finale: entity
resolution su tutto il vault, hub-and-spoke completo, `_index` di ogni cartella
aggiornato, zero note orfane, zero fatti del canone senza padrone, llms.txt (nel vault) e
showcase (in `06_operativo/showcase/`) rigenerati. Fine di ogni sessione: zip
di backup del vault + commit + push + stato.

---

## Sessione 6 — Pre-registrazione e misura «dopo» · Terminale: cartelle di misura

1. **PRIMA di misurare, e non è un consiglio: `06_operativo/predizioni.md` si scrive e
   si COMMITTA prima che la misura «dopo» parta.** Obbligo fissato al gate della
   Sessione 3 (18/08/2026): un delta raccontato a posteriori non è una previsione, è una
   giustificazione. Deve contenere, per iscritto e datato:

   | Voce | Attesa dichiarata |
   |---|---|
   | `contraddizione` | **in salita** — è il tipo che la canonizzazione tocca più direttamente: la nota-conflitto rende esplicita la divergenza che C non vede mai (0 su 14 nella baseline) |
   | `multi_hop` | **in salita** — i wikilink accorciano l'attraversamento |
   | `aggregazione` | **piatta** — dipende dal saper contare, che è il generatore, non l'archivio |
   | `calcolo` | **piatta** — stesso motivo |
   | ⚠️ un balzo su `aggregazione` o `calcolo` | **si indaga, non si festeggia**: se l'archivio organizzato migliorasse ciò che dipende dal generatore, la spiegazione più probabile è che sia cambiato qualcos'altro |
   | difetto **padrone/derivato** (§10.2 del verbale C) | **sparisce** — è la previsione più netta e falsificabile che la baseline C consegna: nel vault il documento-padrone e il derivato sono note distinte con `fonti` esplicite |
   | allucinazione | ferma o in calo |
   | fonti | più precise |

   Più le **due definizioni già fissate** in `metodo_02` (addendum del 18/08), da
   richiamare in `predizioni.md` perché nessuno le riapra a numeri visti:
   **`fonti_corrette` conta il grezzo, la nota è navigazione**; **tasso di allucinazione
   = `allucinata` + `sbagliata` su `non_rispondibile`**.
2. Misure A, B e C col protocollo congelato, perimetro = vault; cartelle
   `04_misurazioni/dopo_<data>_vault_<config>/`.
3. Valutazione in terza sessione; varianza: doppio giro su ~30 domande per il ±.
4. `metriche.md` v2 + righe «dopo» della tabella del README.

---

## Sessione 7 — Analisi, narrazione, pubblicazione · Terminale: radice

⚠️ **Regola vincolante per il README v2 e per ogni materiale commerciale: dove si cita
la correttezza della configurazione C vanno SEMPRE due numeri insieme — 14,5% sulle 282
e 7,6% sulle 251 rispondibili — mai uno separato dall'altro.** Le altre 22 corrette
vengono da domande la cui risposta giusta è «il dato non c'è», e il sistema ci arriva
perché si astiene sempre, non perché sappia distinguere. La riga della tabella dei
risultati **non ha una colonna di correttezza, e va bene così**: le quattro metriche di
P4 non la contengono, e il doppio numero vive nel testo accanto alla tabella, dove c'è
spazio per la spiegazione. Vale identico per le righe «dopo» della Sessione 6.

Confronto per tipo di domanda e per configurazione, delta contro le predizioni, casi
commentati. Demo pack per i clienti: 10 confronti prima/dopo leggibili da un titolare
(la rintracciabilità del lotto L26130 in secondi è il pezzo forte). README v2 con
numeri ricontati da script; licenza; tag `corpus-v1-canonizzato`. Poi, e solo poi:
corpus v2 (prompt già pronto), nuova baseline, nuovo manifest.

---

## Budget di tempo e stop-loss

| Sessione | Stima | Stop-loss |
|---|---|---|
| 0 Fondazioni | 30 min | — |
| 1 Manuale canonizzazione | 1 sessione | se esplode: meno template, mai meno QA |
| 2 Pilota verticale | 1 sessione + review | se il design non regge: si riprogetta, non si rattoppa |
| 3 Pipeline C + baseline C | 1-2 sessioni | prima CPU-only funzionante, poi GPU; parametri congelati alla baseline |
| 4-5 Canonizzazione | 2-3 sessioni | se esplode: lotto più piccolo, mai QA più leggera |
| 6 Misura «dopo» | 1-2 sessioni | parametri congelati, nessuna eccezione |
| 7 Pubblicazione | 1 sessione | niente numeri non ricontati |

Regola generale: quando una sessione supera il doppio della stima ci si ferma e si
riduce lo scope; tirare dritto produce il debito che le sessioni dopo pagano doppio.

---

## Cosa non fare mai

- Toccare i 159 grezzi (né in `Desktop\sources` né in `02_corpus/`): le anomalie
  registrate sono contenuto.
- Aprire `03_valutazione/` in una sessione che genera, canonizza o risponde.
- Ridiscutere un parametro congelato (config A, B o C) o migrare B su Qdrant.
- Espandere il corpus prima della fine del ciclo (l'espansione è corpus v2).
- Scrivere una nota con un fatto senza fonte, o dichiarare un numero non ricontato.
- «Correggere» una contraddizione del canone: è l'oggetto del test.
- Far uscire dati verso il cloud: Notion è solo una fonte in entrata.
