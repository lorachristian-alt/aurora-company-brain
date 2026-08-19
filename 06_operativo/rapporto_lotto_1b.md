# Rapporto del lotto 1B — freddo ed energia: cella CF-02, tunnel TS-01, consumi e fattura

> **Cos'è** · Il rapporto di chiusura del secondo lotto della canonizzazione integrale, da
> portare al titolare per l'approvazione (metodo_03 §9.5, passo 7).
> **Quando si usa** · Una volta, alla chiusura di questo lotto. Poi resta come storia.
> **Cosa non contiene** · Nessuna regola: le regole stanno in `metodo_03`, il piano in
> `matrice_lotti_corpus_v1.md`, lo stato in `stato_canonizzazione.md`.

---

## 1. Il lotto, in una tabella

| | |
|---|---|
| Grezzi del lotto | **4** (ricontati da `inventario_grezzi.py`: 4 righe, 4 nomi distinti, 0 mancanti, 0 già coperti, 0 doppi) |
| Budget dichiarato | **22-30** note di contenuto |
| Note di contenuto prodotte | **38** — **sforato di 8**, e il perché sta al §4 |
| Note di diario | 1 (`sessione-s4-lotto-1b`) |
| Note esistenti estese | **8**: tre hub d'area (`area-manutenzione`, `area-produzione`, `area-qualita`) e cinque `_index` (`areas`, `data`, `docs`, `entities`, `workspace`) |
| Note nel vault, prima → dopo | **106 → 145** (contate da `qa_all.py`) |
| Densità del lotto | **9,5 note di contenuto per grezzo**, contro 6,0 di 1A e 2,1 del pilota |
| QA di lotto | **0 ERRORI, 17 AVVISI** — verde, dopo tre giri di correzione |
| Versione del prompt di giudizio | **v2**, la prima applicazione: il lotto 1A era stato giudicato con la v1 |

### Le 38 note di contenuto, per cartella

| Cartella | Note nuove | Cosa sono |
|---|---|---|
| `areas\` | 23 | la storia della cella CF-02, gli obblighi F-gas, l'energia degli impianti, 5 questioni aperte e il nuovo hub `area-amministrazione` |
| `data\` | 8 | quattro serie contate, due quadrature, una divergenza fra valori e la misura del tunnel |
| `entities\` | 5 | due celle, il tunnel, il manutentore, il fornitore di energia |
| `docs\` | 1 | il limite critico del CCP4 |
| `workspace\` | 1 | la bozza di contratto mai firmata |

---

## 1-bis. I conteggi del vault a chiusura del lotto, da script

<!-- CONTEGGI DEL VAULT — generati da `06_operativo\qa\conta_stato.py` il 2026-08-19.
     Si incollano VERBATIM: non si ricompongono a mano, non si riscrivono in prosa. -->

| Grandezza | Valore |
|---|---|
| Note nel vault | **145** |
| di cui `_index` | 11 |
| di cui note-strumento del progetto | 6 |
| di cui note di diario (`sessione`, `daily`) | 2 |
| **di cui note di contenuto** | **126** |
| Note per cartella | areas 71 · data 20 · entities 19 · projects 8 · docs 7 · code 7 · concepts 5 · workspace 5 · self 1 · outputs 1 · sources 1 |
| Note per `type` | atomica 78 · conflitto 24 · entita 15 · index 11 · hub 11 · concetto 4 · sessione 2 |
| Questioni aperte (`type: conflitto`) | 24 |
| Grezzi in `sources\` | 160 |
| Grezzi citati da almeno una nota | **33** |
| Grezzi restanti | **127** |

⚠️ **Incollato verbatim da `conta_stato.py`**, che nasce a questo gate: in due lotti su due
i totali ricomposti a mano in prosa erano sbagliati, e nessuno dei due errori era di
canonizzazione. Vedi §7.

---

## 2. Lo spezzamento in apertura, e perché il taglio è dove è

Il lotto 1B della matrice approvata aveva **6 grezzi**. Il conteggio dei fatti prima di
scrivere ha proiettato **~41 note contro un budget di 22-30**: +37 %, oltre la soglia del
25 % oltre la quale E21 impone di spezzare.

Il taglio è stato deciso dal titolare fra tre alternative, e il criterio che ha dato è ora
una regola di mestiere: **si spezza lungo le cuciture, mai attraverso le riconciliazioni.**
La storia della cella CF-02 — allarmi di aprile, arretrati di manutenzione già canonizzati
in 1A, +49,7 % di consumo a maggio, contratto mai firmato — è rimasta **intera** in questo
lotto; parco strumenti, tarature e gas tecnici sono diventati il **lotto 1C**.

La matrice passa da 11 a 12 lotti, con la riga di registro e le riassegnazioni della tabella
di tracciamento.

---

## 3. Cosa ha trovato questo lotto

### 3.1 La cella surgelati non è un'anomalia d'impianto: è un punto critico di controllo

È il fatto che riordina tutto il resto, ed è arrivato da un **grezzo di un altro lotto**: il
manuale HACCP mette la cella `CF-02` dentro il **CCP4**, con limite critico ≤ −18 °C,
registrazione in continuo, **soglia di allarme a −16 °C** e notifica a due responsabili
nominati. Le sei risalite di aprile non sono guasti da officina: sono **superamenti di un
limite critico**, con cinque allarmi su sei non presi in carico e nessuna non conformità
aperta.

L'azione correttiva che il manuale prescrive per la cella fuori limite — trasferimento del
prodotto, chiamata del frigorista, valutazione della qualità su tempo e temperatura — non ha
riscontro in nessun documento dell'archivio per aprile.

### 3.2 Tre azioni correttive registrate che il dato disponibile non conferma

È la **famiglia di divergenze nuova** che questo lotto porta al canone, e nessuna delle tre
si risolve sull'archivio:

| Questione | Cosa dichiara il registro | Cosa mostra il dato |
|---|---|---|
| `questione-sbrinamenti-fascia-notturna-cf-02` | `NC-2026-017`, chiusa in quattro giorni: «spostato ciclo sbrinamento su fascia notturna» | ad aprile gli sbrinamenti sono alle 04, 10, 16 e 22, poi otto e dodici al giorno |
| `questione-limite-allarme-porta-cf-02` | `NC-2026-114`: «allarme porta aperta ridotto a 5 min» | il 15/04 il limite era già `LIM=00:05:00` |
| `questione-nc-067-sbrinamenti-tunnel` | `NC-2026-067`: «TS-01 allarme sbrinamento ricorrente, 3 eventi in settimana» | per il tunnel il log non registra **nessuno** sbrinamento; i 192 del mese sono tutti della cella |

⚠️ **Tutte e tre riguardano ciò che un auditor verifica per primo:** se l'azione correttiva
ha funzionato. E tutte e tre nascono da un incrocio fra un registro compilato a mano e una
registrazione automatica — cioè dal tipo di confronto che §5.1-bis rende obbligatorio.

### 3.3 Sul lato energia, tre cose che nessun singolo documento dice

1. **I contatori di reparto misurano il 45,9 % del prelievo fatturato.** 81.915 kWh sommati
   dalle righe contro 178.480 in fattura: più della metà dello stabilimento non è sotto
   contatore, e nessun documento la ripartisce.
2. **Il costo di un kWh ha tre valori.** 0,182 €/kWh applicato a tutte le righe dei consumi,
   0,12611 dichiarato in fattura come prezzo medio della materia energia, 0,1734 calcolato
   come imponibile diviso i kWh. Nessuno coincide, e il documento che fissa lo 0,182 non è
   in archivio.
3. **Il file dei consumi non ha errori di calcolo.** In 68 righe su 186 la somma delle fasce
   non fa il totale e in 174 il costo non è totale × tariffa, ma in **186 su 186** lo scarto
   rientra in 1,5 kWh dal consumo reale: sono arrotondamenti all'intero. Dirlo al contrario
   sarebbe sbagliato quanto non verificarlo.

### 3.4 Il contratto che non c'è

`contratto_manutenzione_impianto_frigo_TS01.docx` è una **bozza rev. 3 mai firmata**, con
cinque punti ancora in trattativa, una clausola «[da definire]», due importi di canone in
successione e **due date affiancate sulla procura del direttore di stabilimento**. La
distinzione che regge tutto il gruppo di note: **il documento vale per ciò che attesta — le
cariche di refrigerante «risultanti dai registri di apparecchiatura» — non per ciò che
pattuisce.** Le clausole in trattativa stanno tutte e cinque nella nota di `workspace\`, e
in nessun'altra.

---

## 4. Il budget sforato, e di che cosa è fatto lo scostamento

**38 note contro un tetto di 30: +27 %.** Lo scostamento non nasce da una proiezione
sbagliata — le 29 note della prima stesura stavano dentro il budget — ma **dai tre passaggi
di controllo**, che hanno prodotto nove note in più:

| Origine | Note | Quali |
|---|---|---|
| Rilievo A8: due fatti in una nota sola | +1 | la potenza impegnata e la pratica per i 630 kW si separano |
| Divergenze di categoria B da promuovere a questione (§5.3) | +3 | le tre azioni correttive del §3.2 |
| Incoerenza intra-file | +1 | i due incrementi dentro la stessa fattura |
| Lacune di copertura trovate dal revisore | +4 | `macchina-cf-01`, il metano dei forni, le letture del tunnel, e il `doc-ccp4-limite-critico` che le lega |

⚠️ **Nessuna delle nove è nata per riempire.** Il revisore ha campionato dodici note contro
le otto richieste e ha dichiarato **zero sovra-atomizzazione**: ogni nota risponde a una
domanda distinta. Il rischio, in questo lotto, era l'opposto — una nota che ne teneva due.

---

## 4-bis. I tre passaggi di controllo

| Passaggio | Note viste | Esito |
|---|---|---|
| Giudizio di provenance, 1º giro | 29 | 24 pulite · **5 «afferma oltre le fonti»** · 0 fonti inutili · 11 lacune di copertura fuori verdetto |
| Revisione indipendente col canone | 29 + i quattro grezzi | **13 A · 6 B · 8 C**, zero fughe di canone, zero sovra-atomizzazione su 12 note campionate |
| Giudizio di provenance, 2º giro (E9) | 37 | 33 pulite · **4 «afferma oltre»** · 0 fonti inutili · 10 lacune fuori verdetto |
| Giudizio di provenance, 3º giro (E9) | 10, le sole riscritte dopo il 2º giro | 6 pulite · **4 «afferma oltre»** · 3 lacune fuori verdetto |
| Giudizio di provenance, 4º giro (E9) | 6, le sole riscritte dopo il 3º giro | 5 pulite · **1 «afferma oltre»** · 2 lacune fuori verdetto |

**Trentuno rilievi distinti accolti in tutto** — 5 dal primo giudizio, 11 nuovi dal revisore
(due dei suoi 13 rilievi A coincidevano con rilievi che il giudizio aveva già visto), 6
divergenze di categoria B, poi 4 + 4 + 1 dai tre giri successivi di giudizio. Tutti
verificati sui grezzi prima di correggere, e tutti risultati fondati: **nessuno è stato
archiviato come falso allarme del giudice**.

### I tre che valevano da soli i tre passaggi

1. **Un'inferenza nel campo macchina.** La sigla `FRIGOTEC-11` del log era finita fra gli
   `aliases` di Frigotecnica Berica. Nessun documento lega quella sigla a quella ragione
   sociale — e la sessione stessa teneva aperta la questione su chi sia il manutentore:
   l'alias **decideva nel frontmatter ciò che la nota-questione dichiara indecidibile**.
   Tolto dagli alias, dichiarato come inferenza nel corpo, registrato in `alias_entita.md`
   classe C. Ha comportato anche il **rinomino della nota** sull'intervento del 24/04, che
   si portava l'attribuzione dentro il nome del file.
2. **Un'azione correttiva che nessuno aveva guardato.** `NC-2026-017`, chiusa in quattro
   giorni a febbraio con «spostato ciclo sbrinamento su fascia notturna», contro un log di
   aprile in cui gli sbrinamenti sono sulle ventiquattro ore. **È l'unica delle sei
   divergenze di categoria B che nessuna nota aveva visto**: l'ha trovata il revisore, ed è
   quella che pesa di più, perché tocca l'efficacia di una non conformità chiusa.
3. **Il contatore che non separa le linee.** Una nota diceva che il consumo dei forni del
   10/05 «conferma che quella domenica si è prodotto sulla Linea 1». Il contatore è
   intestato a `FORNI FT-01/FT-02` **aggregati**: dice che i forni hanno lavorato, non su
   quale linea. Rilievo del terzo compito della v2, ed è esattamente il genere di
   scivolamento che il prompt nuovo esiste per prendere.

⚠️ **Il 2º giro ha prodotto quattro rilievi su note che il 1º aveva dichiarato pulite**,
perché le correzioni le avevano riscritte: è la ragione per cui E9 esiste.

---

## 4-ter. Quattro giri di giudizio, e dove ci si è fermati

E9 dice di rigiudicare le note nate o modificate dalle correzioni, e non dice **quando
smettere**. Correggere riscrive, e riscrivere crea nuove note da giudicare: in questo lotto
il ciclo ha girato quattro volte, ed è la prima volta che succede.

| Giro | Note viste | Rilievi | Su che cosa |
|---|---|---|---|
| 1º | 29 | 5 | attribuzioni e conclusioni di contesto |
| 2º | 37 | 4 | affermazioni su fonti non citate |
| 3º | 10 | 4 | prosa di collegamento: un elenco illustrativo, un argomento sulle linee, una causa non dichiarata, una settimana di promo |
| 4º | 6 | 1 | un'attribuzione: l'annotazione sulla fattura è dell'amministrazione, non del fornitore |

**Tre cose che questa serie mostra, e che valgono più dei quattro giri in sé.**

1. **La curva converge, e converge sul tipo di difetto, non solo sul numero.** Nessuno dei
   quattordici rilievi ha mai riguardato un numero, una data o un codice — quelli li prende
   lo strato deterministico. Tutti riguardavano **la prosa che lega i fatti**: la frase che
   spiega, l'esempio che illustra, il ruolo attribuito a chi firma. È lì che si scivola, ed è
   lì che serve un lettore che non abbia scritto la nota.
2. **Il quarto giro non era prevedibile dal terzo.** Il rilievo che ha trovato — «il fornitore
   di energia vede l'effetto», dove la frase citata è invece un'annotazione interna di Aurora
   sulla propria fattura — è **nato da una correzione del terzo giro**. Senza il quarto giro
   sarebbe rimasto, e sarebbe stato un fornitore esterno a cui il vault attribuiva
   un'analisi che non ha fatto.
3. **Il criterio con cui mi sono fermato, dichiarato:** il quarto giro ha prodotto **un solo
   rilievo, su una frase aggiunta dal giro precedente, e le sue due segnalazioni fuori
   verdetto erano rimandi facoltativi** — non fatti mancanti. La correzione applicata
   **toglie** un'attribuzione e non ne aggiunge nessuna: non crea materiale nuovo da
   giudicare. Fermarsi qui è una decisione, non una stanchezza, e sta scritta.

⚠️ **Candidato chiarimento a `metodo_03` §9.5 passo 5 (E9), da portare al coordinatore.** La
regola dice di rigiudicare, non dice quando smettere, e un ciclo che riscrive genera sempre
materiale nuovo. Proposta: *si rigiudica finché un giro non torna pulito, oppure finché le
correzioni dell'ultimo giro non sono tutte soppressive — cioè tolgono affermazioni senza
aggiungerne. In entrambi i casi il rapporto di lotto dichiara a quale giro ci si è fermati e
con quale dei due criteri.* Non l'ho applicato come regola: l'ho applicato come scelta
dichiarata, che è quello che il metodo permette a chi canonizza.

---

## 5. Gli avvisi della QA, motivati

**18 avvisi**, ricontati dai quattro report figli — `qa_frontmatter` 11 · `qa_link_integrity`
3 · `qa_provenance` 4 · `qa_copertura` 0 — e le famiglie sommano al totale:

| Famiglia | Avvisi | Perché non si corregge |
|---|---|---|
| «corpo fra 301 e 350 parole: si motiva o si spezza» | **9** | Si motivano: otto portano una tabella di confronto o citazioni testuali lunghe — le note-questione devono riportare **entrambe** le versioni, e le note di riconciliazione entrambe le fonti — e la nona è la bozza di contratto, con cinque punti in trattativa da elencare. Nessuna supera il tetto dei 350, e **tre erano sopra il tetto e sono state accorciate** in corso di lotto |
| «`summary` e `title` si sovrappongono per meno del 20 %» | **4** | Il titolo è una domanda o un'affermazione, il riassunto è la risposta con altre parole: la sovrapposizione bassa è voluta |
| «lontana dall'`_index` della propria cartella (3 salti)» | **3** | Sono note di `areas\` il cui hub proprio è la **macchina**, che vive in `entities\`: il percorso è `_index-areas → area-manutenzione → macchina-cf-02 → nota`. È un indizio di collocazione, non un difetto (§7.2), e qui la collocazione è quella giusta: il soggetto è la cella |
| «`summary` contiene più di una frase» | **2** | ⚠️ **Falso positivo dello strumento**, non un difetto delle note: il controllo conta i punti fermi, e i due riassunti contengono `S.r.l.` e `prot.`. Sono una frase sola. Vedi §10, punto 4 |
| **totale** | **18** | |

⚠️ Un avviso ricade in una sola famiglia: le righe sono disgiunte.

**Cinque avvisi sono stati chiusi correggendo, non motivando**, e la chiusura si scrive
sempre: quattro `summary` sopra i 250 caratteri, riscritti più corti senza perdere nessuna
delle due gambe delle questioni; e una reciprocità hub/spoke sulla nota di diario, che
dichiarava come proprio hub la scheda della cella — un diario non si elenca dentro la scheda
di una macchina, e il rimando è stato spostato su una nota di fatto.

---

## 6. Il perimetro vault

| Controllo | Errori sul vault |
|---|---|
| `qa_frontmatter` | **0** |
| `qa_link_integrity` | **0** |
| `qa_provenance` | **0** |
| `qa_copertura` | 130 — **127 grezzi non ancora canonizzati e 3 aree senza hub** |

Le aree senza hub scendono da quattro a tre: `amministrazione` è nata con questo lotto.

---

## 7. Un'errata ai numeri del lotto 1A

⚠️ **Lo stato dichiarava «105 note, di cui 11 `_index` e 6 note-strumento: 88 di
contenuto».** I conti non tornano: `qa_all.py`, a chiusura di 1A, contava **106** note. Il
105 escludeva `_index-sources` ma sottraeva ugualmente tutti e undici gli `_index`. Il
numero corretto è **89 note di contenuto**. Lo stato è stato corretto con l'errata visibile,
come prescrive la regola del gate 1A: un numero dichiarato che si corregge lascia traccia.

---

## 8. Categoria C — i falsi allarmi, perché non tornino al lotto dopo

Otto, dal revisore. I quattro che vale la pena ricordare:

1. **I numeri del canone sulla quadratura dei consumi erano vecchi.** Il canone diceva 59 /
   137 / «165 su 165»; il riconteggio indipendente dà **68 / 174 / 186 su 186**, e le note
   hanno ragione. Il 165 è il numero delle righe con data `gg/mm/aa`: l'analisi che ha
   prodotto quel numero **saltava le 21 righe in formato ISO**. Il canone è stato emendato in
   sezione datata; la sua conclusione qualitativa resta intatta.
2. **`RTC=NOSYNC` è del tunnel, non della cella.** Sembrava che la nota correggesse una
   contraddizione registrata: legge invece il grezzo alla lettera, e semmai è la riga di
   canone a essere lasca. Precisato nella stessa sezione datata.
3. **Tacere sullo 0,205 €/kWh del CapEx è la scelta giusta**, non una questione monca: quel
   grezzo non è canonizzato, e il divieto 9-bis impone il silenzio fino al lotto che lo porta.
4. **La doppia menzione dell'`RTC=NOSYNC` in due note non è spezzatino**: una racconta
   l'evento, l'altra il valore probatorio del file.

---

## 9. Cosa resta aperto per scelta

- **Le questioni aperte dichiarate** salgono a 24 nel vault, cinque delle quali nate qui.
- **La terza gamba di T18**: `elenco_interni_telefonici.txt` scrive «Frigotecnica Berica», ma
  è un grezzo del lotto 10 e il divieto 9-bis impone di non usarlo prima. **Il lotto 10 deve
  aggiungerlo** alla questione e alla scheda entità: tracciato.
- **Il secondo sito, Via Palù 3/A** (T40): il quarto impianto frigorifero è dichiarato dentro
  la nota sulle cariche F-gas, ma il magazzino non ha ancora una nota padrona. Tre suoi
  strumenti, tutti con taratura scaduta, entrano nel lotto 1C.
- **Il terzo Peruffo** (T39): registrato in `alias_entita.md` classe B; la riga «Da non
  confondere con» sulle schede dei due revisori si scriverà nel lotto che canonizza visura e
  bilancio, perché un rimando non può nascere prima della nota che punta.
- **Le tre aree senza hub** — risorse umane, sicurezza e ambiente, ricerca e sviluppo.

---

## 10. Cosa chiedo al titolare

1. **Approvazione del lotto 1B**, con i numeri qui sopra e lo scostamento di budget
   dichiarato al §4.
2. **Presa d'atto di due scelte di collocazione**, entrambe applicazioni del criterio che il
   titolare stesso ha dato: l'area `amministrazione` **aperta qui** e non nel lotto 6, perché
   il lotto porta una fattura passiva e un controllo di budget e l'hub nasce coi suoi fatti;
   e le note F-gas lasciate in `manutenzione` con il tag della dimensione ambientale, con
   l'impegno tracciato come T34.
3. **Nessun emendamento a `metodo_03` da questo lotto.** Le regole hanno retto: E21 sul
   budget in apertura, E25 sul non anticipare, la definizione di bozza del passo 2, la
   grammatica dei locator. L'unico intervento sugli strumenti è un fix a
   `verifica_matrice_lotti.py` (i lotti chiusi si marcano `# CHIUSO`), già applicato e
   dichiarato nel decision log.
4. **Una decisione su un falso positivo della suite.** Il controllo «`summary` contiene più
   di una frase» conta i punti fermi, e sbaglia su ogni riassunto che contenga
   un'abbreviazione — `S.r.l.`, `prot.`, `n.`, `art.` — che in questo corpus sono ovunque.
   Due avvisi su sedici sono suoi. **Non l'ho toccato**: sarebbe un fix che *toglie* avvisi,
   cioè allenta un controllo, e la regola del gate 1A permette solo fix che *aggiungono*
   agganci. Se il coordinatore lo approva, la correzione è di una riga: non chiudere la frase
   su un punto preceduto da una sigla o da un'abbreviazione nota.

---

## Appendice A — 19/08/2026 · Il pattern che ha rigenerato i rilievi (E26)

⚠️ **Obbligo della regola di arresto approvata a questo gate.** Il ciclo di ri-giudizio ha
girato quattro volte, e E26 chiede che il rapporto **nomini la classe d'errore** che ha
prodotto i giri extra, invece di limitarsi a ripetere il ciclo.

**Il pattern è uno solo, e ha un nome: il contesto importato.**

> Una frase scritta per rendere la nota **leggibile** — non per affermare un fatto nuovo —
> che porta dentro qualcosa che chi scrive sa dall'archivio, ma che **le fonti di quella
> nota non contengono**.

I quattordici rilievi dei quattro giri sono tutti di questa classe, e nessuno ha mai
riguardato un numero, una data o un codice:

| Frase | Che cosa importava | Da dove veniva |
|---|---|---|
| «il foglio OEE l'efficienza» | un documento | un altro lotto |
| «il payback del tunnel nuovo» | un'attività dell'azienda | nessun documento |
| «prima che il fermo e il reclamo occupassero l'azienda» | due eventi | il pilota |
| «il direttore di stabilimento» | un ruolo | la tabella alias |
| «una NC aperta e firmata dal capo officina» | un ruolo | la tabella alias |
| «il fornitore di energia vede l'effetto» | un'attribuzione | una nota interna letta male |
| «le altre linee, gli ausiliari, l'illuminazione» | un elenco illustrativo | il buon senso |
| «in piena settimana di promo» | una data | il canone |
| «il tunnel sulla 3, la cella è di stabilimento» | un argomento | il contratto |

**Dove si annida:** nelle sezioni «Perché conta» e nelle frasi di apertura — cioè
esattamente dove si scrive *per far capire*. È il prezzo di note che devono reggersi da sole
come chunk del RAG: per reggersi da sole devono spiegarsi, e spiegando si sconfina.

**Perché il ciclo lo rigenerava:** ogni correzione **riscrive** la frase incriminata, e la
riscrittura è di nuovo una frase di contesto. Il difetto non stava nelle note: stava nel
gesto di correggerle.

**L'antidoto, per i lotti successivi** — costa dieci minuti e va fatto **prima** del primo
giudizio, non dopo il terzo: rileggere ogni «Perché conta» con davanti **solo** le fonti di
quella nota, e per ogni frase chiedersi *«questa la potrei mostrare a chi ha in mano soltanto
questi documenti?»*. Se la risposta è no, la frase o si àncora citando la fonte che la
regge, o si toglie.

---

## Appendice B — 19/08/2026 · Le segnalazioni fuori verdetto del terzo compito (v2)

⚠️ **Obbligo del coordinatore.** Il terzo compito del `PROMPT_GIUDIZIO` v2 — «esiste, fra le
fonti del pacchetto, un documento che misura la stessa grandezza e che la nota non cita?» —
è alla prima applicazione. Questa appendice classifica **una per una** le sue segnalazioni,
perché al gate finale si decida se il compito resta, si tara o si toglie.

**Il conto.** 26 segnalazioni emesse in quattro giri, di cui 7 ripetute da un giro al
successivo: **19 distinte**. Classificate: **10 accolte con correzione, 9 respinte con
motivo** — poco più di una su due è segnale.

### Le 10 accolte

| Nota | Documento segnalato | Che cosa è cambiato |
|---|---|---|
| `fatto-cariche-f-gas-impianti-frigoriferi` | piano di manutenzione | il piano è ora fonte: dichiara `R448A` sul tunnel, cioè la gamba della divergenza |
| `fatto-assistenza-esterna-24-04-cf-02` | piano di manutenzione | ⚠️ **la segnalazione più preziosa dell'intero lotto**: il piano dà lo sbrinamento del 24/04 a «interno (Bissoli)», la centralina a un operatore esterno. Ne sono nate una divergenza di categoria B, la riga di canone e la riga T42 |
| `fatto-assistenza-esterna-24-04-cf-02` | contratto | l'art. 8.1 impone un rapporto di lavoro per ogni intervento: è ciò che rende significativa l'assenza che la nota registra |
| `kpi-consumi-energia-maggio-2026` | fattura | la nota confrontava un totale che non citava |
| `kpi-metano-forni-maggio-2026` | fattura | la nota affermava il perimetro della fattura senza averla fra le fonti |
| `kpi-temperatura-uscita-tunnel-ts-01-aprile` | registro NC | `NC-2026-006`: lo stesso tunnel aveva superato il limite del CCP4 a gennaio. Circoscrive un'affermazione che sembrava generale |
| `fatto-anomalia-consumo-cf-02-maggio` | log allarmi | la nota richiamava il log nel testo senza citarlo |
| `fatto-anomalia-consumo-cf-02-maggio` | fattura | il controllo di gestione imputa lo scostamento del mese alla stessa cella |
| `questione-nc-067-sbrinamenti-tunnel` | piano di manutenzione | il piano registra due sbrinamenti del tunnel ad aprile: **rafforza la questione invece di chiuderla** |
| `fatto-obblighi-registro-f-gas` | piano di manutenzione | «registro FGAS aggiornato» è l'unico riscontro in archivio sullo stato di quel registro |

### Le 9 respinte, con il motivo

| Nota | Documento segnalato | Perché no |
|---|---|---|
| `kpi-sbrinamenti-cf-02-aprile` | piano di manutenzione | **due grandezze diverse con lo stesso nome**: il piano registra sbrinamenti *di manutenzione* (pulizia programmata), il log i *cicli automatici* della centralina |
| `fatto-allarmi-alta-temperatura-cf-02-aprile` | registro NC | il rapporto fra quegli allarmi e il registro ha già una padrona, `fatto-nessuna-nc-per-allarmi-cf-02`. Aggiungerlo qui creerebbe la doppia padrona che `qa_copertura` segnala |
| `kpi-fattura-energia-maggio-2026` | contatori di reparto | il confronto fra le due misure ha una padrona propria, `fatto-contatori-reparto-meta-stabilimento` |
| `fatto-forni-in-temperatura-durante-fermo-10-05` | registro NC | il fermo del 10/05 è padronanza del pilota, `fatto-fermo-pkm-450-l26130` |
| `fatto-tre-domeniche-produttive-in-fascia-f3` | registro NC | la ricostruzione delle domeniche di maggio è una divergenza **tracciata (T12)** che appartiene ai lotti 5 e 7: questa nota possiede la sola gamba della fattura |
| `entita-frigotecnica-berica` | piano di manutenzione | il piano usa **l'altro nome**: citarlo nella scheda di «Berica» significherebbe attribuirle righe intestate a «Scaligera», cioè decidere la questione aperta |
| `macchina-cf-02` | piano di manutenzione | è un hub, e §7.1 clausola 4 lo verifica **contro le note che elenca**: le voci di manutenzione hanno già la loro padrona, linkata dall'hub |
| `kpi-metano-forni-maggio-2026` | rapporto di fermo | la nota cita il fermo solo come rimando; il legame consumo/fermo ha la sua padrona |
| `fatto-assistenza-esterna-24-04-cf-02` | manuale HACCP | la nota non afferma nulla sul limite critico: il CCP4 ha la sua nota padrona, `doc-ccp4-limite-critico` |

### Che cosa dicono questi numeri sul terzo compito

- **Il segnale è alto dove la nota nomina un documento senza citarlo** (cinque accolte su
  cinque): è un difetto oggettivo, e il giudice lo vede meglio di chi ha scritto.
- **Il rumore è tutto di una forma sola:** il giudice non conosce il grafo del vault, quindi
  segnala come lacuna ciò che è **una padrona altrove**. Sette respinte su nove sono questo.
- **Taratura suggerita, non applicata:** dare al giudice, dentro il pacchetto, l'elenco delle
  note del lotto con il loro `summary`. Vedrebbe che una padrona esiste, e il rumore da
  «padrona altrove» sparirebbe senza toccare il segnale. Da valutare al gate finale.

---

## Appendice C — 19/08/2026 · Conferma sulla sigla `FRIGOTEC-11`

Come richiesto dal coordinatore, in una riga: **`FRIGOTEC-11` è declassata a inferenza
dichiarata.** È fuori dagli `aliases` di `entita-frigotecnica-berica`, è registrata in
`alias_entita.md` **classe C** fra i riferimenti che l'archivio non riconcilia, la nota che
raccontava quell'intervento è stata rinominata da `fatto-intervento-frigotecnica-24-04-cf-02`
a `fatto-assistenza-esterna-24-04-cf-02`, e il giro di link è chiuso: hub della cella,
scheda del manutentore, `kpi-sbrinamenti`, nota degli allarmi e mappatura file × fatto
puntano tutti al nome nuovo. La scheda entità dichiara per esteso che l'attribuzione sarebbe
un'inferenza e la appende a `questione-manutentore-frigo-berica-scaligera`.
