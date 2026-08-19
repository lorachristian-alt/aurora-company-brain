# Rapporto del lotto 2A — il lavaggio CIP

> **Cos'è** · Il rapporto di chiusura del primo lotto del tema 2, da portare al gate.
> **Perimetro** · 3 grezzi: `log_lavaggio_CIP_linea1_maggio.log`,
> `IO-05_istruzione_operativa_lavaggio_CIP.docx`,
> `scheda_sicurezza_detergente_acido_lavaggio_CIP.txt`.
> **Chiuso il** · 19/08/2026, **con la coda dei controlli finali dopo la mezzanotte**: i
> report della suite portano quindi due date, `2026-08-19_02a` e `2026-08-20_02a`, e la
> seconda è quella dell'ultima misura. ⚠️ I `data_nota` delle note restano al **19/08**, che
> è il giorno in cui sono state scritte: cambiarli a posteriori romperebbe la relazione
> `data_fatto ≤ data_nota` già verificata su ciascuna.
> ⚠️ **È anche un ESPERIMENTO**: primo lotto canonizzato sotto E29 ed E36, e il §7 porta i
> **due tassi distinti** che il gate deve pesare.

---

## 1. Il lotto, in una tabella

<!-- PERIMETRO DEL LOTTO — generato da `06_operativo\conta_perimetro_lotto.py`
     il 2026-08-19. Si incolla VERBATIM: i numeri non si ricompongono a mano. -->

| Voce | Valore |
|---|---|
| Specie del lotto | **lotto di canonizzazione** |
| Grezzi nell'elenco | **3** |
| Note **candidate** dallo script di apertura | **10** |
| Note **toccate** in corso di lotto (E32) | **7** |
| Note **nate** nel lotto | **33** — 30 contenuto · 3 note-strumento |
| **Note controllate in tutto** | **50** |

| | |
|---|---|
| Capacità attesa | **25-35 note di contenuto** (E31) |
| Prodotte | **30** di contenuto — **dentro la fascia**, nessuno scostamento da dichiarare |
| Densità | **10,0 note per grezzo** *(calcolato: 30 su 3)* — contro 13,5 (1C), 9,5 (1B), 6,0 (1A), 2,1 (pilota) |
| Note riaperte per riconciliazione verticale (E37) | **10, corrette 4** |
| Perché le riaperte non spezzano il lotto | 10 riaperte < 30 nuove: la soglia di E37 non scatta |
| Giri di giudizio | **tre** — vedi §5 |
| QA di lotto | **0 ERRORI**, 44 avvisi motivati al §4 |

---

## 2. L'apertura, e perché il taglio è qui

Il tema 2 era già ridisegnato in 2A/2B/2C nella matrice dal 19/08, ma il ridisegno viveva
**solo in quella tabella**: all'apertura è diventato tre elenchi veri in `qa\lotti\`, e
`lotto_02_igiene.txt` non esiste più. `verifica_matrice_lotti.py` resta verde — 160 grezzi,
0 scoperti, 0 guasti, 16 elenchi.

Il taglio tiene insieme il **log** e l'**istruzione che lo prescrive**: separarli metterebbe
il registro in un lotto e la regola che lo giudica in un altro, cioè il difetto che il lotto
1C ha pagato col manuale HACCP.

### E37 scatta all'apertura, ed è il primo lotto in cui accade

`IO-05` e la scheda di sicurezza sono **fonti prescrittive**, e sono proprio le fonti del
log. E37 impone quindi di riaprire, prima di scrivere, le note già nel vault che parlano di
ciò che quelle fonti governano.

⚠️ **Lo strumento non c'era e si è dovuto costruire.** `candidate_r1.py` era scritto per il
solo lotto R1: perimetro fisso, criterio fisso. Ha acquistato una **modalità ristretta**
(`--dominio cip --lotto lotto_02a_cip`) che cambia **entrambe** le condizioni del criterio,
non solo l'elenco delle fonti:

| Condizione | Nel lotto R1 | In modalità ristretta |
|---|---|---|
| 1 — di che cosa parla la nota | una delle cinque famiglie prescrittive | le **espressioni del dominio**: CIP, lavaggio, sanificazione, risciacquo, conducibilità, soda, detergente, PAA, igiene |
| 2 — quale fonte le manca | una fonte prescrittiva qualsiasi, o il manuale per i punti critici | **le due fonti del lotto**, e nessun'altra |

⚠️ **Le due metà non si separano**, ed è scritto nel codice: le fonti da sole darebbero il
criterio generico su un elenco più corto — cioè la forma di E29 che E36 ha corretto — e le
espressioni da sole non direbbero quale fonte manca. **Il fix è monotono**: aggiunge un
aggancio e non ne allenta nessuno, e il comportamento di default sul lotto R1 è stato
verificato **identico** confrontando l'output con quello della versione committata.

**Esito:** 10 note riaperte, su 156 valutate.

---

## 3. Che cosa il lotto ha trovato

### Il fatto centrale: il PASS del pannello non è l'accettazione di IO-05

`fatto-cip-fuori-criterio` è la nota padrona, ed è una **contraddizione con vincitore già
registrata**: prevale `IO-05`, il log resta com'è, **nessuna questione si apre**. Ma il
confronto, fatto sui numeri, è più largo di quanto la matrice prevedesse:

| Parametro | Prescritto | Registrato | Fuori |
|---|---|---|---|
| Durata delle sei fasi | 10 · 30 · 10 · 20 · 15 · 15 min | 5 · 20 · 5 · 15 · 10 · 10 min | **6 fasi su 6**, sempre più corte |
| Portata | 15 m3/h | 8,4-10,0 m3/h | **170 letture su 170** |
| Temperatura alcalina | 75-80 °C | 74,0-76,0 °C | 57 letture su 116 |
| Temperatura acida | 60-65 °C | 56,2-61,0 °C | 64 letture su 84 |

⚠️ **La radice meccanica è nella forma del criterio, non nella disattenzione di chi lava.**
L'unica soglia che il pannello implementa è `COND<45.0` in fase soda — un controllo di
**concentrazione del detergente**, che infatti ha fermato due cicli. Il criterio di
accettazione di `IO-05` riguarda invece la **conducibilità del risciacquo finale** ed è
espresso come **scarto dall'acqua di rete**: un valore che il pannello non acquisisce e che
il log non registra mai.

⚠️ **Perciò quel criterio non è verificabile sul tracciato, e lo si dichiara invece di
aggirarlo.** L'unica cosa che i numeri permettono di dire, con la sua condizione, è che il
valore assoluto più basso del mese — 300 µS/cm — è già sei volte il **solo margine** ammesso.

### Le tre divergenze nuove, tutte fra le due fonti prescrittive del lotto

Non sono divergenze fra registri: sono **due documenti prescrittivi in vigore che non
concordano**, ed è una specie che la tabella di tracciamento non aveva ancora.

| # | Divergenza | Nota |
|---|---|---|
| T67 | Il detergente acido: `IO-05` prescrive `CHEMIFOOD AN-15` al 15 %, l'unica scheda in archivio è dell'`ACIDFOOD CIP 25` al 20-25 % con acido fosforico. **Nessuna delle due sigle compare nell'altro documento** | `questione-prodotto-acido-cip-an-15-o-acidfood-25` |
| T68 | I DPI: neoprene e filtro `B-P2` per l'istruzione, butile o fluoroelastomero classe 6 e filtro `E` per la scheda | `questione-dpi-cip-due-prescrizioni` |
| T69 | Il lavaocchi: verifica **settimanale** per la scheda, **mensile** per l'annotazione incorporata in `IO-05` | `questione-frequenza-verifica-lavaocchi-cip` |

⚠️ **T67 pesa oltre sé stessa**: se i due documenti non parlano dello stesso prodotto,
l'archivio **non ha la scheda di sicurezza del prodotto in uso**, e ogni confronto fra le
due fonti perde il presupposto. È la ragione per cui la cautela è stata propagata su tutte
le note che ne discendono — vedi §6.

### T21 e T29 si chiudono, ed erano duplicate fra loro

La sonda di conducibilità del `CIP-01` ha la taratura scaduta dall'`08/04/2026`, e la
colonna delle note del piano di manutenzione **rimanda al log**: «sollecitato da QA -
allarmi sonda su log maggio». Il log contiene ciò che quella riga annunciava: **due**
`ALM_COND_PROBE OPEN_CIRCUIT`, il 14/05 e il 28/05, e in **entrambi** i casi il pannello
chiude il ciclo `ESITO=PASS` lasciando in coda «VERIFICA MANUALE RICHIESTA».

Non era una divergenza fra due fonti: era una **catena** che aspettava la seconda metà. È il
terzo caso di righe duplicate nel seme della tabella, dopo T22/T30.

---

## 4. La QA di lotto

**0 ERRORI, 44 AVVISI.** Le famiglie, e perché sono avvisi e non difetti:

| Famiglia | Quanti | Motivazione |
|---|---|---|
| corpo fra 301 e 350 parole | 9 | Note dense per costruzione: ciascuna porta una tabella di parametri e il confronto con la fonte che li prescrive. Spezzarle separerebbe il valore dal suo criterio, che è precisamente ciò che questo lotto esiste per tenere insieme |
| `summary` oltre 250 caratteri | 11 | Sono le note che enunciano una **regola decisionale** — quale fonte prevale, quale limite vale — e E18 impone che il `summary` la porti: è ciò che il retrieval mostra per primo |
| `summary`/`title` sotto il 20 % di sovrapposizione | 6 | Voluto: il titolo nomina l'oggetto, il riassunto porta il numero. Ispezionati a mano, uno per uno |
| lontana dall'`_index` della propria cartella | 5 | Il loro **hub proprio** è `macchina-cip-01`, che sta in `entities\`: sono a due salti dal proprio hub e dall'`_index-entities`, non dalla porta di `areas\`. È un indizio di collocazione, e la collocazione è quella giusta — l'hub dell'impianto è dove un lettore le cerca |
| altri | 9 | tag, wikilink minimi su note di rimando |

---

## 5. I giri di giudizio

*(sezione completata alla chiusura — vedi §5.3)*

### 5.1 Lo strumento di taglio, e la lezione di §4.31 messa in pratica

Il pacchetto del lotto è di **598.571 caratteri**: non entra in un contesto pulito, e va
tagliato. È esattamente lo strumento che nel lotto R1 **scartava l'appendice delle fonti**,
mandando i giudici a confrontare le note con sé stesse.

Il nuovo `taglia_pacchetto.py` fa tre cose che il precedente non faceva:

1. porta a **ogni** fetta il testo integrale delle fonti che le note di quella fetta citano;
2. **si rifiuta di scrivere** una fetta priva di appendice, o con appendice vuota — è una
   guardia, non un controllo di cortesia;
3. scrive in testa a ogni fetta, per il giudice, che **dichiarare degradato il proprio
   ingresso è un esito legittimo** (§4.31).

⚠️ **E ha funzionato in tutti e sei i giudizi**: ogni giudice ha aperto la risposta
verificando l'ingresso, e tutti e sei l'hanno dichiarato **completo**, elencando le fonti
trovate. La riga di §4.31 non è rimasta una massima: è diventata il primo paragrafo di sei
verdetti.

### 5.2 Primo giro — 12 rilievi accolti su 40 note

⚠️ **Uno scostamento da E33, dichiarato.** Il pacchetto del primo giro è stato generato dopo
la QA, ma **sei note su quaranta** sono state modificate dopo, nella seconda tornata della
rilettura del passo 2-bis. Nessun rilievo del giro 1 è caduto su testo inesistente — i sei
rilievi su quelle note riguardavano parti non toccate — ma la regola dice che il pacchetto
si genera **per ultimo**, e qui non lo è stato. Il pacchetto del secondo giro è stato
rigenerato dopo la fine di tutte le correzioni, come E33 prescrive.

I rilievi accolti, per classe:

| Classe | Quanti | Il caso |
|---|---|---|
| **Attribuzione di ruolo non nelle fonti** | 3 | «il capo officina» detto di `Dal Maso I.` in tre note diverse: `IO-05` lo nomina e **non ne dichiara il ruolo**. Il manuale HACCP sì, ma non è fra le fonti di quelle note. È il movimento del `PARLANTE_3` di metodo_03, ripetuto |
| **Nozione tecnica esterna** | 3 | che cosa filtrino le classi `B-P2` ed `E`; la turbolenza come azione meccanica; «la percentuale del principio attivo è ciò su cui si calcola la diluizione» |
| **Giudizio di conformità** | 2 | «è il documento che la legge impone di avere per il prodotto realmente in uso» |
| **Errore vero su una fonte letta male** | 1 | ⚠️ Il migliore dei dodici: «il prerisciacquo, **l'unica** fase alimentata con acqua di rete» — `IO-05` assegna acqua di rete **anche** al risciacquo intermedio. Il giudice ha letto la tabella meglio di chi ha scritto la nota |
| **Fonte che non aggancia più nulla** | 1 | accorciando una nota per rientrare nel tetto di parole era rimasta la fonte senza l'affermazione che sorreggeva |
| **Premessa non qualificata** | 2 | «lo stesso carrello da cui era stata presa la guarnizione»: il verbale non nomina né la guarnizione né la riparazione |

### 5.3 Secondo giro — 7 rilievi accolti su 41 note, e due erano falsi miei

Il pacchetto è stato **rigenerato dopo la fine delle correzioni**, come E33 prescrive.

| Fetta | Note | Rilievi accolti |
|---|---|---|
| 1 | 14 | **4** |
| 2 | 14 | **1** (erano 5 al primo giro) |
| 3 | 13 | **2** |

⚠️ **Due dei quattro rilievi della prima fetta erano errori di fatto veri, e le note
affermavano il falso.** Non erano sfumature di prudenza: erano frasi sbagliate sui dati.

- «con la sonda in circuito aperto **quel controllo non è stato eseguito**» — falso: il
  pannello **rimisura** cinque minuti dopo il guasto, con flag `OK`, e chiude su quella
  lettura. Il difetto vero è più sottile e più forte di quello che avevo scritto: il
  controllo è stato eseguito **da uno strumento che si era appena dichiarato in circuito
  aperto**, e nessun grezzo attesta che sia stato verificato in mezzo.
- «l'11/05 è **l'unico giorno** di maggio con due cicli» — falso: anche il 06/05 e il 21/05
  ne hanno due, e sono i giorni degli `ABORT`, dove il secondo ciclo è la ripartenza del
  primo. Il fatto vero dell'11/05 è un altro: è l'unico giorno in cui i due cicli **non si
  spiegano l'uno con l'altro**.

Gli altri cinque erano attribuzioni non dichiarate come inferenze, nozioni tecniche esterne
alle fonti, e una sezione di hub che parlava di una fonte non sua.

### 5.4 La revisione col canone — 6 rilievi di categoria A, 9 di categoria B, 0 di categoria C

Il revisore ha riprodotto **in modo indipendente tutti i conteggi** delle note di misura, e
tornano al numero. Poi ha trovato quello che il giudizio non poteva trovare, perché il
giudice non ha il canone e non vede fuori dal pacchetto.

⚠️ **Due delle sei A sono ASSENZE DICHIARATE FALSE**, ed è la violazione di E3 — «mai
dichiarare un'assenza senza ricerca su TUTTO `sources\`»:

| L'assenza che avevo scritto | Che cosa c'era davvero |
|---|---|
| «il registro `MOD-HR-11` **non è fra i grezzi dell'archivio**» | `MOD-HR-11` compare in **dieci grezzi**, e uno di essi — il manuale HACCP — **era già fra le fonti di quella nota** |
| «quale sia davvero il valore dell'acqua di rete **l'archivio non lo dice**» | il piano di autocontrollo dell'acqua lo misura: rete di ingresso, **486 µS/cm** |

⚠️ **Le due assenze erano state scritte con la formula giusta — «verificata su tutto
`sources\`, manifest v1.1» — senza che la ricerca fosse stata fatta su tutto `sources\`.**
La formula di E3 esiste per rendere verificabile l'assenza, e usarla senza il gesto che
attesta la rende **peggiore del silenzio**: dà a un'affermazione falsa la forma di una
verificata. È l'errore più grave del lotto, ed è di classe, non di dettaglio: le due note
sono nate a ore diverse e con fonti diverse.

**Come sono state chiuse, e perché non nello stesso modo.** La prima con una ricerca vera e
una riformulazione — le fonti di quella nota non dicono chi fosse abilitato, e il registro
sta in un grezzo del lotto 8: riga **T73**. La seconda **non poteva** essere chiusa scrivendo
il valore: 486 µS/cm sta in un grezzo del **lotto 2B**, e il divieto 9-bis vieta di usarlo
prima. La nota dichiara quindi il criterio non verificabile **sulle proprie fonti** — che è
vero — e la riga **T72** porta l'obbligo per 2B.

⚠️ **E qui il canone e il vault si separano, per la prima volta in modo dichiarato.** Il
canone conosce il limite in valore assoluto — **536 µS/cm**, cioè 486 più i 50 di margine —
e con quello conta **18 cicli su 28** sopra soglia. Il conteggio è stato riprodotto ed è
esatto. Ma **quel numero non è scrivibile nel vault oggi**: nasce da un grezzo non ancora
canonizzato, e scriverlo sarebbe una fuga di canone della stessa specie delle due che il
progetto ha già pagato. La distanza fra i due si chiude con una riga di tracciamento, non
con una deroga.

Le **nove divergenze di categoria B** sono nel canone, in sezione datata del 19/08/2026.
⚠️ Hanno una caratteristica comune che le distingue da tutte le altre registrate finora:
**non sono registri che si contraddicono, sono due documenti PRESCRITTIVI in vigore che non
concordano** — l'istruzione operativa e la scheda di sicurezza. Fino a qui il canone
raccoglieva divergenze fra documenti che *registrano*, o al più fra un registro e la fonte
che lo governa (T64). Qui chi lavora ha davanti **due istruzioni valide che gli dicono cose
diverse**.

Il revisore ha inoltre segnalato **zero casi di categoria C** e, sulla
**sovra-atomizzazione**, ha provato dodici note contro una domanda plausibile:
**nessuna risulta non agganciabile**. Le due più a rischio — le due fette della scheda di
sicurezza — reggono perché sono i due termini che le questioni B1 e B2 mettono a confronto,
e ciascuna ha la propria controparte in `IO-05`.

### 5.5 Che cosa la revisione ha aggiunto al lotto

Tre cose che il lotto non aveva, e che sono diventate contenuto:

1. **Le quattro non conformità del CIP nel 2026** — `fatto-nc-cip-2026`. Il registro delle
   NC era già canonizzato e nessuna nota del lotto lo aveva interrogato sul CIP. ⚠️ La
   `NC-2026-039` del 03/03 dimostra che **il criterio di conducibilità in Aurora si applica
   davvero**: quando un lavaggio esce fuori soglia si apre una NC e il lavaggio si ripete. E
   la `NC-2026-113` del 29/05 spiega un silenzio del tracciato — la concentrazione si misura
   **a mano, per titolazione**, e quel giorno il kit era esaurito.
2. **Lo scarto d'ORDINE della sanificazione**: cade fra acido e risciacquo finale, mentre
   l'istruzione la numera come fase 6, in coda. Nessuna nota lo dichiarava.
3. **Il 10/05 è l'unica giornata di produzione del mese senza un lavaggio avviato**, ed è la
   domenica del lotto reclamato. Il conteggio dei «giorni con righe» lo nascondeva, perché
   quel giorno porta la coda del ciclo della sera prima.

### 5.6 Terzo giro — 9 rilievi accolti su 41 note

| Fetta | Note | Rilievi accolti |
|---|---|---|
| 1 | 14 | **4** |
| 2 | 14 | **2** |
| 3 | 13 | **3** |

I tre giri, in fila: **12 · 7 · 9**. Il ciclo **non converge**, e non converge in un modo
particolare: i rilievi non sono gli stessi che tornano — quelli corretti restano corretti —
ma ne emergono di nuovi **della stessa specie**, su note diverse, a ogni passata.

⚠️ **Uno dei nove ha mostrato che una correzione del giro 2 non era andata a segno**: la
frase «è la prima volta che la ricambistica viene contestata» era stata sostituita in un
turno in cui la sostituzione **fallì in silenzio**, e nessuno se ne accorse perché la QA
resta verde su una frase che c'è ancora. L'ha ripresa il giudice al giro dopo.

### 5.7 Il pattern nominato al terzo giro (E26): L'ATTRIBUTO CHE LA FONTE NON DÀ

Il terzo giro ha prodotto ancora rilievi accolti. **E26 vieta di rispondere con un quarto
giro**: il lotto si chiude dopo che il rapporto ha nominato la classe che li rigenera.

⚠️ **La classe c'è, ed è la stessa dal primo giro.** Messi in fila, i rilievi dei tre giri
sono quasi tutti lo stesso movimento: **attribuire a un soggetto un ATTRIBUTO che la fonte
non dà.** L'attributo cambia di volta in volta — un ruolo, una competenza, un primato,
un'identità fra due eventi, una causa, una categoria — ma il gesto è identico: la nota
aggiunge la proprietà che rende il soggetto comprensibile, e quella proprietà **viene da
altrove**.

| Giro | Il soggetto | La qualifica che la fonte non dà |
|---|---|---|
| 1 | `Dal Maso I.`, in **tre** note diverse | «il capo officina» — `IO-05` lo nomina e basta |
| 1 | il filtro `B-P2` e il filtro `E` | «protegge da gas inorganici» / «dai vapori acidi» — le fonti danno le sigle, non le funzioni |
| 1 | la scheda di sicurezza | «è il documento che la legge impone di avere» |
| 2 | `POPESCU_I` | «è [[entita-ionut-popescu]]», dato per fatto mentre per `BISSOLI_M` la stessa cosa era dichiarata inferenza |
| 2 | il verbale dell'ispezione | «è la prima volta che viene contestata da un'autorità pubblica» |
| 3 | `ing. M. Fantin` | «approvata **dalla direzione**» — la tabella dà la firma, non il ruolo |
| 3 | l'`RSPP` | «la figura aziendale competente» — l'istruzione lo colloca in uno **studio esterno** |
| 3 | Chemifood | «il **fabbricante** della sostanza» — la scheda si dichiara *fornitore*, e riserva quella parola a un terzo |
| 3 | il 10/05 | «l'unica **giornata di produzione** senza lavaggio» — che gli altri giorni senza righe fossero di produzione, le fonti non lo dicono |
| 3 | `NC-2026-013` | «**è lo stesso evento** dei due cicli interrotti» — è una NC di gennaio con causa propria |
| 3 | il pannello | «una forma che il pannello **non può calcolare**» — un limite dello strumento che nessuna fonte dichiara |

**Perché si rigenera, ed è una ragione meccanica, non una disattenzione.** Un archivio
d'impresa nomina le persone e le cose **per sigla**: `OP=BISSOLI_M`, `p.i. S. Bonato`,
`ing. M. Fantin`, `CHEMIFOOD AN-15`. Chi scrive una nota deve rendere quella sigla leggibile
a chi la troverà fuori contesto — è l'obbligo dell'atomicità — e **il gesto naturale per
renderla leggibile è aggiungere la qualifica**. La qualifica quasi sempre è vera: Dal Maso
*è* il capo officina, e il manuale HACCP lo dichiara. Ma lo dichiara **un'altra fonte**, e
la nota che lo scrive senza citarla afferma più di quanto le sue fonti reggano.

⚠️ **È la stessa classe del `PARLANTE_3` che metodo_03 porta come esempio** — l'attribuzione
di una battuta a un nome in una trascrizione con parlanti non verificati — ma là il caso è
presentato come **singolo**, e qui si vede che è una **famiglia**: si applica a persone,
strumenti, aziende, documenti, eventi e date, ogni volta che qualcosa viene reso
comprensibile.

⚠️ **E ha una proprietà che spiega perché tre giri non bastano a esaurirla**: ogni giro di
correzione **riscrive**, e ogni riscrittura è una nuova occasione di rendere comprensibile
un soggetto. È la stessa meccanica del *contesto importato* del lotto 1B — «il difetto non
stava nelle note: stava nel gesto di correggerle» — applicata agli attributi invece che al
contesto. Per questo il ciclo produce 12, poi 7, poi 9: non è una coda che si spegne, è una
**sorgente che il correggere riapre**.

**Che cosa la distingue da E39, con cui si accompagna.** E39 dice di propagare una
qualificazione a tutte le superfici della nota; questa classe riguarda **il gesto opposto**,
l'aggiunta di una qualifica che nessuna fonte porta. Le due si sono incrociate una volta, nel
rilievo su `POPESCU_I`: la cautela c'era su una sigla e non sulle altre due.

**La forma che il candidato prenderebbe, se il coordinatore lo ritenesse**: *quando una nota
rende leggibile una sigla — di persona, strumento, azienda o documento — la qualifica che
aggiunge deve venire da una fonte della nota, o essere dichiarata come inferenza.* Non si
propone come emendamento in questo rapporto: **una classe nominata al primo lotto in cui si
vede vale come osservazione**, e la regola di E28 sul contarne almeno due prima di scrivere
vale anche qui.

---

## 6. E39 al primo impiego: tre casi in un lotto solo

E39 è nato ieri dal gate di R1 e questo è il lotto che lo esercita per primo. **Ha trovato
tre casi**, e nessuno dei tre sarebbe stato preso dallo strato deterministico.

| # | La qualificazione apposta | Dove restava assertiva |
|---|---|---|
| 1 | «che sia la scheda del prodotto che il CIP usa davvero non è stabilito», scritta nel corpo | nel **titolo** della stessa nota — «La scheda di sicurezza **del detergente acido del CIP**» — nell'intestazione, nelle **glosse dell'hub**, in una **cella di tabella**, e nei titoli delle due note che ne discendono |
| 2 | «il log non dice se il pannello esegua il prolungamento o lo esegua senza registrarlo» | nel **summary**, che affermava netto «in nessuno dei due casi il pannello allunga il tempo» |
| 3 | «`IO-05` non dichiara il ruolo di Dal Maso» — tolta dal corpo **su rilievo del giudice** | nel **summary**, che continuava a dire «il capo officina lo controlla ogni primo lunedì del mese» |

⚠️ **Il terzo è il caso da manuale, e va letto due volte**: la cautela era stata appena
apposta al corpo, in quello stesso turno, per chiudere un rilievo. Il summary è rimasto
indietro **nel giro stesso della correzione**. È la conferma meccanica di ciò che E30 dice —
l'intestazione si scrive per prima e si corregge per ultima — e la prova che il gesto di E39
va fatto **subito dopo ogni qualificazione**, non a fine lotto.

⚠️ **E il primo caso mostra perché l'elenco delle superfici doveva restare aperto**: cinque
superfici diverse, di cui **due — le glosse dell'hub e la cella di tabella — non sono nella
nota qualificata**, ma in un'altra nota che la indicizza. Un elenco chiuso su «title e
summary» ne avrebbe prese due su cinque.

### La rilettura contro le sole fonti ha trovato il pattern del lotto 1B

Cinque casi di **contesto importato**, tutti nella stessa sezione — «Perché conta» — e tutti
della stessa forma: una nota di `docs\`, che ha per fonte la sola istruzione operativa,
affermava nel «Perché conta» un fatto **del log**. Nessuno di essi era visibile allo strato
deterministico, perché non conteneva numeri: `PRP-01`, «le due notti in cui il pannello ha
interrotto un ciclo», «ciò che il pannello scrive in ogni riga del log».

---

## 7. L'ESPERIMENTO: i due tassi, e il numero che il gate deve pesare

<!-- generati da `06_operativo\misura_due_tassi.py --lotto lotto_02a_cip --dominio cip --corrette 4` -->

| | Valore | Che cosa misura |
|---|---|---|
| Note riaperte da E37 | **10** | |
| di cui corrette agganciando la prescrizione | **4** | |
| di cui chiuse dichiarando che la fonte non le governa | **6** | |
| **TASSO DI RIAPERTURA** | **40,0 %** *(calcolato: 4 su 10)* | il **DEBITO** |
| Note nate nel lotto | **33**, di cui 3 note-strumento fuori classe | |
| Valutate | **30** | |
| Che parlano del dominio senza la fonte che lo governa | **1** — `fatto-ciclo-cip-straordinario-11-05` | |
| **TASSO DI DIFETTO DI PRODUZIONE** | **3,3 %** *(calcolato: 1 su 30)* | il **METODO** |

⚠️ **Il secondo è il numero che decide, e dice 3,3 % contro il 57,7 % di R1.**

**L'ipotesi del debito storico regge.** Il 57,7 % di R1 misurava note scritte tutte prima che
E29 ed E36 esistessero; qui, con le stesse regole in vigore e sullo stesso criterio, il
metodo produce il difetto in **un caso su trenta**. La differenza è di un ordine di
grandezza, e non è un confronto fra grandezze diverse: è lo stesso criterio, applicato una
volta alle note vecchie e una volta a quelle nuove.

⚠️ **L'unico caso si dichiara col suo nome, e non è stato aggiustato.**
`fatto-ciclo-cip-straordinario-11-05` racconta un ciclo di lavaggio citando il solo log, e
rimanda a un'altra nota per il programma. Aggiungerle `IO-05` fra le fonti avrebbe portato
il tasso a zero: sarebbe stato **truccare il numero che l'esperimento esiste per produrre**,
e non si è fatto.

⚠️ **Un limite del numero, dichiarato perché il gate lo pesi sapendolo**: 30 note e un lotto
solo. Il criterio scritto al gate di R1 chiede **due** lotti chiusi sotto E39 prima di
decidere sul candidato-script; per la questione del debito questo è il primo dei due, e un
solo lotto non chiude una serie.

---

## 8. Le note riaperte, una per una

Il criterio del dominio è **deliberatamente largo**: il costo di guardare una nota che non ne
aveva bisogno è un minuto, quello di non guardarne una che ne aveva bisogno è una nota che
afferma il falso dentro la misura. Delle 10 riaperte, **4 sono state corrette** e 6 chiuse
dichiarando che la fonte non le governa.

| Nota riaperta | Esito |
|---|---|
| `kpi-manutenzioni-arretrate-2026` | **corretta** — la voce della sonda del CIP ha ora la sua conseguenza nel vault |
| `fatto-strumenti-taratura-scaduta-in-uso` | **corretta** — «il CIP gira lo stesso» ha ora il termine di paragone: girava a due terzi della portata prescritta |
| `kpi-produzione-0450-linea1-maggio` | **corretta** — il «CIP profondo» del sabato 09/05 ha un riscontro indipendente nel tracciato |
| `kpi-consumi-energia-maggio-2026` | **corretta** — il centro di costo `CIP-01 / LAVAGGI` ha ora un denominatore |
| `fatto-fermo-forno-ft-01-05-05` · `macchina-ft-01` | non serve: «pulizia» del bruciatore è manutenzione meccanica, non lavaggio CIP |
| `questione-nc-067-sbrinamenti-tunnel` | non serve: «pulizia e sbrinamento profondo» del tunnel |
| `fatto-ispezione-ats-carrello-ricambi` | non serve: «acqua di lavaggio» riguarda la pavimentazione |
| `kpi-quadratura-consumi-energetici-maggio` | non serve: il «contatore CIP illeggibile» è una lettura, non un lavaggio |
| `doc-manuale-haccp` | non serve: presa per la parola «igienico-sanitario» nel corpo |

---

## 9. La sessione si è interrotta a metà lotto, e che cosa è servito per riprenderla

⚠️ **Il lotto è stato scritto a cavallo di un'interruzione forzata**: un limite di quota ha
ucciso **tre subagenti in volo** — due fette del secondo giro di giudizio e il revisore col
canone — mentre la sessione principale stava scrivendo nel vault.

⚠️ **La regola di §5 del prompt dei lotti — «se il contesto finisce, chiudi a confine di
lotto o di giro di giudizio completo, mai a metà» — presuppone una chiusura VOLONTARIA, e
qui non c'è stata**: nessuno ha potuto scegliere il punto in cui fermarsi. La sola difesa
disponibile era verificare, alla ripresa, che il punto in cui ci si era fermati non fosse
corrotto.

**Che cosa ha retto, e perché.** Nulla è andato perduto, e non per fortuna:

| Ciò che ha protetto | Perché ha funzionato |
|---|---|
| Il gate di R1 era **già committato e pushato** | il quinto gesto fatto subito ha messo al sicuro E39, E40 e §4.31 prima che il lotto cominciasse |
| Gli elenchi del perimetro si scrivono **mentre** si tocca una nota (E32), non a fine lotto | alla ripresa i 49 slug erano tutti sul disco: nessuna memoria da ricostruire |
| Ogni numero viene **da uno script**, non dal contesto della conversazione | i due tassi, il perimetro e i conteggi si sono ricalcolati identici |
| Il pacchetto e le fette sono **file**, non stato di sessione | i giudici caduti si sono potuti rilanciare sullo stesso ingresso, byte per byte |

**Il controllo di ripresa è stato affidato a un auditor indipendente**, con l'ordine
esplicito di non riparare nulla. Ha ripetuto in autonomia i sette script, ha confrontato
l'elenco delle note col vault nei due versi, e ha cercato residui e troncature nei due
perimetri. **Esito: nessun danno.** Le tre cose che ha segnalato sono tutte preesistenti e
tutte del corpus simulato — i byte NUL dentro il log sporco, il lock file di Word censito
come grezzo, e un briefing indietro di un commit.

⚠️ **Una divergenza fra i suoi numeri e i miei, e vale la pena scriverla**: l'auditor ha
misurato **41** avvisi di QA dove io ne dichiaro **40**. Non è un errore di nessuno dei due:
ha rilanciato la suite nell'istante precedente alla correzione che chiudeva il quarantunesimo.
**Due misure vere dello stesso oggetto in due istanti diversi**, ed è la ragione per cui i
numeri di questo rapporto portano l'ora della loro misura e non solo il valore.

---

## 9-bis. Adempimenti di chiusura

Tutti eseguiti prima del commit, e ciascuno verificato da uno script.

| Adempimento | Esito |
|---|---|
| Tabella di tracciamento | **T21 e T29 chiuse** (erano duplicate fra loro, terzo caso dopo T22/T30); **T56 avanzata**; **cinque righe nuove**, da T70 a T74. `conta_tracciamento.py`: **74 righe, da T1 a T74, nessuna mancante** |
| CSV file × fatto | **32 righe nuove** per il lotto 2A |
| `# CHIUSO 19/08/2026` sull'elenco | fatto — `verifica_matrice_lotti.py` torna **verde**: 160 grezzi, 0 scoperti, 0 guasti, 16 elenchi |
| Canone accresciuto | **sezione datata del 19/08/2026** con le nove divergenze di categoria B |
| `registro_emendamenti.md` | **nessun emendamento nuovo**: i tre candidati stanno al §10 e non si scrivono ora |
| Elenchi di lotto | il tema 2 è diventato **tre elenchi veri**; `lotto_02_igiene.txt` non esiste più |
| Nota-sessione nel journal | `sessione-s4-lotto-02a`, scritta **prima** del blocco dei conteggi (E34) |
| `llms.txt` | rigenerato |
| Collaudo della suite | **20 su 20**, tutte e cinque le vie |

### I conteggi del vault, generati DOPO la nota-sessione

<!-- CONTEGGI DEL VAULT — generati da `06_operativo\qa\conta_stato.py` il 2026-08-19.
     Si incollano VERBATIM: non si ricompongono a mano, non si riscrivono in prosa. -->

| Grandezza | Valore |
|---|---|
| Note nel vault | **217** |
| di cui `_index` | 11 |
| di cui note-strumento del progetto | 13 |
| di cui note di diario (`sessione`, `daily`) | 5 |
| **di cui note di contenuto** | **188** |
| Note per cartella | areas 109 · data 26 · entities 24 · docs 19 · code 14 · projects 8 · workspace 8 · concepts 6 · self 1 · outputs 1 · sources 1 |
| Note per `type` | atomica 127 · conflitto 37 · entita 19 · hub 13 · index 11 · concetto 5 · sessione 5 |
| Questioni aperte (`type: conflitto`) | 37 |
| Grezzi in `sources\` | 160 |
| Grezzi citati da almeno una nota | **38** |
| Grezzi restanti | **122** |

### Gli strumenti nati o cambiati in questo lotto

| Strumento | Che cosa fa, e perché è nato qui |
|---|---|
| `candidate_r1.py --dominio` | la **modalità ristretta** che E37 richiede. Fix **monotono**: il default sul lotto R1 dà output **identico** alla versione committata, verificato per confronto |
| `taglia_pacchetto.py` | divide il pacchetto del giudizio e **garantisce l'appendice delle fonti**, con la guardia che rifiuta di scrivere una fetta degradata |
| `conteggi_lotto_02a.py` | tutti i numeri del lotto, col valore prescritto accanto a ciascuno |
| `misura_due_tassi.py` | i due tassi dell'esperimento, tenuti **separati** perché misurano grandezze diverse |
| `collaudo_suite.py` | la via **V3** acquista il difetto piantato dell'appendice (§4.29) |

Le prime tre hanno la loro nota-strumento in `code\`; la quarta pure. Nessuna ha `fonti`
(E20).

---

## 10. Candidati emendamento

Il lotto non propone regole nuove sul **modo di scrivere le note**: E29, E36, E37, E39 ed
E40 hanno retto tutte al primo impiego, e ciò che il lotto ha trovato è stato preso dal
metodo com'è. Restano **tre candidati**, tutti sul processo, e per due dei tre la
raccomandazione è di **non scriverli ancora**.

### C1 — La propagazione della cautela si fa NELLO STESSO TURNO della qualificazione

⚠️ **È il candidato con la prova più forte, e la prova è il terzo caso del §6.** Una cautela
apposta al corpo per chiudere un rilievo del giudice **non è arrivata al summary**, nello
stesso turno in cui veniva scritta. E39 dice *che cosa* fare; non dice *quando*, e il caso
mostra che «quando» non è ovvio: chi corregge su rilievo sta pensando al rilievo, non alla
nota intera.

**Forma proposta**, se il coordinatore lo ritiene: E39 acquista una riga — *la ricerca delle
altre occorrenze si fa contestualmente alla qualificazione, non a fine giro*. È un
chiarimento, non una regola nuova, e non cambia il perimetro di nessun controllo.

### C2 — Chi prepara l'ingresso di un giudice si rifiuta di produrne uno degradato

`taglia_pacchetto.py` ha una guardia che **non scrive** una fetta priva di appendice. Oggi
quella guardia vive in un solo script, per scelta di chi l'ha costruito; §4.31 dice perché
serve, ma è giurisprudenza, non obbligo di metodo.

⚠️ **Non si propone come emendamento adesso**, e la ragione è la stessa di E28: **una sola
osservazione**. La guardia non ha mai scattato — tutte e sei le fette erano complete — e una
regola scritta su uno strumento che non ha mai fallito è una regola di cui non si conosce il
costo. Si rivede quando un secondo strumento del progetto dovrà preparare un ingresso.

### C3 — La riga al giudice sull'esito legittimo: funziona, e la prova è che nessuno ne ha avuto bisogno

Ogni fetta porta in testa che **dichiarare degradato il proprio ingresso è un esito
legittimo**. Sei giudici su sei hanno aperto la risposta verificando l'ingresso ed
elencando le fonti trovate — cioè hanno **eseguito** il controllo prima di giudicare, che è
esattamente lo scopo.

⚠️ **Ma il dato è debole nel verso che conta**: nessuno ha dovuto usarla, perché nessun
ingresso era degradato. Che la riga *funzioni quando serve* resta non dimostrato, e
`PROMPT_GIUDIZIO` è congelato dal 18/08. Il candidato per una v3 si tiene, non si applica.
