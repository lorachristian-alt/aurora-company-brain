# Rapporto del lotto 1C — metrologia e gas tecnici: parco strumenti, tarature, azoto

> **Cos'è** · Il rapporto di chiusura del terzo lotto della Sessione 4, da portare al gate.
> **Perimetro** · 2 grezzi: `elenco_attrezzature_taratura_strumenti_2026.csv` e
> `bolla_ingresso_azoto_alimentare_Nordgas_OCR.txt`.
> **Chiuso il** · 19/08/2026.

---

## 1. Il lotto, in una tabella

| | |
|---|---|
| Grezzi | **2** |
| Righe di strumento nell'elenco | **120** — la matrice ne dichiarava 121, errata registrata |
| Budget dichiarato | 12-18 note di contenuto |
| Prodotte | **27** note di contenuto |
| Scostamento | **+50 %** sul massimo del budget, **dichiarato in apertura e approvato** |
| Perché non si è spezzato | **E28** (approvato in apertura di questo lotto): si spezza sopra il +25 % **e** sopra le 30 note. 27 < 30 |
| Densità | **13,5 note per grezzo** — contro 9,5 (1B), 6,0 (1A) e 2,1 (pilota) |
| Note esistenti estese | 13 — 9 di contenuto e 4 hub d'area, più 4 `_index` |
| QA di lotto | **0 ERRORI, 9 AVVISI** |
| Giri di giudizio | **3** (`PROMPT_GIUDIZIO` v2), chiusi dalla regola d'arresto E26 |
| Emendamenti nati qui | **E28** |

### Le 27 note di contenuto, per cartella

**`areas\` (22)** — `fatto-datalogger-dl-001-in-taratura` · `fatto-due-registri-paralleli-della-metrologia` ·
`questione-due-registri-tarature-pt-104` · `questione-convalida-md-3200-due-registri` ·
`questione-convalida-md-1800-scaduta-o-valida` · `questione-sigla-kit-tasselli-ccp3` ·
`questione-posizione-md-3200-in-linea` · `fatto-tassello-aisi-clip-rotta` ·
`fatto-strumenti-taratura-scaduta-in-uso` · `fatto-catena-riferibilita-tarature-interne` ·
`fatto-strumenti-esclusi-da-taratura` · `fatto-verifica-metrologia-legale-bilance` ·
`fatto-buchi-registro-strumenti` · `fatto-due-elenchi-in-un-file-strumenti` ·
`fatto-strumenti-map-azoto-pkm-450` · `fatto-strumenti-cf-02-e-ccp4` ·
`questione-taratura-termoregistratore-cf-02` · `fatto-fornitura-gas-nordgas-06-05` ·
`fatto-certificato-analisi-gas-alimentari` · `fatto-accettazione-con-riserva-gas-06-05` ·
`questione-codici-lotto-azoto-06-05` · `fatto-azoto-due-vie-serbatoio-e-rampa`

**`data\` (2)** — `kpi-parco-strumenti-taratura-2026` (hub del tema) ·
`questione-azoto-quantita-e-livello-06-05`

**`entities\` (3)** — `entita-nordgas` · `entita-metrolab-taratura` · `entita-calservice-italia`

## 1-bis. I conteggi del vault a chiusura del lotto, da script

<!-- CONTEGGI DEL VAULT — generati da `06_operativo\qa\conta_stato.py` il 2026-08-19.
     Si incollano VERBATIM: non si ricompongono a mano, non si riscrivono in prosa. -->

| Grandezza | Valore |
|---|---|
| Note nel vault | **172** |
| di cui `_index` | 11 |
| di cui note-strumento del progetto | 6 |
| di cui note di diario (`sessione`, `daily`) | 2 |
| **di cui note di contenuto** | **153** |
| Note per cartella | areas 93 · entities 22 · data 22 · projects 8 · docs 7 · code 7 · concepts 5 · workspace 5 · self 1 · outputs 1 · sources 1 |
| Note per `type` | atomica 93 · conflitto 32 · entita 18 · hub 12 · index 11 · concetto 4 · sessione 2 |
| Questioni aperte (`type: conflitto`) | 32 |
| Grezzi in `sources\` | 160 |
| Grezzi citati da almeno una nota | **35** |
| Grezzi restanti | **125** |

---

## 2. Il criterio di aggancio: come 120 righe diventano 27 note

**È l'obbligo che il titolare ha messo su questo lotto al momento dello spezzamento**, e va
dichiarato prima dei risultati.

Una riga dell'elenco ha meritato di comparire in una nota **solo se rientra in una di queste
quattro classi**:

| Classe | Criterio | Esempi |
|---|---|---|
| **a** | lo strumento presidia un **punto critico di controllo** o un impianto già canonizzato | `DL-001` (CCP2), `TT-003` (CCP3), `TR-010` (allarmi CF-02), `CV-003` (azoto PKM-450) |
| **b** | la riga porta uno **stato anomalo dichiarato dal registro stesso** | i cinque `SCADUTO`, lo `SMARRITO`, i tre certificati «non trovato» |
| **c** | la riga **contraddice un documento già nel vault** | `MD-3200`, `MD-1800`, i canali del `PT-104` |
| **d** | la riga dichiara una **regola o un obbligo**, non un dato | metrologia legale, tarature interne contro `TS-005`, esenzioni dichiarate |

**Il risultato, contato da script:** **43 matricole su 120** sono nominate esplicitamente, in
**22 note** (le 27 nuove meno quelle della bolla, più le esistenti estese). Le altre **77
righe non hanno una nota propria e non ne avranno una**: vivono nei conteggi dell'hub
`kpi-parco-strumenti-taratura-2026`, che le classifica per stato e per ente di taratura senza
elencarle. **Nessuna riga ha una nota tutta sua**: anche le 43 nominate compaiono dentro note
che raccolgono un fatto, non un oggetto.

⚠️ **Campione al revisore: non un campione, tutte.** Il pacchetto dello strato di giudizio ha
contenuto **tutte** le note del lotto e il testo integrale dei grezzi citati, quindi le 13
note nate dal CSV sono state giudicate una per una, in due giri. La guardia contro la
sovra-atomizzazione chiedeva un campione: qui la copertura è totale, e il giudice **non ha
segnalato nessuna nota come non agganciabile a una domanda**.

---

## 3. Cosa ha trovato questo lotto

### 3.1 Aurora tiene due registri paralleli della stessa metrologia

È il fatto più importante del lotto, ed è una **famiglia nuova per il canone**: non una
divergenza fra due misure, ma **due sistemi di registrazione che censiscono gli stessi oggetti
e non concordano**.

| Strumento | Piano di manutenzione | Elenco attrezzature |
|---|---|---|
| Sonde del `PT-104` | 6 mesi e 3 mesi, **Analytica Veneta**, «rif. CCP2» | quattro canali, 12 mesi, **CalService LAT 087** |
| `MD-3200` | convalida **12 mesi**, `06-feb-26` → `06/02/27` | verifica **semestrale**, `04/03/2026` → `04/09/2026` |
| `MD-1800` | **`SCADUTO`** dal `03/04/26`, sollecitato due volte | **`Conforme`**, `IN USO`, scadenza `19/08/2026` |

⚠️ **L'`MD-1800` è il caso che ha una conseguenza oggi**: due stati opposti dello stesso
strumento, e la scadenza che il secondo registro gli dà cade **il giorno di questo rapporto**.

### 3.2 Sulla cella surgelati cinque registrazioni metrologiche stanno in due registri

Il verbale dell'ispezione sanitaria del 09/06 attesta «ultima verifica taratura **12/02/2026**»
per il termoregistratore della `CF-02`. Nessuno dei tre strumenti dell'elenco porta quella
data; il piano di manutenzione ne dà una quarta — «Registratore temperatura - verifica»,
eseguita il **`2026-02-28`** dall'officina interna — e una quinta registrazione, la taratura
della sonda `PT100-CF2` del `25-mar-26` affidata ad **Analytica Veneta** con nota «rif. CCP4».

**Cinque registrazioni in due registri, tre esecutori diversi sullo stesso impianto, e la data
resa all'autorità non è nessuna delle altre.** È la divergenza di specie nuova del lotto: uno dei due termini è un'**attestazione
verbalizzata in triplice copia davanti all'autorità sanitaria**.

### 3.3 L'azoto entra per due strade, e questo CHIUDE una divergenza invece di aprirla

Il quaderno del capoturno del 6/5 annota «bomb0la n0rdgas cambiata alle 16»; la bolla dello
stesso giorno consegna azoto **sfuso** in serbatoio e bombole di sola CO2. L'inventario di
magazzino — già nel vault dal pilota — registra **18 bombole di azoto «scorta rampa»** con
nota «rampa emergenza PKM-450».

**T17 si chiude come riconciliazione, non come divergenza**, ed è un esito diverso da
«divergenza chiusa»: l'archivio, letto per intero, **toglie** una contraddizione apparente.
La tabella di tracciamento distingue i due esiti, perché una riconciliazione è un risultato
del vault e un pareggio no.

### 3.4 La consegna del 06/05 ha tre codici e due numeri di bolla

`LOT-N-260502` su DDT `26/04512` (bolla) · `NG-26-0506` su DDT `BN-4471` (mass balance) ·
`NG26-0644` (inventario). Il gas è un additivo alimentare che va nella confezione: con tre
codici che non si richiamano, **l'unico elemento che lega le tre registrazioni è la data**.

⚠️ Il **certificato di analisi** `CA-26/0912` che la bolla richiama **non è in archivio**:
verificato con l'estrattore congelato su tutti i 160 file del manifest v1.1. Le analisi dei
due gas esistono solo come trascrizione dentro la bolla, e il laboratorio che le firma è
**interno al fornitore**.

### 3.5 Quattro delle nove divergenze nuove non vengono dai grezzi del lotto

Vengono dal **confronto con ciò che il vault già sapeva**: inventario di magazzino, mass
balance, piano di manutenzione, verbale ATS. È la conferma della giurisprudenza §4.14 — la
riconciliazione incrociata rende di più a ogni lotto che passa — e vale la pena dirlo con un
numero: **su 2 grezzi nuovi, 4 divergenze su 9 sono nate da documenti vecchi**.

---

## 4. Il budget sforato, e di che cosa è fatto lo scostamento

27 note contro un budget di 12-18: **+50 % sul massimo**. Lo scostamento è stato **proiettato
in apertura** (23 note previste) e portato al titolare prima di scrivere una riga, come vuole
E21; le 4 note in più rispetto alla proiezione sono nate dallo scorporo, ordinato dal
coordinatore, della questione unica sui due registri in **tre questioni più una nota che
nomina il pattern**.

**Di che cosa è fatto lo scostamento**, in ordine di peso:

| Voce | Note | Perché |
|---|---|---|
| Le divergenze fra registri | 5 | tre questioni, la nota del pattern, la questione del termoregistratore |
| La bolla dei gas | 6 | consegna, certificato, accettazione, codici, quantità, due vie dell'azoto |
| Lo stato del parco strumenti | 6 | scaduti, esclusi, buchi, due elenchi, catena di riferibilità, metrologia legale |
| Gli strumenti dei punti critici | 4 | datalogger CCP2, CF-02/CCP4, azoto PKM-450, tassello CCP3 |
| Apparato | 6 | l'hub del tema e tre schede entità, più due note di raccordo |

⚠️ **Il budget di 12-18 era costruito sulla densità del pilota** (2,1 note per grezzo). A
consuntivo la densità di questo lotto è **13,5**: il budget non era stretto, era **calcolato
con il modello sbagliato**. È la ragione per cui E28 è nato in apertura di questo lotto, e la
ricalibrazione dei lotti restanti è al §9.

---

## 5. Gli avvisi della QA, motivati

**0 ERRORI, 8 AVVISI**, in tre famiglie disgiunte che sommano al totale.

| Famiglia | Quanti | Motivazione |
|---|---|---|
| `summary` e `title` si sovrappongono per meno del 20 % | 6 | Sono le note-questione, il cui **titolo è una domanda** («La convalida è annuale o semestrale?») e il cui summary è **la risposta con i dati**: per costruzione condividono poche parole. Riscrivere il titolo per far salire la sovrapposizione peggiorerebbe la nota |
| Corpo fra 301 e 350 parole | 2 | `fatto-convalida-md-1800-scaduta` (309) e `fatto-strumenti-cf-02-e-ccp4` (311). Entrambe hanno ricevuto in questo lotto **una gamba nuova** — il secondo registro e il quarto strumento — e spezzarle separerebbe un confronto dal suo termine |

⚠️ **Nessun avviso di fonte inutile e nessuno di link mancante**: il giudice, indipendentemente,
ha confermato che **ogni fonte elencata sorregge almeno un'affermazione** in tutte e 28 le note
del pacchetto.

---

## 6. I passaggi di controllo

| Passaggio | Esito |
|---|---|
| **Rilettura preventiva dei «Perché conta»** contro le sole fonti (antidoto del lotto 1B) | 16 note ritoccate **prima** del primo giudizio |
| **QA di lotto**, primo giro | 14 errori: 9 locator `.csv` fuori grammatica, 3 di provenance, 2 su `llms.txt` |
| **Strato di giudizio, 1º giro** (v2) | 28 note: **16 pulite, 12 con rilievi**, tutti `afferma_oltre` |
| **Revisione col canone** | 9 divergenze di **categoria B** registrate nel canone in sezione datata, 2 riconciliazioni e 1 assenza verificata |
| **Correzioni propagate** | 15 correzioni, di cui 4 nate dalle **lacune di copertura** segnalate dal terzo compito |
| **Strato di giudizio, 2º giro** (E9) | *(vedi §6-bis)* |
| **Re-QA** | **0 ERRORI, 8 AVVISI** |

### I tre rilievi che valevano da soli il passaggio

1. **«La catena di riferibilità si chiude su `TS-REF`»** — falso. Il registro dichiara le
   tarature interne contro **`TS-005`**, che è tarato da MetroLab; `TS-REF` è marcato
   «RIFERIMENTO AZIENDALE» ma **nessuna riga lo mette a monte di nulla**. Avevo costruito
   un'architettura a due livelli che le fonti non dichiarano, e l'avevo scritta in due note.
2. **«I due registri non concordano su niente, nemmeno su chi esegue»** — falso su due righe
   su tre: su `MD-3200` e `MD-1800` **entrambi** i registri indicano Loma Systems Italia. La
   divergenza sull'esecutore vale solo per il `PT-104`.
3. **La lacuna di copertura sulla `CF-02`** — il piano di manutenzione contiene una voce
   «Registratore temperatura - verifica» del `2026-02-28` che nessuna nota citava. È il
   documento che rende la questione del termoregistratore molto più solida: senza quel
   rilievo, la nota avrebbe detto «nessuno dei tre strumenti porta quella data» quando la
   verità è «di date ce ne sono quattro, in tre documenti, con tre esecutori».

### 6-bis. I giri di giudizio, uno per uno

| Giro | Note nel pacchetto | Pulite | Con rilievi | Rilievi accolti |
|---|---|---|---|---|
| 1º | 28 | 16 | 12 | 12 su 12 |
| 2º | 29 | 21 | 8 | 8 su 8 |
| 3º | 29 | 22 | 7 | 7 su 7 |

**Tutti i rilievi dei tre giri sono stati accolti — 27 su 27**, e tutti di tipo
`afferma_oltre`: nessun falso allarme sul merito. I due falsi allarmi registrati al §7 sono
**lacune di copertura** respinte, non rilievi.

⚠️ **Il ciclo si chiude qui per la regola d'arresto E26**, non perché sia esaurito: il terzo
giro ha ancora prodotto rilievi, e in quel caso il lotto «si chiude solo dopo che il rapporto
ha NOMINATO il pattern che li rigenera». I pattern sono due, e sono diversi fra loro.

⚠️ **Il pattern che il 2º giro ha nominato, e che vale per i lotti successivi: il corpo
cautela, l'intestazione afferma.** Cinque rilievi su otto stavano nel `summary` o nel titolo, e
in tre casi il corpo della nota diceva la cosa giusta mentre il summary la irrigidiva —
`fatto-catena-riferibilita-tarature-interne` scriveva nel corpo che nessuna riga mette `TS-REF`
a monte di nulla, e nel summary che «la catena si chiude su `TS-REF`».

**È un pattern diverso da quello del lotto 1B** (il *contesto importato*, la frase scritta per
far capire che porta dentro un fatto che le fonti non contengono), e ha una causa meccanica
propria: **il summary si scrive per primo e si corregge per ultimo**. Quando una correzione
attenua il corpo, l'intestazione resta com'era.

**Antidoto, dal lotto 2 in poi:** dopo ogni giro di correzioni, **rileggere il `summary` e il
`title` di ogni nota toccata come se fossero note a sé**, contro le sole fonti. In questo lotto
l'antidoto ha trovato **due casi in più** di quelli segnalati dal giudice —
`fatto-due-registri-paralleli` («esecutori diversi» era vero solo per il `PT-104`) ed
`entita-metrolab-taratura` («la maggior parte degli strumenti»: 32 su 120 è il numero più alto
fra gli enti, non la maggioranza). Al terzo giro **sei rilievi su sette stavano ancora lì**,
il che dice che l'antidoto va applicato **a ogni giro**, non una volta sola.

### Il secondo pattern, e vale più del primo: LA FONTE TRASVERSALE NON CITATA

Il terzo giro ha segnalato **quattordici lacune di copertura**, e undici indicavano **lo stesso
documento**: `manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt`.

⚠️ **In due casi quel documento conteneva esattamente ciò che la nota dichiarava mancante:**

| La nota diceva | Il manuale HACCP dice |
|---|---|
| «Che l'`MD-1800` sia un punto critico di controllo **non è scritto in queste fonti**» | fase 12 del diagramma: l'`MD-1800` è **«gestito come CCP assimilato al CCP3»**, con medesimi limiti, frequenze e modulistica |
| «Che da questo discenda l'impossibilità di intercettare un frammento di plastica è una **lettura dichiarata**» | nota all'analisi dei pericoli: il pericolo «frammenti di plastica da organi macchina» **non è rilevabile dal metal detector** |
| «servirebbe una procedura che dichiari se la convalida del CCP3 sia annuale o semestrale» | scheda del CCP3: **«verifica annuale del costruttore»** |
| «in archivio non c'è una procedura di gestione delle apparecchiature di misura» | **`PRP-03`** «Manutenzione preventiva impianti e **taratura strumenti**», piano annuale a cura di Dal Maso I. |

E altre due che cambiano il peso delle questioni: il CCP2 prescrive **«taratura sonde
semestrale (centro LAT)»** — e **nessuno dei due registri la rispetta per intero**, uno ha la
frequenza e non l'accreditamento, l'altro l'accreditamento e frequenza doppia; il magazzino di
Via Palù 3/A è **dentro il campo di applicazione** del sistema HACCP, il che rende i suoi tre
strumenti scaduti un fatto di conformità e non di logistica.

**Perché è successo, e perché ricapiterà.** Il manuale HACCP è **la fonte prescrittiva del
vault**: non parla di strumenti, parla di limiti, frequenze e responsabilità. Chi canonizza un
grezzo che *registra* qualcosa cerca gli altri documenti che *registrano* la stessa cosa — i
due registri, l'inventario, il verbale — e non pensa al documento che **prescrive** come quella
cosa vada fatta. La riconciliazione incrociata di §5.1-bis ha funzionato benissimo in
orizzontale e ha mancato la verticale.

**Antidoto, dal lotto 2 in poi:** ⚠️ **quando una nota tocca un punto critico di controllo, una
taratura, una frequenza di verifica o una responsabilità di processo, il manuale HACCP si apre
e si cita — o si dichiara perché non serve.** È il documento che governa quelle grandezze, ed è
già nel vault dal pilota: non citarlo non è una svista di copertura, è una risposta incompleta
data al posto di una completa.

---

## 7. Categoria C — i falsi allarmi, perché non tornino al lotto dopo

| Segnalazione | Perché è stata respinta |
|---|---|
| «`fatto-datalogger-dl-001` non cita la scheda di manutenzione, che misura la stessa grandezza» | **Deliberato.** Quella gamba ha già la sua nota padrona — `fatto-sonde-pt-104-in-taratura`, scritta in 1A — e il confronto fra i due registri ha una questione dedicata. Citarla anche qui creerebbe una **doppia padrona** (metodo_03 §7.4) |
| «`fatto-strumenti-map-azoto` non cita il rapporto di fermo macchina, che misura la stessa grandezza» | La nota afferma **solo che quegli strumenti erano tarati**, e non riporta nessun valore di consumo o di pressione. Il rapporto di fermo è la fonte del racconto del fermo, che ha la sua padrona altrove |
| Rilievi su `fatto-certificato-analisi-gas-alimentari` e su `fatto-strumenti-map-azoto` per frasi **già corrette** | ⚠️ Non è colpa del giudice: **il pacchetto era stato generato prima della rilettura preventiva**, quindi ha giudicato una versione superata di due note. Vedi il candidato emendamento al §8 |

---

## 8. Candidati emendamento, dal lotto 1C

| # | Dove | Che cosa | Perché |
|---|---|---|---|
| 1 | §9.5, passo 4 | **Il pacchetto per lo strato di giudizio si genera DOPO le correzioni pre-giudizio, non prima** | In questo lotto la rilettura dei «Perché conta» ha toccato 16 note **dopo** la generazione del pacchetto: due rilievi su dodici riguardavano testo che non esisteva più. Costa un comando, e toglie rumore dal verdetto |
| 2 | §7, perimetro di lotto | **Il perimetro di lotto deve comprendere le note MODIFICATE dal lotto, non solo quelle che citano i suoi grezzi** | Estendendo `fatto-convalida-md-1800-scaduta` e `fatto-cariche-f-gas` ho introdotto due difetti — una data senza fonte e una nota oltre le 350 parole — che la **QA di lotto non vedeva**, perché quelle note non citano i grezzi di 1C. Li ha presi la QA a perimetro vault, che però non è quella che si lancia a ogni lotto |

⚠️ Il secondo è un **buco vero nella rete**, non un fastidio: chi estende una nota vecchia
esce dal perimetro che lo controlla.

---

## 9. La ricalibrazione della matrice — e perché il calcolo lineare va buttato

**Ordinata dal coordinatore alla chiusura di questo lotto.** I numeri vengono da
`06_operativo\ricalibra_budget.py`.

### 9.1 La densità misurata

| Lotto | Grezzi | Note di contenuto | Densità |
|---|---|---|---|
| pilota L26130 | 22 | 46 | 2,1 |
| 1A | 7 | 42 | 6,0 |
| 1B | 4 | 38 | 9,5 |
| 1C | 2 | 27 | 13,5 |
| **dopo il pilota** | **13** | **107** | **8,2** |

### 9.2 Il calcolo che il coordinatore ha chiesto, e il suo risultato assurdo

Applicando la densità misurata (8,2 per i lotti di contenuto, 6,2 per il normativo, 2,5 per il
rumore) ai 125 grezzi restanti si ottiene: **903 note di contenuto** e **36 lotti invece di 9**,
con un vault finale di oltre **mille note**. Ogni lotto restante supererebbe il tetto di 40
note di E28, rumore compreso.

### 9.3 Perché quel risultato è un artefatto

**Le note per lotto sono molto più stabili del rapporto note/grezzo**, e i numeri lo dicono:

| Grandezza | min | max | dispersione sulla media |
|---|---|---|---|
| Note prodotte per lotto | 27 | 46 | **50 %** |
| Densità note/grezzo | 2,1 | 13,5 | **147 %** |

I grezzi per lotto sono passati **da 22 a 2** mentre le note restavano **fra 46 e 27**. Ciò che
si mantiene costante non è la densità: **è il lotto**. Moltiplicare una densità misurata su
lotti da 2-7 grezzi per lotti da 12-18 grezzi assume che la produzione di note dipenda dal
numero di documenti, e i consuntivi dicono il contrario.

**Le tre cause plausibili, e nessuna è misurabile con i dati di oggi:** (a) i lotti chiusi
contengono i grezzi più densi del corpus, scelti apposta per primi; (b) più il vault sa, più
ogni grezzo produce riconciliazioni — la causa che il coordinatore indica, e che questo lotto
conferma con 4 divergenze su 9 nate da documenti vecchi; (c) **il costo fisso di apparato** —
hub, schede entità, `_index` — si spalma su meno grezzi quando il lotto è piccolo: in 1C sono
4 note su 27.

### 9.4 La proposta: budget a capacità, non a stima

1. **Il budget di un lotto smette di essere una stima di pianificazione e diventa una
   capacità**: ogni lotto punta a **25-35 note di contenuto**, che è la fascia in cui i quattro
   lotti chiusi sono caduti tutti.
2. **Quanti grezzi ci stiano dentro si decide in apertura contando i fatti** (E21), non in
   pianificazione: è già la regola, e questa proposta la rende l'unica.
3. **I lotti 2-10 si spezzano prima di aprirli**, in pacchetti tematici da **3-5 grezzi** per il
   contenuto e fino a **8-10** per il rumore. Il numero dei lotti passa da 12 a **circa 28-30**,
   e questo va detto perché **cambia il calendario delle Sessioni 4-5**, non solo la matrice.
4. **La matrice registra le stime vecchie come superate**, con la riga datata: il registro delle
   modifiche è cronologia, non fotografia.

⚠️ **Quello che non propongo:** riscrivere le fasce dei lotti 2-10 con i numeri del §9.2. Una
stima sbagliata sostituita da una stima peggiore non è una ricalibrazione.

---

## 10. Conflitti: chiusi, aperti dichiarati, tracciati

| Esito | Quanti | Quali |
|---|---|---|
| **Chiusi come riconciliazione** | 1 | **T17** — l'azoto per due vie: la contraddizione apparente sparisce |
| **Chiusi** | 1 | **T20** — la base metrologica dell'arbitrato datalogger/cartaceo c'è. ⚠️ La chiusura ha aperto **T44** |
| **Aperti dichiarati** (nuovi) | 7 | T25, T26, T32 (tracciati e ora chiusi come questioni), **T43** MD-1800, **T44** PT-104, **T45** termoregistratore CF-02, **T46** codici azoto, **T47** quantità azoto, **T48** ritaratura flussimetro |
| **Tracciati** (gamba mancante altrove, E25) | 6 | **T49-T54**: costo taratura nel report OpEx, cruscotto KPI, notifica ATS, registro MOCA, quaderno del tecnologo, ordini d'acquisto |
| **Gamba acquisita, riga ancora aperta** | 1 | **T40** — il magazzino di Via Palù: tre strumenti scaduti su tre e un verbale che lo chiama unità locale separata, ma **il secondo sito non ha ancora una nota padrona** |

---

## 11. Cosa chiedo al titolare

1. **Approvare la chiusura del lotto 1C** con lo scostamento di budget dichiarato: 27 note
   contro 12-18, sotto il tetto di 30 fissato da E28 lo stesso giorno.
2. **Decidere sulla ricalibrazione (§9).** Non porto una tabella di budget nuovi, perché il
   calcolo lineare dà 903 note e 36 lotti ed è un artefatto. Porto una proposta di metodo —
   budget a capacità, 25-35 note per lotto, grezzi decisi in apertura contando i fatti — e la
   conseguenza: **il piano passa da 12 a circa 28-30 lotti**, e questo cambia il calendario
   delle Sessioni 4-5.
3. **Approvare i due candidati emendamento del §8**, o rimandarli al gate finale. Il secondo
   — il perimetro di lotto che deve comprendere le note *modificate* — è un buco vero: due
   difetti introdotti in questo lotto non li ha visti la QA di lotto.
4. **Prendere atto dei due pattern del §6-bis**, che valgono per tutti i lotti successivi. Il
   secondo, la fonte trasversale non citata, ha una conseguenza immediata: **le note dei lotti
   già chiusi che parlano di CCP potrebbero avere la stessa lacuna.** Non l'ho verificato,
   perché sarebbe una revisione di lotti chiusi e non me la sono presa da solo.

⚠️ **Il punto 4 è quello su cui chiedo una decisione esplicita, e ho già il numero.** Nel vault
ci sono oggi **30 note che nominano un punto critico di controllo e non citano il manuale
HACCP**. Non sono trenta difetti: la maggior parte lo nomina di passaggio, in una tabella o in
un rimando. Ma è l'elenco da cui partire, e uno script lo rigenera in un secondo. Se la cosa si
guarda al gate finale invece che adesso, si guarderà con la copertura del vault in mano e con
molte più note dentro.
