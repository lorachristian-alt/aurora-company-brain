# Rapporto del giudice — Misura C (RAG produzione, LLM locale 3B)

**Corpus v1 · Aurora Food Group S.r.l. (simulazione dichiarata)**
Giudizio eseguito il **18/08/2026** su `misuraC_risposte.jsonl` (run del 17/08/2026).
Esito riga per riga in `valutazione_c.jsonl` — 282 righe, 282 id distinti, ordine identico a `eval_set.jsonl`.

## Condizioni della valutazione

| | |
|---|---|
| Modello giudice | `claude-opus-5`, fast mode OFF — lo stesso della valutazione A/B del 14/08/2026 |
| Sessione | terminale nuovo, separato da quello che ha costruito la pipeline e prodotto le risposte |
| Perimetro aperto | `04_misurazioni\` + `03_valutazione\` (P3 della baseline) |
| Perimetro **non** aperto | `02_corpus\`, vault `aurora-cervello`, canone, e `baseline_c_2026-08-17_grezzo\tracce\` |
| Lavorazione | 10 blocchi in append: 9 da 30 voci + 1 da 12 |

Il giudizio è **sempre sul contenuto della risposta contro il criterio di `note_valutazione`**, mai sulla prosa: una risposta scritta male che contiene il dato richiesto è `corretta`, una scritta bene che non lo contiene non lo è.

---

## 1. Risultato complessivo

| Esito | n | % |
|---|---:|---:|
| `corretta` | 41 | 14,5% |
| `parziale` | 75 | 26,6% |
| `sbagliata` | 141 | 50,0% |
| `allucinata` | 25 | 8,9% |
| **Totale** | **282** | **100%** |

`fonti_corrette`: **198 true / 84 false** (70,2% corrette).

### Il numero che conta davvero

**Escludendo le 31 domande `non_rispondibile`, le corrette sono 19 su 251 — il 7,6%.**

Le altre 22 corrette vengono tutte da domande la cui risposta giusta è «il dato non è in archivio», e il modello ci arriva **perché si astiene sempre**, non perché sappia distinguere ciò che c'è da ciò che manca. È lo stesso comportamento che altrove produce decine di astensioni false.

> Le due percentuali — **14,5% complessivo** e **7,6% sulle domande rispondibili** — vanno riportate separate. Il solo dato complessivo racconta una capacità che il sistema non ha.

| Sottoinsieme | n | corrette | parziali | sbagliate | allucinate |
|---|---:|---:|---:|---:|---:|
| Domande rispondibili | 251 | 19 (7,6%) | 72 | 137 | 23 |
| `non_rispondibile` | 31 | 22 (71,0%) | 3 | 4 | 2 |

---

## 2. Per tipo di domanda

| Tipo | n | corrette | % corrette | parziali | sbagliate | allucinate |
|---|---:|---:|---:|---:|---:|---:|
| `non_rispondibile` | 31 | 22 | **71,0%** | 3 | 4 | 2 |
| `lookup` | 86 | 15 | 17,4% | 30 | 31 | 10 |
| `calcolo` | 24 | 2 | 8,3% | 7 | 13 | 2 |
| `multi_hop` | 74 | 2 | 2,7% | 19 | 48 | 5 |
| `aggregazione` | 28 | 0 | **0%** | 1 | 25 | 2 |
| `temporale` | 18 | 0 | **0%** | 4 | 11 | 3 |
| `contraddizione` | 14 | 0 | **0%** | 11 | 3 | 0 |
| `metadato` | 7 | 0 | **0%** | 0 | 6 | 1 |

**Quattro tipi su otto chiudono a zero.**

## 3. Per difficoltà

| Difficoltà | n | corrette | % corrette | parziali | sbagliate | allucinate |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 32 | 9 | 28,1% | 12 | 7 | 4 |
| 2 | 63 | 9 | 14,3% | 18 | 30 | 6 |
| 3 | 92 | 10 | 10,9% | 18 | 57 | 7 |
| 4 | 62 | 11 | 17,7% | 13 | 35 | 3 |
| 5 | 33 | 2 | 6,1% | 14 | 12 | 5 |

**Il tipo di domanda pesa molto più della difficoltà dichiarata.** Fra difficoltà 1 e 4 le corrette oscillano senza andamento monotòno (il rialzo a difficoltà 4 è dovuto alle `non_rispondibile`, quasi tutte lì), mentre fra `lookup` e `aggregazione` c'è un muro netto.

## 4. Per blocco di lavorazione

| Blocco | id | corrette | parziali | sbagliate | allucinate | fonti false |
|---|---|---:|---:|---:|---:|---:|
| 1 | Q001–Q030 | 8 | 12 | 6 | 4 | 3 |
| 2 | Q031–Q060 | 6 | 7 | 14 | 3 | 10 |
| 3 | Q061–Q090 | 1 | 11 | 15 | 3 | 10 |
| 4 | Q091–Q120 | 1 | 2 | 24 | 3 | 13 |
| 5 | Q121–Q150 | 1 | 8 | 19 | 2 | 10 |
| 6 | Q151–Q180 | 2 | 6 | 19 | 3 | 7 |
| 7 | Q181–Q210 | 0 | 7 | 20 | 3 | 14 |
| 8 | Q211–Q240 | 0 | 17 | 12 | 1 | 6 |
| 9 | Q241–Q270 | 19 | 4 | 6 | 1 | 5 |
| 10 | Q271–Q282 | 3 | 1 | 6 | 2 | 6 |
| | **Totale** | **41** | **75** | **141** | **25** | **84** |

---

# Diagnosi

## Punto 1 — Il collo di bottiglia è il generatore, non il retrieval

Il documento atteso era citato nel **70% delle risposte**, e in decine di casi **la risposta nega un dato che sta nel file che la risposta stessa sta citando**. Non è un problema di recupero: è che un LLM da 3B non estrae dal passaggio che ha in mano, non conta righe, non somma, non incrocia.

Casi rappresentativi:

- **Q089** — dichiara non determinabile un conteggio che il registro scrive in chiaro in fondo al file (`TOTALE SCADUTI: 17`).
- **Q170** — alla domanda se qualcuno guidi il muletto senza abilitazione risponde che non è determinabile, citando il registro che riporta testualmente *«NON ABILITATO ALLA GUIDA fino a rinnovo»* accanto a Preda Radu.
- **Q209** — rifiuta di rispondere **perché il dato nel documento è espresso come «circa»**: ha trovato il passaggio, l'ha letto, e l'ha scartato per approssimazione.
- **Q012** — scrive «non è possibile determinare la pratica» e mette *«Pratica n. 28714»* dentro il campo `fonti` della stessa riga.
- **Q106**, **Q112**, **Q115**, **Q087**, **Q097** — stesso schema: astensione con la fonte giusta citata.

Nelle domande di `aggregazione` questo è totale: **28 domande, zero corrette, 25 astensioni o conteggi errati**. Le quattro volte in cui ha provato a contare ha sbagliato di molto (Q099: 1 invece di 3; Q104: 1 invece di 5; Q109: 19 invece di 8; Q113: 4 invece di ~49, avendo contato gli *eventi* invece dei *campioni*).

**Conseguenza operativa: sostituire il generatore lasciando invariata la pipeline è l'unico intervento che può spostare questi numeri.** Il retrieval, su questa misura, non è il fattore limitante.

### Un difetto di retrieval però esiste, ed è isolabile

Quando il corpus contiene un **documento-padrone e un suo derivato** (mail di inoltro, copia di cortesia, contratto che cita il listino), il recupero pesca il derivato:

- **Q033** — condizioni Molino corrette ma attribuite alla mail di aumento invece che al listino.
- **Q052** — cita l'inoltro `.eml` e restituisce il claim commerciale «-22% rispetto al TS-01» al posto dei 0,072 kWh/kg del preventivo.
- **Q049** — fattura di cortesia invece degli XML SDI, e infatti perde il codice destinatario in entrata.
- **Q020**, **Q048**, **Q066**, **Q070** — stesso pattern.

## Punto 2 — Le 75 `parziale` sono il rischio maggiore, non le 25 allucinazioni

La forma dominante non è l'invenzione: è **il sì o il no giusto, nudo**.

> «Sì, in parte a rifiuto» (Q183) · «Sì, era già stato contestato» (Q210) · «No, non aveva la formazione HACCP» (Q191) · «Sì, c'è un problema con il lievito» (Q224) · «La lista buyer contiene duplicati» (Q095)

Sono risposte **vere e inutilizzabili**: nessuna data, nessun codice, nessun importo, nessun FIR, nessuna NC. Chi legge non ha modo di distinguerle da un'ipotesi, e non ha nulla da verificare. In un uso reale questa è la modalità di fallimento più insidiosa della misura C, perché **si comporta come una risposta**.

### Sulle `contraddizione` il difetto diventa sistematico

**14 domande, 11 `parziale`, zero corrette.** Il modello dà quasi sempre il valore giusto e **non si accorge mai che nell'archivio ne esiste un altro**:

- **Q235** — risponde «2» alle NC dell'audit, che è quanto dichiara l'intestazione; la sezione di chiusura dello stesso file parla di NC 1-7.
- **Q240 / Q234** — cita un solo numero d'offerta Criotech su tre in circolazione.
- **Q236** — dà il protocollo giusto della PEC e ignora che il verbale ispettivo ne richiama un altro.
- **Q238** — dà 68,6 senza distinguere la sonda di camera da quella al cuore, che è l'unica rilevante per il CCP2.
- **Q241** — riporta le dimensioni del tunnel dall'offerta senza vedere che con quell'altezza l'impianto non passa sotto la trave: un rischio di progetto da 290.000 €.

**Un sistema documentale che risponde così è più pericoloso di uno che si astiene**: consegna un numero verificabile e nasconde che il dato è contestato.

## Punto 3 — Le allucinazioni sono poche ma concentrate dove fanno danno

25 su 282 (8,9%). Non è il difetto quantitativamente dominante, ma la distribuzione è sfavorevole: cadono su sicurezza alimentare, igiene, adempimenti e denaro.

| id | Allucinazione | Perché pesa |
|---|---|---|
| Q078 | Dà per riuscito un lavaggio CIP finito in `ESITO=ABORT` per conducibilità bassa in fase soda | Evento di sicurezza alimentare dichiarato conforme |
| Q190 | «La situazione igienica non è rientrata» dopo il ricambio originale | I tamponi del 25/05 danno 24 e 2 UFC/cm², conformi |
| Q094 | Nega cinque rotture di stock registrate | Tocca l'OTIF e quindi le penali contrattuali |
| Q144 | «Nessun corso è scaduto da più di un mese» | Un preposto è scaduto dal 15/09/2025, un'addetta primo soccorso dall'08/02/2026 |
| Q272 | Attribuisce al laboratorio una conferma sull'origine del frammento | Il rapporto dichiara che l'attribuzione *esula dalle sue competenze* |
| Q116 | «290.000,00 + 304.500,00 = 594.500,00» | IVA al 105%; le due milestone successive sono invece copiate esatte |
| Q281 | «Non esistono documenti in doppia copia» | L'archivio ne contiene quattro coppie |
| Q193 / Q265 | Fattura Pakmatic da **4.912 €** | **Numero inventato che ricompare identico in due punti del giro** |

### Due errori di sostanza non allucinati, ma altrettanto gravi

- **Q203** — alla domanda se l'investimento stia dentro a quanto approvato dal CdA risponde «è stato approvato dal Consiglio di Amministrazione», lasciando intendere di sì. Il tetto deliberato è 319.000 €, il quadro economico 413.316: **serve una nuova delibera, e la risposta la nasconde.**
- **Q248 / Q251** — costruzione sintattica difettosa: *«Non è ricavabile dai documenti forniti se non che Aurora ha la certificazione ISO 14001»* e *«…se non che Aurora ha comprato il terreno a Minerbe»*. Letta alla lettera, la frase **afferma** ciò che il modello voleva negare, su una certificazione e su un fatto patrimoniale.

### Dove il sistema tiene

Va registrato in positivo: sulle `non_rispondibile` **resiste alle esche**, che erano costruite bene. Non spaccia il consuntivo gestionale per bilancio 2026 (Q245), non deduce il vincitore ERP dal confronto fra le due offerte (Q253), non attribuisce a nessuno il ruolo di referente privacy lasciato «da nominare» (Q254), non fornisce una ragione sociale per il concorrente pugliese di cui esiste solo un'iniziale (Q264), non scambia il codice operatore `IT BIO 006` per il certificato ICEA dell'azienda (Q267). Su una configurazione RAG queste sono le allucinazioni tipiche, e non ci sono cadute.

---

# Guasti di formato

Registrati per l'audit, **non hanno pesato sul giudizio**, che è sempre sul contenuto.

### Le tre anomalie preannunciate — confermate tutte

- **Una risposta vuota**: Q204 (costo complessivo del reclamo).
- **Dodici risposte senza fonti**: campo `fonti` vuoto, in diversi casi con i nomi dei file riversati nel corpo della risposta (Q046, Q084, Q100, Q110, Q134, Q140, Q142, Q197, Q204, Q208, Q217, Q244).
- **Scala `confidenza` a due soli valori** (`alta` / `bassa`, mai `media`): il generatore da 3B non usa la scala, e il campo non ha pesato sul giudizio.

### Tre difetti non preannunciati

- **Segnaposto letterale restituito come risposta**: Q205 (`<la risposta></la risposta>`) e Q282 (`<la risposta>CONFIDEZZA: bassa</la risposta>`, con il campo storpiato).
- **Degenerazione in loop**: Q208 ripete 23 volte la stessa frase fino al troncamento; Q268 la ripete 5 volte; Q278 sei volte; Q148 e Q156 ripetono ciclicamente gli stessi elementi di una lista.
- **Campo `fonti` che esplode in frammenti**: Q183 contiene 18 voci che sono pezzi di una riga CSV di una NC estranea (`"T salita a -15"`, `"prodotto ok da datalogger"`, `"320"`, `"00"`). Casi minori in Q003 (`"file [1"`, `"3"`, `"4"`), Q184 (`"1"`, `"2"`, `"3"`, `"4"`), Q092 e Q162 e Q163 (nomi di **persone** citati come fonti), Q263.
- **Nomi di file inesistenti o storpiati fra le fonti**: Q193 (`Fattura_Elettronica_SDI_Inbound_Q2.txt`, singolare), Q156 (`log_lavaggio_CIP_line`, troncato), Q205 e Q282 (`IT04123980288_p88M2.xml`, `IT03412550281_88wQ1.xml`).
- **Documenti-esca pescati dal retrieval**: Q096 cita `Newsletter_Fiere_alimentari_2026_NON_LEGGERE.eml`; Q253 cita `confronto_ERP_v3_DEFINITIVO_ok2.txt`.

---

# Regola di compilazione di `fonti_corrette`

Dichiarata qui perché il campo sia interpretabile e ricalcolabile, e applicata identica su tutti e dieci i blocchi.

**`true` se e solo se:**
1. fra le fonti citate compare **almeno una delle fonti attese** dall'`eval_set`, **e**
2. nessuna citazione punta a un **documento inesistente** (nome inventato, storpiato o troncato).

**Non degradano il campo:**
- le fonti reali ma non pertinenti aggiunte in coda — rumore frequentissimo in C, presente in quasi tutte le risposte;
- i frammenti che non sono nomi di file ma **intestazioni di sezione, numeri di pagina o righe del documento giusto** (`"CONTO ECONOMICO"`, `"pag. 2"`, `"Art. 5.1"`): sono rumore di formattazione, non citazioni false.

**Separazione dei due campi.** `esito` misura il contenuto, `fonti_corrette` misura la citazione. Sono tenuti distinti apposta, per non contare due volte lo stesso difetto: esistono risposte `corretta` con `fonti_corrette: false` (Q020, Q033, Q121) e risposte `allucinata` con `fonti_corrette: true` (Q016, Q045, Q101).

### ⚠️ Eccezione sulle `non_rispondibile`

Per le 31 domande di tipo `non_rispondibile` **le fonti attese sono vuote**, quindi la regola sopra non si applica e **il campo non è confrontabile con quello degli altri blocchi**. Lì `fonti_corrette` è `false` solo dove una citazione viene usata per **sostenere un'affermazione errata** (Q248 con l'AUA, Q265 col report costi fissi, Q272 con la bozza di lettera). Il 25/30 del blocco 9 va letto con questa avvertenza.

---

# Nota di metodo sui casi limite

Per trasparenza, i criteri con cui ho sciolto le ambiguità ricorrenti:

- **Astensione falsa** («non è possibile determinare» su un dato presente) → `sbagliata`: non è un dato inventato, è una conclusione errata tratta da documenti reali.
- **Negazione assertiva falsa** («nessuno ha…», «non è mai stato…») contraddetta dalla fonte citata → `allucinata`: afferma il falso, non si limita a tacere.
- **Risposta binaria giusta ma priva di qualunque elemento richiesto dal criterio** → `parziale`.
- **Errore accessorio non richiesto dal criterio** → non declassa (Q072); **errore che sposta l'oggetto della domanda** → declassa (Q071).
- **Il criterio di `note_valutazione` è l'ancora**: dove la domanda chiedeva più di quanto il criterio richiedesse, ho seguito il criterio, per non introdurre un metro mio e mantenere la comparabilità con le misure A e B.
