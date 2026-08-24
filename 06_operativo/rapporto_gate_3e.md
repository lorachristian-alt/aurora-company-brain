# Rapporto del gate del lotto 3E — E64, le quattro estensioni, la capacità confermata

> **Che cos'è** · L'esito del gate del lotto 3E, eseguito il 24/08/2026 su
> `06_operativo\prompt\prompt_gate_3e_lotto_3f.txt`. Contiene ciò che il prompt del gate chiede:
> le decisioni sugli **otto punti** del §9 di `rapporto_lotto_03e.md`, la **decisione sulla
> capacità** coi consuntivi del §6 di `rapporto_gate_3d.md` davanti, e la **riconciliazione del
> 425**.
> **Chi lo legge** · Il coordinatore. Le regole che ne nascono vivono in `metodo_03`, non qui.
> **Misure** · tutte da script, ognuna con la sua ora (E44), prese fra le **21:27 e le 21:29**
> del 24/08/2026. ⚠️ **Una porta un'ora diversa e il perché è dichiarato al §7**: la QA a
> perimetro vault resta quella delle **15:17**, perché **il gate non ha toccato nessuna nota**.

---

## 0. La verifica d'apertura, e il commit

`prompt_s4_lotti.txt`, aggiornato dal coordinatore da E63 a E64 più le quattro estensioni e la
capacità rivista, **torna su tutti e sei i controlli**:

| Controllo | Atteso | Misurato |
|---|---|---|
| righe | 793 | **793** |
| byte | 48.384 | **48.384** |
| CRLF | 793 | **793** |
| LF isolati | 0 | **0** |
| BOM | assente | **assente** |
| sha256 | `05fbc8ae…3843770` | **`05fbc8aef51804cbbfd5e4fa39bcb21e68b3e32665bee5d18b3f476b13843770`** |

I due file sono stati committati e pushati **prima** di eseguire, commit `02e7145`, messaggio
«prompt dei lotti a E64 e prompt del gate 3E + lotto 3F».

---

## 1. Le decisioni del gate, in una tabella

| Punto del §9 di `rapporto_lotto_03e.md` | Decisione | Dove vive adesso |
|---|---|---|
| **1.** il tema 3 non chiude con 3E | ✅ **RATIFICATO**: `3F` chiude il tema, la matrice lo registra — **33 elenchi**. Più il **corollario della pianificazione**: §4.50 | matrice, registro delle modifiche · passaggio §4.50 |
| **2.** la metà B di E59 ha respinto al primo impiego | ✅ **NESSUNA REGOLA NUOVA** — è l'estensione di ieri che lavora. **UN RECEPIMENTO**: `\bPRO-QA-11\b` **non rientra** nella rigenerazione del dominio `ritiro` di R2 senza una prova nuova | testa di `qa\lotti\r2_reclami_verticale.txt` · matrice, sezione R2 |
| **3.** il tasso di 3E è degenere | ✅ **E41 SI ESTENDE**: il punto degenere **entra nella serie con la dicitura**. ⚠️ **E non si inventa un dominio artificiale** per ottenere un numero utile | `metodo_03` §9.5 passo 5-ter · registro |
| **4.** la frase di raccordo che asserisce | ✅ **E64, NUOVO**: il rimando nomina, non asserisce | `metodo_03` §4.2 (+ §9.5 passo 2-bis) · registro |
| **5.** le glosse degli hub restano indietro | ✅ **E39 SI ESTENDE** (seconda volta): gli hub sono superfici della ricerca | `metodo_03` §9.5 passo 2-bis · registro |
| **6.** E61 tre correzioni su tre giri | ✅ **E61 SI ESTENDE** (seconda volta): la frase nuova porta il suo riscontro **nel turno** | `metodo_03` §9.5 passo 5 · registro |
| **7.** il debito che resta | ✅ **RATIFICATO dov'è**: T171-T175 aperte dichiarate, R2 a due domini in coda **dopo 3F** | matrice, tabella di tracciamento |
| **8.** cinque righe B dallo stesso accostamento | ✅ **E60 SI ESTENDE**: l'accostamento **per evento** | `metodo_03` §5.1-bis (+ §9.5 passo 2-bis) · registro |
| *fuori tabella* — la revisione della capacità | ✅ **ESEGUITA E CHIUSA**: la fascia **25-35 è confermata** come grandezza di progetto. §4 | `metodo_03` §9.4 · passaggio §6, riga datata |
| *fuori tabella* — il 425 | ⛔ **RICONCILIATO, e il 425 non è mai esistito**. §5 | passaggio §5 · decision log |
| *fuori tabella* — due puntatori a un file che non c'è | ✅ **REFUSI RIPARATI**, dichiarati. §6 | `metodo_03` §5.1-bis · matrice |

**`verifica_emendamenti.py` è verde e concorde a 64**, misura delle **21:27**.

---

## 2. La correzione di FORMA al coordinatore, e non è la settima

Il prompt del gate di 3D scriveva «la chiusura di 3E è la chiusura del tema 3», e la conta dei
fatti in apertura l'ha smentito: **62 fatti**, spezzamento, il tema chiude con `3F`.

⚠️ **NON conta come settima correzione, e la distinzione è sostanziale.** Le sei correzioni
contate finora riguardano affermazioni che, **nel momento in cui furono scritte, erano
verificabili e sbagliate**. Qui il conto di E21 non esisteva ancora: **non c'era nulla di
verificabile da verificare**, e la frase era una previsione ragionevole.

⚠️ **Ma la FORMA era sbagliata, ed è la forma che si corregge.** Il corollario alla regola del
coordinatore, ora in **§4.50** del passaggio di consegne:

> **Una pianificazione scritta in un prompt porta il condizionale della misura** — « ultimo
> pacchetto, **salvo il conto di E21** » — perché **un'apertura può sempre smentire un piano, ed
> è fatta apposta per poterlo fare.**

⚠️ **È E53 applicato a una pianificazione invece che a un dominio**: là «nessun dominio» non si
accetta sulla parola di chi coordina e si verifica da script; qui «questo è l'ultimo lotto» non
si accetta sulla parola e si verifica contando i fatti. ⚠️ **E vale nei due sensi**: chi opera
**non compensa a mano** un piano smentito — lo dichiara, spezza, e scrive nel registro della
matrice che cosa è cambiato e perché. Il lotto 3E l'ha fatto, ed è la ragione per cui la
smentita è costata **una riga di registro e non un lotto da rifare**.

---

## 3. E64 e le quattro estensioni, e dove sono andate

### 3.1 E64 — il rimando nomina, non asserisce · **§4.2**

Una frase di raccordo verso un'altra nota **non afferma nulla del contenuto di quella nota né
delle sue fonti**. « la questione ha le sue fonti e sta in `[[x]]` » regge; « `[[x]]` dice
che… » no.

⚠️ **La ragione è di perimetro, non di stile**: un'affermazione sul contenuto di un'altra nota è
verificabile **solo dalle fonti di quella nota**, cioè da nessuna fonte di questa — e il giudizio
guarda ogni nota contro **le sue** fonti. ⚠️ **La glossa dopo un wikilink è già una superficie di
provenienza** (§7.1, clausola 4): **il controllo c'era, mancava la regola di scrittura.**

⚠️ **Il test operativo è di scrittura e non di controllo**: togli dalla frase tutto ciò che segue
il nome della nota. Se quel che resta regge, era un rimando; **se togliendolo la frase perde
qualcosa, quel qualcosa è un'affermazione** — o ha le sue fonti in questa nota, e allora si
scrive come fatto con la fonte e il locator, oppure non si scrive.

⚠️ **Perché è stata scritta ORA e non dopo l'esperimento**, e non è §4.43. Il criterio
pre-registrato scritto dalla sessione di 3E la sera prima chiedeva la ricomparsa al terzo giro
del **prossimo** lotto. Ma **il terzo giro di 3E l'aveva già nominata da tre fette indipendenti**,
e la sessione ha scritto il criterio **dopo** averle avute davanti: **le osservazioni erano tre e
tutte anteriori al criterio**. È la via di **E50** ed **E51** — quando il terzo giro nomina una
specie con casi plurimi, il gate la scrive. **Aspettare un lotto significa lasciarla scrivere in
quel lotto**, e `3F` tesserà molto grafo verso il tema 3.

⚠️ **La seconda superficie della stessa famiglia — le glosse degli hub — NON è entrata in E64**,
ed è la collocazione giusta: **E64 riguarda che cosa una frase di rimando può dire; l'estensione
di E39 riguarda dove si va a cercare quando una correzione toglie qualcosa.** Sono due lacune
diverse che si toccano su una superficie sola, e metterle sotto lo stesso numero avrebbe reso il
numero inutilizzabile da entrambe le parti.

### 3.2 E41 esteso — il punto degenere si dichiara · **§9.5 passo 5-ter**

Un lotto **mono-fonte il cui unico grezzo È la fonte che governa il dominio** produce uno
`0,0 %` **strutturale**: ogni nota nata cita quella fonte **per costruzione**, e nessuna può
risultare scoperta.

| | |
|---|---|
| **il punto entra** | con la dicitura *«degenere: lotto mono-fonte sulla fonte del dominio»*. **Entra** perché la serie fotografa **le misure come sono state prese** — stessa disciplina per cui il 38,7 % di 3C resta con la sua riserva e il lotto non si rimisura |
| **porta la dicitura** | perché uno `0,0 %` nudo **si legge come un successo del metodo**, e sarebbe la lettura opposta al vero: lì il metodo non è stato messo alla prova. **È E46 portato alle conseguenze** — il numero deve dire anche *che cosa non poteva misurare* |
| **ciò che NON si fa** | **non si inventa un dominio artificiale per ottenere un numero «utile»**: sarebbe il trucco di E41 rovesciato. Là si aggiungeva una fonte per portare il tasso a zero, qui si allargherebbe il dominio per portarlo sopra zero — **la stessa mossa in due direzioni** |
| **e si riconosce in APERTURA** | il conto dei grezzi e la dichiarazione del dominio bastano a dirlo **prima di scrivere una riga**. Un punto degenere riconosciuto solo alla fine è un numero che per qualche ora ha detto una cosa falsa |

⚠️ **Vale SUBITO per `3F`**, che è mono-fonte come 3E: la dichiarazione degenere si scrive in
apertura, se il conto la conferma.

### 3.3 E39 esteso, seconda volta — gli hub sono superfici della ricerca · **§9.5 passo 2-bis**

Quando una correzione **toglie o qualifica** un'affermazione di uno spoke, le **glosse degli hub
che lo elencano** si rileggono **nello stesso turno**. ⚠️ **L'appiglio è il grafo e non chiede
giudizio: chi corregge una nota apre gli hub che la linkano** — i backlink li danno senza
cercarli.

⚠️ **Non è una superficie in più nell'elenco: è una superficie di un'ALTRA nota**, e qui sta la
ragione per cui né E39 base né la sua prima estensione la prendevano. Le superfici di E39 stanno
**dentro** la nota che si corregge; la ricerca del vault (3D) cerca le note **sorelle**, che
**ripetono** la stessa affermazione. **La glossa di un hub non ripete: riassume**, spesso in tre
parole e con parole diverse — **quindi la ricerca testuale non la trova. La trova il grafo.**

⚠️ **E non è un avviso, è un errore**: la clausola 4 di §7.1 classifica come **ERRORE sull'hub**
una glossa che dice ciò che lo spoke non dice. **La regola c'era dal lato del controllo; mancava
il gesto dal lato di chi scrive** — la stessa forma di E42, un turno invece che un perimetro.
**Tre glosse in 3E**, trovate **scavando sotto un falso allarme**.

### 3.4 E60 esteso — l'accostamento per evento · **§5.1-bis**

Se due fonti — **del lotto o già del vault** — registrano **lo stesso evento** (stessa data,
stesso oggetto: un lotto produttivo, un fermo, una consegna, un blocco), il passo pre-giudizio
**le legge una di fronte all'altra, riga per riga**, e il rapporto **dichiara l'accostamento**.

⚠️ **Le grandezze condivise NON bastano, e il caso lo dimostra al numero.** In 3E il blocco del
perimetro e il mass balance di `L26130` — **compilati lo stesso giorno dalla stessa funzione** —
**concordavano su tre numeri** e divergevano su **giacenza, attribuzione e perimetro
comunicato**. L'artefatto d'apertura elenca le grandezze che *coincidono*: **su quelle tre
l'accostamento sarebbe risultato una conferma.** Le cinque righe B sono uscite dalla
**ricostruzione**, non dalle grandezze.

⚠️ **L'appiglio è meccanico**: due fonti con la stessa data e lo stesso oggetto si accostano,
senza chiedersi prima se divergeranno. **Il criterio non è «sembrano in contrasto» — è «parlano
dello stesso fatto».** ⚠️ **Terzo lotto di fila in cui la E2 vera l'ha fatta il revisore** (3A,
3B, 3E): **il ciclo deve riprendersela, e questo è il gesto con cui se la riprende.**

### 3.5 E61 esteso, seconda volta — la frase nuova porta il suo riscontro nel turno · **§9.5 passo 5**

Ogni correzione dichiara **nel proprio turno** la coppia **frase nuova → riscontro**: fonte e
locator, nella grammatica di §2.3, **come una riga B porta il suo** (E49). ⚠️ **Chi non può
citare il riscontro NON corregge: apre un rilievo.**

⚠️ **Perché serviva un gesto e non un richiamo.** Il verso all'indietro, scritto ieri, ha il suo
appiglio meccanico — *se la correzione tocca il blocco `Fonti`, si rilegge la nota intera* — **ma
il verso in avanti non ne aveva nessuno**: diceva «rileggila contro le fonti», che è ciò che il
metodo chiede per ogni frase e che per la frase nuova non accadeva.

| Il consuntivo | |
|---|---|
| **3B** | sette dei dodici rilievi del terzo giro su frasi che al secondo non c'erano |
| **3D** | tre casi, due dentro una riconciliazione di E60 |
| **3E** | **tre correzioni su tre giri**, ognuna presa dal giro successivo |

⚠️ **Il criterio pre-registrato del gate di 3B si è avverato — tre su tre in 3E, dopo tre in 3D e
sette in 3B.** ⚠️ **La rete funziona, ma ogni maglia costa un giro**: un difetto introdotto al
primo giro e preso al secondo consuma un giro intero del budget che E26 concede, e ne concede
tre. ⚠️ **Il gesto è meccanico quanto può esserlo senza uno script**: la coppia dichiarata è
**verificabile da chi rilegge il turno** — non chiede fiducia, chiede una citazione — e questo la
distingue da «rileggere con più attenzione», che è la forma che il manuale rifiuta da E39 in poi.

---

## 4. ⚠️ LA DECISIONE SULLA CAPACITÀ — confermata, e la vigilanza si sposta

I consuntivi sono nel **§6 di `rapporto_gate_3d.md`**: dieci lotti di canonizzazione chiusi, con
`R1` fuori dalla serie (E38). **La soglia della revisione era raggiunta, e la revisione è
eseguita.**

### 4.1 La decisione

| | |
|---|---|
| **la fascia 25-35 è CONFERMATA** | come **grandezza di PROGETTO**: serve al **taglio dei pacchetti in apertura**, cioè a decidere quanti grezzi stanno in un lotto. **Non è una previsione, e non è la soglia che spezza** |
| **a spezzare restano i tetti duri di E28** | 30 con lo scostamento dichiarato, 40 sempre. ⚠️ **Hanno spezzato giusto due volte** — 2B e 3E — e in entrambe la conta d'apertura ha retto |
| **il consuntivo** | fascia rispettata **4 volte su 10**; superata 5, mancata dal basso 1. ⚠️ **Contando il solo ciclo** — togliendo le post-revisione, che E52 tiene già fuori dalla soglia — **i lotti dentro la fascia diventano SEI su dieci** |
| **ciò che NON si fa** | **sostituire la fascia con un'altra fascia** |

### 4.2 ⚠️ Perché NON si ricalibra, ed è il punto che decide

La densità `note/grezzo` dei dieci lotti va da **7,0 a 25,5**. **Ciò che si mantiene costante è
il LOTTO, non la densità** — ed è esattamente la ragione per cui **E31** sostituì le fasce con la
capacità, il 19/08.

⚠️ **Ricalibrare la fascia sui consuntivi ripeterebbe l'errore che E31 ha già corretto, spostato
di un piano.** Il calcolo lineare che diede 903 note e 36 lotti sbagliava perché moltiplicava una
grandezza instabile per una stabile; una fascia nuova costruita sulla dispersione dei dieci lotti
sbaglierebbe allo stesso modo — **prenderebbe per costante una grandezza che il progetto ha già
misurato come variabile.**

### 4.3 La domanda riformulata dal gate di 3D, e la sua risposta

> **«Che cosa consuma il rischio, le note o i giri?»**

**Non sono le note.** I giri di giudizio sono **TRE in SETTE lotti su dieci**, e non per caso:
**il ciclo quasi mai si chiude per esaurimento**, si chiude al terzo giro con il pattern nominato
(E26). **Le tre eccezioni sono 1A** (due giri), **1B** (quattro, prima che E26 esistesse) e
**3D** (due più due dedicati).

⚠️ **UN NUMERO DEL CONSUNTIVO CORRETTO QUI, ED È IL NUMERO SU CUI IL GATE DECIDE.** Il punto 3
del §6.2 di `rapporto_gate_3d.md` scrive **«tre in otto lotti su dieci»**, e **la sua stessa
tabella ne conta sette**: 1C, 2A, 2B, 2B-bis, 3A, 3C, 3B. ⚠️ **A smentirlo è la riga stessa**,
che elenca **tre** eccezioni — «quattro in 1B, due in 1A e in 3D» — e dieci meno tre fa sette.
⚠️ **Il rapporto di quel gate NON si riscrive**: è un verbale, e documenta ciò che quella
sessione ha fatto. **Il numero si corregge dove il progetto lo userà** — `metodo_03` §9.4, il
passaggio di consegne, lo stato, questo rapporto.

⚠️ **E la decisione non cambia**, che è la cosa da dire per prima: sette su dieci e otto su dieci
dicono la stessa cosa — **il ciclo si chiude al terzo giro perché la regola d'arresto lo ferma,
non perché i rilievi si esauriscano**. Il numero sarebbe stato decisivo solo nel verso opposto.

⚠️ **Quindi la vigilanza non si chiude: si SPOSTA**, e da qui in poi guarda due grandezze, nessuna
delle quali è il conteggio delle note del ciclo:

1. **LA DENSITÀ DI DIFETTO DEL GRUPPO POST-REVISIONE.** E52 lo dichiara già come gruppo con esiti
   separati, e il gate lo guarda già. È stato **più alto del ciclo in 3A, in 3D e in 3E** — tre
   lotti su tre in cui il confronto è stato fatto — e **un gruppo piccolo con un tasso molto più
   alto è un segnale che sommarlo al ciclo cancella**.
2. **LA COSTANZA DEI TRE GIRI.** Se un lotto mostrerà che **tre giri sistematicamente non
   bastano**, la domanda si riapre — **sui giri**, non sulle note.

### 4.4 Dove la decisione è scritta, e che cosa si è chiuso

| | |
|---|---|
| `metodo_03` **§9.4** | la riga «la fascia è provvisoria, da rivedere a dieci lotti chiusi» **è sostituita dalla revisione eseguita**, con la decisione, il consuntivo e le due vigilanze. **E38 è allineato**: non diceva più «quando si rivedrà», dice che nella revisione del 24/08 i lotti di manutenzione non ci sono entrati |
| `prompt_s4_lotti.txt` **§2** | già recepito dal coordinatore |
| passaggio di consegne **§6** | riga datata: revisione eseguita, esito, e la vigilanza spostata |
| `stato_canonizzazione.md` | esito nel cappello e nella sezione del gate |

⚠️ **E la lezione di metodo del punto 4 dei consuntivi resta scritta dov'è**, perché serve a chi
li rilegge: **le tre serie di rilievi non si sommano** — rilievi accolti (1A, 1B, 1C, 2A, 2B,
2B-bis), errori (3A), note tornate `afferma_oltre` (3B, 3C) sono **tre grandezze diverse**, e chi
legge quella colonna come una serie sola legge un numero che non esiste. **È E46 applicato a un
consuntivo.**

---

## 5. ⛔ IL 425 NON È MAI STATO MISURATO — il confronto riconciliato

Il §7 di `rapporto_lotto_03e.md` scrive: *«Il vault scende da 108 a 107 errori, e gli avvisi
salgono da 425 a 426.»* Il prompt del gate chiede di dichiarare **quando il 425 è stato preso** e
**di che cosa è fatto il passaggio**.

### 5.1 Il 425 non compare in nessuna misura del progetto

**Cercato ovunque**, con uno script, su tutti i `.md`, `.txt`, `.py`, `.csv` e `.json` del
perimetro consentito: report di QA su disco, versioni **committate** degli stessi report, stato,
passaggio di consegne, matrice, decision log, rapporti di lotto e di gate. ⚠️ **Le uniche
occorrenze del numero «425» anteriori a questo gate sono tre, e sono tutte le 425 formule del
libro unico** (T89, lotto 2B — decision log, matrice, `rapporto_lotto_02b.md`), più un `5.425
kWh` in tre pacchetti di giudizio del lotto 1B. **Nessuna è un conteggio di avvisi.**

**Le misure del vault del 24/08 sono TRE**, e si leggono dai `qa_all.md` versionati — cioè
dall'artefatto, non dalla memoria:

| Quando | Errori | Avvisi | Note nel vault | Commit da cui si legge |
|---|---|---|---|---|
| chiusura del lotto **3D** | 108 | **344** | 432 | `12a41aa` |
| **gate 3D**, 13:27 | 108 | **369** | 432 | `beb91f0` |
| chiusura del lotto **3E**, 15:17 | 107 | **426** | 470 | `babc743` |

⚠️ **L'ultima misura nota prima di 3E era dunque 369, non 425.**

### 5.2 Di che cosa è fatto il passaggio 369 → 426: **+57**

Contato riga per riga sui due report, per specie di avviso:

| Controllo | Da | A | Δ | Di che cosa è fatto |
|---|---|---|---|---|
| `qa_link_integrity` | 25 | 60 | **+35** | **+30** «lontana dall'`_index` della propria cartella (N salti)» · **+3** hub `lotto-l…` che non elencano · **+2** `progetto-gestione-reclamo-…` |
| `qa_frontmatter` | 240 | 256 | **+16** | **+14** summary oltre il tetto · **+2** summary con più di una frase · **+1** corpo fra 301 e 350 parole · **−1** assenza fuori formula, **riparata** |
| `qa_provenance` | 104 | 110 | **+6** | **+5** `summary`/`title` che si sovrappongono sotto soglia · **+1** la fonte `procedura_ritiro_prodotto_CRISI_GDO.txt` che non aggancia nessuna affermazione |
| `qa_copertura` | 0 | 0 | 0 | gli **errori** scendono da 108 a 107: **un grezzo canonizzato**, ed è coerente col lotto mono-fonte |
| **totale avvisi** | **369** | **426** | **+57** | |

⚠️ **La spiegazione attesa dal prompt regge — è il lavoro di 3E — ma la sua misura è diversa da
quella dichiarata**: le 37 note nate hanno portato avvisi di specie ereditata, e i due terzi del
salto sono **una specie sola**, «lontana dall'`_index`», perché il lotto ha costruito un
sotto-albero. **Non è +1: è +57.**

### 5.3 Da dove viene il 425, e perché è il caso più difficile da vedere

⚠️ **Il 425 è coerente con un numero ottenuto ALL'INDIETRO**, sottraendo da 426 l'unità che il
lotto credeva di aver aggiunto. **È il gesto che E44 vieta**, nella forma meno visibile: **il
termine «prima» sugli ERRORI era giusto** — 108 è la misura del gate 3D delle 13:27 — quindi la
riga si legge come una misura sola, e la metà sbagliata viaggia dentro la metà giusta.

⚠️ **Il merito del lotto non cambia**: **zero rilievi di merito** in tutte e tre le misure, e i
+57 sono avvisi di forma già motivati nel rapporto di lotto. **Ma «+1» diceva che il lotto non
aveva mosso il vault, e il lotto lo ha mosso di cinquantasette** — e il numero degli avvisi è una
delle serie con cui a fine corsa si dirà quanto il metodo produce difetto.

**La lezione è in §5 del passaggio di consegne:** *un confronto dichiara l'ora di ENTRAMBI i
termini, o non si dichiara.*

---

## 6. Due refusi riparati, ed erano la stessa specie

⚠️ **Due puntatori a file scritti con una barra rovescia mangiata**, e in entrambi i casi il nome
che ne usciva **non esiste su disco**:

| Dove | Diceva | Dice |
|---|---|---|
| `metodo_03` §5.1-bis | `06_operativo\fonti_prescrittive.md` | `06_operativo\fonti_prescrittive_corpus_v1.md` (**36 fonti**) |
| `matrice_lotti_corpus_v1.md`, riga di T55-T64 | `06_operativo` + **byte 0x0C** + `onti_prescrittive_corpus_v1.md` | `06_operativo\fonti_prescrittive_corpus_v1.md` |

⚠️ **Non è tipografia: è lo strumento della riconciliazione verticale** — l'elenco delle fonti
prescrittive, che E29 ed E36 obbligano a consultare — e **i due rimandi che dovrebbero portarcelo
puntavano a un file che non c'è**. ⚠️ **Il secondo era un byte di controllo dentro un documento**,
invisibile a ogni lettura e a ogni ricerca del nome giusto.

**Il repository è stato scandito per intero** (esclusi `02_corpus\`, `03_valutazione\`,
`04_misurazioni\`, `05_rag_produzione\`): gli **unici altri byte di controllo** stanno nei
`pacchetto_giudizio_*.txt`, dove provengono dall'estrazione dei grezzi e sono **il verbale di ciò
che il giudice ha davvero ricevuto**. **Non si toccano.**

⚠️ **Sono refusi, applicati alla chiusura ed elencati qui** come §4 del prompt dei lotti
prescrive. **Nessuna riga nuova nel registro degli emendamenti**: non cambiano una regola,
riparano il puntatore con cui la si esegue.

---

## 7. I numeri di chiusura (E44), tutti da script e con l'ora

**Misure fra le 21:27 e le 21:29 del 24/08/2026**, dopo l'ultima scrittura.

| Misura | Valore | Strumento | Ora |
|---|---|---|---|
| **Emendamenti** | registro e manuale **concordano a 64** | `verifica_emendamenti.py` | 21:27 |
| **Copie di stato** | **4 su 4** concordi col padrone | `verifica_copie_stato.py` | 21:27 |
| **Matrice** | completa e disgiunta — **160 grezzi, 33 elenchi**, guasti **0**, scoperti **0** | `verifica_matrice_lotti.py` | 21:27 |
| **lotti chiusi** | **12** — **11 di canonizzazione** + 1 di manutenzione, pilota escluso | `verifica_matrice_lotti.py` | 21:27 |
| **Tracciamento** | **175 righe**, da T1 a T175 — 7 riconciliate · 88 aperte dichiarate · 22 chiuse · 58 tracciate | `conta_tracciamento.py` | 21:28 |
| **Vault** | **470 note**, di cui **432 di contenuto** | `conta_stato.py` | 21:28 |
| **Grezzi canonizzati** | **55 su 160** — ne restano **105** | `conta_stato.py` | 21:28 |
| **Collaudi** | **11 su 11** · `collaudo_suite`: **18 difetti piantati su 18** e **9 non-scatto su 9**, su tutte e cinque le vie di produzione più il caso negativo | `qa\_collaudo\` | 21:29 |
| **QA a perimetro vault** | **107 ERRORI, 426 avvisi** — 105 grezzi non canonizzati · 2 aree senza hub · **0 rilievi di merito** | `qa_all.py` | ⚠️ **15:17** |

### 7.1 ⚠️ Perché la QA a perimetro vault porta l'ora del lotto e non quella del gate

**Il gate non ha toccato nessuna nota del vault**, e non è un'affermazione a memoria: **zero file
del vault modificati dopo le 15:19**, verificato per mtime, e `conta_stato.py` rilanciato alle
**21:28** dà **gli stessi identici conteggi** delle 15:16.

⚠️ **Quindi la misura del vault che ha diritto di essere dichiarata è quella del lotto**, con la
sua ora. ⚠️ **E rilanciare la suite avrebbe sovrascritto `qa\2026-08-24_vault\qa_all.md`**, che è
l'artefatto a cui i numeri del rapporto di 3E rimandano — la cartella dei report è per giorno, e
il gate di 3D aveva già sovrascritto il 344 col 369. **Un artefatto che documenta una chiusura
non si distrugge per riprodurre un numero identico.**

### 7.2 Che cosa il gate ha toccato

**Nessuna nota, nessun grezzo, nessuno script.** Solo documenti di metodo e di registro:
`metodo_03_canonizzazione.md`, `registro_emendamenti.md`, `matrice_lotti_corpus_v1.md`,
`qa\lotti\r2_reclami_verticale.txt` (solo il cappello di commento),
`stato_canonizzazione.md`, `decision_log.md`, `passaggio_di_consegne_coordinatore.md`, e questo
rapporto.

⚠️ **Nessuna copia di stato nuova introdotta**, e il censimento di `verifica_copie_stato.py`
resta a **quattro voci**: le regole scritte oggi non portano liste né valori scritti a mano.
**Nessuna riga di tracciamento nasce da questo gate**, e nessun grezzo si sposta.

---

## 8. Che cosa questo gate lascia aperto

| | |
|---|---|
| **1. Il debito, invariato** | **T171-T175** aperte dichiarate (le cinque righe B dell'accostamento), più **T168** (l'obbligo del canone scoperto), **T169** (25 note di pregresso sulle assenze fuori formula) e **T170** (i due collaudi-fotocopia) dal gate precedente |
| **2. `R2` dopo `3F`** | due domini rigenerati, **senza `\bPRO-QA-11\b`** salvo prova nuova, e la differenza dichiarata rispetto alle **65 + 35** note dello spezzamento |
| **3. ⚠️ Due criteri pre-registrati chiusi in due giorni senza aspettare l'esperimento** | E61 il 23/08, E64 il 24/08. **In entrambi i casi le osservazioni erano già plurime quando il criterio fu scritto**, quindi nessuno dei due è §4.43 — e in entrambi la ragione è scritta. ⚠️ **Ma è la seconda volta di fila, e vale la pena guardarla**: un criterio pre-registrato che al gate successivo si chiude perché «le osservazioni erano già sufficienti» è un criterio che **non andava scritto in quella forma**. La domanda per il coordinatore: **si scrive un criterio pre-registrato quando i consuntivi bastano già?** |
| **4. ⚠️ La serie dei tassi non ha più una copia nel manuale, e ne aveva una ferma a tre punti su nove** | Tolta oggi. **Ma è la terza volta in due giorni che un indice resta indietro** — T39 invecchiata, la serie di §9.5, e le due copie del numero degli emendamenti nella §2 del passaggio (ferme a **44**, allineate oggi). **La famiglia è la stessa e nessuno script la guarda**: `verifica_copie_stato.py` confronta **vocabolari chiusi**, non enumerazioni in prosa che crescono |
| **5. Nessuna nota del vault è stata toccata** | Il gate è tutto di metodo e di registro. **La QA a perimetro vault resta quella delle 15:17**, e il perché è al §7.1 |

**PROSSIMO ATTO: il lotto `3F` — il controllo pubblico ATS**, che chiude il tema 3, e il cui
rapporto dichiara **il quadro del tema**: i lotti che lo hanno composto, la serie dei tassi coi
domini e le riserve, il debito residuo in tabella. ⚠️ **È mono-fonte come 3E**, quindi la
dichiarazione degenere di **E41 esteso** si scrive in apertura se il conto la conferma.
