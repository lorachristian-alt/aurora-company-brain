# Rapporto del lotto R1 — riconciliazione verticale

> **Cos'è** · Il rapporto del **primo lotto di manutenzione** del progetto (E35): quello che
> non canonizza grezzi nuovi ma ripara note già scritte, aperto dal gate del lotto 1C.
> **Stato** · ⚠️ **PRIMO GIRO CHIUSO, LOTTO NON CHIUSO.** Le correzioni sono fatte e la QA di
> lotto è verde; mancano lo strato di giudizio, la revisione col canone e il ri-giudizio, che
> `metodo_03` §9.5 affida a **una sessione diversa** da quella che ha scritto le note.
> **Data** · 19/08/2026.

---

## 1. Il lotto, in una tabella

| | |
|---|---|
| Specie | **lotto di manutenzione** (E35, `metodo_03` §9.4-bis): perimetro di sole note |
| Grezzi canonizzati | **0** — è il punto: l'elenco dei grezzi porta `# MANUTENZIONE` e non ha righe utili |
| Perimetro | **71 note**, generate da `06_operativo\candidate_r1.py` in `qa\lotti\r1_riconciliazione_verticale_note.txt` |
| Capacità 25-35 | **non si applica** (E35): un lotto di manutenzione non punta a produrre note |
| Note nuove prodotte | **5**: due di contenuto, da un fatto senza padrone emerso correggendo, e **tre note-strumento** che documentano gli script nati oggi. Le note-strumento non contano nel budget (E17), le due di contenuto sono sotto le 30 di E28: nessuna soglia scattata |
| Note toccate in più (E32) | **6**, dichiarate mentre le si toccava sotto la riga di separazione dell'elenco |
| QA di lotto | **0 ERRORI, 47 AVVISI** — motivati al §5 |
| Giri di giudizio | ⚠️ **0 — da fare in una sessione diversa** |

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

⚠️ **La seconda condizione è stata rafforzata rispetto a come era stata dettata in apertura, e
il perché va scritto.** Il criterio d'ordine diceva «e fra le sue fonti non c'è nessuna fonte
prescrittiva». Applicato alla lettera, lasciava **fuori dal perimetro 26 note che nominano un
punto critico senza citare il manuale HACCP**, perché citavano *un'altra* fonte prescrittiva —
l'elenco delle attrezzature, la checklist del metal detector, il piano di manutenzione. Ma il
limite critico di un CCP lo prescrive **il manuale**, non il registro degli strumenti:
`fatto-strumenti-cf-02-e-ccp4` nomina il CCP4 e cita i due registri della metrologia, e
nessuno dei due dice quale sia il limite critico di quel punto. Lasciarle fuori avrebbe fatto
mancare a R1 **esattamente le note che lo hanno generato**. Il criterio vero è: *una nota deve
avere sotto mano la fonte che prescrive ciò di cui parla*, non una fonte prescrittiva
qualsiasi. Per la famiglia «punto critico» quella fonte è il manuale HACCP; per le altre
quattro vale il criterio d'ordine.

### Il numero di partenza era 30, lo script ne dà 71, e la differenza si spiega

| Conteggio | Note |
|---|---|
| §11 del rapporto 1C: note che nominano un CCP senza citare il manuale | **30** |
| Lo stesso, ricontato dallo script sulla famiglia «punto critico» | **40** |
| Perimetro completo, cinque famiglie | **71** |

**Vince lo script.** La differenza fra 30 e 40 è che la famiglia «punto critico» dello script è
più larga di «nomina un CCP»: comprende anche `limite critico`, `HACCP`, `prerequisito`, `PRP`.
La differenza fra 40 e 71 sono **le altre quattro famiglie**, che al gate di 1C non erano state
contate affatto perché si guardava il solo manuale.

⚠️ Il criterio è **deliberatamente largo** sulla prima condizione. Il costo di guardare una
nota che non ne aveva bisogno è un minuto, e si chiude dichiarando che la fonte non serve — che
è ciò che E29 prescrive di fare. Il costo di **non** guardarne una che ne aveva bisogno è una
nota che afferma il falso dentro la misura «dopo».

---

## 3. I TRE NUMERI CHE E35 PRETENDE

| | |
|---|---|
| **Note guardate** | **71** |
| **Note corrette** | **41** |
| **Tasso di difetto** | **57,7 %** *(calcolato: 41 su 71)* |

⚠️ **È il numero che il gate deve pesare, e non è un numero piccolo.** Più della metà delle
note che parlano di qualcosa di prescritto non aveva sotto mano la prescrizione.

### Le 30 note guardate e chiuse senza correzione, per ragione

| Ragione | Note | Quali |
|---|---|---|
| **Nessuna fonte prescrittiva citabile le governa** — energia, costi, utenze: il corpus non contiene il contratto di fornitura elettrica, e la soglia contrattuale non è una prescrizione di processo | **11** | `area-amministrazione` · `area-direzione` · `area-logistica` · `fatto-energia-reattiva-oltre-soglia` · `fatto-potenza-impegnata-quasi-satura` · `kpi-fattura-energia-maggio-2026` · `kpi-incremento-energia-maggio-su-aprile` · `kpi-metano-forni-maggio-2026` · `kpi-quadratura-consumi-energetici-maggio` · `questione-costo-energia-elettrica` · `entita-veneta-energia` |
| **La prescrizione ha già un padrone che la porta**, e la nota lo linka: copiarla di nuovo violerebbe «un fatto, un padrone» | **19** | `area-manutenzione` · `area-produzione` · `fatto-blackout-21-04-riavvio-centraline` · `fatto-fermo-pkm-450-l26130` · `fatto-integrita-log-allarmi-cf-02` · `fatto-nc-102-origine-interna` · `fatto-porta-cella-cf-02-aperta-38-minuti` · `fatto-quaderno-capoturno-linea1` · `fatto-riunione-direzione-reclamo-l26130` · `fatto-sonda-prodotto-cf-02-in-avaria` · `questione-limite-allarme-porta-cf-02` · `questione-sbrinamenti-fascia-notturna-cf-02` · `concetto-fefo` · `kpi-sbrinamenti-cf-02-aprile` · `questione-scarti-riavvio-l26130` · `doc-scheda-tecnica-af-sn-0450` · `entita-calservice-italia` · `entita-metrolab-taratura` · `macchina-cf-01` |

⚠️ **La seconda riga è il motivo per cui il tasso non è ancora più alto**, ed è una scoperta
del lotto: il vault aveva già tre note-padrone che portano il manuale — `doc-ccp2-limite-critico`,
`doc-ccp4-limite-critico`, `doc-manuale-haccp` — nate in 1B e 1C. La riconciliazione verticale
era quindi **in parte già fatta**; quello che mancava era il collegamento fra la nota che
afferma e la nota che porta la prescrizione.

---

## 4. La distinzione che dà il senso al lotto: incompleta o afferma il falso

`metodo_03` non basta a dirlo, e il gate lo ha chiesto per nome: **una nota che si limita a non
citare la fonte è incompleta; una nota che dichiara mancante ciò che il manuale contiene, o che
attribuisce alla fonte qualcosa che la fonte non dice, AFFERMA IL FALSO.** Il secondo numero è
quello che conta.

| Classe | Note | Esempi |
|---|---|---|
| **Incomplete** — la nota diceva il vero, mancava l'aggancio | **34** | `fatto-tassello-aisi-clip-rotta`, `entita-ionut-popescu`, `macchina-ts-01`, `prodotto-af-sn-0450` |
| **Affermavano il falso** — la nota, con la fonte sotto mano, va riscritta nella sostanza | **7** | vedi sotto |

### Le sette che affermavano il falso

1. **`questione-durata-deviazione-ccp2-l26130`** — scriveva che «la durata della permanenza
   sotto il limite critico è ciò che determina il perimetro del prodotto da segregare». Il
   manuale lega il blocco a **«tutto il prodotto transitato dall'ultimo controllo conforme»**:
   è un'altra grandezza, e più larga.
2. **`fatto-riepilogo-datalogger-inaffidabile`** — attribuiva al piano HACCP una preferenza per
   la registrazione automatica sulla trascrizione manuale. Il piano **le vuole entrambe** e ne
   prescrive il confronto settimanale: sono fatte per verificarsi a vicenda.
3. **`fatto-prodotto-non-segregato-deviazione-ccp2`** — trattava la segregazione come una
   domanda aperta a fine turno. Il manuale la prescrive senza margini, insieme alla notifica
   immediata alla qualità: non era un dubbio, era un adempimento non eseguito.
4. **`fatto-nessuna-nc-per-allarmi-cf-02`** — registrava l'assenza delle non conformità come
   una lacuna del registro. Il manuale rende la registrazione **obbligatoria** per ogni
   deviazione, e dalla seconda nel trimestre aggiunge l'analisi della causa radice: sei eventi
   in un mese superano la soglia di gran lunga.
5. **`questione-tassello-inox-non-passato`** — chiudeva l'episodio come «verifica poi conforme».
   Il manuale prescrive che **una mancata rilevazione, anche di un solo tassello**, apra fermo
   linea, blocco, segregazione e non conformità: la NC mancante non è una lacuna d'archivio, è
   un adempimento non eseguito.
6. **`doc-mod-qa-07`** — dichiarava la frequenza del CCP3 «ogni 60 minuti più avvio e fine
   produzione». Il manuale ne prescrive **due in più**: a cambio prodotto e dopo ogni intervento
   sull'apparecchio.
7. **`concetto-ccp`** — presentava tre punti critici. **Sono quattro**: il CCP4 sta su una linea
   diversa dallo snack, e le fonti della Linea 1 non lo nominano.

⚠️ **In 1C erano quattro su undici, cioè il 36 %. Qui sono sette su 41 corrette, cioè il 17 %.**
La classe più grave è meno frequente di quanto il campione di 1C facesse temere, ma non è
sparita — ed è concentrata dove il vault ragiona sulle conseguenze di una deviazione, cioè
esattamente dove la misura «dopo» andrà a interrogarlo.

---

## 5. Gli avvisi della QA, motivati

**0 ERRORI, 47 AVVISI**, in cinque famiglie disgiunte che sommano al totale.

| Famiglia | Quanti | Motivazione |
|---|---|---|
| Corpo fra 301 e 350 parole | **26** | ⚠️ **È l'avviso che questo lotto produce per costruzione**: aggiungere a una nota la fonte che la prescrive allunga il corpo, e sedici note del perimetro erano già sopra le 280 parole. Nessuna supera il tetto di 350, e in nessun caso la nota è stata spezzata, perché spezzarla separerebbe l'affermazione dalla prescrizione che la governa — cioè esattamente il difetto che il lotto ripara. È il **candidato emendamento 2** del §10 |
| `summary` e `title` si sovrappongono per meno del 20 % | **11** | Sono le note-questione, il cui titolo è una domanda e il cui summary è la risposta con i dati: per costruzione condividono poche parole |
| Riscontro visivo su fonte immagine | **3** | Note costruite su scansioni e fotografie, con `verifica: visiva`: l'estrattore di testo congelato restituisce stringa vuota per costruzione, e i valori sono stati letti a occhio |
| Preesistenti e **non toccati**, per la regola di perimetro | **4** | ⚠️ `fatto-nc-102-origine-interna` (summary di 258 caratteri), `fatto-blackout-21-04-riavvio-centraline` e `fatto-sonda-prodotto-cf-02-in-avaria` (lontane dall'`_index` della cartella), `macchina-pkm-450` (una fonte che sorregge poche affermazioni). **Non appartengono a R1** e non sono stati corretti: il lotto guarda le note su cui una fonte prescrittiva dice qualcosa, non è un ripasso generale. Si dichiarano qui, come la regola impone |
| Citazione o ora senza riscontro, su fonte immagine | **3** | Un orario letto su una scansione, che l'estrattore congelato non restituisce |

---

## 6. I conflitti, dalla tabella di tracciamento

Il numero **non si legge a occhio**: lo produce `06_operativo\conta_tracciamento.py`, nato in
questa stessa giornata perché era l'ultimo numero del progetto dichiarato senza script.

<!-- TABELLA DI TRACCIAMENTO - generata da `06_operativo\conta_tracciamento.py`
     il 2026-08-19. Si incolla VERBATIM: il numero delle righe non si legge a occhio. -->

| Esito | Righe | Quali |
|---|---|---|
| riconciliata | **3** | T17, T22, T30 |
| aperta dichiarata | **24** | T1, T2, T3, T4, T18, T23, T24, T25, T26, T27, T28, T32, T35, T36, T37, T38, T42, T43, T44, T45, T46, T47, T48, T64 |
| chiusa | **2** | T20, T33 |
| tracciata | **35** | T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T19, T21, T29, T31, T34, T39, T40, T41, T49, T50, T51, T52, T53, T54, T55, T56, T57, T58, T59, T60, T61, T62, T63 |
| **totale righe** | **64** | da T1 a T64, nessuna mancante e nessuna duplicata |

**R1 ha aperto dieci righe, da T55 a T64.** Nove nascono dalla **guardia**: una fonte
prescrittiva il cui grezzo appartiene a un lotto non ancora canonizzato **non si cita e non si
usa** — citarla la farebbe risultare «già coperta» e manderebbe in rosso la disgiunzione della
matrice; scriverne il contenuto senza citarla è contesto importato. Si apre invece una riga con
l'obbligo esplicito per il lotto che la porterà. Precedente identico: **T18**.

La decima, **T64**, è una divergenza nuova con **entrambe le gambe canonizzate**, ed è di una
specie che la tabella non aveva ancora: non è un registro contro un altro registro, è **un
registro contro la fonte che prescrive**.

---

## 7. Lo strumento di E29: l'elenco delle fonti prescrittive

Vive in `06_operativo\fonti_prescrittive_corpus_v1.md`, **fuori dal vault** perché è metodo e
non contenuto, ed è generato da `06_operativo\elenco_fonti_prescrittive.py`. Serve a R1 e
servirà a ogni lotto dopo.

| | |
|---|---|
| Fonti prescrittive del corpus | **36** |
| **Citabili oggi** (grezzo già canonizzato) | **8** |
| **Da tracciare** (grezzo in un lotto futuro) | **28** |

**Le otto citabili**: il manuale HACCP (pilota) · la scheda tecnica di prodotto, il manuale
della `PKM-450`, la checklist del metal detector, la scheda di manutenzione, il piano di
produzione (1A) · il contratto di manutenzione del freddo (1B) · l'elenco delle attrezzature (1C).

⚠️ **Che cosa il lotto NON ha potuto usare, e lo dichiara**: `IO-05`, `PRO-QA-08`, il capitolato
degli imballaggi, il DVR, l'accordo quadro con il cliente, la scheda tecnica della farina, la
job description del responsabile di produzione. Sono le prescrizioni che mancano di più alle
note già scritte, e ognuna ha la sua riga di tracciamento.

**Il criterio con cui una fonte è stata dichiarata prescrittiva** sta nel documento e nel
sorgente dello script: prescrive chi dice **come una cosa DEVE essere** — limite, frequenza,
metodo, responsabilità, specifica, obbligo, tariffa in vigore — invece di **registrare ciò che
è successo**. Un certificato **non** è una fonte prescrittiva: attesta uno stato, non lo
prescrive.

---

## 8. I conteggi del vault a chiusura del primo giro, da script

Generati **dopo** la nota-sessione nel journal, come E34 impone da oggi.

<!-- CONTEGGI DEL VAULT — generati da `06_operativo\qa\conta_stato.py` il 2026-08-19.
     Si incollano VERBATIM: non si ricompongono a mano, non si riscrivono in prosa. -->

| Grandezza | Valore |
|---|---|
| Note nel vault | **179** |
| di cui `_index` | 11 |
| di cui note-strumento del progetto | 9 |
| di cui note di diario (`sessione`, `daily`) | 4 |
| **di cui note di contenuto** | **155** |
| Note per cartella | areas 94 · entities 22 · data 22 · code 10 · projects 8 · docs 8 · workspace 7 · concepts 5 · self 1 · outputs 1 · sources 1 |
| Note per `type` | atomica 97 · conflitto 33 · entita 18 · hub 12 · index 11 · concetto 4 · sessione 4 |
| Questioni aperte (`type: conflitto`) | 33 |
| Grezzi in `sources\` | 160 |
| Grezzi citati da almeno una nota | **35** |
| Grezzi restanti | **125** |

**I grezzi restano 125 e i citati 35**, ed è la firma di un lotto di manutenzione: nessun
grezzo nuovo è entrato. Le note di contenuto passano da 153 a **155**, cioè le due nate da
fatti senza padrone; le note-strumento da 6 a **9**, perché `metodo_03` §7 vuole in `code\`
la nota che documenta ogni script del progetto, e oggi ne sono nati tre.

⚠️ **La QA a perimetro vault resta a 128 ERRORI, esattamente com'era prima di R1.** Sono
tutti e 128 l'incompletezza del vault — 125 grezzi non ancora canonizzati e 3 aree senza hub
— e il fatto che il numero non si sia mosso è la prova che il lotto non ha rotto nulla.

---

## 9. ⚠️ COSA MANCA, ed è la ragione per cui il lotto non è chiuso

`metodo_03` §9.5 passo 3 vuole che la revisione col canone la faccia **una sessione diversa da
quella che ha scritto le note**, e il passo 6 vuole lo strato di giudizio su **un subagente a
contesto pulito che non riceve il canone**. Io sono la sessione che ha scritto le correzioni:
non posso essere anche quella che le giudica, e un giudizio auto-somministrato varrebbe zero
esattamente come varrebbe zero un canonizzatore che si riscrive il manuale.

**Resta da fare, nell'ordine:**

1. **Strato di giudizio** con `PROMPT_GIUDIZIO` v2 su tutte le note nuove o modificate. Il
   pacchetto è **già generato dopo le correzioni** (E33), in
   `06_operativo\qa\2026-08-19_r1_riconciliazione_verticale\pacchetto_giudizio_provenance.txt`.
2. **Revisione col canone**, sessione diversa, con il campione delle note nate dalle correzioni.
3. **Ri-giudizio** (E9) con la regola d'arresto di E26: zero rilievi accolti, comunque al terzo
   giro, e se il terzo produce ancora rilievi il rapporto **nomina il pattern**.
4. **Re-QA**, `llms.txt` rigenerato, `_index` e hub riverificati.
5. `# CHIUSO 2026-08-19` in testa all'elenco del lotto — **oggi non c'è, ed è voluto**: il lotto
   non è chiuso e `verifica_matrice_lotti.py` non deve credere il contrario.
6. Riga nel CSV `matrice_corpus_v1.csv`: ⚠️ **non applicabile**, il CSV mappa file × fatto e
   questo lotto non porta file. Lo si dichiara qui invece di lasciarlo dedurre.

**La sessione successiva PRIMA finisce il lotto**, come §5 del prompt dei lotti impone quando
un lotto non si chiude nella sessione che lo apre. Lo stato dice esattamente quali note
esistono e cosa manca.

---

## 10. Candidati emendamento

1. **La condizione 2 del criterio di perimetro va scritta in `metodo_03`, e non è un dettaglio
   di script.** «Una nota deve citare la fonte che prescrive *ciò di cui parla*, non una fonte
   prescrittiva qualsiasi» è la forma corretta di E29, e questo lotto ha dimostrato che la forma
   generica lascia fuori 26 note su 71. **Candidato E36.**
2. **Il tetto delle 350 parole entra in tensione con E29 e la tensione va arbitrata.** Ventidue
   note su 41 corrette sono finite nella fascia 301-350 solo per aver aggiunto la prescrizione
   che le governa. La regola «si motiva o si spezza» qui non aiuta: spezzare separerebbe
   l'affermazione dalla sua prescrizione. **Candidato: escludere dal conteggio la riga che cita
   una fonte prescrittiva, oppure alzare il tetto per le note che ne portano una.**
3. **Il conteggio delle note di un lotto di manutenzione non è confrontabile con quello di un
   lotto di canonizzazione**, e i due non vanno messi nella stessa serie quando si rivedrà la
   fascia 25-35 a dieci lotti chiusi (E31).

---

## 11. Cosa chiedo al titolare e al coordinatore

⚠️ **Il rapporto va al coordinatore PRIMA dell'approvazione del titolare**, perché il tasso di
difetto decide una cosa che vale per tutto il resto del progetto.

**La domanda è una sola: 57,7 % di difetto sul perimetro basta a dire che il ripasso va rifatto
a fine corsa, o E29 in vigore basta a impedire che si riformi?**

I due elementi per decidere, e vanno letti insieme:

- **A favore del «basta E29»**: il difetto è **storico**. Tutte le 71 note del perimetro sono
  state scritte **prima** che E29 esistesse — nasce al gate di 1C, il 19/08/2026. Nessun lotto
  ha ancora canonizzato *sotto* quella regola, quindi il 57,7 % misura il debito accumulato,
  non il tasso di produzione del difetto.
- **A sfavore**: R1 ha potuto usare **8 fonti prescrittive su 36**. Le altre 28 entreranno nei
  lotti 2-10, e ognuna riaprirà note già scritte — comprese quelle che R1 ha appena corretto.
  ⚠️ **Il ripasso a fine corsa non è evitabile: è già dovuto**, e le righe da T55 a T63 lo
  scrivono lotto per lotto. La domanda vera non è *se* rifarlo, ma **se rifarlo una volta sola
  alla fine o pezzo per pezzo alla chiusura di ogni lotto che porta una fonte prescrittiva.**

**La mia proposta**, che non è una decisione: **pezzo per pezzo**, con l'obbligo già scritto
nelle righe di tracciamento, e un secondo R1 a fine corsa come rete, dimensionato su quello che
le righe avranno lasciato aperto. Il motivo è quello di E29 stesso: la fonte che prescrive non
si trova da sola, e più tardi la si cerca più note ha già attraversato.
