# metodo_02 — Misurazione

> **Cos'è** · Il protocollo di misura: configurazioni congelate, i prompt da copiare alla
> lettera, e il verbale della baseline del 14/08/2026 (già eseguita: tempi, esiti e
> analisi sono inclusi più sotto).
> **Quando si usa** · Per la baseline della configurazione C (prima della canonizzazione)
> e per le misure «dopo», a canonizzazione finita. I prompt si copiano alla lettera; si
> adattano SOLO i percorsi.
> **Cosa non toccare** · Parametri delle configurazioni, clausole di perimetro, i quattro
> esiti. Cambiarne uno rende i numeri non confrontabili.
> **Percorsi aggiornati (riorganizzazione del 15/08/2026)** · Dove i prompt storici dicono:
> `Desktop\misure_aurora\` leggi `04_misurazioni\<cartella della misura>\` (la baseline
> sta in `04_misurazioni\baseline_2026-08-14_grezzo\`) · `domande_solo.jsonl` ed
> `eval_set.jsonl` stanno in `03_valutazione\` · `Config_test_13-08-26` sta dentro la
> cartella della baseline · lo script sta in `04_misurazioni\rag_retrieval.py` (per una
> nuova misura adatta le costanti di percorso in testa allo script; il modello congelato è
> in `04_misurazioni\_locale_non_su_github\modelli\bge-m3`).

**Come misurare l'archivio, passo per passo, con i prompt da copiare.**

Si usa quando l'archivio grezzo è finito e prima di organizzarlo in markdown. Produce i
numeri che vanno nella tabella dei risultati del README.

Il documento gemello — `metodo_01_generazione_archivio.md` — spiega come si costruisce l'archivio.
Questo spiega come si misura. Non si sovrappongono.

---

## Regola d'ingaggio: il blocco te lo chiede lui

Ogni prompt qui dentro **chiede con `AskUserQuestion` prima di lavorare**. Tu non devi
tenere il conto di dove sei arrivato: il file di output ce l'ha già scritto dentro, e
l'agente lo legge.

**Cosa deve chiederti sempre:**

- **quale blocco elaborare** — contando le righe già presenti nel file di output e
  proponendoti il successivo come opzione consigliata («ne trovo 60, procedo con 61-90?»)
- **quale misura stai valutando** (A o B), nel passo 5
- **i percorsi**, la prima volta che li usa, se non sono già evidenti dalla cartella
- **cosa fare quando qualcosa non torna**: righe mancanti, `id` duplicati, un blocco che ha
  prodotto meno risposte delle domande ricevute

**Cosa non deve chiederti mai:** i parametri delle due configurazioni. `top_k`, dimensione
dei pezzi, modello di embedding, temperatura, numero di domande per blocco **sono congelati**.
Se te li chiede, la risposta è «quelli scritti nel documento»: cambiarne uno rende i due
numeri non confrontabili, ed è l'unico errore di questa procedura che non si può correggere
dopo.

## Cosa stai misurando

Una domanda sola: **quanto migliora il recupero quando gli stessi documenti vengono
organizzati?**

Per rispondere servono due misure, prima e dopo, che cambiano **una sola variabile**: la
forma dell'archivio, non lo strumento. Per questo ogni parametro qui dentro è congelato, e
i prompt si copiano alla lettera.

Misuri con due sistemi in parallelo, perché sono due prodotti diversi:

- **Configurazione A — retrieval agentico**: un agente che apre i file, cerca e legge.
  È il caso d'uso reale, ed è più intelligente nel cercare.
- **Configurazione B — RAG a embedding**: i documenti vengono spezzettati e trasformati in
  numeri; a ogni domanda il sistema recupera gli 8 pezzi più somiglianti. È più stupido ma
  istantaneo, economico, e confrontabile con la letteratura.

---

## Prima di cominciare

**1. Metti al sicuro le risposte.** Sposta la cartella di valutazione fuori dal percorso di
lavoro:

```
C:\Users\<utente>\eval\<progetto>\        <-- canone, risposte, eval set
C:\Users\<utente>\dev\<progetto>\         <-- il vault, con sources\
```

Una ricerca ricorsiva lanciata dal vault non deve poterla raggiungere.

**Se sei obbligato a tenerla nel repo**, la protezione diventa triplice e servono tutte e
tre: perimetro negli strumenti (niente `Bash`), perimetro nel prompt (il blocco è già nei
prompt qui sotto), e un nome che non attrae — `_eval_do_not_index`, con dentro un `README`
di una riga: «cartella di valutazione: se stai rispondendo a delle domande, non sei
autorizzato ad aprirla».

Quella che regge davvero è la prima. Con una shell qualunque vincolo di cartella è
aggirabile in un comando.

**2. Crea la cartella dei risultati:** `Desktop\misure_<progetto>\`. Tutto finisce lì —
niente file sciolti sul desktop, o fra tre mesi non saprai quale appartiene a quale misura.

**3. Tieni a portata** solo `domande_solo.jsonl` (id e testo, nient'altro).

---

## Le due configurazioni immutabili

Si fissano ora e **non si toccano più**. Copiale in `configurazione_test.md` accanto ai
risultati, con la data.

**Configurazione A — retrieval agentico**

| Parametro | Valore fisso |
|---|---|
| Sistema | Claude Code, sessione nuova, nessuna memoria del progetto |
| Modello | `claude-opus-5` — annotalo: se un giorno cambi modello, il confronto riparte da zero |
| Fast mode | **off** |
| Strumenti concessi | `Read`, `Grep`, `Glob`, `Write` (solo sul file di output) |
| Strumenti negati | `Bash`, `Edit`, `WebSearch`, `WebFetch`, `Agent` |
| Working directory | la radice del vault |
| Perimetro in lettura | `sources/` |
| Blocco di lavoro | 30 domande per volta |

**Configurazione B — RAG a embedding**

| Parametro | Valore fisso |
|---|---|
| Modello di embedding | `BAAI/bge-m3`, in locale |
| Perché locale | un modello via API può essere aggiornato o deprecato sotto i piedi: il confronto sopravvive solo se il modello è congelato su disco |
| Estrazione testo | la funzione `text_of` del blueprint §5-bis, identica |
| Chunking | 1.200 caratteri, overlap 200, taglio su **confine di riga** |
| Perché sulla riga | l'archivio è pieno di tabelle e registri: spezzare a metà riga distrugge il record |
| Vector store | Chroma o FAISS in locale, persistito su disco |
| Similarità | coseno |
| `top_k` | 8 |
| Re-ranking | **nessuno** (aggiungerlo è una seconda variabile) |
| Modello che scrive la risposta | lo stesso della configurazione A, temperatura 0 |
| Metadato per chunk | nome del file di origine, obbligatorio |

Il modello che scrive è lo stesso nelle due configurazioni **apposta**: così la differenza
fra A e B misura il recupero, non la scrittura.

---

## I file che produci, e quante volte lanci ogni prompt

| File | Da cosa nasce | Quante volte |
|---|---|---|
| `misuraA_risposte.jsonl` | P1 | **10 giri** da 30 domande, tutti in append sullo stesso file |
| `rag_retrieval.py` | P2.0 | **una volta sola** — produce UNO script, non uno per domanda |
| `misuraB_contesti.jsonl` | eseguendo lo script | **una volta sola** — lo script gira su tutte le domande da solo |
| `misuraB_risposte.jsonl` | P2.1 | **10 giri** da 30 domande, in append |
| `valutazione.jsonl` | P3 | **10 giri** da 30 voci, in append |
| `metriche.md` | P4 | **una volta sola**, alla fine |

## Dove si esegue ogni passo

Ogni passo è una **sessione di Claude Code aperta in una cartella precisa**, tranne il passo
3 che è un comando in PowerShell. La cartella in cui apri il terminale decide cosa il modello
può vedere, ed è il modo più semplice per far rispettare i perimetri.

| Passo | Apri il terminale in | Cosa può leggere | Cosa scrive |
|---|---|---|---|
| 1 · P1 | `vault\` | **solo** `sources\` | `misuraA_risposte.jsonl` |
| 2 · P2.0 | `vault\` | `sources\` e i due documenti di metodo | `rag_retrieval.py` |
| 3 · script | PowerShell, ovunque | `sources\` | `misuraB_contesti.jsonl` |
| 4 · P2.1 | `Desktop\misure_<progetto>\` | **solo** `misuraB_contesti.jsonl` | `misuraB_risposte.jsonl` |
| 5 · P3 | `Desktop\misure_<progetto>\` | i file di risposte e `eval_set.jsonl` | `valutazione.jsonl` |
| 6 · P4 | `Desktop\misure_<progetto>\` | `valutazione.jsonl` e `eval_set.jsonl` | `metriche.md` |

**Perché i passi 4, 5 e 6 stanno in `misure_<progetto>\` e non nel vault.** Dal passo 4 in
poi non si guardano più i documenti dell'azienda: si lavora solo su ciò che è già stato
recuperato o già risposto. Aprendo il terminale lì, il modello **non ha nemmeno il vault a
portata**, e il perimetro si fa rispettare da solo.

**Non devi incollare i passaggi a mano.** Nel passo 4 il modello legge le righe che gli
indichi direttamente da `misuraB_contesti.jsonl` — sono esattamente i passaggi che il RAG
gli avrebbe passato, quindi leggerli da lì non è barare. Barare sarebbe aprire `sources\`,
e da quella cartella non ci arriva.

**Dal passo 5 in poi le risposte attese servono.** Copia `eval_set.jsonl` dentro
`misure_<progetto>\`: la sessione del giudice ha diritto di vederle, è la sua funzione.

⚠️ **Tre errori di lettura da evitare, perché costano giornate:**

- P2.0 **non** si lancia una volta per domanda: produce un programma che le elabora tutte.
- Lo script **non** va eseguito una volta per domanda: gira una volta e scrive tutti i
  contesti.
- P2.1 **non** si lancia una volta per domanda: si lancia a blocchi, esattamente come P1.

In tutto sono circa **32 lanci di prompt**, non 850.

---

# La procedura, passo per passo

## Passo 1 — Misura A: le risposte dell'agente

Apri un terminale **nuovo** nella cartella del vault. Non deve avere memoria di come
l'archivio è stato costruito.

Incolli il prompt qui sotto con trenta domande alla volta, prese da `domande_solo.jsonl`.
Dieci giri e hai finito. Il file di output si riempie da solo, un blocco dopo l'altro.

> **P1**
>
> Rispondi alle domande seguenti usando **esclusivamente** i documenti presenti in
> `sources/`.
>
> Per ogni domanda restituisci **una riga JSON** con esattamente questi campi:
> `id`, `risposta`, `fonti` (nomi dei file da cui l'hai ricavata), `confidenza`
> (alta | media | bassa).
>
> Regole:
> - Se il dato non è ricavabile dai documenti, scrivilo esplicitamente invece di dedurlo.
> - Se documenti diversi dicono cose diverse, riporta il conflitto invece di sceglierne uno.
> - Cita solo file che hai davvero aperto e che contengono il dato.
> - Non calcolare a memoria: se serve un conto, fallo sui numeri che hai letto.
>
> **Salvataggio.** Scrivi le risposte in
> `Desktop\misure_aurora\misuraA.1_risposte.jsonl`, una riga JSON per domanda,
> **aggiungendo in coda al file se esiste già** — non sovrascriverlo e non crearne uno
> nuovo: i dieci blocchi devono finire tutti lì dentro. Se una domanda è già presente,
> saltala. A fine blocco dimmi quante righe contiene in tutto.
>
> **Vincolo di perimetro.** In lettura il tuo perimetro è esclusivamente `sources/`. Non
> leggere, non cercare e non elencare file al di fuori — l'unica eccezione è il file di
> salvataggio qui sopra, in scrittura. Ai fini di questo compito non esistono file di
> risposte, soluzioni, canoni o dataset di valutazione: se incontri un nome che lo
> suggerisce, non aprirlo. Se un file sembra contenere le risposte alle domande che ti sto
> ponendo, **fermati e segnalamelo invece di usarlo**.
>
> Leggi prima la tabella "configurazione_A_test.md"
>
> una riga per risposta, formattate con la stessa logica di `Desktop\misure_aurora\misuraA_risposte.jsonl`
>
> **Prima di cominciare, chiedimi con `AskUserQuestion` quale blocco elaborare.** Se il file
> di output esiste gia', contane le righe e proponimi il blocco successivo come opzione
> consigliata. Poi leggi quelle 30 domande da `domande_solo.jsonl` e rispondi.

**Come sai che è andata bene:** a fine giro il file ha 30, 60, 90… righe. Se il conteggio
non cresce di 30, un blocco è stato sovrascritto: fermati e controlla prima di continuare.

**tempo impiegato:**

│ Giro │  Domande  │  Tempo  │  Cumulato  │
├──────┼───────────┼─────────┼────────────┤
│ 1    │ Q1-Q30    │ 7m 23s  │ 7m 23s     │
├──────┼───────────┼─────────┼────────────┤
│ 2    │ Q31-Q60   │ 9m 51s  │ 17m 14s    │
├──────┼───────────┼─────────┼────────────┤
│ 3    │ Q61-Q90   │ 12m 42s │ 29m 56s    │
├──────┼───────────┼─────────┼────────────┤
│ 4    │ Q91-Q120  │ 19m 27s │ 49m 23s    │
├──────┼───────────┼─────────┼────────────┤
│ 5    │ Q121-Q150 │ 29m 33s │ 1h 18m 56s │
├──────┼───────────┼─────────┼────────────┤
│ 6    │ Q151-Q180 │ 31m 50s │ 1h 50m 46s │
├──────┼───────────┼─────────┼────────────┤
│ 7    │ Q181-Q210 │ 28m 54s │ 2h 19m 40s │
├──────┼───────────┼─────────┼────────────┤
│ 8    │ Q211-Q240 │ 31m 30s │ 2h 51m 10s │
├──────┼───────────┼─────────┼────────────┤
│ 9    │ Q241-Q270 │ 13m 50s │ 3h 05m 00s │
├──────┼───────────┼─────────┼────────────┤
│ 10   │ Q271-Q282 │ 20m 17s │ 3h 25m 17s │
└──────┴───────────┴─────────┴────────────┘

Medie: 20 m 32 s per blocco, 43,7 secondi per domanda.

Il dato che vale la pena guardare è la curva, non il totale. A parità di lavoro — 30 domande per blocco — il tempo cresce da 7m 23s a 31m 30s: 4,3 volte fra il primo e l'ottavo giro. La crescita è quasi monotona e non è spiegabile con la difficoltà delle domande, che non aumenta in modo sistematico: è il costo di riemettere l'intero file a ogni salvataggio, esattamente il collo di bottiglia che si era manifestato come fallimento di scrittura al giro 8.

La conferma sta nel giro 9: 13m 50s, meno della metà del precedente. È il primo scritto sul file nuovo, partito da 30 righe invece che da 210. Stesso numero di domande, stessa profondità di ricerca, metà tempo.

Il giro 10 risale a 20m 17s pur avendo solo 12 domande, ma per due ragioni diverse: l'inventario completo dell'archivio (Q276-Q282 hanno richiesto di enumerare tutti i 160 file e di verificare allegati, encoding e duplicati) e la riscrittura finale da 210 righe per le correzioni.

Se rifai la misura con Edit concesso, la stima ragionevole è che il tempo resti sui 10-13 minuti per blocco per tutti e dieci i giri: circa 2 ore invece di 3 e mezza, con la differenza interamente spiegata dal salvataggio e non dal retrieval.

---

## Passo 2 — Misura B: costruisci il recupero

Prima ti servono due componenti, una volta sola sul computer:

```
pip install sentence-transformers chromadb
```

`pip` è il magazzino ricambi di Python: scarica codice che altri hanno già scritto.
**`sentence-transformers`** trasforma il testo in numeri che ne rappresentano il
significato — dentro c'è il modello `bge-m3`. **`chromadb`** conserva quei numeri e sa
rispondere a una domanda sola: «quali pezzi somigliano di più a questo?».

Poi fai scrivere lo script. **Una volta sola**: quello che ottieni è un programma, non una
risposta.

> **P2.0**
>
> Leggi la tabella «configurazione B» in `Config_test_13-08-26` e scrivimi lo script di
> retrieval che descrive. Deve leggere i file di `sources/` con la funzione `text_of` del
> §5-bis di `metodo_01_generazione_archivio.md`, spezzarli come indicato, indicizzarli, e per ogni
> domanda di `domande_solo.jsonl` recuperare gli 8 pezzi più vicini con il nome del file di
> origine.
>
> Salva lo script in `Desktop\misure_aurora\rag_retrieval.py`.
>
> Lo script, eseguito **una volta**, deve scrivere
> `Desktop\misure_aurora\misuraB_contesti.jsonl`: una riga JSON per domanda, con `id`,
> `domanda` e `passaggi` (lista di 8 oggetti con `file` e `testo`). Deve poter riprendere se
> interrotto: se il file esiste già, salta le domande già presenti.
>
> Non rispondere alle domande e non aprire nessun file di risposte o di valutazione: il tuo
> compito è solo costruire il recupero.
>
> Stampami alla fine il comando esatto per eseguirlo e quanto dura la prima indicizzazione.

**Cosa fa lo script, per poterlo spiegare a voce:** legge i file e li taglia in pezzi
(un contratto di quaranta pagine non entra in una domanda); trasforma ogni pezzo in numeri
e li mette in Chroma — questa parte è lenta, qualche minuto, e si fa una volta sola;
poi, per ogni domanda, trasforma anche la domanda in numeri e chiede a Chroma gli otto
pezzi più vicini.

La prima volta scarica il modello, circa due giga. Dopo funziona anche senza internet.

**tempo impiegato:**

Numeri misurati su questa macchina (8 core, nessuna GPU):

├───────────────────────────────┼──────────────────────────────────────────────────────────────────┤
│ Scaricamento di bge-m3        │ ~10 min, una volta sola (2,2 GB congelati in modelli\bge-m3)     │
├───────────────────────────────┼──────────────────────────────────────────────────────────────────┤
│ Indicizzazione dei 1897 chunk │ ~78 min (2,1–2,9 s per chunk, i PDF e gli xlsx sono i più lenti) │
├───────────────────────────────┼──────────────────────────────────────────────────────────────────┤
│ Recupero delle 282 domande    │ ~70 s                                                            │
├───────────────────────────────┼──────────────────────────────────────────────────────────────────┤
│ Prima esecuzione, in tutto    │ ~90 min                                                          │
├───────────────────────────────┼──────────────────────────────────────────────────────────────────┤
│ Ogni esecuzione successiva    │ 3 secondi — non riapre niente                                    │
└───────────────────────────────┴──────────────────────────────────────────────────────────────────┘

I 4 .jpg sono invisibili alla configurazione B. La text_of del §5-bis non ha un ramo immagini, quindi MOD-QA-07_10-05-26_L1_T2_scansione.jpg, SKM_C224e26050408520.jpg e i due IMG-... non sono mai entrati nell'indice. Se in configurazione A quei documenti sono stati letti guardandoli, sulle domande che dipendono da loro il confronto non misura il recupero: misura una cecità di formato. Sono da isolare in sede di valutazione, o il delta A-B risulta gonfiato.

---

## Passo 3 — Esegui lo script

**Dove si esegue: in PowerShell, non «dentro Claude».** Claude lo *scrive*, tu lo *esegui* —
quello che P2.0 ti consegna è un programma, e i programmi Python si lanciano da un terminale.

Prima verifica di avere Python:

```
python --version

```
Poi il comando, una volta sola:

```
python "$env:USERPROFILE\Desktop\misure_aurora\rag_retrieval.py"

cd C:\Users\buulo\Desktop\misure_aurora
python rag_retrieval.py

```

Le virgolette servono se il percorso contiene spazi; `$env:USERPROFILE` è il modo di
PowerShell di dire «la mia cartella utente».

**Qui non c'è rischio di leak:** lo script legge solo `sources/` e scrive il file dei
contesti. Il perimetro conta nelle sessioni che *rispondono*, non in quella che costruisce
l'attrezzo.

Al termine hai `misuraB_contesti.jsonl`: una riga per domanda, ciascuna con gli otto
passaggi recuperati. È un file lungo, ed è normale — sono 282 domande × 8 pezzi.

**Controllo:** il file deve avere tante righe quante sono le domande. Se ne ha meno, lo
script si è interrotto: rilancialo, riprende da dove era rimasto.

**tempo impiegato:**

| tempo di elaborazione | vedi sopra - Claude ha eseguito l'indicizzazione in autonomia |

---

## Passo 4 — Misura B: le risposte dal recupero

**Dove:** apri una sessione nuova **in `Desktop\misure_<progetto>\`**, non nel vault. È il
punto che rende la misura B diversa dalla A: da quella cartella il modello **non raggiunge i
documenti dell'azienda**, e può rispondere solo con i passaggi che il retrieval ha estratto.
Il perimetro non è una promessa nel prompt, è una conseguenza di dove hai aperto il terminale.

Non devi incollare niente a mano: gli dici quali righe leggere e lui prende da lì domanda e
passaggi. Trenta righe alla volta, dieci giri.

> **P2.1**
>
> Rispondi alle domande seguenti usando esclusivamente i passaggi forniti per ciascuna.
>
> **Per ogni domanda** restituisci **una riga JSON** con: `id`, `risposta`, `fonti` (i file da cui
> provengono i passaggi che hai usato), `confidenza` (alta | media | bassa).
>
> Regole:
> - Se i passaggi non contengono il dato, rispondi che non è ricavabile. **Non integrare
>   con conoscenza tua**: puoi usare solo i passaggi di queste righe.
> - **Non aprire nessun altro file**, e in particolare nessun documento dell'archivio: il
>   solo file che puoi leggere è `misuraB_contesti.jsonl`.
> - Se i passaggi si contraddicono, riporta il conflitto invece di sceglierne uno.
> - Cita solo i file dei passaggi che hai effettivamente usato.
>
> **Salvataggio.** Scrivi in `Desktop\misure_aurora\misuraB_risposte.jsonl`, una riga
> per domanda, **in coda al file se esiste già**. Salta le domande già presenti. A fine
> blocco dimmi quante righe contiene in tutto.
>
> **Prima di cominciare, chiedimi con `AskUserQuestion` quale blocco elaborare.** Conta le
> righe gia' presenti in `misuraB_risposte.jsonl` e proponimi il blocco successivo come
> opzione consigliata. Poi leggi quelle 30 righe di `misuraB_contesti.jsonl` e rispondi
> usando i passaggi che ciascuna riga si porta dietro.

**tempo impiegato:**

| Giro | Domande | tempo di elaborazione |
|---|---|---|
| 1 | Q1-Q30 | 6m 18s |
| 2 | Q31-Q60 | 7m 4s |
| 3 | Q61-Q90 | 9m 0s |
| 4 | Q91-Q120 | 9m 10s |
| 5 | Q121-Q150 | 14m 27s |
| 6 | Q151-Q180 | 10m 5s |
| 7 | Q181-Q210 | 9m 54s |
| 8 | Q211-Q240 | 9m 32s |
| 9 | Q241-Q270 | 9m 57s |
| 10 | Q271-Q282 | 4m 35s |
|Totale|Q1-Q282| 1h 30m 2s |

**Due numeri che la tabella non mostra:**

Media per domanda: 19,2 s. Molto stabile — i blocchi da 30 stanno quasi tutti fra 9 e 10 minuti, cioè 18-20 s a domanda. L'ultimo blocco costa di più a domanda (22,9 s) perché il costo fisso è per blocco, non per domanda: AskUserQuestion, estrazione, append, validazione si pagano uguali su 12 o su 30.

La curva sale e poi si appiattisce. I primi due giri (6-7 min) sono più veloci perché stavo ancora rispondendo corto; dal terzo in poi si stabilizza sui 9-10. Il blocco 5 a 14m 27s è l'unico fuori scala.

---

## Passo 5 — Valutazione

**Dove:** sessione nuova **in `Desktop\misure_<progetto>\`**, con dentro anche una copia di
`eval_set.jsonl` — questa sessione ha diritto di vedere le risposte attese, è la sua funzione.

Una regola che non puoi violare: **chi valuta non è chi ha risposto**. Se lo chiedi nella
stessa conversazione in cui hai risposto, si giudica da solo e si dà ragione. Sessione nuova,
sempre.

Trenta voci alla volta, per ciascuna delle due misure (quindi il prompt gira venti volte in
tutto, dieci per A e dieci per B).

> **P3**
>
> Valuti risposte date da un sistema documentale. Non devi rispondere alle domande: devi
> giudicare le risposte ricevute.
>
> Per ogni voce ti do: `id`, domanda, risposta attesa, criterio di valutazione, fonti
> corrette, risposta ricevuta, fonti citate.
>
> Assegna esattamente un esito:
> - `corretta` — soddisfa il criterio
> - `parziale` — dato giusto ma incompleto, o manca la contraddizione che andava segnalata
> - `sbagliata` — dato errato, ma ricavato da un documento reale
> - `allucinata` — dato inventato, **oppure** fonte citata che non contiene quel dato
>
> Restituisci una riga JSON per voce con: `id`, `misura` (A o B), `esito`,
> `fonti_corrette` (true/false), `motivazione` (una riga).
>
> Non essere generoso: se la risposta non contiene ciò che il criterio richiede, non è
> corretta anche se è ben scritta.
>
> **Salvataggio.** Scrivi in `Desktop\misure_aurora\valutazione.jsonl`, **in coda al
> file se esiste già**. A fine blocco dimmi quante righe contiene e quante per ciascun
> esito.
>
> **Prima di cominciare, chiedimi con `AskUserQuestion` due cose:** quale misura sto
> valutando (A o B) e quale blocco elaborare — contando le righe gia' presenti in
> `valutazione.jsonl` per quella misura e proponendomi il successivo come consigliato.
>
> Poi prendi quelle 30 voci: domanda, risposta attesa, criterio e fonti stanno in
> `eval_set.jsonl`; risposta ricevuta e fonti citate stanno nel file di risposte della
> misura indicata, accoppiate per `id`.

**Totale misura B (282 voci):**

┌────────────┬─────┬───────┐
│   Esito    │  N  │   %   │
├────────────┼─────┼───────┤
│ corretta   │ 126 │ 44,7% │
├────────────┼─────┼───────┤
│ parziale   │ 77  │ 27,3% │
├────────────┼─────┼───────┤
│ sbagliata  │ 79  │ 28,0% │
├────────────┼─────┼───────┤
│ allucinata │ 0   │ 0%    │
└────────────┴─────┴───────┘

Fonti corrette: 227 su 282 (80,5%).

Ripartizione per tipo — è qui che si legge il sistema:

┌──────────────────┬──────┬──────┬──────┬─────┐
│       Tipo       │ corr │ parz │ sbag │ tot │
├──────────────────┼──────┼──────┼──────┼─────┤
│ non_rispondibile │ 25   │ 6    │ 0    │ 31  │
├──────────────────┼──────┼──────┼──────┼─────┤
│ lookup           │ 53   │ 15   │ 18   │ 86  │
├──────────────────┼──────┼──────┼──────┼─────┤
│ contraddizione   │ 8    │ 3    │ 3    │ 14  │
├──────────────────┼──────┼──────┼──────┼─────┤
│ calcolo          │ 9    │ 9    │ 6    │ 24  │
├──────────────────┼──────┼──────┼──────┼─────┤
│ multi_hop        │ 23   │ 28   │ 23   │ 74  │
├──────────────────┼──────┼──────┼──────┼─────┤
│ temporale        │ 5    │ 9    │ 4    │ 18  │
├──────────────────┼──────┼──────┼──────┼─────┤
│ aggregazione     │ 3    │ 4    │ 21   │ 28  │
├──────────────────┼──────┼──────┼──────┼─────┤
│ metadato         │ 0    │ 3    │ 4    │ 7   │
└──────────────────┴──────┴──────┴──────┴─────┘

**Totale misura A (282 voci):** 199 corrette (70,6%) · 50 parziali (17,7%) · 33 sbagliate (11,7%) · 0 allucinate. Fonti corrette in 259 casi su 282.

Confronto finale fra le due misure:

┌────────────────┬─────────────┬─────────────┐
│     Esito      │      A      │      B      │
├────────────────┼─────────────┼─────────────┤
│ corretta       │ 199 (70,6%) │ 126 (44,7%) │
├────────────────┼─────────────┼─────────────┤
│ parziale       │ 50 (17,7%)  │ 77 (27,3%)  │
├────────────────┼─────────────┼─────────────┤
│ sbagliata      │ 33 (11,7%)  │ 79 (28,0%)  │
├────────────────┼─────────────┼─────────────┤
│ allucinata     │ 0           │ 0           │
├────────────────┼─────────────┼─────────────┤
│ fonti corrette │ 259/282     │ 227/282     │
└────────────────┴─────────────┴─────────────┘

Ripartizione per tipo (corrette / parziali / sbagliate):

┌──────────────────┬──────────────┬──────────────┐
│       Tipo       │      A       │      B       │
├──────────────────┼──────────────┼──────────────┤
│ lookup           │ 71 / 9 / 6   │ 53 / 15 / 18 │
├──────────────────┼──────────────┼──────────────┤
│ multi_hop        │ 39 / 21 / 14 │ 23 / 28 / 23 │
├──────────────────┼──────────────┼──────────────┤
│ non_rispondibile │ 26 / 4 / 1   │ 25 / 6 / 0   │
├──────────────────┼──────────────┼──────────────┤
│ aggregazione     │ 19 / 4 / 5   │ 3 / 4 / 21   │
├──────────────────┼──────────────┼──────────────┤
│ calcolo          │ 19 / 3 / 2   │ 9 / 9 / 6    │
├──────────────────┼──────────────┼──────────────┤
│ temporale        │ 15 / 3 / 0   │ 5 / 9 / 4    │
├──────────────────┼──────────────┼──────────────┤
│ contraddizione   │ 7 / 4 / 3    │ 8 / 3 / 3    │
├──────────────────┼──────────────┼──────────────┤
│ metadato         │ 3 / 2 / 2    │ 0 / 3 / 4    │
└──────────────────┴──────────────┴──────────────┘

Il divario è concentrato dove serve leggere un documento intero: sulle aggregazioni A fa 19 corrette contro 3, sulle temporali 15 contro 5, sui calcoli 19 contro 9. B falliva perché il retrieval consegnava chunk e un conteggio su file troncato non si chiude; A conta, somma e verifica esplicitamente. L'unico tipo dove B è alla pari o meglio è contraddizione (8 contro 7) — lì bastano due passaggi da due documenti, ed è esattamente ciò che un top-k sa fare.

I due limiti sono diversi in natura. B è limitata dal recupero: il chunk giusto non arriva. A è limitata dal parsing: .docx e .xlsx non si aprono, e questo compromette in tutto o in parte una trentina di voci, sempre le stesse fonti — mass balance, foglio marginalità, prospetto straordinari, libro unico, verbale CdA, previsionali di cassa, IO-05, matrice allergeni, cruscotto KPI. È un limite più facile da chiudere: è una questione di libreria, non di architettura.

Il blocco 10 lo mostra bene in entrambe le direzioni. Q272 è la risposta migliore dell'intera valutazione: alla trappola centrale dell'archivio — "il laboratorio ha confermato che il frammento viene dalla guarnizione?" — A risponde "ha confermato la compatibilità, che non è la stessa cosa della provenienza". Q278 trova dodici nomi-istruzione invece dei quattro attesi e chiude con una nota di metodo che nessun criterio chiedeva: "il nome di un file è un'affermazione non verificata, e in questo archivio almeno due si sono rivelate false". Q277 conta correttamente i 160 file per formato. Ma Q280 sceglie l'AUA del 2019 invece del manuale PKM-450 del 2018, e Q281 trova una sola coppia di duplicati su quattro.

Zero allucinazioni su 564 valutazioni complessive, in entrambe le configurazioni.
---

## Passo 6 — Le quattro metriche

Una volta sola, alla fine.

> **P4**
>
> Leggi `Desktop\misure_aurora\valutazione.jsonl` e `eval_set.jsonl` (che contiene il
> campo `tipo` di ogni domanda) e calcolami le metriche, separatamente per la misura A e
> per la misura B.
>
> 1. **Tasso di allucinazione** — percentuale di esiti `allucinata` sulle sole domande di
>    tipo `non_rispondibile`.
> 2. **Riconoscimento dei conflitti** — percentuale di `corretta` sulle sole domande di
>    tipo `contraddizione`.
> 3. **Accuratezza per tipo** — percentuale di `corretta` (e separatamente di
>    `corretta + parziale`) per ciascun tipo, con in evidenza il divario fra `lookup` e
>    `multi_hop`.
> 4. **Precisione delle fonti** — percentuale di voci con `fonti_corrette: true`.
>
> Aggiungi il totale complessivo e il conteggio grezzo dei quattro esiti.
>
> Poi estraimi **cinque casi di fallimento commentati**: due allucinazioni, due conflitti
> non riconosciuti, un attraversamento fallito — con domanda, risposta data e perché è
> sbagliata.
>
> **Salvataggio.** Scrivi tutto in `Desktop\misure_aurora\metriche.md`, e in fondo
> mettimi la riga già formattata in markdown da incollare nella tabella dei risultati del
> README, nel formato:
> `| <misura> | <data> | <allucinazione>% | <conflitti>% | <lookup>% | <multi_hop>% | <fonti>% |`

1. Il campo esito non contiene allucinata. I soli valori nelle 564 righe sono corretta/parziale/sbagliata. Ho definito allucinazione come sbagliata su non_rispondibile e l'ho dichiarato nel file. Ho verificato tutte le 10 parziale su non-rispondibili: arrivano tutte alla conclusione giusta, nessuna inventa un dato. Risultato: A 3,2% (1/31), B 0,0% — e l'unico caso di A non è un'invenzione ma una negazione di un fatto documentato. Con n=31, tra 1 e 0 casi non c'è divario: su questo asse le misure sono pari.

2. Il confronto A vs B è viziato, e va detto. A fallisce quasi ovunque per .xlsx/.docx binari — compare in ~24 delle sue valutazioni negative. B fallisce per «recupero fallito». Il 70,6% di A è l'accuratezza sul sottoinsieme testuale, non sul corpus. Se serve a scegliere un'architettura, va rifatto con un estrattore per binari, altrimenti stai misurando un parser mancante.

3. Il risultato più solido è il divario multi-hop: −29,9 pt in A, −30,5 pt in B. Identico. Non dipende dal recupero. E si dimezza sulla metrica permissiva (−11,9 / −10,2): il sistema si ferma a un hop dalla risposta, non sbaglia strada.

┌───────────────────┬─────────────┬─────────────┐
│                   │      A      │      B      │
├───────────────────┼─────────────┼─────────────┤
│ Totale corretta   │ 70,6% (199) │ 44,7% (126) │
├───────────────────┼─────────────┼─────────────┤
│ corretta+parziale │ 88,3%       │ 72,0%       │
├───────────────────┼─────────────┼─────────────┤
│ sbagliata         │ 33          │ 79          │
├───────────────────┼─────────────┼─────────────┤
│ Fonti corrette    │ 91,8%       │ 80,5%       │
└───────────────────┴─────────────┴─────────────┘

B collassa dove serve vedere tutte le righe insieme: aggregazione 10,7%, metadato 0,0%, temporale 27,8%. Ma cita bene nell'80,5% e risponde bene nel 44,7% — 36 punti di scarto: trova il documento e sbaglia lo stesso.

I cinque casi commentati sono nel file. Il più istruttivo è A/Q217 (sesamo): percorre tre hop correttamente, nota da sé che le referenze condividono la Linea 1, poi manca l'ultima fonte perché binaria e conclude "no" con confidenza alta su una domanda allergeni. Stesso pattern di Q259: quando A non riesce a leggere un file, non si astiene — nega. È il rischio più serio emerso, e riguarda il comportamento più del parser.

Riga README in fondo al file, entrambe le misure:
| A | 14/08/2026 | 3.2% | 50.0% | 82.6% | 52.7% | 91.8% |
| B | 14/08/2026 | 0.0% | 57.1% | 61.6% | 31.1% | 80.5% |

---

## Passo 7 — Porta i numeri nel README

Apri il README e incolla le due righe nella tabella dei risultati. Due righe su quattro
compilate: le altre due si riempiranno dopo l'organizzazione in markdown.

Da questo momento **non toccare più configurazioni e prompt.** Quando rimisurerai, l'unica
cosa cambiata dovrà essere la forma dell'archivio.

---

## Quanto tempo ci vuole

| Passo | Tempo |
|---|---|
| 1 — misura A | 10 giri, circa un'ora e mezza |
| 2 — installazione e script | mezz'ora, più il download del modello |
| 3 — esecuzione dello script | qualche minuto di indicizzazione, poi veloce |
| 4 — misura B | 10 giri, circa un'ora |
| 5 — valutazione | 20 giri, circa un'ora e mezza |
| 6 — metriche | dieci minuti |

Mezza giornata in tutto, distribuibile su più sedute: ogni file si riempie in append,
quindi puoi fermarti a metà e riprendere.

---

## Cosa non fare, mai

- **Far vedere le risposte attese al sistema che risponde.** Se succede, quel test è
  bruciato e non è recuperabile: si può solo rifare il dataset.
- **Valutare nella stessa sessione in cui hai risposto.**
- **Cambiare un parametro fra la misura di adesso e quella dopo l'organizzazione.** Se
  cambi anche lo strumento, i due numeri non si parlano più e la fatica è persa.
- **Riscrivere i prompt a memoria.** Copiali da qui, sempre.

---

## Addendum — Configurazione C: RAG di produzione (aggiunto il 15/08/2026)

Alla coppia A/B si aggiunge una terza configurazione, misurata con questo stesso
protocollo e con gli stessi 282 quesiti:

- **Configurazione C — RAG Advanced ibrido di produzione**: BM25 + embedding densi
  (`bge-m3`), fusione RRF, re-ranking con cross-encoder, generazione con LLM locale a
  temperatura 0, su Qdrant self-hosted. La tabella congelata dei parametri sta in
  `metodo_04_rag_produzione.md` e si fissa il giorno della baseline C.
- **La baseline C si misura sul corpus grezzo PRIMA della canonizzazione**: è l'ultima
  finestra utile, come per A e B. Poi si rimisura sul vault.
- Procedura: la costruzione della pipeline segue `metodo_04_rag_produzione.md`; le
  risposte si producono a blocchi da 30 in append (`misuraC_risposte.jsonl` nella
  cartella della misura), la valutazione usa P3 con `misura = C`, le metriche P4 estese
  alla terza colonna.
- **Chroma resta il metro (config B), Qdrant è il motore (config C).** Non migrare B su
  Qdrant: cambierebbe lo strumento a metà esperimento.
- Il modello che scrive la risposta in C è l'LLM locale della pipeline (non quello di
  A/B): C misura il SISTEMA che il cliente compra, ed è dichiarato come tale nel README.

---

## Addendum — Perimetro della misura «dopo» (fissato il 15/08/2026)

Scritto PRIMA che il vault esista, perché il perimetro non si improvvisa al momento.

- **Oggetto della misura**: il vault Obsidian canonizzato (`Desktop\aurora-cervello`),
  che conterrà le 11 cartelle di note PIÙ la copia dei 160 grezzi in
  `aurora-cervello\sources\`. Si misura l'archivio organizzato nel suo complesso:
  note, indici derivati (llms.txt) e grezzi copiati ne fanno parte; `.obsidian\`
  (configurazione dello strumento, non contenuto) è esclusa.
- **Config A «dopo»**: terminale aperto nella radice del vault; dove P1 dice
  «esclusivamente `sources/`», si legge «esclusivamente il vault `aurora-cervello`,
  esclusa `.obsidian\`». Strumenti concessi/negati, blocchi da 30 e regole invariati;
  il modello si dichiara (se diverso da quello della baseline, lo si annota: il
  confronto ne risente e va detto).
- **Config B «dopo»**: stesso `rag_retrieval.py` con la sola costante SOURCES puntata
  alla radice del vault (la `text_of` congelata legge già i `.md`); chunking e
  parametri invariati; indice NUOVO in una cartella nuova — quello della baseline non
  si riusa e non si aggiorna.
- **Config C «dopo»**: pipeline di `metodo_04_rag_produzione.md` con corpus = vault
  (le note sono chunk naturali, i grezzi seguono il chunking standard).
- **Risultati**: `04_misurazioni\dopo_<data>_vault\`, un file di risposte per
  configurazione, in append, come per la baseline.
- **Domande**: le stesse 282, da `03_valutazione\domande_solo.jsonl`. Le domande di
  tipo `metadato` si riferiscono all'archivio grezzo: nel vault i grezzi vivono in
  `sources\` e restano 160.
- `03_valutazione\` resta fisicamente fuori dal vault: il perimetro si fa rispettare
  da solo, come nella baseline.

---

## Addendum — Due definizioni fissate PRIMA della misura «dopo» (18/08/2026)

Approvate al gate della Sessione 3. Si fissano **ora**, prima che la Sessione 6 esista,
perché una definizione di metrica scelta dopo aver visto i numeri non è una definizione:
è una scelta di risultato.

### 1. `fonti_corrette` quando la risposta cita una NOTA del vault

**La fonte che conta è il GREZZO. La nota è navigazione, non provenienza.**

Nella misura «dopo» il perimetro è l'intero vault, che contiene sia le note sia la copia
dei 160 grezzi in `sources\`. Una risposta può quindi citare `docs\doc-ccp2-limite-
critico.md` invece del manuale HACCP da cui quel fatto viene. Il caso si è già presentato
una volta nella mini-misura di fumo della Sessione 2 (Q019).

Regola:

- `fonti_corrette: true` richiede che sia citato **almeno un file grezzo** fra quelli
  attesi dall'`eval_set`;
- una nota citata **da sola** non soddisfa il requisito, per quanto la nota sia corretta e
  ben scritta;
- una nota citata **in aggiunta** al grezzo non degrada il campo: è rumore utile.

**Perché.** Nella baseline esistevano solo grezzi. Se nella misura «dopo» la nota contasse
come fonte, i due numeri misurerebbero cose diverse e il confronto prima/dopo — che è
l'intero scopo del progetto — non si potrebbe fare. La nota è il percorso per arrivare al
documento; il documento resta ciò che un auditor apre.

### 2. Tasso di allucinazione

**Definizione ufficiale: `allucinata` + `sbagliata` sulle sole domande di tipo
`non_rispondibile`.**

P4 lo definiva come sola percentuale di `allucinata`. Nella valutazione A/B del 14/08 il
campo `allucinata` **non fu mai usato** — zero righe su 564 — e il giudice di allora
ripiegò su `sbagliata`, dichiarandolo. Nella baseline C del 17/08 il campo è stato usato
davvero. Con due definizioni diverse la colonna non si parla.

La somma dei due esiti concilia i casi:

| | A (14/08) | B (14/08) | C (17/08) |
|---|---:|---:|---:|
| `allucinata` su `non_rispondibile` | 0/31 | 0/31 | 2/31 |
| `sbagliata` su `non_rispondibile` | 1/31 | 0/31 | 4/31 |
| **somma — definizione ufficiale** | **1/31 = 3,2%** | **0/31 = 0,0%** | **6/31 = 19,4%** |

⚠️ **Dove il campo `allucinata` è vuoto, la somma coincide esattamente col ripiego del
14/08: le righe A e B della tabella dei risultati non cambiano di una cifra.** È il motivo
per cui questa definizione è stata scelta e non un'altra.

**Cosa misura, detto a parole:** su una domanda la cui risposta giusta è «il dato non è in
archivio», quante volte il sistema ha invece affermato qualcosa. Non distingue l'invenzione
dalla deduzione sbagliata, e va bene così: davanti a un auditor sono lo stesso danno.
