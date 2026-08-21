# Rapporto del lotto 2B — l'autocontrollo analitico

> **Che cos'è** · Il rapporto del **lotto 2B**, il secondo del tema 2 e il **settimo lotto di
> canonizzazione** del progetto. Tre grezzi: il registro dei tamponi di superficie, il piano
> di autocontrollo dell'acqua potabile, l'autocontrollo dello scarico in fognatura.
> **Per chi** · Per il coordinatore, al gate. Ogni numero viene da uno script, e da **E44**
> ogni numero porta l'ora della propria misura.
> **Chiuso il** · **20/08/2026 per la scrittura**, e il 21/08 dopo mezzanotte per gli
> adempimenti di registro. ⚠️ **Il lotto sta a cavallo della mezzanotte, come 2A**: le note
> portano `data_nota: 2026-08-20`, la nota-sessione porta **2026-08-21** perché è stata scritta
> dopo, e in `qa\` ci sono due cartelle datate. **Nessuna data è stata ritoccata per farle
> combaciare**: sono quelle vere, e chi al gate finale confronterà le `data_nota` con la data
> dichiarata del lotto troverà due giorni e ora sa perché.

---

## 1. Il perimetro, e perché il lotto si è spezzato prima di scrivere

⚠️ **Il lotto 2B è arrivato con cinque grezzi e ne ha canonizzati tre.** Lo spezzamento è
stato deciso **in apertura, prima di scrivere una riga**, ed è l'applicazione di **E28**: il
conteggio dei fatti (E21) proiettava **oltre le 40 note**, e sopra 40 la regola non lascia
scelta.

**Dove passa il taglio, e perché lì.** Da una parte i tre registri che portano **risultati di
misura con un limite** — tamponi, acqua potabile, acque reflue. Dall'altra il **sistema
prescrittivo** degli allergeni e la formazione che lo insegna, che vanno a **2B-bis**.

⚠️ **La ragione non è la dimensione, è la riconciliazione verticale.** La scheda allergeni è
una **fonte prescrittiva** — matrice, sequenze di produzione, tipi di lavaggio, rework,
etichettatura precauzionale, stoccaggio — e apre **da sola un dominio** di E37. Tenerla nello
stesso lotto del piano dell'acqua avrebbe messo **due riconciliazioni verticali dentro un
lotto solo**, e nessuna delle due sarebbe stata fatta per intero.

<!-- PERIMETRO DEL LOTTO — generato da `06_operativo\conta_perimetro_lotto.py`,
     misurato il 21/08/2026 alle 00:00:52-00:01:02, dopo l'ultima scrittura (E44).
     Si incolla VERBATIM: i numeri non si ricompongono a mano. -->

| Voce | Valore |
|---|---|
| Specie del lotto | **lotto di canonizzazione** |
| Grezzi nell'elenco | **3** |
| Note **candidate** dallo script di apertura | **5** |
| Note **toccate** in corso di lotto (E32) | **9** |
| Note **nate** nel lotto | **27** — 27 contenuto |
| **Note controllate in tutto** | **41** |
| Esito della suite di lotto | **0 ERRORI, 23 AVVISI** |

**La capacità di E31 è rispettata**: 27 note di contenuto contro una capacità di 25-35, e le
riaperte non contano nella serie perché sono riparazioni.

---

## 2. L'obbligo principale: T72, chiusa da un dato e non da una decisione

⚠️ **È la prima riga di tracciamento del progetto chiusa da un lotto successivo con un
dato.** Il lotto 2A aveva lasciato aperto il criterio di accettazione del risciacquo CIP
perché `IO-05` lo esprime come **scarto dall'acqua di rete** e il log non registra mai l'acqua
di rete. Quel valore era in un grezzo di questo lotto.

| | |
|---|---|
| Conducibilità dell'acqua di rete | **486 µS/cm**, rete d'ingresso, 15/01/2026 |
| Limite di accettazione che ne discende | **536 µS/cm** *(somma di 486 e 50)* |
| Cicli sopra il limite, **ultima** lettura del risciacquo | **18 su 28** *(contati sul log)* |
| Cicli sopra il limite, lettura **più alta** | **24 su 28** *(contati sul log)* |

⚠️ **Il numero non si è scritto da solo, e porta tre condizioni dichiarate**:

1. **la risoluzione del log è più grossolana della tolleranza del criterio** — scalini da 100
   µS/cm contro un margine ammesso di 50: il verdetto regge sui cicli molto sopra il limite,
   non su quelli al bordo;
2. **il termine di paragone è una misura sola, di gennaio**, contro un log di maggio;
3. **quale acqua sia «di rete» non è indifferente** — il registro descrive l'uscita
   dell'addolcitore (512 µS/cm) come l'acqua destinata anche al CIP, e con quella il limite
   sarebbe 562 *(somma di 512 e 50)*. **I conteggi non cambiano**, perché fra i due limiti il
   log non ha letture.

⚠️ **La nota di 2A che dichiarava il criterio «non verificabile» è stata riaperta e
corretta**, non lasciata com'era: è il caso in cui una riga di tracciamento si chiude
davvero, invece di essere dichiarata chiusa.

---

## 3. I due tassi (E41) — la seconda misura della serie

Da `misura_due_tassi.py`, **ripreso dopo l'ultima scrittura il 21/08/2026 alle 00:01:12**
(E44), dominio `acqua`:

| Tasso | Che cosa misura | Lotto 2B |
|---|---|---|
| **Riapertura** | il **DEBITO** ereditato: note vecchie riaperte / corrette | **60,0 %** — 3 corrette su 5 riaperte |
| **Difetto di produzione** | il **METODO**: note nate nel lotto che parlano del dominio senza la fonte che lo governa | **0,0 %** — 0 su 27 |

⚠️ **La prima misura, presa alle 23:10:30, dava 0 su 26**: le note erano ventisei, e la
ventisettesima è nata dal secondo giro di giudizio. **Il tasso non cambia, il denominatore
sì** — ed è la ragione per cui E44 chiede l'ora accanto al numero.

**La serie, che è la cosa che conta** — e da **E46** ogni punto porta il **dominio** su cui è
stato misurato, perché lo script ne controlla uno per volta:

| Misura | Dominio misurato | Riapertura (debito) | Difetto di produzione (metodo) |
|---|---|---|---|
| **R1** (manutenzione, 19/08) | perimetro CCP e tarature | — | **57,7 %** |
| **2A** (20/08) | `cip` | 40,0 % (4/10) | **3,3 %** (1/30) |
| **2B** (21/08, 00:01) | `acqua` | **60,0 %** (3/5) | **0,0 %** (0/27) |

⚠️ **L'etichetta non è decorazione: è la correzione di ciò che questo lotto ha scoperto.** Lo
0,0 % vale sul dominio `acqua`, e nello stesso lotto il giudizio ha trovato **due note
scoperte verso il manuale HACCP**, che è una fonte prescrittiva di un altro dominio. **Le due
misure sono entrambe vere e misurano cose diverse** — vedi §9.1, approvato come **E46** al
gate del 21/08.

⚠️ **Il secondo tasso è il numero che decide, ed è il terzo punto della serie.** Il 57,7 % di
R1 non era il tasso con cui il metodo sbaglia: era il residuo di note scritte quando il metodo
era più povero. Due lotti consecutivi sotto il 4 % lo confermano, e il criterio scritto al
gate di R1 — «due lotti prima di decidere» — è ora **soddisfatto**.

⚠️ **Il primo tasso sale, e non è un peggioramento.** 60 % contro il 40 % di 2A significa che
delle cinque note riaperte tre andavano corrette: **su denominatori piccoli il tasso di
riapertura oscilla**, e con cinque note un caso in più vale venti punti. **Una misura sola è
un aneddoto**: è la serie che conta, e su questa grandezza la serie è ancora corta.

**Le due riaperte NON corrette** sono chiuse dichiarando che la fonte non le governa: il piano
dell'acqua non prescrive i parametri di fase del CIP né le condizioni d'uso del detergente,
che restano governati da `IO-05` e dalla scheda di sicurezza.

---

## 4. La riconciliazione verticale (E37), e il dominio nuovo

`candidate_r1.py` ha ricevuto **due domini nuovi** — `acqua` e `allergeni` — dichiarati nel
codice come prescrive lo strumento, con le fonti che li governano e le espressioni che li
riconoscono.

| Dominio | Fonte che lo governa | Note candidate | Esito |
|---|---|---|---|
| `acqua` | il piano di autocontrollo dell'acqua potabile | **5** | 3 corrette · 2 chiuse dichiarando |
| `allergeni` | la scheda allergeni | **5** | **rinviate a 2B-bis** col lotto |

⚠️ **Il dominio `allergeni` è già dichiarato e già misurato**, ma non è stato eseguito: la sua
fonte non è entrata nel vault con questo lotto. È il modo corretto in cui uno spezzamento
lascia il lavoro: **misurato e consegnato**, non dimenticato.

---

## 5. I giri di giudizio

⚠️ **Prima dei numeri, un difetto di processo che ho commesso io e che va detto.** Il
pacchetto per il giudizio si genera **dopo** la QA e dopo la rilettura (E33). Il primo l'ho
generato al primo verde della QA, e **poi ho fatto il lavoro di T72**: la nota del criterio è
nata dopo, e altre sono cambiate. Me ne sono accorto prima che il giudice finisse, ho
rigenerato il pacchetto e **il giudizio che conta ha letto il testo corrente**. Ma il primo
pacchetto è stato generato troppo presto, ed è esattamente il difetto per cui E33 esiste.
**La lezione non è "rigenerare": è che l'ordine dei passi non ammette un lavoro grosso in
mezzo.**

### 5.1 Primo giro — 8 rilievi accolti su 31 note

| Esito | Note |
|---|---|
| `pulita` | **23** |
| `afferma_oltre` | **8** |
| `fonte_inutile` · `entrambi` | 0 |

**Tutti e otto accolti, nessuno respinto.** Sono di tre specie:

| Specie | Quanti | Esempio |
|---|---|---|
| **l'attributo che la fonte non dà** | 3 | «uno snack alla paprika, **che è un prodotto in sviluppo**» · «la sanificazione parte dall'**avviso telefonico**» |
| **un «unico» che unico non è** | 3 | «l'**unico** punto del registro col limite a 500» — ce n'è un secondo; «aprile e maggio le trovano in **zona 1**» — quella del 13/04 è in zona 3 |
| **un'affermazione fuori dalle fonti citate** | 2 | «l'acido peracetico è il sanificante dell'ultima fase del ciclo CIP» — vero, ma lo dice `IO-05`, che non è fra le fonti di quella nota |

⚠️ **La seconda specie è quella che mi preoccupa di più**, e non compare in nessun
emendamento: **«l'unico», «il primo», «nessun altro» sono affermazioni universali su un
insieme**, e per verificarle bisogna guardare tutto l'insieme, non la riga che le suggerisce.
Sono scritte con la stessa leggerezza di un aggettivo.

**Le lacune di copertura**: 13 segnalate, **4 accolte**. Le due che contano sono vere
riconciliazioni verticali mancate: il **manuale HACCP prescrive lo zoning** dei tamponi (e ne
dichiara **quattro** zone contro le tre del registro) e la **frequenza semestrale** della
verifica di potabilità. Entrambe le note ora citano il manuale. Le altre nove sono respinte
una per una: il giudice non conosce il grafo e segnala come lacuna ciò che ha una padrona
altrove.

### 5.2 Secondo giro — 2 rilievi accolti su 35 note

| Esito | Note |
|---|---|
| `pulita` | **33** |
| `afferma_oltre` | **2** |

Entrambi accolti, ed entrambi **della prima specie**: un'affermazione sul contenuto di un
documento che non è fra le fonti della nota, e — la più istruttiva — «**nessuno dei due
documenti cita l'altro: il collegamento è un'inferenza di questo vault**», che era **falsa**:
il manuale nomina `MOD-QA-19` e lo lega al piano di zoning. ⚠️ **Avevo dichiarato un'inferenza
per prudenza, e la prudenza stessa era un'affermazione non verificata.**

⚠️ **E il secondo giro ha prodotto due lacune di copertura che valgono più dei rilievi:**

1. **La sigla che mancava c'era.** La nota del modulo dichiarava ignoto il codice del registro
   delle non conformità; quel registro **lo dichiara nel proprio titolo**, `MOD-QA-18` rev. 3.
   La riga di tracciamento **T77 si chiude per intero**.
2. **Una positività a Listeria che un registro ha e l'altro no.** `NC-2026-034` del 24/02/2026
   — gravità **critica** — non ha nessuna corrispondenza nel registro dei tamponi. È nata una
   questione aperta e la riga **T82**. ⚠️ **Chi guardasse il solo `MOD-QA-19`, come farebbe un
   auditor, vedrebbe una positività nell'anno invece di due.**

### 5.3 Terzo giro — 3 rilievi accolti su 36 note, e il ciclo si ferma qui

| Esito | Note |
|---|---|
| `pulita` | **33** |
| `afferma_oltre` | **3** |

**Tutti e tre accolti**, più una segnalazione accessoria: una **citazione troncata** nel blocco
delle fonti, che tagliava via il nome del prodotto usato per sanificare e **una sigla di non
conformità** — `NC-26-041` — che il corpo della nota non riportava affatto. Corretta.

⚠️ **Il ciclo NON converge, e per E26 non si fa un quarto giro: si nomina il pattern.**

### 5.4 Il pattern: **l'affermazione universale verificata sul sottoinsieme che l'ha suggerita**

I tre rilievi del terzo giro, letti insieme ai cinque della stessa famiglia nei due giri
precedenti, sono **una specie sola**:

| La frase | Il suo dominio di verifica reale |
|---|---|
| «i quattro valori **più alti dell'anno** cadono tutti nello stesso giorno» | tutte le campagne dell'anno — e quella di maggio li supera tutti |
| «l'**unica** non conformità **dell'archivio** che riguarda una persona» | tutti i registri — e quello delle non conformità ne porta un'altra |
| «la linea lavora su tre turni — **T1 06:00-14:00**, …» | una fonte che dia quegli orari, e fra quelle citate non c'è |
| «l'**unico** punto del registro col limite a 500» *(primo giro)* | tutte le righe del registro — ce n'è un secondo |
| «**nessuno dei due** documenti cita l'altro» *(secondo giro)* | entrambi i documenti — e uno cita l'altro |

⚠️ **Perché si rigenera, ed è meccanico.** Scrivere una nota significa **leggere a fondo un
documento**; un superlativo o un'esclusiva sembra il riassunto di quella lettura, e si scrive
con la leggerezza di un aggettivo. **Ma «l'unico» non è un aggettivo: è un quantificatore
universale**, e le sue condizioni di verità stanno **fuori dal testo che si ha davanti** — in
tutte le righe che non si stanno guardando, o in tutti i documenti che non si stanno citando.
Il gesto che lo produce è lo stesso che produce una buona sintesi: **la specie non si elimina
scrivendo meglio, perché nasce dallo scrivere bene.**

⚠️ **Ed è una FAMIGLIA PIÙ GRANDE di quella nominata al gate di 2A**, non la stessa. «L'attributo
che la fonte non dà» è il caso in cui manca **una** fonte; questo è il caso in cui il dominio di
verifica è **un insieme intero** che nessuna fonte singola contiene. Il primo si ripara citando
un documento in più; il secondo **non si ripara citando**: si ripara **restringendo la frase al
perimetro che si è davvero guardato** — che è esattamente ciò che le tre correzioni hanno fatto,
tutte e tre sostituendo «dell'archivio» con «di questo registro».

**La forma che avrebbe come emendamento** — e che NON si propone adesso, perché è la prima volta
che questa specie viene nominata e vale E28: *un'affermazione di unicità, primato o massimo si
scrive col perimetro su cui è stata verificata, e quel perimetro non è mai più largo delle fonti
della nota.*

> ⚠️ **Aggiornamento del 21/08, dopo il completamento del ciclo.** La revisione col canone ha
> trovato **dieci** casi di questa specie che erano sopravvissuti ai tre giri, e il ri-giudizio
> che è seguito ne ha trovati altri **otto preesistenti più tre che avevo introdotto io
> correggendo** — vedi §10.5. **L'evidenza è ora molto più forte di quando la riga è stata
> scritta.**
>
> ⚠️ **Ma il criterio di scioglimento è stato fissato al gate del 21/08 e dice «al terzo giro di
> giudizio di 2B-bis»: non lo si anticipa.** Rileggerlo adesso, a evidenza vista, sarebbe
> esattamente ciò che §4.43 del passaggio di consegne è nato per impedire — e le sue due
> condizioni qui **non sono soddisfatte**, perché la distinzione su cui poggerebbe la rilettura
> (il giudizio post-revisione conta come «giro»?) **non era consacrata prima dell'esito**.
> **L'evidenza si consegna al coordinatore; il criterio resta quello scritto.**

### 5.5 Il verdetto sulla vigilanza aperta al gate di 2A

Il gate di 2A aveva parcheggiato «l'attributo che la fonte non dà» **col criterio scritto in
anticipo**: se la classe ricompare **al terzo giro** di giudizio del prossimo lotto diventa
emendamento, altrimenti la riga si chiude.

⚠️ **Il verdetto è: la riga si chiude**, e la lettura va data per intero perché è al limite.

- Al **primo** giro la classe c'era, tre volte su otto. Ma al primo giro tutto c'è: è il primo
  giro, ed è la ragione per cui il criterio era stato fissato al terzo.
- Al **terzo** giro, dei tre rilievi accolti, **due sono della specie nuova** e uno solo —
  gli orari dei turni — è della vecchia. ⚠️ **E quell'uno sta in una nota che questo lotto NON
  ha scritto**: `macchina-linea-1` viene da un lotto precedente, e il lotto l'ha soltanto
  toccata.
- **È debito, non produzione**, ed è esattamente la distinzione che E41 esiste per misurare.
  Applicare il criterio alla lettera vorrebbe dire far diventare emendamento una classe che al
  terzo giro **non si è più prodotta**, sulla base di un difetto ereditato.

**Quindi la vigilanza si chiude**, e al suo posto il gate riceve la specie nuova di §5.4.

## 6. Che cosa il lotto ha trovato, oltre ai suoi tre file

⚠️ **Tre riconciliazioni orizzontali (E2) che nessuno dei tre grezzi contiene**, e sono il
guadagno maggiore del lotto:

| Che cosa | Come è emersa |
|---|---|
| **Il tampone delle ganasce dell'11/05 e il guasto della valvola azoto del 10/05** sono lo stesso fatto visto da due registri | il registro dei tamponi annota «prelievo post intervento manutenzione valvola azoto del 10/05»; il vault aveva già il fermo di 3 h 40 min di quel giorno |
| **Il ricambio Pakmatic previsto per il 15/05 è stato montato il 15/05** | il piano di manutenzione lo dava «in arrivo 15/05»; il tampone del 25/05 annota «ricambio originale montato 15/05» — una previsione d'archivio confermata da un secondo registro |
| **La promo del cliente principale compare come causa in due funzioni diverse** | la qualità annota «produzione spinta promo Tosano meno tempo x sanificazione»; la manutenzione motivava già il rinvio di voci programmate con la stessa causa |

⚠️ **E una riconciliazione verticale che scioglie un dubbio scritto in un registro.** Chiudendo
`NC-ACQ-26-01` il compilatore si corregge da solo sul modulo da usare e lascia scritto
«verificare modulo giusto con Marchetti»: il **manuale HACCP** assegna `MOD-QA-31` ai reclami,
e conferma che aveva ragione. **Il registro non sa che cosa sia quel modulo, il manuale non sa
che qualcuno se lo stia chiedendo**: la risposta esiste solo perché stanno nello stesso
archivio. Resta ignota la sigla del registro delle non conformità, che nessuna fonte nomina —
e non è stata dedotta.

---

## 7. E43 alla sua prima esecuzione, e che cosa ha impedito

⚠️ **La regola è nata al gate di stamattina e in questo lotto ha fatto esattamente il suo
mestiere.** La nota della conducibilità stava per affermare che l'acqua di rete «è misurata una
volta sola in tutto l'archivio». La ricerca su tutto `sources\` — 155 file letti, 5 ciechi — ha
trovato il termine in **altri sei documenti** e ha chiuso in errore, come deve: l'assenza,
scritta così, non si poteva dichiarare.

**Che cosa è successo poi, ed è il punto.** Leggendo le sei occorrenze una per una:

- nessuna di esse **misura** la conducibilità dell'acqua di rete, quindi l'affermazione si è
  potuta riscrivere in forma vera, **col rimando all'artefatto** che la rende verificabile;
- ma una di esse ha fatto emergere un fatto che il lotto non avrebbe visto: il registro delle
  non conformità porta un caso di **risciacquo fuori soglia** sullo stesso criterio, aperto
  mesi prima del log di maggio.

⚠️ **E quel fatto aveva già una nota padrona nel vault**, scritta nel lotto 2A. **Stavo per
duplicarlo**: la nota nuova aveva già la sua sezione, la sua fonte e il suo locator. È stato
tolto e sostituito da un link, che è ciò che E40 prescrive. **La ricerca di E43 ha prodotto in
un colpo solo una correzione, un fatto e un mancato doppione** — e il terzo è il più
istruttivo, perché un doppione non lo trova nessun controllo automatico.

⚠️ **Il costo della regola, dichiarato.** L'artefatto sta in
`06_operativo\ricerche_assenza\conducibilita-acqua-di-rete_2026-08-20.md`, e il primo lancio è
costato una lettura completa dell'archivio. **La regola vale il suo costo su questa evidenza,
non in astratto**: una sola esecuzione, e ha impedito un'affermazione falsa.

---

## 8. Gli strumenti cambiati in questo lotto

| Strumento | Che cosa è cambiato |
|---|---|
| `candidate_r1.py` | **due domini nuovi**, `acqua` e `allergeni`, ciascuno con le fonti che lo governano e le espressioni che lo riconoscono. Il criterio finisce nel codice, come lo strumento prescrive, e non nella memoria di nessuno |
| `06_operativo\ricerche_assenza\` | **prima esecuzione vera**: la cartella nasce al gate di stamattina vuota, e adesso porta il suo primo artefatto |

⚠️ **Nessuno script è stato scritto per questo lotto**, e va detto: il lavoro è stato fatto con
gli strumenti che c'erano. `misura_due_tassi.py`, `conta_perimetro_lotto.py`,
`conta_tracciamento.py` e `cerca_assenza.py` hanno retto senza modifiche.

---

## 9. Candidati emendamento

### 9.1 Il tasso di difetto di produzione misura UN dominio, e questo lo sopravvaluta

> ✅ **APPROVATO al gate del 21/08/2026 come E46, nella forma qui proposta.** La serie di §3
> porta ora l'etichetta di dominio, e il manuale la riporta accanto a E41.

⚠️ **È il candidato principale, e nasce da una contraddizione fra due misure di questo
stesso lotto.** `misura_due_tassi.py` dà **0,0 %** di difetto di produzione: nessuna delle 27
note nuove parla del dominio `acqua` senza citare il piano dell'acqua. **Lo strato di giudizio
ha però trovato che due note parlavano di zoning dei tamponi e di frequenza di potabilità
senza citare il manuale HACCP**, che è la fonte che prescrive entrambi.

**Le due misure non si contraddicono: misurano cose diverse.** Lo script controlla il dominio
che il lotto ha dichiarato; il giudice guarda **tutte** le fonti del pacchetto. Ma il numero
che il rapporto dichiara si chiama «tasso di difetto di produzione», e chi lo legge capisce
*tutte* le prescrizioni, non *quella del dominio*.

**La forma dell'emendamento**: il tasso di difetto di produzione si dichiara **col nome del
dominio su cui è misurato**, e il rapporto dice esplicitamente che le prescrizioni di altri
domini non ci entrano. ⚠️ **Non si propone di allargare lo script** — allargarlo
significherebbe dichiarare un dominio per ogni fonte prescrittiva del corpus, e sono
trentasei — ma di **non far dire al numero più di quanto misura**.

### 9.2 Osservazione, non emendamento: «l'attributo che la fonte non dà» è ricomparso

> ✅ **RATIFICATO al gate del 21/08/2026**: la vigilanza si chiude, e la rilettura del criterio
> pre-registrato ha prodotto una riga di giurisprudenza propria — §4.43 del passaggio di
> consegne — perché un criterio riletto a numeri visti, senza regola, diventa il precedente
> con cui truccare i criteri futuri.

⚠️ **La classe parcheggiata al gate di 2A è ricomparsa in questo lotto**, e va registrata
perché il criterio di decisione era stato scritto in anticipo. Tre degli otto rilievi del
primo giro sono esattamente di quella specie:

| La nota | L'attributo che la fonte non dava |
|---|---|
| gli appunti in coda al file delle reflue | «uno snack alla paprika, **che è un prodotto in sviluppo**» |
| le medie non calcolate | «sono state scritte **per essere riempite**» · «la doppia firma ha guardato i dati, non le formule» |
| il laboratorio | «la sanificazione parte dall'**avviso telefonico**» |

⚠️ **Ma il criterio scritto al gate chiede la ricomparsa al TERZO giro di giudizio**, non al
primo, e la ragione è buona: al primo giro la classe si vede in ogni lotto, perché è il primo
giro. **Il verdetto su questa riga lo dà il terzo giro, e sta in §5.**

---

## 9-bis. I numeri di chiusura, presi dopo l'ultima scrittura

⚠️ **Le misure sono state prese due volte**, e valgono quelle nuove: la prima serie alla
chiusura del lotto — 21/08/2026, 00:00:52-00:01:43 — la seconda **dopo il completamento del
ciclo**, il **21/08/2026 fra le 09:22:04 e le 09:22:43**. E44 chiede che si prendano dopo
l'ultima scrittura, e l'ultima scrittura è quella della revisione.

<!-- CONTEGGI DEL VAULT — generati da `06_operativo\qa\conta_stato.py` il 2026-08-21.
     Si incollano VERBATIM: non si ricompongono a mano, non si riscrivono in prosa. -->

| Grandezza | Valore |
|---|---|
| Note nel vault | **246** |
| di cui `_index` | 11 |
| di cui note-strumento del progetto | 14 |
| di cui note di diario (`sessione`, `daily`) | 6 |
| **di cui note di contenuto** | **215** |
| Note per cartella | areas 129 · data 29 · entities 25 · docs 22 · code 15 · workspace 9 · projects 8 · concepts 6 · self 1 · outputs 1 · sources 1 |
| Note per `type` | atomica 152 · conflitto 39 · entita 20 · hub 13 · index 11 · sessione 6 · concetto 5 |
| Questioni aperte (`type: conflitto`) | 39 |
| Grezzi in `sources\` | 160 |
| Grezzi citati da almeno una nota | **41** |
| Grezzi restanti | **119** |

| Misura | Alla chiusura (00:01) | Dopo il completamento (09:22) |
|---|---|---|
| Suite QA, perimetro **di lotto** | 0 ERRORI, 23 AVVISI | **0 ERRORI, 27 AVVISI** |
| Suite QA, perimetro **vault** | 123 ERRORI, 193 AVVISI | **123 ERRORI, 197 AVVISI** |
| Tabella di tracciamento | 82 righe | **89 righe**, da T1 a T89, integra |
| Perimetro del lotto | 41 note | **41 note** (5 candidate + 9 toccate + 27 nate) |
| Due tassi (dominio `acqua`) | 60,0 % · 0,0 % su 27 | **60,0 % · 0,0 % su 27** |
| Collaudo della suite | 22 su 22 | **22 difetti su 22** |
| Emendamenti | concordi a 44 | **concordi a 46** |
| Matrice dei lotti | 17 elenchi | **160 grezzi, 17 elenchi, 0 guasti** |

⚠️ **Gli errori non si muovono e gli avvisi salgono di quattro**: la revisione non ha aggiunto
difetti bloccanti, ha allungato le note. **I conteggi del vault non cambiano affatto** — 246
note, 215 di contenuto, 41 grezzi citati — perché la revisione ha **corretto** e non
**prodotto**: nessuna nota nuova, sedici riscritte.

⚠️ **L'errore del vault scende per la seconda volta consecutiva**, e stavolta di tre:

| Misura | Errori | Di cui incompletezza | Di cui merito |
|---|---|---|---|
| chiusura di R1, 19/08 | **128** | 128 (125 grezzi + 3 aree) | 0 |
| gate di 2A, 20/08 22:25 | **126** | 125 (122 grezzi + 3 aree) | **1** |
| chiusura di 2B, 21/08 00:01 | **123** | 122 (119 grezzi + 3 aree) | **1** |

I tre errori in meno sono **esattamente i tre grezzi** che il lotto ha canonizzato. Il rilievo
di merito è sempre lo stesso: il falso positivo delle doppie padrone, che il gate di 2A ha
deciso di non correggere finché non avrà il suo perimetro chiuso.

---

## 10. La revisione col canone — dichiarata scoperta il 21/08 alle 00:08, eseguita alle 08:52

> ✅ **CHIUSA.** Il gate del 21/08/2026 ha sciolto la contraddizione con **E45**, e il ciclo è
> stato completato nella stessa giornata. Quello che segue è il testo con cui il lotto aveva
> dichiarato il passo scoperto — **si lascia, non si cancella**, perché la decisione di
> fermarsi è stata ratificata come corretta e le premesse sbagliate sono la ragione per cui
> E45 esiste — e sotto c'è l'esito della revisione.

### 10.1 Com'era scritto alla chiusura del lotto, e perché si lascia

⚠️ **Il passo 7 del ciclo di lotto chiede una revisione col canone, e questa sessione non
l'ha fatta.** Non per dimenticanza: **le guardie generali del prompt di questa sessione dicono
«`03_valutazione\` non si apre mai»**, e un subagente che io lancio è questa sessione.

**Perché non ho forzato la lettura.** Il metodo chiede che la revisione sia fatta da una
«sessione diversa da quella che ha scritto», e il senso della guardia è che il canone
**guidi e non appaia**. Le due sole fughe di canone che il progetto abbia pagato sono nate
esattamente da qui. ⚠️ **Fra il rischio di lasciare un passo scoperto e il rischio di
contaminare il vault, ho scelto il primo**, che è reversibile.

**Che cosa manca, in concreto.** La revisione col canone è il passaggio che in 2A ha trovato
le **due assenze dichiarate false** — cioè il difetto che nessuno strato deterministico può
vedere. In questo lotto quel controllo **non è stato fatto**, e i suoi bersagli tipici
restano scoperti:

- la **riproduzione indipendente dei conteggi** delle note di misura;
- le **assenze dichiarate** (una sola in questo lotto, ma con l'artefatto di E43 a sostegno);
- la **copertura dei fatti chiave** dei tre grezzi, che solo il canone conosce.

⚠️ **Il lotto NON si dichiara verificato dal canone**, e il gate deve saperlo prima di
approvarlo. È il caso di §4.31 applicato a se stesso: **un lotto che dichiara scoperto un
proprio controllo vale più di uno che lo dà per fatto.**

### 10.2 Le due premesse erano sbagliate, ed erano del testo del coordinatore

⚠️ **Il canone non vive in `03_valutazione\`: sta in `01_metodo\`.** La guardia riguarda
**l'esame** — domande e risposte — e resta assoluta, subagenti compresi. **Due perimetri, due
ragioni**, e i prompt non portavano la distinzione.

⚠️ **E un subagente a contesto pulito non è la sessione che ha scritto**: il perimetro è
garantito dalla **fisica del contesto**, non da chi preme il tasto di lancio. È il meccanismo
con cui il progetto ha sempre fatto questo passo, 1A 1B 1C R1 e 2A comprese.

⚠️ **Il timore era rovesciato.** Le due fughe di canone del progetto **non sono nate dal
revisore**: sono nate da chi scriveva le note, e nel pilota da un'informazione **del report del
revisore** ricopiata in una nota senza grezzo. Il revisore **deve** avere il canone — la
categoria C esiste perché quattro revisori senza canone segnalarono 82 trappole volute.

**La decisione di fermarsi resta ratificata come corretta**: fra un passo scoperto e dichiarato
e una contaminazione possibile, il primo è reversibile. ⚠️ **Ma è la seconda sessione che lo
stesso dubbio ferma** — R1 chiese l'autorizzazione, 2B si fermò — e a quel punto **si emenda la
fonte**: la regola vive ora in `metodo_03` §9.5 passo 3, come **E45**.

### 10.3 L'esito della revisione: 14 rilievi A, 5 B, 0 C

Eseguita il **21/08/2026** da un **revisore a contesto pulito**, col canone e `alias_entita.md`
alla mano, sulle 41 note del perimetro. ⚠️ **Il primo tentativo è caduto per un errore di rete
a metà lavoro**: l'agente era in sola lettura, e la verifica dell'interruzione — impronta
`sha256` di **250 file** prima e dopo — ha dato **zero differenze**. Il secondo è arrivato in
fondo.

| Categoria | Quanti | Che cosa se n'è fatto |
|---|---|---|
| **A — errore vero** | **14** | verificati **sui grezzi** uno per uno, tutti confermati, tutti corretti |
| **B — divergenza non registrata** | **5** | nel canone, sezione datata 21/08/2026; quattro righe in `alias_entita.md`; sei righe di tracciamento, T83-T88 |
| **C — falso allarme** | **0** | il revisore ne dichiara quattro **considerate e non segnalate**, perché il canone le conosce come volute |

⚠️ **Dieci dei quattordici A sono della specie che il §5.4 aveva già nominato** — l'affermazione
universale verificata sul sottoinsieme che l'ha suggerita: «unica dell'archivio», «prima
volta», «OGNI parametro», «tutte e cinque le campagne», «sempre più vicine». **Il lotto l'aveva
nominata e non l'aveva estirpata**, ed è la prova più forte che quella riga di vigilanza serve.

⚠️ **Due di essi stavano nel `summary`**, cioè nel campo che il retrieval legge per primo, **con
il corpo della nota che li smentiva sei righe più sotto**: la nota della Listeria diceva
«unica positività dell'archivio» in testa e «non è l'unica dell'archivio» nel corpo. **La
propagazione di E39 si era fermata prima dell'intestazione**, che è esattamente il difetto per
cui E30 esiste.

⚠️ **E uno è di specie diversa e più grave — A3.** La nota delle medie non calcolate non
esagerava un quantificatore: **descriveva un meccanismo che il file non ha.** Diceva che due
celle erano vuote e che la terza portava l'errore di una formula su intervallo vuoto. L'XML dice
il contrario su tutti e tre i punti: le due celle **contengono la formula** e non il risultato,
la terza **porta l'errore e nessuna formula**. ⚠️ **La spiegazione plausibile del meccanismo era
in grassetto**, e non veniva da nessuna fonte.

### 10.4 Che cosa la revisione ha trovato che nessuno strato automatico poteva trovare

**I conteggi tornano tutti.** Il revisore ha riprodotto in modo indipendente ventiquattro
grandezze — le 148 righe, le 8 non conformità, i 18 e i 24 su 28, il 536, i valori dello scarico
e lo storico 2025 — e **nessuna è sbagliata**. L'unico numero che ha corretto è il
quantificatore di A7, non un conteggio.

**L'assenza dichiarata regge, e l'artefatto la dimostra solo in parte.** ⚠️ **Tre difetti dello
strumento di E43**, e vanno al gate:

1. l'artefatto scrive «TROVATO in **9 file**» dove sono **9 occorrenze su 6 file**: conta
   coppie file-termine e le chiama file;
2. i termini cercati **non coprono `mS/cm` né il tag `COND`**, quindi il log del CIP — 368
   letture di conducibilità — **è invisibile alla ricerca**. L'affermazione sopravvive perché
   quelle letture sono di circuito e non di rete, **ma è il ragionamento a reggerla, non
   l'artefatto**;
3. un **falso positivo** — «riconducibilità» dentro una nota del commercialista — era entrato
   nella nota come menzione vera. Corretto.

⚠️ **La regola di E43 ha funzionato, lo strumento no del tutto**: l'artefatto prova che il gesto
è stato fatto, non che il perimetro fosse quello giusto.

### 10.5 Il ri-giudizio dopo le correzioni, e la prova che nessuno voleva

Le correzioni della revisione hanno toccato sedici note, e per E9 sono state **rigiudicate**:
pacchetto rigenerato (E33), giudice a contesto pulito, senza canone.

| Esito | Note |
|---|---|
| `pulita` | **25** |
| `afferma_oltre` | **11** |

**Tutti e undici accolti.** Otto erano preesistenti e della specie già nominata — «l'unica
osservazione d'archivio», «l'unico documento dell'archivio», «l'unico controllo dell'archivio»,
«l'unica dell'archivio soggetta a un limite» — più tre attribuzioni: una causa, un meccanismo e
un'intenzione.

⚠️ **Ma tre degli undici li avevo introdotti IO, correggendo, poche ore prima.** Scrivendo la
disambiguazione delle sigle di non conformità — che è la correzione del rilievo B4 — ho scritto
in tre note **«l'archivio porta tre serie parallele di numerazione»**, e le fonti di quelle tre
note **ne documentano due**: la terza sta in un registro che nessuna delle tre cita. Un
quarto rilievo ha la stessa origine: **«il registro delle non conformità interne ne porta almeno
nove con causa di usura»**, un conteggio esatto tratto da un documento che non è fonte di quella
nota.

⚠️ **È la prova che il §5.4 non poteva darsi da solo.** Nominare la specie non la estirpa,
**perché la specie si rigenera nel gesto stesso che la corregge**: scrivere una disambiguazione
significa spiegare *perché* due sigle si somigliano, e la spiegazione migliore è quella che
guarda tutto l'archivio — cioè fuori dalle fonti che si stanno citando. **Il rimedio non è
attenzione: è che ogni affermazione universale nasca già col suo perimetro attaccato.**

⚠️ **E un rilievo è di un'altra specie ancora, e vale come segnalazione al gate.** Il giudice ha
contestato le due formule `AVERAGE` citate nella nota delle medie **perché nel testo estratto
non ci sono**. Ha ragione lui sul testo estratto e ho ragione io sul file: **l'estrattore
congelato del progetto restituisce i valori dei fogli di calcolo, non le formule.** Dell'errore
`#DIV/0!` porta traccia, delle due `AVERAGE` no. ⚠️ **Non è un difetto della nota: è un punto
cieco della catena di provenienza**, perché QA e giudizio girano entrambi su quel testo. La
nota dichiara ora il percorso di lettura, e la riga **T89** porta il problema al gate finale.

### 10.6 Il ciclo si ferma qui, e non con un quarto giro

⚠️ **Per E26 il ciclo non si chiude ripetendo il giro**: il pattern è nominato dal §5.4, il
ri-giudizio ne ha confermato la meccanica, e un altro giro troverebbe altri superlativi senza
dire nulla di nuovo. **Le correzioni sono state applicate, la QA di lotto è tornata verde, e il
lotto si chiude.**

---

---

---

## 11. Il gate finale — che cosa il gate ha chiesto, e che cosa ha trovato

> ✅ **Il lotto 2B è APPROVATO pienamente** al gate del 21/08/2026. Questa sezione registra gli
> adempimenti che il gate ha chiesto e i loro esiti, perché due di essi hanno prodotto numeri
> che nessuno si aspettava.

### 11.1 Il censimento delle formule — T89 ha il suo numero, ed è grande

⚠️ **Il gate lo ha chiesto per una ragione precisa: «T89 non può aspettare il gate finale senza
un numero, oggi nessuno sa se il buco riguardi un file o trenta».** Uno script nuovo
(`06_operativo\censimento_formule.py`) apre ogni foglio di calcolo del corpus come archivio e
conta le celle con formula, distinguendo quelle che l'estrattore congelato **non restituisce
affatto** da quelle di cui restituisce il solo risultato.

<!-- CENSIMENTO DELLE FORMULE — generato da `06_operativo\censimento_formule.py`
     il 2026-08-21 alle 12:39:33. Si incolla VERBATIM. -->

| Grandezza | Valore |
|---|---|
| Fogli di calcolo nel manifest | **15** |
| Con almeno una formula | **13** |
| Con almeno una formula **invisibile** | **13** |
| di cui **non ancora canonizzati** | **10** ← il numero della soglia |
| **Celle con formula, in tutto il corpus** | **1.697** |
| di cui **invisibili all'estrattore** | **1.697** |
| di cui visibili a metà *(risultato sì, formula no)* | **0** |

I dieci file non ancora canonizzati che portano formule invisibili: il **budget per linea**
(332 formule), il **libro unico** (425), il **previsionale di cassa** in due copie (102 ×2), il
**vendor rating** (73), gli **scostamenti dei costi** (115), la **marginalità per referenza**
(84), il **cruscotto KPI qualità** (65), il **registro MOCA** (3) e una cartella di lavoro
vuota di nome (1).

⚠️ **Il numero che conta non è 1.697: è lo ZERO dell'ultima riga.** Nessun foglio di calcolo del
corpus porta valori in cache. **Non è un difetto sporadico di un compilatore distratto: è una
proprietà sistematica dell'archivio**, e cambia la natura del problema. Ogni cella calcolata
risulta vuota nel testo estratto, quindi **«questa colonna è vuota, dunque nessuno l'ha
compilata» è una lettura possibile ma non l'unica** — e finora è stata l'unica offerta.

⚠️ **Il vault regge, e va detto perché non era scontato.** Ho cercato le note che descrivono
colonne vuote su fonti `.xlsx`: `kpi-mass-balance-l26130` scrive «**formule mai calcolate**», che
è esatto; `fatto-piano-produzione-sett19-21` scrive «le colonne calcolate sono vuote», che è
vero ma non dice che sono formule. **Nessuna afferma il falso**, e la prima lo aveva capito
prima che esistesse lo strumento per misurarlo.

✅ **Soglia superata**: il criterio scritto al gate diceva «più di tre grezzi non ancora
canonizzati», e sono **dieci**. **L'estensione di cantiere della QA si farà** — ma la decisione
operativa resta al gate di 2B-bis, come il gate ha prescritto, e **l'estrattore di misura non
si tocca in nessun caso**.

### 11.2 I tre difetti dello strumento di E43, decisi uno a uno

| Difetto | Decisione | Che cosa è cambiato |
|---|---|---|
| «TROVATO in 9 file» dove erano 9 occorrenze in 6 file | **refuso, si corregge** | l'artefatto scrive ora «**N occorrenze in M file**» |
| i termini non coprivano `mS/cm` | **non è un difetto di codice** — la scelta dei termini è giudizio | l'artefatto acquista la sezione «**termini considerati e NON cercati, col perché**» |
| il falso positivo «riconducibilità» | **non si corregge restringendo** | una riga nel docstring dichiara che **il matching è largo apposta** |

⚠️ **La terza decisione è quella che vale, e va motivata perché sembra un difetto lasciato
lì.** Una ricerca che attesta un'**assenza** deve sbagliare per eccesso: meglio dieci risultati
da scartare a mano che una vera occorrenza mancata. **Il difetto del caso «riconducibilità» non
fu il matching largo: fu consumare il risultato senza guardarlo.** La riga nel docstring esiste
perché nessuno «migliori» il matching fra sei mesi.

⚠️ **E la ricerca è stata rifatta col perimetro allargato, ottenendo una prova per il secondo
punto.** Includendo il tag `COND` — che sembrava l'omissione più ovvia — la ricerca restituisce
**96 file su 155** e diventa inservibile, perché come sottostringa matcha «SECONDO»,
«CONDIZIONI», «CONDOTTA». **Quel termine sta ora fra gli scartati con la sua ragione misurata**,
non ipotizzata. Il nuovo artefatto trova **10 occorrenze in 7 file**, e fra queste il log del
CIP, che porta conducibilità vere **di un'altra acqua**: il circuito, non la rete.

### 11.3 Il criterio sulla specie universale è stato aggiornato, non riletto

⚠️ **La distinzione è sottile e va scritta, perché senza di essa questo sarebbe §4.43
violato.** §4.43 vieta di rileggere un criterio **a esito visto**; qui **l'esito di 2B-bis non
esiste ancora**, e il criterio è stato corretto **prima che l'esperimento parta**, per un fatto
sopravvenuto che non prevedeva: la specie rigenerata **in produzione, dentro il gesto di
correzione** (§10.5).

**Resta**: se al terzo giro di 2B-bis la specie compare su note nate o riscritte dal lotto,
diventa emendamento. **Decade**: la chiusura automatica — se non compare, il gate di 2B-bis
decide con tutte le osservazioni davanti. ⚠️ **La ragione è E46 applicato ai criteri**: un giro
di giudizio di un lotto non misura la specie nell'intero metodo, misura la specie in quel
lotto.

### 11.4 Una riga di igiene, perché il gate l'ha chiesta

⚠️ **Durante la verifica dell'interruzione, i due file d'impronta `sha256` sono finiti dentro il
vault**: lo script faceva `os.chdir` sulla cartella del vault e scriveva in quella corrente.
Visti e spostati fuori nello stesso turno. **Non erano `.md` e non sono mai entrati in nessun
conteggio**, ma stavano dove non dovevano.
