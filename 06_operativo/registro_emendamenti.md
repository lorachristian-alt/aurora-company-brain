# Registro degli emendamenti a `metodo_03`

> **Cos'è** · L'indice genealogico dei 46 emendamenti al manuale di canonizzazione: chi li
> ha approvati, quando, e dove vive oggi la regola. **È un indice, non una copia.**
> **Cosa NON contiene** · Il testo delle regole. Quello vive in
> `01_metodo\metodo_03_canonizzazione.md`, che ne resta l'unico padrone: qui c'è l'oggetto
> in una riga, quel tanto che basta a riconoscere l'emendamento, e il puntatore a dove
> leggerlo per intero.
> **Perché esiste** · Fino al 19/08/2026 la genealogia stava sparsa fra i rapporti di gate
> (§9 del gate S2 per E1-E17, §13 del rapporto 1A per E20-E25) e il decision log. Tre
> emendamenti non erano in nessuna tabella — **E18** e **E19**, nati al gate S2 dopo che il
> rapporto era già scritto, ed **E26**, approvato al gate del lotto 1B — e **E27 è nato
> fuori da un gate**. Senza un indice unico, un numero senza riga diventa un numero senza
> storia.

## Come si legge

- **Dove nasce** · l'occasione in cui il coordinatore l'ha approvato. Gli emendamenti li
  approva il coordinatore: **il gate è l'occasione tipica, non la condizione.**
- **Vive in** · la sezione di `metodo_03` dove sta la regola oggi.
- **Marcatore** · dice se nel testo del manuale compare la sigla `(Enn)`. Dove manca,
  l'emendamento è stato applicato riscrivendo il passaggio: è il caso dei refusi, che non
  lasciano cicatrice perché non c'è nulla da ricordare oltre al testo corretto.
- **Il perché** · il documento che porta la motivazione estesa e il caso che l'ha generata.

Sezioni e presenza dei marcatori sono verificate contro `metodo_03` da
`06_operativo\verifica_emendamenti.py`, non a occhio.

## I 44 emendamenti

| # | Data | Dove nasce | Tipo | Oggetto, in una riga | Vive in | Marc. | Il perché |
|---|---|---|---|---|---|---|---|
| **E1** | 17/08/2026 | gate S2 | regola nuova | `fonti` facoltativo per le note-strumento del progetto | §2.4 | sì | `rapporto_gate_s2.md` §9 · decision log 17/08 |
| **E2** | 17/08/2026 | gate S2 | regola nuova | riconciliazione incrociata dei numeri fra le fonti del lotto | §5.1-bis | sì | `rapporto_gate_s2.md` §9 |
| **E3** | 17/08/2026 | gate S2 | regola nuova | mai dichiarare un'assenza senza averla cercata su tutto `sources\` | §10, divieto 12-bis | sì | `rapporto_gate_s2.md` §9 |
| **E4** | 17/08/2026 | gate S2 | refuso | la grammatica `.xlsx` ammette `riga <n>` **e** `righe <n>-<m>` | §2.3 | no (refuso) | `rapporto_gate_s2.md` §9 |
| **E5** | 17/08/2026 | gate S2 | chiarimento | il locator è un prefisso della riga, non la riga intera | §2.3 | sì | `rapporto_gate_s2.md` §9 |
| **E6** | 17/08/2026 | gate S2 | regola nuova | verifica testuale solo per le citazioni di almeno cinque parole | §2.3 · §7.1 | sì | `rapporto_gate_s2.md` §9 |
| **E7** | 17/08/2026 | gate S2 | regola nuova | anche i valori **contati** si dichiarano, non solo quelli sommati | §5.4 · §7.1 | sì | `rapporto_gate_s2.md` §9 |
| **E8** | 17/08/2026 | gate S2 | chiarimento | la normalizzazione toglie il quoting delle mail e genera le varianti di data | §7.1 | sì | `rapporto_gate_s2.md` §9 |
| **E9** | 17/08/2026 | gate S2 | chiarimento | dopo le correzioni si **rigiudica**, non si rilancia solo la QA | §9.5, passo 5 | sì | `rapporto_gate_s2.md` §9 |
| **E10** | 17/08/2026 | gate S2 | chiarimento | il delimitatore del pacchetto per il giudice non può comparire nei grezzi | §7.1 | sì | `rapporto_gate_s2.md` §9 |
| **E11** | 17/08/2026 | gate S2 | chiarimento | la reciprocità si verifica sul **primo** hub di `related`, che è l'hub proprio | §2.1 · §7.2 | sì | `rapporto_gate_s2.md` §9 |
| **E12** | 17/08/2026 | gate S2 | chiarimento | il minimo di due wikilink conta anche quelli di `related` | §4.4 · §7.2 | sì | `rapporto_gate_s2.md` §9 |
| **E13** | 17/08/2026 | gate S2 | chiarimento | in perimetro di lotto, copertura `_index` e componente unica solo sulle cartelle toccate | §7 | sì | `rapporto_gate_s2.md` §9 |
| **E14** | 17/08/2026 | gate S2 | refuso | la coerenza interna si controlla dopo aver rimosso gli orari | §7.1 | sì | `rapporto_gate_s2.md` §9 |
| **E15** | 17/08/2026 | gate S2 | refuso | l'esempio compilato di §3.1 non corrispondeva al file: 49 `ALARM`, non 50 | §3.1 | no (refuso) | `rapporto_gate_s2.md` §9 |
| **E16** | 17/08/2026 | gate S2 | refuso | il locator dell'esempio `concetto-fefo` era fuori dalla grammatica `.csv` | §3.5 | no (refuso) | `rapporto_gate_s2.md` §9 |
| **E17** | 17/08/2026 | gate S2 | chiarimento | il budget di un lotto si misura sulle **note di contenuto** | §9.4 | sì | `rapporto_gate_s2.md` §9 |
| **E18** | 17/08/2026 | gate S2 · ⚠️ nato **durante** il gate, a rapporto già scritto | regola nuova | se una nota stabilisce una regola decisionale, il `summary` la enuncia | §2.1 | sì | decision log 17/08 — origine: la riserva del giudice su Q237 |
| **E19** | 17/08/2026 | gate S2 · ⚠️ nato **durante** il gate, a rapporto già scritto | refuso | il piè di pagina di un `.log` non era puntabile: `§piè di pagina`, `§intestazione` | §2.3 | sì | decision log 17/08 |
| **E20** | 18/08/2026 | gate della matrice | regola nuova | le note-strumento fuori dalla componente unica; l'esenzione è della **classe** | §2.4 · §7.0 · §7.2 | sì | `rapporto_lotto_1a.md` §13 · decision log 18/08 |
| **E21** | 18/08/2026 | gate del lotto 1A | regola nuova | il budget si controlla **prima** di scrivere; la soglia di spezzamento è **corretta da E28** | §9.4 | sì | `rapporto_lotto_1a.md` §13 |
| **E22** | 18/08/2026 | gate del lotto 1A | chiarimento | la data di verifica di un'assenza rimanda a `data_nota`, non si riscrive nel corpo | §10, divieto 12-bis | sì | `rapporto_lotto_1a.md` §13 |
| **E23** | 18/08/2026 | gate del lotto 1A | chiarimento | il marcatore di un valore derivato va **accanto al numero**, entro sessanta caratteri | §5.4 · §7.1 | sì | `rapporto_lotto_1a.md` §13 |
| **E24** | 18/08/2026 | gate del lotto 1A | chiarimento | date e orari si riportano nella grafia della fonte | §10, divieto 4-bis | sì | `rapporto_lotto_1a.md` §13 |
| **E25** | 18/08/2026 | gate del lotto 1A | regola nuova | non si anticipa una divergenza di cui una sola gamba è canonizzata | §10, divieto 9-bis | sì | `rapporto_lotto_1a.md` §13 |
| **E26** | 19/08/2026 | gate del lotto 1B | regola nuova | regola d'arresto del ri-giudizio: zero rilievi accolti, e comunque il terzo giro col pattern nominato | §9.5, passo 5 | sì | `rapporto_lotto_1b.md` appendice A |
| **E27** | 19/08/2026 | ⚠️ **FUORI da un gate — ordine diretto del coordinatore** | regola nuova | l'aggiornamento del passaggio di consegne è il **quinto gesto** del rituale di chiusura | §9.5, passo 8 | sì | decision log 19/08 · principio 5 della scaletta |
| **E28** | 19/08/2026 | ⚠️ **FUORI da un gate — ordine diretto del coordinatore**, in apertura del lotto 1C | chiarimento | **corregge la soglia di E21**: si spezza se la proiezione supera il +25 % **e** le 30 note; sotto le 30 si dichiara e si procede; oltre le 40 si spezza sempre | §9.4 | sì | decision log 19/08 · rapporto del lotto 1C |
| **E29** | 19/08/2026 | gate del lotto 1C | regola nuova | **riconciliazione VERTICALE**: chi tocca un CCP, una taratura o un limite cita la fonte che lo **prescrive**, con l'elenco delle fonti prescrittive come strumento | §5.1-bis | sì | `rapporto_lotto_1c.md` §6-bis · decision log 19/08 — undici note senza il manuale HACCP, quattro delle quali dichiaravano mancante ciò che il manuale contiene |
| **E30** | 19/08/2026 | gate del lotto 1C | chiarimento | `title` e `summary` si rileggono come note a sé **a ogni giro** di giudizio, non una volta sola | §9.5, passo 2-bis | sì | `rapporto_lotto_1c.md` §6-bis — al terzo giro sei rilievi su sette stavano ancora nell'intestazione |
| **E31** | 19/08/2026 | gate del lotto 1C | regola nuova | il budget di lotto è una **capacità** (25-35 note di contenuto), non una stima da densità; la fascia è **provvisoria**, da rivedere a dieci lotti chiusi | §9.4 | sì | `rapporto_lotto_1c.md` §9 — la densità varia del 147 %, le note per lotto del 50 % |
| **E32** | 19/08/2026 | gate del lotto 1C | regola nuova | il perimetro di lotto comprende anche le note che il lotto ha **modificato**, dichiarate in `qa\lotti\<lotto>_note.txt` | §7 | sì | decision log 19/08 — due difetti passati indenni alla QA di lotto in 1C |
| **E33** | 19/08/2026 | gate del lotto 1C | chiarimento | il pacchetto per lo strato di giudizio si genera **dopo** le correzioni pre-giudizio | §9.5, passo 2 | sì | decision log 19/08 — due rilievi su dodici, al primo giro di 1C, su testo che non esisteva più |
| **E34** | 19/08/2026 | ⚠️ **FUORI da un gate — ordine diretto del coordinatore** | regola nuova | il ciclo di chiusura acquista la **nota-sessione** nel journal di `workspace\`, e il blocco dei conteggi di `conta_stato.py` si genera **dopo** di essa, ultimo numero prima del commit | §9.5, passo 5-bis | sì | decision log 19/08 · prompt della manutenzione R1 — il blocco del lotto 1C dichiara 172 note, `qa_all.py` dello stesso giorno 173: la differenza è la nota di diario, scritta dopo il conteggio |
| **E35** | 19/08/2026 | ⚠️ **FUORI da un gate — ordine diretto del coordinatore** | regola nuova | esiste il **LOTTO DI MANUTENZIONE**: ripara note già scritte invece di canonizzare grezzi nuovi — perimetro di sole note con la guardia sullo zero grezzi, elenco generato da script, niente capacità 25-35, tre numeri nel rapporto | §7 · §9.4-bis | sì | decision log 19/08 · prompt della manutenzione R1 — il gate del lotto 1C apre R1, la riconciliazione verticale, che è il primo lotto di questa specie |
| **E36** | 19/08/2026 | ⚠️ **gate intermedio del lotto R1** | chiarimento | **corregge la forma di E29**: la nota cita la fonte che prescrive **ciò di cui parla**, non una fonte prescrittiva qualsiasi | §5.1-bis | sì | `rapporto_lotto_r1.md` §2 · decision log 19/08 — la forma generica lasciava fuori 26 note su 71, cioè quelle che avevano generato il lotto. ⚠️ **Il difetto era nella DETTATURA del coordinatore, non nell'esecuzione**: la sessione ha dichiarato lo scostamento invece di applicarlo in silenzio, ed è ciò che §4 del prompt dei lotti chiede — uno scostamento dichiarato è un dato, uno taciuto è un guasto |
| **E37** | 19/08/2026 | gate intermedio del lotto R1 | regola nuova | la **riconciliazione verticale è un passo del ciclo di lotto**, non una promessa in tabella: chi porta una fonte prescrittiva riapre le note che quella fonte governa, e il rapporto dichiara quante ne ha riaperte e quante corrette | §9.5, passo 5-ter | sì | `rapporto_lotto_r1.md` §11 · decision log 19/08 — una riga di tracciamento ricorda ma non scatta da sola (§4.29). Le note riaperte non contano nella capacità; se superano le nuove, il lotto si spezza |
| **E38** | 19/08/2026 | gate intermedio del lotto R1 | chiarimento | i **lotti di manutenzione non entrano nella serie della capacità** quando a dieci lotti chiusi si rivedrà la fascia 25-35 di E31 | §9.4 | sì | decision log 19/08 — mettere insieme due grandezze che misurano cose diverse è ciò che ha prodotto le 903 note del calcolo lineare |
| **E39** | 19/08/2026 | gate del lotto R1 | regola nuova | **LA CAUTELA SI PROPAGA**: apposta una qualificazione a un'affermazione, la stessa qualificazione va portata su **tutte le altre occorrenze di quell'affermazione** dentro la nota. Estende E30, che resta com'è | §9.5, passo 2-bis | sì | `rapporto_lotto_r1.md` §9 · decision log 19/08 — il pattern con cui R1 si è chiuso al terzo giro (E26) **dopo che due giri di revisione mirata lo avevano mancato**: un difetto che sopravvive a due revisioni non è una disattenzione, è un punto cieco del metodo. ⚠️ **Il caso che la genera**: tre giudici indipendenti, a contesto pulito, su fette diverse, hanno descritto la stessa classe con tre parole diverse. ⚠️ **La forma conta più della regola** — il gesto parte dall'AFFERMAZIONE, non dalla superficie, e non è «rileggere di più»; l'elenco delle superfici resta **aperto**, perché chiuderlo ricreerebbe il difetto di E30 |
| **E40** | 19/08/2026 | gate del lotto R1 | regola nuova | **LA PRESCRIZIONE SI LINKA, NON SI RICOPIA**: si linka la nota padrona della prescrizione, e se non esiste la si crea; il testo prescrittivo non si ricopia dentro la nota | §5.1-bis | sì | `rapporto_lotto_r1.md` §11 · decision log 19/08 — è **il rovescio di E29/E36** e la scoperta più preziosa di R1: agganciando le note alla prescrizione il lotto ha prodotto **17 doppie padrone**, e due prescrizioni erano ricopiate **senza avere alcun padrone**. Per un tratto il vault ha avuto più copie della stessa prescrizione di prima. ⚠️ **Senza E40, E37 è una macchina che produce duplicati**: chi riapre le note che una fonte governa ricopia per gesto naturale. Le due prescrizioni più duplicate — seconda firma e CCP4 — reggono le conclusioni più forti del vault: **se una copia diverge, diverge un'accusa** |
| **E41** | 20/08/2026 | gate del lotto 2A | regola nuova | **OGNI LOTTO DICHIARA I DUE TASSI**, da `misura_due_tassi.py`, tenuti separati: riapertura (il **debito** ereditato) e difetto di produzione (il **metodo**) | §9.5, passo 5-ter | sì | `rapporto_lotto_02a.md` §7 · decision log 20/08 — **una misura sola è un aneddoto: quello che conta è la serie**, ed è la serie che a fine corsa dirà quanto il metodo produce il difetto invece di ereditarlo, con un denominatore vero. Il primo punto è **3,3 % contro il 57,7 %** di R1, stesso criterio, entrambi da script. ⚠️ **Il caso residuo si dichiara col suo nome e non si aggiusta**: aggiungere una fonte per portare il tasso a zero truccherebbe il numero che la misura esiste per produrre. ⚠️ Ne discende una scelta di pianificazione: la rete finale **non è un secondo passaggio sul vault**, è la chiusura delle righe di tracciamento di E37 |
| **E42** | 20/08/2026 | gate del lotto 2A | chiarimento | **corregge il QUANDO di E39**: la propagazione della cautela si fa **nello stesso turno della qualificazione**, non a fine giro | §9.5, passo 2-bis | sì | `rapporto_lotto_02a.md` §6 · decision log 20/08 — E39 diceva *che cosa* fare e non *quando*, e «quando» non è ovvio: **chi corregge su rilievo sta pensando al rilievo, non alla nota intera**. Il caso: in 2A una cautela apposta al corpo per chiudere un rilievo del giudice **non è arrivata al summary nel giro stesso in cui veniva scritta**. È la conferma meccanica di E30 — l'intestazione si corregge per ultima — e rende la ricerca delle altre occorrenze **parte del gesto di qualificare**. E39 resta col suo numero (§4.26) |
| **E43** | 20/08/2026 | gate del lotto 2A | regola nuova | **CHI DICHIARA UN'ASSENZA LASCIA L'ARTEFATTO DELLA RICERCA** in `06_operativo\ricerche_assenza\`, la nota vi rimanda, e la QA verifica che l'artefatto esista | §10, divieto 12-bis · §7.3 | sì | `rapporto_lotto_02a.md` §5.4 · decision log 20/08 — ⚠️ **E3 è stato pagato QUATTRO volte in cinque lotti**: `PRP-09` nel pilota, l'ossigeno residuo in 1A, **due note in 2A** dove la formula di attestazione era scritta senza che la ricerca fosse stata fatta. È §4.20 al rovescio: **quando una regola viene violata sempre, il difetto non è nella diligenza di chi la applica ma nel fatto che nessuno può verificarla**. ⚠️ Nessuno script può verificare il *contenuto* di un'assenza; la **procedura** sì, e tanto basta a chiudere il difetto |
| **E44** | 20/08/2026 | gate del lotto 2A | regola nuova | **generalizza E34 a TUTTE le misure di chiusura** — QA di lotto, QA a perimetro vault, collaudo, `verifica_matrice_lotti`, `conta_tracciamento` — che si eseguono **dopo l'ultima scrittura**, e ogni numero dichiarato **porta l'ora della propria misura** | §9.5, passo 5-bis | sì | `rapporto_lotto_02a.md` §9 · decision log 20/08 — in 2A il report della QA a perimetro vault portava le **19:34** con 214 note e 126 errori, mentre il lotto si è chiuso alle **22:01** con 217 note e 125 errori. **Nessuno dei due è sbagliato: sono due istanti**, ma solo uno è quello che il rapporto ha il diritto di dichiarare. Stessa classe del 172/173 che E34 ha chiuso su `conta_stato`, e lo stesso giorno riapparsa fra due misure della QA di lotto (40 avvisi contro 41): **seconda osservazione, quindi si scrive** |
| **E45** | 21/08/2026 | gate del lotto 2B | chiarimento | **«sessione diversa» significa CONTESTO diverso, non mano diversa**: il revisore del passo 3 può essere un **subagente a contesto pulito**, e **deve** ricevere il canone e la tabella alias; lo strato di giudizio del passo 5 non lo riceve mai | §9.5, passo 3 | sì | decision log 21/08 — ⚠️ **due lotti fermati dallo stesso dubbio**: R1 chiese l'autorizzazione, **2B si è fermato dichiarando il passo scoperto**, perché la risposta viveva solo nel testo incollato di un gate e non nel manuale. Il perimetro è garantito dalla **fisica del contesto**, non da chi lancia. ⚠️ E le due fughe di canone del progetto **non sono nate dal revisore**: sono nate da chi scriveva le note, e nel pilota da un'informazione del report del revisore ricopiata in una nota senza grezzo. ⚠️ Il canone **non vive in `03_valutazione\`** — sta in `01_metodo\` — e la guardia su `03_valutazione\` riguarda l'**esame**, non il canone: due perimetri, due ragioni |
| **E46** | 21/08/2026 | gate del lotto 2B | chiarimento | **i due tassi si dichiarano col nome del dominio su cui sono misurati**, e le scoperture verso fonti di altri domini si contano a parte. Lo script non si allarga | §9.5, passo 5-ter, accanto a E41 | sì | `rapporto_lotto_02b.md` §9.1 · decision log 20/08 — ⚠️ **il caso è istruttivo perché nessuna delle due misure sbagliava**: nel lotto 2B `misura_due_tassi.py` dava **0,0 % su 27 note** nel dominio `acqua`, e lo strato di giudizio trovava **due note** scoperte verso il **manuale HACCP**, che prescrive lo zoning dei tamponi e la frequenza di potabilità. Lo script guarda il dominio dichiarato, il giudice guarda tutte le fonti del pacchetto: **due misure vere di cose diverse**, e il nome del numero prometteva di più. ⚠️ Allargare lo script vorrebbe dire dichiarare un dominio per ognuna delle **36** fonti prescrittive: il lavoro fatto due volte |

## Le anomalie di genealogia, dette per nome

1. **E18 ed E19 non sono nella tabella del rapporto S2** perché sono nati *durante* il
   gate, dopo che il rapporto era stato scritto: il decision log del 17/08 ne conta
   «diciannove», la tabella ne elenca diciassette. Nessuno dei due è mai stato in
   discussione — mancava solo la riga.
2. **E26 non ha una riga di registro** da nessuna parte: il rapporto del lotto 1B lo cita
   nell'appendice A come obbligo già approvato, ma quel gate non ha prodotto una tabella
   di emendamenti come avevano fatto S2 e 1A.
3. **E27, E28, E34 ed E35 sono nati fuori da un gate**, su ordine diretto del coordinatore
   del 19/08/2026, e sono approvati a pieno titolo. ⚠️ **E36-E38 nascono invece a un GATE
   INTERMEDIO**, specie nuova per questo registro: un gate che non approva un lotto ma lo
   **autorizza a finire**, perché il ciclo di giudizio non era ancora girato. La colonna «dove
   nasce» lo dice, perché fra un anno «gate del lotto R1» e «gate intermedio del lotto R1» non
   sembrino la stessa occasione. ⚠️ **E45 ed E46 nascono al gate del lotto 2B**, e sono
   entrambi **chiarimenti, non regole nuove**: E45 dice che cosa «sessione diversa» ha sempre
   significato, E46 dice che cosa un numero già in uso non copre. ⚠️ **Un chiarimento si scrive
   quando l'ambiguità ha già fermato qualcuno**, ed E45 ne aveva fermati **due**. ⚠️ **E41-E44
   nascono al gate del lotto 2A**, un gate di
   merito come quello di R1, e sono la prima volta che quattro emendamenti escono da un solo
   gate. ⚠️ **Dal 19/08/2026 la distinzione non è più teorica: E39 ed
   E40 nascono al GATE del lotto R1**, quello che ne ha approvato il merito, e stanno nella
   stessa giornata di E36-E38 che nascevano al gate intermedio dello stesso lotto. Due
   occasioni diverse, stesso lotto, stesso giorno: è precisamente il caso che questa nota era
   stata scritta per rendere leggibile. ⚠️ E34 ed E35 arrivano per una via ancora
   diversa: sono stati **dettati nel prompt della sessione di manutenzione**, cioè
   nell'artefatto che istruisce la sessione (§4.27 del passaggio di consegne), e la sessione li
   ha applicati come primo adempimento — non li ha decisi. ⚠️ **E29-E33 invece sono del gate del lotto
   1C**, lo stesso giorno: la vicinanza di data non li rende la stessa cosa, e la colonna
   «dove nasce» è l'unico posto in cui la differenza resta scritta. La convenzione del progetto è **«gli
   emendamenti li approva il coordinatore»**, non «solo ai gate»: sta scritto qui perché fra
   un anno un numero senza gate accanto non sembri un numero senza padre.
4. **Tre emendamenti non hanno marcatore inline, e non è un disallineamento: sono i refusi**
   (E4, E15, E16). Un refuso **corregge un testo sbagliato**, non introduce una regola da
   ricordare, e il marcatore `(Enn)` serve a chi rilegge per capire *perché* una regola è
   scritta così. La colonna «Marc.» li segna `no (refuso)`, e `verifica_emendamenti.py`
   **pretende che ogni emendamento senza marcatore sia un refuso**: una **regola nuova** o un
   **chiarimento** senza marcatore sarebbe invece un difetto vero.
   ⚠️ Il controllo vale in **una direzione sola**, ed è deliberato: **E14 ed E19 sono refusi e
   il marcatore ce l'hanno**, perché correggono un passaggio che senza spiegazione tornerebbe
   a sembrare sbagliato. Pretendere che nessun refuso lo porti farebbe fallire il controllo su
   due emendamenti corretti.
5. **E3 era senza marcatore e non è un refuso: il marcatore gliel'ha dato questo controllo**
   (19/08/2026). Nell'elenco iniziale sembrava il quarto dei refusi; è invece una **regola
   nuova** — il divieto di dichiarare un'assenza senza averla cercata — e §10.12-bis la
   portava senza sigla, pur portando quella di E22, che di quel divieto è solo il chiarimento
   sulla data. Non è un marcatore posticcio: è la stessa ratio che esenta i refusi, applicata
   nell'altro verso. **È il primo difetto che il registro ha trovato invece di documentare.**

## Regola di manutenzione

Ogni emendamento nuovo prende **una riga qui, nello stesso turno** in cui entra in
`metodo_03`. Se nasce a un gate, la motivazione estesa resta nel rapporto di quel gate; se
nasce fuori, la porta il decision log. **Questo file non è il padrone di nessuna regola:**
se una riga qui diverge da `metodo_03`, vince `metodo_03` e la riga si corregge nello
stesso turno.
