# Rapporto del lotto R1 — riconciliazione verticale

> **Cos'è** · Il rapporto del **primo lotto di manutenzione** del progetto (E35): quello che
> non canonizza grezzi nuovi ma ripara note già scritte, aperto dal gate del lotto 1C.
> **Stato** · **CHIUSO il 19/08/2026**, dopo tre giri di giudizio, la revisione col canone e
> il ri-giudizio. ⚠️ Il terzo giro ha prodotto ancora rilievi: il lotto si è chiuso
> **nominando il pattern** che li rigenera (E26), non ripetendo il ciclo. Il pattern è al §9.
> **Il gate vero** · Questo rapporto torna al coordinatore per l'approvazione. Il gate
> intermedio del 19/08/2026 aveva autorizzato il lotto a finire, non lo aveva approvato.

---

## 1. Il lotto, in una tabella

⚠️ **Questa tabella non si scrive a mano, ed è il difetto che il gate intermedio ha trovato.**
Nella prima stesura tre numeri su tre erano sbagliati — il perimetro, le note toccate, le note
in fascia di avviso — **nello stesso documento in cui erano appena state sanate tre versioni
divergenti dello stesso conteggio**. La regola di `conta_stato.py` si estende alla tabella del
perimetro: si legge dagli elenchi e dai report della suite, o non si dichiara. Lo script è
`06_operativo\conta_perimetro_lotto.py`, e nasce da questo.

<!-- PERIMETRO DEL LOTTO — generato da `06_operativo\conta_perimetro_lotto.py`
     il 2026-08-19. Si incolla VERBATIM nella tabella §1 del rapporto di lotto.
     I numeri del perimetro non si ricompongono a mano. -->

| Voce | Valore |
|---|---|
| Specie del lotto | **lotto di MANUTENZIONE (E35): perimetro di sole note** |
| Grezzi nell'elenco | **0** |
| Note **candidate** dallo script di apertura | **71** |
| Note **toccate** in corso di lotto (E32) | **4** |
| Note **nate** nel lotto | **10** — 5 contenuto · 4 note-strumento · 1 diario |
| **Note controllate in tutto** | **85** |
| Esito della suite | **0 ERRORI, 51 AVVISI** |

| Famiglia di avviso | Quanti |
|---|---|
| corpo di N parole: fra N e N, si motiva o si spezza | **28** |
| summary e title si sovrappongono per meno del N%: da ispezionare | **12** |
| lontana dall'_index della propria cartella (N salti): indizio di cattiva collocazione | **2** |
| ora senza riscontro in nessuna fonte citata: «N:N» — la nota cita un .jpg, riscontro visivo da chiudere a mano | **2** |
| summary di N caratteri (tetto N) | **1** |
| citazione senza riscontro in nessuna fonte citata: «Verifica di fine turno (capoturno)» — la nota cita un .jpg | **1** |
| citazione senza riscontro in nessuna fonte citata: «dalle N alle N.N linea ferma per rottura valvola azoto. ve | **1** |
| citazione senza riscontro in nessuna fonte citata: «prodoto nn confezionato si acumula meso su carelli in CF O | **1** |
| fonte immagine 'MOD-QA-N_N-N-N_LN_TN_scansione.jpg': riscontro visivo, da chiudere a mano | **1** |
| fonte immagine 'IMG_N_N_frammento_REC-N-N.jpg': riscontro visivo, da chiudere a mano | **1** |
| la fonte 'R_ricambio_valvola_iniezione_azoto_PKMN_URGENTE.eml' non aggancia nessuna affermazione della nota: r | **1** |

| Voce di metodo | Valore |
|---|---|
| Capacità 25-35 | **non si applica** (E35): un lotto di manutenzione non punta a produrre note |
| Soglie di E28 | **non scattate**: le note di contenuto nuove sono 5, sotto le 30 |
| Giri di giudizio | **tre**, più la revisione col canone. Esiti al §8 |

⚠️ **Il perimetro ha due numeri e vanno detti entrambi**: **71** candidate dallo script che
apre il lotto, più **14** toccate o nate in corso di lotto, cioè **85 controllate** dalla
suite. Il tasso di difetto del §3 si calcola sulle **71**, perché è la popolazione che lo
script ha selezionato come sospetta: le altre sono conseguenza del lavoro, non oggetto di
misura.

---

## 2. Il criterio con cui il perimetro è stato generato

E35 lo impone: **l'elenco delle note lo genera uno script e il criterio si scrive qui.** Un
perimetro composto a memoria si restringe da sé, e si restringe proprio sulle note che hanno
più probabilità di essere sfuggite — che sono le stesse che sono sfuggite la prima volta.

Una nota entra nel perimetro se valgono **entrambe** le condizioni:

1. **nomina** almeno una delle cinque cose che una fonte prescrittiva governa — un punto
   critico, una taratura o convalida, una frequenza di verifica, un limite, una responsabilità
   di processo;
2. e fra le sue `fonti` **non c'è la fonte prescrittiva che governa quella famiglia**.

⚠️ **La seconda condizione è stata rafforzata rispetto a come era stata dettata, e il gate
intermedio l'ha ratificata come E36.** Il criterio d'ordine diceva «e fra le sue fonti non c'è
**nessuna** fonte prescrittiva». Applicato alla lettera, lasciava **fuori dal perimetro 26
note che nominano un punto critico senza citare il manuale HACCP**, perché citavano *un'altra*
fonte prescrittiva — l'elenco delle attrezzature, la checklist del metal detector, il piano di
manutenzione. Ma il limite critico di un CCP lo prescrive **il manuale**, non il registro
degli strumenti. Lasciarle fuori avrebbe fatto mancare a R1 **esattamente le note che lo hanno
generato**.

### Il numero di partenza era 30, lo script ne dà 71, e la differenza si spiega

| Conteggio | Note |
|---|---|
| §11 del rapporto 1C: note che nominano un CCP senza citare il manuale | **30** |
| Lo stesso, ricontato dallo script sulla famiglia «punto critico» | **40** |
| Perimetro completo, cinque famiglie | **71** |

**Vince lo script.** Fra 30 e 40 la differenza è che la famiglia «punto critico» dello script è
più larga di «nomina un CCP»: comprende anche `limite critico`, `HACCP`, `prerequisito`, `PRP`.
Fra 40 e 71 sono **le altre quattro famiglie**, che al gate di 1C non erano state contate
perché si guardava il solo manuale.

---

## 3. I TRE NUMERI CHE E35 PRETENDE

| | |
|---|---|
| **Note guardate** | **71** |
| **Note corrette** | **41** |
| **Tasso di difetto** | **57,7 %** *(calcolato: 41 su 71)* |

⚠️ **È il numero che il gate deve pesare.** Più della metà delle note che parlano di qualcosa
di prescritto non aveva sotto mano la prescrizione.

### Le 30 note guardate e chiuse senza correzione, per ragione

| Ragione | Note |
|---|---|
| **Nessuna fonte prescrittiva citabile le governa** — energia, costi, utenze: il corpus non contiene il contratto di fornitura elettrica, e una soglia contrattuale non è una prescrizione di processo | **11** |
| **La prescrizione ha già un padrone che la porta**, e la nota lo linka: ricopiarla violerebbe «un fatto, un padrone» | **19** |

⚠️ **La seconda riga è il motivo per cui il tasso non è più alto**, ed è una scoperta del
lotto: il vault aveva già tre note-padrone che portano il manuale — `doc-ccp2-limite-critico`,
`doc-ccp4-limite-critico`, `doc-manuale-haccp` — nate in 1B e 1C. La riconciliazione verticale
era quindi **in parte già fatta**; quello che mancava era il collegamento fra la nota che
afferma e la nota che porta la prescrizione.

---

## 4. Incompleta o afferma il falso

**Una nota che si limita a non citare la fonte è incompleta; una nota che dichiara mancante ciò
che il manuale contiene, o che attribuisce alla fonte qualcosa che la fonte non dice, AFFERMA
IL FALSO.** Il secondo numero è quello che conta.

| Classe | Note |
|---|---|
| **Incomplete** — la nota diceva il vero, mancava l'aggancio | **34** |
| **Affermavano il falso** — con la fonte sotto mano, la conclusione andava riscritta | **7** |

### Le sette che affermavano il falso

1. **`questione-durata-deviazione-ccp2-l26130`** — scriveva che «la durata della permanenza
   sotto il limite critico è ciò che determina il perimetro del prodotto da segregare». Il
   manuale lega il blocco a **«tutto il prodotto transitato dall'ultimo controllo conforme»**.
2. **`fatto-riepilogo-datalogger-inaffidabile`** — attribuiva al piano HACCP una preferenza per
   la registrazione automatica sulla manuale. Il piano **le vuole entrambe** e ne prescrive il
   confronto settimanale.
3. **`fatto-prodotto-non-segregato-deviazione-ccp2`** — trattava la segregazione come una
   domanda aperta a fine turno. Il manuale la prescrive, insieme alla notifica immediata.
4. **`fatto-nessuna-nc-per-allarmi-cf-02`** — registrava l'assenza delle non conformità come
   una lacuna del registro; il manuale rende la registrazione obbligatoria per ogni deviazione.
5. **`questione-tassello-inox-non-passato`** — chiudeva l'episodio come «verifica poi
   conforme»; il manuale attacca alla mancata rilevazione una catena di adempimenti.
6. **`doc-mod-qa-07`** — dichiarava la frequenza del CCP3 senza le due occasioni che il manuale
   aggiunge: cambio prodotto e dopo ogni intervento.
7. **`concetto-ccp`** — presentava tre punti critici. **Sono quattro.**

⚠️ **In 1C erano quattro su undici, cioè il 36 %. Qui sono sette su 41 corrette, cioè il 17 %.**
La classe più grave è meno frequente di quanto il campione di 1C facesse temere, ma è
concentrata dove il vault ragiona sulle **conseguenze di una deviazione** — cioè esattamente
dove la misura «dopo» andrà a interrogarlo.

---

## 5. Gli avvisi della QA, motivati

⚠️ **Quanti siano sta al §1, generato da script. Qui sta solo il perché**, e la separazione è
deliberata: un conteggio scritto due volte nello stesso documento è la forma in cui nascono i
numeri divergenti che questa sessione ha passato la giornata a sanare.

**Corpo fra 301 e 350 parole.** È l'avviso che questo lotto produce per costruzione: aggiungere
a una nota la fonte che la prescrive allunga il corpo, e sedici note del perimetro erano già
sopra le 280 parole. Nessuna supera il tetto di 350, e nessuna è stata spezzata, perché
spezzarla separerebbe l'affermazione dalla prescrizione che la governa. ⚠️ **Il gate intermedio
ha respinto la proposta di alzare il tetto**, e la ragione è nel codice: `parole_corpo` esclude
già il blocco `## Fonti`, quindi la riga della fonte non è mai stata contata — quelle note sono
cresciute di **prosa**. Il controllo che l'avviso chiedeva l'ha fatto il revisore col canone,
al §7.

**`summary` e `title` si sovrappongono per meno del 20 %.** Sono le note-questione, il cui
titolo è una domanda e il cui riassunto è la risposta con i dati.

**Riscontro visivo, citazioni e orari non estraibili da fonte immagine.** Note costruite su
scansioni e fotografie, con `verifica: visiva`: l'estrattore congelato restituisce stringa
vuota per costruzione. È il caso previsto da `metodo_03` §7.1, clausola 3.

**Quattro avvisi preesistenti, NON toccati.** Cadono nel perimetro ma **non appartengono a
R1**: la regola dice che quello che si trova e non è del lotto va nel rapporto, non nelle
correzioni.

---

## 6. I conflitti, dalla tabella di tracciamento

<!-- TABELLA DI TRACCIAMENTO - generata da `06_operativo\conta_tracciamento.py`
     il 2026-08-19. Si incolla VERBATIM: il numero delle righe non si legge a occhio. -->

| Esito | Righe | Quali |
|---|---|---|
| riconciliata | **3** | T17, T22, T30 |
| aperta dichiarata | **26** | T1, T2, T3, T4, T18, T23, T24, T25, T26, T27, T28, T32, T35, T36, T37, T38, T42, T43, T44, T45, T46, T47, T48, T64, T65, T66 |
| chiusa | **2** | T20, T33 |
| tracciata | **35** | T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T19, T21, T29, T31, T34, T39, T40, T41, T49, T50, T51, T52, T53, T54, T55, T56, T57, T58, T59, T60, T61, T62, T63 |
| **totale righe** | **66** | da T1 a T66, nessuna mancante e nessuna duplicata |

**R1 ha aperto dodici righe, da T55 a T66**, e ne ha estesa una (T24).

- **T55-T63** nascono dalla **guardia**: una fonte prescrittiva il cui grezzo appartiene a un
  lotto non ancora canonizzato **non si cita e non si usa**. Precedente identico: T18.
- **T64, T65, T66** sono divergenze nuove con **entrambe le gambe canonizzate**, e sono di una
  specie che la tabella non aveva: **un registro contro la fonte che prescrive**, e due volte
  **la fonte prescrittiva contro sé stessa**.

---

## 7. Il giudizio e la revisione col canone

### La revisione col canone — 7 A, 3 B, 0 C

Sessione diversa da quella che ha scritto le note, col canone e la tabella alias alla mano.

**Le tre divergenze di categoria B sono state aggiunte al canone in sezione datata**, come
§9.5 passo 3 prescrive, e due riguardano il **manuale HACCP**, cioè il documento prescrittivo
di vertice:

1. **Il manuale dichiara rimosso il carrello ricambi** nella revisione dell'08/04/2026; una non
   conformità del 10/05 lo trova ancora in area produttiva e il 09/06 l'autorità sanitaria
   emette una diffida. ⚠️ È la famiglia isolata in 1B — *un'azione correttiva registrata che il
   dato non conferma* — applicata al manuale di autocontrollo.
2. **La validazione del CCP2 potrebbe essere scaduta, e il manuale lo chiede a sé stesso**: la
   nota «rivalidazione eseguita?» è sopravvissuta a una revisione, e il verbale che dovrebbe
   scioglierla non è in archivio.
3. **L'attività dell'acqua su due matrici** toglie la base all'arbitrato del 18/08: se 0,31 e
   0,93 misurano prodotto e farcitura, il file delle prove non è l'anomalo, e nasce una
   divergenza nuova fra manuale e scheda tecnica.

⚠️ **Nessuna delle tre sarebbe emersa dalla riconciliazione orizzontale**, che confronta i
documenti che registrano. Il manuale non registra: prescrive — e per due volte su tre
prescrive male, o dichiara compiuto ciò che non lo è.

### Le doppie padrone — 17, più due pattern sistemici

Il compito che il gate intermedio ha aggiunto: verificare se la prosa aggiunta **riscrive** una
prescrizione che ha già la sua nota padrona. La risposta è sì diciassette volte, e due
prescrizioni erano ricopiate senza avere alcun padrone:

- **la seconda firma** (§4.3.2.1) era scritta per esteso in **cinque** note. Padrona dichiarata:
  `doc-mod-qa-07`; le altre ora la linkano.
- **la gestione dei reclami** (§10.4) in **tre**, e senza padrone. Ne è nata
  `doc-gestione-reclami-haccp`.

⚠️ **È il difetto opposto a quello che il lotto riparava**, e va detto per intero: mentre
agganciava le note alla fonte che le prescrive, R1 **ha ricopiato il manuale invece di
linkarlo**, e per un tratto il vault ha avuto più copie della stessa prescrizione di quante ne
avesse prima. Le due più duplicate — seconda firma e CCP4 — sono anche quelle su cui il vault
regge le sue conclusioni più forti: se una copia diverge, diverge un'accusa.

---

## 8. I tre giri di giudizio

Strato di giudizio con `PROMPT_GIUDIZIO` v2, subagenti a contesto pulito che **non ricevono il
canone**, su tutte le note nuove o modificate. Pacchetto rigenerato dopo le correzioni a ogni
giro (E33), `title` e `summary` riletti come note a sé a ogni giro (E30).

| Giro | Note giudicate | Pulite | Rilievi accolti |
|---|---|---|---|
| 1 | 44 | 20 | **24** |
| 2 | 47 | 34 | **13** |
| 3 | 13 *(le sole modificate dal giro 2, E9)* | 4 | **9** |

⚠️ **Un guasto dello strumento, trovato dal controllo e non dal caso.** Il primo tentativo di
giro 1 è stato **annullato**: lo script che ritagliava il pacchetto in fette **scartava
l'appendice con il testo estratto delle fonti**, e i giudici si sono trovati a confrontare le
note con sé stesse. **Entrambi hanno dichiarato da sé il proprio verdetto degradato** invece di
emetterlo come valido. Il generatore era sano e i giudici erano sani: il difetto stava **fra
loro**, ed è la classe di §4.29 — la stessa che la manutenzione di stamattina aveva riparato
sulla suite, ricomparsa il pomeriggio sul mio strumento di taglio.

---

## 9. ⚠️ IL PATTERN, NOMINATO — ed è così che il lotto si chiude

E26: se il terzo giro produce ancora rilievi, il lotto **non si chiude ripetendo il ciclo**. Si
chiude dopo che il rapporto ha **nominato il pattern** che li rigenera. Il terzo giro ne ha
prodotti nove, e i tre giudici — indipendenti, a contesto pulito, su fette diverse — hanno
descritto **la stessa classe** con tre parole diverse.

### **LA CAUTELA NON SI PROPAGA**

Si dichiara come lettura ciò che era affermato come dato — e la dichiarazione resta **dove è
stata scritta**. La stessa affermazione, ripetuta altrove nella nota, mantiene la grammatica
del fatto.

I tre luoghi in cui è ricomparsa, uno per giudice:

| Dove | Come si presenta |
|---|---|
| **Nel riassunto** | il corpo dichiara «che cosa misuri `TT_02` il file non lo dichiara», il `summary` continua a dire «la temperatura della sonda di camera» |
| **In una riga di tabella** | il corpo dice che il contratto del freddo è una bozza mai firmata, la tabella di identificazione scrive «Manutentore **a contratto**» |
| **In una glossa a un wikilink** | il fatto vive in un'altra nota, il link la richiama, e la glossa lo afferma qui come se fosse delle fonti di questa |

**Perché due giri di correzioni non l'hanno estirpato:** hanno lavorato sul **corpo**, cioè
dove il difetto era stato segnalato. Ma `summary`, titoli di riga, glosse e frasi di chiusura
sono **apparato di sintesi**, e la sintesi comprime — e comprimendo perde per prima proprio la
qualificazione, che è la parte lunga della frase.

⚠️ **È il pattern del lotto 1C spostato di un posto.** Là il difetto era *il corpo cautela,
l'intestazione afferma*; qui è lo stesso movimento esteso a **ogni** superficie di sintesi
della nota, comprese quelle che nessuno rilegge perché non sembrano prosa: una cella di
tabella, una glossa di tre parole dopo un trattino.

**La regola che manca, e che è il candidato emendamento del §10:** *la cautela deve stare
accanto all'affermazione che sana, non altrove nella nota — e una riga di tabella, una glossa
o un riassunto sono affermazioni di fatto quanto il corpo.*

---

## 10. Emendamenti

**Approvati al gate intermedio e applicati alla chiusura**, con riga nel registro nello stesso
turno:

- **E36** — la nota cita la fonte che prescrive **ciò di cui parla**, non una fonte prescrittiva
  qualsiasi. ⚠️ Il registro dichiara che il difetto era nella **dettatura**, non
  nell'esecuzione: lo scostamento è stato dichiarato invece che applicato in silenzio.
- **E37** — la riconciliazione verticale è **un passo del ciclo di lotto**, non una promessa in
  tabella: chi porta una fonte prescrittiva riapre le note che quella fonte governa.
- **E38** — i lotti di manutenzione **non entrano nella serie della capacità** quando si
  rivedrà la fascia 25-35.

**Candidato nuovo, dal §9 — proposto, non approvato:**

- **La cautela sta accanto all'affermazione che sana.** Il passo 2-bis di §9.5 oggi prescrive
  di rileggere `title` e `summary` come note a sé; questo lotto mostra che **non basta**,
  perché il difetto si annida anche nelle celle delle tabelle e nelle glosse ai wikilink.
  ⚠️ La forma operativa non è «rileggere di più»: è **rileggere ogni superficie di sintesi
  cercando le affermazioni che il corpo ha già qualificato**, e verificare che la
  qualificazione sia arrivata anche lì.

---

## 11. I conteggi del vault a chiusura, da script

Generati **dopo** la nota-sessione nel journal, come E34 impone.

<!-- CONTEGGI DEL VAULT — generati da `06_operativo\qa\conta_stato.py` il 2026-08-19.
     Si incollano VERBATIM: non si ricompongono a mano, non si riscrivono in prosa. -->

| Grandezza | Valore |
|---|---|
| Note nel vault | **183** |
| di cui `_index` | 11 |
| di cui note-strumento del progetto | 10 |
| di cui note di diario (`sessione`, `daily`) | 4 |
| **di cui note di contenuto** | **158** |
| Note per cartella | areas 96 · entities 22 · data 22 · code 11 · docs 9 · projects 8 · workspace 7 · concepts 5 · self 1 · outputs 1 · sources 1 |
| Note per `type` | atomica 100 · conflitto 34 · entita 18 · hub 12 · index 11 · concetto 4 · sessione 4 |
| Questioni aperte (`type: conflitto`) | 34 |
| Grezzi in `sources\` | 160 |
| Grezzi citati da almeno una nota | **35** |
| Grezzi restanti | **125** |

**I grezzi restano 125 e i citati 35**: è la firma di un lotto di manutenzione, nessun grezzo
nuovo è entrato. Le note di contenuto passano da 153 a **158** — le cinque nate da fatti senza
padrone — e le note-strumento da 6 a **10**, perché `metodo_03` §7 vuole in `code\` la nota
che documenta ogni script del progetto, e oggi ne sono nati quattro.

⚠️ **La QA a perimetro vault resta a 128 ERRORI, esattamente com'era prima di R1**: sono tutti
l'incompletezza del vault — 125 grezzi non ancora canonizzati e 3 aree senza hub — e il fatto
che il numero non si sia mosso è la prova che il lotto non ha rotto nulla.

---

## 12. Che cosa il gate deve decidere

Il gate intermedio ha già risposto alla domanda che questo rapporto poneva nella prima
stesura: **il ripasso si fa pezzo per pezzo**, con E37 che lo rende un passo del ciclo invece
di una promessa in tabella, e una rete finale a fine corsa dimensionata su quello che le righe
avranno lasciato aperto.

Resta da decidere **una cosa sola, ed è il §9**: se la regola sulla cautela che non si propaga
vada scritta in `metodo_03` come emendamento, o se basti il passo 2-bis com'è. ⚠️ L'argomento a
favore dello scrivere: il pattern è stato trovato **al terzo giro**, cioè dopo che due giri di
revisione mirata lo avevano mancato — e lo hanno mancato perché guardavano il corpo. Un difetto
che sopravvive a due revisioni non è una disattenzione: è un punto cieco del metodo.

⚠️ **E l'ipotesi del debito storico resta da falsificare, non da ripetere.** Il 57,7 % misura
note scritte tutte **prima** che E29 esistesse. Diventerà dimostrato — o smentito — al primo
lotto canonizzato **sotto** E29: il rapporto del primo lotto del tema 2 dichiarerà il tasso di
riapertura, e sarà quel numero a dire se il debito era storico davvero.
