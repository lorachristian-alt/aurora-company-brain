# Rapporto del lotto 2B-bis — gli allergeni

> **Che cos'è** · Il rapporto del **lotto 2B-bis**, nato dallo spezzamento del lotto 2B (E28)
> e **ottavo lotto di canonizzazione** del progetto. Due grezzi: la scheda con la matrice di
> cross contamination e il materiale della formazione annuale agli operatori.
> **Per chi** · Per il coordinatore, al gate. Ogni numero viene da uno script, e da **E44**
> ogni numero porta l'ora della propria misura.
> **Chiuso il** · **21/08/2026**.

---

## 1. Il perimetro, e perché il taglio passa qui

Lo spezzamento è stato deciso **in apertura del lotto 2B**, prima di scrivere una riga, e la
ragione sta nella natura dei documenti: **la scheda allergeni è una fonte prescrittiva** —
matrice, sequenze, tipi di lavaggio, rework, etichettatura precauzionale, stoccaggio,
responsabilità — e **apre da sola un dominio di riconciliazione verticale**. Tenerla insieme ai
registri analitici avrebbe messo **due riconciliazioni verticali in un lotto solo**.

⚠️ **La previsione si è avverata al di là delle attese.** Dei due grezzi, la scheda ha prodotto
la quasi totalità del contenuto e **sei delle otto divergenze** che la revisione ha poi trovato.

## 2. La riconciliazione verticale (E37), e il dominio `allergeni`

Il dominio è stato aperto in `candidate_r1.py` con le sue espressioni e le sue fonti, ed è
stato eseguito **come passo di apertura** — non a fine lotto. Ha restituito **sei note
arretrate**, che parlano di allergeni, contaminazione crociata, sequenze, rework o etichettatura
precauzionale **senza citare la fonte che quel dominio lo governa**.

⚠️ **Una di esse è stata riaperta e corretta**: `doc-scheda-tecnica-af-sn-0450` affermava che la
scheda descrive i punti critici «con le stesse soglie del piano HACCP» — **un'affermazione che
le sue fonti non sostengono**, e che è stata riscritta come «con le proprie soglie, che
coincidano con quelle del piano HACCP questa fonte non lo dice».

## 3. I tre giri di giudizio, e il criterio pre-registrato che si è avverato

| Giro | Rilievi | Che cosa erano |
|---|---|---|
| **primo** | **11** | ⚠️ Fra questi, **un nome proprio inventato** — `entita-claudia-vicentini`, mentre le fonti danno solo «C. Vicentini» e il manuale dà **Chiara**. E la divergenza sulla soia, emersa **dal giudizio e non dalla scrittura** |
| **secondo** | **7** | **Quattro erano attribuzioni di ruolo** che le fonti non fanno: chi firma un commento, chi affianca il relatore, chi propone il recupero del turno notte, chi ha causato una non conformità |
| **terzo** | **5** | ⚠️ **Tre erano la specie universale**, sulle note nate dal lotto |

⚠️ **Al terzo giro il criterio pre-registrato al gate di 2B si è avverato**, e nelle due
condizioni previste da §4.43: la specie è ricomparsa su note **nate** nel lotto, e la sua
ricomparsa era **prevedibile prima di vederla**. Da lì è nato **E47**.

⚠️ **E47 è il primo emendamento del progetto nato da un criterio pre-registrato che si è
avverato** — non da un errore trovato per caso.

## 4. E47, e perché una regola serviva più dell'attenzione

**Un'affermazione universale si scrive col perimetro su cui è stata verificata, e quel perimetro
non è mai più largo delle `fonti` della nota.**

La ragione per cui non bastava ricordarsene sta nei numeri: **nominata al terzo giro del lotto
2B, la specie è ricomparsa dieci volte nella revisione dello stesso lotto — tre volte dentro le
correzioni che la stavano correggendo** — e poi al primo, secondo e terzo giro di 2B-bis.

⚠️ **Il gesto che la produce è lo stesso che produce una buona sintesi**: chi ha letto a fondo
un documento scrive il superlativo come riassunto onesto di quella lettura, mentre è un
**quantificatore** le cui condizioni di verità stanno **fuori dal testo che si ha davanti**.

## 5. La revisione col canone (E45) — dieci rilievi A, otto B, zero C

Eseguita da un revisore **a contesto pulito**, con il canone alla mano e senza mai vedere lo
strato di giudizio.

### 5.1 I due rilievi verificati sui grezzi prima di correggere

**Nessun rilievo è stato applicato sulla parola del revisore.** I due che cambiavano il senso di
una nota sono stati verificati **aprendo i grezzi**:

**A4 — il barrato.** Aperto il `.docx` come archivio: **quattro run portano il barrato attivo**,
e uno di essi è **esattamente la frase su cui poggiava `fatto-latte-riclassificato-af-sn-0450`**.
Un altro è **metà** della tolleranza sul rework. ⚠️ **Il testo estratto non ne mostra nessuno**:
è il **secondo punto cieco** della catena di provenienza, dopo le formule di T89. Ne è nata una
nota propria, `fatto-passaggi-barrati-scheda-allergeni`, e la riga **T96**.

**A7 — il disallineamento che non esiste.** Il documento avverte che «la tabella si e' rovinata…
le colonne non sono piu' allineate». **Ricontate: intestazione e tutte e sette le referenze
portano sedici campi**, e i valori cadono nella colonna giusta. ⚠️ **La nota aveva propagato
l'avvertenza come un rischio reale**, deducendone che si può attribuire un allergene alla
referenza sbagliata. **Un'autodichiarazione di difetto si verifica, non si cita** — e verificarla
era il compito del lotto. Riga **T105**, chiusa.

### 5.2 Gli altri otto

Locator falso (slide 8 invece di 7, contato riaprendo il `.pptx`); tre righe d'indice che
dicevano cose che le fonti non dicono; una scomposizione di sette referenze che ne descriveva
sei; un «1 e 2» presentato come lettura certa dove la fonte numera due voci con lo stesso
numero; e un «riclassificato su tre referenze» dove la referenza riclassificata è **una**.

### 5.3 La diagnosi del revisore, che vale più dei singoli rilievi

> *«Il difetto non è nella lettura, è nel perimetro: il lotto ha canonizzato dentro i due
> documenti e quasi mai contro ciò che il vault già possiede.»*

⚠️ **È la diagnosi giusta, e i numeri la confermano**: **sei delle otto divergenze B** stanno
fra la scheda allergeni e un documento **che il vault aveva già** — il manuale HACCP,
l'istruzione CIP, il registro delle NC, il registro dei tamponi. **La riconciliazione verticale
era stata fatta in entrata e non in uscita.**

## 6. Le otto divergenze del canone, e le sette che sono entrate nel vault

| | Che cos'è | Esito |
|---|---|---|
| **B1** | Il manuale cerca **soia**, la scheda **sesamo**; trimestrale contro una tantum | `questione-proteine-test-manuale-e-scheda` · **T97** |
| **B2** | La NC del lavaggio da aprire sul modulo dei **reclami** | `questione-nc-lavaggi-sul-modulo-reclami` · **T98** |
| **B3** | Il lavaggio completo, composto in due modi diversi | `questione-composizione-lavaggio-completo` · **T99** |
| **B4** | La nota che motiva un perimetro che la tabella non elenca | dentro `questione-precauzionale-af-sn-0450-soia` · **T100** |
| **B5** | Arachidi e solfiti: possibili in aula, assenti in matrice | `questione-arachidi-solfiti-aula-e-matrice` · **T101** |
| **B6** | Il registro della formazione non conferma nessuna sessione 2026 | ⚠️ **solo canone** · **T102** |
| **B7** | Tamponi allergeni dichiarati in aula, assenti da `MOD-QA-19` | `questione-tamponi-allergeni-non-registrati` · **T103** |
| **B8** | «Non rilevato» come condizione per avviare un prodotto che lo contiene | `fatto-proteina-latte-prima-del-bio` · **T104** |

### 6.1 B3 riapre un arbitrato già scritto nel canone — e al gate il ri-giudizio l'ha richiuso

⚠️ **Il gruppo del lotto 2A arbitrava «`IO-05`, e il log resta com'è»**, concludendo che il
tracciato fosse *più severo del nome che porta*. **Sembrava non reggere**: la fase che il log
esegue in più ha una fonte prescrittiva che la chiede, ed è la scheda allergeni. Su questa
lettura la divergenza cambiava specie, e la riga del canone di 2A ha ricevuto il rimando a B3.

⚠️ **La formulazione di B3 è stata corretta due volte.** La prima dopo il ri-giudizio del lotto
(§8.1): il «cinque contro sei» non stava nelle fonti, e lo scarto vero è che **la scheda omette
il prerisciacquo e include la sanificazione**.

⚠️ **La seconda al gate, e ha ribaltato la conclusione.** §5.3 prescrive quel sanificante **solo
dentro il lavaggio di tipo `L3`, obbligatorio in quattro circostanze nominate**, e §5.4 affida
il tipo di lavaggio al registro del capoturno: **il log non lo dichiara mai**. Quindi **la scheda
non giustifica il `SANIF_PAA` che compare in 28 cicli su 30**, l'arbitrato del lotto 2A **regge**,
e ne esce più preciso — il tracciato è più severo **di entrambi** i documenti, non solo di
`IO-05`. **La divergenza sulla composizione resta vera e vive per conto proprio.** Il dettaglio
sta nel §14.

### 6.2 B6 è vera e non è scrivibile

Il suo grezzo non è in nessun lotto. ⚠️ **Il divieto 9-bis vale anche quando la divergenza è
verificata**: sta nel canone, non nel vault, e la riga T102 dice a quale lotto tocca.

⚠️ **E corrobora una chiusura prudente**: `fatto-turno-notte-senza-formazione` chiude con «la
risposta non è nel materiale», e il registro conferma che al 18/05 il recupero **non risulta
fatto**. **La prudenza era la lettura giusta**, non un ripiego.

### 6.3 Un tratto del documento, non una serie di sviste

⚠️ **Il PRPo1 prescrive molto e si riconcilia poco.** È annesso al manuale e non lo cita mai;
nomina `IO-05` e ne cambia il contenuto; nomina `MOD-QA-31` e intende `MOD-QA-18`; nomina
`MOD-QA-19` per registrazioni che quel registro non porta. **Il canone lo registra come tratto
del documento.**

## 7. Una nota tolta dalla classe sbagliata

`fatto-proteina-latte-prima-del-bio` era nato come `questione-`, `type: conflitto`. **Le sue
fonti sono un file solo**, e §2.4 chiede almeno due file diversi per un conflitto. ⚠️ **Non è
un cavillo di QA: un'incoerenza dentro un documento non è un conflitto fra fonti**, ed è una
distinzione che il vault deve poter fare cercando. Rinominata e riclassificata.

## 8. Il ri-giudizio dopo la revisione (E9) — cinque errori, diciassette avvisi

Il pacchetto è stato generato **per ultimo** (E33) e dato a un giudice **a contesto pulito e
senza il canone** (E45). Ha prodotto **22 rilievi su 41 note**, e sono stati accolti tutti.

### 8.1 I cinque errori, e uno era mio da tre passaggi

| | Che cos'era |
|---|---|
| **1** | ⚠️ **Il «cinque contro sei» del lavaggio non è di nessuna delle due fonti.** La scheda elenca **cinque** operazioni, `IO-05` ne elenca **sei** sotto la frase «il ciclo completo ha 5 fasi». **Il sei l'avevo contato io** |
| **2** | «Il sesamo non è in nessuna ricetta di Linea 1»: la sequenza della linea prevede «[solo su pianificazione dedicata] prove `AF-SN-0470` con sesamo» |
| **3** | Il barrato del §4.3 è troncato **quanto** quello del §7.4, e la nota costruiva una distinzione fra i due |
| **4** | «Sono l'unico caso»: la matrice dà `A` alle uova e alla frutta a guscio in condizione identica |
| **5** | «La nominano **sempre** per iniziale», smentito da una riga **che la nota stessa cita** |

⚠️ **Il primo è il più istruttivo, ed era passato attraverso tre livelli.** Il «sei» viene dal
revisore col canone, che l'ha scritto in buona fede; io l'ho scritto nel canone, in una nota e
in una riga di tracciamento **senza contarlo sulla fonte**. **Il giudice l'ha contato.**

### 8.2 E lo scarto vero era più interessante di quello che avevo scritto

Contate le due fonti, la divergenza non è «una fase in più»: **la scheda omette il
prerisciacquo, che in `IO-05` è la fase 1, e include la sanificazione, che `IO-05` tiene
condizionata al programma**. È `IO-05` **meno la prima e più l'ultima**. ⚠️ **E il log non attua
nessuna delle due composizioni**: le esegue tutte e sei e mette la sanificazione **fra l'acido e
il risciacquo finale**, mentre entrambi i prescrittivi la elencano in coda.

**Il canone, la nota e T99 sono stati riscritti su questa lettura**, e la nota ha cambiato nome:
`questione-composizione-lavaggio-completo`.

### 8.3 Il pattern del ri-giudizio, e perché il ciclo si ferma qui (E26)

I ventidue rilievi si dividono in due famiglie sole.

**a) La specie di E47, ancora.** Quattro rilievi — «l'unico», «sempre», «ogni altro allergene
del sito», «l'unica riga della matrice». ⚠️ **E47 era già in vigore quando sono stati scritti.**
Il che dice una cosa che il gate deve sapere: **E47 non estingue la specie, la rende
trovabile** — il controllo del quantificatore è un gesto **di chi rilegge**, non di chi scrive.

**b) Il conteggio che nasce dalla lettura e non dalla fonte — specie nuova.** Il «sei» del
lavaggio; le «due colonne» riclassificate, che sono **due caselle**; i «due divieti», che sono
un divieto e un obbligo; e due locator spostati — «§8.1» per un elenco che sta in **§7.3**, e
una «colonna `logica FEFO`» che è in realtà **il titolo del file**.

⚠️ **La forma è sempre la stessa: la nota riporta un numero o una posizione che ha ricavato
guardando, e la fonte quel numero non lo dice.** È imparentata con **E23** — il marcatore di
valore derivato — ma E23 è nata per i valori *calcolati*, e qui si tratta di **contare e
localizzare**, che sembrano atti di lettura e sono invece atti di inferenza.

⚠️ **Non si emenda adesso: è la prima volta che la si nomina** (E28), e vale la disciplina che
ha funzionato per E47. **Il criterio di decisione va scritto ora, prima del prossimo lotto** —
sta in §11.

⚠️ **E il ciclo si ferma qui.** Le correzioni sono state applicate e la QA è tornata a zero
errori, ma **non si apre un quarto giro**: la regola d'arresto di E26 chiede di **nominare il
pattern** e fermarsi, non di rincorrere la convergenza.

## 9. I numeri di chiusura, presi dopo l'ultima scrittura (E44)

Ogni riga porta l'ora della propria misura. L'ultima scrittura sul vault è la nota di sessione,
alle **14:46**.

| Misura | Valore | Ora |
|---|---|---|
| Suite QA, perimetro **di lotto** | **0 ERRORI, 25 AVVISI** | 14:47:43 |
| Suite QA, perimetro **vault** | **121 ERRORI, 214 AVVISI** | 14:47:43 |
| Tabella di tracciamento | **106 righe**, da T1 a T106, integra | 14:49:04 |
| Emendamenti | **concordi a 47** | 14:49:04 |
| Matrice dei lotti | **160 grezzi, 17 elenchi, 0 scoperti, 0 guasti** | 14:49:04 |
| Perimetro del lotto | **44 note** — 2 grezzi, 6 candidate, 5 toccate, **33 nate** | 14:49:16 |
| Collaudo della suite | **22 difetti su 22**, cinque vie più il caso negativo | 14:49:39 |
| Note nel vault | **281**, di cui **248 di contenuto** | 14:49:54 |
| Grezzi citati / restanti | **43 / 117** | 14:49:54 |

### 9.1 I due tassi (E41), col nome del dominio misurato (E46)

| Lotto | Dominio misurato | Riapertura (debito) | Produzione (metodo) |
|---|---|---|---|
| **R1** | perimetro CCP e tarature | — | **57,7 %** |
| **2A** | dominio `cip` | — | **3,3 %** |
| **2B** | dominio `acqua` | 60,0 % | **0,0 %** — 0 su 27 |
| **2B-bis** | dominio **`allergeni`** | **0,0 %** — 0 su 6 | **9,1 %** — 3 su 33 |

⚠️ **Il tasso di produzione risale, e va dichiarato così com'è.** Le tre note sono
`fatto-turno-notte-senza-formazione`, `fatto-firma-registro-formazione-all-ingresso` e
`fatto-quasi-incidente-sequenza-novembre`: **tutte e tre del sotto-dominio della formazione**,
dove la fonte che governa è il materiale d'aula e non la scheda prescrittiva.

⚠️ **Questo non è un alibi, ed è una misura e non un giudizio.** Il criterio di
`candidate_r1.py` è **deliberatamente largo**: chiede che una nota che parla di allergeni abbia
fra le fonti la scheda che gli allergeni li prescrive. Le tre note **non ce l'hanno**, e il
numero è 9,1 %. ⚠️ **Se un lotto futuro misurasse un dominio con due fonti governanti, il
criterio andrebbe esteso a entrambe** — ed è un fatto sullo strumento, non sul lotto.

⚠️ **E la riapertura a 0,0 % su 6 non è un lotto pulito**: significa che **nessuna** delle sei
note riaperte è stata agganciata alla scheda allergeni. Cinque sono state chiuse dichiarando
che quella fonte non le governa — esito legittimo, il criterio è largo — e **una è stata
corretta togliendo un'affermazione che le sue fonti non sostenevano**, non agganciandola.
**Correzione vera, che il tasso non conta**, ed è giusto che non la conti: misura gli agganci.

### 9.2 L'errore del vault scende per la terza volta consecutiva

| Misura | Errori | Di cui incompletezza | Di cui merito |
|---|---|---|---|
| chiusura di R1, 19/08 | **128** | 128 | 0 |
| gate di 2A, 20/08 | **126** | 125 | **1** |
| chiusura di 2B, 21/08 | **123** | 122 | **1** |
| **chiusura di 2B-bis, 21/08** | **121** | **120** (117 grezzi + 3 aree) | **1** |

**I due errori in meno sono esattamente i due grezzi che il lotto ha canonizzato.** Il rilievo
di merito è sempre lo stesso: il falso positivo delle doppie padrone, che il gate di 2A ha
deciso di non correggere finché non avrà il suo perimetro chiuso.

## 10. Che cosa il gate deve sapere, in ordine di peso

1. ⚠️ **La catena di provenienza è cieca al barrato**, ed è la **seconda** cecità trovata dopo
   le formule (T89). L'estrattore di misura **non è stato toccato**: la decisione su una
   eventuale estensione di cantiere è del gate, non mia.
2. ⚠️ **B3 riapre un arbitrato già scritto nel canone.** Non l'ho riscritto: ho aggiunto il
   rimando e dichiarato che non regge come formulato.
3. ⚠️ **B6 è vera e non è scrivibile**, e resta in attesa del lotto che porta il registro della
   formazione.
4. ⚠️ **Il tasso di produzione è a 9,1 %** dopo due lotti sotto il 4 %.
5. ⚠️ **Una specie nuova è stata nominata e non emendata**, col suo criterio qui sotto.

## 11. Il criterio pre-registrato per la specie nuova

Scritto **ora**, prima che il prossimo lotto parta, con la stessa disciplina che ha portato a
E47 — perché un criterio riletto a esito visto non misura più niente (§4.43).

| | |
|---|---|
| **La specie** | **Un conteggio o una posizione che la nota ricava guardando la fonte, e che la fonte non enuncia**: «sei fasi», «due colonne», «due divieti», «§8.1», «colonna `logica FEFO`» |
| **Diventa emendamento se** | ricompare **al terzo giro di giudizio** del prossimo lotto **su note nate dal lotto** — produzione, non debito |
| **Forma proposta** | *un numero che la fonte non enuncia è un valore derivato anche quando si ottiene contando, e si scrive col modo in cui è stato ottenuto — oppure non si scrive* |
| **Non decade da sola** | se al terzo giro non compare, **la riga non si chiude automaticamente**: decide il gate con tutte le osservazioni davanti |

⚠️ **Il prossimo lotto NON riceve alcun promemoria sulla specie**, oltre alle regole già in
vigore. **Un esperimento avvertito non misura niente.**

## 12. Un difetto trovato per caso, e riparato: il CSV della matrice file × fatto

⚠️ **Rigenerando le righe del lotto, lo script è andato in errore e ha lasciato il CSV a metà
scrittura** — 293 righe diventate 184, con tre lotti perduti. **Ripristinato subito da git**, e
poi diagnosticato invece di riprovare.

**La causa sono tre righe che portano sette campi invece di sei**: dentro il campo `fatto`
c'è un **punto e virgola non protetto** — «presa in carico a NO; l'episodio si ripete il 30/05» — e
il parser lo legge come separatore.

⚠️ **Non erano righe innocue.** Nel censimento comparivano come **tre lotti fantasma** chiamati
col nome di una nota — `lotto fatto-obblighi-registro-f-gas`, e altri due — perché lo
slittamento dei campi spostava il nome della nota nella colonna del lotto. **Il difetto era nel
CSV da un lotto precedente, e si vedeva: nessuno l'aveva guardato.**

**Riparate riunendo i due tronconi del campo e riscrivendo il file con il quoting corretto**, e
il lotto 1B torna da 49 a **52 righe** — le tre che aveva perso. Poi generate le **41 righe** di
2B-bis: il CSV ha ora **334 righe** e nessun lotto fantasma.

⚠️ **Che cosa il gate deve decidere**: se lo script debba **rifiutarsi di scrivere** quando
rilegge una riga malformata, invece di fermarsi a metà. Oggi il danno è stato reversibile
perché il file è in git; **la prossima volta potrebbe non esserlo**.

---

# PARTE SECONDA — il gate del 21/08/2026

> **Che cos'è** · Gli adempimenti del gate, eseguiti nella stessa sessione che ha chiuso il
> lotto. **Il verdetto sul lotto era già dato**: qui c'è che cosa il gate ha chiesto di
> costruire, e che cosa la costruzione ha trovato.

## 13. E48 e l'estensione di cantiere

### 13.1 La forma, e perché la separazione si prova invece di dichiararla

`estrazione_cantiere.testo_cantiere` parte da `qa_comune.testo_fonte` — **byte-identica, mai
toccata** — e vi **appende in coda** i due strati marcati, `[FORMULA: …]` e `[BARRATO: …]`.

⚠️ **L'append non è una comodità: è ciò che rende la separazione dimostrabile.** Il testo
della via congelata resta un **prefisso esatto** di quello di cantiere, e `--prova` lo verifica
tagliando il secondo alla lunghezza del primo e confrontandoli carattere per carattere.

| Misura | Valore | Ora |
|---|---|---|
| Grezzi esaminati | **161** | 16:23:15 |
| Con almeno uno strato | **24** | 16:23:15 |
| Righe aggiunte in tutto | **1.737** — 1.697 formule, 40 barrati | 16:23:15 |
| **Prefisso violato** | **0** | 16:23:15 |

⚠️ **Le 1.697 formule combaciano cifra per cifra col censimento indipendente** del 21/08
mattina, che le aveva contate aprendo gli `.xlsx` come zip invece che con `openpyxl`. **Due
strumenti diversi, lo stesso numero.**

⚠️ **E i 40 barrati stanno in 11 documenti, non in uno.** Fra questi `IO-05` (2) e il contratto
di manutenzione frigo (6), **entrambi canonizzati da lotti precedenti**.

### 13.2 Due difetti miei, e come sono venuti fuori

**a) Un `break` che ha inventato quindici avvisi.** Agganciando `qa_provenance` al cantiere
avevo messo un'uscita anticipata nel ciclo che conta gli agganci **per fonte** — e il controllo
del «rumore nel payload» legge proprio quel conteggio. Quindici avvisi nuovi su note **non
toccate**.

⚠️ **Il totale non l'avrebbe mostrato.** L'ha mostrato il confronto **riga per riga** col
report precedente: 61 righe prima, 61 dopo, **zero nuove e zero sparite**. Un cambiamento di
strumento che non porta il proprio prima/dopo non è verificato.

**b) Il controllo del revocato che non poteva scattare mai.** La prima stesura toglieva i
marcatori `[BARRATO: …]` dalla coda — ma **il testo barrato sta già dentro il testo congelato**,
perché l'estrattore restituisce le parole di ogni run senza guardarne la formattazione.
Riparato togliendo anche l'occorrenza originale, **un'occorrenza per ogni run barrato**: è
un'approssimazione, e va nella direzione giusta — può far scattare un avviso di troppo, mai
zittirne uno dovuto.

### 13.3 I quattro difetti piantati, e i tre tentativi falliti

Il fix insieme **allenta e stringe**, quindi i difetti sono quattro e non due: un valore che
vive solo in una formula e che prima era rosso *(divieto)*; un valore attribuito a una formula
che non c'è *(deve restare rosso)*; una nota che dà per **vigenti** due clausole barrate *(deve
essere segnalata)*; la gemella che le **dichiara** revocate *(non deve esserlo)*.

**Collaudo da 22 a 24 difetti su 24**, su tutte e cinque le vie più il caso negativo.

⚠️ **I primi tre tentativi sono falliti, e per tre ragioni tutte mie**: le formule fra caporali
sono **una parola sola** e la soglia di citazione ne chiede cinque; una citazione l'avevo
trascritta «proprieta'» dove la fonte scrive «proprietà»; e la nota che doveva **non** dichiarare
la revoca conteneva «cancellati» **nel proprio summary**.

⚠️ **L'ultima è la più istruttiva**: il predicato guarda anche il summary, ed è giusto che lo
faccia — il summary è ciò che il retrieval mostra per primo (E18). **Ho corretto la nota, non
la regola.**

### 13.4 Che cosa ha trovato appena acceso

Al primo giro sul vault il controllo del revocato ha segnalato **quattro casi**, tutti in
`workspace\`: la **bozza del contratto frigo**, che riporta un canone barrato, e la **bozza
della lettera a Tosano**, che riporta frasi barrate della lettera di risposta.

⚠️ **Non erano nel perimetro della riverifica e non sono state toccate.** La riga sta qui perché
il lotto che aprirà quelle bozze sappia che l'avviso esiste già.

## 14. La riverifica del barrato (2.3), e l'arbitrato riaperto (2.4)

### 14.1 Trenta note riviste, quattro corrette

**Mini-perimetro dichiarato (E32): tutte le trenta note che citano la scheda allergeni**, non
quelle che sembravano sospette.

⚠️ **La più grave era `questione-rework-congelamento-slide-e-scheda`**, il cui summary diceva che
«la scheda allergeni **in vigore** tollera il recupero a inizio turno successivo». Quella riga è
**barrata a metà** nel documento — il barrato copre cinque parole su tredici — e la pratica
risulta per giunta **sospesa** (T90). Corrette anche `doc-regole-rework`,
`questione-precauzionale-af-sn-0450-soia` e `doc-etichettatura-precauzionale`, con la
qualificazione propagata nello stesso turno (E39/E42).

⚠️ **Il revisore ha segnalato che la riverifica ha toccato un grezzo su due**: anche `IO-05`
porta due barrati. **Verificati: il vault li dichiara già entrambi** — la cancellazione della
FFP2 da parte dell'RSPP e il «CANCELLATO» sulla fase acida che non si salta. Nessun difetto, e
la segnalazione era giusta lo stesso.

### 14.2 L'arbitrato del 2A: riaperto, e richiuso più preciso

**Tutte e tre le gambe erano canonizzate**, quindi la nota si riformulava invece di limitarsi a
dichiarare l'arbitrato superato. `fatto-programma-p2-ogni-giorno` è passata da `risolto` ad
`aperto` e la conclusione è stata riscritta.

⚠️ **Poi il ri-giudizio l'ha ribaltata, ed è il rilievo più importante di tutto il gate.** §5.3
prescrive il sanificante **solo dentro il lavaggio `L3`**, e l'`L3` **solo in quattro
circostanze nominate**: «Obbligatorio: dopo sesamo; prima del bio; dopo referenze con crema
nocciola; a fine settimana produttiva». ⚠️ **E §5.4 affida il tipo di lavaggio al registro del
capoturno: il log non lo dichiara mai.**

**Che i 28 cicli di maggio fossero `L3` non lo dice nessuna fonte**, e il `SANIF_PAA` compare
in **28 cicli su 30** — molto più spesso delle occasioni dell'`L3`.

⚠️ **Quindi l'arbitrato del lotto 2A regge, e ne esce più preciso**: il tracciato è più severo
**di entrambi** i documenti, non solo di `IO-05`. La nota è tornata a `risolto`; **il canone,
T99 e questo rapporto sono stati corretti**.

⚠️ **La divergenza sulla composizione resta vera** — la scheda omette il prerisciacquo e
include il sanificante — **e vive per conto proprio**: riguarda che cosa sia il lavaggio
completo, non che cosa faccia il pannello di notte.

### 14.3 E B4 del canone cade come l'avevo scritta

Avevo registrato come **incoerenza intra-file** il fatto che la nota alla matrice motivi il
«`PC` soia» su «Linea 1 e Linea 2» mentre nella tabella nessuna referenza di Linea 2 lo porta.

⚠️ **Lo stesso documento dichiara che su Linea 2 girano referenze che la tabella non contiene**:
«crema nocciola usato su referenze fuori scheda (mercato Ho.Re.Ca.) **lavorate su Linea 2**», e
la sequenza tipo della linea le elenca. **Il perimetro esiste: è la matrice a non contenerlo.**

⚠️ **Il fatto sull'archivio resta, ed è più utile di quello che avevo scritto**: chi legge la
sola tabella non può ricostruire da dove venga quella classificazione.

## 15. E49 applicata a sé stessa

**Due delle otto righe B del canone portavano affermazioni che non reggevano** — B3 e B4 — e
nessuna delle due era un refuso: erano **conclusioni** scritte senza riaprire il file.

⚠️ **È esattamente ciò che E49 dice**: la riga B è una nota senza cartella, e un errore scritto
lì **si propaga a tutti i lotti futuri** invece che a una nota sola. La regola è nata a questo
gate e **il gate stesso ne ha fornito due casi**.

⚠️ **Il canone si accresce e si corregge, e la correzione resta visibile**: le due righe portano
ora il proprio ribaltamento scritto dentro, non riscritto in silenzio.

## 16. Il pattern del ri-giudizio del gate, e dove il ciclo si ferma (E26)

**19 rilievi su 6 note: 3 errori e 16 avvisi.** ⚠️ **I tre errori stanno tutti nella parte
riscritta oggi, nessuno in quella corretta oggi** — e nessun rilievo di classe «testo revocato
dato per vigente»: la riverifica del barrato ha tenuto.

Le famiglie sono due, e la prima è già sotto vigilanza:

**a) Il conteggio o l'inferenza data per fatto della fonte** — «quattro divieti», «tre
conseguenze», «sei voci», «è scarto», «tutte e tre costano denaro», la ratio dei divieti. ⚠️ **È
la specie del §11**, che ha già il suo criterio pre-registrato e si osserva al tema 3. **Cinque
istanze in sei note**: non si è spenta.

**b) L'affermazione che si smentisce dentro la nota stessa** — «non più X» dove i fatti
elencati dicono «non solo X»; «nessuno dei due cita l'altro» in una nota che riporta la
citazione; un titolo che dice «l'etichetta» dove il corpo dichiara di non sapere che cosa
finisca sull'etichetta. ⚠️ **È una specie nuova e non si emenda ora** (E28): la si nomina, e se
ricompare al tema 3 avrà il suo criterio.

⚠️ **Il ciclo si ferma qui.** Le correzioni sono applicate e la QA è tornata a zero errori, ma
**non si apre un altro giro**: E26 chiede di nominare il pattern, non di rincorrere la
convergenza.

## 17. I numeri di chiusura del gate (E44)

| Misura | Valore | Ora |
|---|---|---|
| Suite QA, perimetro **vault** | **121 ERRORI, 219 AVVISI** | 16:22:21 |
| Suite QA, perimetro di **riverifica** (31 note) | **0 ERRORI, 19 AVVISI** | 16:20:15 |
| Collaudo della suite | **24 difetti su 24** (erano 22) | 16:22:40 |
| Collaudo dei due tassi | **3 casi su 3**, nei due versi | 16:22:40 |
| Collaudo del CSV | **6 casi su 6** | 16:22:40 |
| Invarianza dell'estrattore di misura | **0 violazioni su 161 grezzi** | 16:23:15 |
| Emendamenti | **concordi a 49** | 16:23:04 |
| Matrice dei lotti | **160 grezzi, 18 elenchi, 0 guasti** | 16:23:04 |
| Tabella di tracciamento | **106 righe**, integra | 16:23:04 |
| CSV file × fatto | **334 righe, 6 campi per riga** | 16:23:06 |
| Note nel vault | **281**, di cui **248 di contenuto** | 16:23:15 |
| Grezzi citati / restanti | **43 / 117** | 16:23:15 |

⚠️ **Gli errori del vault non si muovono — 121 — e gli avvisi salgono di cinque**: quattro sono
i «riscontro in testo revocato» sulle due bozze, e nessuno è un difetto nuovo introdotto dal
gate. **Nessun grezzo è stato canonizzato in questa parte: era manutenzione.**

## 18. Che cosa il coordinatore deve sapere prima del tema 3

1. ⚠️ **Due righe del canone erano sbagliate, e il gate le aveva ratificate** — B3 e B4. Non è
   una svista di trascrizione: erano conclusioni scritte senza riaprire il file, ed è la ragione
   per cui E49 è nata a questo stesso gate.
2. ⚠️ **La PARTE 2.5 chiedeva di insegnare a `misura_due_tassi` le fonti multiple, e le sapeva
   già fare** dal lotto 2A. L'affermazione contraria è **mia**, sta nel rapporto di 2B-bis, ed è
   stata ratificata in buona fede: un fatto sullo strumento ricavato **guardando il risultato
   invece di leggere il codice**. Il difetto vero era la dichiarazione del dominio `allergeni`,
   ora corretta con le due guardie.
3. ⚠️ **La serie dei tassi non è stata riscritta**: il 9,1 % resta il numero misurato con lo
   strumento di allora (E46), e il primo lotto del tema 3 dichiarerà la versione che usa.
4. ⚠️ **Una specie d'errore nuova è stata nominata e non emendata** — l'affermazione che si
   smentisce dentro la nota — accanto a quella del §11 che è ancora aperta.
5. **Il tema 3 non è stato aperto in questa sessione**, e la PARTE 3 lo prevede: la manutenzione
   è stata piena, e i tredici grezzi con il loro ripacchettamento sono lavoro di apertura, non
   una coda.
