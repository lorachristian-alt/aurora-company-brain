# Rapporto del lotto R2 — la riconciliazione verticale a due domini

> **Che cos'è** · L'esito di `R2`, il secondo lotto di **manutenzione** del progetto (E35),
> eseguito il 31/08/2026 secondo il §3-bis di `06_operativo\prompt\prompt_s4_lotti.txt` e la
> PARTE 5 di `prompt\prompt_gate_3f_r2.txt`.
> **Chi lo legge** · Il titolare, e poi il coordinatore. ⚠️ **Questo rapporto contiene due cose
> strutturali** — un guasto dello strumento trovato in apertura e una regola che in un lotto di
> manutenzione non ha margine — raccolte in §9.
> **Misure** · tutte da script, ognuna con la sua ora (E44).

---

## 1. L'apertura: il perimetro si rigenera, e rigenerarlo ha trovato un guasto

### 1.1 ⛔ LE DUE INVOCAZIONI ERANO UN GUASTO, E AVREBBERO PERSO UN DOMINIO INTERO

L'elenco di R2 prescriveva di rigenerare il perimetro così:

```
python candidate_r1.py --dominio reclami --lotto r2_reclami_verticale
python candidate_r1.py --dominio ritiro  --lotto r2_reclami_verticale
```

⛔ **`candidate_r1.py` scrive l'elenco con `"w"`: la seconda invocazione cancella la prima.**
Il perimetro risultante sarebbe stato quello del **solo `ritiro`** — **31 note invece di 102** —
e **il file sarebbe apparso perfettamente corretto**: intestazione giusta, criterio giusto,
note vere. Un dominio intero sparito in silenzio.

⚠️ **È la specie di §4.47**: una procedura che *sembra* comporre e invece sovrascrive. Nessun
errore, nessun avviso, e nulla a valle avrebbe potuto accorgersene — perché 31 note sono un
perimetro plausibile quanto 102.

**Riparato in apertura, prima di leggere una nota**: `--dominio` accetta ora più valori in una
invocazione sola e il perimetro è la loro **unione** — una nota entra se è scoperta per **almeno
uno** dei domini, e le due condizioni di E37+E36 valgono dominio per dominio senza mescolarsi.
⚠️ **Con un dominio solo il comportamento è identico a prima**, ed è un caso del collaudo.

**Difetto piantato in `qa\_collaudo\collaudo_domini_unione.py`, cinque casi:**

| # | Caso | Atteso | Esito |
|---|---|---|---|
| 1 | **LA PREMESSA**: i due perimetri non sono contenuti l'uno nell'altro | diversi (86 e 31, comuni 15) | ✅ |
| 2 | **IL DIFETTO PIANTATO**: due invocazioni sullo stesso `--lotto` | resta solo il secondo (31) | ✅ |
| 3 | l'invocazione unica coi due domini | l'**unione** (102) | ✅ |
| 4 | **non-scatto di regressione**: un dominio solo | invariato (86) | ✅ |
| 5 | l'unione non è la somma: `102 = 86 + 31 − 15` | l'identità regge | ✅ |

⚠️ **Il caso 1 è la premessa senza la quale il 2 passerebbe per il motivo sbagliato**: se un
dominio fosse contenuto nell'altro, sovrascrivere darebbe lo stesso insieme dell'unione e il
difetto non si vedrebbe. **È la stessa disciplina ratificata dal gate di 3F sul collaudo del
delimitatore.**

### 1.2 ⛔ LA DIFFERENZA CHE IL PROGETTO ASPETTAVA DA TRE LOTTI, E NON DICE QUELLO CHE CI SI ASPETTAVA

Il perimetro **si rigenera, non si eredita**, e la differenza rispetto alle **65 + 35** note
degli spezzamenti doveva misurare *quanto 3D, 3E e 3F hanno già sanato*.

| Dominio | Allo spezzamento | Oggi | |
|---|---|---|---|
| `reclami` | **65** (23/08, spezzamento di 3D) | **86** | ⚠️ **+21** |
| `ritiro` | **35** (24/08, spezzamento di 3E) | **31** | −4 |
| **unione** | — | **102** | 15 note in comune ai due domini |

⚠️ **La dichiarazione del dominio `reclami` non è cambiata fra le due misure**: le stesse nove
espressioni in `12a41aa`, `babc743`, `7831199` e `327741b` *(confrontate commit per commit)*. **Il
confronto è quindi sullo stesso strumento**, e la crescita è del vault.

**La decomposizione del dominio `reclami`, che è il punto:**

| | |
|---|---|
| delle **65** vecchie, ancora dentro | **63** |
| **USCITE dal perimetro** — cioè sanate da 3D, 3E o 3F | **2** |
| entrate nuove | **23** |
| **di cui note NATE dal 23/08 in poi** | **23 su 23** |

⛔ **I tre lotti del tema 3 hanno sanato DUE note del perimetro e ne hanno aggiunte
ventitré, scrivendone di nuove.** Il debito della riconciliazione verticale **non si stava
riducendo: stava crescendo**, e cresceva per mano dei lotti stessi.

⚠️ **Non è di per sé un difetto**, ed è importante non leggerlo come tale: una nota nuova che
nomina un dominio senza citarne la fonte è **scoperta solo se quella fonte prescrive ciò di cui
la nota parla** (E36). Quante lo fossero davvero è esattamente ciò che R2 ha misurato, ed è il
§2.

⚠️ **Ma una cosa la dice, e vale per il metodo**: **E37 misura un debito che ogni lotto nuovo
alimenta**, e il perimetro di un lotto di manutenzione invecchia mentre lo si aspetta. Delle 102
note di oggi, **30 sono nate dopo lo spezzamento che ha creato R2**.

---

## 2. I tre numeri del §3-bis

| | |
|---|---|
| **note guardate** | **102** — il perimetro rigenerato dai due domini |
| **note corrette** | **21** — hanno ricevuto la fonte che le governa, con la frase che la usa e il locator |
| **tasso di difetto** | **20,6 %** *(calcolato: 21 su 102)* |

⚠️ **Che cosa questo tasso misura, e non è quello che sembra.** Non è il tasso di errore delle
note: è **la quota del perimetro che era davvero scoperta**. Le altre **81** parlavano del
dominio per una parola e non per la sostanza, e per E36 la fonte non andava aggiunta —
aggiungerla per far scendere il numero sarebbe stato il trucco che E41 vieta, spostato di un
piano.

⚠️ **E il numero decide una cosa sola**, come il §3-bis chiede: se il ripasso vada rifatto a
fine corsa o se la regola in vigore basti. **Un difetto su cinque non è un residuo**: la
riconciliazione verticale su questi due domini **va rifatta a fine corsa**, e la ragione sta nel
§1.2 — il perimetro cresce più in fretta di quanto lo si sani.

### 2.1 Il criterio con cui le 81 non sono state corrette

Il criterio è **E36 alla lettera**: la fonte si aggiunge quando **prescrive ciò di cui la nota
parla**, non quando la nota nomina una parola del dominio. Le 81 si distribuiscono su poche
specie, e la specie si legge dall'espressione che le ha pescate:

| L'espressione che pesca | Note | Perché non è una scopertura |
|---|---|---|
| `\breclam` | 55 | «il reclamo di maggio» come **àncora temporale**: la nota data un fatto, non parla del ciclo del reclamo |
| `\bREC-20\d\d-\d{3}\b` | 12 | il numero di pratica dentro un **wikilink o una glossa** verso l'hub del reclamo |
| `causa radice` | 12 | è il nome di una **colonna del registro delle non conformità**, che un'altra fonte prescrittiva governa |
| `blocco lotti` · `lotti bloccati` | 9 | è il nome di una **riga del cruscotto KPI** |
| `mass balance` | 8 | è il nome del **foglio di calcolo** usato come fonte di dati, non della ricostruzione che la procedura prescrive |
| `corpo estrane` | 8 | descrive il **difetto del prodotto**, che il manuale HACCP governa |
| le altre | 22 | sigle e definizioni citate **dentro l'elenco che la fonte stessa porta** |

⚠️ **Due specie meritano di essere dette per nome**, perché sono quelle in cui la misura
sovrastima:

- **`causa radice` e `mass balance` sono nomi di oggetti, non del dominio.** Il registro delle
  non conformità ha una colonna `Causa_radice`, e il file di rintracciabilità si chiama
  *mass balance*: una nota che li cita sta nominando un campo, non discutendo la procedura.
- **`\breclam` pesca ogni nota che nomini il caso di maggio**, e il caso di maggio attraversa
  metà dell'archivio. **È la parola più produttiva del dominio e la meno specifica.**

⚠️ **Nessuna delle due si tocca, e la ragione è §4.45**: restringere la dichiarazione **a numero
visto** romperebbe la comparabilità della serie. Il caso residuo si dichiara col suo nome, come
al lotto 3F, e il criterio pre-registrato del gate di 3F è esattamente quello che decide se un
giorno si meccanizzerà.

---

## 3. Che cosa il lotto ha corretto, per grappoli

### 3.1 Il blocco cautelativo — quattro note

⚠️ **Il blocco dei lotti L26130 e L26131 non era una decisione: era un adempimento dovuto**, e
due procedure lo prescrivono prima del manuale HACCP a cui le note lo attribuivano. `PRO-QA-08`
§6.2 lo mette fra le **verifiche immediate entro 24 ore** per le classi 1 e 2; `PRO-QA-14` §3.3
lo definisce.

⛔ **E la riunione di direzione del 13/05 lo approva all'unanimità come se fosse una scelta**,
senza che nessuno dei presenti nomini la procedura che lo impone.

### 3.2 Il mock recall — cinque note

⚠️ **Il criterio «ricostruzione ≥ 99 % entro 4 h» non nasce nel manuale HACCP: nasce in
`PRO-QA-14` §10.2**, che è anche l'unica fonte a portare il secondo criterio — la reperibilità
del «team >= 80% al primo tentativo di chiamata» — che nessuna delle misure a confronto
riportava. ⚠️ **E `PRO-QA-14` §10.4 prescrive che l'esito del mock recall sia dato di ingresso
del riesame della direzione**: la decisione sull'ERP rimandata «anche alla luce dell'esito del
mock recall» è la procedura che si vede agire.

### 3.3 Il `MOD-QA-31`, che le due procedure si dividono — cinque note

⚠️ **Il modulo su cui la crisi si registra è il modulo dei reclami**, e `PRO-QA-08` ne assegna
le sezioni: la **sezione A** all'apertura (§6.1), la **sezione C** alla causa radice (§7.1). Le
note che descrivevano la crisi lo trattavano come modulo della procedura di ritiro.

⚠️ **E le due scale di classificazione condividono il modulo e non il termine**: `PRO-QA-08` §5
vuole la classificazione del reclamo **entro 8 ore lavorative dalla ricezione**, `PRO-QA-14` §4
classifica l'evento di crisi senza fissare un termine per la classificazione.

### 3.4 Il perimetro, i termini e gli indicatori — sette note

⚠️ **Il perimetro del ritiro ha due prescrizioni, e la stima del 14/05 non ne nomina nessuna**:
`PRO-QA-08` §6.2 lo ricava dalla rintracciabilità su `MOD-MAG-02`, `PRO-QA-14` §6 lo vuole
ricostruito «entro 4 ORE dalla convocazione».

⚠️ **E gli indicatori dei reclami non nascono nel cruscotto**: `PRO-QA-08` §10 dispone che
«Gli indicatori sono presentati al riesame della direzione e, in forma aggregata, al team
HACCP».

---

## 4. I due fatti che le correzioni hanno fatto emergere

Il §3-bis lo prevede: *se una correzione fa emergere un fatto senza padrone la nota si scrive*.
Ne sono usciti due, ed entrambi vengono dal mettere le due procedure una accanto all'altra —
cosa che nessun lotto aveva mai fatto, perché ciascuna era arrivata col suo.

### 4.1 ⛔ DUE PROCEDURE DELLO STESSO CICLO CHIEDONO DUE CARTELLINI DIVERSI PER LO STESSO BLOCCO

| Fonte | Che cosa prescrive |
|---|---|
| `PRO-QA-08` §6.2, verifiche immediate | «blocca cautelativamente l'eventuale giacenza del lotto a magazzino, con **cartellino giallo NON CONFORME**» |
| `PRO-QA-14` §6, FASE 2 lettera a | «MOD-MAG-02, **cartellini BLOCCATO**» |
| la mail interna del 13/05 | «ho messo in stato **BLOCCATO** a magazzino i lotti L26130-L1-T2 e L26131-L1-T2» |

⚠️ **Le due procedure non sono in alternativa: sono in sequenza** — il punto 5 dello stesso §6.2
manda a convocare il team per la valutazione di attivazione della procedura di ritiro. **Un
lotto può quindi essere bloccato due volte, a due titoli**, e nessuna delle due dice che cosa
succeda al cartellino nel passaggio. Nota: `questione-due-cartellini-per-lo-stesso-blocco`.

### 4.2 ⚠️ UN CLIENTE E IL SUO TERMINE, NOMINATI DENTRO UNA PROCEDURA INTERNA

`PRO-QA-08` §8.1 porta come esempio «Assicurazione Qualità Tosano: riscontro entro 48 h» e
dispone che «i termini contrattuali del cliente prevalgono su quelli del par. 6.3 se più
stringenti». ⚠️ **La richiesta del 14/05, che l'archivio raccontava come un vincolo esterno
piombato addosso alla pratica, attiva una clausola che la procedura aveva già scritto** — e i
quattro adempimenti che il cliente elenca stanno già tutti nel contenuto che lo stesso paragrafo
impone alla risposta. Nota: `fatto-le-48-ore-gia-in-procedura`.

---

## 5. I tre censimenti, riparati nel perimetro (§2.5 del gate di 3F)

| Censimento | Censite nel perimetro | Riparate |
|---|---|---|
| **T142** — superlativi sull'archivio | **3** | **3** |
| **T158** — affermazioni che vivono solo nell'intestazione | **6** | **6** |
| **T169** — assenze sull'archivio senza artefatto | **10** | **10** |

⛔ **Uno dei tre superlativi era del lotto 3F, scritto il giorno prima** — «il costo stimato non
torna con l'**unico** preventivo che l'**archivio** porta» — ed è **E47 colto in flagranza dal
censimento**, non da una rilettura.

⚠️ **E le assenze non si sono chiuse con un artefatto: si sono chiuse restringendo il
perimetro.** Tre note portavano la formula di attestazione di E3 senza l'artefatto che E43
impone; **la ricerca è stata rifatta** con `cerca_assenza.py` e **ha TROVATO i termini** — la
segregazione compare in dieci documenti, i materiali della guarnizione in cinque. **L'assenza
non era dell'archivio: era delle fonti citate**, e le due ricerche restano come artefatti
datati del 31/08/2026 a documentare la decisione.

⚠️ **È la seconda via che E43 ammette, ed è quella giusta qui**: cinque delle dieci assenze
erano affermazioni **interpretative** — «nessun documento dice quale lettura sia giusta» — che
nessuna ricerca per termini può verificare. **Un artefatto non le avrebbe rese vere.**

---

## 6. Il giudizio dedicato alle note nate (E58)

Le due note nate dalle correzioni non avevano mai visto un giudice: hanno avuto il loro
**giudizio dedicato**, a contesto pulito, una fetta ciascuna.

| Nota | Esito |
|---|---|
| `questione-due-cartellini-per-lo-stesso-blocco` | ✅ **pulita** |
| `fatto-le-48-ore-gia-in-procedura` | ⛔ `afferma_oltre` — **due rilievi, accolti entrambi** |

### 6.1 ⛔ E57 ESTESO COLTO IN FLAGRANZA, UN GIORNO DOPO ESSERE STATO SCRITTO

La nota diceva: «**È l'unico cliente che il paragrafo nomina**». ⛔ **Il §8.1 ne nomina
quattro** — «Tosano Cerea S.p.A., Alì S.p.A., Rossetto Trade S.p.A., Famila Nordest» — e Tosano
è l'unico che compare **con un termine**, non l'unico che compare.

⚠️ **È esattamente la specie che E57 esteso ha chiuso al gate di 3F il giorno prima**: un
superlativo il cui soggetto è **un elenco della fonte**, che la fonte riletta smentisce. **La
regola c'era, era fresca, ed è stata violata comunque** — e a prenderla non è stata la
scrittura ma il giudizio.

⚠️ **La correzione applica la regola nuova alla lettera**: «l'unico dei **quattro** clienti GDO
nominati dal paragrafo a comparire con un termine *(contati)*». **Il superlativo con
soggetto-elenco porta il conto.**

### 6.2 ⚠️ Il secondo rilievo, ed è di perimetro

La nota diceva che le 48 ore erano «**il termine che Aurora si era data** per questo cliente».
⚠️ **La fonte dice il contrario**: sono «i termini contrattuali **del cliente**», e la procedura
dispone che **prevalgano** sui propri. **Il termine resta del cliente; ciò che è di Aurora è la
regola che gli cede il passo.** Corretto.

---

## 7. La revisione col canone, e che cosa ha trovato

La revisione gira in **sessione diversa** e riceve il canone (E45). Su un lotto di manutenzione
il suo compito è particolare, ed è stato scritto nel mandato: **guardare se una frase aggiunta
oggi contraddice una frase che era già lì.**

| | Che cos'è | Quanti |
|---|---|---|
| **rilievi A** | errori dentro le note | **17**, di cui **9 su ciò che R2 ha scritto oggi** — tutti accolti e corretti |
| **righe B** | divergenze nuove fra le due procedure e l'archivio | **8** |

### 7.1 ⛔ L'ERRORE PIÙ GRAVE È MIO, E LO STRUMENTO CE L'HA MESSO DENTRO

R2 aveva scritto che il registro dei reclami **non** usa la scala di `PRO-QA-08` §5: che la sua
colonna «Gravità» dicesse *minore, maggiore, CRITICO* dove la procedura dice *classe 1, 2, 3*.

⛔ **È falso.** La tabella del §5 dà «1 **Critico**», «2 **Maggiore**», «3 **Minore**», «4
Segnalazione»: **sono esattamente le parole del registro**, e il registro classifica con la
scala della procedura chiamandola col nome invece che col numero.

⚠️ **Perché non l'avevo vista, ed è un fatto sullo strumento, non sulla mia attenzione:
l'estrazione di cantiere mette le tabelle del `.docx` IN CODA al documento**, non nel punto in
cui stanno. La tabella compare a circa **11.400 caratteri** dall'inizio, dopo il §12, mentre il
§5 mostra un buco fra «secondo la seguente scala:» e il capoverso successivo. **Un buco nel
punto giusto sembra un'assenza.**

⚠️ **E nella stessa riga avevo citato come vigente una frase BARRATA** — «I reclami di classe 1
e 2 vengono comunicati al titolare solo se il cliente è del canale GDO» — che il documento porta
cancellata, con accanto la correzione di chi l'ha riscritta e il capoverso che la supera.

**Tracciato a T195, non riparato**: tocca l'estrattore, e questa sessione non lo ha toccato di
propria iniziativa.

### 7.2 Gli altri otto rilievi su ciò che R2 ha scritto

| Nota | Che cosa non tornava |
|---|---|
| `doc-classi-di-gravita-della-crisi` | «`PRO-QA-14` non fissa un termine per la classificazione»: **lo fissa, ed è più stretto** — la classificazione sta dentro la «VALUTAZIONE PRELIMINARE (entro 2 ORE da T0)» |
| `fatto-blocco-cautelativo-lotti` | «L'archivio non contiene il calcolo che porta a quella cifra»: **il calcolo c'è, nella fonte che R2 aveva appena aggiunto** — 3.290 + 1.480 + 3.630 = 8.400 |
| `doc-verifiche-immediate-reclamo` | «la revisione e il titolo coincidono con quelli che `PRO-QA-08` attribuisce alla `PRO-QA-11`»: **`PRO-QA-08` non attribuisce nessuna revisione** |
| `questione-due-cartellini-per-lo-stesso-blocco` | «un blocco disposto **il giorno prima**»: la data non viene da nessuna delle tre fonti |
| `fatto-test-rintracciabilita-audit-2h50` | il 99,6 % attribuito all'esercitazione del 07/11/2025: sono **due prove diverse col medesimo numero** |
| `kpi-mass-balance-l26130` | il `summary` applicava il metro che il corpo dichiara **non applicabile**, e «entrambi i termini» non erano quelli |
| `kpi-indicatori-2025-consuntivo` | blocco copiato dalla nota gemella: parlava del cruscotto, e la fonte di questa nota è il verbale |
| `fatto-classe-2-provvisoria-sul-frammento` | «il termine della prima era già scaduto»: eccede le fonti, e il modulo porta la classificazione col 12/05 |

⚠️ **Sette degli otto sono della stessa specie**: una frase aggiunta oggi che afferma **oltre le
fonti citate** o **contro una frase già presente nella nota**. ⚠️ **È E65 il giorno dopo che è
stato scritto, e E51 accanto** — e a prenderli non è stata la scrittura, ma il solo strato che
legge la nota **intera** avendo il canone davanti.

### 7.3 Le otto righe B, e sei non entrano in vault

| | La divergenza | Dove è finita |
|---|---|---|
| **H1** | i **cinque recapiti** di reperibilità del team di crisi divergono, cinque su cinque | ⏳ **T187**, tracciata |
| **H2** | una procedura **approvata a settembre** rendiconta eventi di **novembre** | ⏳ **T188** |
| **H3** | anche la procedura dei reclami ha **due codici** — `PRO-QA-13` per `PRO-QA-14` | ⏳ **T189**, gemella di **F1** |
| **H4** | **due scale assegnano il ritiro a classi diverse** | ⏳ **T190** — ✅ risponde all'obbligo di **F8** del lotto 3D |
| **H5** | **tre versioni della data del blocco**, e da lì decorrono le 24 ore | ⏳ **T191** |
| **H6** | i **due cartellini** per lo stesso blocco | ✍️ **T192, SCRITTA** |
| **H7** | una **quarta tabella di obiettivi 2026**, dentro `PRO-QA-08` §10 | ⏳ **T193** |
| **H8** | un obbligo attribuito al **capitolato** sta nell'**accordo quadro** | ⏳ **T194**, forza media |

⛔ **Sei si tracciano e NON si scrivono, ed è una decisione dichiarata, non una dimenticanza.**
Scriverle avrebbe voluto dire aprire un ciclo nuovo — note, giudizio, revisione — dentro un
lotto che stava chiudendo. **Le righe le portano con sé col loro obbligo**, e il gate decide se
vale un lotto proprio.

⚠️ **E tutte e otto nascono dallo stesso gesto**: `PRO-QA-08` e `PRO-QA-14` sono arrivate in due
lotti diversi, e **nessuno le aveva mai messe una accanto all'altra**. È esattamente ciò per cui
E37 esiste.

---

## 8. ⚠️ IL TETTO DELLE 350 PAROLE NON HA MARGINE IN UN LOTTO DI MANUTENZIONE

**È la voce strutturale di questo lotto, e nasce dal contarla, non dall'impressione.**

In un lotto di canonizzazione la nota si scrive da zero e il tetto è un vincolo di progetto: si
sta dentro perché si sceglie che cosa dire. ⚠️ **In un lotto di manutenzione la correzione è
un'AGGIUNTA a una nota già scritta bene**, e il tetto non ha margine per lei.

| | |
|---|---|
| correzioni che hanno superato il tetto al primo tentativo | **8 su 21** *(contate)* |
| il margine più stretto misurato | **5 parole** (`fatto-richiesta-relazione-48-ore`, 345 su 350) |
| costo di un rimando `[[…]]` nel conteggio | **6-10 parole**, perché il contatore toglie le parentesi e conta lo slug |

⚠️ **Che cosa si è fatto, e in quest'ordine**: prima si è stretta la correzione al minimo che
regge la citazione; poi si è compressa **la ripetizione che aveva già un padrone altrove** —
nominare invece di spiegare, che è E64 usato per far spazio; e **una sola volta** la nota si è
divisa, perché il fatto nuovo stava in piedi da solo (`fatto-le-48-ore-gia-in-procedura`).

⛔ **Che cosa NON si è fatto: tagliare un fatto per stare nel budget.** In un caso la
compressione aveva tolto una frase che portava tre azioni immediate del reclamo; **è stata
rimessa**, e al suo posto è uscita la spiegazione di una prescrizione che ha il suo padrone in
un'altra nota.

⚠️ **La domanda per il gate, e non è retorica: un lotto di manutenzione deve stare sotto lo
stesso tetto di uno di canonizzazione?** Le tre risposte possibili sono tutte scomode —
alzare il tetto indebolisce E28 dove serve, esentare la manutenzione crea due regimi, dividere
ogni nota che cresce moltiplica le note su un vault che ne ha già 509. **Qui si è tenuto il
tetto e si è pagato in compressione**, ed è il conto sopra.

---

## 9. Le misure di chiusura (E44), tutte da script e con l'ora

**Tutte del 31/08/2026.**

| Misura | Valore | Strumento | Ora |
|---|---|---|---|
| specie del lotto | **manutenzione (E35): 0 grezzi, perimetro di sole note** | `conta_perimetro_lotto.py` | 15:04 |
| note **candidate** dallo script d'apertura | **102** | `conta_perimetro_lotto.py` | 15:04 |
| note **nate** nel lotto | **3** — 2 di contenuto, 1 di diario | `conta_perimetro_lotto.py` | 15:04 |
| **note controllate** | **105** | `conta_perimetro_lotto.py` | 15:04 |
| **QA, perimetro lotto** | **0 ERRORI, 109 avvisi** | `qa_all.py` | 15:04 |
| **note corrette** | **21** | — | — |
| **tasso di difetto** | **20,6 %** *(calcolato: 21 su 102)* | — | — |
| **Collaudi** | **14 su 14** — il quattordicesimo è `collaudo_domini_unione.py`, nato da questo lotto | `_collaudo\` | 15:04 |
| **Copie di stato** | ogni copia concorda col suo padrone | `verifica_copie_stato.py` | 15:04 |
| **Matrice** | completa e disgiunta — **160 grezzi, 34 elenchi**, guasti 0 | `verifica_matrice_lotti.py` | 15:04 |
| **lotti chiusi** | **14** — 12 di canonizzazione + **2 di manutenzione** | `verifica_matrice_lotti.py` | 15:04 |
| **Tracciamento** | **195 righe**, da T1 a T195 — 7 riconciliate · 103 aperte dichiarate · 23 chiuse · 62 tracciate | `conta_tracciamento.py` | 15:04 |
| **Emendamenti** | registro e manuale **concordano a 65** | `verifica_emendamenti.py` | 14:59 |
| **Vault** | **510 note** · **56/160** grezzi citati | `conta_stato.py` | 14:59 |

⚠️ **Nessun emendamento nuovo**: il registro resta a **65**. R2 lascia **domande al gate**, non
regole scritte da sé.

---

## 10. Che cosa torna al coordinatore

| | Voce | Stato |
|---|---|---|
| **1** | ⛔ **L'estrazione di cantiere mette le tabelle del `.docx` in coda al documento** | **T195, tracciata e NON riparata** — tocca l'estrattore. ⚠️ **Il costo è già stato pagato dentro questo lotto**, e ogni giudizio dato su un `.docx` con tabelle l'ha pagato senza saperlo |
| **2** | ⚠️ **Il tetto delle 350 parole non ha margine in un lotto di manutenzione** | 8 correzioni su 21 lo hanno superato al primo tentativo, margine minimo **5 parole**. Le tre risposte possibili sono tutte scomode, e il §8 le mette in fila |
| **3** | ⚠️ **La riconciliazione verticale va rifatta a fine corsa** | tasso **20,6 %**, e il perimetro **cresce più in fretta di quanto lo si sani**: 2 uscite contro 23 entrate |
| **4** | ⛔ **Sei divergenze tracciate e non scritte** | **T187-T194**. Due pesano più delle altre: **H4** risponde all'obbligo di F8 del lotto 3D, **H3** è la gemella di F1 |
| **5** | ⚠️ **Il guasto delle due invocazioni era nell'elenco del lotto, scritto da un gate** | riparato e collaudato. ⚠️ **La forma prescritta era sbagliata e nessuno l'aveva eseguita prima**: un'istruzione operativa scritta e mai provata è un difetto che aspetta |
