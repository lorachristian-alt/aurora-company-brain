# Rapporto del lotto 3C — certificazione e audit

> **Chiuso il** 22/08/2026 · **Grezzi** 4 · **Tema** 3, sistema qualità · **Anticipato su 3B**
> al gate del lotto 3A, e il motivo sta nel registro delle modifiche della matrice: il
> rapporto d'audit porta **sette divergenze già nel canone** che nessun lotto poteva scrivere,
> **due delle quali correggono cose già scritte nel vault**.

---

## 1. L'apertura, e la prima verifica del dominio da script (E53)

### 1.1 I quattro grezzi, e il censimento dei fatti prima di scrivere (E21)

| Grezzo | Righe | Che cosa porta |
|---|---|---|
| `Rilievo_Audit_BRC_IFS_CSQA_febbraio2026.txt` | 282 | il rapporto d'audit: programma, evidenze, 2 NC, 5 osservazioni, 3 OSS di miglioramento, **e la sezione 6 compilata dall'ente sulla chiusura** |
| `Certificato_BRCGS_Food_Issue9_Aurora_2026.pdf` | 220 | il titolo in vigore, lo scope, le esclusioni, **le sei condizioni di validità e uso del marchio**, l'allegato per referenza |
| `R_R_R_scadenza_certificato_BRCGS_e_audit_di_rinnovo.eml` | 101 | quattro messaggi in catena fra CSQA e la RSGQ, dal sollecito alla chiusura con riserva |
| `Conferma_incarico_audit_rinnovo_2026.pdf` | 56 | l'incarico dell'audit di rinnovo: date, gruppo, corrispettivo, **documentazione preliminare a 20 giorni** |

**Censimento delle 10:06:30 del 22/08/2026**, distinti dopo l'unione fra i quattro grezzi:
**26 date · 15 clausole di schema · 15 attrezzature o impianti · 13 sigle di documento ·
8 persone nominate · 7 codici articolo · 5 fornitori · 3 percentuali · 1 importo.**

⚠️ **Il grezzo denso è uno solo.** Il rapporto d'audit da solo porta più fatti degli altri tre
messi insieme, e i restanti tre lo **commentano**: il certificato ne è l'esito, la mail ne è
lo strascico, l'incarico ne è il seguito. **Il pacchetto non è quattro documenti su un tema:
è un documento e le sue tre code**, ed è la ragione per cui regge in un lotto solo.

### 1.2 E53 al primo impiego: il dominio si verifica, non si dichiara

**Strumento nuovo, nato per questo passo:** `06_operativo\verifica_dominio.py`. Cerca nei
grezzi del lotto le **sigle** e i **nomi** delle fonti prescrittive dell'elenco, e riporta i
riscontri in **due classi che non si sommano mai**.

**Esito delle 10:05:31 del 22/08/2026 — il dominio c'è, e con riscontri forti:**

| Fonte citata **per sigla** | Dove | Citabile |
|---|---|---|
| `manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt` | rapporto, incarico, mail | **sì** |
| `IO-05_istruzione_operativa_lavaggio_CIP.docx` | rapporto, riga 113 | **sì** |
| `Scheda_tecnica_prodotto_AF-SN-0450_rev4.pdf` | certificato e rapporto | **sì** |
| `scheda_sicurezza_detergente_acido_lavaggio_CIP.txt` | rapporto, riga 113 | **sì** |
| `DoC_MOCA_Flexipack_film_PP_EVOH_2026.pdf` | rapporto, riga 67 | no — lotto 2C |
| `procedura_ritiro_prodotto_CRISI_GDO.txt` · `listino_prezzi_canale_GDO_fresco_v3.csv` | sigla `GDO` | no |

⚠️ **La domanda che 3A non aveva potuto porsi ha risposta in venti secondi di script**, e la
risposta è **sì**. Un rapporto d'audit **registra** rilievi, ma **cita** criteri prescrittivi
per costruzione: qui ne cita quattro citabili, con la sigla, alla riga.

### 1.3 Lo script è nato con un difetto, e il difetto era muto

⚠️ **Il primo `RX_SIGLA` finiva con `\b`**, e fra la `I` di `CPI_certificato_…` e l'underscore
**non c'è un confine di parola** — l'underscore è un carattere di parola. **Ogni sigla del
corpus veniva scartata in silenzio**, e restavano solo i riscontri deboli: `certificato`,
`manutenzione`, `produzione`, `febbraio`.

**Il numero che ha tradito il difetto: 28 fonti su 36 «nominate».** Un elenco che dice quasi
sempre di sì non è una verifica, ed è per quel numero — non per una rilettura del codice —
che sono andato a guardare. ⚠️ **Uno script che tace non è uno script che assolve.**

Da lì le **due classi di forza**, che restano nello strumento: una **sigla** dentro un
documento è una **citazione** — chi scrive «IO-05» sta indicando quel documento; una **parola
comune del nome** non dimostra nulla da sola. **Sette forti, ventuno deboli, e non si sommano.**

### 1.4 Il dominio `certificazione`, e la regola dell'elenco che ha dovuto cedere

⚠️ **Il lotto porta dentro il vault due fonti prescrittive nuove**, e per ammetterle è stato
necessario **affinare una regola in vigore** del padrone dell'elenco, che diceva:

> «Un certificato non è una fonte prescrittiva: attesta uno stato, non lo prescrive.»

**È vera sulla metà del documento che aveva guardato.** Il certificato `BRC/IT/24/00871`
porta **sei condizioni di validità e uso del marchio numerate**: dove il logo si può usare e
dove è **vietato**, entro quanti giorni si comunica una modifica di processo, che cosa fa
decadere il titolo. **Quelle prescrivono, e vincolano Aurora.**

**Regola nuova, scritta nel padrone:** *un certificato non è prescrittivo **per i requisiti
che attesta** — quelli vivono nella norma, che in questo corpus non c'è — **ma le condizioni
di validità stampate sopra prescrivono***. L'elenco passa da **36 a 38 fonti**, da **11 a 12
citabili**.

### 1.5 La riconciliazione verticale arretrata (E37), e un criterio sbagliato colto dal numero

`candidate_r1.py --dominio certificazione` — **19 note riaperte**, che entrano nel perimetro
di QA del lotto (E32) e **non contano nella capacità 25-35**: sono riparazioni.

⚠️ **Il primo taglio delle espressioni del dominio dava 119 note su 288 valutate**, cioè **due
note del vault su cinque**. Un debito vero non ha quella forma. Dentro c'erano
`certificat[oi]`, `non conformità`, `NC-\d` e `scope` — che in un archivio di qualità
alimentare stanno **dappertutto**, e «certificato» prende per primo il **certificato di
TARATURA**, che è di un altro dominio e ha già la sua fonte.

⚠️ **È il difetto che E36 ha corretto, ricomparso dall'altra parte: il criterio generico
applicato a un elenco più corto.** Un dominio si riconosce dalle espressioni che nomina **lui
e nessun altro** — l'ente, gli schemi, il titolo, il marchio; non la parola «certificato».
**Il criterio corretto sta nel sorgente, col suo perché, ed è quello che il rapporto dichiara.**

### 1.6 La proiezione, e la soglia

| | |
|---|---|
| Note **nuove** proiettate | **~32** |
| Note **riaperte** (E37) | **19** — non contano nella capacità |
| Capacità attesa | 25-35 |
| Tetto di spezzamento (E28) | 40 |
| **Decisione** | **non si spezza**: la proiezione sta dentro la capacità, e le riaperte sono riparazioni |
| **Note nuove EFFETTIVE** | **38** — 37 di contenuto + 1 di diario |

⚠️ **Lo scostamento è di sei note sulla proiezione, e si dichiara** (E28: sotto le 40 non si
spezza). ⚠️ **Ma la parte che conta è come si compone**: **trentadue nate dal ciclo** e **sei
nate DOPO**, dal giudizio e dalla revisione col canone. Per E52 le seconde non contano nella
soglia di spezzamento — **ma si dichiarano sempre come gruppo**, ed è il §7.2.

⚠️ **E52 governa questo passo**: le soglie valgono sulla **proiezione d'apertura** e sulla
**scrittura del ciclo**; le note che nascessero dalla revisione si dichiareranno come gruppo
a parte, con esiti di giudizio separati.

---

## 2. E55, e il primo caso in cui la grammatica dei locator non sapeva indirizzare un documento

**La grammatica dei locator è chiusa** (`metodo_03` §2.3), e per il `.eml` prevede due sole
forme: `corpo, punto <n>` e `header <Nome>`.

⚠️ **`R_R_R_scadenza_certificato_BRCGS_e_audit_di_rinnovo.eml` porta QUATTRO messaggi**, quotati
uno dentro l'altro, dall'11 marzo al 7 aprile. **«corpo, punto 1)» ne indica quattro diversi**,
e chi verifica non sa quale.

**E55, chiarimento applicato in corsa e dichiarato qui** (§4 del prompt dei lotti): se il file è
una **catena**, il locator nomina prima **quale** messaggio, con la sua data —
`corpo del messaggio del <GG/MM>, punto <n>`. La forma breve resta valida per un `.eml` a
messaggio unico, che è il caso di tutti i lotti precedenti.

⚠️ **Il difetto era nel corpus da prima di 3C**: il prefisso `R_R_R_` dice da solo che il file
è una catena, e nessun lotto ci era ancora arrivato.

### 2.1 Il fix allenta un controllo, quindi §4.9 alla lettera

`qa_frontmatter.py` non conosceva la forma nuova e la rifiutava come «locator fuori
grammatica»: **una regola in vigore che lo strumento rendeva impossibile**, la stessa specie di
guasto di E48 col `verifica: strutturale`.

**Collaudo nuovo, a perimetro chiuso, nei due versi:** `_collaudo\collaudo_locator_eml.py`.

| Caso | Atteso | Esito |
|---|---|---|
| la forma **nuova** su una catena | non deve scattare | **tace** ✅ |
| la forma **breve** di sempre | non deve scattare | **tace** ✅ |
| una forma **fuori da entrambe** | **deve** scattare | **scatta** ✅ |

⚠️ **Il terzo è il difetto piantato, ed è quello che conta**: dice che la grammatica è ancora
chiusa **dopo** l'allargamento. Senza di lui i primi due proverebbero soltanto che il controllo
è stato spento.

## 3. Il certificato non stava dove il metodo lo manda, e il metodo lo diceva con un esempio

**Il certificato BRCGS era stato scritto in `docs\`.** Aggiornando `_index-docs` ho letto la
riga che quella cartella porta da sempre:

> «Gli attestati che Aurora **riceve** da terzi non stanno qui: sono attributi dell'azienda, e
> stanno in `self\`.»

⚠️ **E `metodo_03` §5 ha un esempio svolto su QUESTO stesso file**: riga 3 della tabella —
«Certificato BRCGS Food Issue 9 grade AA, cert. BRC/IT/24/00871 → `self\` → `self-certificazioni.md`
… **Scartata `docs`**: in `docs` vanno i documenti che Aurora **scrive e applica**, non gli
attestati che riceve da terzi». Anche l'`area` era prescritta: `qualita`.

**Corretto**: la nota è `self\self-certificazioni.md`, e gli otto wikilink che la puntavano
l'hanno seguita. ⚠️ **`self\` era vuota da quattro mesi e si apre con questo lotto**: è la
prima nota che descriva **che cosa Aurora è**, invece di che cosa ha fatto o di che cosa
prescrive.

⚠️ **La lezione non è che il metodo andasse riletto meglio.** È che **l'errore è stato trovato
dall'indice della cartella, non da chi scriveva**: la riga era sotto gli occhi al momento di
aggiornare `_index-docs`, e non un minuto prima.

## 4. La riconciliazione verticale ha trovato quattro lacune vere, e una porta un ritrovamento

**Le quattro note del lotto che discutevano una cosa prescritta senza avere sotto mano il
documento che la prescrive** (E29/E36):

| Nota | Che cosa prescrive, e dove |
|---|---|
| `fatto-nc2-carrello-ricambi-a-bordo-linea` | il manuale HACCP impone «ispezione avvio linea, controllo integrità dopo ogni intervento, `MOD-PR-04`» — **il modulo che l'azione correttiva propone era già prescritto** |
| `fatto-vendor-rating-senza-imballaggi-e-laboratorio` | `PRP-05` prescrive il vendor rating annuale e `PRP-12` nomina **`F0044` e `F0031` uno per uno** — cioè esattamente i due che dalla valutazione mancano |
| `fatto-zanzariera-lacerata-e-porta-officina` | `PRP-02` è la disinfestazione e il monitoraggio infestanti |
| `fatto-quattro-neoassunti-linea2-senza-formazione-allergeni` | `PRP-04` è «Igiene e formazione del personale», col `MOD-HR-11` come registro |

### 4.1 ⚠️ Il ritrovamento: l'azione correttiva è assegnata al prerequisito sbagliato

**Il rapporto d'audit propone di inserire il controllo delle aperture nel «giro ispettivo
mensile `PRP-08`».** Nel manuale HACCP di Aurora **`PRP-08` è «Controllo corpi estranei: vetro
e plastica dura»**; il prerequisito degli infestanti è **`PRP-02`**.

⚠️ **L'azione correttiva di un rilievo sugli infestanti è stata assegnata al prerequisito del
vetro**, e nessuno dei due documenti se ne accorge. **O l'auditor ha citato la sigla sbagliata,
o Aurora usa una numerazione dei PRP diversa da quella del proprio manuale.** T118.

⚠️ **Non l'avrebbe trovato nessun controllo automatico**: si vede solo aprendo il manuale per
agganciare la prescrizione, cioè facendo esattamente ciò che E29 impone.

## 5. I due tassi (E41/E46), e perché il secondo misura la dichiarazione e non il metodo

**Dominio dichiarato in apertura: `certificazione`** — il rapporto con l'ente di
certificazione: titolo in vigore, scope, condizioni di validità e uso del marchio, obblighi di
comunicazione, chiusura delle non conformità e programmazione degli audit.

| | |
|---|---|
| **Tasso di riapertura** *(debito)* | **26,3 %** — 5 note corrette su **19** riaperte |
| **Tasso di difetto di produzione** *(metodo)* | **38,7 %** — 12 su 31 valutate |

### 5.1 Il primo taglio del dominio dava 119 note, e il numero lo ha tradito

⚠️ **Le prime espressioni del dominio riaprivano 119 note su 288 valutate**, cioè **due note del
vault su cinque**. Un debito vero non ha quella forma. Dentro c'erano `certificat[oi]`,
`non conformità`, `NC-\d` e `scope` — e **«certificato» prende per primo il certificato di
TARATURA**, che è di un altro dominio e ha già la sua fonte.

**È il difetto che E36 corresse per le note, ricomparso nella dichiarazione di un dominio: il
criterio generico applicato a un elenco più corto.** Corretto, il perimetro scende a **19**.

### 5.2 ⚠️ E il 38,7 % ha lo stesso problema, un gradino più in là

**È il tasso più alto della serie**, e va guardato prima di crederlo. Delle dodici note contate
come scoperte:

| | Quante |
|---|---|
| citano **un'altra fonte prescrittiva** che governa ciò di cui parlano davvero — il manuale HACCP, il registro delle tarature | **8** |
| hanno la prescrizione **fuori dal corpus**, nel protocollo BRCGS | **3** |
| rimandano a una «procedura interna» che l'archivio non ha | **1** |

⚠️ **Il numero NON è stato aggiustato** (E41): nessuna fonte è stata aggiunta per abbassarlo, e
**le quattro correzioni verticali vere del §4 non lo toccano affatto**, perché riguardano il
dominio del manuale HACCP e non quello dichiarato.

⚠️ **Il sospetto, e va al gate**: **le ESPRESSIONI del dominio riconoscono le note che parlano
dell'AUDIT, mentre le sue FONTI governano il TITOLO e gli obblighi verso l'ente.** Il dominio è
dichiarato più largo di quello che le sue fonti sanno governare. **T129.**

### 5.3 La serie, con questo punto

| Lotto | Dominio | Tasso di difetto di produzione |
|---|---|---|
| R1 | perimetro CCP e tarature | **57,7 %** |
| 2A | `cip` | **3,3 %** |
| 2B | `acqua` | **0,0 %** |
| 2B-bis | `allergeni` | **9,1 %** — 3 su 33 |
| 3A | — | **NON MISURATO** — dominio non dichiarato in apertura per errore del gate |
| **3C** | **`certificazione`** | **38,7 %** — 12 su 31 ⚠️ **con la riserva del §5.2** |

## 6. Due fonti prescrittive nuove, e una regola dell'elenco che ha dovuto cedere

**Il lotto porta dentro il vault due fonti prescrittive**, e per ammetterle è stato necessario
affinare una regola in vigore del padrone dell'elenco, che diceva: «un certificato non è una
fonte prescrittiva: attesta uno stato, non lo prescrive».

⚠️ **È vera sulla metà del documento che aveva guardato.** Il certificato porta **sei condizioni
di validità e uso del marchio numerate** — il logo vietato sull'imballo destinato al
consumatore, i **tre giorni lavorativi** per comunicare una modifica o un evento grave, la non
trasferibilità, la facoltà di sospensione. **Quelle prescrivono, e vincolano Aurora.**

**Regola nuova, scritta dal padrone:** *un certificato non è prescrittivo **per i requisiti che
attesta** — quelli vivono nella norma, che in questo corpus non c'è — **ma le condizioni di
validità stampate sopra prescrivono***.

L'elenco passa da **36 a 38 fonti**, da **11 a 12 citabili**.

---

## 7. I tre giri di giudizio, e la classe d'errore che li ha chiusi

| Giro | Note giudicate | `pulita` | `afferma_oltre` | `fonte_inutile` |
|---|---|---|---|---|
| **1º** | 51 | 44 | **7** | 0 |
| **2º** | 55 | 53 | **2** | 0 |
| **3º** | 55 | 50 | **5** | 0 |

⚠️ **Il terzo giro ha trovato PIÙ rilievi del secondo, e non è un peggioramento: è che gli è
stato detto che cosa cercare.** I due rilievi del secondo giro avevano la stessa forma, e la
forma è stata **nominata**; il terzo giro è partito con l'istruzione di setacciare il lotto su
quella classe, e ne ha trovati altri tre che i primi due non avevano visto.

**Il ciclo si chiude qui per E26**: comunque al terzo, e **dopo che il rapporto ha nominato il
pattern che rigenera i rilievi**. È questo:

### 7.1 ⚠️ Il pattern: il superlativo sull'archivio

> «è **la sola parte dell'archivio** in cui…» · «questo documento è **il solo dell'archivio** a
> nominarla» · «è il termine **più stretto che questo archivio conosca**» · «è **l'unico
> riscontro in archivio** sullo stato di quel registro»

⚠️ **Nessuna fonte citata può reggere un'affermazione di questa forma**, perché parla di ciò
che l'archivio contiene **altrove** — e nessuna nota ha l'archivio fra le proprie fonti.

⚠️ **La regola non è «niente superlativi», ed è il punto che rende la classe utile.** Il terzo
giro ne ha verificati **quattordici** e ne ha confermati **dieci**: tutti quelli il cui
soggetto è **un documento citato**. «È l'unica cosa che questo verbale chiami *obiettivo
primario*» è vero e verificabile riga per riga; «nessuna riga del file porta una matricola
`TP-`» pure.

**Il discrimine è il soggetto:**

| Soggetto del superlativo | Verificabile? |
|---|---|
| **un documento fra le `fonti`** | **sì** — si legge e si conta |
| **il pacchetto dei grezzi del lotto** | **sì**, se sono tutti fra le fonti |
| **l'archivio, il vault, «tutto il resto»** | ⚠️ **no**, mai |

⚠️ **È la stessa forma di E36, un gradino più su**: là l'affermazione eccedeva il documento,
qui eccede il **perimetro**. **Candidato emendamento al gate** — vedi §10.

⚠️ **E uno dei quattro era una nota preesistente**, `fatto-obblighi-registro-f-gas` del lotto
1B: **la classe non è nata in 3C, ci è stata solo trovata.**

### 7.2 Il gruppo post-revisione, e il criterio pre-registrato che si è risolto

**Il gate del 22/08 aveva scritto il criterio PRIMA di questo lotto**: *se al prossimo lotto
che produce note post-revisione il tasso di rilievi del gruppo è ancora più del doppio di
quello del ciclo, il gruppo prende un mini-ciclo dedicato; altrimenti E54 è bastato.*

| | Note | Rilievi al 2º giro | Tasso |
|---|---|---|---|
| **gruppo post-revisione** | **4** | **0** | **0,0 %** |
| **note del ciclo** | 51 | 2 | **3,9 %** |

✅ **Il criterio NON scatta: E54 è bastato.** ⚠️ **È la prima volta in questo progetto che un
criterio pre-registrato viene esercitato e si chiude senza discussione** — e la ragione per cui
funziona è che era stato scritto quando non si sapeva ancora come sarebbe andata.

⚠️ **Il gruppo però è cresciuto dopo**: i ritrovamenti del **terzo** giro hanno prodotto altre
**due** note, e quelle **non sono passate dal giudizio**. **T141**, debito di processo
dichiarato.

## 8. Che cosa la revisione col canone ha trovato

**7 rilievi `A`, 8 divergenze `B`, 7 falsi allarmi `C`.**

### 8.1 Le A, e la più grave

⚠️ **`A1` smontava l'argomento centrale di una questione aperta.** La nota sulle clausole della
`NC 1` scriveva «la mail è l'unica voce indipendente, ed è quella che diverge» e «il documento
interno di Aurora concorda con il rapporto, non con la mail». **Falso in entrambe le metà**: il
registro delle non conformità interne di Aurora porta una **terza** combinazione, `BRCGS
2.10.2 / IFS 5.1.2`, che **incrocia** le altre due e che nessun documento dell'ente contiene.

⚠️ **La nota riscritta è più forte di prima**: con due versioni si poteva pensare a un refuso;
con tre, di cui una mista, si vede che **nessuno le ha mai messe a confronto** — e la
combinazione mista è quella con cui Aurora ha archiviato la NC a sistema.

⚠️ **`A2` lasciava nel vault due fatti incompatibili, entrambi dati per pacifici**: una nota
diceva che l'efficacia sarà verificata all'audit di **sorveglianza del 02/2027**, un'altra
all'audit di **rinnovo del giugno 2026**. **Quattro giorni separano i due atti dell'ente.** Ora
c'è una questione padrona e le due note vi rimandano.

**Le altre cinque:** un'attribuzione d'intervista sbagliata, una citazione presa da un grezzo
non dichiarato, un «tutti e quattro i documenti» con tre fonti, e sette citazioni fuori forma.
⚠️ **Sulla trappola ortografica `.txt`/`.eml` contro `.pdf`, zero errori su 532 citazioni.**

### 8.2 Le B: otto divergenze, quattro scritte e quattro no

**Scritte** — tutte le gambe canonizzate: l'inventario delle evidenze del 02/04 che non torna
(**D1**), i due cluster su quando l'ente tornerà (**D2**), le tre date della convalida del
metal detector (**D3**), le tre versioni della clausola (**D4**).

🚫 **Non scritte, divieto 9-bis** — la parcella dell'audit in quattro versioni incompatibili
(**D5**), la fattura che decide la durata (**D6**), le due partite IVA di CSQA entrambe valide
al controllo di Luhn (**D7**), i due obblighi di comunicazione senza traccia d'adempimento
(**D8**). **Canone, sezione datata 22/08/2026; matrice, T133-T137.**

⚠️ **`D6` chiuderebbe una riga aperta oggi**: la fattura elettronica dettaglia «2 GG UOMO X 2
AUDITOR», cioè la versione del rapporto contro quella del certificato — ma è del lotto 6, e
**T123 resta aperta con l'obbligo esplicito**.

### 8.3 Le C, e una che vale come regola

**Sette falsi allarmi, tutti annotati nel decision log** perché non tornino al lotto dopo. Uno
merita di essere citato: `C7` non è un errore di nota ma **una riga della tabella alias ormai
superata** — «il nome per esteso lo dà UNA fonte sola» per Chiara Vicentini, mentre il rapporto
d'audit lo scrive per esteso. **Le fonti ora sono due, e l'avvertenza è stata aggiornata.**

## 9. Due ritrovamenti che hanno corretto cose scritte in questo stesso lotto

⚠️ **Il «sedici giorni» non era un refuso del vault.** Questo rapporto aveva già scritto la
correzione a **quindici** quando il terzo giro ha segnalato che il registro delle non
conformità interne porta `NC-2026-061`: «Invio a CSQA evidenze chiusura NC audit **con 16 gg di
ritardo** sulla scadenza». **Aurora conta sedici in due documenti diversi, ed è coerente con sé
stessa**; l'ente conta quindici perché il termine è suo e lo fissa al 18/03.

**La riga T126 è stata riscritta dentro lo stesso lotto**, e dice che cosa diceva prima. ⚠️ **La
prima stesura affermava che il vault era «sbagliato»: non lo era, contava da un altro giorno.**

> 🛑 **ERRATA del 23/08/2026, scritta al gate di questo lotto.** Il capoverso qui sopra
> resta come fu scritto — un rapporto documenta cio' che la sessione fece — ma **due sue
> affermazioni non reggono sulle fonti**, e le ha trovate il **giudizio dedicato di E58**:
>
> - «**Aurora conta sedici in due documenti diversi**»: ⚠️ **il verbale di riesame non porta
>   ne' «sedici» ne' «16»** — verificato riga per riga. Fissa la scadenza al **17/03**, che del
>   sedici e' la **premessa**, non l'enunciato. **Il sedici ha un solo titolare: `NC-2026-061`.**
> - «**l'ente conta quindici**»: ⚠️ **il quindici non lo scrive nessuno.** E' il conto del vault
>   fra il 18/03 e il 02/04, e ora porta la marca `(contati)` (E50). ⚠️ **L'ente un conteggio
>   pero' lo scrive**, contro un altro termine: il rapporto d'audit §6 dice «oltre il termine di
>   sollecito del 01/04/2026 **(un giorno)**».
>
> ⚠️ **La sostanza del §9 regge — termini diversi, conti diversi, Aurora coerente con se'
> stessa — ma la lettura «due contatori veri» no.** **T126 e' alla terza stesura**, e tutte e
> tre sono cadute sullo stesso punto: **un conteggio attribuito a una fonte che non lo enuncia**,
> la classe di E49 e di E50. La correzione vive in T126 e nella nota
> `fatto-evidenze-audit-oltre-termine`; qui resta l'errata, come prescrive la regola del gate 1A.


⚠️ **E il vendor rating: i tre fornitori che l'audit dà per mancanti sono classificati nel
riesame di marzo**, dentro la «Valutazione fornitori 2025». **Un indizio punta a una
valutazione ritoccata dopo l'audit** — la motivazione di classe B per Flexipack è una bobina
fuori spessore del **10/02/26**, di una settimana prima dell'audit, che una valutazione del
2025 non poteva contenere. **Non decide**, e la nota lo dichiara. **T140.**

## 10. Che cosa il gate deve decidere

| | |
|---|---|
| **1. Il dominio `certificazione` è dichiarato troppo largo?** | Il tasso di difetto di produzione è **38,7 %**, il più alto della serie, ma **otto delle dodici note contate come scoperte citano un'altra fonte prescrittiva** e tre hanno la prescrizione fuori dal corpus. ⚠️ **Il numero non è stato aggiustato.** **T129** |
| **2. Il superlativo sull'archivio diventa un emendamento?** | Il pattern è nominato e verificato su quattordici casi: **il discrimine è il soggetto**, non la forma. È una regola sul MODO DI SCRIVERE le note, quindi per §4 va al coordinatore prima di entrare in `metodo_03`. **T142** |
| **3. Le due note non giudicate** | Nate dai ritrovamenti del terzo giro, hanno passato QA e citazioni ma **non lo strato di giudizio**. La regola d'arresto E26 ha la precedenza sul ri-giudizio: si dichiara. **T141** |
| **4. E55 va ratificato** | Chiarimento applicato in corsa alla grammatica dei locator, con collaudo a perimetro chiuso nei due versi. **Già nel registro** |
| **5. La regola sul certificato prescrittivo** | L'elenco delle fonti prescrittive è passato da 36 a 38 e la sua regola è stata affinata dal padrone: **un certificato non prescrive i requisiti che attesta, ma le sue condizioni di validità sì.** Va confermata |
| **6. Il debito verso i lotti 5 e 6** | **Quattro divergenze** aspettano l'amministrazione e il commerciale — T133, T134, T135, T136 — e una di esse **chiuderebbe T123** |

---

## 11. I numeri di chiusura (E44), tutti da script e con l'ora della misura

**Misure delle 12:16:45 e delle 12:18:40 del 22/08/2026, dopo l'ultima scrittura.**

| Misura | Valore | Strumento |
|---|---|---|
| **QA, perimetro lotto** | **0 ERRORI, 36 avvisi** — esito **GIALLO** | `qa_all.py` |
| **QA, perimetro vault** | **114 ERRORI, 257 avvisi** | `qa_all.py` |
| di cui grezzi non ancora canonizzati | **111** | |
| di cui aree senza hub | **3** — ricerca-sviluppo, risorse-umane, sicurezza-ambiente | |
| di cui **rilievi di merito** | **0** | |
| **Perimetro del lotto** | 4 grezzi · **19 candidate** · **4 toccate** · **38 nate** = **61 note controllate** | `conta_perimetro_lotto.py` |
| **Collaudi** | **5 su 5 superati**: suite 18+9, due tassi 5, CSV 7, doppie padrone 3, locator eml 3 | `_collaudo\` |
| **Emendamenti** | registro e manuale **concordano** a **55** | `verifica_emendamenti.py` |
| **Matrice** | **completa e disgiunta**: 160 grezzi, 23 elenchi | `verifica_matrice_lotti.py` |
| **Tracciamento** | **142 righe**, da T1 a T142, nessuna mancante | `conta_tracciamento.py` |
| **Vault** | **362 note**, di cui **327 di contenuto** | `conta_stato.py` |
| **Grezzi canonizzati** | **49 su 160** — ne restano **111** | `conta_stato.py` |
| **Questioni aperte** (`type: conflitto`) | **50** | `conta_stato.py` |

⚠️ **Il vault passa da 118 a 114 errori, e la differenza sono esattamente i quattro grezzi di
questo lotto**: nessun rilievo di merito è stato introdotto e nessuno ne è stato spento.
