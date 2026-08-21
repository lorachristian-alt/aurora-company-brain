# Stato della canonizzazione — vault `aurora-cervello`

> **Cos'è** · Lo stato di oggi del vault: cosa è stato canonizzato, con quale esito, e
> cosa resta. Solo stato, mai una regola: le regole stanno in
> `01_metodo\metodo_03_canonizzazione.md`, le decisioni in `06_operativo\decision_log.md`.
> **Aggiornato al** · **21/08/2026, GATE FINALE del lotto 2B, che lo ha APPROVATO pienamente.**
> ⚠️ **È il primo gate del progetto che NON produce emendamenti nuovi al metodo** — il manuale
> resta a 46 — ed è un segnale che vale la pena registrare: il metodo si sta stabilizzando.
> Prima, nella stessa giornata, il **COMPLETAMENTO del ciclo del lotto 2B** — la revisione col
> canone, che alla chiusura era stata dichiarata scoperta, è stata eseguita e il ciclo è
> intero. Prima, nella notte, la **chiusura del lotto 2B** — l'autocontrollo analitico:
> tamponi di superficie, acqua potabile, acque reflue. ⚠️ **Il lotto è arrivato con cinque
> grezzi e ne ha canonizzati tre**: si è spezzato in apertura (E28) e gli allergeni sono
> passati a **2B-bis**. Prima, il 20/08: il **GATE del lotto 2A**, che lo ha **APPROVATO** e ha
> prodotto **E41-E44**, quattro emendamenti da un solo gate. Prima ancora, il 19/08: la
> chiusura di 2A, il gate di R1 con E39 ed E40, la manutenzione degli strumenti, E34 ed E35, il
> gate intermedio con E36-E38 e la chiusura di R1. Tutti i numeri qui dentro sono riportati da
> script, **e da E44 ognuno porta l'ora della propria misura**.
> Lo stato della pipeline RAG sta in `06_operativo\stato_rag_produzione.md`, non qui; il
> piano dei lotti e la tabella di tracciamento delle questioni trasversali stanno in
> `06_operativo\matrice_lotti_corpus_v1.md`, non qui.

---

## Dove siamo

| | |
|---|---|
| Lotti chiusi | **7 di canonizzazione** — `l26130` (fetta pilota, S2), **`1A`** (Linea 1: turno, CCP, confezionatrice), **`1B`** (freddo ed energia), **`1C`** (metrologia e gas tecnici), **`2A`** (il lavaggio CIP), **`2B`** (l'autocontrollo analitico) e **`2B-bis`** (gli allergeni) — **più `R1`**, il primo **lotto di manutenzione** (E35), approvato al suo gate il 19/08/2026. ⚠️ **R1 vale un lotto nel ritmo ma NON entra nella serie della capacità** (E38): misura riparazioni, non produzione |
| Grezzi copiati nel vault | 160/160, verificati contro `manifest_corpus_v1.1.json`: zero scarti, zero estranei, zero sottocartelle |
| I conteggi del vault | nel blocco qui sotto, **incollato verbatim** da `conta_stato.py` |
| Suite QA | **verde sul perimetro di lotto**; ⚠️ **dal gate del 21/08 la provenance legge l'ESTRAZIONE DI CANTIERE** (E48), che aggiunge marcati formule e barrato — l'estrattore di misura resta byte-identico e `estrazione_cantiere.py --prova` lo dimostra su tutti i 161 grezzi; sul vault tre controlli su quattro sono a zero errori. ⚠️ Dal gate di 2A la QA ha **due controlli nuovi**: l'artefatto di ricerca che E43 impone a chi dichiara un'assenza, e **l'omogeneità dei fine riga** — il primo controllo del progetto che non guarda il contenuto di una nota ma il suo **supporto** |
| `llms.txt` | rigenerato dal frontmatter, allineato |
| Matrice dei lotti | 160/160 grezzi, zero scoperti, zero doppi (`verifica_matrice_lotti.py` verde). ⚠️ **I budget dei lotti 2-10 sono SUPERATI** e il piano non è più a 12 lotti: vale **E31**, la capacità di 25-35 note per lotto, e i grezzi si decidono in apertura. **Stima: circa 28-30 lotti**, scritta anche nella scaletta perché cambia il calendario di S4-S5. Ridisegnato in dettaglio **solo il tema 2** (2A · 2B · 2C) |
| **PROSSIMO ATTO** | **Il TEMA 3, il sistema qualità: tredici grezzi, da RIPACCHETTARE in apertura** (E31) in pacchetti da 3-5 lungo le cuciture, col conteggio dei fatti prima di scrivere (E21). ⚠️ **Il primo pacchetto eredita cinque obblighi già in tabella di tracciamento**, e il cruscotto KPI porta **65 formule** che l'estrazione di cantiere ora vede: è il primo lotto che la esercita su dati veri, e il rapporto dovrà dichiarare quanti riscontri arrivino dallo strato `[FORMULA]` |

⚠️ **Errata del 19/08/2026 sui numeri del lotto 1A.** Questo stato dichiarava «105 note, di
cui 11 `_index` e 6 note-strumento: 88 di contenuto». `qa_all.py` a chiusura di 1A contava
**106** note: il 105 escludeva `_index-sources` ma sottraeva ugualmente tutti e undici gli
`_index`. Il numero corretto è **89 note di contenuto**. La correzione resta visibile, come
prescrive la regola del gate 1A.

## I conteggi, da script

<!-- CONTEGGI DEL VAULT — generati da `06_operativo\qa\conta_stato.py` il 2026-08-21.
     Si incollano VERBATIM: non si ricompongono a mano, non si riscrivono in prosa. -->

| Grandezza | Valore |
|---|---|
| Note nel vault | **281** |
| di cui `_index` | 11 |
| di cui note-strumento del progetto | 15 |
| di cui note di diario (`sessione`, `daily`) | 7 |
| **di cui note di contenuto** | **248** |
| Note per cartella | areas 151 · docs 31 · data 29 · entities 27 · code 16 · workspace 10 · projects 8 · concepts 6 · self 1 · outputs 1 · sources 1 |
| Note per `type` | atomica 177 · conflitto 46 · entita 22 · hub 13 · index 11 · sessione 7 · concetto 5 |
| Questioni aperte (`type: conflitto`) | 46 |
| Grezzi in `sources\` | 160 |
| Grezzi citati da almeno una nota | **43** |
| Grezzi restanti | **117** |

⚠️ **Questo blocco non si riscrive a mano.** Nasce al gate del lotto 1B da due sviste di
conteggio in due lotti — 46 contro 32 nel rapporto 1A, 105 e 88 in questo stato quando
`qa_all.py` contava 106 e 89 — e nessuna delle due era un errore di canonizzazione: erano
sottrazioni fatte a mano su numeri veri. Da qui in poi lo stato e i rapporti **incollano**,
non ricompongono.

## Il lotto 2A, chiuso il 19/08/2026 — il lavaggio CIP

**Perimetro:** 3 grezzi — il log del lavaggio CIP di maggio, `IO-05` che lo prescrive, la
scheda di sicurezza del detergente acido — più **10 note riaperte** da E37, **7 toccate** e
**33 nate**: **50 note controllate**.

| | |
|---|---|
| Capacità attesa | 25-35 note di contenuto (E31) |
| Prodotte | **30** di contenuto — **dentro la fascia** |
| Densità | **10,0 note per grezzo** |
| QA di lotto | **0 ERRORI, 44 AVVISI**, motivati nel rapporto §4 |
| Giri di giudizio | **tre**: 12, 7 e 9 rilievi accolti — **il ciclo non converge** |
| Revisione col canone | **6 A · 9 B · 0 C** |
| Righe di tracciamento | **T21 e T29 chiuse**; **cinque nuove**, da T70 a T74 |
| Canone | **nove divergenze nuove**, in sezione datata |

### L'esperimento, e il numero che il gate deve pesare

| Tasso | Valore | Misura |
|---|---|---|
| di **riapertura** | **40,0 %** *(4 su 10)* | il **debito** |
| di **difetto di produzione** | **3,3 %** *(1 su 30)* | il **metodo** |

⚠️ **Contro il 57,7 % di R1, l'ipotesi del debito storico regge.** R1 misurava note scritte
tutte prima che E29 ed E36 esistessero; qui, con le stesse regole in vigore e lo stesso
criterio, il metodo produce il difetto in **un caso su trenta**. L'unico caso è dichiarato
col suo nome e **non è stato aggiustato**: bastava aggiungere una fonte per portare il tasso
a zero.

### Che cosa ha trovato

Il tracciato chiude conformi **28 cicli su 30**, e **nessuno** ha girato con i parametri
prescritti: sei fasi su sei più corte, **170 letture di portata su 170** sotto il valore
prescritto, temperature fuori finestra. Vince `IO-05`, il log resta com'è.

⚠️ **La radice è nella forma del criterio**: l'accettazione è scritta come **scarto
dall'acqua di rete**, un riferimento che il pannello non acquisisce. E **tre divergenze di
specie nuova** — due documenti **prescrittivi** in vigore che non concordano fra loro, su
quale sia il detergente acido, su quali DPI, su ogni quanto verificare il lavaocchi.

⚠️ **Due assenze dichiarate false**, ed è l'errore più grave del lotto: la formula di E3 usata
**senza** la ricerca su tutto `sources\`. Le ha trovate la revisione col canone.

## Il lotto R1, chiuso il 19/08/2026 — riconciliazione verticale

**Perimetro:** **0 grezzi, 71 note candidate** più 14 toccate o nate in corso di lotto, per
**85 note controllate**. È il primo **lotto di manutenzione** (E35): non canonizza grezzi
nuovi, ripara note già scritte. L'elenco dei grezzi porta `# MANUTENZIONE` e nessuna riga
utile; il perimetro vero è l'elenco delle note accanto, **generato da
`06_operativo\candidate_r1.py`** e mai a memoria.

| | |
|---|---|
| Note guardate | **71** |
| Note corrette | **41** |
| **Tasso di difetto** | **57,7 %** *(calcolato: 41 su 71)* |
| di cui affermavano il falso | **7** — contro 34 semplicemente incomplete |
| Note nuove | **10** — 5 di contenuto, 4 note-strumento, 1 di diario |
| QA di lotto | **0 ERRORI, 51 AVVISI**, motivati nel rapporto §5 |
| Giri di giudizio | **tre**: 24, 13 e 9 rilievi accolti |
| Revisione col canone | **7 A · 3 B · 0 C**, più 17 doppie padrone |
| Righe di tracciamento | **12 nuove**, da T55 a T66, più T24 estesa |

**Cosa ha trovato.** Che più della metà delle note che parlano di un punto critico, di una
taratura, di una frequenza, di un limite o di una responsabilità di processo **non aveva sotto
mano il documento che quella cosa la prescrive**. Sette non erano solo incomplete:
**affermavano il falso** — la più grave legava il perimetro del prodotto da segregare alla
*durata* della deviazione, mentre il manuale lo lega **all'ultimo controllo conforme**.

⚠️ **E ha trovato che il documento prescrittivo di vertice ha due difetti propri.** Il manuale
HACCP **dichiara rimosso** il carrello dei ricambi un mese prima che una non conformità e una
diffida lo trovino ancora in linea, e **non sa dire se la validazione del proprio CCP2 sia
stata rifatta**. Più una terza divergenza che rimette in discussione un arbitrato già fatto:
l'attività dell'acqua su due matrici. Tutte e tre sono nel canone, in sezione datata.

⚠️ **Il lotto si è chiuso NOMINANDO UN PATTERN, non con un quarto giro** (E26). Il pattern è
**«la cautela non si propaga»**: si dichiara come lettura ciò che era affermato come dato, e la
dichiarazione resta dove è stata scritta — mentre la stessa affermazione, ripetuta nel
riassunto, in una cella di tabella o in una glossa a un wikilink, mantiene la grammatica del
fatto. È il pattern del lotto 1C esteso a **ogni** superficie di sintesi della nota.

**Lo strumento di E29 è nato qui**: `06_operativo\fonti_prescrittive_corpus_v1.md`, **36 fonti
prescrittive** di cui **8 citabili** e **28 da tracciare**. E con lui tre script nuovi:
`elenco_fonti_prescrittive.py`, `candidate_r1.py`, `conta_perimetro_lotto.py`.

### Il gate di R1, 19/08/2026 — APPROVATO

Il coordinatore ha letto il rapporto per intero e riverificato i numeri sul disco. Cosa il
gate ha prodotto, e resta a verbale:

| | |
|---|---|
| Verdetto | **APPROVATO** |
| Emendamenti | **E39** — la cautela si propaga (§9.5 passo 2-bis) · **E40** — la prescrizione si linka, non si ricopia (§5.1-bis). Metodo a **40** |
| Giurisprudenza | **§4.31** del passaggio di consegne: un giudice che dichiara degradato il proprio ingresso vale più di uno che emette |
| Collaudo | la via **V3** acquista un secondo difetto piantato — il pacchetto deve **portare l'appendice** col testo delle fonti (§4.29). Verificato per iniezione: senza appendice il collaudo diventa rosso. `collaudo_suite.py` **verde, 20 su 20** su tutte e cinque le vie |
| Candidato parcheggiato | lo script che segnala le superfici di sintesi rimaste assertive: **non si costruisce ora** (E28, una sola osservazione), si decide **dopo due lotti chiusi sotto E39**, col criterio già scritto in §6 del passaggio di consegne |

⚠️ **La QA a perimetro vault è stata RIMISURATA dopo la chiusura** (17:45, dopo il rapporto
delle 17:42) e resta a **128 ERRORI, tutti di incompletezza**: nessuna regressione, e il numero
è **misurato, non asserito**.

## Il lotto 1C, chiuso il 19/08/2026

**Perimetro:** 2 grezzi, elencati in `06_operativo\qa\lotti\lotto_01c_metrologia_gas.txt`.
L'elenco delle attrezzature con lo stato di taratura di 120 strumenti, e la bolla di ingresso
dei gas alimentari Nordgas del 06/05, in OCR degradato.

| | |
|---|---|
| Budget dichiarato | 12-18 note di contenuto |
| Prodotte | **27** di contenuto — **sforato di 9**, dichiarato in apertura e approvato |
| Densità | **13,5 note per grezzo**, contro 9,5 di 1B, 6,0 di 1A e 2,1 del pilota |
| Perché non si è spezzato | **E28**, approvato in apertura di questo lotto: si spezza sopra il +25 % **e** sopra le 30 note. 27 note stanno sotto il tetto, e i due grezzi sono una storia sola |
| QA di lotto | **0 ERRORI, 14 AVVISI**, motivati nel rapporto. ⚠️ *Errata del 19/08/2026: questa cella diceva 9. Il report di lotto conta 14 — `qa_frontmatter` 6, `qa_provenance` 8 — e lo stesso numero era ricomposto in prosa anche nel §5 del rapporto 1C, dove diceva 8. Tre valori per un numero solo: sono tutti e tre corretti a partire dallo script, che è l'unica fonte.* |
| Passaggi di controllo | rilettura dei «Perché conta» contro le sole fonti (antidoto 1B), **tre giri di giudizio** — 27 rilievi, tutti accolti — e revisione col canone |
| Versione del prompt di giudizio | **v2** |
| Righe dell'elenco | **120**, non 121 come diceva la matrice: errata registrata nel registro delle modifiche |

**Cosa ha trovato.** Che **Aurora tiene due registri paralleli della stessa metrologia** — il
piano di manutenzione e l'elenco delle attrezzature — e che dove si sovrappongono non
concordano su date, periodicità e, sul pastorizzatore, nemmeno sull'esecutore. Il caso più
grave è l'`MD-1800`: un registro lo dà `SCADUTO` dal 03/04/26, l'altro `Conforme` fino al
19/08/2026. Sulla cella surgelati le registrazioni metrologiche sono **quattro, in tre
documenti, con tre esecutori diversi**, e nessuna coincide con la data che il verbale
dell'ispezione sanitaria attesta.

**Sul lato gas:** l'azoto entra per due strade — serbatoio criogenico e rampa di bombole di
scorta — e questo **chiude T17 come riconciliazione, non come divergenza**. La consegna del
06/05 è identificata da tre codici di lotto e due numeri di bolla diversi, e il certificato di
analisi che la bolla richiama **non è in archivio**.

⚠️ **La riconciliazione col vault ha reso più dei due grezzi**: quattro delle nove divergenze
nuove nascono dal confronto con documenti già canonizzati — inventario di magazzino, mass
balance, piano di manutenzione, verbale ATS — e non dalla lettura dei due file del lotto.

⚠️ **Il terzo giro di giudizio ha trovato un difetto che riguarda tutto il vault, non questo
lotto:** undici note discutevano punti critici, tarature e frequenze **senza citare il manuale
HACCP**, che è la fonte che le prescrive — e in quattro casi il manuale conteneva esattamente
ciò che la nota dichiarava mancante. **Nel vault ci sono oggi 30 note che nominano un CCP e non
citano il manuale.** ⚠️ **La decisione è PRESA, e la porta il gate del lotto 1C: si guardano
ora, ed è il lotto R1.** Questa riga diceva ancora «la decisione è del titolare e sta nel
rapporto 1C §11», che era vero prima del gate e non lo è più — il prossimo atto in cima a
questo file e questa riga dicevano due cose diverse. ⚠️ **30 è il numero di partenza noto, non
il perimetro di R1**: il perimetro lo genera uno script, il criterio si scrive nel rapporto, e
se lo script dà un altro numero vince lo script (E35).

## Il lotto 1B, chiuso il 19/08/2026

**Perimetro:** 4 grezzi, elencati in `06_operativo\qa\lotti\lotto_01b_freddo_energia.txt`.
Il log delle centraline frigorifere di aprile, il contratto di manutenzione degli impianti
del freddo — una bozza mai firmata —, i contatori di reparto di maggio e la fattura
dell'energia elettrica dello stesso mese.

| | |
|---|---|
| Nato da | **spezzamento in apertura** del vecchio 1B da 6 grezzi: proiettava ~41 note contro un budget di 22-30 (+37 %), oltre la soglia di E21 |
| Budget dichiarato | 22-30 note di contenuto |
| Prodotte | **38** di contenuto, più 1 di diario — **sforato di 8**, e lo scostamento è tutto post-revisione |
| Densità | **9,5 note per grezzo**, contro 6,0 di 1A e 2,1 del pilota |
| QA di lotto | **0 ERRORI, 18 AVVISI**, famiglie disgiunte che sommano al totale |
| Passaggi di controllo | **quattro giri di giudizio** più la revisione col canone: 31 rilievi distinti accolti, tutti fondati |
| Calibrazione del ritmo | **1B = 4 giri di giudizio e 31 rilievi accolti su 4 grezzi.** Il pattern che ha richiesto i giri extra è il **contesto importato** — la frase scritta per far capire, che porta dentro un fatto che le fonti della nota non contengono. Antidoto per i lotti successivi: rileggere ogni «Perché conta» contro le sole fonti della nota **prima** del primo giudizio (rapporto 1B, appendice A) |
| Aree nuove | **`amministrazione`**, quarto hub d'area: nasce qui e non nel lotto 6, perché è il lotto che porta una fattura passiva |
| Versione del prompt di giudizio | **v2**, prima applicazione |

**Cosa ha trovato.** Che la cella surgelati `CF-02` **è dentro il CCP4** — il manuale HACCP
le prescrive limite critico −18 °C, soglia di allarme −16 e notifica nominale — e che quindi
le sei risalite di aprile sono superamenti di un limite critico, non guasti d'impianto.
E **tre azioni correttive registrate che il dato disponibile non conferma**: è una famiglia
di divergenze nuova per il canone, e riguarda ciò che un auditor verifica per primo.

**Sul lato energia:** i contatori di reparto misurano il 45,9 % del prelievo fatturato, il
costo di un kWh ha tre valori diversi e nessuno coincide con quello usato nei conti interni,
e le somme che «non tornano» nel file dei consumi sono arrotondamenti — verificato, non
assunto.

⚠️ **Il riconteggio ha corretto tre numeri del canone** (59/137/165 → 68/174/186): la
conclusione qualitativa resta, il conteggio no. Il canone è stato accresciuto in sezione
datata, non riscritto.

## Il lotto 1A, chiuso il 18/08/2026

**Perimetro:** 7 grezzi, elencati in `06_operativo\qa\lotti\lotto_01a_linea1_turno_ccp.txt`.
Il quaderno del capoturno di Linea 1, la trascrizione del MOD-QA-07, il manuale della
PKM-450, la scheda tecnica di AF-SN-0450, le prove di shelf life, il piano di produzione e
la scheda di manutenzione.

| | |
|---|---|
| Budget dichiarato | 34-42 note di contenuto |
| Prodotte | **42** — dentro il budget, al suo estremo alto |
| Note esistenti estese | 18 |
| Densità | **6,0 note per grezzo**, contro 2,1 del pilota |
| QA di lotto | **0 ERRORI, 30 AVVISI**, famiglie disgiunte che sommano al totale |
| Giudizio di provenance, 1º giro | 46 note · 38 pulite · 8 «afferma oltre» |
| Revisione col canone | **10 A · 10 B · 11 C · 0 sovra-atomizzazione** su 18 note campionate |
| Giudizio di provenance, 2º giro (E9) | 48 note · 40 pulite · 8 «afferma oltre» |
| Rilievi accolti in tutto | **26**, tutti verificati sui grezzi prima di correggere |
| Emendamenti approvati al gate | **E21-E25** in `metodo_03`, più `PROMPT_GIUDIZIO` v2 e un fix della suite |
| Versione del prompt di giudizio usata | **v1** — la v2 vale dal lotto 1B, mai retroattiva |

**I tre conflitti tracciati dal gate S2 sono chiusi**, tutti e tre come *aperti dichiarati*:
l'archivio non dà un vincitore a nessuno. Il più grave è nuovo: la scansione del `MOD-QA-07`
del 10/05 e la sua trascrizione destinata alla cartella evidenze per il cliente **non
raccontano lo stesso turno**.

⚠️ **Due difetti che il pilota aveva già pagato si sono ripresentati**: una fuga di canone e
una dichiarazione di assenza falsa. Entrambi trovati dai passaggi di revisione, entrambi
corretti. Il dettaglio sta in `06_operativo
apporto_lotto_1a.md`.

## Il perimetro vault

⚠️ **Misurato il 21/08/2026 alle 09:22:21**, dopo l'ultima scrittura del **completamento** del
lotto 2B (E44). Alla chiusura della notte i numeri erano 123 e 193: **gli errori non si sono
mossi, gli avvisi sono saliti di quattro** perché la revisione ha allungato le note.

| Controllo | Errori su tutto il vault |
|---|---|
| `qa_frontmatter` · `qa_link_integrity` · `qa_provenance` | **0 ciascuno** |
| `qa_copertura` | **123** — 119 grezzi non ancora canonizzati, 3 aree senza hub, **1 rilievo di merito** |
| **totale suite** | **123 errori, 197 avvisi** |

⚠️ **Il totale del vault scende per la seconda volta consecutiva** — 128 → 126 → **123** — e
scende ogni volta **esattamente dei grezzi che il lotto ha canonizzato**. **Ma non tutti gli errori sono più incompletezza**:
il centoventiseiesimo è un **rilievo di merito**, il controllo delle doppie padrone che
accosta due note per i valori `0,9 · 1,1 · 1,4`. È un **falso positivo dimostrabile** — le due
note non hanno nessuna fonte in comune e i numeri sono grandezze diverse con unità diverse —
e **non è stato corretto**: la correzione allenta un controllo, e §4.9 vuole per quello un
perimetro chiuso e un difetto piantato nuovo. Sta fra le vigilanze del passaggio di consegne,
da chiudere prima del gate finale.

## ~~Densità del pilota — il dato per dimensionare i lotti di S4~~ — SUPERATA da E31

⚠️ **Superata il 19/08/2026 dall'emendamento E31**, al gate del lotto 1C: il budget di un
lotto è una **capacità** — 25-35 note di contenuto — e non una stima ricavata moltiplicando
una densità per un numero di file. I quattro consuntivi danno 2,1 · 6,0 · 9,5 · 13,5 note per
grezzo: la densità varia del 147 % sulla propria media, le note per lotto del 50 %.
**L'invariante non è la densità, è il lotto.** Quanti grezzi entrino si decide in apertura
contando i fatti (E21, E28).

**Non si cancella**, come le fasce della matrice: è la misura che ha retto la pianificazione
per quattro lotti, e la sezione barrata è il solo posto in cui resta scritto su che cosa
poggiavano i budget di allora.

~~**41 note di contenuto su 22 grezzi** al momento del gate, **46 su 22** a chiusura: poco più
di due note di contenuto per documento. È la prima misura disponibile del rapporto fra
documenti e fatti, e serve a dimensionare i lotti delle Sessioni 4-5: **un lotto da 30 grezzi
va preventivato attorno alle 60-70 note di contenuto**, più gli `_index` delle cartelle che
tocca.~~

~~⚠️ Il rapporto non è costante e non va usato come formula: dipende da quanti fatti porta ogni
documento. La fetta pilota era **densa per costruzione** — è il caso centrale dell'archivio —
e un lotto di rumore di fondo produrrà molte meno note per documento.~~

## In cima al prossimo lotto della Linea 1: il quaderno del capoturno

`appunti_capoturno_quaderno_linea1_OCR.txt` è la gamba mancante di **tre** conflitti trovati
dalla misura di fumo e non registrabili in questa fetta perché il file non c'era. Quando
entrerà, obbligherà a riaprire `fatto-verifiche-ccp3-turno-l26130`,
`questione-pezzi-prodotti-l26130` e `fatto-fermo-pkm-450-l26130`. **Va messo in cima al lotto
che tocca la Linea 1**, non incontrato per caso a metà Sessione 5.

## Il lotto `l26130` — la fetta pilota

**Perimetro:** 22 grezzi, elencati in `06_operativo\qa\fetta_l26130.txt`. Il nucleo del
caso del 10/05/2026 (log del pastorizzatore, foglio OEE, mass balance, MOD-QA-07 e
MOD-QA-31, reclamo, richiesta 48 ore, lettera in bozza, le due foto, rapporto di fermo
macchina, mail sul ricambio, inventario FEFO, registro NC, trascrizione della riunione,
verbale ATS, estratto HACCP), più la convocazione della riunione e **due coppie di
duplicati** — rapporto di prova del laboratorio e certificato di analisi della farina —
volute in fetta per collaudare la regola «un duplicato, una nota, due nomi in `fonti`»
prima che arrivi in produzione nelle Sessioni 4-5.

**Note prodotte, per cartella** *(contate da `qa_all.py`, non a memoria)*

| Cartella | Note |
|---|---|
| `areas\` | 24 |
| `entities\` | 9 |
| `projects\` | 8 |
| `code\` | 7 |
| `data\` | 5 |
| `docs\` | 3 |
| `concepts\` | 2 |
| `workspace\` | 2 |
| `self\` | 1 |
| `outputs\` | 1 |
| `sources\` | 1 |
| **totale** | **63** |

**Per `type`:** 25 atomica · 11 index · 11 conflitto · 8 hub · 7 entita · 1 concetto.

Escluse `workspace\` e `sources\` dai conteggi di qualità: **60** note.

`self\` e `outputs\` contengono per ora il solo `_index`: il lotto pilota riguarda un lotto
di produzione e la sua gestione, non l'identità di Aurora, e la risposta al cliente non è
mai uscita dallo stato di bozza.

## Esito della suite QA

Perimetro di lotto, ultimo passaggio dopo le correzioni del gate: **0 ERRORI, 33 AVVISI**.
Copertura **22/22** grezzi, nessun documento muto.

⚠️ Il pass **`--perimetro vault` è rosso**, ed è corretto che lo sia: 138 grezzi non sono
ancora citati da nessuna nota. **Il grafo invece non lo è più:** la questione delle
note-strumento staccate, lasciata aperta dal gate S2, è stata chiusa il 18/08 con
l'emendamento **E20** — l'esenzione dalla componente unica vale per la **classe
nota-strumento del progetto**, non per la cartella `code\`, e un `_index` partecipa solo se
la sua cartella ha almeno una nota valutabile. Effetto misurato:
`qa_link_integrity --perimetro vault` è passato da 1 errore a **0 errori, 0 avvisi**.
Il vault verde resta il traguardo delle Sessioni 4-5, non di un lotto.

**Gli avvisi, motivati per iscritto come richiede §9.5 passo 2.** Sono di tre famiglie, e
nessuna richiede una correzione:

- **21 avvisi di riscontro visivo** — le note costruite sulle tre immagini della fetta (la scansione del modulo del metal detector, la foto del pannello della confezionatrice, la foto del frammento col righello) portano `verifica: visiva`, e l'estrattore di testo congelato sulle immagini restituisce stringa vuota per costruzione. **Ogni immagine è stata letta a occhio** e i valori riportati corrispondono a ciò che si vede. È esattamente il caso previsto da §7.1 clausola 3.
- **5 avvisi «summary e title si sovrappongono per meno del 20%»** — su note il cui titolo è una domanda («Di che materiale è la guarnizione…») e il cui riassunto è la risposta: le parole non si ripetono perché il riassunto non parafrasa il titolo, che è ciò che si vuole.
- **1 avviso di lunghezza** su un riassunto al limite dei 250 caratteri.

**La storia dei passaggi.** Il primo giro aveva prodotto **31 errori**: 22 erano falsi
positivi di controlli troppo ingenui — corretti negli script — e 9 errori veri nelle note.
Dopo il giro del revisore ne sono rientrati altri 4, tutti miei: citazioni ricomposte
invece che riportate alla lettera, e un locator fuori grammatica.

## Collaudo della suite

Prima di usarla, la suite è stata collaudata su due note sintetiche in
`06_operativo\qa\_collaudo\` — una corretta, costruita su valori riscontrati nei grezzi
veri, e una con cinque difetti piantati apposta (fonte inventata, numero senza riscontro,
wikilink rotto, area fuori vocabolario, stato sbagliato). Esito: **5 difetti su 5 trovati,
0 falsi positivi sulla nota corretta**. Il collaudo è rieseguibile con
`python collaudo_suite.py` e ha già fatto il suo mestiere: al primo giro ha scoperto un
ramo invertito nel riconoscimento dei wikilink rotti.

## Strato di giudizio della provenance

Eseguito da un subagente a contesto pulito, che non ha ricevuto il canone e ha confrontato
ogni nota contro i propri grezzi. Esito: **26 note pulite su 33**, 6 «afferma oltre le
fonti» e 1 «fonte inutile». Tutti e sette i rilievi sono stati verificati e corretti.

## Revisione indipendente

Eseguita da un secondo subagente a contesto nuovo, **con il canone e la tabella alias alla
mano**, come prescrive §9.5 passo 3. Esito: **13 rilievi A, 5 B, 10 C**.

- Le **A** sono state tutte chiuse. Le più importanti: mancava la nota padrona della revisione del manuale HACCP (contraddizione registrata dal canone e da nessuna nota dichiarata); la data di apertura del reclamo era stata risolta scegliendo un vincitore che il canone non dà; la misura del frammento ribaltava l'arbitrato del canone; due conteggi erano sbagliati (righe del MOD-QA-07 e data di una non conformità); mancavano le schede delle persone nominate negli hub.
- Le **B** sono cinque divergenze reali che il canone non elencava: TMC e modo di consegna del lotto di farina, materiale della guarnizione, codice del kit valvola, ora di arrivo della segnalazione. Tutte hanno ora la loro nota-questione nel vault e **la loro riga nel canone**, in una sezione datata 16/08/2026 accanto a quella della Sessione 1. La sesta riga registra la terza misura del frammento.
- Le **C** sono dieci trappole riconosciute e non segnalate come errori: sono elencate nel decision log perché non tornino al lotto successivo.

**Il rilievo A che era rimasto aperto — le note di `code\` senza `fonti` — è stato chiuso al
gate** con l'emendamento E1: l'esenzione vale per la **nota-strumento** (prefisso `script-`
dentro `code\`), non per la cartella, e nel corpo di ciascuna è stato aggiunto il percorso
del sorgente nel repository. Nessun rilievo A resta aperto.

## Il giudizio di provenance, rieseguito su tutto

Alla chiusura lo strato di giudizio è stato **rieseguito su tutte le 46 note candidate** —
comprese le 8 che nel primo giro non erano mai state giudicate, perché nate dalle correzioni
del revisore. Esito: **42 pulite, 4 «afferma oltre le fonti», 0 fonti inutili**, tutti e
quattro i rilievi corretti.

⚠️ Il più importante dei quattro: una nota affermava una divergenza sui pezzi per cartone che
**nessuna sua fonte conteneva** — l'informazione veniva dal report del revisore, che aveva il
canone. **Era una fuga di canone dentro il vault**, la cosa che il guardrail 1 esiste per
impedire, ed è stata rimossa. È anche la ragione per cui la regola E9 — rigiudicare le note
nate dalle correzioni — vale la pena: quella nota era stata scritta *dopo* il primo giro di
giudizio, e senza il secondo giro sarebbe rimasta.

## Cosa resta

- **125 grezzi** non ancora canonizzati, che sono l'oggetto del resto delle Sessioni 4-5.
  ⚠️ *Errata del 19/08/2026: questa riga diceva 127. Era un errore di trascrizione, non di
  canonizzazione — il blocco dei conteggi qui sopra e la tabella del perimetro vault dello
  stesso file dicevano già 125.*
- Le **tre aree** del vocabolario chiuso ancora senza hub: risorse umane, sicurezza-ambiente,
  ricerca-sviluppo. Nasceranno con i lotti che le toccheranno; `amministrazione` è nata con
  il lotto 1B.
- La **nota di inventario dell'archivio** in `data\`, che dovrà tenere i conteggi per
  formato, i duplicati e i file privi di contenuto informativo: è la nota che soddisfa la
  copertura sui file muti, e senza di essa `_index-sources` non può dichiarare un numero.
- Due dati della **scheda prodotto** — pezzi per cartone e ITF-14 — che nella fetta non
  sono attestati da fonti leggibili con l'estrattore congelato: si scriveranno quando
  entrerà il documento che li porta.
- La **mappatura file × fatto** (`06_operativo\matrice_corpus_v1.csv`), che si compila lotto
  per lotto e si committa a ogni chiusura di lotto — non in blocco.
- Le righe della **tabella di tracciamento**, che vivono in `matrice_lotti_corpus_v1.md`
  e al gate finale sono la prova che nessun conflitto è stato dimenticato. ⚠️ Due coppie del
  seme iniziale — T21/T29 e T22/T30 — sono **duplicati**: la duplicazione è dichiarata sulle
  righe, non risolta cancellandone una.
  ⚠️ *Errata del 19/08/2026: questa riga diceva «41 righe», e le righe sono 54. Da qui in poi
  il numero non si legge più a occhio: lo produce `06_operativo\conta_tracciamento.py`, ed è
  l'ultimo numero del progetto che era ancora dichiarato senza script.*

<!-- TABELLA DI TRACCIAMENTO - generata da `06_operativo\conta_tracciamento.py`
     il 2026-08-19. Si incolla VERBATIM: il numero delle righe non si legge a occhio. -->

| Esito | Righe | Quali |
|---|---|---|
| riconciliata | **3** | T17, T22, T30 |
| aperta dichiarata | **23** | T1, T2, T3, T4, T18, T23, T24, T25, T26, T27, T28, T32, T35, T36, T37, T38, T42, T43, T44, T45, T46, T47, T48 |
| chiusa | **2** | T20, T33 |
| tracciata | **26** | T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T19, T21, T29, T31, T34, T39, T40, T41, T49, T50, T51, T52, T53, T54 |
| **totale righe** | **54** | da T1 a T54, nessuna mancante e nessuna duplicata |

## Il gate del lotto 2B-bis, 21/08/2026 — l'estensione di cantiere

**2B-bis approvato.** Il gate ha poi chiesto una manutenzione piena, e questa è la parte che ne
è uscita.

⚠️ **E48: l'estrazione di cantiere.** La QA e il pacchetto del giudizio leggono ora un testo che
**aggiunge marcati** i due strati che l'estrattore congelato non vede — `[FORMULA: …]` e
`[BARRATO: …]`. **L'estrattore di misura non è stato toccato**, e la separazione **si prova**:
il testo della via congelata è un **prefisso esatto** di quello di cantiere su tutti i 161
grezzi, zero violazioni. Lo strato vede **1.697 formule e 40 barrati in 24 file**, e le 1.697
combaciano cifra per cifra col censimento indipendente della mattina.

⚠️ **E49: la riga B è una nota senza cartella.** Ogni affermazione che entra nel canone porta lo
stesso riscontro che porterebbe in una nota, **valori contati compresi**. ⚠️ **Il gate ne ha
fornito subito due casi**: B3 e B4 portavano conclusioni scritte senza riaprire il file, e sono
state entrambe ribaltate dal ri-giudizio.

⚠️ **L'arbitrato del lotto 2A regge, e ne esce più preciso.** La scheda allergeni prescrive il
sanificante **solo dentro il lavaggio `L3`, obbligatorio in quattro circostanze**, e il log non
dichiara mai il tipo di lavaggio: **il tracciato è più severo di entrambi i documenti**, non
solo di `IO-05`.

**Trenta note riviste contro il file aperto come archivio, quattro corrette.** La più grave
dava per vigente una tolleranza **barrata a metà** su una pratica **sospesa**.

**Collaudo della suite da 22 a 24 difetti su 24**, più due collaudi nuovi a perimetro chiuso —
i due tassi e il CSV. Il dettaglio sta nella **parte seconda** di `rapporto_lotto_02b_bis.md`.

## Il lotto 2B-bis, chiuso il 21/08/2026 — gli allergeni

**Due grezzi**: la scheda con la matrice di cross contamination e il materiale della formazione
annuale agli operatori. **33 note nate**, 44 controllate, **0 errori e 25 avvisi** sul perimetro
di lotto alle 14:47:43.

⚠️ **Il criterio pre-registrato al gate di 2B si è avverato**: al terzo giro di giudizio, tre
dei cinque rilievi erano della specie universale, **su note nate dal lotto**. Ne è nata **E47**,
il primo emendamento del progetto nato da un criterio scritto in anticipo.

⚠️ **La revisione col canone ha trovato la seconda cecità dell'estrattore**: quattro passaggi
**barrati** nel `.docx`, invisibili nel testo estratto, di cui il vault ne aveva colto uno solo
— e solo perché un commento accanto usa la parola «cancellata». **Riga T96**, e l'estrattore
**non è stato toccato**.

⚠️ **E ha trovato un documento che dichiara un difetto che non ha**: l'avvertenza sul
disallineamento della matrice, che la nota aveva propagato senza contare le colonne. **Contate:
sedici campi su tutte e sette le referenze.** Riga T105, chiusa.

**Otto divergenze nuove nel canone**, di cui **sei fra la scheda e un documento che il vault
aveva già** — la diagnosi del revisore era che il lotto avesse canonizzato *dentro* i suoi due
file e non *contro* l'archivio, e i numeri la confermano. **Una riapre un arbitrato del canone**
(B3); **una è vera e non scrivibile** (B6), perché il suo grezzo non è in nessun lotto.

**I due tassi, dominio `allergeni`** (E46): riapertura **0,0 %** su 6, produzione **9,1 %** su
33. ⚠️ **Il tasso di produzione risale dopo due lotti sotto il 4 %**, e le tre note sono tutte
del sotto-dominio della formazione, dove la fonte che governa è il materiale d'aula.

**Il ri-giudizio dopo la revisione** ha prodotto 5 errori e 17 avvisi, tutti accolti. ⚠️ **Uno
era un numero che avevo contato io e che nessuna fonte enuncia** — il «sei fasi» del lavaggio,
passato attraverso il revisore, il canone, una nota e una riga di tracciamento. **Da lì la
specie nuova**, nominata e non emendata (E28), col criterio nel §11 del rapporto.

Il dettaglio sta in `rapporto_lotto_02b_bis.md`.

## Il lotto 2B, chiuso il 20-21/08/2026 — l'autocontrollo analitico

⚠️ **Il lotto sta a cavallo della mezzanotte, come 2A**: le note portano `data_nota:
2026-08-20`, la nota-sessione porta **2026-08-21** perché è stata scritta dopo, e in `qa\`
ci sono due cartelle datate. **Nessuna data è stata ritoccata.**

| | |
|---|---|
| Grezzi | **3 su 5** — il lotto si è spezzato in apertura (E28), gli allergeni vanno a **2B-bis** |
| Note nate | **27** di contenuto, dentro la capacità 25-35 di E31 |
| Note riaperte (E37, dominio `acqua`) | **5**, di cui **3 corrette** |
| Note toccate (E32) | **9** |
| Giri di giudizio | **3** — 8, 2 e 3 rilievi accolti. **Non converge**, e il rapporto **nomina la specie** invece di fare un quarto giro |
| Righe di tracciamento | **T72 chiusa**, T71 e T82 aperte dichiarate, T77 riconciliata, sei nuove tracciate. Totale **82** |
| Revisione col canone | ✅ **eseguita il 21/08/2026**, dopo che **E45** ha sciolto la contraddizione: **14 rilievi A, 5 B, 0 C**. I 14 A verificati sui grezzi e corretti; le 5 B nel canone in sezione datata; ri-giudizio delle note toccate, **11 rilievi accolti**, e QA di lotto di nuovo verde |

**Che cosa ha chiuso.** La conducibilità dell'acqua di rete — **486 µS/cm** — è entrata nel
vault, e il criterio del risciacquo CIP che 2A aveva dichiarato non verificabile è stato
applicato: **superato in 18 cicli su 28** se fa fede l'ultima lettura, in **24** se fa fede la
più alta. ⚠️ **È la prima riga di tracciamento del progetto chiusa da un lotto successivo con
un dato**, non con una decisione.

**Che cosa ha aperto.** Una positività a **Listeria del 24/02/2026**, gravità critica, che sta
nel registro delle non conformità e **non** in quello dei tamponi: chi guardasse il solo
`MOD-QA-19`, come farebbe un auditor, vedrebbe una positività nell'anno invece di due.
