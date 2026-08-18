# Matrice dei lotti — canonizzazione del corpus v1

> **Cos'è** · Il piano di lavoro delle Sessioni 4-5: come i **138 grezzi non ancora
> canonizzati** si dividono in dodici lotti tematici, in che ordine si eseguono, con quale
> budget di note e con quali obblighi ciascuno.
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
| 2 | Igiene, sanificazione, autocontrollo, MOCA | 12 | 20-30 | — |
| 3 | Sistema qualità, certificazioni, audit, crisi | 13 | 22-32 | — |
| 4 | Filiera in entrata, fornitori, logistica | 14 | 26-36 | — |
| 5 | Commerciale: cliente, listini, marginalità | 15 | 28-38 | — |
| 6 | Amministrazione, bilancio, cassa | 15 | 28-40 | `amministrazione` |
| 7 | Persone: lavoro, organico, sindacato | 15 | 24-34 | `risorse-umane` |
| 8 | Sicurezza sul lavoro, ambiente, assicurazioni | 11 | 16-24 | `sicurezza-ambiente` |
| 9 | R&D, nuovi prodotti, investimenti, visione | 12 | 22-30 | `ricerca-sviluppo` |
| 10 | Rumore di fondo e forma dell'archivio | 18 | 14-22 | — |
| | **totale** | **138** | **246-352** | 4 hub d'area nuovi |

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
- ⚠️ **121 righe di strumento non fanno 121 note.** Vale la guardia contro la
  sovra-atomizzazione: il rapporto di lotto dichiara **il criterio con cui una riga diventa
  una nota**, e il revisore riceve un campione da verificare. Una selezione deve restare
  una selezione;
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
non a memoria.** Una riga può uscire solo in due modi: `chiusa` — la gamba è arrivata e la
nota lo dice — oppure `aperta dichiarata` — l'archivio non la chiude, e c'è una nota
`type: conflitto` che lo scrive. Nessuna riga sparisce.

Le righe qui sotto sono il **seme**, ricavato dagli obblighi di lotto e dalla lista di
tracciamento del gate S2 §6.2. Le questioni che nasceranno canonizzando si aggiungono qui.

| # | Questione | Aperta da | Gamba mancante attesa in | Stato |
|---|---|---|---|---|
| T1 | MOD-QA-07, tre versioni delle verifiche CCP3 dello stesso turno | pilota S2 | chiusa in **1A** | **aperta dichiarata** — `questione-verifiche-ccp3-10-05-tre-versioni`: il modulo scansionato registra 5 verifiche con le 16:00 e le 17:00 barrate, la trascrizione ne registra 8 comprese quelle, il quaderno ne dichiara 2 saltate. Nessuna delle tre prevale |
| T2 | Pezzi del turno L26130-L1-T2: il quaderno porta una terza fonte | pilota S2 | chiusa in **1A** | **aperta dichiarata** — `questione-pezzi-prodotti-l26130` estesa: il quaderno dà 4.100 «+ quelo di T1», ed è **l'unica delle tre fonti che dichiara il proprio perimetro** |
| T3 | Arrivo dell'officina al fermo PKM-450: 15:25 contro 15:50 | pilota S2 | chiusa in **1A** | **aperta dichiarata** — nota nuova `questione-arrivo-officina-fermo-pkm-450`: 25 minuti di scarto, nessun terzo documento con marca temporale |
| T4 | Codice dell'allarme PKM-450: `E-214 GAS` contro `AL-217` | pilota S2 | chiusa in **1A** | **aperta dichiarata** — l'estratto del manuale **non contiene la tabella allarmi** (assenza verificata sui 160 file del manifest con l'estrattore congelato) e usa una **terza codifica**, `A031` per la pressione gas. Serve il manuale completo, 184 pagine, che in archivio non c'è |
| T5 | Ora di arrivo della segnalazione del reclamo: 18:23 contro le 17:55 della catena mail | pilota S2 (canone, add. 16/08) | **lotto 3** (notifica del form del sito) | tracciata |
| T6 | Data di apertura di REC-2026-011: 12/05 sulla scheda, 13/05 secondo la responsabile qualità | pilota S2 | **lotto 3** (PRO-QA-08, procedura reclami) | tracciata |
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
| T17 | Azoto: la bolla Nordgas del 06/05 registra scarico **in serbatoio fisso** SB-AUR-01 e bombole solo di CO2; il quaderno dello stesso giorno scrive «bombola nordgas cambiata alle 16 ma durata poco» | **lotto 1A** (gamba del quaderno) | **lotto 1C** (bolla Nordgas) | tracciata — ⚠️ in 1A **la gamba del quaderno non ha ancora una nota propria**: metodo_03 §2.4 vuole ≥ 2 file diversi per un `conflitto`, quindi la nota nasce in 1B citando entrambi i grezzi |
| T18 | Frigotecnica **Berica** (contratto) contro Frigotecnica **Scaligera** (scheda manutenzione), sugli stessi impianti CF-02 e TS-01 | **lotto 1A** (gamba della scheda) | **lotto 1B** (contratto, che è una **bozza non firmata**) — ⚠️ **prima di dichiararle due aziende si verifica che non sia la stessa entità con due nomi**; se resta indecidibile è classe C in `alias_entita.md` | tracciata — come T17, in 1A la gamba esiste ma non ha nota propria: serve la seconda fonte |
| T19 | Linea 1 in produzione domenica 10/05 su tre turni, mentre il piano della settimana 19 non la prevede | **lotto 1A** — aperta: `questione-linea1-domenica-10-05-fuori-piano` | **lotti 5 e 7** — gamba della storia «domeniche della promo», vedi T12 | tracciata |
| T20 | Base metrologica dell'arbitrato datalogger contro registro cartaceo | **lotto 1A** — **gamba trovata dove non era prevista**: la scheda di manutenzione attesta le tarature delle sonde del PT-104, nota `fatto-sonde-pt-104-in-taratura` | **lotto 1C** (elenco tarature, per il datalogger `DL-001`) | tracciata |
| T21 | Sonda di conducibilità del CIP-01 con taratura scaduta dall'08/04/2026, «allarmi sonda su log maggio» | **lotto 1A** (scheda manutenzione) | **lotto 2** (log CIP e IO-05) | tracciata |
| T22 | Manutenzioni arretrate su CF-02 (assorbimenti scaduti dal 30/04, resistenze di sbrinamento rimandate) | **lotto 1A** (scheda manutenzione) | **lotto 1B** (log allarmi CF-02 e consumi) | tracciata |
| T23 | O2 residuo in confezione: la scheda tecnica prescrive **max 1,0 %**, il quaderno applica **«lim 2%»** | **lotto 1A** | — | **aperta dichiarata** — `questione-limite-o2-residuo`. In più la scheda **non dichiara a quale momento** della vita del prodotto valga il tetto: lacuna registrata in `doc-limite-o2-residuo-af-sn-0450` |
| T24 | aw e umidità di AF-SN-0450: scheda tecnica e **rapporto di prova del laboratorio accreditato** concordano su aw ≈ 0,93 e umidità ≈ 32 g/100 g; le prove di shelf life danno 0,31 e 5,6 % | **lotto 1A** | — | **aperta dichiarata** — `questione-aw-umidita-af-sn-0450`. ⚠️ **Il primo impianto della nota era rovesciato**: sembrava che la scheda tecnica fosse la fonte dubbia. Il ri-giudizio ha segnalato l'esistenza del rapporto di prova, che misura lo stesso lotto con metodo normato e dichiara **conformi** i valori della scheda. L'anomalia sta nel file delle prove, che è la base della proposta di TMC a sei mesi |
| T25 | Convalida annuale dell'`MD-3200`: la scheda di manutenzione la data al `06-feb-26` con scadenza `06/02/27`; l'elenco tarature dà altre date | **lotto 1A** | **lotto 1C** (elenco tarature) | tracciata |
| T26 | Kit dei tasselli di prova del CCP3: `TL-114` sul MOD-QA-07, `TST-CERT-KIT` sulla scheda di manutenzione, e una terza sigla nell'elenco tarature | **lotto 1A** — confronto dichiarato in `macchina-md-3200`, senza aprire una questione con due sole gambe deboli | **lotto 1C** (elenco tarature) | tracciata |
| T27 | Materiale della guarnizione **originale** della valvola azoto: PTFE (mail del costruttore), FKM (manuale della macchina), EPDM (piano di manutenzione) | **lotto 1A** — `questione-materiale-guarnizione-pkm-450` estesa | — | **aperta dichiarata**: due fonti su tre danno un fluoropolimero, la terza no, e nessun documento le mette a confronto |
| T28 | Codice del ricambio della valvola azoto: le sigle salgono da due a **quattro**, e due vengono dal costruttore stesso | **lotto 1A** — `questione-codice-ricambio-valvola-pkm-450` estesa | — | **aperta dichiarata** |
| T29 | Sonda di conducibilità del `CIP-01`, taratura scaduta dall'`2026-04-08`, «allarmi sonda su log maggio» | **lotto 1A** (scheda manutenzione) | **lotto 2** (log CIP e IO-05) | tracciata |
| T30 | Assorbimenti del compressore `CF-02` scaduti dal `30/04/26` e resistenze di sbrinamento rimandate, con «assorbimento anomalo segnalato 08/05» | **lotto 1A** (scheda manutenzione) | **lotto 1B** (log allarmi CF-02 e consumi) | tracciata |
| T31 | Proposta di R&D di portare il TMC a **sei mesi** contro i **45 giorni** della scheda tecnica in vigore | **lotto 1A** — registrata in `kpi-shelf-life-af-sn-0450` | **lotto 9** (R&D), se il corpus porta la revisione | tracciata — non è una contraddizione fra documenti: è una proposta contro una specifica in vigore |
| T32 | Posizione dell'`MD-3200` in linea: la scheda tecnica lo colloca **fra il raffreddamento e il confezionamento**, l'elenco attrezzature lo dà «Linea 1 - post confezionamento» | **lotto 1A** — trovata dallo strato di giudizio, che ha visto la nota affermare il contrario della propria fonte | **lotto 1C** (elenco tarature) | tracciata — cambia cosa il metal detector può intercettare |
| T33 | Il rapporto di prova del laboratorio contiene **prove chimico-fisiche** sul lotto L26130 che nessuna nota del pilota aveva canonizzato: aw, pH, umidità, cloruri, con metodo e incertezza | **lotto 1A** — trovato dal ri-giudizio | il grezzo appartiene alla fetta pilota: la lacuna di copertura si chiude qui, non in un lotto futuro | **chiusa** — le prove sono ora citate da `questione-aw-umidita-af-sn-0450` |
| T34 | Le note F-gas del contratto frigo nascono in `area: manutenzione`, perché è l'area che governa quei fatti oggi e **le note non traslocano** | **lotto 1B** — decisione del titolare del 19/08/2026 | **lotto 8**, alla nascita di `area-sicurezza-ambiente`: l'hub nuovo le **linka come rimandi laterali**, il `related` principale resta l'hub di manutenzione (E11) | tracciata — non è una divergenza dell'archivio: è un impegno di grafo che il lotto 8 deve onorare |

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

La matrice è un piano: si annota quando cambia, non si riscrive in silenzio.

| Data | Lotto | Cosa è cambiato, e perché |
|---|---|---|
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

### `lotto_02_igiene.txt` — 12 grezzi

- `log_lavaggio_CIP_linea1_maggio.log`
- `IO-05_istruzione_operativa_lavaggio_CIP.docx`
- `scheda_sicurezza_detergente_acido_lavaggio_CIP.txt`
- `registro_tamponi_superfici_listeria_salmonella.csv`
- `piano_autocontrollo_acqua_potabile_analisi.csv`
- `analisi_acque_reflue_autocontrollo_2026.xlsx`
- `scheda_allergeni_matrice_cross_contamination.docx`
- `formazione_allergeni_operatori_2026.pptx`
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
