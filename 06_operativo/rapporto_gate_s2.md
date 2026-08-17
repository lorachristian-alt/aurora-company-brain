# Rapporto di gate — Sessione 2, fetta pilota L26130

> **Cos'è** · Il documento che si porta al gate della Sessione 2: cosa è stato costruito,
> con quali numeri, cosa il pilota ha rotto del design e cosa propone di cambiare.
> **Data** · 16/08/2026.
> **Regola che governa ogni numero qui dentro** · nessuno è scritto a memoria: vengono da
> `qa_all.py` (note ed esiti QA), `conta_fumo.py` (misura di fumo), `collaudo_suite.py`
> (collaudo) e da conteggi eseguiti sui grezzi.

---

## 1. Cosa è stato prodotto

| | |
|---|---|
| Grezzi copiati e verificati | **160/160** contro `manifest_corpus_v1.1.json`: zero scarti, zero estranei, zero sottocartelle |
| Grezzi della fetta | **22** |
| Note prodotte | **58** |
| Suite QA | 6 script + modulo comune, collaudata |
| Esito QA di lotto | **0 ERRORI · 27 AVVISI** |
| Copertura | **22/22** grezzi citati, nessun documento muto |

**Note per cartella:** `areas\` 20 · `entities\` 9 · `projects\` 8 · `code\` 7 · `data\` 4 ·
`docs\` 3 · `concepts\` 2 · `workspace\` 2 · `self\` 1 · `outputs\` 1 · `sources\` 1.
Escluse `workspace\` e `sources\` dai conteggi di qualità: **55**.

**Note per `type`:** 22 atomica · 11 index · 9 conflitto · 8 hub · 7 entita · 1 concetto.

⚠️ **Il budget dichiarato era 20-30 note; ne sono state prodotte 58.** Le note di contenuto
vero sono **41** (58 meno gli 11 `_index` e le 6 note-strumento di `code\`), e di queste 8
sono nate dalle correzioni del revisore. Lo sforamento è reale e va deciso: o il budget si
intende sulle sole note di contenuto e va riscritto in metodo_03, oppure il lotto era
troppo grande.

**Collaudo della suite:** 5 difetti piantati su 5 trovati, 0 falsi positivi sulla nota
corretta. Al primo giro ha scoperto un ramo invertito nel riconoscimento dei wikilink rotti.

**I 27 avvisi, motivati:** 21 sono riscontri visivi su immagini (l'estrattore congelato non
legge i `.jpg`, e le tre immagini sono state lette a occhio); 5 sono note il cui titolo è
una domanda e il cui riassunto è la risposta, quindi non si sovrappongono lessicalmente;
1 è un riassunto al limite dei 250 caratteri.

---

## 2. Mini-misura di fumo — numeri NON ufficiali

Ricontati da `06_operativo\qa\conta_fumo.py` sui due `.jsonl`.

| Esito | Fumo (vault) | Baseline A (grezzo), stessi id | Delta |
|---|---|---|---|
| corretta | **28** (93,3%) | 23 (76,7%) | **+5** |
| parziale | 2 (6,7%) | 6 (20,0%) | −4 |
| sbagliata | 0 | 1 (3,3%) | −1 |
| allucinata | 0 | 0 | 0 |
| fonti corrette | **30/30** | 27/30 | **+3** |

**5 migliorati, 0 peggiorati, 25 invariati.** I migliorati: Q074, Q132, Q138, Q199, Q238.

**Condizioni della misura, da dichiarare ogni volta che questi numeri si citano:**

- **Stesso modello** per rispondente e baseline A: `claude-opus-5`. Il confronto non è
  inquinato dal cambio di modello.
- **Un solo blocco da 30 domande**, senza la suddivisione in dieci giri del P1 della
  baseline: manca quindi l'effetto di degrado su giri successivi che la baseline poteva
  avere, e questo **gioca a favore della fumo**. Va detto.
- 30 domande su 282: una differenza di due o tre esiti non è significativa. Il campione
  dice **se il design regge**, non quanto rende.
- Perimetro fisico rispettato: canone ed eval set erano fuori dal filesystem montato, non
  soltanto vietati da una clausola di prompt.

⚠️ **`giudice_rapporto.md` non esiste su disco.** Nella cartella della misura ci sono
`domande_fumo.jsonl`, `fumo_risposte.jsonl`, `fumo_valutazione.jsonl` e
`rispondente_rapporto.md`. Il verbale del giudice esiste quindi solo nella forma riga-per-riga
del `.jsonl`: le sue motivazioni sono state lette da lì.

---

## 3. La regola di esclusione del giudizio di provenance — 33 note su 41

Lo strato di giudizio ha ricevuto **33 note**; le note candidate oggi sono **41**. La
differenza si spiega con due esclusioni per costruzione e una per cronologia.

**Escluse dal pacchetto, per regola** — il filtro è nel codice di `qa_provenance.py`,
funzione `pacchetto_giudizio`: *salta le note con `type: index` e quelle senza `fonti`*.

1. **Gli 11 `_index`.** Non affermano fatti propri e non possono avere `fonti` (§2.4 lo
   vieta). Le loro annotazioni di mezza riga si verificano contro le note che elencano
   (§7.1 clausola 4), non contro fonti proprie: darle al giudice significherebbe chiedergli
   di giudicare un fatto contro un documento che non c'è.
2. **Le 6 note di `code\`.** Documentano gli script della suite e non discendono da nessun
   grezzo: non hanno `fonti` da cui essere giudicate. È lo stesso buco di specifica del
   rilievo A ancora aperto (§4).

**Escluse di fatto, per cronologia — ed è la parte che va dichiarata:**

3. **8 note non hanno mai visto lo strato di giudizio**, perché sono nate *dopo*, dalle
   correzioni del revisore: `doc-manuale-haccp`, `questione-data-apertura-rec-2026-011`,
   `questione-misura-frammento-strumentale`, `questione-materiale-guarnizione-pkm-450`,
   `questione-codice-ricambio-valvola-pkm-450`, `questione-consegna-farina-mv26-0429a`,
   `entita-elena-marchetti`, `entita-ivano-dal-maso`.

   Sono passate dalla **QA deterministica** (verde) ma non dal giudizio umano/LLM sulle
   affermazioni qualitative. **Il ciclo di §9.5 prescrive di rilanciare la suite dopo le
   correzioni, ma non dice di rilanciare anche lo strato di giudizio**: è una lacuna del
   processo, ed è un emendamento proposto (E9).

11 + 6 + 8 = 25; 41 − 8 = 33 note candidate al momento del pacchetto, tutte giudicate.
**Nessuna nota è andata persa nel passaggio**: la verifica ha inizialmente contato 34
intestazioni nel pacchetto, ma la 34ª era un falso positivo — la stringa `NOTA:` compare
anche dentro il testo del manuale HACCP incluso come fonte. È un difetto del formato del
pacchetto, non del giudizio (emendamento E10).

---

## 4. Il rilievo A ancora aperto: quale e perché

**A9 — le sei note di `code\` non hanno `fonti`.**

`fonti` è obbligatorio e non vuoto per `type: atomica` (§2.4) ed è ERRORE bloccante in
`qa_frontmatter.py` (§7.3). Le sei note che documentano gli script — `script-qa-all`,
`script-qa-frontmatter`, `script-qa-link-integrity`, `script-qa-provenance`,
`script-qa-copertura`, `script-genera-llms-txt` — non ne hanno.

**Perché non è un difetto di compilazione ma un buco della specifica.** Una nota di `code\`
documenta uno **strumento del progetto**, non un fatto dell'azienda: non esiste un grezzo
del corpus da cui discenda. Le uniche fonti candidate sarebbero i documenti di metodo, e
citarli è vietato due volte — §2.3 («le fonti sono SOLO file del corpus») e i divieti 7-8.
Come `type: atomica` quelle note sono quindi **strutturalmente fatti senza fonte**, cioè
violano il divieto 6 per costruzione.

**Come è stato gestito in sessione, e perché resta aperto.** Ho implementato l'eccezione
negli script — costante `SENZA_FONTI = {"code"}` in `qa_comune.py`, con il commento che
dichiara l'emendamento in attesa — così la QA passa. **Ma la regola non è ancora scritta in
metodo_03, e finché non lo è la QA verde poggia su una deroga decisa da me.** È la ragione
per cui il revisore considera il lotto non chiudibile: ha ragione sul piano formale.

Si chiude con la decisione E1 di §7.

---

## 5. Il 22° grezzo: com'è entrato

**Non è entrato un file di nascosto: è un mio errore di conteggio, dichiarato tardi.**

La ricostruzione esatta:

| Passaggio | Conteggio reale | Cosa avevo scritto |
|---|---|---|
| Nucleo elencato nel prompt di sessione | **17 file** | avevo scritto «16 su 16 trovati» |
| Opzione consigliata = nucleo + convocazione + coppia Analytica | **20 file** | avevo etichettato l'opzione «19 file» |
| La tua risposta: «aggiungi anche i 2 duplicati (fetta = 21 file)» | 20 + 2 = **22** | 19 + 2 = 21 secondo il conteggio sbagliato |

L'errore è a monte: **il nucleo del tuo prompt contiene 17 file, non 16** — «le due foto»
vale due, e li avevo contati una volta sola nel totale. Da lì ogni cifra successiva è
slittata di uno, fino al «21» della tua risposta.

**Nessun file è quindi il "22°" in senso proprio**: la fetta è esattamente il nucleo che
avevi indicato più le tre aggiunte che hai approvato, e l'elenco integrale è in
`06_operativo\qa\fetta_l26130.txt` dalla prima riga. L'ho dichiarato prima di scrivere una
sola nota, ma l'ho dichiarato come «22 anziché 21», non come «il mio conteggio era sbagliato
di uno»: è quest'ultima la formulazione corretta.

**Se vuoi tornare a 21**, l'unico modo sensato sarebbe togliere una coppia di duplicati
intera (due file, arrivando a 20): togliere una sola gamba distruggerebbe proprio il
collaudo della regola sui duplicati che avevi chiesto. Non lo consiglio.

---

## 6. I cinque conflitti non registrati, classificati

Classificazione eseguita con script sulle gambe di ciascun conflitto, contro
`fetta_l26130.txt`.

### 6.1 Gambe tutte dentro la fetta → **buco di canonizzazione**

Sono i due casi in cui il vault *avrebbe potuto e dovuto* registrare la divergenza con i
soli documenti che aveva in mano. Alimentano l'emendamento **E2 — riconciliazione
incrociata dei numeri fra fonti**.

**(3) Scarti al riavvio: 348 contro 330.**
`report_fermo_macchina_confezionatrice_MAP.txt` §4 dichiara «confezioni scartate al riavvio
(spurgo + taratura): **348 pz**»; `calcolo_sfrido_efficienza_OEE_linea_bakery.csv` riga 145
dà `Scarto_prodotto_pz` = **330** per l'intero turno. Entrambi in fetta, entrambi già citati
da note esistenti (`fatto-riparazione-guarnizione-non-originale` e `kpi-oee-l26130-l1-t2`).
Nessuna nota ha confrontato i due numeri. E il confronto è imbarazzante: se i perimetri
fossero «riavvio» e «turno intero», il numero di turno dovrebbe essere **il maggiore**, e
invece è il minore.

**(5) NC-2026-102 attribuisce un'origine che il laboratorio rifiuta di attribuire.**
`non_conformita_interne_registro_2026.csv` riga 106, del 20/05: «Esito FTIR Analytica
Veneta: frammento compatibile con elastomero guarnizione non originale, incompatibile con
film MAP e con MOCA di linea», causa radice «**conferma origine interna**».
`Rapporto_di_Prova_AnalyticaVeneta_2026_04187.pdf` §4.3 e §5: «L'attribuzione a una
specifica origine **esula dalle competenze del laboratorio** e dalle prove richieste».
Entrambi in fetta. La nota `fatto-esito-laboratorio-frammento` argomenta correttamente che
«compatibilità non è provenienza», ma **non registra che un documento aziendale ha già fatto
quel salto** — che è il fatto più significativo dei due.

⚠️ Questo secondo caso è più grave del primo: non è un numero che non torna, è una
**conclusione non autorizzata messa a registro** su una pratica che viaggia verso un
cliente e potenzialmente verso un'autorità.

### 6.2 Almeno una gamba fuori dalla fetta → **lista di tracciamento per S4-S5**

Non sono buchi di questo lotto: la fonte che li rende visibili non era nel perimetro. Vanno
tracciati perché il lotto che porterà dentro quella fonte li chiuda.

| Conflitto | Gambe in fetta | Gambe fuori | Da riprendere quando entra |
|---|---|---|---|
| **(1) MOD-QA-07, tre versioni dello stesso turno** | `MOD-QA-07_…scansione.jpg` | `checklist_metal_detector_manuale_operaio.txt`, `appunti_capoturno_quaderno_linea1_OCR.txt` | la trascrizione del modulo e il quaderno del capoturno |
| **(2) Pezzi del turno: esiste una terza fonte** | mass balance, foglio OEE | `appunti_capoturno_quaderno_linea1_OCR.txt` («0450: solo 4.100 pz oggi + quelo di T1») | il quaderno del capoturno |
| **(4) Arrivo dell'officina: 15:25 contro 15:50** | `report_fermo_macchina_…txt` | `appunti_capoturno_quaderno_linea1_OCR.txt` | il quaderno del capoturno |

**Il quaderno del capoturno (`appunti_capoturno_quaderno_linea1_OCR.txt`) è la gamba
mancante di tre conflitti su tre.** È il singolo file che, entrando, obbligherà a riaprire
`fatto-verifiche-ccp3-turno-l26130`, `questione-pezzi-prodotti-l26130` e
`fatto-fermo-pkm-450-l26130`. Va messo in cima al lotto che tocca la Linea 1.

---

## 7. Il vaglio dei tre rilievi espliciti del rispondente

Tutti e tre verificati da me sui grezzi, uno per uno.

### 7.1 PRP-09 — la nota `lotto-l26130` dichiara un'assenza che è falsa · **CONFERMATO, ed è un errore mio**

**Il manuale HACCP È DENTRO la fetta** — è fonte di sei note — e dichiara la regola di
composizione del codice di lotto in **due punti**:

- riga 176, Fase 14: «Etichettatura e stampa lotto/TMC (**formato lotto: L26\<ggg\>-\<linea\>-\<turno\>**)»;
- riga 353, **PRP-09 Rintracciabilità**: «PRO-QA-08: identificazione lotto L26\<ggg\>-\<linea\>-\<turno\>».

La nota `lotto-l26130` afferma invece che «la regola di composizione del codice **non è
scritta in nessuno dei grezzi di questa fetta**» e presenta la decodifica come inferenza
dichiarata. **L'affermazione è falsa**, e l'ironia è che riguarda proprio il watch-item del
15/08: il watch-item è stato «risolto» nel modo sbagliato, riformulando come inferenza un
fatto che una fonte in fetta attesta per esteso.

**Perché è successo, ed è la parte che conta.** Ho cercato la regola nei documenti dove mi
aspettavo di trovarla — il mass balance, il rapporto di fermo, il modulo del metal detector
— e non l'ho cercata in tutto `sources\`. Ho poi scritto l'assenza come se l'avessi
verificata. È esattamente l'errore che il divieto §10.6 vieta, applicato a un'assenza invece
che a una presenza.

→ Alimenta l'emendamento **E3 — mai dichiarare un'assenza senza ricerca su tutto `sources\`**.

### 7.2 Integrità del datalogger dichiarata fallita, non rilevata da nessuna nota · **CONFERMATO**

Il footer del log chiude con: «**Checksum: 8f3a…41bc – verifica integrità fallita**», e
poco sopra «Sonda T_CUORE: anomalia rilevata (vedi codice guasto) - **validità parziale**».
Nessuna nota del vault lo registra. `macchina-pt-104` documenta il codice `-999.9`/`FAULT`
ma non che **il file dichiara sé stesso non integro**.

Non intacca le letture usate — la finestra della deviazione è pulita e coerente — ma è
precisamente il genere di fatto su cui un auditor apre una discussione: un tracciato che
attesta un punto critico e che dichiara la propria integrità fallita.

→ Nota da creare in `areas\` (`area: qualita`), esito del gate.

### 7.3 Il footer sbaglia sonda e durata · **CONFERMATO**

Due affermazioni del footer non reggono contro le righe dello stesso file:

- «**Temperatura minima registrata TT_02: 68.6 C alle 14:30:37**» — `TT_02` è la sonda **di
  camera**, non quella al cuore. Chi legge il footer come riepilogo della grandezza
  governata dal CCP2 riporta **68,6** invece di **68,9 °C**.
- «**Permanenza sotto soglia 72.0 °C: 27 min ca.**» — il conteggio sulle righe dà **24 min
  30 s** (14:20:07 → 14:44:37). La non conformità interna e la riunione dicono **29 min**
  (14:18-14:47), finestra che include quattro letture fra 72,4 e 72,9 °C, cioè sotto il set
  point ma **sopra** il limite critico: è probabilmente lì che nasce l'errore, avendo preso
  l'inizio del flag `WARN` per l'inizio della violazione.

Sulla stessa grandezza, nello stesso file, circolano quindi **tre durate: 24,5 · 27 · 29
minuti**, e il conteggio sulle righe è l'unico verificabile. Il vault ne registra due (24,5
nella nota, 29 come divergenza dichiarata) e **non registra la terza, che sta nel footer
della fonte principale**.

→ Nota-questione da creare, esito del gate. Ottimo candidato anche per E2.

### 7.4 La finestra 18:45-19:08 dopo il riavvio · **CONFERMATO integralmente**

Ricontato da me riga per riga:

| Fatto | Verifica |
|---|---|
| Riavvio `MACHINE_RUN` | 18:45:07 ✓ |
| Nastro riparte a 2,0 m/min | `BELT_START SPEED_SP=2.0` alle 18:46:37 ✓ |
| Nastro a velocità di regime 4,2 m/min | `BELT_SP_CHANGE SPEED_SP=4.2` alle 18:52:07 ✓ |
| `MODE HEATING` | riga 1623, 18:58:07 ✓ (nel file la sintassi è `MODE;HEATING`, il rispondente l'ha parafrasata come `MODE=HEATING`: il fatto è esatto) |
| Letture `T_CUORE` sotto 72,0 fra riavvio e risalita | **33**, tutte con flag `OK` ✓ |
| Risalita sopra il limite | 74,5 °C alle 19:08:07 ✓ |

**Nessun documento dell'archivio commenta questa finestra** — né la non conformità, né la
riunione, né la scheda reclamo, né alcuna nota. Il rispondente non ha concluso che sia una
seconda deviazione, e ha fatto bene: il tracciato marca la fase come riscaldamento, quindi
la logica di macchina non applica la soglia. Ma **il nastro era in marcia a velocità di
regime**, e la domanda se sul nastro ci fosse prodotto l'archivio non la pone.

→ **Candidata nota-questione** in `areas\` (`area: qualita`), `stato: aperto`, esito del
gate. Con l'avvertenza che la nota deve fermarsi dove si è fermato il rispondente: riportare
i dati e la marcatura `HEATING`, **senza concludere** che ci fosse prodotto.

---

## 8. Q019 e Q237 — le due voci del verbale del giudice

### 8.1 Q019 · il rispondente ha citato una **nota del vault**, non un documento del canone

**Il fatto, verificato:** in `fumo_risposte.jsonl`, Q019 porta
`"fonti": ["manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt", "docs/doc-ccp2-limite-critico.md"]`.
È **l'unica** delle 30 risposte che cita una nota del vault: il rapporto del rispondente ne
dichiara «due casi», ma il conteggio sul file ne trova uno solo.

**La correzione di interpretazione.** Nel verbale del giudice quella citazione è descritta
come «documento del canone». **Non lo è, e non poteva esserlo:** `docs\doc-ccp2-limite-critico.md`
è una **nota del vault**, scritta in questa sessione; il canone (`01_metodo\canone_aurora.md`)
era **fisicamente fuori dal perimetro montato** del rispondente, che aveva `--add-dir` solo
su `04_misurazioni\`. Nessun accesso al canone è avvenuto né era possibile.

⚠️ **Il testo del giudice non è stato modificato** e non va modificato: è testimonianza di
come un valutatore, che vedeva solo i nomi dei file citati, ha interpretato un percorso
`docs/…md`. La correzione vive qui e nel decision log, non nel verbale.

**La domanda vera che questo apre, e che non si decide adesso:** quando la risposta cita una
nota del vault invece del grezzo, **come conta `fonti_corrette`?** Nella misura «dopo» il
perimetro è l'intero vault, quindi citare una nota sarà legittimo e frequente — ma se conta
come fonte corretta, il confronto con la baseline A (dove esistevano solo grezzi) misura due
cose diverse. **Proposta da discutere in pre-registrazione, prima della Sessione 6: la fonte
che conta resta il grezzo; la nota è navigazione, non provenienza.** Registrata nel decision
log come decisione da prendere, non come decisione presa.

### 8.2 Q237 · riserva del giudice, riesame a occhio

Esito assegnato: **corretta**, fonti corrette. La motivazione porta però una riserva
esplicita: «la prevalenza è applicata nella conclusione ma **non enunciata come regola**».

**Riesame a occhio, come previsto al gate.** La risposta afferma che il turno non è stato
conforme, fondando il verdetto sul datalogger (50 letture sotto 72,0, minimo 68,9, flag
`ALARM` su 49) contro il «74,5 conforme» del registro cartaceo, e cita quattro fonti fra cui
il quaderno del capoturno. **La riserva è fondata ma non cambia l'esito:** il criterio
chiedeva di stabilire la non conformità, e la risposta la stabilisce con i dati giusti; non
enunciare «fra cartaceo e datalogger prevale il datalogger» come regola generale è una
mancanza di forma, non di sostanza. **Confermo `corretta`.**

Vale però come segnale sul vault: la regola di prevalenza *è* scritta in
`fatto-registro-cartaceo-mod-qa-12`, e il rispondente non l'ha ripresa. Se una regola
dichiarata nelle note non arriva nella risposta, è un indizio che va enunciata anche nel
`summary`, che è ciò che il retrieval mostra per primo.

---

## 9. Emendamenti proposti a metodo_03

Classificati come richiesto: **refuso** (il manuale dice una cosa sbagliata), **chiarimento**
(dice una cosa ambigua), **regola nuova** (non dice nulla e serve).

| # | Sezione | Tipo | Cosa cambia, e perché |
|---|---|---|---|
| **E1** | §2.4 | **regola nuova** | **`fonti` facoltativo per le note di `code\`.** Una nota che documenta uno strumento del progetto non discende da un grezzo, e citare un documento di metodo è vietato. Senza questa riga sei note violano lo schema per costruzione. **È il rilievo A ancora aperto.** |
| **E2** | §5.1 o §7.4 | **regola nuova** | **Riconciliazione incrociata dei numeri fra fonti del lotto.** Quando due grezzi dello stesso lotto riportano la stessa grandezza, il confronto va fatto e l'esito scritto — anche quando i due numeri stanno in note diverse. Il pilota ha mancato due divergenze con entrambe le gambe in fetta (§6.1). |
| **E3** | §10, nuovo divieto | **regola nuova** | **Mai dichiarare un'assenza nei grezzi senza averla cercata su tutto `sources\`.** Un'assenza affermata è un fatto, e va verificata come un fatto. Il pilota ha scritto che nessun grezzo dichiarava la regola del lotto, mentre il manuale HACCP la dichiara in due punti (§7.1). |
| **E4** | §2.3, tabella locator | **refuso** | La grammatica `.xlsx` prescrive `foglio «X», riga <n>`, ma gli esempi del manuale usano `righe 6-9`. Ammettere `riga <n>` **e** `righe <n>-<m>`. |
| **E5** | §2.3 | **chiarimento** | Il locator è un **prefisso** della riga, non la riga intera: dopo di esso è ammesso il testo che spiega cosa si trova lì. Senza, ogni locator con una coda esplicativa risulta fuori grammatica. |
| **E6** | §7.1 | **regola nuova** | **Verifica testuale solo per le citazioni di almeno cinque parole.** In italiano «…» marca anche nomi di foglio, titoli di sezione ed etichette — e metodo_03 le usa così nei propri esempi. Senza soglia, la QA boccia le note corrette. |
| **E7** | §5.4 / §7.1 clausola 2 | **regola nuova** | I **valori contati** (non solo quelli sommati) vanno dichiarati: «50 letture *(contate: una ogni 30 s da … a …)*». §5.4 copre l'aritmetica sugli addendi ma non i conteggi, che sono altrettanto frequenti. |
| **E8** | §7.1 clausola 1 | **chiarimento** | La normalizzazione prima del confronto deve: togliere il **quoting delle mail** (`> ` a inizio riga, che spezza le citazioni delle `.eml`), generare le **varianti di data** a due e quattro cifre d'anno, e rimuovere l'enfasi markdown. |
| **E9** | §9.5 | **chiarimento** | Dopo le correzioni si rilancia la suite **e lo strato di giudizio sulle note nuove o modificate**. Oggi il ciclo prescrive solo la QA: 8 note nate dalle correzioni non hanno mai visto il giudizio (§3). |
| **E10** | §7.1 | **chiarimento** | Il pacchetto per il giudice deve usare un **delimitatore che non possa comparire nei grezzi**: `NOTA:` collide col testo del manuale HACCP e falsa il conteggio delle note inviate. |
| **E11** | §7.2 | **chiarimento** | La **reciprocità hub/spoke** si verifica sul **primo hub** citato in `related` (l'hub proprio della nota) e non sulle note `type: hub`: `related` porta anche i rimandi laterali, e pretenderli tutti annega il controllo nel proprio rumore. |
| **E12** | §4.4 | **chiarimento** | Il **minimo di due wikilink** conta anche quelli di `related`, non solo quelli del corpo: è in `related` che vive il rimando spoke → hub. Il grafo degli orfani resta invece sui soli link del corpo, come già scritto. |
| **E13** | §7 | **chiarimento** | In perimetro di lotto, **copertura degli `_index` e componente unica** si valutano sulle sole cartelle che il lotto tocca. Pretenderle su tutte e undici fa fallire ogni lotto per un difetto che è solo l'incompletezza del vault. |
| **E14** | §7.1 | **refuso** | Il controllo di **coerenza interna** va eseguito dopo aver rimosso gli orari: «dalle 14:20:07 alle 14:44:37» viene altrimenti letto come l'etichetta «dalle 14» con due valori diversi, e boccia proprio le note che descrivono bene una finestra temporale. |
| **E15** | §3.1, esempio compilato | **refuso** | L'esempio di `fatto-deviazione-ccp2-l26130` dice «50 letture consecutive» con flag `ALARM`: le letture sotto 72,0 sono 50, ma le `ALARM` sono **49** (la prima, alle 14:20:07, è `WARN`). E «alle 14:49:37 il processo è rientrato»: il rientro sopra il limite è alle **14:45:07**, il flag torna `OK` alle **14:47:07**. |
| **E16** | §3.5, esempio `concetto-fefo` | **refuso** | Il locator «intestazione riga 1 «logica FEFO»» non rispetta la grammatica `.csv` che il manuale stesso fissa. |
| **E17** | §9.4 o §9.5 | **chiarimento** | Dichiarare **su cosa si misura il budget di un lotto**: le note di contenuto, oppure tutte comprese `_index` e note-strumento. Il pilota ha prodotto 41 note di contenuto e 58 in totale, contro un budget di 20-30 (§1). |

---

## 10. Il prompt di giudizio, da congelare

Il testo è già nella costante `PROMPT_GIUDIZIO` di `06_operativo\qa\qa_provenance.py`, con
`PROMPT_GIUDIZIO_DATA = "2026-08-16"`. **Ha funzionato**: ha prodotto 33 giudizi con una
riga JSON ciascuno, 7 rilievi tutti fondati e verificati, nessun falso allarme, nessuna
riscrittura delle note, nessuna richiesta del canone.

Congelandolo si accetta anche la sua **rubrica chiusa a quattro esiti** (`pulita`,
`fonte_inutile`, `afferma_oltre`, `entrambi`) e le tre clausole che lo hanno tenuto onesto:
un'inferenza dichiarata non si segnala; una nota che riporta due valori divergenti senza
sceglierne uno sta facendo il suo mestiere; il giudice non riceve il canone.

---

## 11. Cosa NON è stato fatto, per vincolo esplicito

- **Nessuna modifica al prompt del rispondente per la Sessione 6.** Gli esiti della fumo non
  toccano lo strumento di misura: fra «prima» e «dopo» cambia solo la forma dell'archivio.
  Il P1 resta quello congelato in metodo_02.
- **Nessuna nota è stata corretta dopo la fumo.** Il vault è congelato allo stato con cui la
  misura è stata eseguita: le correzioni sono esito del gate, e dopo di esse la suite QA si
  rilancia da capo.

---
---

# Appendice — Esito della chiusura

> Aggiunta il **17/08/2026**, dopo l'approvazione del gate. **Il corpo del rapporto qui sopra
> resta com'era al momento del gate** e non è stato ritoccato: questa appendice registra cosa
> è stato deciso e cosa ne è seguito.

## Cosa è stato approvato

I **17 emendamenti**, con quattro precisazioni vincolanti che li hanno modificati in meglio:

1. **E1 vale per la nota-strumento, non per la cartella `code\`.** Il discrimine è il prefisso `script-`: una futura nota su un'automazione aziendale — fondata su grezzi — resta a schema pieno. Nel corpo della nota-strumento va il percorso del sorgente nel repository. Le note esenti restano fuori dallo strato di giudizio e si rivedono a occhio a ogni gate.
2. **E3: l'assenza dichiarata si data e si riferisce al manifest** («verificata su tutto `sources\`, manifest v1.1, <data>»), così non marcisce in silenzio quando arriverà il corpus v2.
3. **E11 va scritto anche in §2**, dove `related` si definisce, non solo in §7.2: chi canonizza legge §2.
4. **E17 deciso**: il budget si misura sulle note di contenuto e si fissa lotto per lotto nel prompt di lotto.

Più due regole aggiunte in corso di applicazione:

- **E18** — se una nota stabilisce una regola decisionale, il `summary` la enuncia. Nata dalla riserva del giudice su Q237 e applicata **come regola generale di vault**, non come ritocco alla nota che una domanda della fumo aveva toccato.
- **E19** — il **piè di pagina di un `.log` non era puntabile**: la grammatica prevedeva solo forme con timestamp, e un riepilogo di export non ne ha. Emerso scrivendo le note del gate.

**Totale: 19 emendamenti applicati a metodo_03.**

## Le due verifiche retroattive imposte al gate

- **`fatto-deviazione-ccp2-l26130` non ha ereditato gli errori dell'esempio E15.** Distingue il `WARN` delle 14:20:07 dall'`ALARM` dalle 14:20:37 (49 letture) e dà il rientro a 14:45:07 con `OK` alle 14:47:07. **La nota era più precisa del manuale che la conteneva**, e il manuale è stato corretto su di essa.
- **La settima nota di `code\` è `_index-code.md`**: è un `index`, quindi senza `fonti` per la regola generale §2.4 e fuori dal giudizio per la stessa ragione — non per l'esenzione delle note-strumento. In `code\` non esiste oggi alcuna nota fondata su grezzi.

## Le correzioni applicate

Tutte e sei le autorizzate, più le due azioni aggiuntive:

| # | Correzione | Esito |
|---|---|---|
| 1 | `lotto-l26130` dichiarava falsamente che nessun grezzo contiene la regola del lotto | riscritta: la regola è in due punti del manuale HACCP, ora citato in `fonti` |
| 2 | scarti 348 contro 330 | nata `data\questione-scarti-riavvio-l26130` |
| 3 | NC-2026-102 contro il rifiuto del laboratorio di attribuire l'origine | nata `areas\fatto-nc-102-origine-interna` |
| 4 | integrità del datalogger dichiarata fallita | nata `areas\fatto-riepilogo-datalogger-inaffidabile`, che copre anche la sonda sbagliata nel piè di pagina |
| 5 | tre durate per la stessa finestra (24,5 · 27 · 29 min) | nata `areas\questione-durata-deviazione-ccp2-l26130` |
| 6 | finestra 18:45-19:08 dopo il riavvio | nata `areas\fatto-risalita-termica-post-riavvio-l26130`, **con la clausola di freno rispettata**: dati e marcatura riportati, nessuna conclusione sul prodotto in nastro |
| 7 | E18 applicata a tutte le note dove ricorre | riscritti i `summary` di `fatto-registro-cartaceo-mod-qa-12` e `fatto-deviazione-ccp2-l26130` |
| 8 | `giudice_rapporto.md` | creato nella cartella della fumo, **etichettato come trascrizione salvata a posteriori** |

## Il giudizio retroattivo (E9 applicato al pilota stesso)

Rieseguito su **tutte le 46 note candidate** — le 8 mai giudicate, le 5 nate al gate e tutte
quelle toccate dalle correzioni — da un subagente a contesto pulito, senza canone.

| Esito | Note |
|---|---|
| `pulita` | **42** |
| `afferma_oltre` | 4 |
| `fonte_inutile` | 0 |
| **giudicate** | **46** |

**I quattro rilievi, tutti fondati e tutti corretti:**

- **`prodotto-af-sn-0450`** — affermava una «divergenza nota» sui pezzi per cartone che **nessuna fonte contiene**. ⚠️ È il rilievo più grave del giro: quell'informazione veniva dal report del revisore, che aveva il canone. **Era una fuga di canone dentro il vault**, ed è stata rimossa.
- **`questione-materiale-guarnizione-pkm-450`** — attribuiva alle tre fonti citate il PTFE del kit originale, che sta invece nella mail del costruttore: fonte aggiunta.
- **`fatto-risalita-termica-post-riavvio-l26130`** — presentava come «leggibile nel tracciato» una spiegazione che il tracciato non dà, e il record di riscaldamento arriva **tredici minuti dopo** le prime letture già marcate normali. Riscritta come ipotesi dichiarata, con il rilievo temporale.
- **`questione-consegna-farina-mv26-0429a`** — attribuiva al mass balance la parola «sacco», che sta solo nell'inventario: tabella corretta.

## Numeri finali, dopo le correzioni

*(ricontati da `qa_all.py`, non a memoria)*

| | Al gate | Alla chiusura |
|---|---|---|
| Note totali | 58 | **63** |
| Note di contenuto | 41 | **46** |
| `_index` · note-strumento | 11 · 6 | 11 · 6 |
| Questioni aperte (`type: conflitto`) | 9 | **11** |
| QA di lotto | 0 errori · 27 avvisi | **0 errori · 33 avvisi** |
| Copertura | 22/22 | **22/22** |

**Note per cartella:** `areas\` 24 · `entities\` 9 · `projects\` 8 · `code\` 7 · `data\` 5 ·
`docs\` 3 · `concepts\` 2 · `workspace\` 2 · `self\` 1 · `outputs\` 1 · `sources\` 1.

**Per `type`:** 25 atomica · 11 index · 11 conflitto · 8 hub · 7 entita · 1 concetto.

I 33 avvisi restano delle tre famiglie già motivate: riscontri visivi sulle immagini,
riassunti che rispondono al titolo invece di parafrasarlo, una lunghezza al limite.

## Il pass di vault, e perché è rosso

Lanciato anche `--perimetro vault`, e **fallisce come deve**: 138 grezzi non ancora citati da
nessuna nota e il grafo in più componenti, perché le note-strumento di `code\` non sono
agganciate al resto. **Non è un difetto del lotto**: è la fotografia di un vault che ha
canonizzato 22 documenti su 160. Il pass di vault verde è il traguardo delle Sessioni 4-5.

⚠️ Da portare in Sessione 4: **le note-strumento formano una componente staccata del grafo**.
Vanno agganciate in modo non artificioso, o va deciso che `code\` è esclusa dal controllo di
componente unica come lo sono `workspace\` e `sources\`.

## Il prompt di giudizio: congelato

Il testo resta in `06_operativo\qa\qa_provenance.py`, costante `PROMPT_GIUDIZIO`, data
`2026-08-16`. Ha retto due giri completi — 33 giudizi al primo, 46 al secondo — con 11
rilievi complessivi, **tutti fondati e nessun falso allarme**.
