# Revisione indipendente — Sessione 4, lotto 1B (freddo ed energia)

> **Cos'è** · Il rapporto del revisore indipendente sulle 29 note del lotto 1B, redatto col
> canone alla mano secondo `metodo_03_canonizzazione.md` §9.5. Chi scrive non ha scritto le note
> (divieto 35).
> **Quando si usa** · Al passo 3 del ciclo di lotto, prima delle correzioni propagate e della
> seconda passata di QA.
> **Cosa non toccare** · Nessuna nota è stata modificata: il revisore riporta, non corregge.

**Data:** 19/08/2026 · **Perimetro:** 29 note nuove in `areas\`, `data\`, `entities\`,
`workspace\` · **Grezzi del lotto:** `log_allarmi_cella_frigo_surgelati_aprile.log`,
`contratto_manutenzione_impianto_frigo_TS01.docx`,
`consumi_energetici_forni_kwh_maggio26.csv`, `bolletta_VenetaEnergia_maggio2026.pdf` ·
**Grezzi di lotti precedenti riverificati:** `scheda_manutenzione_ordinaria_forni_industrial.csv`,
`non_conformita_interne_registro_2026.csv`, `report_fermo_macchina_confezionatrice_MAP.txt`

**Esito in una riga:** nessuna fuga di canone, nessuna correzione di contraddizione voluta,
nessuna violazione del divieto 9-bis. **13 rilievi di categoria A** (nessuno strutturale sul
metodo, uno solo con effetto su un fatto affermato), **6 di categoria B**, **8 di categoria C**.

| Categoria | Numero |
|---|---|
| **A — errore vero** | 13 |
| **B — contraddizione non registrata** | 6 |
| **C — falso allarme** | 8 |

---

## A — errori veri

Ordinati per gravità. «Gravità» qui significa: quanto cambia ciò che il vault afferma.

### A1 · `entities/entita-frigotecnica-berica.md` — `FRIGOTEC-11` messo fra gli `aliases` — **alta**

- **Cosa c'è che non va.** Il campo `aliases` contiene `FRIGOTEC-11`. Nessuna fonte lega quella
  sigla a Frigotecnica Berica: il log la porta come identificativo dell'operatore esterno in
  assistenza, e nulla più. È un'inferenza fatta passare per dato (divieto 12), ed è aggravata dal
  fatto che **la stessa sessione tiene aperta la questione su chi sia il manutentore**
  (`questione-manutentore-frigo-berica-scaligera`): mettere la sigla negli alias di «Berica»
  decide nel campo macchina proprio ciò che la nota-questione dichiara indecidibile.
  `alias_entita.md` classe C: «non si uniscono e non si sceglie».
- **Prova sul grezzo.** `log_allarmi_cella_frigo_surgelati_aprile.log`, riga 08:55:02 del 24/04:
  `CF02 EVT SERVICE_MODE ON OP=EXT ID=FRIGOTEC-11` (e riga 11:40:47, `SERVICE_MODE OFF`). Sono le
  due sole occorrenze della sigla in tutto il file.
- **Cosa andrebbe fatto.** Togliere `FRIGOTEC-11` da `aliases`; lasciarlo nel corpo come sigla
  attestata dal log, senza attribuzione; aprire in `alias_entita.md` una riga di **classe C** che
  registra la sigla come riferimento non riconciliato.

### A2 · `areas/fatto-intervento-frigotecnica-24-04-cf-02.md` — l'attribuzione sta nel nome del file — **alta**

- **Cosa c'è che non va.** Il corpo della nota è impeccabile («un operatore esterno, identificato
  dalla sigla `FRIGOTEC-11`», e non dice mai chi sia). Ma **il nome del file** attribuisce
  l'intervento a Frigotecnica, e la scheda `entita-frigotecnica-berica` lo elenca sotto «Dove
  compare» come intervento **proprio**. Il nome e il grafo affermano ciò che il testo si è
  astenuto dall'affermare. Stessa radice di A1.
- **Prova sul grezzo.** Stessa riga 08:55:02 del 24/04. Il log non nomina nessuna impresa.
- **Cosa andrebbe fatto.** Rinominare in `fatto-assistenza-esterna-24-04-cf-02` (i nomi in
  `related` e negli hub vanno propagati), oppure — se si preferisce non rinominare — dichiarare
  in una riga, dentro la nota e dentro la scheda entità, che l'attribuzione è un'inferenza sulla
  sigla e resta appesa a `questione-manutentore-frigo-berica-scaligera`.

### A3 · `areas/questione-manutentore-frigo-berica-scaligera.md` — una terza fonte non cercata — **alta**

- **Cosa c'è che non va.** La nota dichiara che il contratto è l'unico documento che identifica
  l'impresa («nessun altro documento la identifica così») e costruisce su questo tutto il «Cosa
  servirebbe per chiuderla». Esiste però un **terzo grezzo, interno e operativo**, che nomina
  l'impresa: e nomina «Berica». La nota non lo cita, e nemmeno `entita-frigotecnica-berica` — che
  invece dovrebbe, perché metodo_03 §1.3 esempio 18 stabilisce che l'elenco interni **si spalma
  sulle schede entità**. Non chiude la questione, ma ne sposta il peso: due documenti interni su
  tre scrivono «Berica».
- **Prova sul grezzo.** `elenco_interni_telefonici.txt`, riga 34: «manutenzione frigo
  **Frigotecnica Berica** (h24)  0444 69 33 07». Il recapito h24 combacia con l'art. 4.3 del
  contratto («reperibilità telefonica 24 ore su 24»).
- **Cosa andrebbe fatto.** Aggiungere il file a `fonti` della questione e della scheda entità, con
  il locator; riformulare la riga «nessun altro documento la identifica così» e il «Cosa
  servirebbe per chiuderla». La questione resta aperta: manca ancora una fattura o un rapporto di
  intervento con partita IVA accanto al nome.

### A4 · `areas/fatto-integrita-log-allarmi-cf-02.md` — la coda del file è descritta male, tre volte — **media**

- **Cosa c'è che non va.** Tre affermazioni non reggono al riscontro:
  1. «la penultima ha il timestamp e un valore corrotti» — **falso**: la penultima riga ha il
     timestamp integro e i valori corrotti; è l'**antepenultima** ad avere il timestamp corrotto;
  2. in `## Fonti`: «riga 23:58:42 del 30/04, **l'ultima lettura leggibile**, seguita dalle **due**
     righe finali troncate e corrotte» — quella riga è **essa stessa corrotta**, e ne segue **una
     sola**;
  3. «431 letture della cella … *(contate: righe di tipo `RD` per ciascun impianto)*» — le righe
     `CF02 RD` nel file sono **432**. 431 è il numero delle sole righe **ben formate**, che è il
     criterio usato da `conteggi_lotto_1b.py` ma **non** quello dichiarato nella nota (§5.4: il
     criterio si scrive accanto al numero).
- **Prova sul grezzo.** `log_allarmi_cella_frigo_surgelati_aprile.log`, righe 1271-1273:
  `2026-04-30T23:55:1è CF02 RD TMAN=-19.ì2 …` (timestamp corrotto) ·
  `2026-04-30T23:58:42 CF02 RD TMAN=-19.4 TRIP=-1␀␀ù8.0 … COMP_H=<byte non valido>` (timestamp
  integro) · `2026-05-01T00:0#*^~~~~`. Conteggio `CF02 RD` sull'intero file: 432; `TS01 RD`: 429.
- **Cosa andrebbe fatto.** Riscrivere le due righe descrittive sulla coda del file e allineare il
  criterio dichiarato: o «righe `RD` ben formate», o il numero 432. Il fatto sostanziale della nota
  — il log è un tabulato ricostruito, non una registrazione — **non cambia**.

### A5 · `areas/fatto-cariche-f-gas-impianti-frigoriferi.md` — il quarto impianto frigorifero non è dichiarato — **media**

- **Cosa c'è che non va.** La nota parla dei «tre impianti frigoriferi». Il contratto ne elenca
  **quattro**: alla premessa a) compare anche la «cella surgelati del magazzino di Via Palù 3/A»,
  che l'art. 2 non carica perché un commento della direzione la esclude. La nota non dichiara né
  il quarto impianto né la sua esclusione, e il lettore del vault ne ricava che Aurora ha tre
  impianti frigoriferi soggetti. È lo stesso grezzo a dire il contrario.
- **Prova sul grezzo.** `contratto_manutenzione_impianto_frigo_TS01.docx`, §premessa a), quarto
  trattino: «cella surgelati del magazzino di Via Palù 3/A», con il commento «Fantin M. - il Palù
  lo teniamo fuori, ha ancora la garanzia dell'installatore fino a novembre 2026. Rientra col
  rinnovo».
- **Cosa andrebbe fatto.** Aggiungere una riga alla nota (l'impianto esiste, sta in un secondo
  sito, è escluso dall'oggetto per la garanzia dell'installatore) e valutare la nota padrona del
  magazzino di Via Palù — vedi la verifica 1, dove il tema è trattato come lacuna di copertura.

### A6 · `areas/fatto-anomalia-consumo-cf-02-maggio.md` — «l'officina interviene tre volte» — **media**

- **Cosa c'è che non va.** Il `summary` dichiara tre interventi dell'officina. Il file ne annota
  **due** — 16/05, «sbrinamento manuale Bissoli»; 24/05, «intervento tampone Dal Maso» — mentre
  l'annotazione del 12/05 è un rinvio alla manutenzione con ordine di lavoro, non un intervento
  eseguito, e quella dell'08/05 è la segnalazione iniziale. Conteggio non riscontrabile nelle
  fonti (guardrail 2, e §5.4 sui valori contati).
- **Prova sul grezzo.** `consumi_energetici_forni_kwh_maggio26.csv`, colonna `Note`: riga 47
  (08/05, «assorbimento in salita da stanotte?»), riga 72 (12/05, «compressore CF-02 spunti
  anomali - vedi manutenzione (OdL-26-0175)»), riga 96 (16/05), riga 146 (24/05).
- **Cosa andrebbe fatto.** Correggere il `summary` («due interventi e una segnalazione girata alla
  manutenzione»), oppure dichiarare il criterio di conteggio accanto al numero.

### A7 · `entities/macchina-ts-01.md` — manca la sezione `## Questioni aperte` — **media**

- **Cosa c'è che non va.** La nota è `type: entita`, `stato: aperto`, e ha una questione aperta che
  la riguarda (`questione-refrigerante-ts-01`), ma non ha la sezione `## Questioni aperte`: il
  rimando è annegato dentro «Dove compare», in mezzo agli altri. §5.3 impone che la scheda entità
  **linki la questione nella sezione «Questioni aperte»**, e §2.4 avverte che quel titolo è uno dei
  **due a nome fisso perché uno script li cerca**. Il confronto interno al lotto lo conferma:
  `macchina-cf-02`, scritta nella stessa sessione, la sezione ce l'ha.
- **Prova.** Struttura della nota (`## Identificazione` → `## Dove compare` → `## Da non confondere
  con` → `## Fonti`).
- **Cosa andrebbe fatto.** Estrarre `[[questione-refrigerante-ts-01]]` da «Dove compare» e metterla
  sotto `## Questioni aperte`.

### A8 · `areas/fatto-potenza-impegnata-e-preventivo-tunnel.md` — due fatti in una nota — **media**

- **Cosa c'è che non va.** La nota tiene insieme **il picco di potenza di maggio** (482,4 kW su 500
  impegnati) e **la richiesta di preventivo per 630 kW del 22/04**. Il test di §5.1: una risposta
  corretta userebbe le due affermazioni **insieme**, non l'una al posto dell'altra → sono due
  fatti, e servono due note. Il sintomo è nel frontmatter: `data_fatto: 2026-04-22` data la nota
  sull'evento secondario mentre la tabella principale è di maggio, e la nota è per metà fuori dalla
  finestra della sua stessa data.
- **Prova sul grezzo.** `bolletta_VenetaEnergia_maggio2026.pdf`, pag. 1 §caratteristiche tecniche e
  §1 «LETTURE E CONSUMI» riga `Potenza max prelevata (kW)` = 482,4 (dato di maggio) · pag. 4
  §comunicazioni al cliente, «Vs. richiesta prot. VE-2026-3391 del 22/04/2026 (preventivo potenza
  630 kW…)» (evento di aprile).
- **Cosa andrebbe fatto.** Spezzare in due note — la saturazione della potenza (`data_fatto:
  2026-05-31`) e la pratica di aumento di potenza per il tunnel (`data_fatto: 2026-04-22`) — che si
  linkano fra loro. La seconda appartiene con naturalezza al filo del tunnel nuovo.

### A9 · `areas/fatto-energia-reattiva-oltre-soglia.md` — «meno di un millesimo» — **bassa**

- **Cosa c'è che non va.** «L'importo è piccolo — meno di un millesimo del totale della fattura».
  39,95 € su 34.044,10 € è **1,17 ‰**, cioè **più** di un millesimo (il millesimo sarebbe 34,04 €).
  Anche sull'imponibile, 30.949,18 €, il rapporto è 1,29 ‰.
- **Prova sul grezzo.** `bolletta_VenetaEnergia_maggio2026.pdf`, pag. 3 §3, riga `REATT` (39,95 €)
  e pag. 1 §sintesi importi (`TOTALE DA PAGARE  34.044,10`).
- **Cosa andrebbe fatto.** «poco più di un millesimo», oppure il valore dichiarato come calcolato.
  Il punto della nota — l'importo non conta, il segnale sì — regge comunque.

### A10 · `areas/area-amministrazione.md` e `entities/entita-veneta-energia.md` — locator con una colonna che non esiste — **bassa**

- **Cosa c'è che non va.** Entrambe chiudono con «`consumi_energetici_forni_kwh_maggio26.csv` —
  **riga 1, colonna `intestazione`**». Nel file la colonna `intestazione` non esiste: la riga 1 è la
  riga di titolo, e l'intestazione delle colonne è la riga 2. Locator fuori dalla grammatica chiusa
  di §2.3 e parafrasi al posto di un riferimento (divieto 18).
- **Prova sul grezzo.** `consumi_energetici_forni_kwh_maggio26.csv`, riga 1: `LETTURE CONTATORI DI
  REPARTO - MAGGIO 2026 - fornitore: Veneta Energia S.p.A. (F0081) - a cura L.Trentin;;;;;;;;;` ·
  riga 2: `Data;Centro_costo;kWh_F1;…`.
- **Cosa andrebbe fatto.** Scrivere semplicemente «riga 1».

### A11 · `entities/entita-veneta-energia.md` — «Da non confondere con» usato per un non-omografo — **bassa**

- **Cosa c'è che non va.** La sezione «Da non confondere con» rimanda a
  `[[entita-frigotecnica-berica]]`. Le due entità non sono confondibili in nessun senso: quella
  sezione serve alla entity resolution (`alias_entita.md`, classe B: «quasi-omografi che sono
  soggetti diversi»), e riempirla con un accostamento tematico la svuota proprio dove servirà. Ha
  anche l'aria di un link aggiunto per arrivare al minimo (divieto 25).
- **Prova.** Testo della sezione: «è il manutentore degli impianti frigoriferi, non il venditore di
  energia».
- **Cosa andrebbe fatto.** Togliere la sezione (o spostare il rimando fra i `related`). Se serve una
  vera riga «Da non confondere con», il candidato è il **distributore e-distribuzione**, che la
  fattura distingue esplicitamente dal venditore.

### A12 · `data/questione-costo-energia-elettrica.md` — assenza dichiarata senza la formula di verifica — **bassa**

- **Cosa c'è che non va.** «Il documento che fissa il valore di 0,182 €/kWh — una nota di budget, un
  listino, una delibera interna — **che in archivio non c'è**». È l'affermazione di un'assenza, e
  il divieto 12-bis (con E22) impone di dichiararla come tale: «verificata su tutto `sources\`,
  manifest v1.1, alla `data_nota` di questa nota». Le altre note del lotto usano la formula
  correttamente; questa no.
- **Verifica del revisore.** L'assenza **regge nel merito**: cercando `0,182` / `0.182` con
  l'estrattore congelato su tutti e 160 i file del manifest v1.1, il valore compare solo in
  `consumi_energetici_forni_kwh_maggio26.csv` (colonna `Costo_unit_EUR`). Le occorrenze in
  `analisi_marginalita_per_referenza_2026.xlsx` sono coincidenze di sottostringa (0,1829 e 0,2055
  €/pz, non €/kWh).
- **Cosa andrebbe fatto.** Aggiungere la formula di dichiarazione dell'assenza.

### A13 · `areas/fatto-obblighi-registro-f-gas.md` — un fatto del 10/05 affermato da una nota che non ne ha la fonte — **bassa**

- **Cosa c'è che non va.** «…la **non conformità 2 dell'audit** del febbraio 2026 sui ricambi
  custoditi in produzione — **la stessa che il 10/05 si materializza sulla confezionatrice**». La
  seconda metà è un fatto del 10/05, e l'unica fonte della nota è il contratto, che non lo contiene.
  Guardrail 2: ciò che una fonte lascia intendere ma non dice si scrive come inferenza dichiarata,
  o non si scrive.
- **Prova sul grezzo.** `contratto_manutenzione_impianto_frigo_TS01.docx`, §art. 5.4, commento
  «Marchetti E. - clausola inserita dopo la NC 2 dell'audit CSQA di febbraio (BRCGS cl. 4.7.5,
  attrezzi e ricambi in area produttiva)». Il commento si ferma qui: non nomina il 10/05.
- **Cosa andrebbe fatto.** Riformulare come rimando («la stessa non conformità che
  `[[fatto-riparazione-guarnizione-non-originale]]` ritrova sulla confezionatrice») invece che come
  affermazione propria.

---

## B — contraddizioni non registrate

Divergenze reali del corpus, **con entrambe le gambe già canonizzate**, che il canone non
elenca in nessuno dei tre gruppi né nelle aggiunte del 16/08 e del 18/08. Per ciascuna serve, per
§9.5, una nota-questione e una riga di canone in sezione datata.

### B1 · La non conformità sul tunnel e il log che non la sorregge

| Gamba | Locator |
|---|---|
| `NC-2026-067` del **10/04/2026**: «TS-01 allarme sbrinamento ricorrente, **3 eventi in settimana**, capacita ridotta», causa «obsolescenza impianto», gravità alta, `IN CORSO`, costo stimato 2.600 € | `non_conformita_interne_registro_2026.csv`, riga `NC-2026-067`, colonne `Descrizione` e `Causa_radice` |
| Il log dello **stesso mese e dello stesso impianto** non contiene **nessun** evento di sbrinamento né allarme del tunnel: tutti i 192 `DEFROST_START` portano il prefisso `CF02`, e le uniche righe `TS01` sono 429 letture `RD` più il `SYS BOOT` del 21/04 | `log_allarmi_cella_frigo_surgelati_aprile.log`, righe `TS01 …` (conteggio verificato: 429 `RD`, 1 `SYS`, 0 `EVT`) |

**Valore da preferire: nessuno.** O il log non copre gli eventi del tunnel — pur avendone le
letture — o la non conformità attribuisce all'impianto sbagliato ciò che stava succedendo alla
cella, che negli stessi giorni sbrina otto e poi dodici volte al giorno. L'archivio non decide.
⚠️ La divergenza **è già dichiarata** dentro `fatto-nessuna-nc-per-allarmi-cf-02`, in un ⚠️ finale,
e la nota fa bene a non scegliere. Ma §5.3 vuole una nota `type: conflitto` propria, linkata
dall'hub e dall'`_index`: così com'è, chi naviga per questioni aperte non la trova.

### B2 · L'azione correttiva che introduce una soglia già in vigore

| Gamba | Locator |
|---|---|
| `NC-2026-114` del **30/05/2026**, azione correttiva: «riparazione fermo porta, **allarme porta aperta ridotto a 5 min**» | `non_conformita_interne_registro_2026.csv`, riga `NC-2026-114`, colonna `Azione_correttiva` (riga con separatore virgola anziché punto e virgola) |
| Il **15/04/2026** il limite era **già** cinque minuti: `CF02 EVT ALARM DOOR_TIMEOUT LIM=00:05:00 ACK=NO` | `log_allarmi_cella_frigo_surgelati_aprile.log`, riga 10:27:41 del 15/04 |

**Valore da preferire: nessuno.** O l'azione correttiva descrive come nuovo un parametro che
esisteva già un mese e mezzo prima, o il limite era stato allargato e poi riportato indietro senza
che nessun documento lo registri. Stessa situazione di B1: la divergenza è **dichiarata dentro**
`fatto-porta-cella-cf-02-aperta-38-minuti` ma non ha nota-questione né riga di canone.

### B3 · L'azione correttiva di gennaio che il log di aprile non conferma

| Gamba | Locator |
|---|---|
| `NC-2026-017` del **30/01/2026**, gravità alta, **CHIUSA** il 03/02: causa «sbrinamento evaporatore programmato in orario di carico», azione «**spostato ciclo sbrinamento su fascia notturna**» | `non_conformita_interne_registro_2026.csv`, riga `NC-2026-017`, colonne `Causa_radice`, `Azione_correttiva`, `Data_chiusura`, `Stato` |
| In aprile gli sbrinamenti della CF-02 sono distribuiti **sulle ventiquattro ore**: dal 01 all'11/04 quattro al giorno alle ~04, ~10, ~16 e ~22; dal 12/04 otto al giorno; dal 20/04 dodici | `log_allarmi_cella_frigo_surgelati_aprile.log`, righe `CF02 EVT DEFROST_START` (es. 04:02:04, 10:00:15, 16:01:20, 22:03:17 del 01/04) |

**Valore da preferire: nessuno.** Una non conformità di gravità alta chiusa in quattro giorni con
un'azione che il dato di due mesi dopo non evidenzia. È **la divergenza più utile del lotto per il
tema «la cella surgelati»**, perché tocca l'efficacia di un'azione correttiva chiusa — cosa che
BRCGS e IFS chiedono di verificare — ed è l'unica delle sei che **nessuna nota ha visto**.

### B4 · Due percentuali per lo stesso incremento, dentro la stessa fattura

| Gamba | Locator |
|---|---|
| «ctr budget energia mag: **+9,4% su apr**» | `bolletta_VenetaEnergia_maggio2026.pdf`, pag. 4, §riepilogo sintetico per la contabilità |
| Il grafico dei dodici mesi della **stessa fattura** dà `apr26 169.302` e `mag26 178.480`, cioè **+5,4 %** *(calcolato)* | `bolletta_VenetaEnergia_maggio2026.pdf`, pag. 2, §grafico consumi ultimi 12 mesi |

**Valore da preferire: nessuno, e il perimetro non è dichiarato.** Il +9,4 % potrebbe essere in
euro anziché in kWh — il contratto è indicizzato al PUN, quindi i due possono divergere
legittimamente — ma **la fattura non lo dice**, e le fatture di aprile non sono in archivio.
`fatto-tre-domeniche-produttive-in-fascia-f3` cita l'annotazione contabile per intero, +9,4 %
compreso, senza confrontarla col grafico che sta due pagine prima: è esattamente il confronto che
§5.1-bis rende obbligatorio dentro il lotto.

### B5 · Il terzo Peruffo — quasi-omografo non registrato

| Soggetto | Locator |
|---|---|
| **Attilio Peruffo**, legale rappresentante di Frigotecnica Berica S.r.l., Montecchio Maggiore (VI) | `contratto_manutenzione_impianto_frigo_TS01.docx`, §intestazione delle parti e §firme; compare anche come autore di due commenti di trattativa, «Peruffo A. (Frigotecnica)» |
| **Peruffo Maria Grazia**, revisore legale, Registro n. 148223, nomina 28/04/2025 | `visura_camerale_ordinaria_AuroraFoodGroup.pdf` |
| **Peruzzi Maurizio**, revisore legale unico, Registro n. 118442, nomina 14/05/2024 | `bilancio_esercizio_2025_deposito_CCIAA.pdf` |

Non è una divergenza fra valori: è una **trappola di entity resolution** che il corpus ora contiene
in tre esemplari. `alias_entita.md` registra già la coppia Peruffo/Peruzzi in **classe B**; il
terzo omografo non è registrato da nessuna parte, e né `entita-frigotecnica-berica` né le schede
dei revisori portano un «Da non confondere con». Un retrieval per «Peruffo» oggi restituisce due
persone senza avvisare che sono tre.
**Cosa andrebbe fatto.** Riga di classe B in `alias_entita.md` e «Da non confondere con» su
`entita-frigotecnica-berica`.

### B6 · Due date per la stessa procura, nella stessa riga

| Gamba | Locator |
|---|---|
| «in persona del Direttore di Stabilimento ing. Marco Fantin, **giusta procura del 15/09/2024 03/11/2025**» — due date affiancate, senza congiunzione | `contratto_manutenzione_impianto_frigo_TS01.docx`, §intestazione delle parti |

È un'**incoerenza intra-file**, prodotta dalle «revisioni NON accettate» che il documento dichiara
in testa — lo stesso meccanismo dei due canoni dell'art. 9.1 (`Euro 14.800,00` / `Euro 16.200,00`),
che invece è stato canonizzato in `bozza-contratto-manutenzione-frigo`. Per il precedente fissato
dal canone il 18/08 sul riepilogo della scheda di manutenzione, un'incoerenza intra-file **si
scrive come nota che la dichiara, non come questione aperta**. Qui non è scritta da nessuna parte,
e il potere di firma del direttore di stabilimento non è un dettaglio di forma.

---

## C — falsi allarmi

Da annotare nel decision log perché non tornino al lotto successivo.

### C1 · I numeri della quadratura dei consumi: hanno ragione le note, non il canone

Il canone (§«Un caso che sembra un errore e non lo è») dichiara **59** righe in cui la somma delle
fasce non fa il totale, **137** in cui il costo non è totale × tariffa, e «**165 righe su 165**»
entro 1,5 kWh dal consumo reale. `kpi-quadratura-consumi-energetici-maggio` scrive **68**, **174** e
**186 su 186**, e sembra quindi contraddire il canone.

Ho ricontato in modo indipendente sul grezzo: **186 righe di dato** (prima colonna una data), **68**
con somma fasce ≠ totale, **174** con costo ≠ totale × tariffa, **186 su 186** entro 1,5 kWh dal
consumo ricavato come costo ÷ tariffa. **Le note hanno ragione.** L'indizio su come nasce il numero
del canone: le righe con data in formato `gg/mm/aa` sono esattamente **165**, e le altre **21** sono
in `aaaa-mm-gg` — l'analisi che ha prodotto «165 su 165» leggeva solo il primo formato.

**Nessuna nota va toccata.** Va invece **emendato il canone**, in sezione datata: il divieto 36
(«non dichiarare un numero che uno script non ha ricontato») vale esplicitamente anche per i numeri
scritti nei documenti di metodo. La conclusione qualitativa del canone — non sono errori di
calcolo, sono arrotondamenti — **resta intatta ed è confermata**.

### C2 · L'`RTC=NOSYNC` è del tunnel, non della cella: la nota non sta correggendo il canone

La riga di canone «Integrità del log cella» dice «dopo il riavvio del 21/04 l'orologio è
`RTC=NOSYNC`». `fatto-integrita-log-allarmi-cf-02` **distingue**: alla ripartenza il tunnel dichiara
`RTC=NOSYNC` mentre la cella dichiara `RTC=SYNC`, e avverte che confonderle «significherebbe
togliere valore proprio agli allarmi di temperatura, che restano datati». Sembrava una correzione di
contraddizione voluta (guardrail 3). **Non lo è:** la nota legge il grezzo alla lettera —
`log_allarmi_cella_frigo_surgelati_aprile.log`, riga 03:19:11 `CF02 SYS BOOT … RTC=SYNC` e riga
03:19:13 `TS01 SYS BOOT … RTC=NOSYNC` — e la conclusione del canone («il log non è utilizzabile come
evidenza in audit») resta in piedi sugli altri due difetti. È semmai la formulazione del canone a
essere lasca, e vale la pena precisarla quando lo si emenda per C1.

### C3 · Le tre domeniche: nessuna violazione del divieto 9-bis

`fatto-tre-domeniche-produttive-in-fascia-f3` tocca un tema su cui il canone registra già una
contraddizione a tre gambe (libro unico: due domeniche; consumi/budget/RSU: tre; conferma d'ordine:
26/04, 03/05, 10/05). Sospetto di anticipazione. **Verificato: la nota registra solo la propria
gamba** — l'attestazione del fornitore di energia — non nomina nessuna fonte non canonizzata, e
rimanda a `questione-linea1-domenica-10-05-fuori-piano`, che è nel vault dal lotto 1A. L'unica frase
generica («l'archivio contiene altre fonti sulle domeniche di maggio») non nomina né numera nulla.
Corretto così.

### C4 · Il costo dell'energia: tacere sullo 0,205 del CapEx è la scelta giusta

Il canone registra la coppia «0,182 €/kWh nei consumi mensili · 0,205 nel CapEx». La nota
`questione-costo-energia-elettrica` non nomina lo 0,205 e apre invece il confronto fra 0,182 e i due
valori ricavabili dalla fattura. Sembrava una questione monca. **Non lo è:**
`calcolo_CapEx_linea3_bakery_nuova.csv` non è fra i grezzi del lotto né canonizzato altrove, quindi
il divieto 9-bis impone il silenzio: la divergenza 0,182/0,205 nascerà nel lotto che porta dentro il
CapEx. La nota si è fermata al punto giusto — ed è la stessa disciplina la cui assenza aveva
prodotto le due sole fughe di canone del progetto.

### C5 · I totali per centro di costo che non coincidono con la tabella in coda

Le somme delle righe giornaliere (41.237 · 16.740 · 4.292 · 3.390) non coincidono con la tabella
«CONFRONTO MAGGIO 2025» dello stesso file (41.252 · 16.739 · 4.290 · 3.391). Sembra un errore.
**Non lo è:** gli scarti di 15, 1, 2 e 1 kWh sono compatibili con la somma di 31 arrotondamenti
all'intero per centro di costo, e il file dichiara in coda due giornate di letture stimate. Due
centri su sei coincidono al kWh. `kpi-consumi-energia-maggio-2026` mette le due colonne una accanto
all'altra, dichiara lo scarto e **non lo risolve**: è esattamente ciò che §5.2-§5.3 chiedono.

### C6 · Nessuna non conformità sulla CF-02 in aprile

Sembrava un'affermazione forte da verificare. **Verificata:** il registro apre 22 non conformità in
aprile, da `NC-2026-060` (01/04) a `NC-2026-081` (30/04), e nessuna riguarda la cella; le voci
CF-02 del 2026 sono di gennaio (`NC-2026-017`), febbraio (`NC-2026-025`), marzo (`NC-2026-050`) e
maggio (`NC-2026-107`, `NC-2026-114`). Anche la caratterizzazione del registro di aprile fatta dalla
nota è esatta (micro-fermate `NC-2026-073`, CCP2 mancante `NC-2026-068`, film MAP fuori FEFO
`NC-2026-078`, tensione di cassa `NC-2026-080`).

### C7 · Il tunnel nel log: nessun fatto nascosto sul CCP4

Le 429 letture `TS01 RD` sono l'unica evidenza continua in archivio della temperatura di uscita del
prodotto surgelato, e il CCP4 prescrive ≤ −18 °C. Sospetto di un fatto grosso non canonizzato.
**Verificato: non c'è.** Con nastro attivo (`BELT=1`, 180 letture su 15 giornate di aprile)
`TPRODOUT` sta sempre fra −18,6 e −20,8 °C: nessuna deviazione. Il lotto non ha mancato nessuna
anomalia su quel fronte — semmai c'è un'evidenza **positiva** che nessuno possiede (vedi verifica 1).

### C8 · La doppia menzione dell'`RTC=NOSYNC` in due note

`fatto-blackout-21-04-riavvio-centraline` e `fatto-integrita-log-allarmi-cf-02` riportano entrambe
le due righe `SYS BOOT`. Sembrava una violazione di «un fatto, un padrone» (divieto 19). **Non lo è:**
i due fatti sono distinti — il primo è *l'evento* (31 minuti senza tensione, due centraline
riavviate), il secondo è *il valore probatorio* del file — e la nota sul blackout rimanda
esplicitamente all'altra come padrona della conseguenza documentale. È il caso di scuola di §1.2
(«lo stesso grezzo alimenta spesso una nota per parte, e non è una duplicazione»).

---

## Verifica 1 — Copertura dei fatti chiave

### Le quattro righe di canone che il titolare ha nominato: tutte coperte

| Riga di canone | Nota padrona | Esito |
|---|---|---|
| **Allarmi della cella surgelati** — sei allarmi in escalation da −16,1 a −11,4 °C fra il 10 e il 26/04, cinque con `ACK=NO`; nessuna NC aperta | `fatto-allarmi-alta-temperatura-cf-02-aprile` + `fatto-nessuna-nc-per-allarmi-cf-02` | ✅ **coperta e verificata riga per riga.** Le sei aperture, i sei reset, le temperature, gli scarti dal set point, le durate e i sei `ACK` combaciano col log. La lettura del canone — «l'anomalia CF-02 segnalata il 12/05 era leggibile un mese prima» — è resa dal rimando fra `fatto-anomalia-consumo-cf-02-maggio` e la nota di aprile |
| **Integrità del log cella** — `DUR=` nel record di apertura, `RTC=NOSYNC` dopo il riavvio | `fatto-integrita-log-allarmi-cf-02` | ✅ coperta, con la precisazione di C2 e i tre difetti descrittivi di A4 |
| **Consumi energetici** — il file che non supera una verifica aritmetica ingenua ma non è difettoso | `kpi-quadratura-consumi-energetici-maggio` (+ `kpi-consumi-energia-maggio-2026`) | ✅ coperta, con la correzione dei numeri **a favore delle note**: vedi C1 |
| **Domeniche di maggio** | `fatto-tre-domeniche-produttive-in-fascia-f3` | ✅ coperta per la sola gamba del lotto, nel rispetto del divieto 9-bis: vedi C3 |

### Fatti che i quattro grezzi attestano e che sono rimasti senza padrone

1. **La cella surgelati del magazzino di Via Palù 3/A** — quarto impianto frigorifero, in un
   **secondo sito**, escluso dall'oggetto del contratto per la garanzia dell'installatore fino a
   novembre 2026 (`contratto_manutenzione_impianto_frigo_TS01.docx`, §premessa a) e commento
   Fantin). Nessuna nota. È la lacuna più rilevante, perché il sito è attestato in tutto il corpus —
   `manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt` righe 32 e 179 («magazzino di prodotto finito
   surgelato sito in Via Palù 3/A»), `Rilievo_Audit_BRC_IFS_CSQA_febbraio2026.txt` riga 10 («Sito
   aggiuntivo / Additional storage»), `elenco_attrezzature_taratura_strumenti_2026.csv` righe 12, 24
   e 57 (tre strumenti della cella surgelati del Palù, **tutti con taratura SCADUTA**),
   `report_costi_fissi_OpEx_manutenzioni.txt` — e il lotto del freddo è il posto naturale in cui
   almeno dichiararlo. Vedi anche A5.
2. **CF-01, cella a +4 °C** — nessuna scheda entità, benché tre grezzi di questo lotto la
   descrivano: contratto §art. 2.3 (R134a, 12,0 kg, GWP 1.430, 17,2 t CO2eq),
   `scheda_manutenzione_ordinaria_forni_industrial.csv` righe 53-55,
   `consumi_energetici_forni_kwh_maggio26.csv` riga 196 (+22,3 % anno su anno, il secondo scarto
   dopo la CF-02). `alias_entita.md` §A.4 prevede già il nome padrone `macchina-cf-01`, e oggi il
   nome non esiste. La CF-01 compare inoltre fra i quattro punti critici del preavviso di ispezione
   ATS (`NC-2026-107`, «intonaco cella CF-01»).
3. **Il metano dei forni** — la colonna `m3_metano` del CSV porta **31 righe di dato per 27.536 m³**
   *(sommati dal revisore)*, ed è l'unico vettore energetico non elettrico misurato nel corpus. La
   bolletta di Veneta Energia è solo elettrica. Nessuna nota lo possiede:
   `fatto-forni-in-temperatura-durante-fermo-10-05` ne cita tre giorni come contorno. È un buco
   visibile in un lotto che si chiama «energia».
4. **Evidenza positiva sul CCP4** — le 429 letture `TS01 RD` mostrano `TPRODOUT` sempre fra −18,6 e
   −20,8 °C nelle 15 giornate di nastro attivo (vedi C7). Non è un'anomalia, ma è **l'unica evidenza
   continua di conformità del CCP4** in tutto l'archivio, e in un vault costruito per rispondere a
   un auditor vale una nota `data\` breve.
5. **`alias_entita.md` non è stato esteso per il lotto 1B.** Il «Registro delle aggiunte» si ferma al
   lotto 1A. Mancano: classe A — `CELLA SURGELATI CF-02` (dal CSV), `Veneta Energia S.p.A.` /
   `F0081` / POD `IT001E63488210`, `Frigotecnica Berica` con la sua P.IVA e il certificato
   `IT-FG-0044821`, `TS01`/`CF02` come scritti nel log; classe B — Attilio Peruffo (B5); classe C —
   Berica contro Scaligera, R404A contro R448A, e `FRIGOTEC-11` (A1). Il file dichiara di sé
   «questo file **cresce**: ogni sessione che canonizza aggiunge le varianti nuove che incontra».

### Cosa invece è coperto e regge

Tutti e nove i tipi di evento del log hanno una nota padrona: 6 `ALARM HIGH_TEMP`, `DOOR_TIMEOUT`,
`PROBE_FAIL`, `POWER_FAIL`, i 192 `DEFROST_START`/`END`, i due `PARAM_CHANGE`, i due
`SERVICE_MODE`, il `MANUAL_DEFROST`, i due `SYS BOOT`. Sul lato energia: fattura, contatori di
reparto, quadratura del file, copertura dei contatori sul prelievo, reattiva, potenza, fasce
orarie. Sul lato contratto: cariche F-gas, obblighi F-gas, dismissione del tunnel, identità del
manutentore, refrigerante, natura di bozza. Le due domande di riconciliazione incrociata previste da
§5.1-bis che il lotto **ha** eseguito bene sono il ponte fra il log di aprile e i consumi di maggio
sulla CF-02, e fra il file dei consumi e il rapporto di fermo del 10/05 sui forni rimasti in
temperatura: quest'ultima è la nota migliore del lotto.

---

## Verifica 2 — Sovra-atomizzazione

**Esito: nessuna sovra-atomizzazione.** Ho campionato **dodici** note, non otto, chiedendomi per
ciascuna qual è la domanda a cui è la risposta migliore.

| Nota | Domanda a cui risponde | Esito |
|---|---|---|
| `fatto-allarmi-alta-temperatura-cf-02-aprile` | «La cella surgelati è andata fuori temperatura ad aprile?» | ✅ |
| `fatto-integrita-log-allarmi-cf-02` | «Quel log lo posso portare in audit?» | ✅ domanda diversa dalla precedente, e con risposta opposta |
| `fatto-porta-cella-cf-02-aperta-38-minuti` | «La porta della cella è mai rimasta aperta oltre il limite?» | ✅ |
| `fatto-sonda-prodotto-cf-02-in-avaria` | «La temperatura del prodotto è sempre stata misurata?» | ✅ |
| `fatto-blackout-21-04-riavvio-centraline` | «C'è stata un'interruzione di alimentazione?» | ✅ |
| `kpi-sbrinamenti-cf-02-aprile` | «Quanto sbrinava la cella, e la cadenza è cambiata?» | ✅ il numero è il soggetto: `data\` è la cartella giusta |
| `fatto-nessuna-nc-per-allarmi-cf-02` | «Quegli allarmi sono finiti in una non conformità?» | ✅ |
| `kpi-consumi-energia-maggio-2026` | «Quanto ha consumato ciascun reparto a maggio?» | ✅ |
| `kpi-quadratura-consumi-energetici-maggio` | «Di quel file mi posso fidare?» | ✅ è la domanda che il canone dichiara decisiva, e merita la sua nota |
| `fatto-contatori-reparto-meta-stabilimento` | «I contatori di reparto coprono lo stabilimento?» | ✅ la migliore del gruppo energia: risponde a una domanda che nessuno si pone e che cambia ogni conto |
| `fatto-cariche-f-gas-impianti-frigoriferi` / `fatto-obblighi-registro-f-gas` | «Quanto gas c'è?» contro «chi risponde degli adempimenti?» | ✅ due domande, due note. Il test di §5.1 (l'una **al posto** dell'altra?) dà no |
| `fatto-forni-in-temperatura-durante-fermo-10-05` | «Il fermo del 10/05 ha avuto un costo energetico?» | ✅ nasce dall'incrocio fra due lotti, ed è il tipo di nota che il metodo vuole |

**Il rischio in questo lotto è l'opposto**: una nota che tiene **due** fatti
(`fatto-potenza-impegnata-e-preventivo-tunnel`, rilievo A8). Le uniche sovrapposizioni notate — la
doppia menzione dell'`RTC=NOSYNC` (C8) e la doppia menzione dello scarto fra somme e tabella di
confronto in `kpi-consumi` e `kpi-quadratura` — hanno in entrambi i casi una padrona dichiarata e un
rimando esplicito: non sono spezzatino.

Nessuna nota è nata «per file»: i quattro grezzi hanno prodotto 29 note ma **nessuna** delle 29 ha
per soggetto un documento, salvo le due che devono averlo per natura
(`bozza-contratto-manutenzione-frigo`, che è una bozza, e `fatto-integrita-log-allarmi-cf-02`, che
ha per soggetto il valore probatorio di un file).

---

## Verifica 3 — Il caso della bozza

**Esito: la costruzione regge.** Il `.docx` si dichiara «bozza rev.3 del 22/01/2026 - revisioni NON
accettate - copia di lavoro uff. tecnico», ha le firme su righe vuote e la data del luogo in bianco;
la nota descrittiva sta in `workspace\` come vuole il **passo 2** dell'albero di §1.1, e i fatti che
il documento **riporta** stanno in `areas\`. Nessuna delle quattro note che usano il file presenta
le clausole come prescrizioni in vigore senza qualificarle.

**La distinzione che tiene in piedi la scelta** è quella dichiarata da
`fatto-cariche-f-gas-impianti-frigoriferi`: le cariche di refrigerante **non sono una clausola in
trattativa**, perché l'art. 2.4 dichiara che sono «quelle risultanti dai registri di apparecchiatura
alla data di stipula» — un dato riportato, non un patto. Il documento non firmato resta una fonte
valida per ciò che **attesta**; non lo è per ciò che **pattuisce**. Le note lo applicano
correttamente, e i punti veramente in trattativa — canone 14.800/16.200, tempi di intervento nei
festivi, penali, proprietà dei 48 kg di R404A recuperati, clausola `b-bis)` «[da definire]» — stanno
**tutti e cinque** nella nota di `workspace\`, come punti aperti, e in nessun'altra.

**Tre riserve, in ordine di peso.**

1. **`fatto-obblighi-registro-f-gas` è la nota più esposta del gruppo.** Il suo soggetto **è** la
   ripartizione contrattuale degli obblighi, cioè precisamente ciò che una bozza non firmata non
   stabilisce. Il `summary` qualifica correttamente («La bozza di contratto mette in capo al
   manutentore…»), ma il **titolo** afferma al presente («Chi tiene il registro F-gas degli impianti
   di Aurora») e la tabella «A chi tocca» è scritta come se il riparto fosse vigente; l'avvertenza
   arriva **in fondo**. Nel RAG la nota è un chunk solo e l'avvertenza viaggia con essa, quindi il
   danno è contenuto — ma titolo e prima riga sono ciò che il retrieval mostra per primo.
   *Suggerimento:* portare «secondo la bozza rev. 3, non firmata» nel titolo o nella prima riga del
   corpo.
2. **La penale di 250 € è enunciata come vigente**: «La responsabilità del manutentore **è**
   assistita da una penale di 250,00 € per ogni comunicazione omessa o tardiva». È un patto, non un
   dato riportato, e sta nella metà del documento che non è in vigore. Stessa medicina della riserva
   1.
3. **`fatto-ts-01-fine-vita-dismissione` regge bene** perché non poggia sulla sola bozza: mette tre
   fonti indipendenti a confronto (piano di manutenzione riga 42, premessa d) del contratto,
   `NC-2026-067`) e la premessa d) è una **constatazione di fatto** («è previsto nel corso del 2026
   l'avvio del cantiere…, come da ordine CapEx della Committente»), non una clausola. Le conseguenze
   contrattuali della dismissione — riduzione del canone, proprietà del gas — sono correttamente
   marcate come non decise.

Nessuna nota di `areas\` afferma che il contratto sia in vigore; `bozza-contratto-manutenzione-frigo`
dichiara al contrario, con la formula di verifica dell'assenza, che «ciò che l'azienda applica
davvero con il manutentore non risulta da nessun documento dell'archivio». Il collocamento in
`workspace\` è corretto anche per il metabolismo (§1.4): se il contratto verrà firmato, la bozza si
**promuove**, ed è l'unica cartella da cui la promozione è ammessa.

---

## Cosa il coordinatore deve fare, in ordine

1. **A1-A3** (le tre attribuzioni a Frigotecnica) prima di tutto: sono un errore solo, propagato in
   tre punti, e §9.5 passo 4 chiede di cercarlo anche nei lotti precedenti — nel lotto 1A la stessa
   forma di errore era stata trovata sui codici ricambio.
2. **B3** merita una nota-questione propria: è l'unica delle sei divergenze che nessuno ha visto.
   **B1 e B2** hanno bisogno solo di essere estratte dalle note che già le dichiarano e promosse a
   `type: conflitto`.
3. **C1**: emendare il canone in sezione datata con i numeri ricontati (68 · 174 · 186 su 186), e
   precisare nella stessa occasione la riga «Integrità del log cella» come da C2.
4. **Estendere `alias_entita.md`** con la riga di registro del lotto 1B e le classi A, B e C elencate
   nella verifica 1, punto 5.
5. Le lacune di copertura 1-4 della verifica 1 decidono se il lotto 1B si chiude o si allarga: la
   cella del Palù e la scheda CF-01 costano poche righe e chiudono due buchi che il lotto successivo
   erediterebbe.
