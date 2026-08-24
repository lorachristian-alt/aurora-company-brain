# Matrice dei lotti — canonizzazione del corpus v1

> **Cos'è** · Il piano di lavoro delle Sessioni 4-5: come i grezzi non ancora canonizzati
> si dividono in lotti tematici, in che ordine si eseguono, con quale capacità di note e
> con quali obblighi ciascuno.
> ⚠️ **Al 19/08/2026, dopo il gate del lotto 1C: 35 grezzi canonizzati, 125 restanti, e il
> piano vale circa 28-30 lotti, non dodici.** I dodici temi restano l'ossatura, ma i temi
> 3-10 si ripacchettizzano in apertura (E31); solo il tema 2 è già ridisegnato in 2A/2B/2C.
> Le fasce di note dei lotti 2-10 sono **barrate**, non cancellate. Il perché e la data
> stanno nel **registro delle modifiche** in fondo a questo file, che è il padrone della
> cronologia di questa matrice.
> **Quando si usa** · All'apertura di ogni lotto, per sapere cosa entra e cosa ci si
> aspetta. E al gate finale, per dimostrare che i 160 sono stati coperti tutti.
> **Cosa non toccare** · La regola di partizione: **ogni grezzo sta in esattamente un
> lotto**, e i conteggi si ricavano solo da `verifica_matrice_lotti.py`.

> **Gerarchia** · Artefatto derivato da `01_metodo\metodo_03_canonizzazione.md` §9.3 e
> §9.4. **È un piano, non un vincolo**: se canonizzando si scopre che un fatto sta
> altrove, si aggiorna la matrice e si va avanti — è la matrice a seguire le note.
> Nessuna regola nuova vive qui.

---

## Da dove vengono i numeri

Tutti da script, mai a mano (regola d'oro 5). Due strumenti, entrambi in
`06_operativo\`:

| Script | Cosa conta |
|---|---|
| `inventario_grezzi.py` | grezzi su disco, grezzi già citati da almeno una nota, grezzi restanti, ripartizione per estensione |
| `verifica_matrice_lotti.py` | che ogni grezzo stia in **esattamente un** elenco, che nessun elenco nomini un file inesistente, che nessun lotto contenga un grezzo già coperto |

Esito dell'inventario del **18/08/2026**, a vault fermo dopo la Sessione 2:

```
Grezzi su disco in sources\ .. 160
Nomi nel manifest v1.1 ....... 160
Grezzi CITATI da almeno una nota 22
Grezzi RESTANTI .............. 138
```

Esito della verifica della matrice, stessa data:

```
grezzi su disco ............ 160
nomi distinti nella matrice  160
scoperti ................... 0
guasti ..................... 0
```

**Come si tratta il file di avvertenza.** `_QUESTO_ARCHIVIO_E_SIMULATO.txt` **è dentro il
manifest v1.1** — che ha 160 voci, non 159 — quindi la copertura di §7.4 lo pretende come
tutti gli altri. Non riceve una nota propria: è uno dei file privi di contenuto
informativo, e si copre dentro `kpi-composizione-archivio` in `data\` insieme al lock file
di Word `~$ttera_risposta_Tosano_reclamo_BOZZA_v3.docx` (metodo_03 §7.4). Entrambi stanno
nel **lotto 10**, che è il lotto che scrive quella nota.

---

## I dodici lotti, in ordine di esecuzione

Il numero del lotto **è** l'ordine di esecuzione.

| # | Tema | Grezzi | Budget note di contenuto | Aree nuove che apre |
|---|---|---|---|---|
| 1A | Linea 1: il turno, i CCP e la confezionatrice | 7 | 34-42 | — |
| 1B | Freddo ed energia: cella CF-02, tunnel TS-01, consumi e fattura | 4 | 22-30 | — |
| 1C | Metrologia e gas tecnici: parco strumenti, tarature, azoto alimentare | 2 | 12-18 | — |
| 2 | Igiene, sanificazione, autocontrollo, MOCA | 12 | ~~20-30~~ **SUPERATO** — ridisegnato in 3 pacchetti, vedi sotto | — |
| 3 | Sistema qualità, certificazioni, audit, crisi | 13 | ~~22-32~~ **SUPERATO** — da ripacchettizzare in apertura | — |
| 4 | Filiera in entrata, fornitori, logistica | 14 | ~~26-36~~ **SUPERATO** — da ripacchettizzare in apertura | — |
| 5 | Commerciale: cliente, listini, marginalità | 15 | ~~28-38~~ **SUPERATO** — da ripacchettizzare in apertura | — |
| 6 | Amministrazione, bilancio, cassa | 15 | ~~28-40~~ **SUPERATO** — da ripacchettizzare in apertura | `amministrazione` |
| 7 | Persone: lavoro, organico, sindacato | 15 | ~~24-34~~ **SUPERATO** — da ripacchettizzare in apertura | `risorse-umane` |
| 8 | Sicurezza sul lavoro, ambiente, assicurazioni | 11 | ~~16-24~~ **SUPERATO** — da ripacchettizzare in apertura | `sicurezza-ambiente` |
| 9 | R&D, nuovi prodotti, investimenti, visione | 12 | ~~22-30~~ **SUPERATO** — da ripacchettizzare in apertura | `ricerca-sviluppo` |
| 10 | Rumore di fondo e forma dell'archivio | 18 | ~~14-22~~ **SUPERATO** — da ripacchettizzare in apertura | — |
| | **totale** | **138** | ~~246-352~~ — il budget non si stima più a tavolino: **E31** | 4 hub d'area nuovi |

### ⚠️ I budget dei lotti 2-10 sono SUPERATI, e il piano non è più a 12 lotti — 19/08/2026

**Le fasce qui sopra restano scritte e barrate**: erano costruite sulla densità del pilota
(2,1 note per grezzo), e i consuntivi dei quattro lotti chiusi le smentiscono. **Non sono
state sostituite con altre fasce**, perché sostituire una stima sbagliata con una peggiore
non è una ricalibrazione: al loro posto vale **E31**, il budget come **capacità**.

| | |
|---|---|
| **Capacità di un lotto** | **25-35 note di contenuto** — la fascia in cui sono caduti tutti e quattro i lotti chiusi (46 · 42 · 38 · 27) |
| **Quanti grezzi ci stanno** | si decide **in apertura**, contando i fatti (E21, E28), non in pianificazione |
| **Pacchetti indicativi** | **3-5 grezzi** per i lotti di contenuto, **8-10** per il rumore di fondo |
| **Stima del numero di lotti** | ⚠️ **circa 28-30 invece di 12.** Cambia il calendario delle Sessioni 4-5, non solo questa matrice |
| **La capacità è PROVVISORIA** | 25-35 poggia su **quattro osservazioni**, tre delle quali su lotti piccolissimi: **si rivede a dieci lotti chiusi** |

⚠️ **Solo il lotto 2 è ridisegnato in dettaglio** (qui sotto). Gli altri restano temi, non
lotti: ripacchettizzarli tutti adesso sarebbe di nuovo pianificazione a lungo raggio su dati
scarsi, cioè l'errore che questa stessa ricalibrazione ha appena smontato.

### Il ridisegno del tema 2 — igiene, sanificazione, autocontrollo, MOCA

Dodici grezzi, tre pacchetti che seguono le cuciture della storia e non il conteggio dei file.
⚠️ **I budget qui sotto sono capacità attese, non promesse**: valgono fino al conteggio dei
fatti in apertura, che può spezzare ancora.

| Lotto | Tema | Grezzi | Capacità attesa |
|---|---|---|---|
| **2A** | **Il lavaggio CIP**: il log di maggio, l'istruzione operativa che prescrive il criterio, la scheda di sicurezza del detergente | `log_lavaggio_CIP_linea1_maggio.log` · `IO-05_istruzione_operativa_lavaggio_CIP.docx` · `scheda_sicurezza_detergente_acido_lavaggio_CIP.txt` | 25-35 |
| **2B** | **L'autocontrollo ANALITICO**: i tre registri che portano risultati di misura con un limite — tamponi di superficie, acqua potabile, acque reflue | `registro_tamponi_superfici_listeria_salmonella.csv` · `piano_autocontrollo_acqua_potabile_analisi.csv` · `analisi_acque_reflue_autocontrollo_2026.xlsx` | 25-35 |
| **2B-bis** | **Gli allergeni**: la scheda con la matrice di cross contamination e la formazione annuale che la insegna agli operatori | `scheda_allergeni_matrice_cross_contamination.docx` · `formazione_allergeni_operatori_2026.pptx` | 25-35 |
| **2C** | **I materiali a contatto**: registro MOCA, dichiarazione di conformità del film col suo duplicato, capitolato degli imballaggi | `estratto_registro_carico_scarico_MOCA.xlsx` · `DoC_MOCA_Flexipack_film_PP_EVOH_2026.pdf` · `doc 2 (1).pdf` · `capitolato_tecnico_fornitura_imballaggi_plastici.txt` | 25-35 |

**Perché il taglio è dove è.** `IO-05` è la **fonte prescrittiva** del log CIP (E29): separarli
metterebbe il registro in un lotto e la regola che lo giudica in un altro, che è esattamente il
difetto che il lotto 1C ha pagato col manuale HACCP. Il duplicato `doc 2 (1).pdf` resta con il
suo originale, perché è **una nota sola con due nomi in `fonti`** (divieto 21). Gli allergeni
stanno con l'autocontrollo e non con i MOCA: la contaminazione crociata è un pericolo di
processo, la migrazione dal film è un pericolo di materiale.

**Il budget si misura sulle note di CONTENUTO** (E17): esclusi gli `_index`, che nascono
per cartella toccata, e le note-strumento di `code\`. Le fasce qui sopra non sono una
formula: sono una stima costruita sulla densità del pilota — **46 note di contenuto su 22
grezzi**, cioè 2,1 — corretta lotto per lotto secondo quanti fatti porta ciascun gruppo di
documenti. I lotti 1A e 6 stanno sopra la densità del pilota perché contengono documenti
che portano molti fatti indipendenti; il lotto 10 sta molto sotto, perché è rumore di
fondo e «rumore significa nota corta e pochi link» (metodo_03 §1.3, esempio 23).

⚠️ **Sforare il budget non è un errore da nascondere: è un dato.** Il rapporto di lotto
dichiara lo scostamento e il perché. Un budget rispettato tagliando fatti è peggio di un
budget sforato.

### La regola di apertura, nata dal lotto 1 — 18/08/2026

**Il conteggio dei fatti si fa PRIMA di scrivere, all'apertura di ogni lotto.** Si leggono
i grezzi, si elenca cosa merita una nota e si proietta il totale. **Se la proiezione supera
il budget di oltre il 25%, ci si ferma e si spezza il lotto prima di scrivere**, non dopo.

Nasce da un caso reale: il lotto 1 ha proiettato **~62 note contro un budget di 26-36** —
densità **4,8 note per grezzo contro 2,1 del pilota** — perché quattro dei suoi documenti
sono multi-fatto (il quaderno del capoturno copre nove giornate, la trascrizione del
MOD-QA-07 copre 195 verifiche orarie, la scheda di manutenzione 112 voci, la scheda tecnica
nove sezioni). Un grezzo denso non è un grezzo grande: **il numero dei file non dice niente
sul numero dei fatti**, ed è per questo che il budget si controlla sui fatti contati, non
sui file elencati.

Lo stop-loss della scaletta dice «lotto più piccolo, mai QA più leggera»: questa regola lo
rende eseguibile prima che il danno sia fatto. ⚠️ **Candidato chiarimento a `metodo_03` §9**,
da portare al gate finale della canonizzazione.

### La guardia contro la sovra-atomizzazione — 18/08/2026

Spezzare un lotto perché i fatti sono tanti ha un rischio speculare: **produrre note perché
si può, non perché servono**. La soglia dichiarata, e il rapporto di lotto la deve riportare:

> **Un fatto merita nota propria se esiste una domanda plausibile a cui quella nota è la
> risposta migliore** — non se il grezzo lo nomina. La citazione letterale non basta: un
> elenco anagrafico non è un fatto (metodo_03 §1.3, esempio 18), e un dettaglio che si legge
> solo dentro il racconto di un altro fatto appartiene a quel fatto.

Al revisore indipendente si chiede esplicitamente di **verificare un campione delle note nate
dai documenti multi-fatto**: se non sono agganciabili a una domanda, è sovra-atomizzazione, e
se ne discute nel rapporto di lotto — non al gate finale, quando sarebbero centinaia.

### Perché quest'ordine

- **Il lotto 1A è imposto dal prompt** e dal rapporto di gate S2 §6.2: porta dentro
  `appunti_capoturno_quaderno_linea1_OCR.txt`, che è la gamba mancante di tutti e tre i
  conflitti in lista di tracciamento. Va fatto per primo perché tre note del pilota
  restano incomplete finché quel file non entra. **1B e 1C lo seguono subito**: sono lo
  stesso terreno, e chiudono le riconciliazioni che 1A lascia aperte per mancanza della
  seconda gamba — **T18, T22 e T30 in 1B** con il contratto di manutenzione e i consumi,
  **T17, T20, T25, T26 e T32 in 1C** con l'elenco delle tarature e la bolla dell'azoto.
- ⚠️ **Alla chiusura di 1A + 1B + 1C i budget dei lotti restanti si ricalibrano sui consuntivi.**
  Le stime da 2 a 6 sono state fatte con la densità del pilota; se anche solo uno dei due
  lotti conferma una densità sopra le 3 note per grezzo, le fasce dei lotti densi vanno
  rifatte prima di aprirli. La matrice segue le note.
- **I lotti 2 e 3 chiudono il tema qualità** finché le entità e gli hub del caso L26130
  sono freschi: CCP, CIP, allergeni, audit, procedura reclami. Il lotto 3 riapre anche il
  reclamo `REC-2026-011`, perché contiene la notifica del form del sito.
- **Il 4 precede il 5** — prima la filiera a monte, poi il mercato a valle: il costo delle
  materie prime è la gamba che serve al lotto commerciale per leggere la marginalità, e le
  schede fornitore nascono prima di essere citate.
- **6, 7, 8 e 9 aprono le quattro aree ancora senza hub.** Vengono dopo perché ciascuna
  riconcilia numeri con note che i lotti precedenti hanno già scritto (il costo della non
  qualità con il cruscotto, gli straordinari con il piano di produzione, il CapEx con i
  consumi energetici).
- **Il 10 è l'ultimo, e non per pigrizia**: `kpi-composizione-archivio` deve dichiarare i
  conteggi del vault e i file muti, e `elenco_interni_telefonici.txt` e
  `elenco_chiavi_e_accessi.txt` non producono note proprie ma **righe nelle schede delle
  persone** (metodo_03 §1.3, esempio 18) — che a quel punto esistono tutte.

---

## Gli obblighi che ogni lotto si porta dietro

### Lotto 1A — Linea 1: il turno, i CCP e la confezionatrice · **7 grezzi · 34-42 note**

`appunti_capoturno_quaderno_linea1_OCR.txt` **sta in cima all'elenco**, ed è la ragione
per cui questo lotto è il primo.

**I tre conflitti tracciati vanno CHIUSI qui**, riaprendo le note del pilota:

| Conflitto (rapporto di gate S2 §6.2) | Nota da riaprire |
|---|---|
| MOD-QA-07, tre versioni dello stesso turno | `areas\fatto-verifiche-ccp3-turno-l26130` |
| Pezzi del turno: il quaderno porta una terza fonte («0450: solo 4.100 pz oggi + quelo di T1») | `data\questione-pezzi-prodotti-l26130` |
| Arrivo dell'officina: 15:25 contro 15:50 | `areas\fatto-fermo-pkm-450-l26130` |

Le altre due gambe del primo conflitto entrano con lo stesso lotto:
`checklist_metal_detector_manuale_operaio.txt` è la trascrizione del modulo.

Altro che questo lotto deve produrre o riconciliare:

- **la scheda tecnica di AF-SN-0450** porta i pezzi per cartone, che il canone dichiara in
  conflitto con listino e accordo quadro: la seconda gamba arriva nel lotto 5, e la
  divergenza si chiude lì. Qui si scrive quello che la scheda dice, e i due dati che la
  scheda prodotto aspettava dalla Sessione 2 (pezzi per cartone e ITF-14) si compilano se
  attestati;
- **le velocità nominali delle linee** del piano di produzione vanno confrontate con il
  foglio OEE già canonizzato (E2, riconciliazione con le note esistenti);
- **il manuale della PKM-450** è l'estratto che servirebbe a chiudere
  `questione-codice-allarme-pkm-450`: se la tabella allarmi non c'è, l'assenza si dichiara
  con ricerca su tutto `sources\`, datata e riferita al manifest (E3), e la questione
  resta aperta;
- **la scheda di manutenzione** porta due fatti che nessun altro documento dice: la
  sostituzione preventiva della guarnizione della valvola azoto era **scaduta dal
  12/01/2026**, e la revisione della valvola modulante vapore del PT-104 era **rimandata due
  volte** con annotata «oscillazioni in regolazione». Vanno scritti, e vanno linkati ai fatti
  del 10/05 senza concludere un nesso che nessuna fonte afferma.

### Lotto 1B — Freddo ed energia: cella CF-02, tunnel TS-01, consumi e fattura · **4 grezzi · 22-30 note**

⚠️ **Nato dal secondo spezzamento del 19/08/2026**: il vecchio 1B da 6 grezzi proiettava
~41 note contro un budget di 22-30, e E21 impone di spezzare prima di scrivere. Il taglio
segue le cuciture: **la storia della cella CF-02 resta intera**, perché gli allarmi di
aprile, le manutenzioni arretrate già canonizzate in 1A, il +49,7 % di consumo di maggio e
il contratto mai firmato sono lo stesso fatto visto da quattro documenti.

- **i consumi energetici dei forni** non si trattano come un file con errori di calcolo:
  arrotondamenti, non difetti (metodo_03 §5.5 e divieto 4). Il costo dell'energia va
  confrontato con la bolletta VenetaEnergia dello stesso lotto; la terza gamba (0,205
  €/kWh del CapEx) arriva nel lotto 9 e **non si anticipa** (E25);
- **il log allarmi della cella surgelati** dichiara la propria integrità compromessa
  (`DUR=` già presente nel record di apertura dell'allarme, `RTC=NOSYNC` su una delle due
  centraline dopo il blackout del 21/04, file troncato a metà riga): l'integrità
  autodichiarata è **contenuto** e va registrata;
- **il contratto Frigotecnica** porta la gamba mancante di T18, aperta nel lotto 1A. ⚠️ È
  una **bozza rev. 3 non firmata**, con clausole ancora in discussione: le sue clausole non
  prescrivono nulla, e la nota che lo descrive vive in `workspace\` (metodo_03 §1.1
  passo 2). I fatti che il contratto attesta — cariche di refrigerante, impianti coperti —
  si scrivono dichiarando che la fonte è una bozza;
- **le manutenzioni arretrate su CF-02** già canonizzate in 1A (T22, T30) trovano qui le
  altre due gambe: gli allarmi di aprile e le annotazioni sui consumi di maggio;
- **gli obblighi F-gas** stanno in `area: manutenzione` con il **tag trasversale** della
  dimensione ambientale: le note non traslocano, quindi l'area si assegna a chi governa i
  fatti oggi, non a un assetto futuro. L'hub `area-sicurezza-ambiente` nasce nel lotto 8
  con i suoi fatti e linka queste note come rimandi laterali (T34).

### Lotto 1C — Metrologia e gas tecnici: parco strumenti, tarature, azoto · **2 grezzi · 12-18 note**

- **l'elenco tarature** attesta che il datalogger del PT-104 era in taratura valida il
  10/05: è la base metrologica dell'arbitrato datalogger contro registro cartaceo (T20).
  Riapre anche **T25** (convalida dell'MD-3200), **T26** (sigle dei tasselli del CCP3) e
  **T32** (posizione dell'MD-3200 in linea);
- ⚠️ **Le righe di strumento non fanno altrettante note.** Vale la guardia contro la
  sovra-atomizzazione: il rapporto di lotto dichiara **il criterio con cui una riga diventa
  una nota**, e il revisore riceve un campione da verificare. Una selezione deve restare
  una selezione;
  ⚠️ **Errata del 19/08/2026: le righe sono 120, non 121.** Il numero di questa matrice era
  stato scritto a mano in fase di pianificazione; `conta_1c.py` ne conta **120 di strumento**,
  più **due righe di intestazione** — la seconda a riga 64, con nomi di colonna diversi dalla
  prima. Vale il numero dello script (regola d'oro 5);
- **la bolla Nordgas** porta la gamba mancante di T17: registra scarico di azoto **in
  serbatoio fisso** SB-AUR-01 e bombole solo di CO2, mentre il quaderno dello stesso giorno
  scrive «bombola nordgas cambiata alle 16».

### Lotto 2 — Igiene, sanificazione, autocontrollo, MOCA · **12 grezzi · 20-30 note**

- **CIP contro IO-05** è una contraddizione **con vincitore** già registrata nel canone:
  nota padrona `stato: risolto`, IO-05 prevale, il log resta com'è (metodo_03 §5.2, ed è
  l'esempio 17 del manuale). Non si apre una questione.
- `doc 2 (1).pdf` è il **duplicato** di `DoC_MOCA_Flexipack_film_PP_EVOH_2026.pdf`: una
  nota sola, entrambi i nomi in `fonti`, una riga che dichiara la duplicazione.
- **DoC contro capitolato CTF-IMB-02 rev. 4** sulla barriera al vapore (4,5 contro 4,0
  g/m²·24h): il capitolato firmato prevale, e il film in uso non soddisfa la specifica.
- Il registro MOCA e i tamponi superficie si agganciano al caso del frammento già
  canonizzato: E2 verso `projects\fatto-esito-laboratorio-frammento`.

### Lotto 3 — Sistema qualità, certificazioni, audit, crisi · **13 grezzi · 22-32 note**

- ⚠️ **`segnalazione_qualita_cliente_privato_corpo_estraneo.txt` è la notifica del form
  del sito del reclamo Grigolon**, non un secondo reclamo. Porta l'orario `12/05/2026
  18:23:47`, cioè la gamba della divergenza sull'ora di arrivo già registrata nel canone
  (S2, addendum del 16/08). Questo lotto **riapre**
  `projects\questione-data-apertura-rec-2026-011` e il progetto
  `progetto-gestione-reclamo-rec-2026-011`.
- Il **rilievo di audit CSQA** di febbraio contiene le due NC minori che il filo rosso fa
  materializzare il 10/05: la nota padrona di ciascuna NC linka i fatti del pilota.
- **Certificazioni possedute → `self\`**, non `docs\` (metodo_03 §1.3, esempio 3):
  `self-certificazioni` nasce qui, `area: qualita`.
- **Il costo della non qualità** del cruscotto è una delle divergenze del terzo gruppo del
  canone (24.420 · 29.600 · 39.500 · 135.793): le altre gambe stanno nei lotti 5 e 6, la
  questione si apre qui e si completa lì.

### Lotto 4 — Filiera in entrata, fornitori, logistica · **14 grezzi · 26-36 note**

- **Contratto contro listino Molino Veneto**: prevale il contratto (formula unica, +8,8%
  contro +9,8%; semola 655,00 €/t contro 66,10 €/q.le). Contraddizione **con vincitore**.
- **DDT 48392 letto due volte**: `SKM_C224e26050408520.jpg` (12 colli da 1.000 kg, targa BF
  442 XY) contro `DDT_MOLINO_VENETO_..._OCR_SPORCO.txt` (480 sacchi da 25 kg, targa EV 512
  KT). **Non sono duplicati**: sono due letture divergenti, e non vince nessuna delle due.
  La foto porta `verifica: visiva`.
- `img20260428_09241055.txt` **è** il duplicato di `DDT_Euroglass_Boccacci_Vetro_N99201.txt`:
  una nota, due nomi in `fonti`.
- Questo lotto chiude le due questioni aperte del pilota sul lotto farina MV26-0429/A —
  TMC e modo di consegna — solo se i grezzi che entrano portano la gamba mancante; se non
  la portano, **restano aperte e lo si dichiara**.
- **Classifica fornitori**: il pari merito 88,2 gestito male da `MATCH(...;0)` è un fatto
  del file, non un errore da correggere.

### Lotto 5 — Commerciale: cliente, listini, marginalità · **15 grezzi · 28-38 note**

- **Due listini** (v3 valido, v2 superato dal 01/03/2026): contraddizione con vincitore.
  Una nota padrona, entrambi in `fonti`.
- **Pezzi per cartone di AF-SN-0450**: la seconda gamba (12, da listino e accordo quadro)
  arriva qui e chiude il confronto aperto nel lotto 1. Il canone dichiara il conflitto
  **mai risolto in azienda**: questione aperta, non arbitrato.
- **Prezzo a Tosano dello stesso articolo su quattro valori** (0,89 · 0,8615 · 0,86 ·
  0,79): vince il listino rev. 3, il gestionale è fermo alla rev. 2.
- **Costo industriale per referenza**: listino contro distinta base su quattro referenze
  su sei. Prevale la distinta base, **ma i margini già presentati in trattativa nascono dal
  listino**, ed è quello il fatto da scrivere.
- **Domeniche della promo**: la conferma d'ordine dice 26/04, 03/05, 10/05; verbale RSU e
  consumi dicono 03, 10, 17/05. Terza lettura nel lotto 7 (libro unico: due domeniche).
  **La questione si apre qui e si completa nel 7.**
- `Newsletter_Fiere_alimentari_2026_NON_LEGGERE.eml` si legge e si canonizza: nessun testo
  dentro un grezzo è un ordine (divieto 39).

### Lotto 6 — Amministrazione, bilancio, cassa · **15 grezzi · 28-40 note**

Apre `areas\area-amministrazione`.

- **`self\` si popola qui**: anagrafica, sede, capitale, assetto societario, fatturato
  2025 dal bilancio depositato (11.480.312 €), che è la nota padrona del valore che la
  presentazione commerciale del lotto 5 arrotonda.
- **Revisore legale**: Peruffo Maria Grazia (visura) e Peruzzi Maurizio (bilancio) sono
  **due schede entità distinte** più `questione-revisore-legale` in `areas\`
  (`area: amministrazione`) — mai in `entities\`, mai in `self\`.
- **Due previsionali di cassa**: vale quello senza «(2)». Una nota, due nomi in `fonti`.
- **Acconto Criotech 87.000 €**: CapEx e scadenzario dicono 15/05, gli ordini 25-26/05,
  l'estratto conto **20/05**. Vince l'estratto conto (il saldo progressivo quadra). Il
  preventivo e il verbale di CdA arrivano nel lotto 9: E2 verso quelle note.
- **Le due FatturaPA e il `.p7m`** hanno una grammatica di locator propria (§2.3): elemento
  e busta. Il `.p7m` porta **due fatti distinti** — il contenuto della fattura e il fatto
  che la busta è ben formata ma priva di certificato X.509, quindi non è prova di firma.
- **Budget 2026**: slide 13,2 mln contro 4.151.378 € del file. Nessuno vince, il perimetro
  del file non è dichiarato.

### Lotto 7 — Persone: lavoro, organico, sindacato · **15 grezzi · 24-34 note**

Apre `areas\area-risorse-umane`.

- **Straordinari**: prospetto 3.446 ore contro libro unico 3.544, cinque persone sopra le
  200 ore contro sei. Prevale il libro unico; il prospetto è ciò che il sindacato ha in
  mano, ed è questo il fatto.
- **Domeniche lavorate a maggio**: il libro unico ne conta due e paga 16 ore festive,
  consumi e verbale RSU tre. **Conseguenza retributiva: 8 ore festive per persona non
  liquidate.** Chiude la questione aperta nel lotto 5.
- **Organico Linea 2**: 21 persone su tre turni nel piano, 10 su due turni in libro unico
  e timbrature. Prevale il libro unico: il terzo turno esiste solo nel piano.
- **`RANZATO_F` e `CESTARO_L`**: schede entità con ciò che i grezzi dicono, più una
  questione aperta sull'export parziale delle timbrature. **Non si inventa una matricola e
  non si conclude che le persone non esistano** (classe C della tabella alias).
- ⚠️ **`Nuova cartella di lavoro.xlsx` non è un file vuoto**: contiene «prova estrazione
  ore», «chiedere a Federica il file giusto delle timbrature», due valori (38 e 42) e una
  **cella `SUM` mai calcolata**. È il caso del divieto 11: non si fonda un fatto su una
  formula non calcolata, che l'estrattore congelato legge `None`.

### Lotto 8 — Sicurezza sul lavoro, ambiente, assicurazioni · **11 grezzi · 16-24 note**

Apre `areas\area-sicurezza-ambiente`.

- **Infortunio Corradin del 28/04**, denuncia INAIL: esiste, e va distinto dal «nessun
  contenzioso giudiziale» del canone.
- **Impianto assicurativo**: in archivio c'è la polizza Novaria (RC prodotti 5 mln,
  scadenza 30/06/2026); il report OpEx del lotto 6 parla di Generali e AIG e apre un
  sinistro su una polizza che non esiste. Prevale la polizza; E2 verso la nota del lotto 6.
- CPI, AUA, verifica DPR 462, registro rifiuti, estintori: adempimenti con scadenze che
  tornano da sole — è la definizione di `areas\`, non di `projects\`.

### Lotto 9 — R&D, nuovi prodotti, investimenti, visione · **12 grezzi · 22-30 note**

Apre `areas\area-ricerca-sviluppo`.

- **Sviluppo AF-SN-0470**: la ricetta data la v12 al 16/04 con paprika Italspezie, il
  quaderno di laboratorio la prova l'11/05 con paprika La Dehesa, la mail del 07/05 dice
  «parte la settimana prossima». Prevalgono quaderno e mail, contemporanei ai fatti.
- **Costo ingredienti dello snack nuovo**: 0,26 €/pz nel business case contro 0,5478 della
  marginalità (lotto 5). Prevale la distinta base: col dato vero il margine passa dal 35%
  al 7,6%. E2 verso la nota del lotto 5.
- **Tunnel Criotech**: `projects\progetto-tunnel-surgelazione` come hub, `stato: attivo`.
  Il preventivo esiste in due copie (PDF e mail di inoltro): una nota, due nomi in `fonti`
  se sono lo stesso documento, due note se la mail porta fatti propri.
- **Costo dell'energia 0,205 €/kWh** dichiarato «media contratto gen-apr»: terza gamba
  della divergenza aperta nel lotto 1.
- **Aurora Vega**: esistono la localizzazione a Minerbe, una valutazione «meramente
  esplorativa» a verbale e un accenno nella job description. **Non esistono preventivo,
  computo o business plan**, e l'assenza si dichiara con la ricerca su tutto `sources\`
  (E3).

### Lotto 10 — Rumore di fondo e forma dell'archivio · **18 grezzi · 14-22 note**

- Produce **`data\kpi-composizione-archivio`**: conteggi per formato, le quattro coppie di
  duplicati, i file privi di contenuto informativo (`~$ttera_...docx`,
  `_QUESTO_ARCHIVIO_E_SIMULATO.txt`). È la nota che chiude la copertura sui file muti e
  senza la quale `_index-sources` non può dichiarare un numero (metodo_03 §7.4).
- **Rumore non significa «non canonizzare»**: significa nota corta e pochi link
  (esempio 23). Menù, palestra, condominio, cancelleria, cena aziendale: una nota breve
  ciascuno, perché una domanda può chiederne il contenuto.
- `elenco_interni_telefonici.txt` e `elenco_chiavi_e_accessi.txt` **non producono note
  proprie**: i dati vanno nelle schede persona, e i due file compaiono in `fonti` di
  ciascuna (esempio 18).
- Costi minori (fotocopiatrice, antivirus, distributori): E2 verso
  `report_costi_fissi_OpEx_manutenzioni` canonizzato nel lotto 6.

---

## La tabella di tracciamento viva

**Obbligo del titolare, gate della matrice del 18/08/2026.** Una questione che un lotto
apre e un altro completa è il modo più facile di perdere un conflitto: nel lotto che la
apre sembra un lavoro finito, e nel lotto che dovrebbe chiuderla nessuno si ricorda che
esiste. Questa tabella è il rimedio, e **si aggiorna alla chiusura di ogni lotto**, prima
del commit.

⚠️ **Al gate finale, «conflitti chiusi / aperti dichiarati» si prova con questa tabella,
non a memoria.** Nessuna riga sparisce, e gli esiti con cui una riga esce sono **tre**, non
due — la distinzione è del coordinatore, al gate del lotto 1C:

| Esito | Che cosa significa |
|---|---|
| **chiusa** | la gamba mancante è arrivata, la nota lo dice, e la questione non era una divergenza o si è risolta con un vincitore |
| **aperta dichiarata** | l'archivio non la chiude, e c'è una nota `type: conflitto` che lo scrive |
| **riconciliata** | ⚠️ **due fonti che sembravano contraddirsi smettono di farlo**, perché una terza spiega il meccanismo che le concilia |

⚠️ **La terza non è un pareggio: è un risultato del vault**, ed è ciò che la misura «dopo»
dovrà saper mostrare. Un archivio grezzo lascia la contraddizione apparente dov'è; un archivio
che ha capito il meccanismo la scioglie e lo dichiara.

⚠️ **Quante righe escono con quale esito NON si scrive qui, e non si legge a occhio.** Il
numero lo produce `06_operativo\conta_tracciamento.py`, e si incolla nello stato e nei
rapporti di lotto. Questo paragrafo dichiarava «due righe riconciliate, T22 e T17» ed era
già vecchio di una riga: è esattamente il motivo per cui il conteggio è passato a uno
script il 19/08/2026.

Le righe qui sotto sono il **seme**, ricavato dagli obblighi di lotto e dalla lista di
tracciamento del gate S2 §6.2. Le questioni che nasceranno canonizzando si aggiungono qui.

| # | Questione | Aperta da | Gamba mancante attesa in | Stato |
|---|---|---|---|---|
| T1 | MOD-QA-07, tre versioni delle verifiche CCP3 dello stesso turno | pilota S2 | chiusa in **1A** | **aperta dichiarata** — `questione-verifiche-ccp3-10-05-tre-versioni`: il modulo scansionato registra 5 verifiche con le 16:00 e le 17:00 barrate, la trascrizione ne registra 8 comprese quelle, il quaderno ne dichiara 2 saltate. Nessuna delle tre prevale |
| T2 | Pezzi del turno L26130-L1-T2: il quaderno porta una terza fonte | pilota S2 | chiusa in **1A** | **aperta dichiarata** — `questione-pezzi-prodotti-l26130` estesa: il quaderno dà 4.100 «+ quelo di T1», ed è **l'unica delle tre fonti che dichiara il proprio perimetro** |
| T3 | Arrivo dell'officina al fermo PKM-450: 15:25 contro 15:50 | pilota S2 | chiusa in **1A** | **aperta dichiarata** — nota nuova `questione-arrivo-officina-fermo-pkm-450`: 25 minuti di scarto, nessun terzo documento con marca temporale |
| T4 | Codice dell'allarme PKM-450: `E-214 GAS` contro `AL-217` | pilota S2 | chiusa in **1A** | **aperta dichiarata** — l'estratto del manuale **non contiene la tabella allarmi** (assenza verificata sui 160 file del manifest con l'estrattore congelato) e usa una **terza codifica**, `A031` per la pressione gas. Serve il manuale completo, 184 pagine, che in archivio non c'è |
| T5 | Ora di arrivo della segnalazione del reclamo: 18:23 contro le 17:55 della catena mail | pilota S2 (canone, add. 16/08) | **lotto 3D** (la notifica del form del sito) | **aperta dichiarata** — ⛔ **NON chiusa: il lotto 3D ha portato il documento che serviva, e la divergenza si e' ALLARGATA.** La notifica automatica del form dichiara `2026-05-12 18:23:47 CEST`, e la riunione concorda; ⚠️ **ma la prima mail interna sul reclamo, delle 14:33 dello stesso giorno, dice che era arrivato ALLE 13:05 dal form** — cinque ore e diciotto minuti prima. **L'intera catena interna del 12/05 sta prima delle 18:23**, non solo il messaggio delle 17:55 che questa riga nominava. **La divergenza ha una padrona**: `questione-ora-di-arrivo-della-segnalazione` |
| T6 | Data di apertura di REC-2026-011: 12/05 sulla scheda, 13/05 secondo la responsabile qualita' | pilota S2 | **lotto 3D** (PRO-QA-08, procedura reclami) | **aperta dichiarata** — ✅ **La gamba che mancava e' arrivata**: la notifica del form e la mail delle 09:22 del 13/05 («Apro reclamo su MOD-QA-31, n. progressivo REC-2026-011») sono canonizzate dal lotto 3D. ⚠️ **Ma la scheda continua a datare l'apertura al 12/05 e nessuna fonte nuova lo spiega**, quindi la questione **non si chiude**: cambia il suo stato di prova, non il suo esito. ⚠️ **E il lotto 3D ha corretto una FALSA ASSENZA in quella nota**: dichiarava che l'archivio non conteneva la notifica automatica del form, e l'archivio la contiene |
| T7 | TMC del lotto farina MV26-0429/A: 29/12 · 04/11 · 30/10 | pilota S2 | **lotto 4** (contratto e scheda tecnica Molino Veneto) | tracciata |
| T8 | Modo di consegna dello stesso lotto: sfuso in autocisterna contro sacchi da 25 kg | pilota S2 | **lotto 4** (i due DDT) | tracciata |
| T9 | Pezzi per cartone di AF-SN-0450: 10 sulla scheda tecnica, 12 su listino e accordo quadro | **lotto 1A** — gamba acquisita: `ST-0450` rev. 4 dichiara 10 | **lotto 5** (listino v3, accordo quadro) | tracciata |
| T10 | Costo dell'energia elettrica: 0,182 €/kWh nei consumi, ~0,126 e ~0,173 ricavabili dalla bolletta, 0,205 nel CapEx | **lotto 1B** — le prime due gambe stanno **entrambe** nel lotto | **lotto 9** (CapEx linea 3) — **tre gambe, non due**; la terza **non si anticipa** (E25) | tracciata |
| T11 | Costo della non qualità gen-mag: 24.420 · 29.600 · 39.500 · 135.793 | **lotto 3** (cruscotto) | **lotto 6** (budget) — il registro NC è già canonizzato | tracciata |
| T12 | Domeniche lavorate a maggio: due, tre, o le tre della conferma d'ordine | **lotto 5** | **lotto 7** (libro unico, timbrature) | tracciata |
| T13 | Costo ingredienti di AF-SN-0470: 0,26 €/pz nel business case contro 0,5478 della marginalità | **lotto 5** | **lotto 9** (business case) | tracciata |
| T14 | Data di pagamento dell'acconto Criotech: 15/05 · 20/05 · 25-26/05 | **lotto 6** | **lotto 9** (preventivo e verbale di CdA) | tracciata |
| T15 | Impianto assicurativo: la polizza in archivio è Novaria, il report OpEx parla di Generali e AIG | **lotto 6** | **lotto 8** (polizze) | tracciata |
| T16 | Costi fissi OpEx contro i contratti minori (fotocopiatrice, antivirus, distributori) | **lotto 6** | **lotto 10** | tracciata |
| T17 | Azoto: la bolla Nordgas del 06/05 registra scarico **in serbatoio fisso** SB-AUR-01 e bombole solo di CO2; il quaderno dello stesso giorno scrive «bombola nordgas cambiata alle 16 ma durata poco» | **lotto 1A** (gamba del quaderno) | chiusa in **1C** | **RICONCILIATA** — non era una divergenza. `fatto-azoto-due-vie-serbatoio-e-rampa`: l'inventario registra **18 bombole di azoto «scorta rampa»** con nota «rampa emergenza PKM-450», quindi le bombole esistono in giacenza e non devono essere arrivate quel giorno per poter essere cambiate quel giorno. ⚠️ Che *quella* bombola venisse dalla rampa resta una lettura dichiarata, non un fatto di una fonte |
| T18 | Frigotecnica **Berica** (contratto) contro Frigotecnica **Scaligera** (scheda manutenzione), sugli stessi impianti CF-02 e TS-01 | **lotto 1A** (gamba della scheda) | chiusa in **1B** | **aperta dichiarata** — `questione-manutentore-frigo-berica-scaligera`: il contratto è l'unico documento con P.IVA e certificato F-gas, il piano di manutenzione non porta identificativi. Registrata in `alias_entita.md` classe C. ⚠️ **Terza gamba nota e non ancora canonizzata**: `elenco_interni_telefonici.txt` riga 34 scrive «manutenzione frigo Frigotecnica Berica (h24)». Quel file è del **lotto 10** (metodo_03 §1.3 esempio 18: si spalma sulle schede, non fa nota propria) e il divieto 9-bis impone di non usarlo prima: **il lotto 10 deve aggiungerlo alla questione e alla scheda entità** |
| T19 | Linea 1 in produzione domenica 10/05 su tre turni, mentre il piano della settimana 19 non la prevede | **lotto 1A** — aperta: `questione-linea1-domenica-10-05-fuori-piano` | **lotti 5 e 7** — gamba della storia «domeniche della promo», vedi T12 | tracciata |
| T20 | Base metrologica dell'arbitrato datalogger contro registro cartaceo | **lotto 1A** — **gamba trovata dove non era prevista**: la scheda di manutenzione attesta le tarature delle sonde del PT-104, nota `fatto-sonde-pt-104-in-taratura` | chiusa in **1C** | **chiusa** — `fatto-datalogger-dl-001-in-taratura`: il canale del cuore prodotto è tarato dal 28/11/2025 al 28/11/2026 da un laboratorio accreditato, incertezza ±0,15 °C. ⚠️ **La chiusura ha però aperto T44**: i due registri della metrologia del `PT-104` non concordano su date, periodicità ed esecutore |
| T21 | Sonda di conducibilità del CIP-01 con taratura scaduta dall'08/04/2026, «allarmi sonda su log maggio» | **lotto 1A** (scheda manutenzione) | chiusa in **2A** | **chiusa** — `fatto-cicli-cip-chiusi-con-sonda-guasta`: il log di maggio porta **due** `ALM_COND_PROBE OPEN_CIRCUIT`, il 14/05 e il 28/05, con lettura `-999.9` e flag `FAULT`, e in **entrambi** i casi il pannello chiude il ciclo `ESITO=PASS` lasciando in coda «VERIFICA MANUALE RICHIESTA». ⚠️ Non era una divergenza fra due fonti: la scheda di manutenzione **rimandava** al log — «sollecitato da QA - allarmi sonda su log maggio» — e il log contiene ciò che quella riga annunciava. La verifica manuale richiesta non ha riscontro in nessun grezzo |
| T22 | Manutenzioni arretrate su CF-02 (assorbimenti scaduti dal 30/04, resistenze di sbrinamento rimandate) | **lotto 1A** (scheda manutenzione) | chiusa in **1B** | **RICONCILIATA** — non era una divergenza: `fatto-anomalia-consumo-cf-02-maggio` lega l'ordine di lavoro `OdL-26-0175` della scheda alle annotazioni dei consumi, e `fatto-allarmi-alta-temperatura-cf-02-aprile` porta la gamba di aprile. ⚠️ **T30 è la stessa questione, duplicata nel seme della tabella** |
| T23 | O2 residuo in confezione: la scheda tecnica prescrive **max 1,0 %**, il quaderno applica **«lim 2%»** | **lotto 1A** | — | **aperta dichiarata** — `questione-limite-o2-residuo`. In più la scheda **non dichiara a quale momento** della vita del prodotto valga il tetto: lacuna registrata in `doc-limite-o2-residuo-af-sn-0450` |
| T24 | aw e umidità di AF-SN-0450: scheda tecnica e **rapporto di prova del laboratorio accreditato** concordano su aw ≈ 0,93 e umidità ≈ 32 g/100 g; le prove di shelf life danno 0,31 e 5,6 % | **lotto 1A** | — | **aperta dichiarata** — `questione-aw-umidita-af-sn-0450`. ⚠️ **Terza gamba dal lotto R1, e rimette in discussione l'arbitrato**: il manuale HACCP §5.1 dà per la famiglia dello snack **due** valori su **due matrici** — aw 0,30-0,40 per il prodotto, 0,90-0,94 per la farcitura in massa. Se i due numeri della divergenza misurano matrici diverse, il file delle prove non è l'anomalo e nasce invece una divergenza nuova, **manuale contro scheda tecnica sull'aw del prodotto** (0,30-0,40 contro 0,93). Il canone si accresce e la riga del 18/08 resta. ⚠️ **Il primo impianto della nota era rovesciato**: sembrava che la scheda tecnica fosse la fonte dubbia. Il ri-giudizio ha segnalato l'esistenza del rapporto di prova, che misura lo stesso lotto con metodo normato e dichiara **conformi** i valori della scheda. L'anomalia sta nel file delle prove, che è la base della proposta di TMC a sei mesi |
| T25 | Convalida annuale dell'`MD-3200`: la scheda di manutenzione la data al `06-feb-26` con scadenza `06/02/27`; l'elenco tarature dà altre date | **lotto 1A** | chiusa in **1C** | **aperta dichiarata** — `questione-convalida-md-3200-due-registri`: `06-feb-26` → `06/02/27` e frequenza 12 mesi contro `04/03/2026` → `04/09/2026`, cioè semestrale. Cambia il mese e la durata della copertura |
| T26 | Kit dei tasselli di prova del CCP3: `TL-114` sul MOD-QA-07, `TST-CERT-KIT` sulla scheda di manutenzione, e una terza sigla nell'elenco tarature | **lotto 1A** — confronto dichiarato in `macchina-md-3200`, senza aprire una questione con due sole gambe deboli | chiusa in **1C** | **aperta dichiarata** — `questione-sigla-kit-tasselli-ccp3`, e le sigle sono **quattro**, non tre: alla terza dell'elenco (`TT-001`/`TT-002`/`TT-003`, tre certificati distinti) si aggiunge `KIT-MD-05` dell'inventario di magazzino, che era già nel vault e nessuno aveva confrontato |
| T27 | Materiale della guarnizione **originale** della valvola azoto: PTFE (mail del costruttore), FKM (manuale della macchina), EPDM (piano di manutenzione) | **lotto 1A** — `questione-materiale-guarnizione-pkm-450` estesa | — | **aperta dichiarata**: due fonti su tre danno un fluoropolimero, la terza no, e nessun documento le mette a confronto |
| T28 | Codice del ricambio della valvola azoto: le sigle salgono da due a **quattro**, e due vengono dal costruttore stesso | **lotto 1A** — `questione-codice-ricambio-valvola-pkm-450` estesa | — | **aperta dichiarata** |
| T29 | Sonda di conducibilità del `CIP-01`, taratura scaduta dall'`2026-04-08`, «allarmi sonda su log maggio» | **lotto 1A** (scheda manutenzione) | chiusa in **2A** | **chiusa** — **duplicato di T21**, stessa questione con altre parole: il seme della tabella la conteneva due volte, come già per T22 e T30. Nessuna riga sparisce, si dichiara la duplicazione, e l'esito è quello di T21 |
| T30 | Assorbimenti del compressore `CF-02` scaduti dal `30/04/26` e resistenze di sbrinamento rimandate, con «assorbimento anomalo segnalato 08/05» | **lotto 1A** (scheda manutenzione) | chiusa in **1B** | **RICONCILIATA** — **duplicato di T22**, stessa questione con altre parole: il seme della tabella la conteneva due volte (come T21 e T29). Nessuna riga sparisce, si dichiara la duplicazione. ⚠️ **Allineata a T22 il 19/08/2026**: usciva come «chiusa» mentre la riga di cui è dichiarata duplicato usciva come «riconciliata», e la stessa questione con due esiti diversi indebolisce proprio la tabella con cui al gate finale si provano i conflitti. L'esito vero è quello di T22: non era una divergenza |
| T31 | Proposta di R&D di portare il TMC a **sei mesi** contro i **45 giorni** della scheda tecnica in vigore | **lotto 1A** — registrata in `kpi-shelf-life-af-sn-0450` | **lotto 9** (R&D), se il corpus porta la revisione | tracciata — non è una contraddizione fra documenti: è una proposta contro una specifica in vigore |
| T32 | Posizione dell'`MD-3200` in linea: la scheda tecnica lo colloca **fra il raffreddamento e il confezionamento**, l'elenco attrezzature lo dà «Linea 1 - post confezionamento» | **lotto 1A** — trovata dallo strato di giudizio, che ha visto la nota affermare il contrario della propria fonte | chiusa in **1C** | **aperta dichiarata** — `questione-posizione-md-3200-in-linea`: la colonna `Ubicazione` dell'elenco dà «Linea 1 - post confezionamento». Cambia l'oggetto del controllo, e in una delle due letture ricadrebbe nel campo del metal detector anche ciò che entra **durante** il confezionamento |
| T33 | Il rapporto di prova del laboratorio contiene **prove chimico-fisiche** sul lotto L26130 che nessuna nota del pilota aveva canonizzato: aw, pH, umidità, cloruri, con metodo e incertezza | **lotto 1A** — trovato dal ri-giudizio | il grezzo appartiene alla fetta pilota: la lacuna di copertura si chiude qui, non in un lotto futuro | **chiusa** — le prove sono ora citate da `questione-aw-umidita-af-sn-0450` |
| T35 | La non conformità `NC-2026-067` del 10/04 attribuisce al tunnel `TS-01` sbrinamenti ricorrenti che il log dello stesso mese registra solo sulla cella `CF-02` | **lotto 1B** | — | **aperta dichiarata** — `questione-nc-067-sbrinamenti-tunnel` |
| T36 | L'azione correttiva di `NC-2026-017`, chiusa il 03/02, sposta gli sbrinamenti in fascia notturna; ad aprile sono distribuiti sulle ventiquattro ore | **lotto 1B** | — | **aperta dichiarata** — `questione-sbrinamenti-fascia-notturna-cf-02`. È la divergenza che nessuna nota aveva visto: l'ha trovata il revisore |
| T37 | L'azione correttiva di `NC-2026-114` del 30/05 «riduce» a cinque minuti l'allarme di porta aperta, che il 15/04 era già a `LIM=00:05:00` | **lotto 1B** | — | **aperta dichiarata** — `questione-limite-allarme-porta-cf-02` |
| T38 | Incremento dell'energia da aprile a maggio: **+9,4 %** nel riepilogo contabile contro **+5,4 %** ricavabile dal grafico dei dodici mesi della stessa fattura | **lotto 1B** | le fatture di aprile, che in archivio non ci sono | **aperta dichiarata** — `kpi-incremento-energia-maggio-su-aprile`. Incoerenza **intra-file**: si dichiara, non si sceglie |
| T39 | Il **terzo quasi-omografo Peruffo**: Attilio Peruffo, legale rappresentante del manutentore frigorista, accanto a Peruffo Maria Grazia e Peruzzi Maurizio | **lotto 1B** — registrato in `alias_entita.md` classe B | **lotto 6** (visura e bilancio): alla nascita delle schede dei due revisori, la riga «Da non confondere con» va scritta su tutte e tre | tracciata — un rimando non può nascere prima della nota che punta ⚠️ **AGGIORNATA al gate del lotto 3D (24/08/2026), dal censimento degli obblighi del canone (E62): LA FAMIGLIA NEL VAULT È QUATTRO, non tre.** Il lotto 3B ha portato **Peruzzi Erika**, operaia di Linea 2 (canone, sezione 23/08/2026, **E13**), e l'obbligo per il lotto 6 vale quindi su **tutte e quattro** le schede. ⚠️ **E nel corpus i quasi-omografi sono SEI**: `PERUZZI Loris` e `Peruzzi Luciano` stanno in due grezzi non canonizzati, e **chi li porta li registra in classe B** — non si uniscono mai |
| T40 | La **cella surgelati del magazzino di Via Palù 3/A** è il quarto impianto frigorifero, in un secondo sito, escluso dall'oggetto del contratto per la garanzia dell'installatore fino a novembre 2026 | **lotto 1B** — dichiarata in `fatto-cariche-f-gas-impianti-frigoriferi` | gamba aggiunta in **1C**; restano i lotti che portano manuale HACCP e rilievi di audit | tracciata — **gamba acquisita**: i tre strumenti del Palù sono tutti `SCADUTO` (`fatto-strumenti-taratura-scaduta-in-uso`), e il verbale ATS pag. 3 §1.7 tratta il deposito come **unità locale separata**, non ispezionata quel giorno. ⚠️ Il secondo sito **non ha ancora una nota padrona**: i due grezzi di 1C non lo descrivono, lo nominano soltanto |
| T41 | Il **metano dei forni** non ha una fattura in archivio: il consumo è misurato solo dai contatori interni | **lotto 1B** — `kpi-metano-forni-maggio-2026` | **lotto 6** o **lotto 10**, se il corpus porta una fattura gas | tracciata |
| T42 | Lo sbrinamento della cella `CF-02` del 24/04: il piano di manutenzione lo dà a «interno (Bissoli)», il log della centralina a un operatore esterno in sessione di assistenza | **lotto 1B** — dichiarata dentro `fatto-assistenza-esterna-24-04-cf-02`, con entrambe le fonti citate | — | **aperta dichiarata** — ⚠️ **senza nota-questione propria**: il fatto padrone è l'intervento del 24/04, e «un fatto, un padrone» vale anche per le divergenze che lo riguardano. Se il titolare preferisce una questione a sé, la nota si scorpora in due minuti |
| T43 | Il metal detector `MD-1800` della Linea 3: `SCADUTO` dal `03/04/26` nel piano di manutenzione, `Conforme` e `IN USO` fino al `19/08/2026` nell'elenco attrezzature | **lotto 1C** | — | **aperta dichiarata** — `questione-convalida-md-1800-scaduta-o-valida`. Non sono due date per lo stesso intervento: sono **due stati opposti dello stesso punto critico** |
| T44 | La metrologia del `PT-104` censita due volte: sonde ogni 3 e 6 mesi da Analytica Veneta nel piano di manutenzione, quattro canali del datalogger ogni 12 mesi da CalService nell'elenco attrezzature | **lotto 1C** | — | **aperta dichiarata** — `questione-due-registri-tarature-pt-104`. Nessuna fonte dichiara se le voci del piano e le matricole dell'elenco siano lo stesso strumento |
| T45 | Il verbale dell'ispezione sanitaria attesta per il termoregistratore `CF-02` una taratura al `12/02/2026` che nessuno dei tre strumenti dell'elenco porta | **lotto 1C** | — | **aperta dichiarata** — `questione-taratura-termoregistratore-cf-02`. ⚠️ Specie nuova: uno dei due termini è un'attestazione resa **all'autorità** |
| T46 | Tre codici di lotto e due numeri di documento di trasporto per la stessa consegna di azoto del 06/05 | **lotto 1C** | — | **aperta dichiarata** — `questione-codici-lotto-azoto-06-05`: `LOT-N-260502` su DDT `26/04512`, `NG-26-0506` su DDT `BN-4471`, `NG26-0644` |
| T47 | Quantità e livello del serbatoio di azoto del 06/05: `2.350` m³ e livello `87 %` sulla bolla, 2.310 m³ e «livello 68%» sull'inventario | **lotto 1C** | — | **aperta dichiarata** — `questione-azoto-quantita-e-livello-06-05` in `data\`. L'inventario **attribuisce alla bolla** un livello che la bolla non contiene |
| T48 | La ritaratura del flussimetro azoto del 04/05, dichiarata chiusa dalla `NC-2026-082`, non compare nel registro degli strumenti, che per `CV-003` si ferma al 16/12/2025 | **lotto 1C** — dichiarata dentro `fatto-strumenti-map-azoto-pkm-450` | — | **aperta dichiarata** — è la famiglia isolata in 1B (**azione correttiva che il dato non conferma**), applicata a uno strumento |
| T49 | Costo della taratura dei due metal detector: il report OpEx scrive «1.240 €» per `MD-3200` e `MD-1800` insieme, il piano di manutenzione dà 850,00 € + 180,00 € per il solo `MD-3200` | **lotto 1C** — vista in ricerca, **non scritta** in nessuna nota (E25) | **lotto 6** (report costi fissi OpEx) | tracciata |
| T50 | Il cruscotto KPI qualità conta «taratura strumenti scaduta» fra le voci del costo della non qualità, con 4 eventi e 1.200 € | **lotto 1C** — vista in ricerca, **non scritta** (E25) | **lotto 3** (cruscotto) | tracciata — è la gamba economica degli strumenti scaduti di `fatto-strumenti-taratura-scaduta-in-uso` |
| T51 | La notifica di ispezione ATS annota «taratura sonde e verifica md-3200: certificati ok, ma il rapporto dell'ultima verifica…» | **lotto 1C** — vista in ricerca, **non scritta** (E25) | **lotto 3** (notifica ATS) | tracciata — terza gamba possibile su T25 e T45 |
| T52 | Il registro di carico/scarico MOCA registra l'11/02/2026 quattro **pacchi bombole** di azoto E941 da Nordgas | **lotto 1C** — vista in ricerca, **non scritta** (E25) | **lotto 2** (registro MOCA) | tracciata — è una gamba in più sulle due vie dell'azoto, che 1C ha chiuso con l'inventario |
| T53 | Il «registro a parte» delle verifiche con sali saturi dell'aw-metro: il quaderno del tecnologo registra una verifica del 06/05/26 con soluzione satura di NaCl | **lotto 1C** — vista in ricerca, **non scritta** (E25) | **lotto 9** (quaderno di laboratorio) | tracciata |
| T54 | Quanto azoto è stato ordinato: l'ordine `OA-26-0160` dà 3.500 m³ a 0,38 €/m³, chiuso il 06/05 | **lotto 1C** — vista in ricerca, **non scritta** (E25) | **lotto 6** (ordini d'acquisto aperti) | tracciata — terza gamba su T47 |
| T34 | Le note F-gas del contratto frigo nascono in `area: manutenzione`, perché è l'area che governa quei fatti oggi e **le note non traslocano** | **lotto 1B** — decisione del titolare del 19/08/2026 | **lotto 8**, alla nascita di `area-sicurezza-ambiente`: l'hub nuovo le **linka come rimandi laterali**, il `related` principale resta l'hub di manutenzione (E11) | tracciata — non è una divergenza dell'archivio: è un impegno di grafo che il lotto 8 deve onorare |
| T55 | **Il manuale HACCP chiama `PRO-QA-08` la procedura di RINTRACCIABILITÀ**, mentre in archivio esiste un grezzo `PRO-QA-08_gestione_reclami_cliente_rev2.docx`: la stessa sigla su due procedure diverse | **lotto R1** — vista in riconciliazione verticale, **non scritta in nessuna nota** (E25: una sola gamba canonizzata) | **lotto 3**, che porta il grezzo `PRO-QA-08` | tracciata — ⚠️ **obbligo esplicito per il lotto 3**: al momento di canonizzare quel file va confrontata la sigla con quella che il manuale HACCP assegna alla rintracciabilità, e la divergenza va aperta o spiegata. Finché la seconda gamba non è nel vault, non se ne scrive nulla |
| T56 | **Sei fonti prescrittive del lotto 2 riguardano note già scritte**: `IO-05` lavaggio CIP, scheda di sicurezza del detergente acido, scheda allergeni, capitolato imballaggi, DoC MOCA, piano di autocontrollo dell'acqua | **lotto R1** — elencate in `06_operativoonti_prescrittive_corpus_v1.md`, **non citabili** perché il loro lotto non è canonizzato | **2A** le prime due · **2B** e **2C** le altre quattro | tracciata — ⚠️ **le prime due sono entrate in 2A**, ed è il primo impiego di E37: `candidate_r1.py --dominio cip` ha riaperto **10** note, **4 corrette** e 6 chiuse dichiarando che la fonte non le governa. Restano da onorare in **2B** (scheda allergeni, piano acqua) e in **2C** (capitolato imballaggi, DoC MOCA) ✅ **Il piano dell'acqua è entrato in 2B il 20/08/2026** e la sua riconciliazione verticale è stata fatta: `candidate_r1.py --dominio acqua` ha riaperto **5** note, **3 corrette** e 2 chiuse dichiarando che la fonte non le governa. ⚠️ **La scheda allergeni NON è entrata in 2B**: il lotto si è spezzato in apertura (E28) e la scheda è passata a **2B-bis**, col suo dominio `allergeni` già dichiarato in `candidate_r1.py` e **5 note candidate** già misurate. Restano da onorare: **2B-bis** (scheda allergeni) e **2C** (capitolato imballaggi, DoC MOCA) |
| T57 | **Tre fonti prescrittive del lotto 3**: `PRO-QA-08` gestione reclami, procedura di ritiro e richiamo, politica per la qualità e la sicurezza alimentare | **lotto R1** — non citabili, lotto non canonizzato | **lotto 3** | tracciata — ⚠️ **obbligo esplicito per il lotto 3**: le note del reclamo `REC-2026-011` — data di apertura, misura del frammento, blocco cautelativo, relazione al cliente — vanno riagganciate alla procedura che le prescrive. Oggi si appoggiano al solo §10.4 del manuale HACCP |
| T58 | **Quattro fonti prescrittive del lotto 4**: contratto di fornitura Molino Veneto firmato, scheda tecnica della farina tipo 0, listino del fornitore, tariffe dei vettori terzi | **lotto R1** — non citabili, lotto non canonizzato | **lotto 4** | tracciata — ⚠️ **obbligo esplicito per il lotto 4**: `lotto-mv26-0429a` e `questione-tmc-farina-mv26-0429a` discutono TMC e modo di consegna senza la fonte che li prescrive. La scheda tecnica della farina è il termine prescrittivo mancante delle due questioni aperte dal pilota |
| T59 | **Due fonti prescrittive del lotto 5**: accordo quadro private label firmato e listino GDO rev. 3 in vigore | **lotto R1** — non citabili, lotto non canonizzato | **lotto 5** | tracciata — ⚠️ **obbligo esplicito per il lotto 5**: `fatto-richiesta-relazione-48-ore` afferma che il cliente «attiva l'articolo dell'accordo quadro» e richiama la clausola risolutiva, ma l'accordo non è citabile: alla canonizzazione del lotto 5 quella nota va riaperta e agganciata all'articolo vero |
| T60 | **Quattro fonti prescrittive del lotto 7**: job description del responsabile di produzione, piano turni degli apprendisti, calendario di reperibilità, circolare INPS | **lotto R1** — non citabili, lotto non canonizzato | **lotto 7** | tracciata — ⚠️ **obbligo esplicito per il lotto 7**: le note che assegnano responsabilità di processo — chi conduce la linea, chi firma, chi è reperibile — oggi si appoggiano al solo manuale HACCP. La job description è la seconda gamba, e va confrontata con i ruoli che il manuale assegna ai punti critici |
| T61 | **Cinque fonti prescrittive del lotto 8**: estratto del DVR, autorizzazione unica ambientale, certificato di prevenzione incendi, polizza RCT/RCO, polizza RC prodotto | **lotto R1** — non citabili, lotto non canonizzato | **lotto 8** | tracciata — ⚠️ **obbligo esplicito per il lotto 8**: nessuna nota del vault tocca oggi limiti di scarico, misure di prevenzione o massimali; quando il lotto 8 le porterà, le note di manutenzione e impianti già scritte vanno riguardate contro quelle prescrizioni |
| T62 | **Due fonti prescrittive del lotto 9**: specifiche dell'ingrediente nuovo dichiarate dal fornitore e formulazione della ricetta in prova | **lotto R1** — non citabili, lotto non canonizzato | **lotto 9** | tracciata — ⚠️ **obbligo esplicito per il lotto 9**: la proposta di R&D di portare il TMC a sei mesi va confrontata con la shelf life di 45 giorni che **scheda tecnica e manuale HACCP dichiarano concordi**, e la referenza con il sesamo obbliga a un riesame pre-lancio che il manuale prescrive |
| T63 | **Due fonti prescrittive minori del lotto 10**: contratto di noleggio dei distributori e contratto copie della fotocopiatrice | **lotto R1** — non citabili, lotto non canonizzato | **lotto 10** | tracciata — nessuna nota del vault dipende da queste due: si tracciano per completezza dell'elenco delle fonti prescrittive, non per un obbligo di riconciliazione |
| T64 | **La taratura del datalogger del CCP2 è semestrale o annuale?** Il manuale HACCP prescrive la taratura semestrale delle sonde del CCP2; il registro degli strumenti dà i quattro canali del datalogger — di cui uno marcato «registrazione automatica CCP2» — con periodicità annuale | **lotto R1** — divergenza VERTICALE, entrambe le gambe canonizzate | — | **aperta dichiarata** — `questione-periodicita-taratura-canali-datalogger-ccp2`. ⚠️ Specie nuova per questa tabella: non è un registro contro un altro registro, è **un registro contro la fonte che prescrive**. Che il canale di un acquisitore ricada nella voce «sonde» del manuale è dichiarato come lettura, non come dato di una fonte |
| T65 | **Il manuale HACCP dichiara rimosso il carrello ricambi, e tre documenti successivi lo trovano ancora in linea**: la revisione dell'08/04/2026 scrive «il carrello ricambi di linea è stato rimosso», la `NC-2026-089` del 10/05 dà come causa radice «carrello ricambi ancora in area produttiva nonostante chiusura NC audit», e il verbale dell'ispezione del 09/06 chiude con una diffida | **lotto R1** — revisione col canone, entrambe le gambe canonizzate | — | **aperta dichiarata** — `questione-carrello-ricambi-dichiarato-rimosso`. ⚠️ **Specie nuova**: è la famiglia isolata in 1B — *un'azione correttiva registrata che il dato non conferma* — applicata al **manuale di autocontrollo**, cioè al documento prescrittivo di vertice. Riga aggiunta al canone in sezione datata |
| T66 | **La validazione del CCP2 potrebbe essere scaduta, e il manuale lo chiede a sé stesso**: §8.1 prescrive «challenge test/validazione trattamento ogni 3 anni», §11.3 dichiara l'ultima del 2021 e lascia dentro il testo «rivalidazione eseguita? vedi verbale team 03/2024» | **lotto R1** — revisione col canone; incoerenza **intra-file** su un documento prescrittivo | il **verbale del Team HACCP del 03/2024**, che in archivio non c'è | **aperta dichiarata** — `questione-validazione-ccp2-mai-confermata`. La nota interrogativa è sopravvissuta alla revisione dell'08/04/2026, quindi è stata riletta e riapprovata così com'è. Riga aggiunta al canone in sezione datata |
| T67 | **Il detergente acido del CIP ha due identità**: `IO-05` prescrive `CHEMIFOOD AN-15`, «Acido nitrico 15%»; l'unica scheda di sicurezza in archivio è quella dell'`ACIDFOOD CIP 25`, cod. `CF-AC-025`, nitrico al 20-25 % più fosforico. Stesso fornitore, e nessuna delle due sigle compare nell'altro documento | **lotto 2A** | — | **aperta dichiarata** — `questione-prodotto-acido-cip-an-15-o-acidfood-25`. ⚠️ **Pesa oltre sé stessa**: se i due documenti non parlano dello stesso prodotto, l'archivio non ha la scheda di sicurezza del prodotto in uso, e ogni confronto fra le due fonti — DPI, concentrazioni, temperature — perde il presupposto. Servirebbe il registro SDS del reparto CIP o un documento d'acquisto |
| T68 | **Due prescrizioni in vigore sui DPI dell'acido**: `IO-05` §2 impone guanti in neoprene e semimaschera con filtro `B-P2`; la scheda di sicurezza §8.2 prescrive guanti in butile o fluoroelastomero classe 6 e facciale con filtro tipo `E` | **lotto 2A** | il **DVR** (lotto 8), par. 6.3 sul rischio chimico, che l'annotazione dell'RSPP cita e l'archivio non contiene | **aperta dichiarata** — `questione-dpi-cip-due-prescrizioni`. ⚠️ **Obbligo esplicito per il lotto 8**: quando il DVR entra nel vault, questa questione va riaperta e confrontata col suo par. 6.3 |
| T69 | **La verifica del lavaocchi di sala CIP: settimanale o mensile?** La scheda di sicurezza §8.2 la prescrive settimanale; `IO-05` §3 incorpora l'annotazione del capo officina, «ogni primo lunedì del mese» | **lotto 2A** | il registro delle verifiche del lavaocchi, che l'annotazione dichiara esistente e l'archivio non contiene | **aperta dichiarata** — `questione-frequenza-verifica-lavaocchi-cip`. ⚠️ Specie particolare: non è una regola contro una regola, è **una regola contro una prassi**, e il documento verificato dall'RSPP incorpora la seconda senza segnalare la prima |
| T70 | **Il registro CIP cartaceo non è in archivio**, e `IO-05` §7 vi impone cinque registrazioni per ciclo più la seconda firma del capoturno, dichiarando che «un registro senza seconda firma è una non conformità» | **lotto 2A** — assenza verificata su tutto `sources\`, manifest v1.1 | nessun lotto lo porta: non è nella matrice | tracciata — non è una divergenza ma una **lacuna dell'archivio** che tocca una prescrizione forte: il tracciato del pannello registra orari e allarmi ma **non porta nessuna firma**, e la conformità alla seconda firma sul CIP non è verificabile su questo corpus |
| T71 | **`MOD-QA-19`, il piano di monitoraggio dei tamponi di superficie**, è prescritto da `IO-05` §8 come quarto criterio di accettazione del lavaggio — «di norma 2 punti a settimana per linea, di più dopo le produzioni con allergeni» | **lotto 2A** | **lotto 2B**, che porta il registro dei tamponi | **aperta dichiarata** — ✅ **l'obbligo è stato onorato il 20/08/2026**: il registro è canonizzato ([[doc-piano-tamponi-superfici]], `kpi-tamponi-superfici-2026`) e il confronto con la frequenza prescritta è stato fatto **da script**, non a occhio. ⚠️ **Non coincidono, e la divergenza non è di volume ma di ritmo**: 6 settimane su 20 hanno un prelievo, e la Linea 1 supera il volume prescritto (58 prelievi-punto contro 40) perché li concentra in una campagna al mese, mentre le Linee 2 e 3 restano a 15 su 40. La questione resta **aperta** perché `IO-05` non dice se «2 punti a settimana» sia un minimo di volume o una cadenza, e la clausola «di norma» non ha né deroga scritta né chi la firmi: `questione-frequenza-tamponi-prescritta-e-reale`. ✅ La seconda metà dell'obbligo è **soddisfatta**: i punti coprono la Linea 1 dopo i lavaggi di maggio (campagne dell'11/05, del 13/05 e del 25/05). ⚠️ Il «di più dopo le produzioni con allergeni» **non è verificabile** su queste fonti — serve il programma di produzione — e passa al lotto che lo porta |
| T72 | **Il criterio di conducibilità di `IO-05` è DIFFERENZIALE e il suo termine di paragone non era nel lotto 2A**: «≤ 50 µS/cm sopra il valore dell'acqua di rete», e il log del CIP non misura mai l'acqua di rete | **lotto 2A** — la conducibilità di rete era stata **vista in ricerca e NON scritta** (E25) | **lotto 2B**, che porta il piano di autocontrollo dell'acqua potabile | **chiusa il 20/08/2026** — ✅ il termine mancante è entrato nel vault: **486 µS/cm** alla rete d'ingresso, 15/01/2026 (`kpi-conducibilita-acqua-per-punto`), e il limite diventa **536 µS/cm**. Applicato ai cicli di maggio, risulta **superato in 18 cicli su 28** se fa fede l'ultima lettura del risciacquo e in **24** se fa fede la più alta: `fatto-criterio-conducibilita-cip-superato`, e la nota di 2A che dichiarava il criterio non verificabile è stata riaperta e corretta. ⚠️ **La chiusura porta con sé tre condizioni dichiarate**, e vanno lette con il numero: la risoluzione del log è di 100 µS/cm contro una tolleranza di 50; il valore della rete è **una misura sola, di gennaio**, contro un log di maggio; e l'acqua che il registro dice destinata al CIP è quella dell'addolcitore, 512 µS/cm — che darebbe 562 e **lo stesso conteggio**. ⚠️ È la prima riga di tracciamento del progetto **chiusa da un lotto successivo con un dato, non da una decisione** |
| T73 | **Chi era abilitato a condurre i lavaggi CIP di maggio?** `IO-05` subordina l'avvio del ciclo alla formazione registrata su `MOD-HR-11`, e il log porta tre sigle di operatore — `BISSOLI_M`, `POPESCU_I`, `DALMASO_I` — che nessuna delle fonti del lotto 2A collega a una persona abilitata | **lotto 2A** — il registro di formazione è stato **visto in ricerca e NON scritto** (E25): il grezzo che lo contiene appartiene al lotto 8 | **lotto 8**, che porta il verbale della formazione | tracciata — ⚠️ **obbligo esplicito per il lotto 8**: al momento di canonizzare quel verbale va confrontato l'elenco degli abilitati al CIP con le sigle che compaiono nel log di maggio, e la divergenza va aperta o spiegata. ⚠️ Finché la seconda gamba non è nel vault non se ne scrive nulla, nemmeno in forma attenuata: `fatto-abilitazione-obbligatoria-cip` dichiara soltanto che **le proprie fonti** non dicono chi fosse abilitato |
| T74 | **Gli strumenti del CIP-01 non stanno tutti nello stesso registro**: la sonda di conducibilità `COND-S7` è nel piano di manutenzione (riga 57, `SCADUTO` dall'`2026-04-08`) ma **non** nell'elenco delle attrezzature, dove per il `CIP-01` compaiono solo i due manometri; e il **misuratore di portata** che produce le 170 letture `FT_CIP` non compare in **nessuno** dei due registri | **lotto 2A** — vista in ricerca, **non scritta in nessuna nota** | il **prossimo lotto che tocca la metrologia**, o il lotto di manutenzione di fine corsa | tracciata — ⚠️ È la famiglia **«due registri paralleli della metrologia»** isolata nel lotto 1C (T44) applicata al `CIP-01`: stessi due registri, stessa discordanza di censimento, su strumenti che misurano un criterio di accettazione. Uno strumento che non è in nessun registro di taratura non ha una scadenza da rispettare. ⚠️ **Perché non si scrive qui**: la nota nascerebbe dopo la generazione del pacchetto del terzo giro, e non vedrebbe mai il giudizio — è il buco che E9 vieta. Si scrive nel lotto che la potrà far giudicare |
| T75 | **L'atto che prescrive l'autocontrollo dello scarico non è canonizzato**: il file delle acque reflue dichiara di rispondere a «AUA Det. Provincia di Verona n. 987/2019 - prescrizione A.5 punto 2 - frequenza trimestrale» e di recepirne i limiti in sez. A.4, ma l'autorizzazione sta in un grezzo di un altro lotto | **lotto 2B** — la nota registra **che il file dichiara di rispondervi**, non che cosa l'atto prescriva (limite di E29) | **il lotto che porta `AUA_autorizzazione_unica_ambientale_scarichi.pdf`** | tracciata — ⚠️ **obbligo esplicito**: alla canonizzazione dell'AUA va verificato che i dodici limiti applicati siano quelli dell'atto, che la frequenza trimestrale sia quella prescritta, e che cosa dica sui «limiti più restrittivi del regolamento Acque Veronesi» che il file nomina senza riportarli |
| T76 | **Una sigla di non conformità con due formati e due oggetti**: il registro dei tamponi apre `NC-26-055` l'11/05/2026 sul nastro del forno; una sigla omologa in formato esteso compare in un grezzo **non ancora canonizzato**, con un oggetto diverso | **lotto 2B** — per E25 la nota del nastro **non scrive nulla** dell'altra sigla: una divergenza con una sola gamba canonizzata vive solo qui | **lotto 2B-bis**, che porta la scheda allergeni | tracciata — ⚠️ **obbligo esplicito per 2B-bis**: al momento di canonizzare la scheda va confrontata la numerazione delle non conformità e, se le due sigle designano eventi diversi nello stesso anno, si apre la questione |
| T77 | **Il dubbio del compilatore sul modulo di chiusura di `NC-ACQ-26-01`**: «su `MOD-QA-31`? no, registro NC qualità (refuso, verificare modulo giusto con Marchetti)» | **lotto 2B** | **già in archivio** — il manuale HACCP §10.4 assegna `MOD-QA-31` ai **reclami**, e il registro delle non conformità dichiara nel proprio titolo di essere `MOD-QA-18` rev. 3 | **riconciliata** — ✅ **sciolta per intero il 20/08/2026**, e in due tempi: il manuale dice che cosa `MOD-QA-31` **non** è, il registro delle non conformità dichiara la propria sigla. ⚠️ **La seconda metà l'ha trovata lo strato di giudizio al secondo giro**, non la scrittura: la nota dichiarava la sigla ignota, e il giudice ha segnalato che stava nel titolo di un documento del pacchetto. `fatto-modulo-nc-acqua-riconciliato`. ⚠️ **Resta non affermato** che la chiusura vi sia stata registrata: nel registro non c'è nessuna voce con quella sigla |
| T78 | **La conducibilità dell'acqua di rete è misurata una volta sola in tutto l'archivio** — 15/01/2026 — e non è misurata affatto sull'utenza `CIP-01` né sul produttore di ghiaccio | **lotto 2B** | **nessun lotto la porta**: è un'assenza dell'archivio, non di un lotto | tracciata — ⚠️ È il **denominatore** del criterio di accettazione del risciacquo CIP (T72): un criterio differenziale verificato contro un bianco annuale. Da segnalare al gate finale come **limite strutturale del corpus**, non come difetto di una nota |
| T79 | **Un dato dovuto e mai arrivato**: gli `Enterobacteriaceae` sullo scivolo `MD-3200` dell'11/05/2026 hanno risultato ed esito vuoti, con nota «dato non pervenuto dal lab sollecitato» | **lotto 2B** | **nessuna fonte in archivio lo porta**: nessun rapporto successivo integra il referto `AV-26/0218` | **aperta dichiarata** — la nota è `fatto-lettura-mancante-registro-tamponi`, `stato: aperto`. ⚠️ Cade nella campagna che apre due non conformità di zona 1 sulla stessa linea |
| T80 | **Il rifacimento della tubazione dell'ala spogliatoi è segnalato e il suo esito è ignoto**: «Programmare rifacimento tubazione ala spogliatoi nel piano investimenti (segnalato a Fantin)», dopo il superamento del ferro di aprile | **lotto 2B** | **il lotto che porta il piano investimenti** (tema 9, ricerca e investimenti) | tracciata — ⚠️ **obbligo esplicito**: alla canonizzazione del piano investimenti va cercato se la voce ci sia entrata. È il secondo caso del lotto in cui una segnalazione è documentata e il suo esito no — l'altro è la frequenza di pulizia del degrassatore |
| T81 | **L'entità `Analytica Veneta` nasce in 2B, ma cinque note anteriori la nominano senza collegarvisi**: prove su reclami e tarature scritte nei lotti precedenti | **lotto 2B** — la scheda entità è nuova, e la tabella `alias_entita.md` prescriveva già lo slug | **lotto di manutenzione (E35)**, non un lotto di canonizzazione | tracciata — ⚠️ **Non si è ricucito in questo lotto per scelta**: aggiungere il rimando a cinque note fuori tema sarebbe tappezzeria (divieto 25) e le farebbe entrare nel perimetro senza che il lotto le abbia lette. È debito di manutenzione, e si sana con le altre riaperture |
| T82 | **Una positività a Listeria che sta in un registro e non nell'altro**: il registro delle non conformità apre `NC-2026-034` il 24/02/2026 — «Positivita Listeria spp. su tampone ambientale zona scarico Linea 3», gravità **critica** — e il registro dei tamponi `MOD-QA-19` non porta nessun prelievo in quella data né quel risultato | **lotto 2B** — trovata dallo strato di giudizio al secondo giro, non dalla scrittura | **entrambe le gambe sono già canonizzate**: il registro NC dal lotto 1A, il registro tamponi da questo | **aperta dichiarata** — `questione-listeria-24-02-non-nel-registro-tamponi`. ⚠️ **Non è una divergenza fra valori: è un evento che un registro ha e l'altro no**, e le spiegazioni possibili — prelievo fuori piano, specie diverse (`Listeria spp.` contro `Listeria monocytogenes`), registro incompleto — nessuna fonte dell'archivio le distingue. ⚠️ **Pesa sul conteggio dell'anno**: chi guardasse il solo `MOD-QA-19`, come farebbe un auditor, vedrebbe una positività invece di due |
| T83 | **Un auditor CSQA in stabilimento sette giorni prima delle date certificate**: il registro dei tamponi annota «prelievo in presenza auditor CSQA prova a campione» sulla campagna del **10/02/2026**, il verbale dell'audit dà **17-18/02/2026** | **lotto 2B** — trovata dalla **revisione col canone**, non dalla scrittura | **entrambe le gambe sono canonizzate**: il verbale dell'audit da un lotto precedente, il registro dei tamponi da questo | **aperta dichiarata** — ⚠️ **nessuno dei due documenti prevale e l'archivio non scioglie**: o c'è stata una presenza CSQA una settimana prima, o la campagna di febbraio è datata male — **ed è l'unica del file in grafia `aaaa-mm-gg`** — o l'annotazione è finita sulla riga sbagliata. Canone, sezione 21/08/2026, rilievo B1 ⚠️ **Cercata nel lotto 3C, e NON si scioglie: resta aperta dichiarata.** I quattro documenti dell'ente — certificato, rapporto d'audit, conferma d'incarico, catena di mail — **non nominano il 10/02/2026 in nessuna forma**, ne' parlano di prelievi o tamponi in presenza di auditor. Verificato da script sul testo di cantiere dei quattro grezzi il 22/08/2026. ⚠️ **L'unico documento che potrebbe scioglierla e' il rapporto `AU-2026-0233` della piattaforma BRCGS, che non e' quello in archivio** (`questione-data-di-emissione-del-rapporto-di-audit`) |
| T84 | **Un tampone di superficie fuori limite che `MOD-QA-19` non contiene**: `NC-2026-005` del 13/01/2026, «Tampone superficie **impastatrice IMP-300** oltre limite CBT», con azione «tampone di verifica `MOD-QA-19`» | **lotto 2B** — dalla revisione col canone | **entrambe canonizzate**: registro NC dal lotto 1A, registro tamponi da questo | **aperta dichiarata** — ⚠️ **Pesa più della gemella del 24/02 (T82)**: l'evento cade **nello stesso giorno di una campagna registrata**, e `IMP-300` non compare fra i 21 punti dell'anno. Indebolisce la spiegazione «prelievo straordinario fuori piano». Canone, rilievo B2 |
| T85 | **`NC-2026-034` dichiara due azioni che il registro dei tamponi non conferma**: «ritampone a 48 h negativo» e «aumento frequenza `MOD-QA-19`», su una non conformità di gravità **critica** chiusa in quattro giorni | **lotto 2B** — dalla revisione col canone | **entrambe canonizzate** | **aperta dichiarata** — ⚠️ Il registro **non porta nessun prelievo il 26/02** e **non mostra alcun infittimento** né a marzo né ad aprile: l'unico passaggio a frequenza quindicinale è di **maggio**, e il registro lo motiva con la positività di **aprile**. È la famiglia già isolata in 1B — *un'azione correttiva registrata che il dato non conferma* — applicata al piano di monitoraggio ambientale. Canone, rilievo B3 |
| T86 | **Il quarto criterio di accettazione del CIP è scoperto per metà, e nessuna nota lo dichiarava**: `IO-05` §8 chiede «**ATP ≤ 150 RLU**; micro come da `MOD-QA-19`», e il registro dei tamponi **non porta una sola lettura ATP** | **lotto 2B** — dalla revisione col canone | **nessun lotto la porta**: è un'assenza dell'archivio, non di un lotto | **aperta dichiarata** — ⚠️ La nota della conducibilità scriveva che «il quarto dei controlli ha ora il suo registro»: **è vero per metà**, e la metà mancante non aveva casa. Da segnalare al gate finale come **limite strutturale del corpus**, con T78 |
| T87 | **La sola datazione del collaudo del `CR-SP180` che l'archivio porti**: «ultima campagna su `TS-01` prima del **collaudo `CR-SP180` previsto autunno**», ultima riga del registro dei tamponi, 25/05/2026 | **lotto 2B** | **il lotto che porta il piano investimenti** (tema 9) e il preventivo Criotech | tracciata — ⚠️ **obbligo esplicito**: `macchina-ts-01` e la nota della dismissione non hanno nessuna data di collaudo, e il manuale HACCP vi appende due impegni (rivalidazione CCP4 e riesame straordinario). Alla canonizzazione del piano investimenti va cercata la data vera |
| T88 | **Tre serie parallele di numerazione delle non conformità, con collisioni fra soggetti diversi**: `NC-26-nnn` nel registro tamponi, `NC-2026-nnn` nel registro interno `MOD-QA-18`, `NC-ACQ-26-nn` nel registro dell'acqua — e la differenza fra le prime due è di **due cifre nell'anno** | **lotto 2B** — dalla revisione col canone | **già in archivio**: tutte le gambe sono canonizzate | **riconciliata** — ✅ **le quattro coppie sono entrate in `alias_entita.md` come classe B** (quasi-omografi che non si uniscono mai), e le tre note del vault che portano una sigla ambigua hanno ora la sezione «Da non confondere con» con la sua fonte. ⚠️ **Ma la riconciliazione è locale**: nessun documento dell'archivio riconcilia le tre serie, e **nessuna non conformità dei due registri analitici compare in `MOD-QA-18`**, che pure dichiara di essere il registro delle non conformità interne. Canone, rilievo B4 |
| T89 | **L'estrattore congelato del corpus non vede le formule dei fogli di calcolo**, e il censimento del 21/08/2026 alle 12:39:33 dice quanto e' grande il buco: **1.697 celle con formula in 13 file su 15, e TUTTE invisibili** — zero celle con valore in cache in tutto il corpus. **Dieci dei tredici file non sono ancora canonizzati**, fra cui il budget per linea (332 formule), il libro unico (425), il cruscotto KPI (65) e il vendor rating (73) | **lotto 2B** — emersa dalla revisione col canone; contata da `06_operativo\censimento_formule.py` | **gate di 2B-bis**, che decide col numero in mano | tracciata — ⚠️ **Non e' un difetto di una nota: e' un punto cieco della catena di provenienza**, perche' QA e strato di giudizio girano entrambi sul testo estratto. ⚠️ **E non e' sporadico: e' sistematico.** Nessun `.xlsx` del corpus porta valori in cache, quindi **ogni cella calcolata risulta vuota** — e «questa colonna e' vuota, quindi nessuno l'ha compilata» e' una lettura possibile ma non l'unica. ✅ **Soglia superata**: il criterio scritto al gate del 21/08 dice «piu' di tre grezzi non ancora canonizzati», e sono **dieci**. L'estensione di cantiere della QA si fa, ma **la decisione operativa e' al gate di 2B-bis**: due difetti piantati, perimetro chiuso, e **l'estrattore di misura non si tocca comunque** |
| T90 | **Il riesame straordinario del 05/06/2026 sul rework di Linea 1**: la consulente chiede il divieto, il direttore di stabilimento sospende in via cautelativa con **disposizione verbale del 26/05**, e la decisione e' rimandata a un riesame | **lotto 2B-bis** | **il lotto che porta i verbali di riesame della direzione** (tema 3, sistema qualita') | tracciata — ⚠️ **obbligo esplicito**: alla canonizzazione dei verbali va cercato l'esito del riesame del 05/06. Finche' manca, **il documento in vigore porta la tolleranza e la pratica e' sospesa**, e chi legge il solo §7.4 legge una regola che non e' applicata |
| T91 | **La sessione di formazione di recupero del turno notte, proposta per il 26/03/2026**: l'assistente qualita' la propone per le 5:30 prima dell'attacco, e nessuna fonte del lotto dice se sia stata fatta | **lotto 2B-bis** | **il lotto che porta il registro della formazione `MOD-HR-11`** (tema 7, persone) | tracciata — ⚠️ **obbligo esplicito**: alla canonizzazione del registro va verificato se il 26/03 compaia, e chi vi abbia firmato. E' l'unico modo di sapere se la copertura della formazione 2026 sia completa |
| T92 | **Il cartello degli allergeni del 2024 e le slide vecchie in bacheca**: due documenti superati che circolano, e le contromisure sono prescritte in aula il 19/03 senza che l'esito sia registrato | **lotto 2B-bis** | **nessun lotto**: e' un'assenza dell'archivio | **aperta dichiarata** — `fatto-cartello-bacheca-2024-senza-sesamo`. ⚠️ **Il cartello e' il documento che un operatore guarda quando ha un dubbio in linea**, e non ha il sesamo: e' il documento piu' esposto e quello che manca del dato piu' recente |
| T93 | **Le referenze «fuori scheda» del canale Ho.Re.Ca. lavorate su Linea 2**: introducono frutta a guscio e **non hanno una riga nella matrice allergeni**, che pure dichiara di coprire ogni referenza a listino e i prototipi | **lotto 2B-bis** | **il lotto che porta il listino e l'anagrafica articoli** (temi 5 e 10) | tracciata — ⚠️ **obbligo esplicito**: alla canonizzazione del listino va verificato se quelle referenze vi compaiano e quali siano. **Tre referenze a listino portano `PC` frutta a guscio a causa di prodotti che la matrice non descrive**: chi legge la tabella vede l'effetto e non la causa |
| T94 | **L'etichettatura precauzionale dello snack multicereali dichiara latte e sesamo, la matrice prescrive anche la soia** | **lotto 2B-bis** — trovata dallo strato di giudizio al primo giro, non dalla scrittura | **entrambe le gambe sono canonizzate**: la scheda tecnica dal lotto 1A, la matrice da questo | **aperta dichiarata** — `questione-precauzionale-af-sn-0450-soia`. ⚠️ **Le date non risolvono da sole**: la scheda tecnica e' del 03/03 e la matrice del 21/04, ma **la scheda dichiarava gia' il latte a marzo**, cioe' era avanti su un allergene che la matrice ha riclassificato dopo. **Se era avanti sul latte, il silenzio sulla soia non si spiega col fatto che sia vecchia** |
| T95 | **Il nome per esteso della consulente esterna lo da' UNA fonte sola**, il manuale di autocontrollo: la scheda allergeni e il materiale di formazione la nominano solo per iniziale | **lotto 2B-bis** | **gia' in archivio** | **riconciliata** — ✅ riga in `alias_entita.md`, classe A. ⚠️ **Non e' una curiosita' bibliografica: e' il caso in cui questa sessione ha INVENTATO un nome proprio** — «Claudia» invece di «Chiara» — canonizzando due documenti che il nome non lo portavano. **L'ha trovato lo strato di giudizio al primo giro**, e la riga di alias esiste perche' non succeda di nuovo |
| T96 | **Il secondo punto cieco della catena di provenienza: l'estrattore congelato non vede il BARRATO.** Nel `.docx` della scheda allergeni **quattro passaggi portano il barrato attivo** — la revisione superata, la riga del latte riclassificato, la deroga di Linea 2 e **meta'** della tolleranza sul rework — e **nessuno dei quattro si distingue nel testo estratto**: le parole stanno dove stanno tutte le altre, e l'attributo che le cancella vive in una proprieta' del carattere. **Il vault ne aveva registrato uno solo, e non perche' l'avesse visto: perche' un commento accanto usa la parola «cancellata»** | **revisione col canone del lotto 2B-bis**, 21/08/2026 | **nessun lotto: e' un limite dello strumento, non una gamba mancante** | **tracciata** — ⚠️ **Stessa famiglia di T89**, e la seconda volta che la catena di provenienza si scopre cieca a qualcosa che sta nel file: **prima le formule mai calcolate, ora il formato del carattere.** ⚠️ **Questa riga sta qui e non in una nota**, perche' e' un'affermazione sull'intero archivio e nessuna nota ha per fonti l'intero archivio (E47). ⚠️ **L'estrattore di misura NON si tocca** (metodo_01 §5-bis): l'eventuale estensione di cantiere e' materia del gate, e finche' non c'e', **l'unica difesa e' aprire il `.docx` come archivio a mano** — cioe' una verifica che dipende da chi legge |
| T97 | **Il manuale HACCP e la scheda allergeni non concordano su quali proteine si cercano ne' ogni quanto**: il manuale prescrive latte, uovo e **soia** con **una validazione a trimestre per linea**; la scheda cerca latte, uovo e **sesamo** e tratta la validazione come adempimento **una tantum**, legato all'arrivo del tunnel | **revisione col canone del lotto 2B-bis** | **entrambe le gambe sono canonizzate**: il manuale dal lotto 1A, la scheda da questo | **aperta dichiarata** — `questione-proteine-test-manuale-e-scheda`. ⚠️ **E' la piu' pesante delle otto**: il **sesamo**, l'allergene nuovo, **non e' nel piano di test del documento di vertice**, che pure lo riconosce come pericolo in farcitura. ⚠️ **Il lotto poteva coglierla da solo** — il manuale era gia' nel vault e questo stesso lotto lo cita come fonte |
| T98 | **La scheda allergeni fa aprire la non conformita' sul modulo dei RECLAMI**: §6.4 prescrive «apertura NC su `MOD-QA-31`» dopo due esiti non conformi consecutivi, e `MOD-QA-31` e' la scheda reclami — le NC interne stanno su `MOD-QA-18` | **revisione col canone del lotto 2B-bis** | **gia' in archivio** | **aperta dichiarata** — `questione-nc-lavaggi-sul-modulo-reclami`. ⚠️ **Estende la famiglia di B4 del canone — le serie parallele di numerazione delle NC — dai NUMERI ai MODULI.** ⚠️ **Lo stesso inciampo e' gia' auto-segnalato nel registro dell'acqua** («refuso, verificare modulo giusto con Marchetti»): li' qualcuno se n'e' accorto, **qui e' rimasto dentro un documento approvato** |
| T99 | **Come sia composto «il lavaggio completo CIP».** `IO-05` §5 elenca **sei voci** sotto la frase «il ciclo completo ha **5** fasi» — il conto torna solo escludendo la sanificazione, che e' condizionata al programma; la scheda allergeni §5.3 definisce l'`L3` «completo CIP secondo `IO-05`» **omettendo il prerisciacquo e includendo la sanificazione**. ⚠️ **Non e' «IO-05 piu' una fase»: e' IO-05 meno la prima e piu' l'ultima**, e il log le esegue tutte e sei mettendo la sanificazione dove nessuno dei due la elenca | **revisione col canone del lotto 2B-bis** | **tutte le gambe sono canonizzate**: `IO-05` e il log dal lotto 2A, la scheda da questo | **aperta dichiarata** — `questione-composizione-lavaggio-completo`. ⚠️ **HA RIAPERTO UN ARBITRATO GIA' SCRITTO NEL CANONE, E IL RI-GIUDIZIO L'HA RICHIUSO.** Sembrava che la fase in piu' avesse una fonte prescrittiva che la chiede, e quindi che l'arbitrato del 2A non reggesse; ma §5.3 prescrive quel sanificante **solo dentro l'`L3`, obbligatorio in quattro circostanze**, e §5.4 affida il tipo di lavaggio al registro del capoturno: **il log non lo dichiara mai**, e il `SANIF_PAA` compare in **28 cicli su 30**. ⚠️ **L'arbitrato regge e ne esce piu' preciso: il tracciato e' piu' severo di ENTRAMBI i documenti.** La divergenza sulla composizione resta vera e vive per conto proprio, e la divergenza cambia specie — da *etichetta che non corrisponde al contenuto* a *due prescrittivi che non concordano*. La riga del canone porta ora il rimando |
| T100 | **La nota alla matrice motiva un perimetro che la TABELLA non elenca**: «"`PC` soia" su **Linea 1 e Linea 2**», e nella tabella nessuna referenza di Linea 2 porta `PC` sulla soia (due `C`, una `A`) | **revisione col canone del lotto 2B-bis** | **nessuna** | **aperta dichiarata** — dentro `questione-precauzionale-af-sn-0450-soia`. ⚠️ **Era stata registrata come incoerenza intra-file, e il ri-giudizio l'ha corretta**: lo stesso documento dichiara che su Linea 2 girano «referenze fuori scheda (mercato Ho.Re.Ca.)», che la matrice per costruzione non elenca. **Il perimetro esiste; e' la tabella a non contenerlo.** ⚠️ Il fatto sull'archivio resta, ed e' piu' utile: chi legge la sola tabella non puo' ricostruire da dove venga quella classificazione |
| T101 | **L'aula da' arachidi e solfiti come possibili, la matrice li da' assenti**: le slide scrivono «non presente ma ATTENZIONE ai fornitori» e «possibile in alcune materie prime», la matrice li classifica `A` su tutte e sette le referenze — e `A` significa «non in ricetta **e non presente nel flusso della linea**» | **revisione col canone del lotto 2B-bis** | **entrambe le gambe sono nel lotto** | **aperta dichiarata** — `questione-arachidi-solfiti-aula-e-matrice`. ⚠️ **E l'elenco degli allergeni «non presenti nel sito» e' di sei voci, e arachidi e solfiti non ci sono**: sono l'unico caso in cui la classificazione piu' forte non e' sostenuta dall'elenco che dovrebbe sostenerla. ⚠️ **Qui l'operatore ha imparato una cosa piu' cauta di quella che il documento tecnico afferma** — l'inverso del caso del rework |
| T102 | **Il registro della formazione non conferma nessuna delle sessioni allergeni del 2026**: in `registro_presenze_corsi_HACCP_scaduti.csv` le sole righe «Allergeni (PRPo1)» sono **cinque, tutte del 09/10/2025**, con validita' **biennale** mentre §9.1 prescrive il richiamo **annuale**; nessuna riga per il 19-20/03/2026 ne' per la straordinaria del 10/04, e **nessuno dei tre nomi che la scheda dichiara formati ha una riga allergeni** | **revisione col canone del lotto 2B-bis** | **il lotto che porta `registro_presenze_corsi_HACCP_scaduti.csv`** (tema 7, persone) | ✅ **CHIUSA nel lotto 3B del 23/08/2026.** ⚠️ **Il grezzo non e' arrivato dal tema 7 come la riga si aspettava: e' arrivato con 3B**, perche' il ripacchettamento del tema 3 lo ha messo accanto alla politica — la formazione e' un prerequisito del sistema qualita' prima che una pratica di HR. **Entrambe le gambe sono ora canonizzate e la divergenza e' scritta**: `fatto-formazione-allergeni-registrata-biennale` porta le cinque righe e il confronto fra validita' registrata e prescritta; `questione-sessioni-allergeni-2026-non-a-registro` porta l'assenza delle sessioni 2026. ⚠️ **E la questione dichiara un limite che la riga non prevedeva**: il registro **non dichiara di essere** il `MOD-HR-11` che la prescrizione nomina, quindi l'assenza di righe non prova che la formazione non sia registrata dove deve — prova che questo estratto non la porta. **T145** |
| T103 | **In aula si dice che i tamponi post-pulizia cercano anche la proteina del latte, e `MOD-QA-19` non ne porta traccia**: il registro ha **sette parametri**, tutti microbiologici | **revisione col canone del lotto 2B-bis** | **entrambe le gambe sono canonizzate**: il registro dal lotto 2B, le slide da questo | **aperta dichiarata** — `questione-tamponi-allergeni-non-registrati`. ⚠️ **La lettura innocente esiste** — il relatore potrebbe parlare dei test rapidi, che la scheda tiene su un binario separato — **ma il fatto sull'archivio resta**: i test rapidi lasciano traccia **solo quando qualcosa va storto**, e chi cercasse dove sono registrati i tamponi allergeni non troverebbe nulla |
| T104 | **Un limite «non rilevato» come condizione di avvio di un prodotto che quell'allergene lo contiene**: §6.2 impone il test proteina **latte** prima di ogni partenza bio su Linea 2, e la matrice classifica il latte **`C` — ingrediente** — sulla sfogliatina bio di quella linea | **revisione col canone del lotto 2B-bis** | **nessuna: e' intra-file** | **aperta dichiarata** — `fatto-proteina-latte-prima-del-bio`, **`type: atomica` e non `conflitto`**, perche' un'incoerenza dentro un solo documento non e' un conflitto fra fonti (§2.4). ⚠️ **La scheda sovrappone due vincoli di natura diversa**: quello del bio e' di **certificazione biologica** — contaminazione da convenzionale, vincolo ICEA — non allergenica |
| T105 | **La scheda dichiara un proprio difetto che il file non presenta**: il commento del controllo qualita' avverte che «la tabella si e' rovinata... le colonne non sono piu' allineate», e **la matrice e' allineata** — intestazione e tutte e sette le referenze portano **sedici campi**, e i valori cadono nella colonna giusta | **revisione col canone del lotto 2B-bis** | **nessuna** | **chiusa** — ✅ ricontata riga per riga sul grezzo. ⚠️ **Il difetto non era nel documento, era nella nota**: `fatto-scheda-allergeni-modifiche-non-accettate` aveva **propagato l'avvertenza come un rischio reale**, deducendone che chi legge la matrice puo' attribuire un allergene alla referenza sbagliata. **Un'autodichiarazione di difetto si VERIFICA, non si cita** — e verificarla era esattamente il compito del lotto |
| T106 | **`ICEA` e' nominato come vincolo e non ha una scheda entita'**: la scheda allergeni motiva l'ordine di produzione di Linea 2 «anche per vincolo `ICEA`», e nel vault l'ente di certificazione biologica non esiste come entita' | **revisione col canone del lotto 2B-bis** | **il lotto che porta i certificati e le certificazioni di prodotto** (tema 3, sistema qualita') | **tracciata** — lacuna minore e dichiarata: la sigla e' leggibile nella nota che la cita, ma **chi interrogasse il vault su «chi certifica il bio di Aurora» non troverebbe una scheda**. Non si apre adesso: **una entita' nasce dal lotto che porta i suoi documenti**, non da una menzione di passaggio ✅ **CHIUSA il 22/08/2026 dal lotto 3C**: l'allegato al certificato BRCGS nomina l'ente, il codice `IT BIO 006`, la norma (Reg. UE 2018/848) e la referenza (`AF-CR-0220`), e dichiara quella certificazione **distinta e non oggetto** del certificato BRCGS. La scheda e' `entita-icea`. ⚠️ **Il criterio ha retto**: l'entita' e' nata dal lotto che porta i suoi documenti, non dalla menzione di passaggio del lotto 2B-bis — e infatti **la menzione dava una sigla, il certificato da' quattro fatti** |
| T107 | ⚠️ **LA POLITICA PER LA QUALITA' HA NOVE IMPEGNI E IL NONO E' BARRATO**: «perseguire la crescita del fatturato quale obiettivo primario dell'organizzazione», in un documento che dichiara la sicurezza alimentare. **Nel testo estratto e' indistinguibile dagli altri otto** | **apertura del tema 3**, 21/08/2026 — trovato dall'estrazione di cantiere PRIMA che il lotto fosse aperto | **lotto 3B** (la politica e la formazione) | ✅ **CHIUSA nel lotto 3B del 23/08/2026, e l'obbligo e' stato eseguito alla lettera**: `fatto-politica-otto-impegni-e-il-nono-ritirato` scrive **otto** impegni in vigore *(contati)* e registra il nono come **proposta ritirata**, con l'annotazione di chi ne ha chiesto la rimozione — «in una politica per la qualita' l'obiettivo primario dichiarato non puo' essere il fatturato». ⚠️ **E' la prova, su dati veri, che E48 non era un adempimento formale**: nel testo dell'estrattore congelato il punto 9 sta in fila con gli altri otto, e senza lo strato del barrato sarebbe entrato nel vault come nono impegno della politica aziendale. **Nessun controllo deterministico lo avrebbe fermato**, perche' non c'e' niente di sbagliato in una riga che dice quello che dice |
| T108 | **`PRO-QA-08` porta TRE passaggi barrati, tutti sostanziali**: che la procedura si applichi anche ai reclami dei FORNITORI; che i reclami di classe 1 e 2 si comunichino al titolare solo per il canale GDO; e che le analisi siano eseguite dal laboratorio INTERNO — quest'ultimo con un commento firmato che spiega la correzione, «il lab interno fa solo tamponi e pH, l'identificazione materiali va fuori» | **apertura del tema 3**, 21/08/2026 | **lotto 3D** (i reclami) | **tracciata** — ⚠️ **`PRO-QA-08` e' fonte PRESCRITTIVA, e i tre barrati toccano il perimetro, la catena di comunicazione e il laboratorio**: alla canonizzazione ognuno va dichiarato come revocato, e va verificato se il testo che li sostituisce esista. ⚠️ **Solo uno dei tre porta un commento che ne spiega la ragione**: gli altri due sono cancellazioni mute |
| T109 | ⚠️ **IL MOCK RECALL DEL 10/03 E' CONFORME PER DUE FONTI E NON CONFORME PER IL RIESAME**: il manuale HACCP prescrive «≥ 99% entro **4 h**», il registro delle NC classifica le 3 h 50 «**entro il limite di 4 h della PRO-QA-14**» con gravita' media, e il verbale le dichiara «**NON conforme**» contro un obiettivo di **2 h** | **revisione col canone del lotto 3A**, 22/08/2026 | **tutte le gambe sono canonizzate** | **aperta dichiarata** — `questione-mock-recall-due-ore-o-quattro`. ⚠️ **E' la divergenza piu' pesante del lotto**: dalla non conformita' discende un obiettivo 2026 dichiarato a **zero per cento** e il rinvio della decisione sul gestionale a settembre. ⚠️ **Il verbale prende META' del criterio del manuale** — applica la soglia del 99 % sul bilancio di massa e sostituisce il tempo. ⚠️ **E il lotto se l'era preclusa per decisione scritta**: l'elenco dichiarava «E37 non scatta su questo lotto» perche' il verbale delibera e non prescrive, senza accorgersi che **il verbale CITA un criterio prescrittivo e lo cambia** |
| T110 | **I reclami di gennaio-febbraio 2026: cinque nel verbale, tre nel registro, e nessuno coincide**: l'unico reclamo Ali' del bimestre e' per muffa e non per saldature, l'unico consumatore e' arrivato dal form del sito e non dal numero verde, e «Famila» non compare fra i reclami di nessun registro | **revisione col canone del lotto 3A** | **entrambe le gambe sono nel lotto** | **tracciata** — ⚠️ **obbligo esplicito**: al lotto che apre `PRO-QA-08` (3D) va verificato se il registro dei reclami sia uno solo. **Due grezzi dello stesso lotto, stesso oggetto, stessa finestra temporale, e tre descrizioni su tre non combaciano** |
| T111 | **Il cruscotto dichiara di derivare i target dal riesame, e non si mappa**: due target su dieci contraddicono la tabella obiettivi, quattro obiettivi del riesame non hanno riga, cinque righe del cruscotto non hanno obiettivo | **revisione col canone del lotto 3A** | **entrambe le gambe sono nel lotto** | **aperta dichiarata** — `questione-cruscotto-e-obiettivi-non-si-mappano`. ⚠️ **Una gamba resta fuori**: `PRO-QA-08` §10 porta «Obiettivo 2026: < 8,0» su un denominatore diverso — **confezioni** invece di **pezzi** — ed e' il grezzo del lotto **3D**: la spiegazione della divergenza sui reclami per milione sta li' e **non e' scrivibile finche' 3D non apre** |
| T112 | **Il costo della non qualita' ha due totali nello stesso workbook**: 24.420 euro sommando la riga mensile, 39.500 sommando l'analisi di Pareto, sullo stesso periodo dichiarato | **revisione col canone del lotto 3A** | **nessuna: e' intra-file** | **aperta dichiarata** — `kpi-costo-non-qualita-due-totali`. ⚠️ **Il canone portava gia' i due valori senza dire che sono lo stesso file.** ⚠️ **E nessuna delle due somme e' scritta nel foglio**: la riga mensile non ha totale, e la cella `TOTALE` del Pareto e' una formula mai calcolata — **si vedono solo sommando** |
| T113 | **Il cruscotto dei tamponi non e' ricavabile da `MOD-QA-19`**: nove punti contro ventuno, un punto in zona 2 che il registro mette in zona 1, una «zona 4» che il registro non ha, e percentuali che nessun numero di prelievi del registro puo' produrre — al massimo sette in un mese | **revisione col canone del lotto 3A** | **entrambe le gambe sono canonizzate** | **aperta dichiarata** — `questione-due-registri-dei-tamponi`. ⚠️ **Due registri paralleli della stessa grandezza, nessuno dichiarato prevalente**: e' la famiglia isolata nel lotto 1C, applicata al monitoraggio ambientale |
| T114 | **Quattro divergenze fra il verbale e i registri gia' nel vault**: il costo al 28/02 (6.800 contro 2.400), le deviazioni CCP collocate a febbraio invece che a gennaio, il Pareto che conta 56 non conformita' dove il registro ne ha 119, e le tarature di marzo che il registro degli strumenti non ha | **revisione col canone del lotto 3A** | **tutte le gambe sono canonizzate** | **tracciata** — ⚠️ **Non sono state scritte come note perche' il lotto aveva gia' esaurito la capienza** (v. T117): stanno nel canone alle voci C5, C7, C8 e C11, e **il primo lotto di manutenzione che tocchi questi registri le riprende**. ⚠️ **La piu' insidiosa e' quella delle tarature**: e' un'attestazione resa alla direzione contro il registro che dovrebbe sostenerla, ed e' la specie isolata in 1C |
| T115 | **Due incoerenze intra-file del verbale**: la tabella delle azioni perde i co-responsabili che il corpo nomina (`A4`, `A5`, `A7`), e il consuntivo 2025 e' chiuso con un evento del **10/03/2026**, posteriore alla riunione e fuori dal periodo dichiarato | **revisione col canone del lotto 3A** | **nessuna: e' intra-file** | **tracciata** — canone C14 e C15. ⚠️ **La prima cade sull'unica tabella che va in bacheca ai reparti come estratto**: due azioni congiunte diventano individuali e una cambia funzione |
| T116 | ⚠️ **`Rilievo_Audit_BRC_IFS_CSQA_febbraio2026.txt` PORTA SETTE DIVERGENZE E NON E' IN NESSUN LOTTO**: il termine e' il **18/03** e non il 17/03; le non conformita' sono **sette** e non due, contando le osservazioni; due termometri dei CCP hanno la taratura scaduta dal 30/11/2025 e **non esistono nel registro degli strumenti**; c'e' stato un sollecito PEC e un avviso di **riduzione del grade AA**; la rivalidazione del CCP2 ha una risposta; il test di rintracciabilita' dell'audit e' **conforme** in 2 h 50; e i neoassunti senza formazione allergeni sono **quattro**, non tre | **revisione col canone del lotto 3A** | **il lotto 3C** (certificazione e audit) | **tracciata** — ⚠️ **NESSUNA delle sette e' scrivibile** (divieto 9-bis): il file non e' canonizzato da nessun lotto. ⚠️ **E' la vena piu' ricca del perimetro di 3A, e sta dietro a un file che il progetto non ha ancora aperto.** ⚠️ **Due di esse correggono cose gia' scritte nel vault**: i «sedici giorni» di ritardo sono **quindici**, e la questione aperta dal lotto R1 sulla rivalidazione del CCP2 **ha una risposta** ✅ **CHIUSA il 22/08/2026 dal lotto 3C: tutte e sette le voci sono state scritte, e la settima ha retto alla verifica.** Il «quattro, non tre» e' confermato: il registro delle non conformita' interne porta `NC-2026-015` del **28/01/2026** — «registro formazione MOD-HR-11 non aggiornato per **3 neoassunti Linea 2**» — e l'audit del 17-18/02 ne trova **quattro**. ⚠️ **La divergenza e' ora una nota sua**, `questione-tre-o-quattro-neoassunti-senza-formazione`, e porta un fatto che nessuna delle due gambe dichiara: **la non conformita' interna scadeva il 20/02, due giorni DOPO la fine dell'audit** — l'auditor ha trovato scoperto un punto su cui l'azienda aveva gia' una NC aperta. ⚠️ **La verifica e' costata due ricerche**: la prima, ristretta ai documenti che nominano gli allergeni, non trovo' nulla e avrebbe fatto scrivere che il «tre» non esisteva. **Il registro delle NC dice «registro formazione», non «allergeni»** |
| T117 | **Il lotto 3A ha sforato il proprio patto di apertura**: il conteggio dei fatti dichiarato prima di scrivere diceva **36 note**, la scrittura ne ha prodotte **38**, e la revisione col canone ne ha aggiunte **quattro** — totale **42**, oltre la soglia dei 40 di E28 | **lotto 3A**, 22/08/2026 | **nessuna: e' un fatto sul metodo** | **chiusa** — ✅ **ratificata al gate del 22/08/2026 con E52**: le soglie governano la proiezione e la scrittura del ciclo, le note post-revisione ne sono fuori ma si dichiarano sempre come gruppo con esiti separati. ⚠️ **La regola viene da due consuntivi, 1B e 3A.** ⚠️ **Il patto diceva «se la scrittura sfora i 40 si spezza in corsa»**, e non e' stato fatto. La ragione: **le quattro note oltre il tetto sono nate dalla REVISIONE**, a lotto gia' scritto e giudicato tre volte, e spezzare li' avrebbe significato rifare il ciclo su due lotti invece di uno. ⚠️ **Ma la regola non distingue fra sforare SCRIVENDO e sforare per divergenze trovate DOPO**, e questa e' una decisione che spetta al gate, non alla sessione |
| T118 | ⚠️ **L'azione correttiva di un rilievo sugli infestanti e' assegnata al prerequisito del vetro**: il rapporto d'audit propone di inserire il controllo delle aperture nel «giro ispettivo mensile PRP-08», ma nel manuale HACCP `PRP-08` e' «Controllo corpi estranei: vetro e plastica dura» e il prerequisito degli infestanti e' `PRP-02` | **lotto 3C** — riconciliazione **verticale**: la nota e' nata dal rapporto, la divergenza e' emersa aprendo il manuale che governa i prerequisiti | **entrambe le gambe sono canonizzate**: il manuale dal pilota, il rapporto d'audit da questo lotto | **aperta dichiarata** — ⚠️ **nessuno dei due documenti prevale**: o l'auditor ha citato la sigla sbagliata, o Aurora usa una numerazione dei PRP diversa da quella del proprio manuale. ⚠️ **In entrambi i casi il controllo delle aperture e' finito in un giro ispettivo che il manuale destina ad altro**, e la nota lo dichiara: `fatto-zanzariera-lacerata-e-porta-officina` |
| T119 | **Due termometri che misurano un punto critico non esistono nel registro degli strumenti**: l'audit trova `TP-08` e `TP-11` con taratura scaduta il 30/11/2025, e nel registro delle attrezzature 2026 **non c'e' nessuna matricola `TP-`** — i termometri a sonda sono `TS-001`…`TS-027` — **ne' alcuna riga con quella scadenza** | **lotto 3C** | **entrambe le gambe sono canonizzate**: il registro dal lotto 1C, il rapporto d'audit da questo | **aperta dichiarata** — ⚠️ **le due letture hanno conseguenze diverse e l'archivio non sceglie**: o il registro non copre tutti gli strumenti che misurano un CCP, o lo stesso oggetto ha due sigle in due documenti. **In entrambi i casi, partendo dal registro non si arriva ai due strumenti scaduti**: `fatto-termometri-tp08-tp11-fuori-dal-registro` |
| T120 | **L'ente chiude «le NC 1-7» in un rapporto che di non conformita' ne ha classificate due**, e il certificato ne riporta due: le cinque «osservazioni» hanno pero' lo stesso apparato delle NC — clausola, requisito, evidenza, root cause, termine, stato | **lotto 3C** | **il rapporto `AU-2026-0233` della piattaforma BRCGS**, che non e' il file in archivio | **aperta dichiarata** — ⚠️ **due piu' cinque fa sette, ma nessuna riga dei due documenti dichiara quella somma**, e le conseguenze non sono simmetriche: se i rilievi da chiudere erano sette, il certificato tace su cinque; se erano due, l'ente ha dichiarato chiuse cinque cose che non aveva aperto come NC. `questione-sette-nc-o-due` |
| T121 | **Il rinnovo della certificazione e' programmato SETTE MESI PRIMA della finestra che il certificato prescrive**: il certificato fissa il riaudit «dal 06/02/2027 al 06/03/2027», la conferma d'incarico programma l'audit di rinnovo fra il 01/06 e il 31/07/2026 e lo fissa al 23-24 giugno, dichiarando nello stesso foglio la scadenza del 09/04/2027 | **lotto 3C** | **l'edizione 2 del certificato**, che l'archivio non ha, o il **Regolamento Generale CSQA `REG-01 rev. 21`**, che il certificato richiama e che nel corpus non c'e' | **aperta dichiarata** — ⚠️ **La programmazione sembra seguire la scadenza VECCHIA** — il 28/07/2026 del primo messaggio della catena — **mentre tutti i documenti dichiarano quella nuova**, e la frase «ulteriori slittamenti no» ha senso solo contro la vecchia. `questione-scadenza-certificato-luglio-o-aprile` |
| T122 | **La stessa non conformita' porta due coppie di clausole diverse, entrambe scritte da CSQA**: il rapporto e il certificato danno BRCGS cl. 2.10.2 e IFS cl. 2.3.9.2, la mail di chiusura da' BRCGS clausola 3.11.3 e IFS req. 5.1.2, per un'evidenza descritta negli stessi termini | **lotto 3C** | **il rapporto della piattaforma BRCGS**, o il regolamento di schema | **aperta dichiarata** — ⚠️ **La maggioranza non e' un criterio**: il rapporto e il certificato discendono l'uno dall'altro e valgono come una fonte sola, e **la mail e' l'unica voce indipendente**. ⚠️ **Il verbale interno di Aurora concorda col rapporto**, non con la mail. `questione-clausola-della-nc1-in-due-versioni` |
| T123 | **Il certificato e il rapporto descrivono lo stesso audit in tre modi diversi**: categorie di prodotto (07 sola contro 07 + 15), durata (2,0 giornate/uomo contro 2 giorni per 2 auditor e 32 h in sito), esclusioni (quattro numerate contro «Esclusioni: nessuna») | **lotto 3C** | **il rapporto `AU-2026-0233`** citato dal certificato e non presente in archivio | **aperta dichiarata** — ⚠️ **Nessuna delle tre e' una sfumatura**: la categoria decide se i semilavorati siano certificati, **le giornate/uomo sono la misura con cui il protocollo BRCGS stabilisce se un audit sia durato abbastanza**, e sulle esclusioni **il certificato afferma che nel rapporto c'e' una cosa che nel rapporto non c'e'**. `questione-categorie-e-durata-audit-divergenti` |
| T124 | **Il documento che l'archivio possiede non e' quello che il certificato richiama**: il certificato cita il rapporto `AU-2026-0233 del 18/02/2026`, disponibile sulla piattaforma BRCGS Directory; il rapporto in azienda dichiara emissione **27/02/2026** con integrazione della sezione 6 il **03/04/2026**, e **non porta nessun numero** | **lotto 3C** | **la piattaforma BRCGS Directory**, fuori dall'archivio | **aperta dichiarata** — ⚠️ **E' la radice di T120 e T123**: se le due versioni divergono, l'azienda tiene quella che non contiene le proprie esclusioni. **Chi volesse verificarlo dovrebbe uscire dall'archivio.** `questione-data-di-emissione-del-rapporto-di-audit` |
| T125 | **Fra il sollecito e la trasmissione ci sono due termini diversi, e il piu' stretto e' quello «informale»**: la sezione compilata dall'ente registra un «nuovo termine perentorio: 01/04/2026», la mail parla di una «proroga informalmente accordata dalla dott.ssa Franceschini al 27/03» | **lotto 3C** | nessuna: i due documenti sono entrambi di CSQA e nessuno nomina il termine dell'altro | **aperta dichiarata** — ⚠️ **Una concessione che ACCORCIA il termine non e' una concessione**, e le due date sono incompatibili nel verso sbagliato. ⚠️ **Il ritardo e' misurato contro termini diversi nei due documenti**: sei giorni contro uno. `questione-proroga-informale-al-27-03` |
| T126 | **Il vault dava il ritardo delle evidenze a SEDICI giorni, e i documenti dell'ente lo danno a QUINDICI**: il termine e' il **18/03/2026** — «28 gg dalla riunione di chiusura» — e il verbale interno lo trascrive al **17/03** contandolo «dalla notifica» | **lotto 3C** — correzione di una nota gia' scritta | **entrambe le gambe canonizzate**: il verbale dal lotto 3A, i tre documenti dell'ente da questo | **riconciliata** — ⚠️ **Non e' un errore di nessuno dei due**: entrambe le decorrenze fanno ventotto giorni, cambia il punto di partenza. **Vale il termine dell'ente, che e' chi lo impone.** ⚠️ **Prima revisione, dentro il lotto 3C, dal terzo giro di giudizio: il «sedici» NON era un refuso del vault.** Il registro delle non conformita' interne porta `NC-2026-061` — «Invio a CSQA evidenze chiusura NC audit **con 16 gg di ritardo** sulla scadenza». ⚠️ **SECONDA REVISIONE, al gate del 23/08/2026, e questa toglie un numero invece di aggiungerlo.** La prima revisione concluse che **«Aurora conta sedici in DUE documenti, il verbale e il registro»**: ⚠️ **il verbale di riesame non porta ne' «sedici» ne' «16»** — verificato riga per riga — **fissa la scadenza al 17/03 e basta**, che del sedici e' la premessa, non l'enunciato. ⚠️ **E il «quindici» non lo scrive nessuno**: nessuna fonte dell'ente conta i giorni, ne' il rapporto ne' le due mail. **Il solo conteggio SCRITTO in una fonte del corpus e' il «16 gg» di `NC-2026-061`**; quindici e sedici, dove il vault li confronta, sono **valori contati dalle date** e ora portano la marca (E50). ⚠️ **La sostanza regge — due termini diversi, due conti diversi — ma «due contatori veri, di due titolari diversi» era la lettura sbagliata: il contatore e' UNO, e l'altro numero e' aritmetica del vault.** ⚠️ **E' la terza stesura di questa riga in due sessioni, e tutte e tre sono cadute sullo stesso punto: un conteggio attribuito a una fonte che non lo enuncia** — la classe di E49 e di E50. **La prima diceva che il vault era «sbagliato», la seconda che Aurora contava in due documenti, la terza conta le fonti che contano davvero: una.** L'ha trovata il **giudizio dedicato di E58**, non una rilettura |
| T127 | **La questione che il lotto R1 lascio' aperta sulla rivalidazione del CCP2 ha una risposta, e viene da fuori**: l'osservazione `OSS-1` del rapporto d'audit constata che la rivalidazione «non risulta ancora formalizzata» e giudica la validazione 2021 «tecnicamente applicabile non essendo intervenute modifiche di prodotto/processo» | **lotto 3C** | — | **chiusa** — ⚠️ **La gamba e' `Rilievo_Audit_BRC_IFS_CSQA_febbraio2026.txt`, §5, `OSS-1`.** La risposta sta in `fatto-rivalidazione-ccp2-non-formalizzata`; `questione-validazione-ccp2-mai-confermata` passa a `risolto` e vi rimanda. ⚠️ **Ma l'incoerenza intra-file NON e' sanata**: la domanda «rivalidazione eseguita?» e' ancora dentro la revisione dell'08/04/2026, sei settimane dopo che l'auditor aveva risposto |
| T128 | **Il grade AA e' sotto avvertimento, e il vault non lo sapeva**: l'ente registra il ritardo a sistema e scrive che una reiterazione al prossimo ciclo comportera' «la segnalazione ai fini del grading BRCGS (riduzione a grade A) e la valutazione ai sensi del regolamento IFS Integrity Program» | **lotto 3C** | — | **chiusa** — ⚠️ **E' il fatto nuovo piu' pesante del pacchetto**, e non riguarda un'inadempienza tecnica ma **il solo ritardo di trasmissione**. ⚠️ **Contro di esso il vault aveva scritto che la direzione chiama quelle certificazioni «obiettivo primario»**: le due note ora si linkano, `fatto-grade-aa-messo-in-guardia` e `fatto-sistema-adeguato-con-riserve` |
| T129 | **Il tasso di difetto di produzione del lotto 3C e' 38,7 %, il piu' alto della serie**, e dodici note su trentuno lo compongono — ma **otto di quelle dodici citano un'altra fonte prescrittiva** che governa cio' di cui parlano davvero (il manuale HACCP, il registro delle tarature), e delle quattro restanti **tre hanno la propria prescrizione FUORI dal corpus**, nel protocollo BRCGS, e una in una «procedura interna» che l'archivio non ha | **lotto 3C** — misura di apertura, non divergenza documentale | **il gate**, che deve decidere se il dominio `certificazione` sia dichiarato troppo largo | ✅ **CHIUSA al gate del 23/08/2026 con E56.** ⚠️ **La risposta e' SI', ed e' una regola non un aggiustamento**: la dichiarazione del dominio e' una **coppia espressioni-fonti che si giustificano a vicenda** — ogni espressione entra solo se una fonte del dominio governa cio' che riconosce, ogni fonte governante si dichiara. ⚠️ **I due versi dell'errore sono stati pagati entrambi**: 2B-bis troppo stretto (9,1 % gonfiato, mancava il materiale d'aula), 3C troppo largo (38,7 % gonfiato, espressioni sull'audit e fonti sul titolo). **Due casi, due versi: la regola viene dai consuntivi.** ⚠️ **IL LOTTO NON SI RIMISURA e il 38,7 % RESTA nella serie**, con la riserva del §5.2 del rapporto scritta accanto (E46: il numero dice su che cosa e' misurato). La serie fotografa le dichiarazioni **come sono state fatte**, ed e' cosi' che insegna: rimisurare darebbe sei punti tutti prodotti con la regola dell'ultimo gate, cioe' una serie che non puo' piu' mostrare il proprio miglioramento |
| T130 | **L'inventario delle evidenze del 02/04 non torna, e la voce che manca e' quella decisiva**: l'ente registra **nove** voci ricevute, la RSGQ ne elenca **cinque** e copre due dei sette rilievi; l'ente verbalizza «foto rimozione carrello ricambi», il mittente allega «foto dell'armadio dedicato ordinato (in consegna)» | **lotto 3C** — **revisione col canone** | — | **aperta dichiarata** — ⚠️ **Le tre righe non stanno insieme in nessun ordine**: se la foto della rimozione fosse arrivata, la riserva del 7 aprile non avrebbe ragione di esistere; se non e' arrivata, la registrazione del 3 aprile elenca una prova che nessuno ha mandato. `questione-evidenze-del-02-04-nove-o-cinque` |
| T131 | **Il prossimo controllo dell'ente e' di sorveglianza a febbraio 2027 o di rinnovo a giugno 2026**: due cluster coerenti al loro interno, scritti dallo stesso ente **a quattro giorni di distanza**, che divergono su quando, su che tipo di audit sia, e su quando Aurora sara' misurata sull'applicazione della seconda firma | **lotto 3C** — **revisione col canone** | — | **aperta dichiarata** — ⚠️ **Nessuno dei quattro documenti nomina l'altro cluster e nessuno dichiara di superarlo: non c'e' una revoca, c'e' un silenzio.** ⚠️ Il campione annunciato nella mail e' «aprile-giugno», cioe' le registrazioni che Aurora stava producendo mentre leggeva la mail. `questione-quando-l-ente-torna-a-verificare` |
| T132 | **La convalida annuale del metal detector `MD-3200` ha tre date**: `11/2025` secondo il rapporto d'audit — cioe' **dichiarata all'auditor** — `06-feb-26` secondo il piano di manutenzione, `04/03/2026` secondo il registro delle attrezzature | **lotto 3C** — **revisione col canone** | — | **aperta dichiarata** — ⚠️ **La terza voce e' esterna**, e i due registri paralleli della metrologia erano gia' noti al vault dal lotto 1C. ⚠️ **E la periodicita' non torna nemmeno fra i due interni**: dodici mesi contro sei, sullo stesso strumento e nello stesso anno, mentre il manuale HACCP prescrive «verifica annuale». `questione-convalida-md-3200-tre-date` |
| T133 | **La parcella dell'audit di febbraio esiste in QUATTRO versioni incompatibili**: fattura `2201/26` del 28-02-2026 pagata **5.490,00** il 13/05 · «fattura CSQA n. **2026/1187** = **6.850 €** + iva» **pagata il 15/04** · un saldo di **6.100** atteso al 30/06 con «fattura ferma da marzo» | **lotto 3C** — **revisione col canone** | **il lotto 6, amministrazione** (fatture, estratto conto, report costi, previsionale di cassa) | **tracciata** — 🚫 **NON scrivibile, divieto 9-bis**: tre gambe su quattro stanno in un lotto non canonizzato. Canone, sezione 22/08/2026, **D5**. ⚠️ **Obbligo esplicito per il lotto dell'amministrazione** |
| T134 | **La durata dell'audit ha un terzo testimone, ed e' quello che decide**: la fattura elettronica dettaglia **«2 GG UOMO X 2 AUDITOR»**, cioe' la versione del rapporto contro quella del certificato | **lotto 3C** — **revisione col canone** | **il lotto 6, amministrazione** | **tracciata** — 🚫 **NON scrivibile, divieto 9-bis.** ⚠️ **Chiuderebbe T123**, che oggi resta aperta dichiarata: alla canonizzazione del lotto 6 si torna su quella riga. ⚠️ **Corollario, e domanda per S7**: il rinnovo costa **4.850,00** per **meta'** delle giornate/uomo fatturate a febbraio, e nessun documento lo spiega. Canone **D6** |
| T135 | **CSQA ha due partite IVA nel corpus, entrambe valide**: `02603680246` nel pie' di pagina della mail, **`IT02052850241`** nell'intestazione della fattura elettronica — stessa ragione sociale, stesso indirizzo | **lotto 3C** — **revisione col canone** | **il lotto 6, amministrazione** | **tracciata** — 🚫 **NON scrivibile, divieto 9-bis.** ⚠️ **Entrambe superano il controllo di Luhn**, quindi per la regola di ammissione della tabella alias **non sono una variante ma due identificativi distinti**: non si uniscono. `entita-csqa-certificazioni` ne porta una sola. Canone **D7** |
| T136 | **Due obblighi di comunicazione con un termine, e nessuna traccia dell'adempimento in tutto il corpus**: il certificato impone **3 giorni lavorativi** per i provvedimenti dell'Autorita' — e il corpus ha un verbale ATS **con diffida**; l'accordo quadro Tosano impone **5 giorni lavorativi** per ogni **downgrade** o esito di audit di certificazione | **lotto 3C** — **revisione col canone** | **il lotto 5, commerciale** (accordo quadro Tosano) | **tracciata** — 🚫 **La meta' Tosano NON e' scrivibile, divieto 9-bis.** ⚠️ **E' l'anello che manca a `fatto-grade-aa-messo-in-guardia`**: quella nota chiama il declassamento il fatto piu' pesante del pacchetto **senza sapere che un downgrade e' un evento contrattuale con un termine di cinque giorni e una clausola risolutiva**. Canone **D8** |
| T137 | **La quinta gamba della divergenza sulle clausole della NC 1 non e' citabile**: `PRO-QA-08_gestione_reclami_cliente_rev2.docx` riga 113 ripete «rif. BRCGS 9 cl. 2.10.2 / IFS 5.1.2», la stessa combinazione mista del registro interno | **lotto 3C** — **revisione col canone** | **il lotto 3D, reclami** | **tracciata** — 🚫 **divieto 9-bis.** ⚠️ **Rafforzerebbe la nota invece di cambiarla**: due documenti interni contro uno, sulla stessa combinazione. Alla canonizzazione di 3D la riga va aggiunta a `questione-clausola-della-nc1-in-due-versioni`. Canone **D4** |
| T138 | **Una nota del vault e' stata scritta su un valore che nessuno aveva contato, e la verifica ha richiesto DUE ricerche**: la settima voce di T116 diceva «i neoassunti senza formazione allergeni sono quattro, **non tre**», e la prima ricerca — ristretta ai documenti che nominano gli allergeni — non trovo' nulla | **lotto 3C** | — | **chiusa** — ⚠️ **Il «tre» esiste**, ed e' in `non_conformita_interne_registro_2026.csv` riga 17: «Audit interno: registro formazione MOD-HR-11 non aggiornato per **3 neoassunti Linea 2**». **Il registro dice «registro formazione», non «allergeni»**, e una ricerca fatta sul tema invece che sull'oggetto lo mancava. ⚠️ **La lezione e' di metodo: un termine di ricerca ristretto puo' produrre un'assenza falsa**, e un'assenza falsa e' peggio di un dubbio |
| T139 | **Aurora ha aperto DUE non conformita' interne contro se' stessa sul ritardo verso l'ente**, e le ha chiuse in una settimana: `NC-2026-049` del 17/03 («scadenza 28 gg al 17/03 SUPERATA», gravita' **alta**) e `NC-2026-061` del 02/04 («con 16 gg di ritardo»), chiusa il **09/04/2026** | **lotto 3C** — **terzo giro di giudizio**, lacuna di copertura | — | **chiusa** — ⚠️ **Sono le due sigle che l'annotazione a margine del verbale nominava senza descrivere**, e il contenuto stava in un altro file dell'archivio: `fatto-due-nc-interne-sul-proprio-ritardo`. ⚠️ **La seconda NC riassume la nota di CSQA come «richiamo a pianificazione scadenze enti»** — quella nota, letta per intero, contiene **l'avvertimento sul grade AA** |
| T140 | **I tre fornitori che l'audit da' per mancanti dal vendor rating 2025 sono classificati nel riesame di marzo**: l'osservazione n. 5 del 17-18/02 dice che mancano `F0044`, `F0031` e `F0090`; il verbale del 12/03, §6.2 «Valutazione fornitori 2025», li mette **tutti e tre in classe A o B** | **lotto 3C** — **terzo giro di giudizio**, lacuna di copertura | — | **aperta dichiarata** — ⚠️ **Le due letture non pesano uguale**: o il rilievo e' infondato, o le classi sono state assegnate **dopo** l'audit e presentate come valutazione 2025. ⚠️ **Un indizio sta dentro il verbale**: la motivazione di classe B per Flexipack e' «bobina fuori spessore **10/02/26**», di una settimana prima dell'audit — un dato che una valutazione dell'anno 2025 non poteva contenere. **Ma non decide**, e la nota lo dice: `questione-vendor-rating-2025-c-e-o-non-c-e` |
| T141 | ⚠️ **DUE NOTE DEL LOTTO NON SONO PASSATE DAL GIUDIZIO**, e sono quelle nate dai ritrovamenti del **terzo** giro: `fatto-due-nc-interne-sul-proprio-ritardo` e `questione-vendor-rating-2025-c-e-o-non-c-e` | **lotto 3C** — debito di processo dichiarato | **il gate**, e il prossimo lotto che produca note post-revisione | ✅ **CHIUSA al gate del 23/08/2026: le due note sono state giudicate, ed E58 e' nato da qui.** ⚠️ **IL GIUDIZIO DEDICATO HA TROVATO DIFETTI IN ENTRAMBE — due su due `afferma_oltre`**, e questo e' il dato che giustifica la regola: se il debito fosse stato formale, il giudizio sarebbe tornato pulito. **La prima** attribuiva all'ente conteggi e contenuti che la sua unica fonte — il registro NC interne — non riporta, e il titolo diceva «le chiude in una settimana» mentre `NC-2026-049` va dal 17/03 al 02/04; **la seconda** chiudeva con «l'archivio non scioglie», che e' la classe di E57 in una nota nata due giorni prima che E57 esistesse, e portava un «nessuno lo ha contestato» mentre il rapporto d'audit registra «Azione correttiva proposta... Stato: APERTA». ⚠️ **Le correzioni sono in massima parte soppressive** (criterio 1B): i fatti tolti non si perdono, hanno gia' la loro nota padrona e la nota vi rimanda (E40). ⚠️ **Due affermazioni erano invece AGGIUNTE, quindi mai giudicate, e hanno preso il secondo giro dedicato che E58 prescrive.** ⚠️ **E un difetto trovato per strada**: `fatto-evidenze-audit-oltre-termine` portava la stessa fonte due volte in `fonti`, corretto. Esiti in `qa\2026-08-23_giudizio_t141\` |
| T142 | **La classe d'errore che il terzo giro ha cercato perche' gliel'hanno nominata: IL SUPERLATIVO SULL'ARCHIVIO.** «e' la sola parte dell'archivio in cui...», «e' il solo documento dell'archivio a nominarla», «e' il termine piu' stretto che questo archivio conosca», «e' l'unico riscontro in archivio» — quattro affermazioni che **nessuna fonte citata puo' reggere**, perche' parlano di cio' che l'archivio contiene ALTROVE | **lotto 3C** — nominata al secondo giro, cercata al terzo | **il gate**: e' un candidato emendamento | **aperta dichiarata** — ✅ **la REGOLA e' chiusa, il CENSIMENTO no.** **DIVENTATA E57 al gate del 23/08/2026**, col test operativo del §7.1: **il discrimine e' il SOGGETTO**. Soggetto-documento si verifica sulla fonte e regge (dieci casi su quattordici); soggetto-archivio non e' verificabile da nessuna nota, mai, e si restringe al perimetro citato o passa in questa tabella. **RESTA APERTA come riga di censimento**, con l'obbligo scritto qui sotto. ⚠️ **CENSIMENTO da `06_operativo\censimento_superlativi.py`, misura delle 15:22:56 del 23/08/2026 su 325 note esaminate** (esclusi `_index`, `code`, `workspace`, `sources`): **9 note, 10 occorrenze** di classe `superlativo` — `doc-dpi-detergente-acido` · `fatto-listeria-scarico-pt-104-aprile` · `fatto-preventivo-potenza-630-kw-tunnel` · `kpi-conducibilita-acqua-per-punto` · `kpi-metano-forni-maggio-2026` · `kpi-temperatura-uscita-tunnel-ts-01-aprile` · `macchina-cip-01` · `questione-prodotto-acido-cip-an-15-o-acidfood-25` (due) · `questione-sbrinamenti-fascia-notturna-cf-02`. ⚠️ **IL PRIMO CENSIMENTO DAVA 42 NOTE E 47 OCCORRENZE, e quel numero mescolava DUE REGIMI**: accanto ai superlativi c'erano gli esistenziali NEGATIVI — «nessun documento dell'archivio riporta X» — che sono **assenze dichiarate** e le governano gia' **E3 ed E43**, con la ricerca su tutto `sources` e il suo artefatto datato. **Le due classi non si sommano**: sono **31 note e 32 occorrenze** di classe `assenza`, verificabili, e **9 di classe `superlativo`**, che sono le sole scoperte. Sommarle avrebbe ripetuto in piccolo l'errore del 38,7 %. ⚠️ **Il numero e' un LIMITE INFERIORE**: lo script riconosce una forma, il soggetto lo decide chi legge. ⚠️ **LE NOVE NOTE NON SI RIPARANO ORA**: si riparano **nel lotto che le tocca** o nella rete finale, come il debito di E43 — aprire un giro sul vault per una classe di scrittura e' il calcolo lineare di 1C in un'altra forma. ⚠️ **E la classe non e' nata in 3C**: `fatto-obblighi-registro-f-gas` e' del lotto **1B** |
| T143 | **LE ORE DI FORMAZIONE PER ADDETTO HANNO DUE VALORI PER IL 2025 E DUE OBIETTIVI PER IL 2026, in due documenti aziendali**: la politica `DOC-QA-01` rev. 8, emessa il 12/01/2026, da' **4,2** e target **>= 6**; il verbale di riesame del 12/03 da' **6,2** e **>= 8**, e lo scrive due volte — nel consuntivo §5.1 e nella tabella obiettivi §10.1 | **lotto 3B**, riconciliazione orizzontale (E2) col verbale gia' canonizzato in 3A | **entrambe le gambe canonizzate**: il verbale dal lotto 3A, la politica da questo | **aperta dichiarata** — `questione-ore-formazione-due-valori-per-il-2025`. ⚠️ **La spiegazione ovvia — un dato aggiornato fra gennaio e marzo — NON regge**: se il consuntivo fosse stato corretto al rialzo l'obiettivo si sarebbe alzato con lui o sarebbe rimasto fermo, e invece **i due si muovono in direzioni opposte**. ⚠️ **Nessuno dei due documenti dichiara come il valore sia ottenuto**, ne' il denominatore ne' che cosa conti come ora di formazione; e **il registro della formazione non porta le ore**, porta corsi e scadenze. Servirebbe `formazione_master.xlsx`, che in archivio non c'e' |
| T144 | **Le persone che lavorano in Aurora sono CINQUANTA secondo la politica e CINQUANTADUE secondo il registro della formazione** *(contati)*, a quattro mesi di distanza | **lotto 3B**, riconciliazione orizzontale fra i due grezzi del lotto | **entrambe le gambe canonizzate in questo lotto** | **aperta dichiarata** — `questione-cinquanta-o-cinquantadue-persone`. ⚠️ **I due numeri non contano la stessa cosa**: la politica da' il cinquanta in una frase sulla cultura, il registro intesta righe a chiunque abbia un titolo censito. Tolti i tre nomi che al 18/05 non sono personale in forza — una **cessata** la cui riga il registro stesso dichiara «da eliminare», un **agente** di cui dubita che sia in perimetro, una **tirocinante** che entra il 15/06 — restano **49** *(calcolato)*. ⚠️ **La sottrazione mostra che i due numeri sono COMPATIBILI, non che siano lo stesso numero contato due volte**: il registro censisce chi ha un titolo, non chi e' in organico, e chi fosse in forza senza corsi non comparirebbe. Serve un documento di organico con una data |
| T145 | **IL REGISTRO DELLA FORMAZIONE NON DICHIARA DI ESSERE IL `MOD-HR-11`** che il prerequisito `PRP-04` del manuale HACCP e il §9.1 della scheda allergeni nominano come registro della formazione: la sigla **non compare in nessuna delle sue 96 righe** | **lotto 3B** — emerso agganciando la prescrizione (E29/E36) | **il lotto che porti il `MOD-HR-11` vero, se esiste**, oppure la rete finale | **aperta dichiarata** — ⚠️ **E' un limite che pesa su tre note del lotto**, e ognuna lo dichiara invece di aggirarlo: finche' quel legame non e' scritto da un documento, **l'assenza di una riga in questo estratto non prova che la formazione non sia registrata dove deve**. ⚠️ **Il padrone del dato e' `formazione_master.xlsx` foglio 2, che in archivio non c'e'**: questo file dichiara di esserne un'estrazione del 18/05/2026. ⚠️ **Senza sciogliere questo nodo, T102 e T143 restano leggibili in due modi** |
| T146 | **La politica impegna Aurora a trattare i reclami «secondo la procedura `PRO-QA-08`»**, che e' una fonte prescrittiva del corpus **non ancora canonizzata**: appartiene al lotto 3D | **lotto 3B** — limite della riconciliazione verticale, divieto 9-bis | **lotto 3D** (i reclami) | ✅ **CHIUSA dal lotto 3D il 23-24/08/2026, e l'obbligo esplicito e' stato eseguito.** L'impegno 6 della politica dice «ascoltare i clienti e i consumatori, trattando ogni reclamo come un'occasione di miglioramento secondo la procedura PRO-QA-08»; il §1 della procedura dichiara di definire come Aurora «riceve, registra, classifica, indaga e chiude i reclami» di clienti e consumatori finali. ⚠️ **Cio' che la politica le attribuisce e cio' che la procedura prescrive CORRISPONDONO**, e la corrispondenza e' sui soggetti (clienti **e** consumatori) prima che sull'oggetto. ⚠️ **La procedura non nomina il «miglioramento» come scopo**: i suoi quattro scopi al §1 sono risposta tempestiva, causa radice, indicatori per il riesame e conformita' agli standard — il «miglioramento» e' la lettura che la politica ne da'. La procedura ha ora la sua padrona: `doc-pro-qa-08` |
| T147 | **La formazione ANTINFORTUNISTICA del registro — preposto, antincendio, primo soccorso, carrello elevatore, rischio alto, RLS, dirigente — e' governata dal `DVR`, fonte prescrittiva del lotto 8, non canonizzata**: sono **17 titoli scaduti su 17, di cui 7 di questa famiglia** *(contati)*, piu' le tre righe antincendio in scadenza allo stesso 30/06 | **lotto 3B** — esclusa dal dominio `formazione` proprio per questo (E56) | **lotto 8** (sicurezza e ambiente) | **tracciata** — ⚠️ **Le note del lotto REGISTRANO quei titoli e le loro scadenze**, che stanno nel grezzo canonizzato, **e non dicono nulla dell'obbligo che li impone**: quello lo prescrive il `DVR`, che non e' citabile. ⚠️ **Obbligo esplicito per il lotto 8**: al momento di canonizzare il `DVR` si riaprano le note della formazione antinfortunistica e si agganci la prescrizione. ⚠️ **E si guardi per prima la riga «squadra emergenza - PRIORITA'»** del turno di notte |
| T148 | ⚠️ **AL PRIMO LOTTO DICHIARATO SOTTO E56, LA COPPIA ESPRESSIONI-FONTI E' NATA SBAGLIATA — nello stesso verso di 3C.** Il primo taglio del dominio `formazione` dava un tasso di difetto di produzione del **63,6 % su 22 note**, il piu' alto della serie | **lotto 3B**, apertura e chiusura | **il gate**, che deve decidere se il punto misurato regga e che cosa insegni | ✅ **CHIUSA il 23/08/2026, al gate del lotto 3B: la risposta e' E59.** Il gate ratifica **36,4 %** come punto della serie, con la sua storia dichiarata (63,6 → 36,4, stretto una volta su prova per espressione) e senza rimisurarlo (E41). ⚠️ **Ma cio' che questa riga insegna e' un'altra cosa, ed e' quella che diventa regola: TRE DICHIARAZIONI SU TRE SONO NATE SBAGLIATE** — 2B-bis stretta, 3C larga, e 3B larga **sotto la regola della coppia**, cioe' con E56 gia' in vigore e applicata. **Una regola che chiede attenzione ha fallito al primo impiego: la cura non basta, serve la prova.** Da qui **E59**, che meccanizza esattamente il gesto che questa riga descrive — ⚠️ **La prova del difetto e' per ESPRESSIONE, non per numero, ed e' il test che E56 prescrive**: `\bformazion` da sola pescava **tutte e quattordici** le scoperte, perche' riconosce **la parola** — e con essa la struttura del registro, chi lo estrae, la sua intestazione ripetuta, l'indicatore delle ore. **Nessuna fonte del dominio governa un file o un KPI: governano l'OBBLIGO di formare e di registrare.** Fuori anche `HACCP base` e `HACCP avanzato` (nomi di corso, la cui validita' viene da una procedura che il corpus non ha) e `ore/addetto`. ⚠️ **Stretta la coppia, il punto scende a 36,4 % (8 su 22), e QUELLO e' il numero dichiarato.** ⚠️ **La stretta si e' fatta UNA VOLTA SOLA e poi ci si e' fermati**: delle otto residue **tre sono lacune vere** — corrette agganciando la prescrizione — e **cinque le pesca `registro (?:della )?formazion` e `nuovo assunto`**, che riconoscono la MENZIONE del registro e non l'obbligo. **Continuare a restringere a numero visto sarebbe il trucco che E41 vieta, spostato di un piano** (§4.43), e il residuo si dichiara invece di sparire. ⚠️ **E il tasso NON e' stato rimisurato dopo le tre correzioni**: E41 lo vieta, e la serie fotografa il lotto come il ciclo lo ha prodotto |
| T149 | 🚫 **IL `MOD-HR-11` ESISTE IN ARCHIVIO, ED E' UN ALTRO DOCUMENTO.** `verbale_formazione_sicurezza_lavoratori_accordo_stato_regioni.txt` porta in riga 1 «MOD-HR-11 rev.2 - registro formazione», e in calce «Registrazione su scadenzario formazione MOD-HR-11 a cura di F. Sartori» — cioè chiama «scadenzario formazione MOD-HR-11» proprio il file del lotto 3B | **revisione col canone del lotto 3B** | **il lotto che porta `verbale_formazione_sicurezza_lavoratori_accordo_stato_regioni.txt`** | **tracciata** — ⚠️ **Il legame che TRE note di 3B dichiarano «non affermato da nessuna fonte» E' affermato**, e da un documento che il divieto 9-bis rende non citabile: `doc-scadenzario-formazione-2026`, `questione-sessioni-allergeni-2026-non-a-registro` e `questione-tre-o-quattro-neoassunti-senza-formazione` sono corrette **sul loro perimetro** e incomplete sul corpus. ⚠️ **E due documenti diversi portano lo stesso codice di modulo**, in contraddizione con l'intestazione di quello che lo afferma. ⚠️ **Obbligo esplicito**: chi canonizza quel grezzo torna su queste tre note, su T102 e su T145 |
| T150 | 🚫 **IL REGISTRO NON PORTA NESSUNA RIGA DEL 2026: zero su 96** *(contate)*, e la data di corso piu' recente e' il 09/10/2025 — mentre tre sessioni del 2026 sono datate da fonti gia' canonizzate e **una la annota il registro stesso**, riga 35, «agg. 4h fatto 03/2026» su una riga con `Data corso` ferma al 10/12/2024 | **revisione col canone del lotto 3B** | **il lotto che porta il corso sicurezza del 14-15/04/2026**, per la quarta gamba | **aperta dichiarata** — ⚠️ **Non e' l'assenza di una sessione: e' l'assenza dell'intero anno.** Le tre gambe scrivibili sono nel vault (`questione-sessioni-allergeni-2026-non-a-registro`); la quarta — sedici ore a ventidue persone il 14-15/04, con venti attestati numerati — sta in un grezzo non canonizzato. ⚠️ **Completa 2B-bis B6**, che il divieto 9-bis teneva ferma e che questo lotto ha scaricato solo a meta' |
| T151 | **«Attestati HACCP in scadenza nel quadrimestre: n. 5» dichiarato alla direzione il 12/03, contro i DIECI del registro** *(contati)* — e nessun altro titolo HACCP scade fra il 12/03 e il 12/07/2026 | **revisione col canone del lotto 3B** | **entrambe le gambe canonizzate**: il verbale dal lotto 3A, il registro da questo | **aperta dichiarata** — ⚠️ **E' la specie di C11 e del lotto 1C**: un'attestazione resa alla direzione contro il registro che dovrebbe sostenerla, e qui **il verbale cita il registro per nome**. ⚠️ **La conseguenza e' operativa**: da quel cinque discende l'azione `A9`, dimensionata sulla meta' del problema. Canone, sezione datata 23/08/2026, E7 |
| T152 | **LA SESSIONE DI RECUPERO HACCP HA TRE DATE**: `A9` del riesame la fissa al **21/05/2026**, la scheda allergeni §9.3 la da' per **tenuta il 21/05 con due assenti da recuperare il 04/06**, e il registro estratto il 18/05 dalla stessa responsabile di `A9` la dichiara «prenotata: **09/06/2026**» | **revisione col canone del lotto 3B** | **tutte e tre le gambe canonizzate** | **aperta dichiarata** — ⚠️ **Tre giorni prima della scadenza dell'azione, chi ne risponde prenota la sessione DOPO la scadenza.** ⚠️ **Una lettura possibile e' che la scheda abbia preso la scadenza dell'azione per la data della sessione** — ma i «2 assenti da recuperare il 04/06» sono un dettaglio che una scadenza non produce, e nessun documento riconcilia. Canone, E6 |
| T153 | **DUE TABELLE DI OBIETTIVI 2026 CHE NON SI MAPPANO, e un riesame che riconferma la politica «senza modifiche»**: nove obiettivi ciascuna *(contati)*, **due soli indicatori in comune e su entrambi i valori divergono**, un terzo quasi-omonimo che diverge, sei righe per parte senza corrispondenza | **revisione col canone del lotto 3B** | **entrambe le gambe canonizzate** | **aperta dichiarata** — ⚠️ **E' C4 del lotto 3A con un TERZO documento**: l'azienda porta tre tabelle di obiettivi 2026 — cruscotto, verbale e politica — e **nessuna delle tre cita le altre**. ⚠️ **E il verbale §9.5 scrive che la politica e' «riconfermata senza modifiche»**, cioe' la riconferma senza confrontarne gli obiettivi coi propri. Canone, E2 |
| T154 | **IL 97,32 % COMPARE COME «VALORE 2025» IN UN DOCUMENTO EMESSO IL 12/01/2026**, e nell'archivio quel numero e' l'esito dell'audit del **17-18/02/2026** | **revisione col canone del lotto 3B** | **entrambe le gambe canonizzate**: il rapporto dal lotto 3C, la politica da questo | **aperta dichiarata** — ⚠️ **O l'audit 2025 ha dato lo stesso punteggio a due decimali** — e nessun documento del corpus lo dice — **oppure quella riga e' stata scritta dopo il 18/02 in un documento che porta la data del 12/01 e la firma del 15/01**. ⚠️ Stessa specie di **C15 (3A)**: un consuntivo chiuso con un evento fuori dal periodo. Canone, E3 |
| T155 | **RECLAMI PER MILIONE: «confezioni» contro «pezzi», e la conversione non chiude.** La politica da' **9,4 per milione di confezioni** con target **< 8,0**; il verbale **0,89 per milione di pezzi** con obiettivo **< 1,0** e target 2026 **< 0,85** | **revisione col canone del lotto 3B** | **entrambe le gambe canonizzate**: ⚠️ **C3 del lotto 3A dava la gamba «confezioni» per NON scrivibile** perche' stava in `PRO-QA-08` (lotto 3D): **la politica la rende scrivibile oggi** | **aperta dichiarata** — ⚠️ **Il denominatore diverso e' gia' trappola dichiarata; cio' che e' nuovo e' il CONSUNTIVO.** Dai due: 41/0,89 = **46,07 milioni di pezzi**, 41/9,4 = **4,36 milioni di confezioni**, rapporto **10,56** *(calcolati)*. Con quel fattore il target della politica varrebbe **0,76** per milione di pezzi, non 0,85. **Nessun documento riconcilia.** Canone, E1 |
| T156 | 🚫 **UNA PRESCRIZIONE DEL RSPP ESEGUITA SU UNA FRAZIONE DEL PERIMETRO CHIESTO, e un divieto operativo senza un atto che lo chiuda.** La nota di sopralluogo chiede l'addestramento a registro «per tutti gli addetti Linea 3 e magazzino» e il registro lo annota **su una riga sola**; e il magazziniere «NON ABILITATO ALLA GUIDA fino a rinnovo» non ha una riga di rinnovo | **revisione col canone del lotto 3B** | **il lotto 8** (sicurezza e ambiente), che porta il fascicolo dell'infortunio, e il lotto che porta le timbrature | **tracciata** — ⚠️ **La gamba del registro E' scrivibile e il lotto l'ha scritta** (`fatto-tre-righe-del-registro-con-un-obbligo-non-chiuso`): il divieto, la squadra di emergenza scoperta e l'addestramento da registrare. ⚠️ **Non e' scrivibile cio' che la nota RSPP chiede e cio' che le timbrature registrano.** Obbligo esplicito per chi porta quei due grezzi. Canone, E10 ed E11 |
| T157 | **IL BARRATO E' UN TRATTO DEL CORPUS, e il §6 del canone non lo elenca.** Tre grezzi portano testo barrato — la politica (il nono impegno), la scheda allergeni (quattro frammenti, con «modifiche non accettate presenti nel documento») e il contratto frigo, che le dichiara in testa | **revisione col canone del lotto 3B** | **il canone**: e' una riga di §6, accanto a OCR, encoding e date multiformato | ✅ **CHIUSA il 23/08/2026, al gate del lotto 3B: la riga e' in §6 del canone**, in sezione datata, accanto a OCR, encoding e date multiformato. ⛔ **ERRATA SUL CONTEGGIO DI QUESTA RIGA: i grezzi che portano testo barrato sono UNDICI, non tre** — **40 passaggi** in tutto, di cui **6 grezzi gia' canonizzati** (misurato il 23/08/2026 con `estrazione_cantiere.testo_cantiere` su tutti i 160 grezzi, E49). ⚠️ **I «tre» erano i tre che la revisione aveva davanti**, ed e' esattamente la specie che E47 ed E57 descrivono: **un'affermazione il cui soggetto e' l'ARCHIVIO, verificata sul sottoinsieme che l'ha suggerita**. Il canone porta il numero **contato**, non il riportato — ⚠️ **Un'estrazione che non porta il barrato legge NOVE impegni invece di otto**, e restituisce **con citazione vera** l'esatta frase che il consulente ha fatto togliere perche' «in audit e' un rilievo servito su un piatto». ⚠️ **E48 ha dato lo strumento; il §6 non ha ancora la riga che dice a chi legge di aspettarselo.** Canone, E12 |
| T158 | ⚠️ **QUATTORDICI AFFERMAZIONI DEL VAULT VIVONO SOLO NEL `title` O NEL `summary`, E NESSUNA FONTE CITATA LE SORREGGE** *(contate)*. Fino al 23/08/2026 **nessun controllo deterministico guardava li'**: passavano la QA a verde. Quasi tutte della stessa specie — **date scritte con l'anno dove la fonte non lo scrive**: `05/05/2026` nella nota, `5/5` nel quaderno OCR che ne e' la fonte | **gate del lotto 3B**, censimento delle superfici (§4.49) | **la rete finale di fine corsa**, o il lotto che tocca ciascuna nota | **aperta dichiarata** — ⚠️ **E' debito, non produzione**, e resta **AVVISO** per §4.35: quelle note sono nate quando nessuno guardava quella superficie, e renderle rosse bloccherebbe ogni lotto futuro dietro una sanatoria. **ERRORE dalle note nate dal 23/08/2026 in poi.** ⚠️ **E' la superficie su cui il progetto trova piu' difetti**: cinque emendamenti la dichiarano portante — E18, E30, E39, E42, E51 — e **nessuno dei cinque aveva uno strato deterministico dietro**. ⚠️ **Le dodici note toccate**: `fatto-fermo-forno-ft-01-05-05` (tre affermazioni), `fatto-quaderno-capoturno-linea1` (due), `fatto-contatori-reparto-meta-stabilimento`, `kpi-consumi-energia-maggio-2026`, `macchina-ft-01`, `fatto-carica-in-salita-linea-1-aprile`, `fatto-mani-addetto-farcitura-non-conforme`, `fatto-operatore-senza-formazione-haccp-l26130`, `fatto-piano-produzione-sett19-21`, `fatto-sonde-pt-104-in-taratura`, `fatto-richiesta-relazione-48-ore`, `questione-arrivo-officina-fermo-pkm-450` |
| T159 | ⛔ **LA SCHEDA DEL RECLAMO NON DICHIARA DI CLASSIFICARE SECONDO `PRO-QA-08`: attribuisce la scala al par. 4 di UN'ALTRA PROCEDURA**, e lo scrive due volte — in intestazione e nella valutazione del rischio. Quella procedura **non e' ancora nel vault** | **lotto 3D**, segnalazione di copertura del primo giro di giudizio | **il lotto che porta quella procedura** — la sigla compare in `procedura_ritiro_prodotto_CRISI_GDO.txt`, del **lotto 3E** | **tracciata** — ⚠️ **Cambia la forma della questione sulla classe** (`questione-classe-del-reclamo-rec-2026-011`): non e' detto che le fonti stiano leggendo la stessa scala in due modi, potrebbero applicarne **due diverse**. ⚠️ **Il divieto 9-bis vale per intero**: il vault registra che la scheda cita quella procedura, e **non dice nulla di cio' che essa contiene**. ⚠️ **Obbligo esplicito per 3E**: al momento di canonizzarla si verifichi se porti una scala di classificazione dei reclami, se coincida con quella di `PRO-QA-08` §5, e quale delle due governi ✅ **CHIUSA il 24/08/2026, al lotto 3E: la procedura e' arrivata, e la risposta e' che LE SCALE SONO DUE.** `PRO-QA-14` §4 porta una scala propria — **tre classi**, senza denominazione, col discrimine del corpo estraneo **«tagliente/perforante»** contro il **«pericoloso»** delle **quattro** classi di `PRO-QA-08` §5 *(contate su entrambe)*. ⚠️ **Non coincidono, e condividono i numeri 1, 2 e 3**: «Classe 2» senza il nome della procedura e' un'etichetta ambigua. ⚠️ **E la ragione per cui nessuno se n'era accorto e' che sul caso concreto le due scale danno lo STESSO NUMERO per criteri diversi** — non pericoloso e non tagliente portano entrambi alla classe 2. ⚠️ **Quale delle due governi resta aperto**, ed e' ora la forma della questione: `PRO-QA-08` §6.1 punto 4 prescrive di classificare «secondo il par. 5», la scheda applica il §4 dell'altra, e **nessuna delle due dichiara di cedere il passo** |
| T160 | ⚠️ **IL SECONDO RECLAMO E' REGISTRATO SU UNA REFERENZA E UN LOTTO CHE NESSUNA FONTE DELLA VICENDA CONFERMA**: il registro del cruscotto lo segna su `AF-SN-0450` lotto `L26130-L1-T2`, la responsabile qualita' lo attribuisce alla `AF-SN-0455` del formato promozionale **dichiarandolo come inferenza**, e il segnalante scrive di **non ricordare il lotto** e di aver buttato la confezione | **lotto 3D**, riconciliazione orizzontale fra il cruscotto e la corrispondenza | **il `MOD-QA-31` della pratica `REC-2026-012`**, che l'archivio non contiene | **aperta dichiarata** — padrona: `questione-referenza-del-secondo-reclamo`. ⚠️ **Il dato piu' preciso e' il meno sostenuto**, e se la referenza fosse la `0455` il perimetro comprenderebbe un formato che il blocco cautelativo non nomina |
| T161 | ⛔ **UN'ASSENZA DICHIARATA CHE ERA FALSA QUANDO E' STATA SCRITTA, e l'ha corretta il lotto che ha portato il documento.** `questione-data-apertura-rec-2026-011` elencava fra le cose che servivano «la mail automatica di notifica della segnalazione, **che l'archivio non contiene**»: l'archivio la contiene, ed e' `segnalazione_qualita_cliente_privato_corpo_estraneo.txt` | **lotto 3D** | — | ✅ **CHIUSA con la correzione, il 24/08/2026.** ⚠️ **E' E3 pagato per la QUINTA volta in sette lotti**: il grezzo esisteva in `sources\` fin dall'inizio, in un lotto non ancora canonizzato — e **E3 chiede la ricerca su TUTTO `sources\`, non sui lotti chiusi**. ⚠️ **Il controllo di E43 non poteva prenderla**: quella nota non usa la formula di attestazione, dichiara l'assenza dentro un elenco di «cosa servirebbe per chiuderla». **La superficie in cui un'assenza si nasconde e' piu' larga della formula che la dichiara** |
| T162 | ⚠️ **IL SECONDO CASO DEL CORPO ESTRANEO E' ARRIVATO SENZA CONFEZIONE, SENZA LOTTO E SENZA FOTOGRAFIA, E IL FRAMMENTO E' CONSERVATO DAL SEGNALANTE**: l'archivio non dice se sia mai stato ritirato, ne' se sia stato analizzato | **lotto 3D** | **il fascicolo di `REC-2026-012`**, che l'archivio non contiene | **aperta dichiarata** — ⚠️ **La procedura prescrive la richiesta del reperto e il ritiro a cura dell'azienda** (`doc-campione-reso`), e il segnalante ne offre la consegna: **che cosa sia seguito, nessuna fonte lo dice**. ⚠️ **E' un'assenza di documenti, non un'omissione accertata**: il vault registra il vuoto, non lo interpreta |
| T163 | ⛔ **LA PROCEDURA DI RITIRO E RICHIAMO HA DUE CODICI, e le due gambe sono canonizzate**: `PRO-QA-08` §3 rimanda a **`PRO-QA-11`**, il manuale HACCP §10.3 a **`PRO-QA-14` rev. 3**, e il §9 del manuale ripete «vedi PRO-QA-14 per il ritiro». ⚠️ **`PRO-QA-11` compare in UN SOLO FILE su 160** *(cercato su tutti i grezzi)*, ed e' `PRO-QA-08` stessa | **lotto 3D**, revisione col canone (F1) | **il documento stesso**, che nessun lotto ha ancora canonizzato | **aperta dichiarata** — padrona: `questione-due-codici-per-la-procedura-di-ritiro`. ⚠️ **Il documento piu' recente dei due — la procedura, 14/03/2026 — e' quello che usa la sigla che nessun altro conosce.** ⚠️ **La sigla e' cio' che dice a chi opera quale documento aprire**: se il documento e' uno solo, una delle due ricerche non trova nulla ⚠️ **AGGIORNATA al lotto 3E: il documento e' arrivato e si chiama `PRO-QA-14`**, come il manuale HACCP dichiarava. **Resta aperto perche' `PRO-QA-08` §3 la chiami `PRO-QA-11`**, sigla che non compare in nessun altro grezzo *(ricerca su tutto `sources\` depositata in `06_operativo\ricerche_assenza\pro-qa-11-e-pro-qa-14-messe-in-relazione_2026-08-24.md`)*. ⚠️ **E il documento arrivato ne apre una TERZA**: chiama `PRO-QA-13` la procedura dei reclami. Padrona del quadro: `questione-tre-sigle-per-le-procedure-di-qualita` |
| T164 | ⛔ **LA SIGLA `PRO-QA-08` DESIGNA DUE PROCEDURE DIVERSE**: il documento che la porta e' la procedura dei **reclami**, il manuale HACCP la usa per la procedura di **rintracciabilita'** del prerequisito `PRP-09` | **lotto 3D**, revisione col canone (F2) | — | **aperta dichiarata** — padrona: `questione-pro-qa-08-reclami-o-rintracciabilita`. ⚠️ **E' il codice con cui la POLITICA PER LA QUALITA' impegna l'azienda** «secondo la procedura PRO-QA-08»: se la sigla ne designa due, l'impegno rimanda a una delle due e il documento non lo dice. ⚠️ **Classe C della tabella alias**: e' omografia, non variante, e unirle deciderebbe la questione |
| T165 | ⚠️ **IL «RIESAME TRIMESTRALE HACCP» IN CUI L'ALLERTA VIENE REGISTRATA NON ESISTE IN NESSUN'ALTRA FONTE**: il manuale da' team **almeno semestrale** (§4.2) e riesame del piano **annuale** (§12.1), il verbale colloca il prossimo ordinario a **marzo 2027** | **lotto 3D**, revisione col canone (F3) | **un verbale di riesame trimestrale**, che l'archivio non contiene | **aperta dichiarata** — padrona: `questione-riesame-trimestrale-haccp`. ⚠️ **Non e' detto sia un errore**: «almeno semestrale» e' un minimo. **Ma allora sarebbe una prassi che nessun documento istituisce**, e l'evidenza d'audit finirebbe in un verbale la cui esistenza non e' prescritta. ⚠️ **E il §12.1 dice che il riesame straordinario si apre per «allerta RASFF su ingredienti in USO»**: non essendo l'additivo in uso, non era dovuto |
| T166 | ⚠️ **LA RICHIESTA DELL'AUDITOR CHE MOTIVA LA REGISTRAZIONE DELL'ALLERTA NON E' NEL RAPPORTO D'AUDIT**: due NC minori e cinque osservazioni, e ne' «allerta» ne' «RASFF» compaiono nel documento | **lotto 3D**, revisione col canone (F4) | **le note di campo o il verbale di chiusura dell'audit**, che l'archivio non contiene | **aperta dichiarata** — padrona: `questione-richiesta-auditor-sulle-allerte`. ⚠️ **Non e' detto che sia falso**: un auditor chiede piu' di quanto finisca in un rapporto, e una domanda orale non lascia traccia. ⚠️ **Ma un'evidenza tenuta a sistema per rispondere a una richiesta risponde a qualcosa che l'archivio non contiene**, e cio' che manca non e' la ragione: e' la sua attribuzione |
| T167 | ✅ **I RECLAMI SI CONTANO SU DUE DENOMINATORI DIVERSI, E LA GAMBA PRESCRITTIVA CHE MANCAVA E' ARRIVATA**: `PRO-QA-08` §10 prescrive «per milione di **confezioni vendute**» con obiettivo **< 8,0**, come la politica; il verbale di riesame §4.1 conta «per milione di **pezzi**» con obiettivo **< 1,0** e target **< 0,85** | **lotto 3B** (T155), e **lotto 3D** che porta la gamba | — | **aperta dichiarata** — ✅ **la divergenza era gia' a canone da C3 del lotto 3A e da E1 del lotto 3B, e cio' che mancava era il PRESCRITTIVO**: adesso c'e', e la questione ha una padrona, `questione-reclami-per-confezioni-o-per-pezzi`. ⚠️ **I due obiettivi sono coerenti solo se una confezione contiene circa otto pezzi**, ed e' un'aritmetica che nessuna fonte conferma |
| T168 | 🚫 **LA TERZA GAMBA DELL'ORGANICO RIAPRE IL CONTO, E IL CANONE LA PORTA SENZA CHE NESSUNA RIGA LA CHIEDESSE**: `verbale_formazione_sicurezza_lavoratori_accordo_stato_regioni.txt` porta **22 convocati**, di cui **17 nomi che il registro della formazione non contiene** *(contati)*, e il corpus arriva a nominare almeno **69 persone** *(calcolato)* — contro le **50** della politica e del verbale di riesame, e le **52** righe del registro | **gate del lotto 3D** — censimento una tantum di **E62** sugli obblighi del canone (sezione 23/08/2026, **E8**) | **il lotto che canonizza la formazione sicurezza**, insieme a T149 | **tracciata** — ⚠️ **L'obbligo era scritto nel canone e in nessuna riga di questa tabella**, ed è la specie che E62 esiste per chiudere: il canone è il padrone del contenuto, ma **l'apertura di un lotto legge la tabella**. ⚠️ **T144 non lo copriva**: quella riga tiene il 50 contro 52 misurato sui due grezzi di 3B e si chiude con «serve un documento di organico con una data» — **non conosce la terza gamba**, che il divieto 9-bis teneva fuori dal lotto. ⚠️ **Obbligo esplicito**: chi canonizza quel grezzo torna su T144 e su `questione-cinquanta-o-cinquantadue-persone`, e dichiara se i 69 siano un organico o un elenco di chiunque il corpus nomini |
| T169 | ⚠️ **VENTICINQUE NOTE DEL VAULT DICHIARANO UN'ASSENZA SULL'ARCHIVIO FUORI DALLA FORMULA DI ATTESTAZIONE DI E3** *(contate da script)*, e fino al 24/08/2026 **nessun controllo guardava quella superficie**: passavano la QA a verde. La forma tipica è l'assenza scritta in prosa, spesso dentro l'elenco «cosa servirebbe per chiuderla» | **gate del lotto 3D**, estensione del controllo di E43 (§7.3) — misura di `qa_frontmatter.py` delle **13:24:46 del 24/08/2026** | **la rete finale di fine corsa**, o il lotto che tocca ciascuna nota | **aperta dichiarata** — ⚠️ **È debito, non produzione**, e resta **AVVISO** per §4.35: quelle note sono nate quando nessuno guardava quella superficie. **ERRORE dalle note nate dal 24/08/2026 in poi.** ⚠️ **Il numero è un LIMITE INFERIORE**: lo strumento riconosce una forma, il soggetto lo decide chi legge — è la stessa riserva di T142, e la grammatica è la stessa. ⚠️ **E il controllo ha trovato QUATTRO casi in flagranza sulle note del lotto 3D**, nate lo stesso giorno e quindi ERRORE: `fatto-nessuno-risponde-a-voce-al-consumatore`, `fatto-quattro-clienti-gdo-nominati-dalla-procedura`, `questione-due-codici-per-la-procedura-di-ritiro`, `questione-riesame-trimestrale-haccp`. **Corretti nello stesso turno**, e **due delle quattro affermazioni erano FALSE**, e la ricerca su tutto `sources\` lo mostra: v. il §4 di `rapporto_gate_3d.md`. ⚠️ **Le venticinque**: `doc-sds-detergente-acido-cip` · `entita-veneta-energia` · `fatto-allerta-rasff-2026-1467` · `fatto-blackout-21-04-riavvio-centraline` · `fatto-manutenzioni-rimandate-per-promo` · `fatto-operatore-senza-formazione-haccp-l26130` · `fatto-operatori-ccp3-linea1-maggio` · `fatto-riepilogo-datalogger-inaffidabile` · `fatto-risalita-termica-post-riavvio-l26130` · `kpi-mass-balance-l26130` · `questione-carrello-ricambi-dichiarato-rimosso` · `questione-classe-del-reclamo-rec-2026-011` · `questione-codice-allarme-pkm-450` · `questione-consegna-farina-mv26-0429a` · `questione-convalida-md-1800-scaduta-o-valida` · `questione-data-apertura-rec-2026-011` · `questione-data-di-emissione-del-rapporto-di-audit` · `questione-frequenza-tamponi-prescritta-e-reale` · `questione-limite-o2-residuo` · `questione-manutentore-frigo-berica-scaligera` · `questione-pezzi-prodotti-l26130` · `questione-prodotto-acido-cip-an-15-o-acidfood-25` · `questione-sigla-kit-tasselli-ccp3` · `questione-taratura-termoregistratore-cf-02` · `questione-tassello-inox-non-passato` |
| T170 | ⚠️ **DUE COLLAUDI RIFANNO LA LOGICA CHE VOGLIONO PROVARE INVECE DI CHIAMARLA**: `collaudo_related_rotto.py` e una parte di `collaudo_suite.py` reimplementano il controllo che collaudano, cioè provano **una via equivalente** e non **la via di produzione** | **gate del lotto 3B** (punto 4 di ciò che quel gate lascia aperto), **ratificato come debito al gate del lotto 3D** | **la prossima occasione che tocca la suite QA** | **tracciata** — ⚠️ **È §4.29 al contrario**, e §4.29 nasce da un caso pagato: il pacchetto del giudizio tagliato in fette **da una via equivalente e mai esercitata**, con i giudici che confrontavano le note con se stesse. ⚠️ **Un collaudo che rifa' la logica prova la propria copia, non il controllo**: il giorno in cui la produzione cambia, il collaudo resta verde su codice che nessuno esegue più. ⚠️ **Non si ripara oggi perché non è il lavoro di questo gate**, e i due collaudi nuovi del 23-24/08 — `collaudo_intestazione.py` e `collaudo_assenza_fuori_formula.py` — **chiamano già la via di produzione**: la famiglia si sta sanando dal lato nuovo. **Un debito dichiarato non è un debito dimenticato** |
| T171 | ⚠️ **IL PERIMETRO DEL BLOCCO E IL MASS BALANCE, COMPILATI LO STESSO GIORNO DALLA STESSA FUNZIONE, NON CONCORDANO SU NESSUNO DEI NUMERI**: la giacenza bloccata di `L26130-L1-T2` vale **3.290** nel blocco e **1.180** nel mass balance *(scarto 2.110, calcolato)*; il **5.100** che il blocco attribuisce a `L26131-L1-T2` e' lo **spedito di `L26130-L1-T2`** col suo DDT; e il cliente principale e' stato avvisato la mattina per **9.360** pezzi contro le **~8.400** che il blocco conta la sera | **lotto 3E**, revisione col canone (G1-G3) | **entrambe le gambe canonizzate** | **aperta dichiarata** — padrona: `questione-perimetro-del-blocco-e-mass-balance`. ⚠️ **Il primo scarto e' impossibile in un verso solo**: la finestra 18:45-22:00 e' un sottoinsieme del turno. ⚠️ **Il vault aveva entrambe le gambe da agosto e non le aveva mai messe una di fronte all'altra**: e' E2 orizzontale, trovata dalla revisione col canone e non dal ciclo |
| T172 | ⚠️ **UN CLIENTE RISULTA IN RICHIAMO MENTRE LA CLASSIFICAZIONE IN VIGORE DICE RITIRO**: il mass balance marca la consegna a Rossetto Trade `RICHIAMATO` e registra un «richiamo autorizzato» il **15/05 alle 08:05**, mentre l'annotazione del giorno prima classifica **«Classe 2 per ora (ritiro, non richiamo)»** | **lotto 3E**, revisione col canone (G4) | **entrambe le gambe canonizzate** | **aperta dichiarata** — padrona: `questione-un-richiamo-in-classe-2`. ⚠️ **Le due letture non sono equivalenti**: uso corrente della parola in un foglio di lavoro, oppure un richiamo autorizzato fuori dalla classe — e in quel caso mancano l'avviso al consumatore e la notifica all'Autorita' entro 24 h che la classe 1 impone. ⚠️ **Nessuna fonte le distingue**, e la seconda e' la grave |
| T173 | ⚠️ **IL TURNO 3 HA 1.480 CONFEZIONI BLOCCATE E NON ESISTE NEL MASS BALANCE**: `L26130-L1-T3` compare nel blocco del perimetro e in **nessuna** delle sette righe del foglio «A valle» ne' delle due della quadratura *(contate)* | **lotto 3E**, revisione col canone (G5) | **entrambe le gambe canonizzate** | **aperta dichiarata** — padrona: `fatto-il-turno-3-non-e-nel-mass-balance`. ⚠️ **E' una gamba NUOVA di F6 del lotto 3D**, e piu' pesante: la' il turno 3 mancava fra due mail, qui manca nel documento con cui la rintracciabilita' si dimostra a un cliente e a un ente, il cui foglio di quadratura si intitola «requisito BRCGS cl. 3.9.2» |
| T174 | ⚠️ **LA PROCEDURA CHE GOVERNA RITIRI E RICHIAMI NON RECEPISCE L'OBBLIGO DI NOTIFICA ALL'ENTE**: il certificato BRCGS impone di notificare a CSQA **entro 3 giorni lavorativi** richiami, ritiri, allerte e provvedimenti dell'Autorita', e `PRO-QA-14` elenca **tre destinatari** *(contati)* fra cui l'ente non compare, ne' nel §6 FASE 3 ne' nelle sette righe del §7 | **lotto 3E**, revisione col canone (G6) | **entrambe le gambe canonizzate** | **aperta dichiarata** — padrona: `questione-il-ritiro-non-notifica-all-ente`. ⚠️ **Non manca la registrazione dell'adempimento: manca la prescrizione**, e chi esegue la procedura alla lettera non notifica. ⚠️ **Completa D8 del lotto 3C dal lato scrivibile**: la' si registrava l'assenza di traccia, qui l'assenza dell'obbligo |
| T175 | **IL RECAPITO DELLO STUDIO DELLA CONSULENTE HACCP PORTA IL PREFISSO DI UN'ALTRA CITTA'**: `PRO-QA-14` §5 da' allo studio il **049**, e nella riga successiva assegna il **045** al legale dichiarato di Verona; il manuale HACCP e `PRO-QA-08` collocano entrambi lo **Studio Alimentaria a Verona** | **lotto 3E**, revisione col canone (G7) | **entrambe le gambe canonizzate** | **aperta dichiarata**, forza **media** — padrona: `questione-prefisso-dello-studio-della-consulente`. ⚠️ **La stessa tabella dimostra che i prefissi sono usati con precisione.** ⚠️ **Ma uno studio puo' avere una seconda sede, e nessuna fonte lo esclude ne' lo afferma**: la forza si dichiara invece di gonfiarla |

---

## La mappatura file × fatto, accumulata

`metodo_03` §9.3 chiede una riga per **(file × fatto)** in
`06_operativo\matrice_corpus_v1.csv`, con le colonne `file` · `fatto` ·
`cartella_prevista` · `nota_padrona_prevista` · `lotto` · `stato`.

**Non si compila in blocco adesso**, e la ragione è che compilarla per 138 grezzi
significherebbe leggerli tutti prima di canonizzarne uno, cioè fare il lavoro due volte.
Si compila **lotto per lotto**: all'apertura di un lotto si scrivono le righe previste,
alla chiusura si aggiorna la colonna `stato` (`da fare` / `fatta` / `assorbita in altra
nota`) su quello che è realmente successo. Il CSV **si committa alla chiusura di ogni
lotto**, insieme a stato, decision log e canone — obbligo del titolare, gate della matrice.

A fine corsa quel file è la mappatura completa che la scaletta chiede come input delle
Sessioni 4-5, e la prova che nessun grezzo è entrato senza lasciare un fatto.

---

## Cosa questa matrice NON è

Non è la mappatura file × fatto di `metodo_03` §9.3: quella è un CSV a sé, e come si
compila sta nella sezione sopra. Non è un vincolo: è un piano, e le note lo correggono.
E non è un registro di regole — se leggendola sembra che una regola nuova viva qui, è un
difetto di questo documento, e la regola sta in `metodo_03`.

---

## Registro delle modifiche alla matrice

### 24/08/2026 — il lotto 3E si spezza in DUE lotti di canonizzazione: 3E e 3F

⚠️ **La conta dei fatti in apertura (E21) dà 62 fatti sui due grezzi** — **38** la procedura di
ritiro con la sua annotazione manoscritta e il blocco del perimetro, **24** la notifica ATS con
la catena delle due mail interne. **La proiezione supera le quaranta note che impongono lo
spezzamento COMUNQUE** (E28), e il lotto si dichiara e si spezza **prima di scrivere una riga**.

| | |
|---|---|
| **`lotto_03e_crisi_ritiro`** | `procedura_ritiro_prodotto_CRISI_GDO.txt` — la `PRO-QA-14`, il ciclo della crisi e il caso di maggio |
| **`lotto_03f_controllo_pubblico_ats`** | `notifica_ATS_ispezione_programmata_igiene.txt` — il preavviso di ispezione e i quindici giorni che lo precedono. ⚠️ **Chiude il tema 3** |

⚠️ **La cucitura è documentale, non tematica** (E31): i due grezzi restano insieme nella storia
— sono i due casi in cui il sistema risponde a qualcuno di fuori — ma sono **due soggetti
diversi**, una procedura interna dell'azienda e un atto di un'autorità pubblica, e nessuna
riconciliazione passa attraverso il taglio. **Le grandezze condivise fra i due grezzi erano
zero**, misurate da `grandezze_condivise.py`.

⚠️ **L'elenco vecchio si chiamava `lotto_03e_crisi_ispezioni` ed è stato RINOMINATO**, non
riusato: un nome che dice «ispezioni» su un elenco che le ispezioni non le contiene più
afferma ciò che lo spezzamento ha smentito. È E30 esteso applicato a un elenco invece che a
una nota.

⚠️ **E il tema 3 non chiude più con 3E**: chiude con **3F**. La §3 del passaggio di consegne e
il prompt del gate lo dicevano, ed è stata la misura a cambiarlo — non una scelta di comodo.

### 24/08/2026 — la verticale del dominio `ritiro` va a R2, che copre due domini

⚠️ **E37 scatta anche su 3E**: `candidate_r1.py --dominio ritiro` riapre **35 note**, contro una
proiezione di 30-35 nuove. Le riaperte **escono dal lotto di canonizzazione**, come la regola
impone.

⚠️ **Non nasce un terzo lotto di manutenzione, ed è una decisione MISURATA**: **14 delle 35 note
del dominio `ritiro` stanno già nel perimetro di R2** *(misurato il 24/08/2026)*, e due elenchi
di manutenzione che si contendono le stesse quattordici note sarebbero **due padroni dello
stesso lavoro**. `PRO-QA-08` e `PRO-QA-14` sono le due metà dello stesso ciclo: chi ripara l'una
guarda l'altra.

**R2 si apre quindi con due domini rigenerati** — `reclami` e `ritiro` — e la differenza rispetto
alle 65 + 35 di partenza si dichiara in apertura. **Resta in coda al tema**, cioè dopo 3F.

### 24/08/2026 — il lotto 3D si spezza, e nasce il lotto di manutenzione R2

⚠️ **La riconciliazione verticale arretrata (E37) sul dominio `reclami` ha riaperto **65 note**, contro le **35** che il ciclo di 3D ha prodotto. **Le riaperte superano le nuove**, e la soglia di E37 impone di dichiararlo e di spezzare il lotto in uno di canonizzazione piu' uno di manutenzione — stessa logica di E28: una soglia sulla grandezza che il rischio consuma.

| | |
|---|---|
| **`lotto_03d_reclami`** | resta di canonizzazione: i tre grezzi, e le note che 3D tocca |
| **`r2_reclami_verticale`** | **nuovo**, di manutenzione: le note riaperte dalla verticale sul dominio `reclami` |

⚠️ **Il perimetro di R2 si RIGENERA alla sua apertura, non si eredita**: con `PRO-QA-08` ormai canonizzata da 3D, `candidate_r1.py --dominio reclami` restituira' un insieme diverso, e la differenza misura quanto 3D ha gia' sanato.

⚠️ **Gli elenchi passano da 27 a 28.** R2 vale un lotto nel ritmo e resta **fuori dalla serie della capacita'** (E38).


La matrice è un piano: si annota quando cambia, non si riscrive in silenzio.

| Data | Lotto | Cosa è cambiato, e perché |
|---|---|---|
| **23/08/2026** | **3B** | ⚠️ **Il lotto 3B apre l'ottava area del vocabolario: `risorse-umane`.** Lo scadenzario della formazione e' di HR e riguarda la qualita', e l'hub `area-risorse-umane` nasce **pieno**, non per comodita' di archiviazione. Restano senza hub `sicurezza-ambiente` e `ricerca-sviluppo`. ⚠️ **Due obblighi ereditati chiusi**: **T107** — la politica scritta con OTTO impegni e il nono registrato come proposta ritirata — e **T102**, che la riga si aspettava dal tema 7 e che e' arrivata qui col ripacchettamento. ⚠️ **Sei righe nuove, T143-T148**, di cui una — **T148** — sul dominio dichiarato male al primo taglio. **Il piano dei lotti non cambia: restano 3D e 3E** |
| **23/08/2026** | **gate 3C** | ⚠️ **Tre righe di tracciamento chiuse o qualificate dal gate, e nessun grezzo si sposta.** **T129** chiusa con **E56** — il dominio `certificazione` era dichiarato troppo largo, e la risposta e' la regola della coppia espressioni-fonti; **il 38,7 % resta nella serie con la sua riserva, il lotto non si rimisura**. **T141** chiusa col **giudizio dedicato** alle due note mai giudicate (**due su due `afferma_oltre`**), da cui nasce **E58**. **T142** diventa **E57** e resta aperta **come riga di censimento**: 9 note e 10 occorrenze di classe `superlativo`, da riparare nel lotto che le tocca o nella rete finale. ⚠️ **Il piano dei lotti non cambia: il prossimo atto resta `3B`** |
| **22/08/2026** | **tema 3** | ⚠️ **`3C` (certificazione e audit) ANTICIPATO su `3B`**, al gate del lotto 3A. **Il motivo non è l'ordine tematico: è che il rapporto d'audit porta due correzioni a cose GIÀ SCRITTE nel vault** — il «sedici» giorni di ritardo nel titolo di una nota, che i documenti danno a **quindici**, e la questione che il **lotto R1** lasciò aperta sulla rivalidazione del CCP2, che **ha una risposta** — **più un fatto che il vault non sa affatto**: il grade AA messo in guardia, con sollecito PEC e termine perentorio, mentre la direzione lo chiama «obiettivo primario». ⚠️ **Più tardi arriva la gamba, più note ha già attraversato**: ogni lotto che passa senza di essa è un lotto in cui il vault resta sbagliato su cose che l'archivio sa |
| **21/08/2026** | **tema 3** | ⚠️ **RIPACCHETTATO IN APERTURA (E31): i tredici grezzi del sistema qualità diventano CINQUE pacchetti.** `3A` riesame della direzione e dati di ingresso *(verbale + cruscotto KPI)* · `3B` la politica e la formazione *(politica + registro presenze)* · `3C` certificazione e audit *(certificato + rilievo + incarico + email)* · `3D` i reclami *(`PRO-QA-08` + segnalazione consumatore + RASFF)* · `3E` la crisi e il controllo pubblico *(procedura di ritiro + notifica ATS)*. ⚠️ **I pacchetti sono da 2-4 grezzi e non da 3-5, e il criterio è il conteggio dei fatti** (E21/E28), non il numero dei file: i grezzi di questo tema sono molto più densi di quelli dei temi 1 e 2 — **il solo verbale di riesame porta 45 sezioni numerate** — e tre di essi insieme avrebbero superato le quaranta note che impongono lo spezzamento comunque. ⚠️ **Le cuciture non sono tematiche ma documentali**: il cruscotto non è un documento a sé, si intitola «riesame direzione» e dichiara «target definiti nel riesame del 12/03/2026». ⚠️ **Il verso del legame è stato corretto al secondo giro di giudizio del lotto 3A**: qui era scritto che il cruscotto fosse *il dato di ingresso* del verbale, e **è il contrario** — porta dati fino a maggio e target che il riesame di marzo ha già definito, quindi **ne discende**. **La cucitura regge lo stesso, e meglio**: il cruscotto misura se gli obiettivi di quel riesame stiano reggendo, e separarli avrebbe messo la delibera in un lotto e la sua verifica in un altro |
| 2026-08-20 | **2B** | **Il lotto 2B si SPEZZA in apertura, prima di scrivere una riga (E28): `lotto_02b_autocontrollo_igiene.txt` non esiste più, al suo posto `lotto_02b_autocontrollo_analitico.txt` (3 grezzi) e `lotto_02b_bis_allergeni.txt` (2).** Il conteggio dei fatti in apertura (E21) proietta **oltre le 40 note**, e sopra 40 E28 non lascia scelta: si spezza sempre. ⚠️ **Dove passa il taglio, e perché lì**: da una parte i tre registri che portano **risultati di misura con un limite** — tamponi, acqua potabile, acque reflue — dall'altra il **sistema prescrittivo** degli allergeni e la formazione che lo insegna. La scheda allergeni apre **da sola un dominio di riconciliazione verticale** (E37): tenerla insieme al piano dell'acqua avrebbe messo due riconciliazioni verticali dentro un lotto solo, e nessuna delle due sarebbe stata fatta per intero. **T72 resta in 2B** — la conducibilità di rete sta nel piano dell'acqua — e **T71 pure**, perché il registro dei tamponi è qui. `verifica_matrice_lotti.py` resta verde: 160 grezzi, 0 scoperti, 0 guasti, **17 elenchi** |
| 2026-08-19 | **2A** | **Il tema 2 diventa tre elenchi veri: `lotto_02a_cip`, `lotto_02b_autocontrollo_igiene`, `lotto_02c_moca`.** Il ridisegno era scritto qui dal 19/08 ma viveva solo in questa tabella: all'apertura di 2A è diventato tre file in `qa\lotti\`, e `lotto_02_igiene.txt` non esiste più. `verifica_matrice_lotti.py` resta verde: 160 grezzi, 0 scoperti, 0 guasti, 16 elenchi. ⚠️ **T21 e T29 si chiudono** — erano duplicate fra loro, come T22/T30 — e nascono **cinque righe nuove, da T67 a T71**: tre questioni aperte dichiarate del lotto, l'assenza del registro CIP cartaceo, e l'obbligo su `MOD-QA-19` per il lotto 2B |
| 2026-08-19 | **R1**, giro 1 | **Due righe nuove — T65 e T66 — dalla revisione col canone, ed entrambe riguardano il manuale HACCP.** Il documento prescrittivo di vertice dichiara compiuta una rimozione che due documenti successivi smentiscono (T65), e non sa dire se la validazione del proprio CCP2 sia stata rifatta (T66). ⚠️ **T24 estesa**: il manuale dà l'attività dell'acqua su **due matrici**, e questo toglie la base all'arbitrato del 18/08 che dava il file delle prove come anomalo. Le tre divergenze sono state aggiunte al canone in sezione datata, come §9.5 passo 3 prescrive per la categoria B |
| 2026-08-19 | **R1** | **Dieci righe nuove di tracciamento, da T55 a T64, aperte dalla riconciliazione verticale.** Nove nascono dalla **guardia** del lotto R1: una fonte prescrittiva il cui grezzo appartiene a un lotto non ancora canonizzato **non si cita e non si usa** — citarla la farebbe risultare «già coperta» e manderebbe in rosso la disgiunzione di questa matrice — quindi si apre una riga con l'obbligo esplicito per il lotto che la porta. Precedente identico: **T18**. Le fonti sono **36 in tutto**, di cui **8 citabili** oggi e **28 da tracciare**, elencate in `06_operativo\fonti_prescrittive_corpus_v1.md` e generate da `elenco_fonti_prescrittive.py`. La decima, **T64**, è una divergenza nuova con entrambe le gambe canonizzate: la periodicità di taratura del datalogger del CCP2 |
| 2026-08-19 | **manutenzione** | **Il cappello allineato, T30 allineata a T22, e il numero delle righe passa a uno script.** Il cappello diceva ancora «138 grezzi in dodici lotti tematici» mentre le fasce dentro erano già barrate: è la prima cosa che si legge, e diceva il contrario del corpo. **T30 usciva «chiusa» mentre T22, di cui è dichiarata duplicato, usciva «RICONCILIATA»**: la stessa questione con due esiti, sulla tabella che al gate finale è la prova dei conflitti. Allineata a RICONCILIATA tenendo la dichiarazione di duplicazione — nessuna riga sparisce. E le righe della tabella si contano ora con `06_operativo\conta_tracciamento.py`: era **l'ultimo numero del progetto dichiarato senza script**, ed era già uscito sbagliato una volta (lo stato ne dichiarava 41, sono 54) |
| 2026-08-19 | **2-10** | **RICALIBRAZIONE: i budget dei lotti 2-10 sono SUPERATI, e il piano passa da 12 a ~28-30 lotti.** Le fasce erano costruite sulla densità del pilota (2,1 note per grezzo); i consuntivi danno 6,0 · 9,5 · 13,5. ⚠️ **Il calcolo lineare chiesto dal coordinatore è stato eseguito e rifiutato**: dà 903 note e 36 lotti, perché moltiplica una grandezza instabile (densità, dispersione 147 %) per una stabile. L'invariante è il **lotto** (27-46 note, dispersione 50 %), non la densità. Al posto delle fasce vale **E31**, il budget come capacità 25-35, **provvisoria fino a dieci lotti chiusi**. Ridisegnato in dettaglio **solo il tema 2** (in 2A, 2B, 2C); gli altri restano temi da ripacchettizzare in apertura. Le stime vecchie **restano barrate, non cancellate** |
| 2026-08-19 | **1C** | **Errata: le righe dell'elenco tarature sono 120, non 121.** Il conteggio della matrice era a mano, quello di apertura del lotto è da script (`conta_1c.py`). Il file porta inoltre **due righe di intestazione**, la seconda a riga 64 con nomi di colonna diversi: non è un difetto da aggirare, è un fatto dell'archivio e ha una nota nel vault |
| 2026-08-18 | 1 · 10 | `bolletta_VenetaEnergia_maggio2026.pdf` spostata dal lotto 10 al lotto 1: sta con `consumi_energetici_forni_kwh_maggio26.csv`, di cui è la gamba di riconciliazione sul costo dell'energia. Non è rumore |
| 2026-08-18 | 7 · 10 | `Nuova cartella di lavoro.xlsx` spostata dal lotto 10 al lotto 7: ispezionata, **non è un file vuoto** — contiene un appunto sulle timbrature e una `SUM` mai calcolata. Il nome ingannava |
| 2026-08-19 | **1B → 1B + 1C** | **Secondo spezzamento, e i lotti passano da 11 a 12.** Il conteggio dei fatti in apertura ha proiettato **~41 note contro un budget di 22-30** (+37 %): densità **6,8 note per grezzo**, sopra le 6,0 del lotto 1A. Il taglio segue le cuciture della storia, non il numero dei file: **1B** (4 grezzi, budget 22-30) tiene intera la vicenda della cella `CF-02` — allarmi di aprile, arretrati di manutenzione, +49,7 % di consumo, contratto non firmato — e **1C** (2 grezzi, budget 12-18) tiene il parco strumenti, le tarature e i gas tecnici. Riassegnazioni in tabella di tracciamento: **T18, T22, T30** a 1B; **T17, T20, T25, T26, T32** a 1C. Decisione del titolare, che ha aggiunto due obblighi: dichiarare nel rapporto **il criterio di aggancio** con cui 121 righe di strumento diventano una dozzina di note, e dare al revisore **un campione** di quelle note |
| 2026-08-18 | **1 → 1A + 1B** | **Il lotto 1 è stato SPEZZATO in due, e i lotti passano da 10 a 11.** Il conteggio dei fatti in apertura ha proiettato **~62 note contro un budget di 26-36**: densità **4,8 note per grezzo** contro le 2,1 del pilota, perché quattro dei tredici documenti sono multi-fatto. Lo stop-loss della scaletta dice «lotto più piccolo, mai QA più leggera». **1A** (7 grezzi, budget 34-42) tiene il turno, i CCP e la confezionatrice, e chiude i tre conflitti tracciati; **1B** (6 grezzi, budget 22-30) tiene impianti ausiliari, energia, celle e tarature. Da questo caso nasce la **regola di apertura** scritta sopra |

---

## Appendice — l'elenco dei file, lotto per lotto

Generata da `qa\lotti\*.txt`, che sono gli stessi elenchi che la suite QA legge
con `--perimetro lotto @lotti/<file>.txt`. Se questa appendice e l'elenco
divergono, vince l'elenco: e' lui che la QA esegue.

### `lotto_01a_linea1_turno_ccp.txt` — 7 grezzi

- `appunti_capoturno_quaderno_linea1_OCR.txt`
- `checklist_metal_detector_manuale_operaio.txt`
- `manuale_uso_manutenzione_PKM450_estratto.pdf`
- `Scheda_tecnica_prodotto_AF-SN-0450_rev4.pdf`
- `test_shelf_life_accelerata_confezione_MAP_snack.csv`
- `piano_produzione_settimanale_sett19_21.xlsx`
- `scheda_manutenzione_ordinaria_forni_industrial.csv`

### `lotto_01b_freddo_energia.txt` — 4 grezzi

- `log_allarmi_cella_frigo_surgelati_aprile.log`
- `contratto_manutenzione_impianto_frigo_TS01.docx`
- `consumi_energetici_forni_kwh_maggio26.csv`
- `bolletta_VenetaEnergia_maggio2026.pdf`

### `lotto_01c_metrologia_gas.txt` — 2 grezzi

- `elenco_attrezzature_taratura_strumenti_2026.csv`
- `bolla_ingresso_azoto_alimentare_Nordgas_OCR.txt`

### `lotto_02a_cip.txt` — 3 grezzi

- `log_lavaggio_CIP_linea1_maggio.log`
- `IO-05_istruzione_operativa_lavaggio_CIP.docx`
- `scheda_sicurezza_detergente_acido_lavaggio_CIP.txt`

### `lotto_02b_autocontrollo_igiene.txt` — 5 grezzi

- `registro_tamponi_superfici_listeria_salmonella.csv`
- `piano_autocontrollo_acqua_potabile_analisi.csv`
- `analisi_acque_reflue_autocontrollo_2026.xlsx`
- `scheda_allergeni_matrice_cross_contamination.docx`
- `formazione_allergeni_operatori_2026.pptx`

### `lotto_02c_moca.txt` — 4 grezzi

- `estratto_registro_carico_scarico_MOCA.xlsx`
- `DoC_MOCA_Flexipack_film_PP_EVOH_2026.pdf`
- `doc 2 (1).pdf`
- `capitolato_tecnico_fornitura_imballaggi_plastici.txt`

### `lotto_03_sistema_qualita.txt` — 13 grezzi

- `Certificato_BRCGS_Food_Issue9_Aurora_2026.pdf`
- `Rilievo_Audit_BRC_IFS_CSQA_febbraio2026.txt`
- `Conferma_incarico_audit_rinnovo_2026.pdf`
- `R_R_R_scadenza_certificato_BRCGS_e_audit_di_rinnovo.eml`
- `verbale_riesame_direzione_SGQ_2026.txt`
- `politica_qualita_e_sicurezza_alimentare_2026.docx`
- `cruscotto_KPI_qualita_2026.xlsx`
- `registro_presenze_corsi_HACCP_scaduti.csv`
- `PRO-QA-08_gestione_reclami_cliente_rev2.docx`
- `procedura_ritiro_prodotto_CRISI_GDO.txt`
- `segnalazione_qualita_cliente_privato_corpo_estraneo.txt`
- `Fwd_Fwd_Fwd_ATTENZIONE_richiamo_prodotto_concorrente_RASFF.eml`
- `notifica_ATS_ispezione_programmata_igiene.txt`

### `lotto_04_filiera_logistica.txt` — 14 grezzi

- `contratto_fornitura_MolinoVeneto_2026_firmato.pdf`
- `Listino_MolinoVeneto_giu2026.pdf`
- `Comunicazione_aumento_listino_farine_indicizzazione.eml`
- `scheda_tecnica_farina_tipo_0_MolinoVeneto.txt`
- `DDT_MOLINO_VENETO_Farina_0_N48392_OCR_SPORCO.txt`
- `SKM_C224e26050408520.jpg`
- `DDT_Euroglass_Boccacci_Vetro_N99201.txt`
- `img20260428_09241055.txt`
- `ordini_acquisto_materie_prime_aperti_giugno.csv`
- `analisi_scostamenti_costo_materie_prime.xlsx`
- `vendor_rating_fornitori_2026.xlsx`
- `tariffe_vettori_terzi_trasporto_fresco_2026.csv`
- `contestazione_logistica_Tosano_ritardo_Cerea.txt`
- `reso_pallet_EPAL_conteggio_Tosano.txt`

### `lotto_05_commerciale.txt` — 15 grezzi

- `listino_prezzi_canale_GDO_fresco_v3.csv`
- `listino prezzi GDO v2 VECCHIO non usare.csv`
- `accordo_quadro_private_label_Tosano_2026_firmato.txt`
- `Ordine_Tosano_2026_PRM_118_119_120.pdf`
- `Conferma_ordine_Tosano_promo_sottocosto_settimane_19_21.eml`
- `verbale_incontro_Mario_Rossi_Buyer_Tosano_05_05.txt`
- `analisi_sell_out_Tosano_marzo_aprile2026.csv`
- `analisi_marginalita_per_referenza_2026.xlsx`
- `proiezione_ARR_contratti_GDO_2026_2027.csv`
- `presentazione_commerciale_Aurora_GDO_2026.pptx`
- `anagrafica_articoli_export_gestionale.xlsx`
- `lista_contatti_buyer_GDO_nordest.csv`
- `richiesta_campionatura_fiera_Cibus_2026.csv`
- `Newsletter_Fiere_alimentari_2026_NON_LEGGERE.eml`
- `brief_agenzia_packaging_restyling_snack.docx`

### `lotto_06_amministrazione.txt` — 15 grezzi

- `bilancio_esercizio_2025_deposito_CCIAA.pdf`
- `visura_camerale_ordinaria_AuroraFoodGroup.pdf`
- `previsionale_cassa_giugno_agosto2026.xlsx`
- `previsionale cassa giugno-agosto DEF (2).xlsx`
- `estratto_conto_unicredit_maggio26.csv`
- `scadenzario_effetti_RIBA_giugno26.csv`
- `budget_2026_vs_consuntivo_per_linea.xlsx`
- `report_costi_fissi_OpEx_manutenzioni.txt`
- `Fattura_TosanoCerea_2026_0188_copia_cortesia.pdf`
- `IT03984710230_00188.xml`
- `IT03984710230_00215.xml`
- `IT03984710230_00215.xml.p7m`
- `Fatture_Elettroniche_SDI_Inbound_Q2.txt`
- `R_sollecito_pagamento_fattura_scaduta_Oleificio.eml`
- `nota_commercialista_credito_imposta_beni_strumentali.docx`

### `lotto_07_persone.txt` — 15 grezzi

- `libro_unico_lavoro_estratto_maggio2026.xlsx`
- `log_timbrature_fabbrica_maggio_settimana2.csv`
- `Prospetto_straordinari_gen-apr_2026.xlsx`
- `contestazione_sindacale_straordinari_Tosano.txt`
- `email_HR_dimissioni_operai_linea2.txt`
- `organigramma_aziendale_aggiornato_marzo26.pptx`
- `job_description_responsabile_produzione.docx`
- `CV_Tommaso_Refosco_2026.pdf`
- `R_candidatura_spontanea_tecnologo_alimentare.eml`
- `piano_turni_apprendisti_tecnologi_food.txt`
- `reperibilita_gennaio_febbraio_2026.csv`
- `Circolare_INPS_aliquote_contributive_2026.txt`
- `nota_spese_trasferte_Zampieri_aprile.csv`
- `comunicazione_chiusura_estiva_2026.txt`
- `Nuova cartella di lavoro.xlsx`

### `lotto_08_sicurezza_ambiente.txt` — 11 grezzi

- `DVR_estratto_valutazione_rischi_2026.pdf`
- `verbale_formazione_sicurezza_lavoratori_accordo_stato_regioni.txt`
- `nota_infortunio_INAIL_operaio_linea3.txt`
- `ordine_DPI_scarpe_antinfortunistiche.csv`
- `registro_estintori_scadenze.csv`
- `CPI_certificato_prevenzione_incendi_VVF.pdf`
- `verifica_periodica_impianto_terra_DPR462.pdf`
- `AUA_autorizzazione_unica_ambientale_scarichi.pdf`
- `registro_carico_scarico_rifiuti_estratto_2026.pdf`
- `assicurazione_polizza_RCT_RCO_quietanza_2026.pdf`
- `polizza_RC_prodotto_rinnovo_2026_OCR.txt`

### `lotto_09_rd_investimenti.txt` — 12 grezzi

- `ricetta_base_esperimento_snack_salato_v12.txt`
- `appunti_tecnologo_quaderno_prove_pilota_OCR.txt`
- `mail_fornitore_ingrediente_nuovo_paprika_specifiche.txt`
- `panel_test_assaggio_interno_cornetto_premium.csv`
- `verbale_scale_up_industriale_cornetto_premium.txt`
- `bozza_presentazione_nuova_linea_snack_CDA.pptx`
- `preventivo_Criotech_tunnel_CR-SP180_rev2.pdf`
- `Fwd_preventivo_tunnel_surgelazione_Criotech_rev2.eml`
- `verbale_CDA_approvazione_investimento_tunnel.docx`
- `calcolo_CapEx_linea3_bakery_nuova.csv`
- `preventivo_software_ERP_CSB_System_vs_SAP.txt`
- `mail_titolare_Aurora_visione_aziendale_5anni.txt`

### `lotto_10_rumore_archivio.txt` — 18 grezzi

- `menu_mensa_aprile_maggio.txt`
- `volantino_convenzione_palestra.txt`
- `verbale_assemblea_condominio_capannone.txt`
- `ordine cancelleria marzo.txt`
- `preventivo_tinteggiatura_uffici_NON_ACCETTATO.txt`
- `noleggio_distributori_automatici_contratto.txt`
- `iscritti_cena_aziendale_dicembre.csv`
- `prenotazioni_sala_riunioni_maggio.csv`
- `segnalazione_guasto_cancello_carraio.txt`
- `elenco_interni_telefonici.txt`
- `elenco_chiavi_e_accessi.txt`
- `Fwd_newsletter_confindustria_marzo.txt`
- `manutenzione_fotocopiatrice_contratto_copie.csv`
- `fattura_antivirus_licenze_2026.txt`
- `modulo richiesta ferie VUOTO da stampare.txt`
- `corso_inglese_aziendale_proposta.txt`
- `~$ttera_risposta_Tosano_reclamo_BOZZA_v3.docx`
- `_QUESTO_ARCHIVIO_E_SIMULATO.txt`

**Totale: 138 grezzi**, cioe' i 138 restanti dopo la fetta pilota di 22.
