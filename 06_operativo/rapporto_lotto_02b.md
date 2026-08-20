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

**La serie, che è la cosa che conta:**

| Misura | Riapertura (debito) | Difetto di produzione (metodo) |
|---|---|---|
| **R1** (manutenzione, 19/08) | — | **57,7 %** |
| **2A** (20/08) | 40,0 % (4/10) | **3,3 %** (1/30) |
| **2B** (21/08, 00:01) | **60,0 %** (3/5) | **0,0 %** (0/27) |

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

⚠️ **È il candidato principale, e nasce da una contraddizione fra due misure di questo
stesso lotto.** `misura_due_tassi.py` dà **0,0 %** di difetto di produzione: nessuna delle 26
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

⚠️ **Tutte le misure che seguono sono state prese il 21/08/2026 fra le 00:00:52 e le
00:01:43**, cioè **dopo** l'ultima scrittura nel vault, come impone E44.

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

| Misura | Valore | Ora |
|---|---|---|
| Suite QA, perimetro **di lotto** | **0 ERRORI, 23 AVVISI** | 00:00:58 |
| Suite QA, perimetro **vault** | **123 ERRORI, 193 AVVISI** | 00:01:20 |
| Tabella di tracciamento | **82 righe**, da T1 a T82, integra | 00:01:15 |
| Collaudo della suite | **22 difetti su 22**, cinque vie più il caso negativo | 00:01:35 |
| Emendamenti | registro e manuale **concordano** | 00:01:43 |

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

## 10. La revisione col canone NON è stata eseguita, e il perché va letto

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

---
