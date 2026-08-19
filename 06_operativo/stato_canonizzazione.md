# Stato della canonizzazione — vault `aurora-cervello`

> **Cos'è** · Lo stato di oggi del vault: cosa è stato canonizzato, con quale esito, e
> cosa resta. Solo stato, mai una regola: le regole stanno in
> `01_metodo\metodo_03_canonizzazione.md`, le decisioni in `06_operativo\decision_log.md`.
> **Aggiornato al** · 19/08/2026, **apertura e primo giro del lotto R1** — la riconciliazione
> verticale, primo lotto di manutenzione del progetto. Nella stessa giornata: la sessione di
> manutenzione degli strumenti, E34 ed E35 in `metodo_03`, i numeri riportati da script.
> ⚠️ **R1 NON è chiuso**: mancano giudizio, revisione col canone e ri-giudizio.
> Lo stato della pipeline RAG sta in `06_operativo\stato_rag_produzione.md`, non qui; il
> piano dei lotti e la tabella di tracciamento delle questioni trasversali stanno in
> `06_operativo\matrice_lotti_corpus_v1.md`, non qui.

---

## Dove siamo

| | |
|---|---|
| Lotti chiusi | **4** — `l26130` (fetta pilota, S2), **`1A`** (Linea 1: turno, CCP, confezionatrice), **`1B`** (freddo ed energia) e **`1C`** (metrologia e gas tecnici) |
| Grezzi copiati nel vault | 160/160, verificati contro `manifest_corpus_v1.1.json`: zero scarti, zero estranei, zero sottocartelle |
| I conteggi del vault | nel blocco qui sotto, **incollato verbatim** da `conta_stato.py` |
| Suite QA | **verde sul perimetro di lotto**; sul vault tre controlli su quattro sono a zero errori |
| `llms.txt` | rigenerato dal frontmatter, allineato |
| Matrice dei lotti | 160/160 grezzi, zero scoperti, zero doppi (`verifica_matrice_lotti.py` verde). ⚠️ **I budget dei lotti 2-10 sono SUPERATI** e il piano non è più a 12 lotti: vale **E31**, la capacità di 25-35 note per lotto, e i grezzi si decidono in apertura. **Stima: circa 28-30 lotti**, scritta anche nella scaletta perché cambia il calendario di S4-S5. Ridisegnato in dettaglio **solo il tema 2** (2A · 2B · 2C) |
| **PROSSIMO ATTO** | ⚠️ **FINIRE R1, prima di qualunque altra cosa.** Il lotto è aperto e il primo giro di correzioni è chiuso — 71 note guardate, 41 corrette, QA di lotto verde — ma **il lotto non è chiuso**: mancano lo strato di giudizio, la revisione col canone e il ri-giudizio, che `metodo_03` §9.5 affida a una **sessione diversa** da quella che ha scritto le correzioni. §5 del prompt dei lotti: la sessione successiva **prima** finisce il lotto. Solo dopo: il tema 2 |

⚠️ **Errata del 19/08/2026 sui numeri del lotto 1A.** Questo stato dichiarava «105 note, di
cui 11 `_index` e 6 note-strumento: 88 di contenuto». `qa_all.py` a chiusura di 1A contava
**106** note: il 105 escludeva `_index-sources` ma sottraeva ugualmente tutti e undici gli
`_index`. Il numero corretto è **89 note di contenuto**. La correzione resta visibile, come
prescrive la regola del gate 1A.

## I conteggi, da script

<!-- CONTEGGI DEL VAULT — generati da `06_operativo\qa\conta_stato.py` il 2026-08-19.
     Si incollano VERBATIM: non si ricompongono a mano, non si riscrivono in prosa. -->

| Grandezza | Valore |
|---|---|
| Note nel vault | **176** |
| di cui `_index` | 11 |
| di cui note-strumento del progetto | 6 |
| di cui note di diario (`sessione`, `daily`) | 4 |
| **di cui note di contenuto** | **155** |
| Note per cartella | areas 94 · entities 22 · data 22 · projects 8 · docs 8 · code 7 · workspace 7 · concepts 5 · self 1 · outputs 1 · sources 1 |
| Note per `type` | atomica 94 · conflitto 33 · entita 18 · hub 12 · index 11 · concetto 4 · sessione 4 |
| Questioni aperte (`type: conflitto`) | 33 |
| Grezzi in `sources\` | 160 |
| Grezzi citati da almeno una nota | **35** |
| Grezzi restanti | **125** |

⚠️ **Questo blocco non si riscrive a mano.** Nasce al gate del lotto 1B da due sviste di
conteggio in due lotti — 46 contro 32 nel rapporto 1A, 105 e 88 in questo stato quando
`qa_all.py` contava 106 e 89 — e nessuna delle due era un errore di canonizzazione: erano
sottrazioni fatte a mano su numeri veri. Da qui in poi lo stato e i rapporti **incollano**,
non ricompongono.

## Il lotto R1 — APERTO il 19/08/2026, primo giro chiuso, lotto NON chiuso

**Perimetro:** **0 grezzi, 71 note.** È il primo **lotto di manutenzione** del progetto (E35):
non canonizza grezzi nuovi, ripara note già scritte. L'elenco dei grezzi
`06_operativo\qa\lotti\r1_riconciliazione_verticale.txt` porta `# MANUTENZIONE` e non ha righe
utili; il perimetro vero è l'elenco delle note accanto, **generato da
`06_operativo\candidate_r1.py`** e mai a memoria.

| | |
|---|---|
| Note guardate | **71** |
| Note corrette | **41** |
| **Tasso di difetto** | **57,7 %** *(calcolato: 41 su 71)* |
| di cui affermavano il falso | **7** — contro 34 semplicemente incomplete |
| Note nuove | **2** — `doc-gestione-deviazioni-haccp` e `questione-periodicita-taratura-canali-datalogger-ccp2` |
| Note toccate in più (E32) | **6**, dichiarate mentre le si toccava |
| QA di lotto | **0 ERRORI, 45 AVVISI**, motivati nel rapporto §5 |
| Giri di giudizio | ⚠️ **0 — da fare** |
| Righe di tracciamento aperte | **10**, da T55 a T64 |

**Cosa ha trovato.** Che più della metà delle note che parlano di un punto critico, di una
taratura, di una frequenza, di un limite o di una responsabilità di processo **non aveva sotto
mano il documento che quella cosa la prescrive**. Sette di quelle note non erano soltanto
incomplete: **affermavano il falso** — la più grave legava il perimetro del prodotto da
segregare alla *durata* della deviazione, mentre il manuale lo lega **all'ultimo controllo
conforme**.

**Lo strumento di E29 è nato qui**: `06_operativo\fonti_prescrittive_corpus_v1.md`, **36 fonti
prescrittive** del corpus di cui **8 citabili** oggi e **28 da tracciare**, perché i loro grezzi
stanno in lotti non ancora canonizzati. Quelle 28 non si citano e non si usano: hanno una riga
in matrice con l'obbligo esplicito per il lotto che le porterà.

⚠️ **ESATTAMENTE COSA MANCA, perché la sessione dopo lo sappia senza cercarlo:**

1. strato di giudizio con `PROMPT_GIUDIZIO` v2, subagente a contesto pulito, sulle note nuove e
   modificate. **Il pacchetto è già generato dopo le correzioni** (E33), in
   `06_operativo\qa\2026-08-19_r1_riconciliazione_verticale\pacchetto_giudizio_provenance.txt`;
2. revisione col canone, **sessione diversa**, con un campione delle note nate dalle correzioni;
3. ri-giudizio (E9) con la regola d'arresto di E26;
4. re-QA, `llms.txt` rigenerato, `_index` e hub riverificati;
5. `# CHIUSO <data>` in testa all'elenco del lotto — **oggi assente, ed è voluto**: il lotto non
   è chiuso e `verifica_matrice_lotti.py` non deve credere il contrario;
6. il rapporto `06_operativo\rapporto_lotto_r1.md` esiste già e va completato ai §9 e §11.

Il rapporto porta la domanda per il coordinatore: **57,7 % di difetto basta a dire che il
ripasso va rifatto a fine corsa, o E29 in vigore basta a impedire che si riformi?**

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

| Controllo | Errori su tutto il vault |
|---|---|
| `qa_frontmatter` | **0** |
| `qa_link_integrity` | **0** |
| `qa_provenance` | **0** |
| `qa_copertura` | 128 — **125 grezzi non ancora canonizzati e 3 aree senza hub** |

Tutti gli errori residui del vault sono la sua **incompletezza**: nessuno è un difetto delle
note che esistono.

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
