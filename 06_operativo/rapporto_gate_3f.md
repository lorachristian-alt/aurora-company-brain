# Rapporto del gate del lotto 3F — E65, le tre estensioni, e il tema 3 chiuso

> **Che cos'è** · L'esito del gate del lotto 3F, eseguito il **31/08/2026** su
> `06_operativo\prompt\prompt_gate_3f_r2.txt`. Contiene ciò che il prompt del gate chiede: le
> decisioni sulle **cinque voci** del §10 di `rapporto_lotto_03f.md`, il **fix dell'esenzione
> della data derivata** col suo collaudo e il confronto riga per riga, e i **due adempimenti
> arretrati di 3E**.
> **Chi lo legge** · Il coordinatore. Le regole che ne nascono vivono in `metodo_03`, non qui.
> **Misure** · tutte da script, ognuna con la sua ora (E44), prese fra le **18:05 e le 18:10**
> del 31/08/2026. ⚠️ **Questo gate HA toccato il vault** — la data del 26/05 è rientrata in una
> nota — quindi la misura del vault è del gate e non del lotto.

---

## 0. La verifica d'apertura, e il commit

`prompt_s4_lotti.txt`, aggiornato dal coordinatore da E64 a E65 più tre estensioni, verificato
sulle **sei metriche prima di eseguire**:

| Metrica | Atteso | Misurato | |
|---|---|---|---|
| righe | 823 | **823** | ✅ |
| byte | 50.373 | **50.373** | ✅ |
| CRLF | 823 | **823** | ✅ |
| LF isolati | 0 | **0** | ✅ |
| BOM | assente | **assente** | ✅ |
| sha256 | `718a49c7…78d239` | `718a49c7…78d239` | ✅ |

⚠️ **Anche i CR isolati sono zero**, misurati fuori dalle sei metriche: un CR orfano non
comparirebbe in nessuna delle sei e romperebbe il file lo stesso.

I due file di prompt sono stati **committati e pushati prima di eseguire** — `626b3e2`,
«prompt dei lotti a E65 e prompt del gate 3F + apertura R2».

### 0.1 ⚠️ LA DATA DEL PROMPT E LA DATA DELL'ESECUZIONE NON COINCIDONO

Il prompt del gate è **scritto dal coordinatore il 25/08/2026**; il gate è stato **eseguito
il 31/08/2026**. ⚠️ **Le regole si datano col gate che le scrive, e le misure con l'ora in
cui sono prese** (E44): **E65 e le tre estensioni portano quindi il 31/08/2026**, in
`metodo_03` come nel registro, e le misure di chiusura portano l'ora del 31.

⚠️ **Il CONTROLLO DI SCOSTAMENTO del prompt dei lotti resta concorde**: la sua riga dice
*Ultimo emendamento recepito: E65*, e l'ultima riga del registro è E65. ⚠️ **La riga di
allineamento di `prompt_s4_lotti.txt` porta «Allineato al: 2026-08-25» e NON è stata
toccata**: quel file è l'istruzione data alla sessione, e **una sessione non riscrive le
proprie istruzioni**. Si segnala qui, che è il posto in cui il coordinatore lo legge.

---

## 1. Le decisioni del gate, in una tabella

| | Voce del §10 | Decisione | Dove vive |
|---|---|---|---|
| **1** | il secondo delimitatore | ✅ **E10 ESTESO** — la proprietà vale per **ogni** delimitatore della catena | `metodo_03` §7.1 |
| **2** | la data derivata | ✅ **E50 ESTESO, e il fix fatto SUBITO** | `metodo_03` §9.5 · `qa_provenance.py` · `_collaudo\collaudo_data_derivata.py` |
| **3** | il superlativo sull'elenco | ✅ **accolta dentro E65**, con la sua regola operativa che resta: **E57 ESTESO** | `metodo_03` §9.5 |
| **4** | l'unità della misura dei due tassi | ⛔ **RESPINTA: lo strumento non si tocca**, con criterio pre-registrato | §6 del passaggio di consegne |
| **5** | il perimetro dell'affermazione | ✅ **E65 NASCE, ed è il cappello** | `metodo_03` §9.5, passo 5 |

**Il lotto è APPROVATO, e con lui il TEMA 3 è chiuso.**

---

## 2. ⚠️ E65 — perché un cappello e non una sesta porta

La famiglia era già stata affrontata **una porta per volta**, e ogni volta la classe rientrava
da quella che nessun emendamento presidiava:

| La specie | La sua porta, prima di E65 |
|---|---|
| primato sull'archivio | **E47** · **E57** |
| assenza sull'archivio | **E3** · **E43** |
| rimando che descrive | **E64** |
| **regola generale importata** | ⚠️ **nessuna** |
| **nesso causale non stabilito** | ⚠️ **nessuna** |

⚠️ **Le due specie senza porta sono anche le due che nessun controllo deterministico può
vedere**: non contengono numeri, non contengono superlativi, non contengono negazioni. **Le
vede solo chi confronta la frase col perimetro** — lo strato di giudizio, o chi rilegge con la
domanda giusta in mano. È la ragione per cui E65 è una regola **di scrittura** e non di suite:
nessuno script la farà rispettare al posto di chi scrive.

⚠️ **E65 non sostituisce le quattro porte: le contiene.** Ognuna resta la regola operativa
della sua specie e continua a scattare dove scattava.

**Le due sole vie per uscire dal perimetro** — l'**artefatto** della ricerca (E43) e il
**rimando** che nomina (E64). ⚠️ **E la terza, che sembra una via e non lo è: aggiungere una
fonte.** Una fonte si aggiunge quando prescrive ciò di cui la nota parla (E36), non per
giustificare una frase già scritta: quello è il gesto che E41 vieta sui tassi, spostato sulla
provenienza.

---

## 3. ⛔ IL FIX DELL'ESENZIONE, E IL CONFRONTO RIGA PER RIGA

E50 diceva che il numero contato è un derivato e si scrive con la marca. **Lo strato
deterministico aveva preso la regola alla lettera**: l'esenzione di `qa_provenance` valeva per
il solo `genere == "numero"`, e **una data derivata non ne aveva nessuna** — respinta anche
marcata.

### 3.1 Che cosa il fix cambia, e che cosa no

⚠️ **È un fix di PERIMETRO di un controllo** (§4), non un allentamento: `valori_esenti`
raccoglie ora **per genere**, e restituisce `{numero, data}` invece di un insieme piatto. **La
marca resta obbligatoria**, e **la finestra resta stretta** — sessanta caratteri prima della
marca, come per i numeri. ⚠️ **E i due generi non si travasano**: un numero marcato non esenta
una data, e viceversa.

### 3.2 Il collaudo, otto casi nei due versi

| # | Caso | Atteso | Esito |
|---|---|---|---|
| 1 | **LA PREMESSA**: la fonte finta non contiene né la data né il numero | non c'è | ✅ |
| 2 | **difetto piantato, verso 1**: data derivata **marcata** | tace | ✅ |
| 3 | **difetto piantato, verso 2**: stessa data **senza marca** | **SCATTA** | ✅ |
| 4 | **non-scatto di regressione**: numero derivato marcato | tace | ✅ |
| 5 | regressione, verso opposto: numero senza marca | **SCATTA** | ✅ |
| 6 | **la finestra resta stretta**: marca oltre i sessanta caratteri | **SCATTA** | ✅ |
| 7 | **i generi non si travasano**: marca su un numero, data non marcata accanto | **SCATTA** | ✅ |
| 8 | la data che la fonte **enuncia**, senza marca | tace | ✅ |

⚠️ **Il caso 1 è la premessa, e senza di lei i casi 3, 6 e 7 tacerebbero per il motivo
sbagliato**: è la stessa disciplina ratificata sul collaudo del delimitatore.

⚠️ **I casi 6, 7 e 8 sono quelli che impediscono al fix di diventare un condono**, e valgono
quanto i due difetti piantati.

### 3.3 Il confronto riga per riga sul fuori perimetro

| | Prima del fix | Dopo il fix |
|---|---|---|
| righe di `qa_provenance` a perimetro vault | **116** | **116** |
| sparite | | **0** |
| comparse | | **0** |

⚠️ **Zero differenze, ed è il risultato giusto**: nessuna nota del vault usava ancora la forma
nuova, quindi il fix non poteva sanare nulla retroattivamente — **e non ha rotto nulla**. Il
difetto piantato prova che funziona; il confronto prova che non ha fatto altro.

### 3.4 E la data è rientrata

⚠️ **Il 26/05 è tornato nel corpo di `fatto-riunione-di-preparazione-il-mattino-dopo`**, con la
marca *(derivato: il giorno dopo la mail del 25/05)*, e la QA del lotto resta a **0 errori**.
**Lo slug resta com'è**: «il mattino dopo» non afferma il falso, e un rinomino senza necessità
è churn.

⚠️ **Una cosa che il fix ha reso visibile, e vale per chi scrive**: `RE_DERIVATO` richiede che
la marca **cominci** con la parola chiave — `(derivato: …)`, `(contate)`, `(calcolato)`. Una
marca come `(rapporto fra le due cifre, calcolato)` **non è riconosciuta**, perché la parola
chiave non è in testa. Il collaudo l'ha scoperto al primo giro, sul suo stesso caso 2.

---

## 4. ⛔ LA VOCE 4 RESPINTA, E IL CRITERIO CHE LA SOSTITUISCE

I tre residui-enumerazione di 3F **dichiarati col loro nome sono la forma giusta.** Cambiare
l'unità della misura **a numeri visti** romperebbe la comparabilità della serie (§4.45) e
sarebbe un fix che allenta (§4.9) — **su tre casi di un solo lotto**, e di un lotto fatto di
elenchi per natura.

> **CRITERIO PRE-REGISTRATO** (§6 del passaggio di consegne): **se in DUE lotti futuri i
> residui-enumerazione sono la metà o più delle scoperte del tasso**, la distinzione
> affermazione/enumerazione **si meccanizza** con la disciplina di §4.9 — perimetro chiuso,
> difetti piantati nei due versi — e **la serie annota il cambio d'unità dal punto in cui
> vale**, senza rimisurare i punti anteriori. **Se non accade, il residuo dichiarato basta.**

⚠️ **È la forma che il progetto ha imparato a dare a un dubbio**: non si decide su
un'impressione, e non si rimanda a tempo indeterminato — si scrive **che cosa si guarderà** e
**quando basterà**.

---

## 5. Le due partite di 3E, pagate qui

Il rapporto del lotto 3E aveva composto **a mano** i numeri del perimetro — «4 toccate» —
perché `conta_perimetro_lotto.py` dava **zero** e nessuno l'ha dichiarato guasto.

| Voce | Diceva | È |
|---|---|---|
| note nate | 37 | **37** — confermato |
| note toccate (E32) | **4**, più i sei hub | **12** |
| note controllate | **58** | **49** |

⚠️ **È la stessa malattia dei numeri a mano del gate di 3B, comparsa stavolta DENTRO una
sessione — e peggiore.** Là i numeri erano sbagliati; qui erano **giusti**, ed è esattamente
per questo che hanno **nascosto il guasto dello strumento per un lotto intero**. La prassi
dello strumento è scritta nell'intestazione del suo stesso output — *si incolla verbatim, i
numeri del perimetro non si ricompongono a mano* — e **un controllo che dà un numero
impossibile si dichiara, non si aggira** (§4.25).

**ADEMPIUTO**: errata datata in §6.1 di `rapporto_lotto_03e.md`, e riga in §5 del passaggio di
consegne.

---

## 6. Le ratifiche che valgono da precedente

| | |
|---|---|
| **la forma del fix del delimitatore** | il prefisso che un grezzo non scrive, la guardia che confronta i **caratteri** e non la presenza, e **la PREMESSA nel collaudo** — che è ciò che impedisce al caso di passare per il motivo sbagliato |
| **il controfattuale NON cercato** | un giudizio su fonti troncate è **ingresso degradato** (§4.31) e vale zero: non si va a vedere «che cosa avrebbe detto», si rifà |
| **E60 per evento al primo impiego** | sei confronti col verbale canonizzato in S2 — cinque note e due questioni che **senza l'artefatto non sarebbero esistite**, e l'estensione aveva poche ore |
| **E59 sul dominio storico** | `pulizi` e `\bigien` respinte dal collaudo ed espunte con la ragione scritta; **il 3,3 % di 2A NON si rimisura** (§4.45) e prende l'annotazione |
| **l'espressione MUTA resta** | `tampon[ei] superfic` riconosce **zero** note (`collauda_dominio.py`, prova A, **31/08 alle 18:12**), **ma toglierla lascerebbe scoperte le note future sui tamponi ambientali**: resta nella dichiarazione **con la mutezza annotata** in `candidate_r1.py`, si riesamina a ogni esercizio del dominio, e il collaudo di E59 la riproverà comunque. ⚠️ **E la mutezza è stata verificata, non creduta**: la locuzione compare in **sette** punti del vault *(contati)*, e **tutti e sette stanno dentro il blocco `## Fonti`** — titoli di file e locator, cioè ciò che `testo_della_nota` esclude apposta (E36 applicato allo strumento). **Nessuna nota ne parla nel corpo**, ed è per questo che la misura la vede muta |
| **il punto non degenere** | dichiarato con la clausola di E41 esteso **che si è fermata da sé**, e i tre residui dichiarati senza aggiustare: **la forma giusta due volte** |
| **B3 / T184** | la divergenza fermata da `verifica_matrice_lotti` **con la QA verde e la nota corretta**: a fermare la fuga è stato **un controllo, non una lettura** |
| **`conta_perimetro_lotto.py`** | riparato **nella sua disciplina** — i dati allineati alla forma che lo strumento dichiara, **non lo strumento allargato ad accettare due forme** |

---

## 7. I numeri di chiusura (E44), tutti da script e con l'ora

| Misura | Valore | Strumento | Ora |
|---|---|---|---|
| **Emendamenti** | registro e manuale **concordano a 65** | `verifica_emendamenti.py` | 18:05 |
| **Collaudi** | **13 su 13** — il tredicesimo è `collaudo_data_derivata.py`, nato da questo gate | `_collaudo\` | 18:09 |
| **QA, perimetro vault** | **106 ERRORI, 444 avvisi** | `qa_all.py` | 18:09 |
| di cui grezzi non ancora canonizzati | **104** | | |
| di cui aree senza hub | **2** — `ricerca-sviluppo`, `sicurezza-ambiente` | | |
| di cui **rilievi di merito** | **0** | | |
| errori per controllo | copertura **106** · frontmatter **0** · provenance **0** · link **0** | | 18:09 |
| **Matrice** | completa e disgiunta — **160 grezzi, 33 elenchi**, guasti 0 | `verifica_matrice_lotti.py` | 18:10 |
| **lotti chiusi** | **13** — 12 di canonizzazione + 1 di manutenzione, pilota escluso | `verifica_matrice_lotti.py` | 18:10 |
| **Tracciamento** | **186 righe**, da T1 a T186, integra | `conta_tracciamento.py` | 18:10 |
| **Copie di stato** | ogni copia concorda col suo padrone | `verifica_copie_stato.py` | 18:10 |
| **Vault** | **507 note** · **56/160** grezzi citati | `conta_stato.py` | 18:10 |

⚠️ **La QA a perimetro vault porta l'ora del GATE e non quella del lotto**, al contrario di
quanto fatto al gate di 3E: **questo gate ha toccato il vault**, perché la data del 26/05 è
rientrata in una nota. **La misura che ha diritto di essere dichiarata è quella successiva
all'ultima scrittura** (E44).

---

## 8. Che cosa questo gate lascia aperto

| | |
|---|---|
| **il criterio pre-registrato sulla voce 4** | §6 del passaggio di consegne: due lotti futuri, e la metà delle scoperte |
| **la vigilanza su E65** | §6: se `R2` — che è di manutenzione e **riscrive note già giudicate** — ne produce ancora. **Un lotto che corregge è il terreno naturale della specie**, perché chi qualifica una frase tende ad allargarne il soggetto |
| **T184** | l'obbligo esplicito per il **lotto 07**: alla canonizzazione di `comunicazione_chiusura_estiva_2026.txt` la divergenza si apre come questione, con la gamba del verbale già canonizzata da 3F |
| **i tre censimenti** | **T142**, **T158**, **T169**: `R2` ripara le occorrenze che cadono nel suo perimetro e **dichiara il conto** — «censite nel perimetro: N, riparate: M» |
| **il prossimo atto** | **`R2`**, e **dopo R2 il ripacchettamento del tema 4** (E31), al suo gate e non prima |
