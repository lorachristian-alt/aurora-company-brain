# Stato della canonizzazione — vault `aurora-cervello`

> **Cos'è** · Lo stato di oggi del vault: cosa è stato canonizzato, con quale esito, e
> cosa resta. Solo stato, mai una regola: le regole stanno in
> `01_metodo\metodo_03_canonizzazione.md`, le decisioni in `06_operativo\decision_log.md`.
> **Aggiornato al** · 17/08/2026, chiusura della Sessione 2 (fetta pilota) dopo il gate.
> Riga «prossima sessione» allineata il 18/08 alla chiusura della Sessione 3; lo stato
> della pipeline RAG sta in `06_operativo\stato_rag_produzione.md`, non qui.

---

## Dove siamo

| | |
|---|---|
| Lotti chiusi | **1** — `l26130`, la fetta pilota |
| Grezzi copiati nel vault | 160/160, verificati contro `manifest_corpus_v1.1.json`: zero scarti, zero estranei, zero sottocartelle |
| Grezzi canonizzati | **22** dei 160 |
| Note prodotte | **63** (di cui 11 `_index` e 6 note-strumento) |
| Suite QA | implementata, collaudata e **verde** sul perimetro di lotto |
| `llms.txt` | rigenerato dal frontmatter, allineato |
| **Prossima sessione** | **S4 — canonizzazione integrale** (S3 chiusa il 18/08: baseline C misurata, gate approvato) |

## Densità del pilota — il dato per dimensionare i lotti di S4

**41 note di contenuto su 22 grezzi** al momento del gate, **46 su 22** a chiusura: poco più
di due note di contenuto per documento. È la prima misura disponibile del rapporto fra
documenti e fatti, e serve a dimensionare i lotti delle Sessioni 4-5: **un lotto da 30 grezzi
va preventivato attorno alle 60-70 note di contenuto**, più gli `_index` delle cartelle che
tocca.

⚠️ Il rapporto non è costante e non va usato come formula: dipende da quanti fatti porta ogni
documento. La fetta pilota era **densa per costruzione** — è il caso centrale dell'archivio —
e un lotto di rumore di fondo produrrà molte meno note per documento.

## In cima al prossimo lotto della Linea 1: il quaderno del capoturno

`appunti_capoturno_quaderno_linea1_OCR.txt` è la gamba mancante di **tre** conflitti trovati
dalla misura di fumo e non registrabili in questa fetta perché il file non c'era. Quando
entrerà, obbligherà a riaprire `fatto-verifiche-ccp3-turno-l26130`,
`questione-pezzi-prodotti-l26130` e `fatto-fermo-pkm-450-l26130`. **Va messo in cima al lotto
che tocca la Linea 1**, non incontrato per caso a metà Sessione 5.

## Il lotto `l26130` — la fetta pilota

**Perimetro:** 22 grezzi, elencati in `06_operativo\qa\fetta_l26130.txt`. Il nucleo del
caso del 10/05/2026 (log del pastorizzatore, foglio OEE, mass balance, MOD-QA-07 e
MOD-QA-31, reclamo, richiesta 48 ore, lettera in bozza, le due foto, rapporto di fermo
macchina, mail sul ricambio, inventario FEFO, registro NC, trascrizione della riunione,
verbale ATS, estratto HACCP), più la convocazione della riunione e **due coppie di
duplicati** — rapporto di prova del laboratorio e certificato di analisi della farina —
volute in fetta per collaudare la regola «un duplicato, una nota, due nomi in `fonti`»
prima che arrivi in produzione nelle Sessioni 4-5.

**Note prodotte, per cartella** *(contate da `qa_all.py`, non a memoria)*

| Cartella | Note |
|---|---|
| `areas\` | 24 |
| `entities\` | 9 |
| `projects\` | 8 |
| `code\` | 7 |
| `data\` | 5 |
| `docs\` | 3 |
| `concepts\` | 2 |
| `workspace\` | 2 |
| `self\` | 1 |
| `outputs\` | 1 |
| `sources\` | 1 |
| **totale** | **63** |

**Per `type`:** 25 atomica · 11 index · 11 conflitto · 8 hub · 7 entita · 1 concetto.

Escluse `workspace\` e `sources\` dai conteggi di qualità: **60** note.

`self\` e `outputs\` contengono per ora il solo `_index`: il lotto pilota riguarda un lotto
di produzione e la sua gestione, non l'identità di Aurora, e la risposta al cliente non è
mai uscita dallo stato di bozza.

## Esito della suite QA

Perimetro di lotto, ultimo passaggio dopo le correzioni del gate: **0 ERRORI, 33 AVVISI**.
Copertura **22/22** grezzi, nessun documento muto.

⚠️ Il pass **`--perimetro vault` è rosso**, ed è corretto che lo sia: 138 grezzi non sono
ancora citati da nessuna nota, e il grafo ha più componenti perché le note-strumento di
`code\` non sono agganciate al resto. Il vault verde è il traguardo delle Sessioni 4-5, non
di un lotto. **Da decidere in Sessione 4:** se agganciare le note-strumento al grafo in modo
non artificioso, o se escludere `code\` dal controllo di componente unica come già avviene
per `workspace\` e `sources\`.

**Gli avvisi, motivati per iscritto come richiede §9.5 passo 2.** Sono di tre famiglie, e
nessuna richiede una correzione:

- **21 avvisi di riscontro visivo** — le note costruite sulle tre immagini della fetta (la scansione del modulo del metal detector, la foto del pannello della confezionatrice, la foto del frammento col righello) portano `verifica: visiva`, e l'estrattore di testo congelato sulle immagini restituisce stringa vuota per costruzione. **Ogni immagine è stata letta a occhio** e i valori riportati corrispondono a ciò che si vede. È esattamente il caso previsto da §7.1 clausola 3.
- **5 avvisi «summary e title si sovrappongono per meno del 20%»** — su note il cui titolo è una domanda («Di che materiale è la guarnizione…») e il cui riassunto è la risposta: le parole non si ripetono perché il riassunto non parafrasa il titolo, che è ciò che si vuole.
- **1 avviso di lunghezza** su un riassunto al limite dei 250 caratteri.

**La storia dei passaggi.** Il primo giro aveva prodotto **31 errori**: 22 erano falsi
positivi di controlli troppo ingenui — corretti negli script — e 9 errori veri nelle note.
Dopo il giro del revisore ne sono rientrati altri 4, tutti miei: citazioni ricomposte
invece che riportate alla lettera, e un locator fuori grammatica.

## Collaudo della suite

Prima di usarla, la suite è stata collaudata su due note sintetiche in
`06_operativo\qa\_collaudo\` — una corretta, costruita su valori riscontrati nei grezzi
veri, e una con cinque difetti piantati apposta (fonte inventata, numero senza riscontro,
wikilink rotto, area fuori vocabolario, stato sbagliato). Esito: **5 difetti su 5 trovati,
0 falsi positivi sulla nota corretta**. Il collaudo è rieseguibile con
`python collaudo_suite.py` e ha già fatto il suo mestiere: al primo giro ha scoperto un
ramo invertito nel riconoscimento dei wikilink rotti.

## Strato di giudizio della provenance

Eseguito da un subagente a contesto pulito, che non ha ricevuto il canone e ha confrontato
ogni nota contro i propri grezzi. Esito: **26 note pulite su 33**, 6 «afferma oltre le
fonti» e 1 «fonte inutile». Tutti e sette i rilievi sono stati verificati e corretti.

## Revisione indipendente

Eseguita da un secondo subagente a contesto nuovo, **con il canone e la tabella alias alla
mano**, come prescrive §9.5 passo 3. Esito: **13 rilievi A, 5 B, 10 C**.

- Le **A** sono state tutte chiuse. Le più importanti: mancava la nota padrona della revisione del manuale HACCP (contraddizione registrata dal canone e da nessuna nota dichiarata); la data di apertura del reclamo era stata risolta scegliendo un vincitore che il canone non dà; la misura del frammento ribaltava l'arbitrato del canone; due conteggi erano sbagliati (righe del MOD-QA-07 e data di una non conformità); mancavano le schede delle persone nominate negli hub.
- Le **B** sono cinque divergenze reali che il canone non elencava: TMC e modo di consegna del lotto di farina, materiale della guarnizione, codice del kit valvola, ora di arrivo della segnalazione. Tutte hanno ora la loro nota-questione nel vault e **la loro riga nel canone**, in una sezione datata 16/08/2026 accanto a quella della Sessione 1. La sesta riga registra la terza misura del frammento.
- Le **C** sono dieci trappole riconosciute e non segnalate come errori: sono elencate nel decision log perché non tornino al lotto successivo.

**Il rilievo A che era rimasto aperto — le note di `code\` senza `fonti` — è stato chiuso al
gate** con l'emendamento E1: l'esenzione vale per la **nota-strumento** (prefisso `script-`
dentro `code\`), non per la cartella, e nel corpo di ciascuna è stato aggiunto il percorso
del sorgente nel repository. Nessun rilievo A resta aperto.

## Il giudizio di provenance, rieseguito su tutto

Alla chiusura lo strato di giudizio è stato **rieseguito su tutte le 46 note candidate** —
comprese le 8 che nel primo giro non erano mai state giudicate, perché nate dalle correzioni
del revisore. Esito: **42 pulite, 4 «afferma oltre le fonti», 0 fonti inutili**, tutti e
quattro i rilievi corretti.

⚠️ Il più importante dei quattro: una nota affermava una divergenza sui pezzi per cartone che
**nessuna sua fonte conteneva** — l'informazione veniva dal report del revisore, che aveva il
canone. **Era una fuga di canone dentro il vault**, la cosa che il guardrail 1 esiste per
impedire, ed è stata rimossa. È anche la ragione per cui la regola E9 — rigiudicare le note
nate dalle correzioni — vale la pena: quella nota era stata scritta *dopo* il primo giro di
giudizio, e senza il secondo giro sarebbe rimasta.

## Cosa resta

- **138 grezzi** non ancora canonizzati, che sono l'oggetto delle Sessioni 4-5.
- Le **quattro aree** del vocabolario chiuso ancora senza hub: amministrazione, risorse
  umane, sicurezza-ambiente, ricerca-sviluppo. Nasceranno con i lotti che le toccheranno.
- La **nota di inventario dell'archivio** in `data\`, che dovrà tenere i conteggi per
  formato, i duplicati e i file privi di contenuto informativo: è la nota che soddisfa la
  copertura sui file muti, e senza di essa `_index-sources` non può dichiarare un numero.
- Due dati della **scheda prodotto** — pezzi per cartone e ITF-14 — che nella fetta non
  sono attestati da fonti leggibili con l'estrattore congelato: si scriveranno quando
  entrerà il documento che li porta.
- La **matrice dei 159** (`06_operativo\matrice_corpus_v1.csv`), che si produce all'inizio
  della Sessione 4.
