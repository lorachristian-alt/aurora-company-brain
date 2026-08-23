# Stato della canonizzazione — vault `aurora-cervello`

> **Cos'è** · Lo stato di oggi del vault: cosa è stato canonizzato, con quale esito, e
> cosa resta. Solo stato, mai una regola: le regole stanno in
> `01_metodo\metodo_03_canonizzazione.md`, le decisioni in `06_operativo\decision_log.md`.
> **Aggiornato al** · **23/08/2026, chiusura del LOTTO 3B** — la politica per la qualità e lo
> scadenzario della formazione. **L'area `risorse-umane` si apre**, ed è l'ottava delle dieci del
> vocabolario: restano scoperte `sicurezza-ambiente` e `ricerca-sviluppo`. Prima, nella stessa
> giornata, il **GATE del lotto 3C**, che lo ha **APPROVATO** e ha prodotto **E56, E57 ed E58**.
> ⚠️ **Due controlli bacati riparati in un giorno solo, e nessuno dei due l'ha trovato uno
> script**: la lista dei lotti canonizzati scritta a mano dentro `verifica_dominio.py`, e
> `qa_link_integrity.py` che cercava i wikilink rotti **solo nel corpo** — col vault che ne
> portava **due** e la QA a **zero errori**. ⚠️ **E `E56` ha colto il proprio autore**: il primo
> dominio dichiarato sotto la regola della coppia è nato **troppo largo**, nello stesso verso di
> 3C. Tutti i numeri qui dentro sono riportati da script, **e da E44 ognuno porta l'ora della
> propria misura**.
> Lo stato della pipeline RAG sta in `06_operativo\stato_rag_produzione.md`, non qui; il
> piano dei lotti e la tabella di tracciamento delle questioni trasversali stanno in
> `06_operativo\matrice_lotti_corpus_v1.md`, non qui.

---

## Dove siamo

| | |
|---|---|
| Lotti chiusi | **11 in tutto: 10 di canonizzazione** — `l26130` (fetta pilota, S2), **`1A`**, **`1B`**, **`1C`**, **`2A`**, **`2B`**, **`2B-bis`**, **`3A`**, **`3C`** e **`3B`** (la politica e la formazione) — **più `R1`**, il primo e finora unico **lotto di manutenzione** (E35). ⚠️ **R1 vale un lotto nel ritmo ma NON entra nella serie della capacità** (E38). ⚠️ **Il conto è da script**, sui marcatori `# CHIUSO` degli elenchi (dieci file) più il pilota, che elenco non ne ha perché è anteriore alla matrice |
| Grezzi copiati nel vault | 160/160, verificati contro `manifest_corpus_v1.1.json`: zero scarti, zero estranei, zero sottocartelle |
| I conteggi del vault | nel blocco qui sotto, **incollato verbatim** da `conta_stato.py` |
| Suite QA | **verde sul perimetro di lotto**; ⚠️ **dal gate del 21/08 la provenance legge l'ESTRAZIONE DI CANTIERE** (E48), che aggiunge marcati formule e barrato — l'estrattore di misura resta byte-identico e `estrazione_cantiere.py --prova` lo dimostra su tutti i 161 grezzi; sul vault tre controlli su quattro sono a zero errori. ⚠️ Dal gate di 2A la QA ha **due controlli nuovi**: l'artefatto di ricerca che E43 impone a chi dichiara un'assenza, e **l'omogeneità dei fine riga** — il primo controllo del progetto che non guarda il contenuto di una nota ma il suo **supporto** |
| `llms.txt` | rigenerato dal frontmatter, allineato |
| Matrice dei lotti | 160/160 grezzi, zero scoperti, zero doppi (`verifica_matrice_lotti.py` verde). ⚠️ **I budget dei lotti 2-10 sono SUPERATI** e il piano non è più a 12 lotti: vale **E31**, la capacità di 25-35 note per lotto, e i grezzi si decidono in apertura. **Stima: circa 28-30 lotti**, scritta anche nella scaletta perché cambia il calendario di S4-S5. Ridisegnato in dettaglio **solo il tema 2** (2A · 2B · 2C) |
| **PROSSIMO ATTO** | **Il gate del lotto 3B**, e poi **`3D`** *(i reclami)* e **`3E`** *(crisi e ispezioni)*, che chiudono il tema 3. ⚠️ **Il gate ha sette cose da decidere**, e la prima è un candidato emendamento: **la correzione è una scrittura, e nessuno la giudica come tale**. ⚠️ **E `3D` porta un obbligo esplicito**: `PRO-QA-08`, che la politica nomina nell'impegno 6 e di cui nessuna nota può ancora dire nulla (**T146**) |

⚠️ **Errata del 19/08/2026 sui numeri del lotto 1A.** Questo stato dichiarava «105 note, di
cui 11 `_index` e 6 note-strumento: 88 di contenuto». `qa_all.py` a chiusura di 1A contava
**106** note: il 105 escludeva `_index-sources` ma sottraeva ugualmente tutti e undici gli
`_index`. Il numero corretto è **89 note di contenuto**. La correzione resta visibile, come
prescrive la regola del gate 1A.

## I conteggi, da script

<!-- CONTEGGI DEL VAULT — generati da `06_operativo\qa\conta_stato.py` il 2026-08-23,
     alle 18:42, dopo la nota-sessione (E34) e dopo l'ultima scrittura (E44).
     Si incollano VERBATIM: non si ricompongono a mano, non si riscrivono in prosa. -->

| Grandezza | Valore |
|---|---|
| Note nel vault | **386** |
| di cui `_index` | 11 |
| di cui note-strumento del progetto | 15 |
| di cui note di diario (`sessione`, `daily`) | 10 |
| **di cui note di contenuto** | **350** |
| Note per cartella | areas 229 · data 41 · docs 38 · entities 31 · code 16 · workspace 13 · projects 8 · concepts 6 · self 2 · outputs 1 · sources 1 |
| Note per `type` | atomica 270 · conflitto 53 · entita 23 · hub 14 · index 11 · sessione 10 · concetto 5 |
| Questioni aperte (`type: conflitto`) | 53 |
| Grezzi in `sources\` | 160 |
| Grezzi citati da almeno una nota | **51** |
| Grezzi restanti | **109** |

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

## Il lotto 3B, chiuso il 23/08/2026 — la politica e la formazione

**Perimetro:** 2 grezzi — la **Politica per la qualità `DOC-QA-01` rev. 8** e lo **scadenzario
della formazione** estratto il 18/05/2026 — più **8 note riaperte** da E37 e **23 nate**.

| | |
|---|---|
| Capacità attesa | 25-35 note di contenuto (E31) |
| Prodotte | **23** — **sotto la fascia**, e si dichiara: due grezzi, non tre o quattro |
| QA di lotto | **0 ERRORI, 43 avvisi** — misura delle 18:39 |
| Giri di giudizio | **tre**: 18, 10 e 12 rilievi — ⚠️ **il terzo non è andato meglio del secondo** |
| Revisione col canone | **2 A · 13 B · 5 C** |
| Giudizio dedicato (E58) | **tre giri**: 2, 2 e **0** rilievi — chiuso sul giro pulito |
| Tassi (E41/E46) | riapertura **12,5 %** · produzione **36,4 %** su 22, dominio `formazione` |

### ⚠️ L'area `risorse-umane` nasce, e nasce piena

Fino a oggi il vocabolario chiuso portava `risorse-umane` **senza che nessuna nota lo usasse**.
L'hub apre con **tredici note**, non con una cartella vuota per comodità di archiviazione.
⚠️ **E la formazione non è solo di quest'area**: il manuale HACCP la porta come prerequisito
`PRP-04`, quindi le note guardano anche a `area-qualita`.

### ⚠️ Due controlli bacati, e nessuno dei due l'ha trovato uno script

| Controllo | Il buco | Chi l'ha visto |
|---|---|---|
| `verifica_dominio.py` | l'insieme dei lotti canonizzati era **una lista di nomi scritta a mano**: portava un nome morto dal 20/08 e non portava tre lotti chiusi. **Dichiarava NON CITABILE il certificato BRCGS il giorno dopo che 3C lo aveva canonizzato** | **un numero**, in apertura |
| `qa_link_integrity.py` | cercava i wikilink rotti chiamando `Nota.wikilink()`, che legge **il solo CORPO**: `related` restava fuori, e **il vault ne portava due con la QA a zero errori** — uno da un lotto precedente | **la revisione col canone** |

⚠️ **Entrambi sono COPIE o PERIMETRI, non logiche sbagliate**, ed entrambi per §4 sono guasti e
non candidati: riparati subito, ciascuno col suo difetto piantato. **I collaudi passano da
cinque a sette.**

### ⚠️ E56 al primo impiego ha colto il proprio autore

Il dominio `formazione` — **il primo dichiarato sotto la regola della coppia** — è nato **troppo
largo**, nello stesso verso di 3C. **La prova è per espressione, non per numero**: `\bformazion`
da sola pescava **tutte e quattordici** le scoperte, perché riconosce **la parola** e con essa la
struttura del registro, chi lo estrae e un indicatore.

**Stretta la coppia: 63,6 % → 36,4 %.** ⚠️ **E ci si è fermati lì, dopo UNA stretta**:
continuare a restringere a numero visto sarebbe il trucco che E41 vieta, spostato di un piano.
**T148.**

### ⚠️ Il pattern che ha chiuso il ciclo: la correzione è una scrittura

Dei dodici rilievi del terzo giro, **almeno sette cadono su frasi che al secondo non c'erano:
le ha scritte la correzione**. Due forme — l'intestazione rimasta indietro *(nota: E30, E51)* e
**la frase scritta correggendo che afferma essa stessa oltre le fonti** *(nuova)*.

⚠️ **Il caso peggiore**: «la foto decisiva non compare in nessuno dei due elenchi» era la
correzione di una frase vaga, **e il §6 della fonte la elenca**. La correzione ha reso **falsa**
una frase che prima era soltanto imprecisa. **Candidato emendamento al gate.**

### La revisione col canone, e la diagnosi che ribalta la domanda

**Tredici divergenze nuove nel canone**, otto scrivibili. Le tre che pesano: il **97,32 %** come
«Valore 2025» in un documento emesso il 12/01 quando l'audit è del 17-18/02; «attestati HACCP in
scadenza: **n. 5**» dichiarato alla direzione contro i **dieci** del registro — **e da quel
cinque discende l'azione `A9`**; i reclami per milione, dove la politica rende scrivibile una
gamba che 3A dava per bloccata.

⚠️ **Non c'è sovra-atomizzazione: c'è il contrario.** Un fatto con tre padroni, e **cinque righe
del registro senza nessuna nota** — fra cui un'**addetta alla squadra di emergenza col primo
soccorso scaduto da tre mesi**, con l'unico «SUBITO» di tutto il file. ⚠️ **E la diagnosi vera**:
*il lotto ha letto benissimo i due grezzi come DOCUMENTI, e quasi mai uno contro il vault* —
**sette delle otto divergenze scrivibili nascono dall'accostamento col verbale di riesame**.

## Il gate del lotto 3C, 23/08/2026 — tre emendamenti, e il giudizio che ha trovato di piu'

**Il lotto 3C e' APPROVATO.** Il gate ha prodotto **E56, E57 ed E58**, ha esercitato il primo
criterio pre-registrato che si chiude senza discussione, e ha corretto una propria ratifica.

| Emendamento | Che cosa dice | Da dove viene |
|---|---|---|
| **E56** | la dichiarazione del dominio e' una **coppia espressioni-fonti che si giustificano a vicenda**; nello strumento le citazioni hanno **due classi di forza** che non si sommano | **due consuntivi opposti**: 2B-bis troppo stretto (9,1 %), 3C troppo largo (38,7 %) |
| **E57** | il **discrimine e' il soggetto**: superlativo su un documento citato regge, superlativo sull'archivio no | il pattern che E26 impone di **nominare** al terzo giro |
| **E58** | **E26 ferma il ciclo, non la prima esposizione**: ogni nota vede il giudizio almeno una volta, e le note dell'ultimo giro ne ricevono uno **dedicato** | un debito che l'esecutore aveva **dichiarato** invece di lasciar passare (T141) |

⚠️ **Il 38,7 % NON e' stato rimisurato, ed e' una scelta.** La dichiarazione era sbagliata e la
regola che la corregge esiste da oggi, ma **la serie fotografa le dichiarazioni come sono state
fatte**: rimisurare darebbe punti tutti prodotti con la regola dell'ultimo gate, cioe' una serie
che non puo' piu' mostrare il proprio miglioramento. **Il numero resta con la riserva accanto**
(E46). **T129 chiusa.**

### E58 al primo impiego: due note su due difettose

Le due note di **T141** — `fatto-due-nc-interne-sul-proprio-ritardo` e
`questione-vendor-rating-2025-c-e-o-non-c-e` — avevano passato QA e controllo delle citazioni
**senza mai vedere un giudice**. Giudicate a contesto pulito, con pacchetto generato solo per
loro (E33): **`afferma_oltre` entrambe.**

⚠️ **E' il dato che giustifica la regola meglio di qualsiasi argomento**: se il debito fosse
stato formale, il giudizio sarebbe tornato pulito. ⚠️ **E una delle due chiudeva con «l'archivio
non scioglie»**, cioe' con la classe di E57, in una nota nata due giorni prima che E57
esistesse. **Al secondo giro dedicato entrambe tornano `pulita`.**

### ⚠️ Il giudizio ha trovato piu' di quello che cercava, e corregge una ratifica di questo gate

`fatto-evidenze-audit-oltre-termine` era entrata nel perimetro **solo** per una correzione
soppressiva: portava la stessa fonte **due volte** in `fonti`. Giudicata, e' tornata
`afferma_oltre`, e il rilievo era grosso.

| Che cosa il vault diceva | Che cosa dicono le fonti |
|---|---|
| «Aurora conta sedici in **due documenti**, il verbale e il registro» | ⚠️ **il verbale non porta ne' «sedici» ne' «16»**: fissa la scadenza al 17/03, che ne e' solo la premessa |
| «l'ente conta **quindici**» | ⚠️ **il quindici non lo scrive nessuno**: e' aritmetica del vault fra il 18/03 e il 02/04 |
| «nessuna fonte dell'ente conta i giorni» *(la mia prima correzione)* | ⚠️ **falso a sua volta**: il rapporto d'audit §6 scrive «oltre il termine di sollecito del 01/04/2026 **(un giorno)**» |

⚠️ **La sostanza regge** — termini diversi, conti diversi — **ma «due contatori veri, di due
titolari diversi» era la lettura sbagliata**, ed era la formula con cui il gate stesso aveva
ratificato T126. **La riga e' alla terza stesura, e tutte e tre sono cadute sullo stesso punto:
un conteggio attribuito a una fonte che non lo enuncia** — la classe di E49 e di E50.

⚠️ **E la terza riga della tabella e' la piu' istruttiva**: la correzione scritta per chiudere
un'affermazione eccedente ne conteneva **un'altra**, con la stessa forma. **E' la firma di E47**,
e il giudizio dedicato l'ha presa al giro dopo. Da qui la regola d'arresto aggiunta a **E58**:
il giudizio dedicato eredita l'arresto di E26, altrimenti gira all'infinito.

### Il censimento di E57 (T142), e perche' e' stato spezzato in due

`06_operativo\censimento_superlativi.py`, **misura delle 15:22:56 del 23/08/2026** su **325 note
esaminate** (esclusi `_index`, `code\`, `workspace\`, `sources\`):

| Classe | Note | Occorrenze | Chi la governa |
|---|---|---|---|
| **`superlativo`** — affermativo sull'archivio | **9** | **10** | **E57**, e sono le sole scoperte |
| **`assenza`** — esistenziale negativo | **31** | **32** | **E3 ed E43**, con la ricerca e il suo artefatto |

⚠️ **Il primo giro dava 42 note e 47 occorrenze**, e quel numero mescolava i due regimi:
pubblicarlo avrebbe ripetuto in piccolo l'errore del 38,7 %. ⚠️ **Il numero e' un LIMITE
INFERIORE**: lo script riconosce una forma, il soggetto lo decide chi legge. ⚠️ **Le nove note
non si riparano ora**: si riparano nel lotto che le tocca o nella rete finale, come il debito di
E43.

### I numeri di chiusura del gate (E44), tutti dopo l'ultima scrittura

| Misura | Valore | Ora |
|---|---|---|
| **QA, perimetro del giudizio dedicato** | **0 ERRORI, 17 avvisi** — esito **GIALLO** | 15:53 |
| **QA, perimetro vault** | **114 ERRORI, 258 avvisi** | 15:53 |
| di cui grezzi non ancora canonizzati | **111** | |
| di cui aree senza hub | **3** | |
| di cui **rilievi di merito** | **0** | |
| **Emendamenti** | registro e manuale **concordano a 58** | 15:54 |
| **Matrice** | completa e disgiunta: 160 grezzi, **25 elenchi** | 15:54 |
| **Tracciamento** | **142 righe** — 7 riconciliate · 63 aperte dichiarate · 15 chiuse · 57 tracciate | 15:54 |
| **Collaudi** | **5 su 5**: suite 18+9, due tassi 5, CSV 7, doppie padrone 3, locator eml 3 | 15:47 |
| **Vault** | **362 note**, di cui **327 di contenuto** | 15:54 |

⚠️ **Il vault resta a 114 errori come alla chiusura di 3C, e nessuno e' di merito**: il gate ha
corretto tre note senza introdurre regressioni. **L'avviso in piu' — 258 contro 257 — e'
`fatto-due-nc-interne-sul-proprio-ritardo`** che entra nella fascia 301-350 parole.

⚠️ **Nessuna nota-sessione per questo gate, ed e' una scelta dichiarata**: la nota di diario e'
un gesto di chiusura di LOTTO (E34), e i gate precedenti non ne hanno mai scritta una.
Inventarne una qui sposterebbe il conteggio delle note di diario senza che un lotto sia stato
canonizzato. Il blocco di `conta_stato.py` resta comunque **l'ultimo numero prodotto prima del
commit**, che e' cio' che E34 protegge.

### Le tre ratifiche che valgono da precedente

✅ **IL GRADE AA E' SOTTO AVVERTIMENTO, ed e' canonizzato.** L'ente ha registrato il ritardo a
sistema e ha scritto che alla reiterazione scattano la segnalazione ai fini del grading BRCGS —
riduzione a grade A — e la valutazione IFS. ⚠️ **La nota e' linkata a quella che riporta il
«obiettivo primario» del verbale**, ed e' esattamente il tipo di confronto che la misura
«dopo» esiste per mostrare: un fatto che sta in due documenti diversi e che nessuna ricerca per
parole chiave mette insieme.

✅ **DUE RIGHE DALLO STRUMENTO DI E53, e valgono oltre il caso.** Il primo `verifica_dominio.py`
chiudeva la sigla con ``, e fra la `I` di `CPI_certificato_…` e l'underscore **non c'e' confine
di parola**: ogni sigla del corpus veniva scartata **in silenzio**. A tradirlo e' stato **un
numero — 28 fonti su 36 «nominate» — non una rilettura del codice.**

> **Un elenco che dice quasi sempre di si' non e' una verifica.**
> **Uno script che tace non e' uno script che assolve.**

⚠️ **Le due righe si sono riesercitate lo stesso giorno del gate**, sul censimento di E57: il
primo giro dava 42 note su 325, e il numero era plausibile abbastanza da essere creduto. Guardare
le frasi ha mostrato che mescolava due regimi.

✅ **IL GRAFO HA LAVORATO, e va detto perche' e' la prima volta che si vede.** Il certificato
BRCGS era stato scritto in `docs\`; **l'errore l'ha trovato l'`_index` della cartella**, che porta
da sempre la riga «gli attestati che Aurora riceve da terzi stanno in `self\`» — letta al momento
di aggiornare l'indice, non un minuto prima. **Non l'ha trovato chi scriveva.**
⚠️ **E `self\` si popola dopo quattro mesi di vuoto**: e' la prima nota che descriva **che cosa
Aurora e'**, invece di che cosa ha fatto o di che cosa prescrive.

### Il criterio pre-registrato sul gruppo post-revisione: chiuso

✅ **Non ha scattato** — gruppo **0,0 %**, ciclo **3,9 %** — e **E54 e' bastato**. E' la prima
volta che un criterio di questo progetto si esercita e si chiude senza discussione.
⚠️ **Ma ha guardato nel posto sbagliato**: il difetto non stava nel gruppo, stava nelle **due
note nate DOPO il gruppo**, che il criterio non guardava perche' guardava un tasso. La risposta
strutturale e' **E58**, che non guarda tassi.

## Il lotto 3C, chiuso il 22/08/2026 — certificazione e audit

**Il primo pacchetto dell'archivio scritto da qualcuno che non è Aurora**: il certificato
BRCGS, il rapporto d'audit CSQA, la conferma d'incarico del rinnovo e una catena di quattro
mail. **Trentotto note nuove, QA verde, tre giri di giudizio.**

⚠️ **Il fatto che il vault non sapeva: il grade AA è sotto avvertimento.** L'ente ha registrato
il ritardo a sistema e scritto che alla prossima reiterazione il grade scende ad **A** — non
per un difetto tecnico, **per il solo ritardo di trasmissione** — mentre la direzione chiama
quelle certificazioni «obiettivo primario».

**E53 al primo impiego**: dominio verificato da script in apertura, sette fonti prescrittive
citate per sigla dentro i grezzi. **E55**: la grammatica dei locator non sapeva indirizzare un
`.eml` a **catena**, e questo ne porta quattro messaggi.

⚠️ **`self\` si apre con questo lotto**, dopo quattro mesi di vuoto: il certificato stava in
`docs\`, e `metodo_03` §5 aveva un esempio svolto **su quel file esatto** che lo manda in
`self\`. **L'errore l'ha trovato l'indice della cartella, non chi scriveva.**

⚠️ **La classe d'errore nominata al secondo giro e cercata al terzo: il superlativo
sull'archivio.** Quattordici verificati, **dieci confermati** — tutti quelli il cui soggetto è
un documento citato. **Il discrimine è il soggetto, non la forma.**

## Il gate del lotto 3A, 22/08/2026 — tre emendamenti e il falso positivo chiuso

**3A approvato**, ed è insieme **il lotto più difettoso del progetto e quello che ha prodotto più
regole**: cinque emendamenti in due giorni, due da criteri pre-registrati e tre dal proprio gate.

⚠️ **Il miglior singolo ritrovamento del progetto per S7 è la lettura strutturale del cruscotto**:
**il verso di ogni confronto vive solo dentro la formula** — chi legge il foglio non può sapere se
un 64 % contro un target di 70 sia un successo o un fallimento.

⚠️ **E l'errore di apertura era del coordinatore, che lo dichiara**: l'esenzione «E37 non scatta su
3A» stava nel prompt del gate precedente, ed è **il terzo caso in tre gate** in cui un'affermazione
del coordinatore era sbagliata nel merito — **il primo in cui l'esecutore non poteva
contraddirla**, perché un'esenzione non si presenta come un ordine da verificare. Da qui **E53**:
il dominio si verifica **da script**.

**E52** ratifica lo sforamento e chiude T117 · **E53** il dominio da script · **E54** nessuna nota
cita un documento non aperto. Registro a **54**.

⚠️ **Il falso positivo delle doppie padrone è chiuso**, dopo essere stato rosso dal gate di 2A:
tutte e quattro le coppie avevano **zero fonti in comune**, quella originaria compresa. Il fix
chiede **fonte condivisa** e **valori identificanti**, con collaudo nei due versi. **Vault da 122 a
118 errori: 115 grezzi + 3 hub, zero di merito.**

## Il lotto 3A, chiuso il 22/08/2026 — il riesame della direzione

**Due grezzi**, il verbale di riesame del 12/03 e il cruscotto degli indicatori. **42 note nate**,
54 controllate, **0 errori e 28 avvisi** sul perimetro di lotto alle 01:38:50.

⚠️ **Primo impiego dell'estrazione di cantiere su dati veri, e il ritrovamento non è un numero
mancante**: delle 65 formule del cruscotto, quelle della colonna «Stato» contengono **il verso di
ogni confronto** — se il target sia un tetto o un pavimento la tabella non lo dice, lo dice la
formula, e cambia riga per riga.

⚠️ **Due emendamenti da due criteri scritti in anticipo, verificati nello stesso giro**: **E50**
*(un numero che la fonte non enuncia è derivato anche quando si ottiene contando)* e **E51**
*(un'affermazione non può essere smentita dalla nota che la contiene)*. Il registro passa a **51**.

⚠️ **La diagnosi del revisore, che il lotto si porta dietro**: ha letto i due grezzi come
documenti, **quasi mai uno contro l'altro e mai contro il vault**. Le tre omissioni più costose
erano in casa — il costo della non qualità con **due totali diversi nello stesso file**, lo stesso
indicatore che vale 6.800 in un grezzo e 2.400 nell'altro, cinque reclami contro tre nella stessa
finestra.

⚠️ **E la più grave era stata esclusa in apertura per una decisione scritta**: «E37 non scatta su
questo lotto». L'argomento era corretto — il verbale delibera e non prescrive — **ma il verbale
cita un criterio prescrittivo e lo cambia**, e il mock recall risulta dentro il limite per due
fonti e fuori per il riesame.

**Quindici divergenze nuove nel canone**, di cui **sette non scrivibili**: stanno dietro al
rapporto d'audit, che nessun lotto ha aperto. Il dettaglio in `rapporto_lotto_03a.md`.

## Il gate del tema 3, 21/08/2026 — ratifiche e adempimenti minori

**Ripacchettamento approvato**, e **due contraddizioni al prompt ratificate entrambe**.

⚠️ **Lo strato del barrato ha impedito il suo primo errore PRIMA di essere usato in un lotto.**
Aprendo il tema 3 per contare i fatti, ha mostrato che **il nono impegno della politica per la
qualità è barrato** — «perseguire la crescita del fatturato quale obiettivo primario
dell'organizzazione» — dentro il documento prescrittivo di vertice del tema, che dichiara la
priorità della sicurezza alimentare. **Nel testo estratto è indistinguibile dagli altri otto.**
Righe **T107** e **T108**.

⚠️ **Due gate consecutivi senza emendamenti al modo di scrivere le note.** Il registro resta a
**E49**: quello del lotto 2B-bis ne aveva prodotti due, questo nessuno. Gli adempimenti sono
stati tutti sugli **strumenti** e sui **registri**.

**Adempimenti**: l'etichetta «161 grezzi» corretta in **160** *(erano i file di `sources\`,
`_index` compreso)*, con lo script che ora esclude i `.md` e **dichiara il passaggio nel
report**; la contabilità del collaudo che dichiara la propria composizione — **18 difetti
piantati e 9 controlli di non-scatto, che non si sommano**; il criterio della terza specie
scritto **prima** dell'esperimento; l'errata datata nel rapporto 2B-bis sullo strumento dei due
tassi; e la riga **§4.44** — *un ordine di gate che discende da una riga di registro eredita la
provenienza di quella riga*.

## Il gate del lotto 2B-bis, 21/08/2026 — l'estensione di cantiere

**2B-bis approvato.** Il gate ha poi chiesto una manutenzione piena, e questa è la parte che ne
è uscita.

⚠️ **E48: l'estrazione di cantiere.** La QA e il pacchetto del giudizio leggono ora un testo che
**aggiunge marcati** i due strati che l'estrattore congelato non vede — `[FORMULA: …]` e
`[BARRATO: …]`. **L'estrattore di misura non è stato toccato**, e la separazione **si prova**:
il testo della via congelata è un **prefisso esatto** di quello di cantiere su tutti i 160
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
