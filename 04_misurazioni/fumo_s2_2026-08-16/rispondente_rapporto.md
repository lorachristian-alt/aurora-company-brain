# Rapporto di chiusura del rispondente — mini-misura di fumo S2

**Sessione:** 2 — fetta pilota L26130
**Data di esecuzione:** 16/08/2026
**Ruolo:** rispondente (P1 adattato al vault), sessione fredda
**Modello:** **Opus 5** — id esatto `claude-opus-5`
**Deliverable:** `fumo_risposte.jsonl` — 30 righe, una per domanda
**Esito formale:** 30/30 id coperti, 0 duplicati, 0 righe preesistenti (file creato in questa sessione), schema `id` / `risposta` / `fonti` / `confidenza` validato riga per riga con parsing JSON

⚠️ **Numeri non ufficiali.** Non entrano nel README e non sono confrontabili con le misure delle Sessioni 6-7.

---

## 1. Perimetro, e come è stato rispettato

In lettura ho toccato **esclusivamente** il vault `aurora-cervello`: le undici cartelle di note, la copia dei grezzi in `sources\` e `llms.txt`. Esclusa `.obsidian\`. L'unico accesso fuori dal vault è stato in **scrittura**, sul file di salvataggio indicato dal prompt (e ora su questo rapporto, su richiesta esplicita del coordinatore).

**Non ho incontrato né aperto file di risposte, canoni o dataset di valutazione.** Il canone (`01_metodo\`) e il dataset (`03_valutazione\`) erano fisicamente fuori dal perimetro montato, come previsto dal principio 6 della scaletta: non è stata una clausola di prompt a tenerli fuori, è stato il filesystem. Nessuna astensione è stata causata dal perimetro.

Un solo file del vault porta un nome che poteva richiedere una valutazione — `sources\_QUESTO_ARCHIVIO_E_SIMULATO.txt` — e non è stato aperto: non serviva a nessuna delle 30 domande.

## 2. Metodo

### 2.1 Ordine di lettura

1. **Le domande per prime**, per sapere cosa cercare prima di leggere qualsiasi cosa.
2. **`llms.txt`**, che si è rivelato la porta d'ingresso più efficiente: dichiara le undici cartelle, gli hub dei temi e — soprattutto — l'elenco delle **nove questioni che l'archivio non chiude**. Sapere in anticipo dove stanno i conflitti noti ha orientato tutto il resto.
3. **Le note del vault**: indici, hub d'area, note atomiche `fatto-*`, note di conflitto `questione-*`, `docs\`, `data\`, `entities\`, `projects\`, `concepts\`, `workspace\`.
4. **I grezzi in `sources\`**, aperti solo dove serviva il dato primario.

### 2.2 Il principio operativo: la nota orienta, il grezzo decide

Le note del vault sono state usate come **mappa**, non come fonte del dato. Ogni numero finito in una risposta è stato riletto sul grezzo che lo attesta. Questo ha pagato due volte:

- ha permesso di **confermare** le note dove erano giuste (e lo erano quasi sempre, con locator corretti);
- ha permesso di **trovare cinque conflitti che le note non registrano** (§4), che sarebbero rimasti invisibili a chi si fosse fermato al livello delle note.

### 2.3 Niente conti a memoria

Tutti i conteggi e le aritmetiche sono stati eseguiti sui dati letti, con script, mai a stima:

| Conto | Come è stato fatto | Risultato |
|---|---|---|
| Letture T_CUORE in allarme | parsing riga per riga del `.log`, campo flag | 49 `ALARM` (+1 `WARN` sotto limite = 50 letture sotto 72,0) |
| Durata deviazione CCP2 | differenza fra primo e ultimo timestamp sotto limite | 14:20:07 → 14:44:37 = 24 min 30 s |
| Quadratura L26131 | somma degli addendi del foglio «A valle» | 4.260 + 980 + 2.380 + 0 = 7.620 = pz prodotti → quadra |
| Quadratura L26130 | idem | 5.100 + 1.440 + 1.180 + 220 = 7.940 vs 8.940 → mancano 1.000 |
| Costo NC critiche 2026 | filtro su gravità = `critica`, somma dei costi valorizzati | 13 NC, di cui 7 valorizzate → 42.430,00 € |
| Disponibilità turno 2 | (480 − 220) / 480, verificata anche su altre righe del foglio | 54,17% ≈ 54,2 dichiarato → torna |
| Qualità turno 2 | 5.250 / 5.580 | 94,09% ≈ 94,1 dichiarato → torna |
| OEE turno 2 | 0,542 × 0,715 × 0,941 | 0,3646 ≈ 36,5 dichiarato → torna |
| Misura del frammento sulla foto | scala letta sul righello (1 cm ≈ 240 px), poi misura del frammento | ~7-8 mm × ~5-5,5 mm |

### 2.4 Criterio di citazione

In `fonti` sono elencati **solo file effettivamente aperti e che contengono il dato**. Dove il dato viene dal grezzo, è citato il grezzo; le note del vault sono citate solo quando la risposta usa una loro elaborazione (due casi: `doc-ccp2-limite-critico.md`).

### 2.5 Criterio sui conflitti

Dove due fonti dicono cose diverse, la risposta **riporta entrambe con il loro locator** e dichiara, quando c'è, quale fonte ha più peso e perché — senza mai sceglierne una in silenzio. Dove l'archivio non permette di scegliere, la risposta lo dice.

### 2.6 Astensioni

**Nessuna astensione piena è stata necessaria**: tutte e 30 le domande hanno trovato risposta nell'archivio. In tre casi la risposta contiene un'astensione **parziale**, dichiarata:

- **Q137** — il totale dei costi delle NC critiche è strutturalmente incompleto (6 NC su 13 senza importo); ho dato la somma dei valorizzati dicendo che non è il costo delle NC critiche.
- **Q035** — le misure del frammento sono sei e non concordano: nessuna è stata eletta a risposta.
- **Q076 / Q238** — «la temperatura più bassa» non ha una risposta sola: ne ho date tre, distinte per significato (vedi §5).

## 3. Fonti aperte

**Grezzi (17):** `log_temperature_pastorizzatore_linea1_10_05_26.log` · `non_conformita_interne_registro_2026.csv` · `manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt` · `MOD-QA-31_reclamo_REC-2026-011.pdf` · `certificato_analisi_lotto_farina_MV26_0429A.pdf` · `report_fermo_macchina_confezionatrice_MAP.txt` · `R_ricambio_valvola_iniezione_azoto_PKM450_URGENTE.eml` · `calcolo_sfrido_efficienza_OEE_linea_bakery.csv` · `tracciabilita_lotti_massbalance_L26130.xlsx` · `Rapporto_di_Prova_AnalyticaVeneta_2026_04187.pdf` · `log_allarmi_cella_frigo_surgelati_aprile.log` · `checklist_metal_detector_manuale_operaio.txt` · `MOD-QA-07_10-05-26_L1_T2_scansione.jpg` (verifica visiva) · `IMG_20260514_152241_frammento_REC-2026-011.jpg` (verifica visiva) · `trascrizione_riunione_direzione_12_05_2026.txt` · `RE_RE_URGENTE_reclamo_corpo_estraneo_lotto_L26130.eml` · `appunti_capoturno_quaderno_linea1_OCR.txt`

**Note del vault:** tutte quelle di `areas\`, `data\`, `docs\`, `entities\`, `projects\`, più `concepts\concetto-fefo.md`, `workspace\bozza-lettera-tosano-reclamo.md`, gli `_index-*` e `llms.txt`.

**Non aperti** perché non necessari alle 30 domande: `I_Fwd_Richiesta_relazione_48_ore_Tosano.eml`, `IMG-20260510-WA0007.jpg`, `Verbale_ispezione_ATS_09_06_2026.pdf`, `inventario_magazzino_scadenze_FEFO_maggio.csv` e il resto di `sources\`. Nessuno di questi è citato in `fonti`.

## 4. Conflitti

### 4.1 Conflitti già registrati dal vault, riportati nelle risposte

Codice ricambio valvola (`PK45-VN2-08` vs `PKV-088-N2`/`PKV-088-KIT`) · materiale della guarnizione (gomma / silicone / polimero fluorurato) · misura del frammento, foto contro laboratorio · pezzi prodotti L26130 (8.940 contro 5.580) · quadratura del mass balance (mancano 1.000 pz). Su tutti l'archivio si comporta come le note dichiarano.

### 4.2 ⚠️ Conflitti NON registrati dalle note del vault

Sono il ritrovamento principale di questa sessione. Emergono solo leggendo i grezzi.

**(1) MOD-QA-07 del 10/05 turno 2 — tre versioni dello stesso turno.**
- *Scansione JPG* (verifica visiva diretta): 8 righe — 14:05 conforme, 15:00 «macchina ferma», **16:00 e 17:00 barrate e vuote**, poi 18:50, 19:55 (unica con 2ª firma, «MF»), 21:00, 22:00. Verifica di fine turno del capoturno **in bianco**. Nota a piè di modulo: «dalle 15 alle 18.45 linea ferma per rottura valvola azoto, verifiche non eseguite».
- *Trascrizione* in `checklist_metal_detector_manuale_operaio.txt`: orari diversi (14:10, 16:00, 17:00, 18:00, 19:05, 20:00, 21:00, 21:55) e verifiche **16:00-18:00 dichiarate eseguite e conformi**. La trascrittrice stessa annota il sospetto che quelle righe siano state scritte tutte insieme a fine serata.
- *Quaderno del capoturno*: terza versione ancora — «saltata verifica ore 15 e 16 x fermo!!! riprese ore 17 0k 18 0k 19 0k».

La nota `fatto-verifiche-ccp3-turno-l26130` descrive correttamente la sola scansione, ma **non registra che esistono altre due letture incompatibili dello stesso modulo**. Il vault non ha una `questione-*` su questo.

**(2) Conteggio pezzi del turno — esiste una terza fonte.**
Il vault tratta il conflitto come binario (8.940 mass balance contro 5.580 OEE). Il quaderno del capoturno annota per la stessa giornata: «0450: solo 4.100 pz oggi + quelo di T1». Terzo numero, mai citato in `questione-pezzi-prodotti-l26130`.

**(3) Scarti al riavvio — 348 contro 330.**
MOD-PR-04 §4: «confezioni scartate al riavvio (spurgo + taratura): **348 pz**». Foglio OEE, stessa riga di turno: `Scarto_prodotto_pz` = **330**. Perimetri diversi (riavvio vs intero turno) e valori diversi, e — se i perimetri fossero quelli — il numero di turno dovrebbe essere il maggiore, non il minore. Nessun documento riconcilia.

**(4) Ora di arrivo dell'officina — 15:25 contro 15:50.**
MOD-PR-04 §2: «15:25 - arrivo». Quaderno del capoturno: «chiamato ivano di nuovo … ariva ore 15.5O circa». Venticinque minuti di differenza sul primo intervento, su un fermo che è diventato oggetto di relazione a un cliente.

**(5) NC-2026-102 attribuisce un'origine che il laboratorio si rifiuta di attribuire.**
Il registro NC del 20/05 scrive: «Esito FTIR Analytica Veneta: frammento compatibile con elastomero guarnizione non originale, **incompatibile con film MAP e con MOCA di linea**», causa radice «**conferma origine interna**». Il rapporto di prova, §4.3 e §5, dice l'opposto in termini di competenza: «L'attribuzione a una specifica origine esula dalle competenze del laboratorio e dalle prove richieste», e i risultati «si riferiscono esclusivamente ai campioni analizzati». Il registro interno ha trasformato una compatibilità di materiale in una conferma di provenienza. La nota `fatto-esito-laboratorio-frammento` argomenta benissimo che «compatibilità non è provenienza», ma **non registra che un documento aziendale ha già fatto quel salto**.

### 4.3 Altri scarti minori annotati nelle risposte

- Ora di arrivo del reclamo: mail RSGQ del 12/05 ore 14:33 «è arrivato **alle 13:05** dal form»; in riunione si dice «ieri sera **alle 18 e 23**». È un terzo elemento oltre a quelli già in `questione-data-apertura-rec-2026-011`.
- Data del laboratorio sulla scheda reclamo: MOD-QA-31 §4 data l'invio al **18/05**; il rapporto dichiara accettazione **14/05 ore 16:40** ed emissione **22/05**.
- Blocco cautelativo: la scheda elenca **tre** lotti (L26130-L1-T2, L26130-L1-T3, L26131-L1-T2), la mail RSGQ ne elenca **due**.
- Il manuale HACCP (PRP-09) **dichiara la regola di composizione del lotto** — `L26<ggg>-<linea>-<turno>` — che la nota `lotto-l26130` afferma non essere scritta in nessun grezzo della fetta. La nota è da correggere.

## 5. ⚠️ Anomalia datalogger — la parte da leggere per intero

Il file `log_temperature_pastorizzatore_linea1_10_05_26.log` è la fonte più densa della fetta e contiene **cinque trappole distinte**. Tre sono note al vault, due no.

### 5.1 Il valore che non è una temperatura *(nota al vault)*

Alle **16:10:00** l'evento `SENSOR_FAULT` con dettaglio `T_CUORE OPEN_CIRCUIT`, flag `ALARM`. Da **16:10:07 a 16:55:07** la sonda scrive **91 letture consecutive a −999,9 con flag `FAULT`** — circa 45 minuti. Prima lettura valida successiva: 16:56:07, 58,9 °C.

Un `min()` ingenuo sulla colonna restituisce **−999,9** come «temperatura minima del turno». Non è una temperatura: è il codice di sonda in avaria. Il guasto cade **a linea ferma**, quindi non c'è prodotto in trattamento in quella finestra.

### 5.2 La sonda sbagliata nel footer *(non registrata dal vault)*

Il footer dell'export dichiara: «**Temperatura minima registrata TT_02: 68.6 C alle 14:30:37**».

`TT_02` è la sonda **di camera**, non quella al cuore. Chi legge il footer come riepilogo della grandezza governata dal CCP2 riporta 68,6 °C invece di 68,9 °C. Verificato riga per riga: alle 14:30:37 `TT_02` segna effettivamente 68,6 e `T_CUORE` segna 69,0; il minimo di `T_CUORE` è **68,9 °C**, prima occorrenza 14:21:07. `TT_02` ha una sua finestra di allarme (32 letture `ALARM`, 14:23:07-14:39:37) sfasata rispetto a quella del cuore.

### 5.3 Il footer che si contraddice con le proprie righe *(non registrata dal vault)*

Footer: «**Permanenza sotto soglia 72.0 °C: 27 min ca.** - verificare registro CCP2 (MOD-QA-12)».
Righe: **24 min 30 s** (14:20:07 → 14:44:37, 50 letture a 30 s), 25 min 30 s da ultima a prima lettura conforme, 24 min netti di flag `ALARM`.
NC-2026-088 e riunione di direzione: **29 min** («dalle 14:18 alle 14:47») — finestra che include quattro letture (14:18:07-14:19:37) che stanno fra 72,4 e 72,9 °C, cioè **sotto il set point ma sopra il limite critico**. È probabilmente da lì che nasce l'errore: si è preso l'inizio del flag `WARN` per l'inizio della violazione.

Quindi sulla stessa grandezza, nello stesso file, circolano tre durate: 24,5 · 27 · 29 minuti. Il conteggio sulle righe è l'unico verificabile.

### 5.4 La finestra che nessuno ha guardato *(non registrata da alcun documento dell'archivio)*

Dopo il riavvio delle **18:45:07** (`MACHINE_RUN`):
- il nastro riparte a **2,0 m/min dalle 18:46:37** e a **4,2 m/min dalle 18:52:07** (velocità di regime, la stessa del pomeriggio);
- `T_CUORE` risale lentamente e **supera 72,0 °C solo alle 19:08:07** (74,5 °C);
- nell'intervallo si contano **33 letture sotto il limite critico** (da 58,3 a 70,1 °C), **tutte con flag `OK`**.

Perché nessun allarme: alle 18:58:07 il tracciato registra `MODE=HEATING`, quindi la logica di macchina classifica quella fase come riscaldamento e non come produzione, e non applica la soglia.

**Nessun documento dell'archivio commenta questa finestra** — né la NC, né la riunione, né la scheda reclamo, né alcuna nota del vault. Non ho concluso che sia una seconda deviazione: l'ho riportata come osservazione sui dati, dichiarando che il tracciato la marca come riscaldamento. Ma se il prodotto stava transitando sul nastro in marcia, la domanda è aperta e l'archivio non la pone.

### 5.5 L'integrità del file, dichiarata fallita *(non registrata dal vault)*

Ultima riga del footer: «**Checksum: 8f3a…41bc – verifica integrità fallita**». In coda al file compaiono anche righe corrotte (caratteri spuri dentro i valori). Il file dichiara di non essere integro, e nessuna nota del vault lo rileva. Non intacca le letture usate — la finestra della deviazione è pulita e coerente — ma è un fatto che un auditor guarderebbe.

### 5.6 Distribuzione dei flag, per riferimento

| Flag su `T_CUORE` | Conteggio | Significato |
|---|---|---|
| `OK` | 394 | in specifica |
| `WARN` | 269 | sotto il set point 74,0-76,0 ma **sopra** il limite critico |
| `ALARM` | 49 | sotto 72,0 in modo persistente — tutte nella finestra 14:20:37-14:44:37 |
| `FAULT` | 91 | sonda in avaria, valore −999,9 |
| **Totale** | **803** | |

Le 269 letture `WARN` sono la trappola inversa: chi le conta come «anomalie» gonfia il problema di un fattore cinque.

Riepilogo del footer, per completezza: 12.390 campioni acquisiti, 12.293 validi; allarmi del periodo `ALM_LOW_TEMP(1) DEV_CCP2(1) MACHINE_STOP(1) SENSOR_FAULT(1) RTC_BATT_LOW(1)`; durata esercizio 13h 01m, durata fermo 3h 40m (coincide con il MOD-PR-04).

## 6. Confidenze dichiarate

| Livello | Numero | Note |
|---|---|---|
| alta | 29 | dato letto direttamente sul grezzo che lo attesta, o conto verificato |
| media | 1 | **Q035** — la misura del frammento: una delle sei letture è una mia misura sul riferimento metrico della foto, non un dato di fonte |
| bassa | 0 | |

Nessuna risposta è stata data per inferenza non dichiarata. Dove ho inferito (la misura sulla foto, il denominatore da 480 minuti della disponibilità, la finestra §5.4), l'inferenza è scritta dentro la risposta.

## 7. Note per il confronto con la baseline

- **Modello: Opus 5 (`claude-opus-5`).** Se la baseline A del 14/08 è stata prodotta con un modello diverso, il confronto ne risente e va dichiarato nel raffronto.
- **Un solo blocco**, 30 domande, nessuna suddivisione: non c'è l'effetto di degrado su giri successivi che il P1 della baseline (282 domande in dieci giri) poteva avere.
- **Sessione fredda reale**: nessuna conoscenza del canone, di come il vault è stato costruito, né di quali fossero le risposte attese. La struttura del vault è stata scoperta in sessione, a partire da `llms.txt`.
- `llms.txt` **ha accelerato molto** l'orientamento: l'elenco delle questioni aperte in testa ha funzionato da indice dei conflitti. È un dato utile a chi valuta l'architettura, non solo le risposte.
- Le note del vault sono risultate **accurate nei locator**: ogni volta che ho verificato un riferimento sul grezzo, l'ho trovato dove la nota diceva. I cinque conflitti di §4.2 non sono errori delle note, sono **assenze**: fatti presenti nei grezzi che nessuna nota ha ancora catturato.

## 8. Limiti di questo lavoro

- Le 30 domande coprono la sola fetta pilota L26130: **niente di quanto sopra dice qualcosa sul resto dell'archivio.**
- Non ho aperto tutti i grezzi: `sources\` contiene oltre 150 file e ne ho letti 17. Conflitti ulteriori possono benissimo stare nei restanti.
- La misura del frammento sulla foto (§2.3) è affidabile all'ordine del millimetro, non oltre: il righello è su un piano più basso del frammento e l'inquadratura potrebbe non essere ortogonale — le stesse riserve che la nota `questione-misura-frammento-strumentale` già solleva.
- Il rapporto non esprime alcun giudizio sulla qualità delle risposte: quello spetta alla valutazione, che è fuori dal perimetro del rispondente e che non ho visto.
