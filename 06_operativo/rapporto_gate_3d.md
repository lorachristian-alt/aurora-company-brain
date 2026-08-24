# Rapporto del gate del lotto 3D — E62-E63, le quattro estensioni, il controllo delle assenze

> **Che cos'è** · L'esito del gate del lotto 3D, eseguito il 24/08/2026 su
> `06_operativo\prompt\prompt_gate_3d_lotto_3e.txt`. Contiene ciò che il prompt del gate
> chiede: l'esito dell'adempimento una tantum di **E62** sugli obblighi del canone, il fix del
> controllo di **E43** col suo collaudo, e la **raccolta dei consuntivi** per la revisione
> della capacità.
> **Chi lo legge** · Il coordinatore. Le regole che ne nascono vivono in `metodo_03`, non qui.
> **Misure** · tutte da script, ognuna con la sua ora (E44), prese fra le **13:27 e le 13:30**
> del 24/08/2026.

---

## 1. Le decisioni del gate, in una tabella

| Punto del §9 di `rapporto_lotto_03d.md` | Decisione | Dove vive adesso |
|---|---|---|
| **1.** la metà B di E59 si può fare a lotto chiuso | ✅ **E59 si ESTENDE**: due prove che non si sommano, B dichiarata inapplicabile e **eseguita a chiusura** | `metodo_03` §9.5 passo 5-ter · registro |
| **2.** la correzione che aggiunge una fonte muove il perimetro | ✅ **E61 si ESTENDE all'indietro**, con l'appiglio del blocco `Fonti` | `metodo_03` §9.5 passo 5 · registro |
| **3.** lo slug è una superficie che nessun controllo guarda | ✅ **E30 si ESTENDE**: lo slug è la terza intestazione. ⚠️ **Nessun controllo di QA sullo slug**, e il perché è scritto | `metodo_03` §9.5 passo 2-bis · registro |
| **4.** E39 va cercata anche FRA le note | ✅ **E39 si ESTENDE**: il perimetro della ricerca è il vault, con lo strumento | `metodo_03` §9.5 passo 2-bis · registro |
| **5.** un obbligo del canone lo vede solo chi ha il canone | ✅ **E62, nuovo** — più il censimento una tantum: §2 di questo rapporto | `metodo_03` §9.5 passo 3 · **T168** |
| **6.** il contrario della sovra-atomizzazione, due lotti di fila | ✅ **E63, nuovo** — la copertura si verifica anche al contrario | `metodo_03` §9.5 passo 2-bis · registro |
| **7.** il debito resta dov'è, R2 dopo 3E | ✅ **ratificato**: T159-T160, T162-T167 restano; R2 in coda **dopo** 3E | matrice, tabella di tracciamento |
| **8.** `PRO-QA-11`, metà non scrivibile | ✅ **ratificato**: la metà con entrambe le gambe è **T163**, l'altra aspetta 3E. Nessun anticipo (divieto 9-bis) | **T163**, **T159** |
| *fuori tabella* — la quinta E3 | ✅ **il controllo di E43 acquista il riconoscitore della classe `assenza`**: §4 | `qa_frontmatter` · `metodo_03` §7.3 e §10 · **T169** |
| *fuori tabella* — i due collaudi-fotocopia | ✅ **debito dichiarato**, non riparato oggi | **T170** |
| *fuori tabella* — la revisione della capacità | ✅ **dovuta**: dieci lotti di canonizzazione chiusi. **Consuntivi raccolti al §6**, decisione al gate di 3E | §6 di questo rapporto |

**`verifica_emendamenti.py` è verde e concorde a 63**, misura delle **13:29:41**.

---

## 2. ⚠️ L'ADEMPIMENTO UNA TANTUM DI E62 — ho scorso il canone, e ne manca UNO

E62 dice che un obbligo scritto nel canone verso un lotto futuro **si specchia in tabella nello
stesso turno**. L'adempimento una tantum chiede di guardare all'indietro: **ogni obbligo ancora
aperto ha la sua riga T?**

**Perimetro: tutte le sezioni datate di `canone_aurora.md`**, cercando le formule con cui il
canone assegna un compito a un lotto che non ha ancora aperto — «obbligo esplicito per…», «alla
canonizzazione di…», «il lotto che porta…», «che dovrà tornare su…», e i 🚫 di non scrivibilità
che rimandano a un lotto nominato.

### 2.1 L'esito, riga per riga

| Riga del canone | L'obbligo, verso chi | Riga T | Esito |
|---|---|---|---|
| «Esito dei lavaggi CIP» *(20/08)* | lotto **2B**: applicare il criterio ai 28 cicli | **T72** | ✅ e **già chiusa** il 20/08 |
| **D4** *(22/08)* | lotto **3D**: aggiungere la quinta gamba alla nota | ⛔ **nessuna** | ⚠️ **è il caso che ha generato E62** — eseguito dal passo 3 di 3D, alla fine del ciclo. **Obbligo esaurito**: non prende una riga oggi |
| **D5** | lotto **6**, amministrazione | **T133** | ✅ |
| **D6** | lotto **6**, che dovrà tornare su T123 | **T134** | ✅ |
| **D7** | lotto **6**, la seconda partita IVA | **T135** | ✅ |
| **D8** | lotto **5**, l'accordo quadro Tosano | **T136** | ✅ |
| **E5** *(23/08)* | rimanda a **E9** per la quarta gamba | **T150** | ✅ |
| **E6** · **E7** | entrambe le gambe già canonizzate | **T152** · **T151** | ✅ |
| **E8** | **il lotto che canonizza la formazione sicurezza** | ⛔ **NESSUNA** | ❌ **LA APRE ADESSO: T168** |
| **E9** | il suo lotto: tornare su tre note, T102 e T145 | **T149** | ✅ |
| **E10** · **E11** | lotto **8** e il lotto delle timbrature | **T156** | ✅ |
| **E13** | lotto **6**, i quasi-omografi | **T39** | ⚠️ ✅ **ma il conteggio era fermo**: v. §2.3 |
| **F1** | il lotto che porta la procedura di ritiro | **T163** | ✅ |
| **F8** | il lotto che porta la procedura di ritiro | **T159** | ✅ |
| **C16** *(22/08)* | il lotto del rilievo d'audit | **T116** | ✅ e **chiusa** |
| **B6** di 2B-bis *(21/08)* | il lotto del registro | **T102** | ✅ e **chiusa** |

**Sedici obblighi guardati, quindici coperti, uno scoperto.**

### 2.2 ⛔ L'UNICO SCOPERTO: la terza gamba dell'organico — **T168**

Il canone, alla riga **E8** del 23/08, scrive che
`verbale_formazione_sicurezza_lavoratori_accordo_stato_regioni.txt` porta **22 convocati**, di
cui **17 nomi che il registro della formazione non contiene**, e che il corpus arriva a nominare
almeno **69 persone** — contro le **50** della politica e del verbale, e le **52** righe del
registro. Chiude con **«Obbligo esplicito per il lotto che canonizza la formazione sicurezza»**.

⚠️ **Nessuna riga della tabella lo diceva, e T144 non lo copre.** T144 tiene il 50 contro 52
misurato **sui due grezzi di 3B** e si chiude con «serve un documento di organico con una data»:
**non conosce la terza gamba**, che il divieto 9-bis teneva fuori da quel lotto. Un lotto futuro
che aprisse leggendo la tabella — cioè come si apre un lotto — **non troverebbe l'obbligo**.

⚠️ **È esattamente la specie di D4, e a distanza di un giorno**: l'obbligo scritto nel canone e
in nessun indice. **Quindici su sedici erano già a posto**, e questo è il dato che rende E62 una
regola e non un allarme: il difetto non è sistematico, è **intermittente** — e un difetto
intermittente è quello che la diligenza non prende, perché quattordici volte su quindici la
diligenza ha funzionato.

### 2.3 ⚠️ E una riga T che era vera e non lo è più: **T39**

T39 porta l'obbligo per il lotto 6 sui quasi-omografi Peruffo/Peruzzi e dice «la riga *Da non
confondere con* va scritta su **tutte e tre**». ⚠️ **Nel vault sono quattro dal lotto 3B**, che
ha portato Peruzzi Erika (canone, **E13**) — e **nel corpus sono sei**: `PERUZZI Loris` e
`Peruzzi Luciano` stanno in due grezzi non canonizzati.

**Riga aggiornata** col conteggio nuovo e con l'obbligo di classe B per chi porterà i due grezzi.
⚠️ **Non è un obbligo mancante ma un indice invecchiato**, ed è la seconda malattia della stessa
famiglia: E62 impedisce che un obbligo nasca senza riga, **non** che una riga resti indietro
quando il canone cresce. **La cura è la stessa di §4.47 — la copia si confronta col padrone — e
qui il confronto l'ha fatto questo censimento, non uno script.** Chi vorrà meccanizzarlo dovrà
partire da qui.

---

## 3. LE DUE REGOLE NUOVE E LE QUATTRO ESTENSIONI, dove sono andate

| | Dove vive | Marcatore |
|---|---|---|
| **E62** — l'obbligo del canone si specchia in tabella | `metodo_03` §9.5, passo 3, accanto a E49 | sì |
| **E63** — la copertura si verifica anche al contrario | `metodo_03` §9.5, passo 2-bis | sì |
| **E30 esteso** — lo slug è la terza intestazione | dentro il testo di E30, §9.5 passo 2-bis, datato | — |
| **E39 esteso** — la ricerca corre fra le note | dentro il testo di E39, §9.5 passo 2-bis, datato | — |
| **E59 esteso** — la metà B a lotto chiuso | dentro il testo di E59, §9.5 passo 5-ter, datato | — |
| **E61 esteso** — la rilettura all'indietro | dentro il testo di E61, §9.5 passo 5, datato | — |

**Le quattro estensioni non prendono un numero nuovo**: entrano **dentro** il testo del loro
emendamento, datate con l'occasione, e la riga di registro di ciascuno prende **la coda
dell'estensione**. È la disciplina di E42 rispetto a E39 — un chiarimento non fonda una regola.

⚠️ **Una nota sulla forma di E30, perché è una decisione e non una dimenticanza: NON si
costruisce un controllo di QA sullo slug.** Un nome compresso non ha grammatica, e un controllo
che leggesse gli slug come affermazioni **fabbricherebbe un rilievo su ogni nota corretta**. La
rete è già doppia: il gesto alla correzione, e il **giudice**, che lo slug lo vede per primo
perché è la prima cosa che il pacchetto gli mette davanti. **È il rovescio della decisione del
gate 3B sull'intestazione**, e i due casi insieme dicono la regola: si costruisce il controllo
dove c'è una grammatica da controllare, non dove c'è una superficie.

---

## 4. ⛔ IL CONTROLLO DI E43 GUARDA LA SUPERFICIE, E HA TROVATO QUATTRO CASI IN FLAGRANZA

### 4.1 Che cosa è cambiato: l'aggancio, non il requisito

Il controllo cercava **la formula** di attestazione di E3 e da lì risaliva all'artefatto. ⚠️ **Un
assenza scritta in prosa non la vedeva nessuno** — ed è T161, la quinta E3: la mail di notifica
dichiarata mancante dentro un elenco di «cosa servirebbe per chiuderla», mentre stava in
`sources\` dall'inizio.

Adesso l'assenza si riconosce per **due vie che non si sostituiscono**: la formula, e il
**riconoscitore della classe `assenza`**. Il requisito resta quello di E43 — l'artefatto della
ricerca — ed è un fix che **AGGIUNGE agganci** (§4.9).

⚠️ **E LA GRAMMATICA È UNA SOLA.** Il riconoscitore stava in `censimento_superlativi.py`, che con
esso conta la classe per T142. **È stato spostato in `qa_comune`**, dove ora lo leggono
entrambi: due copie della stessa grammatica divergono in un mese, e il giorno in cui
divergessero **il progetto conterebbe una classe e ne fermerebbe un'altra**. È lo stesso riuso
deliberato che 3D ha fatto con `qa_provenance.estrai_affermazioni`, e la stessa disciplina con
cui `qa_comune` tiene la definizione di nota-strumento.

⚠️ **Lo spostamento è stato TAGLIA-E-INCOLLA, e la prova è una misura, non una dichiarazione**:
il censimento è stato eseguito **prima e dopo** sullo stesso vault, con `--frasi`, e le due
uscite sono **identiche riga per riga** salvo l'ora. Non è un dettaglio: uno spostamento che
riscrive è una riscrittura, e le riscritture cambiano i numeri in silenzio.

### 4.2 ⛔ QUATTRO CASI IN FLAGRANZA, SULLE NOTE DEL LOTTO CHIUSO IERI — e due erano FALSI

Il controllo, al primo lancio, ha dato **quattro ERRORI**: quattro note **nate il 24/08**, cioè
sotto la regola nuova. Nessuna era un falso positivo.

| Nota | L'affermazione | La ricerca su tutto `sources\` |
|---|---|---|
| `questione-riesame-trimestrale-haccp` | «**Nessun documento dell'archivio** conosce una cadenza trimestrale» | ⛔ **FALSA**: `trimestral` è in **22 grezzi**, e uno è `PRO-QA-08` — **un grezzo dello stesso lotto**, che usa «trimestrale» per due indicatori dei reclami |
| `fatto-quattro-clienti-gdo-nominati-dalla-procedura` | «un elenco che **nessun altro documento dell'archivio** compila» | ⛔ **FALSA**: «Rossetto Trade» e «Famila Nordest» stanno in **altri sedici grezzi**, e uno di essi è `lista_contatti_buyer_GDO_nordest.csv` |
| `questione-due-codici-per-la-procedura-di-ritiro` | «**nessun documento dell'archivio** le mette in relazione» | ✅ **VERA**: `PRO-QA-11` in un file, `PRO-QA-14` in cinque, **nessuno porta entrambe** |
| `fatto-nessuno-risponde-a-voce-al-consumatore` | «**nessun altro documento del corpus** riporta un episodio di risposta impropria» | ⚠️ **non provabile**: è un'affermazione su un *tipo di evento*, non su un termine — nessuna ricerca la attesta |

⚠️ **DUE AFFERMAZIONI SU QUATTRO ERANO FALSE, ed è E3 pagato per la SESTA e la SETTIMA volta** —
lo stesso giorno, sullo stesso lotto, e da un controllo nato per prendere la quinta. ⚠️ **Il caso
peggiore è il primo**, perché il documento che smentisce l'assenza **è un grezzo di quel lotto**:
chi ha scritto la nota aveva la fonte aperta.

⚠️ **E la classe non è nuova: è E57 al negativo.** Il censimento dei superlativi le aveva già
separate — `superlativo` affermativo, che nessuna procedura verifica, e `assenza` esistenziale
negativa, «che è verificabile, e la sua verifica ha già una procedura». **La procedura c'era, il
controllo che la esigeva no**, perché guardava la formula. Le due classi non si sommano, e la
seconda era scoperta.

### 4.3 Le quattro correzioni, e perché non riaprono il ciclo

| Nota | Correzione | Specie |
|---|---|---|
| `questione-riesame-trimestrale-haccp` | ristretta alle proprie fonti, **due** affermazioni (anche il «che l'archivio non contiene» dell'elenco di chiusura), col rimando all'artefatto che mostra perché la larga non regge | **soppressiva** |
| `fatto-quattro-clienti-gdo-nominati-dalla-procedura` | l'affermazione falsa tolta e sostituita con ciò che il §8.1 sorregge, col rimando all'artefatto | **soppressiva** |
| `fatto-nessuno-risponde-a-voce-al-consumatore` | ristretta all'annotazione, che è la sola fonte della nota | **soppressiva** |
| `questione-due-codici-per-la-procedura-di-ritiro` | **attestazione** dell'assenza col rimando all'artefatto: l'affermazione resta, adesso è provata | **additiva della sola prova** |

⚠️ **Tre sono soppressive e si applicano senza riaprire il ciclo** (criterio 1B del lotto 1B,
ripreso da E58). ⚠️ **La quarta non aggiunge un'affermazione su Aurora**: aggiunge la prova di
una che c'era già, e il perimetro delle fonti **non si muove** — quindi non scatta nemmeno E61
esteso, che si aggancia al blocco `Fonti`. ⚠️ **E il divieto 9-bis è stato rispettato**: uno dei
grezzi che porta `PRO-QA-14` è del lotto **3E**, e nella nota **non si scrive nulla del suo
contenuto** — l'artefatto vive in `06_operativo\`, che non è il vault.

⚠️ **Tre artefatti nuovi in `06_operativo\ricerche_assenza\`**, tutti col perimetro dichiarato e
i termini scartati col loro perché.

### 4.4 Il collaudo: dieci casi, nei due versi, e il non-scatto

`qa\_collaudo\collaudo_assenza_fuori_formula.py` **chiama la via di produzione**, non una copia
della sua logica (§4.29).

| # | Caso | Atteso | Avuto |
|---|---|---|---|
| 1 | **il difetto piantato**: assenza in prosa, nota nata sotto la regola, nessun artefatto | ERRORE | ✅ |
| 2 | la stessa, su nota **anteriore** al 24/08 | AVVISO col debito (§4.35) | ✅ |
| 3 | assenza fuori formula **con artefatto che esiste** | tace | ✅ |
| 4 | assenza fuori formula con artefatto che **non esiste** | ERRORE | ✅ |
| 5 | **la formula** senza artefatto — l'aggancio vecchio non si è rotto | ERRORE | ✅ |
| 6 | **superlativo affermativo**: è la classe di E57, non questa | tace | ✅ |
| 7 | perimetro **ristretto per iscritto** | tace | ✅ |
| 8 | omonimia: l'**archivio cartaceo** di Aurora | tace | ✅ |
| 9 | **nota-strumento** del progetto (E20) | tace | ✅ |
| 10 | nota pulita | tace | ✅ |

⚠️ **Cinque casi su dieci provano il NON-SCATTO**, ed è la metà che decide se un controllo
sopravvive: un controllo che fa rumore viene disattivato, e §4.35 lo dice già.

⚠️ **Il caso 9 è una decisione, non una deroga.** Le note-strumento sono esenti (E20): «la
promessa del vault è che nessuna nota sia irraggiungibile» **non è un'assenza dichiarata sul
corpus**. È lo stesso perimetro che il censimento esclude, e per la stessa ragione — se il
perimetro fosse diverso, il numero contato e il numero fermato non sarebbero lo stesso numero.

### 4.5 Il pregresso, contato: **25 note** — **T169**

⚠️ **ERRORE dalle note nate dal 24/08/2026, AVVISO dichiarato per le altre** (§4.35, come per
E43 il 20/08 e per la superficie dell'intestazione il 23/08). Gli avvisi del vault salgono da
**344 a 369**: **+25**, ed è esattamente il debito.

⚠️ **Il numero è un LIMITE INFERIORE**: lo strumento riconosce una forma, il soggetto lo decide
chi legge — la stessa riserva di T142, con la stessa grammatica. Le 25 si riparano **nel lotto
che le tocca o nella rete finale**, non aprendo un giro sul vault (T142, e il calcolo lineare di
1C).

---

## 5. IL DEBITO DICHIARATO E NON RIPARATO: i due collaudi-fotocopia — **T170**

`collaudo_related_rotto.py` e una parte di `collaudo_suite.py` **reimplementano il controllo che
provano** invece di chiamarlo: è §4.29 al contrario, e §4.29 nasce da un caso pagato — il
pacchetto del giudizio tagliato in fette da una via equivalente e mai esercitata, coi giudici
che confrontavano le note con sé stesse.

⚠️ **Un collaudo che rifà la logica prova la propria copia, non il controllo**: il giorno in cui
la produzione cambia, il collaudo resta verde su codice che nessuno esegue più. **Si riporta alla
chiamata della via di produzione alla prossima occasione che tocca la suite**, non oggi.

⚠️ **La famiglia si sta sanando dal lato nuovo**: `collaudo_intestazione.py` (23/08) e
`collaudo_assenza_fuori_formula.py` (oggi) chiamano già la via di produzione. **Un debito
dichiarato non è un debito dimenticato.**

---

## 6. LA REVISIONE DELLA CAPACITÀ È DOVUTA — i consuntivi, raccolti

**Dieci lotti di canonizzazione chiusi**, letti dai marcatori con `verifica_matrice_lotti.py`,
misura delle **13:29:47**. I lotti di manutenzione non entrano (E38): misurano riparazioni, non
produzione. La §2 del prompt dei lotti fissa la revisione **a dieci lotti chiusi**: la soglia è
raggiunta.

### 6.1 La serie, incollata dai rapporti di lotto

| Lotto | Grezzi | Note di contenuto **nate** | Giri di giudizio | Rilievi, per giro | Fonte |
|---|---|---|---|---|---|
| **1A** | 7 | **42** | 2 | 8 · 8 | `rapporto_lotto_1a.md` |
| **1B** | 4 | **38** | **4** | 5 · 4 · 4 · 1 | `rapporto_lotto_1b.md` |
| **1C** | 2 | **27** | 3 | 12 · 8 · 7 *(27 su 27 accolti)* | `rapporto_lotto_1c.md` |
| **2A** | 3 | **30** | 3 | 12 · 7 · 9 | `rapporto_lotto_02a.md` |
| **2B** | 3 | **27** | 3 | 8 · 2 · 3 | `rapporto_lotto_02b.md` |
| **2B-bis** | 2 | **33** | 3 | 11 · 7 · 5 | `rapporto_lotto_02b_bis.md` |
| **3A** | 2 | **42** — 38 ciclo + 4 revisione | 3 | 26 · 9 · 5 *(errori; i rilievi grezzi erano 68 · 22 · 16)* | `rapporto_lotto_03a.md` |
| **3C** | 4 | **38** — 37 di contenuto + 1 di diario | 3 | 7 · 2 · 5 *(note `afferma_oltre`)* | `rapporto_lotto_03c.md` |
| **3B** | 2 | **22** | 3 | 18 · 10 · 12 *(note `afferma_oltre`)* | `rapporto_lotto_03b.md` |
| **3D** | 3 | **45** — 35 ciclo + 10 revisione | 2 + **2 dedicati** | 17 · 5, poi 7 · 1 | `rapporto_lotto_03d.md` |

### 6.2 ⚠️ QUATTRO NUMERI CHE IL COORDINATORE DEVE AVERE DAVANTI, E UNA RISERVA

1. **La capacità 25-35 è stata rispettata QUATTRO volte su dieci**: 1C (27), 2A (30), 2B (27),
   2B-bis (33). **Cinque volte è stata superata** — 1A (42), 1B (38), 3A (42), 3C (38), 3D (45)
   — e **una volta mancata** dal basso, 3B (22).
2. **Il tetto dei 40 di E28 è stato superato tre volte**: 1A, 3A, 3D. In **due** di quei tre lo
   sforamento viene dalle **note nate dalla revisione**, che E52 tiene fuori dalla soglia: 3A
   scrive 38 nel ciclo, 3D ne scrive **35** — cioè **esattamente il bordo alto della fascia**.
   **Contando il solo ciclo, i lotti dentro la fascia diventano sei su dieci.**
3. **I giri di giudizio sono TRE in otto lotti su dieci**, e la ragione è la regola d'arresto di
   E26, non il caso: quattro in 1B (prima che E26 esistesse), due in 1A e in 3D. **Il ciclo non
   si chiude quasi mai per esaurimento**, si chiude al terzo giro col pattern nominato.
4. **La colonna dei rilievi NON è omogenea, e va detto prima che qualcuno la sommi**: 1A, 1B,
   1C, 2A, 2B e 2B-bis contano **rilievi accolti**; 3A conta **errori** su una colonna di rilievi
   grezzi tre volte più grande; 3B e 3C contano **note** tornate `afferma_oltre`, che è un'altra
   grandezza ancora. **Le tre serie non si sommano** — è la lezione del censimento che mescolava
   due regimi, e di E46: un numero dice su che cosa è misurato.

⚠️ **LA RISERVA CHE PESA PIÙ DI TUTTE, e per cui la decisione non si prende qui.** La densità
`note/grezzo` va da **7,0** a **25,5** *(dal consuntivo di `ricalibra_budget.py`)*: **ciò che si
mantiene costante è il LOTTO, non la densità**, ed è la ragione per cui E31 sostituì le fasce
con la capacità. Una capacità rivista sui consuntivi rischia di ripetere l'errore delle fasce
**se si tocca la grandezza sbagliata**: la domanda vera non è «25-35 è il numero giusto?» ma
**«che cosa consuma il rischio, le note o i giri?»** — e i tre giri quasi costanti dicono che
potrebbe essere la seconda.

**Decisione al gate di 3E, coi numeri davanti** — come il prompt di questo gate ordina.

---

## 7. I NUMERI DI CHIUSURA (E44), tutti da script e con l'ora

**Misure fra le 13:27 e le 13:30 del 24/08/2026.** ⚠️ **Questo gate ha toccato quattro note del
vault**, e non era previsto: sono le quattro prese in flagranza dal controllo nuovo (§4.2), tutte
del lotto 3D e tutte corrette nello stesso turno.

| Misura | Valore | Strumento | Ora |
|---|---|---|---|
| **QA, perimetro vault** | **108 ERRORI, 369 AVVISI** — esito **ROSSO** | `qa_all.py` | 13:27 |
| di cui grezzi non ancora canonizzati | **106** | | |
| di cui aree senza hub | **2** — `ricerca-sviluppo`, `sicurezza-ambiente` | | |
| di cui **rilievi di merito** | **0** | | |
| ⚠️ avvisi: **344 → 369** | **+25**, il pregresso delle assenze fuori formula (T169) | | |
| errori per controllo | copertura **108** · frontmatter **0** · provenance **0** · link **0** | | 13:27 |
| **Collaudi** | **11 su 11** — il nuovo è `collaudo_assenza_fuori_formula` (10 casi) | `_collaudo\` | 13:29 |
| **Emendamenti** | registro e manuale **concordano a 63** | `verifica_emendamenti.py` | 13:29 |
| **Copie di stato** | **4 su 4** concordi col padrone | `verifica_copie_stato.py` | 13:29 |
| **Matrice** | completa e disgiunta — **160 grezzi, 30 elenchi**, guasti 0 | `verifica_matrice_lotti.py` | 13:29 |
| **lotti chiusi** | **11** — **10 di canonizzazione** + 1 di manutenzione, pilota escluso | `verifica_matrice_lotti.py` | 13:29 |
| **Tracciamento** | **170 righe**, da T1 a T170 — 7 riconciliate · 83 aperte dichiarate · 21 chiuse · 59 tracciate | `conta_tracciamento.py` | 13:30 |
| **Vault** | **432 note**, di cui **395 di contenuto** | `conta_stato.py` | 13:30 |
| **Grezzi canonizzati** | **54 su 160** — ne restano **106** | `conta_stato.py` | 13:30 |

⚠️ **Nessuna copia di stato nuova introdotta dal fix**: la data di nascita della regola
(`NASCITA_ASSENZA_FUORI_FORMULA`) non è stato ricavabile da una fonte — è un fatto sulla regola,
come `NASCITA_E43` — e il censimento di `verifica_copie_stato.py` resta a quattro voci. **La
riga del prompt dei lotti chiede di dichiararlo, ed è dichiarato.**

---

## 8. Che cosa questo gate lascia aperto

| | |
|---|---|
| **1. Un indice può invecchiare senza che nessuno se ne accorga** | E62 impedisce che un obbligo del canone nasca **senza** riga T; **non** impedisce che una riga T resti indietro quando il canone cresce. **T39 lo era**, e l'ha presa un censimento a mano. ⚠️ **Chi vorrà meccanizzarlo parte da qui**: il confronto è fra due prose, e §4.47 dice già che una copia non controllata mente in silenzio |
| **2. Le 25 assenze del pregresso** | **T169**, aperta dichiarata. Entrano nella rete finale o nel lotto che tocca ciascuna nota, come le 14 di T158 e le 9 di T142. ⚠️ **Il debito dichiarato del vault sale a tre righe di censimento**, ed è la prima volta: sono tre superfici scoperte in tre giorni |
| **3. I due collaudi-fotocopia** | **T170**, tracciata. Alla prossima occasione che tocca la suite |
| **4. La revisione della capacità** | I consuntivi sono al §6. ⚠️ **La domanda che porto al gate di 3E non è quella che il prompt poneva**: non «25-35 regge?» ma **«la grandezza giusta sono le note o i giri?»** |
| **5. L'obbligo esplicito di T168** | Il lotto della formazione sicurezza deve tornare su T144 e sulla questione dei cinquanta |
| **6. Il debito verso 3E** | **T159** e la metà di **T163**, più le altre righe che la tabella assegna al pacchetto: confermate tutte dal gate |
