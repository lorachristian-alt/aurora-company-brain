# Revisione indipendente del lotto 1A — Linea 1: il turno, i CCP e la confezionatrice

> **Chi** · Revisore indipendente, sessione diversa da quella che ha scritto le note
> (metodo_03 §9.5 passo 3, divieto 35). Canone e tabella alias letti prima delle note.
> **Perimetro** · I sette grezzi di `06_operativo\qa\lotti\lotto_01a_linea1_turno_ccp.txt`,
> le 57 note del perimetro di lotto, più gli `_index` e gli hub d'area aggiornati.
> **Cosa NON è stato fatto** · Nessun file è stato modificato. `03_valutazione\` non è
> stata aperta. Nessuna riga del canone è stata copiata nel vault né suggerita per esso.

---

## Conteggio

| Categoria | Quante |
|---|---|
| **A — errori veri** (bloccano la chiusura del lotto) | **10** |
| **B — contraddizioni non registrate** (da aprire e da aggiungere al canone in sezione datata) | **10** |
| **C — falsi allarmi** (trappole volute, non si tocca niente) | **11** |
| **Sovra-atomizzazione** | **0** su 18 note campionate |

**Verdetto:** il lotto **non è chiudibile** finché A1 e A4 non sono sanate. A1 è una fuga di
canone — il difetto più grave possibile in questo progetto — e A4 è un fatto del filo rosso
senza nota padrona.

Il lotto è, nel merito, di buona qualità: la riconciliazione incrociata dei numeri è stata
fatta quasi ovunque, i conteggi derivati sono dichiarati col criterio e rieseguibili (li ho
ricontati tutti, tornano al numero), le contraddizioni volute non sono state «corrette», e
le nove questioni aperte nuove sono ben costruite. I rilievi qui sotto sono in gran parte
di igiene, con due eccezioni pesanti.

---

## A — Errori veri

### A1 · Fuga di canone in `docs\doc-scheda-tecnica-af-sn-0450.md`

**La nota dice** (riga 40):

> «⚠️ Il **pezzi per cartone** dichiarato qui è **10**. Il canone del progetto registra che
> listino e accordo quadro ne dichiarano 12: la seconda gamba di quel confronto non è in
> questo lotto e la divergenza si scioglierà quando entrerà, non prima.»

**Cosa dicono le fonti.** L'unica fonte della nota è
`Scheda_tecnica_prodotto_AF-SN-0450_rev4.pdf`, che a pag. 3 dichiara «Cartone ondulato a
vassoio con coperchio, **10 pezzi per cartone**» e **nient'altro**. Il valore **12**, il
listino e l'accordo quadro non compaiono in nessuna fonte citata, e — verificato con un
grep su tutto il vault — **nessuna nota del vault cita il listino o l'accordo quadro**: quei
grezzi non sono ancora canonizzati. Il «12» è entrato nel vault **dalla porta sbagliata**,
e la nota lo dichiara apertamente nominando il canone.

**Cosa viola.** metodo_03 §5.5 guardrail 1 («non compare mai in `fonti`; non si copia nel
vault, né intero né a pezzi, né citato fra virgolette»), guardrail 2 (riscontro testuale
nelle fonti citate), divieti §10.6, §10.7 e §10.9.

**Cosa andrebbe fatto.** Cancellare l'intero capoverso. Il dato «10» resta, attribuito alla
scheda tecnica. La divergenza nasce quando entra il listino, nel lotto commerciale, e nasce
lì come questione aperta con entrambe le gambe citate.

**Propagazione, da controllare nello stesso turno.** La stessa conoscenza compare in forma
attenuata in `entities\prodotto-af-sn-0450.md`: «la scheda tecnica dice **10**, e altre
fonti dell'archivio **non ancora canonizzate ne dichiarano un numero diverso**». Non nomina
il canone e non scrive il 12, ma afferma comunque l'esistenza e il segno di una divergenza
che nessuna delle sue quattro fonti attesta. Va tolta anche quella: la cautela corretta è
non dire nulla finché la seconda gamba non è in archivio-vault.

---

### A2 · Fatti scritti senza che le fonti citate li contengano (CCP4 e Linea 3)

**Le note dicono.**

- `entities\macchina-linea-1.md`: «Tre dei quattro punti critici di controllo del piano
  HACCP stanno su questa linea… **Il quarto, la surgelazione, sta sulla Linea 3.**»
- `areas\fatto-convalida-md-1800-scaduta.md`, sezione «Da non confondere con»: «**La Linea 3
  è quella dei prodotti surgelati.**»

**Cosa dicono le fonti citate.** `macchina-linea-1` cita scheda tecnica, quaderno e piano di
produzione: la scheda tecnica dichiara CCP1, CCP2 e CCP3 e **non nomina né il CCP4 né la
Linea 3**. `fatto-convalida-md-1800-scaduta` cita la sola scheda di manutenzione, che scrive
«MD-1800 · Convalida annuale **linea 3**» senza mai dire che la Linea 3 sia la linea dei
surgelati.

**Dove il fatto esiste davvero.** In `manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt`, che
porta «**CCP4 - SURGELAZIONE (LINEA 3)**» e la riga «fase 11 → CCP4». Quel file **non è fra
le `fonti` di nessuna delle due note**. Non è quindi materiale inventato: è materiale vero
citato senza la sua fonte, che per la QA di provenance è indistinguibile da un fatto senza
fonte (divieto §10.6, guardrail 2).

**Variante minore, stesso difetto.** `concepts\concetto-ccp.md` mette in tabella «CCP2 …
Dove si registra: **MOD-QA-12**». Le due fonti citate sono la scheda tecnica e la
trascrizione del MOD-QA-07; la scheda tecnica nomina `MOD-QA-12` **solo** per l'ossigeno
residuo («analizzatore gas — 1 conf./30 min (MOD-QA-12 sez. gas)»), non per il CCP2. Il
legame CCP2 ↔ MOD-QA-12 è attestato altrove (manuale HACCP; e la stessa scheda di
manutenzione, riga 21, scrive «rif. CCP2 - MOD-QA-12»), ma non nelle fonti citate.

**Cosa andrebbe fatto.** Aggiungere `manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt` alle
`fonti` delle tre note con il locator puntuale (§8.1, scheda CCP4), oppure togliere le
affermazioni. La prima opzione è preferibile: i fatti sono veri e utili.

---

### A3 · Riconciliazione obbligatoria mancata: il riepilogo interno della scheda di manutenzione

**Cosa dice la fonte.** `scheda_manutenzione_ordinaria_forni_industrial.csv`, riga 59,
contiene una riga di riepilogo scritta dall'azienda:

> `--- RIEPILOGO PARZIALE: interventi SCADUTI n. 7 / RIMANDATI n. 8 (agg. 09/05/26 L.T.) ---`

**Cosa dicono le righe.** Ricontato: **11 righe `SCADUTO`** e **7 righe `RIMANDATO`**, che
al netto delle tre righe duplicate alla lettera fanno **16 voci arretrate distinte**. Anche
restringendo il conto alle sole righe che precedono il riepilogo (lettura più benevola, dato
il «PARZIALE») si ottiene **6 scaduti e 7 rimandati**: nessuno dei due tagli restituisce 7/8.
Il riepilogo del file **non quadra con il file stesso**, in nessuna lettura.

**Cosa dice la nota.** `data\kpi-manutenzioni-arretrate-2026.md` conta le righe una per una,
dichiara il criterio, elenca le sedici voci — ed **è corretta rispetto alle righe**. Ma **non
nomina mai il riepilogo interno** e non ne dichiara l'esito del confronto. Verificato con
grep su tutto il vault: nessuna nota lo menziona.

**Cosa viola.** metodo_03 §5.1-bis (E2): «Quando due grezzi dello stesso lotto riportano la
stessa grandezza, i due valori si confrontano, e **l'esito del confronto si scrive**» — e a
maggior ragione quando i due valori stanno nello stesso file, dove nessuno li guarda insieme.
È esattamente il modo di fallire che §5.1-bis descrive: la nota è corretta rispetto alla
propria fonte, e manca il confronto.

**Aggravante.** Il vault contiene già l'analogo fatto bene:
`areas\fatto-riepilogo-datalogger-inaffidabile.md` esiste proprio perché il piè di pagina di
un tracciato non quadra col tracciato. Il modello c'era ed è stato applicato altrove.

**Cosa andrebbe fatto.** Trattandosi di un'incoerenza **interna a un solo file**, metodo_03
§2.4 è esplicito: non è una nota `conflitto`, è un'`atomica` che la dichiara. O una nota
propria, o un paragrafo di `kpi-manutenzioni-arretrate-2026` con i due numeri, il criterio di
entrambi i tagli e la constatazione che il riepilogo non quadra. Va poi registrata anche nel
canone (vedi B11 nella sezione B: la divergenza è reale e non elencata).

---

### A4 · Manca la nota padrona della decisione dell'08/05 di proseguire con la valvola che perdeva

**Cosa dichiara il canone.** Filo rosso, punto 3: «**08/05** — Dal Maso segnala che la
valvola di iniezione azoto della PKM-450 perde. Il ricambio originale Pakmatic arriva solo
il 15/05. **Si va avanti lo stesso.**» È uno dei fatti che reggono l'intera vicenda: senza
di esso il guasto del 10/05 è un imprevisto, con esso è un rischio noto e accettato.

**Cosa c'è nel vault.** Nessuna nota ha questo fatto per soggetto. Verificato: elenco
completo delle 103 note, più grep su `fantin`, `andiamo avanti`, `monitorare`, `08/05`. Il
fatto vive **solo come un capoverso dentro `areas\fatto-fermo-pkm-450-l26130.md`**, la cui
padronanza è un altro fatto (il fermo del 10/05). Il nome «Fantin» compare in tutto il vault
una volta sola, e in un locator che riguarda tutt'altro.

**Cosa dicono le fonti.** Il fatto è largamente attestato, su tre documenti di due lotti:

- `report_fermo_macchina_confezionatrice_MAP.txt`, §1 «ANTEFATTO - venerdi 08/05»: sibilo
  rilevato alle 10:30, consumo azoto **+15 %** al flussimetro, consumo bombole Nordgas su del
  15-20 % «già da fine aprile», rapportino di segnalazione **n. 2026/081**, chiamata Pakmatic
  alle 11:15 con consegna confermata al 15/05 e preventivo 1.240,00 €, e poi la riga che
  conta: «Riunione veloce con **Zanella e Fantin** (08/05 ore 14): decisione di **ANDARE
  AVANTI** fino all'arrivo del ricambio, vista la promo Tosano sett. 19-21 e la domenica già
  programmata. Monitoraggio a vista ogni turno. **Verbale non fatto, decisione a voce.**»
- `non_conformita_interne_registro_2026.csv`, riga 90: «si decide di proseguire la produzione
  con monitoraggio».
- **Il quaderno del capoturno — grezzo di questo lotto — è l'unica fonte che documenta
  l'escalation su tre giorni**, e nessuna nota la porta:
  - pag. 41, mer 6/5: «PKM 45O az0to consumo strano?? bomb0la n0rdgas cambiata alle 16 ma
    durata p0co · ch1esto a ivano di guardare dom»;
  - pag. 42, gio 7/5: «ivano vist0 PKM: dice valv0la azoto perde p0co "tenemo d ochio"»;
  - pag. 43, ven 8/5: «IVANO C0NFERMA valvola azoto PKM perde · fato vedere anche a fantin ·
    ric. originale pakmatic ordinato ariva ven 15/5 · **fantin dice andiamo avanti cosi
    monitorare** · io segno qua x sicureza».

**Perché è categoria A e non un'osservazione.** Il test di §5.1 è netto: una risposta
corretta a «chi ha deciso di andare avanti con la valvola che perdeva, quando, e con quale
motivazione?» userebbe questo fatto **al posto** del fermo del 10/05, non insieme a esso.
Sono due fatti, e il secondo non è padrone del primo. Il mandato del revisore lo dice
esplicito: un fatto chiave senza padrona blocca la chiusura.

**Cosa andrebbe fatto.** Una nota `atomica` in `areas\`, `area: manutenzione` (o `direzione`,
se si privilegia chi ha deciso), `data_fatto: 2026-05-08`, con le tre fonti sopra e i loro
locator, che tenga: il segnale montante su tre giorni, la data di consegna del ricambio, chi
ha deciso, con quale motivazione dichiarata e **che il verbale non è stato fatto**. Va
linkata da `fatto-fermo-pkm-450-l26130`, da `macchina-pkm-450`, da `area-manutenzione` e da
`fatto-guarnizione-pkm-450-manutenzione-scaduta`. ⚠️ Non deve affermare nessun nesso causale
col guasto: le fonti la sequenza la danno, il nesso no.

**Nota di equità.** La gamba principale (il MOD-PR-04) apparteneva al lotto pilota; la gamba
del quaderno è di questo lotto. Il buco viene da prima, ma questo è il lotto in cui il
quaderno entra, ed è qui che va chiuso.

---

### A5 · Locator sbagliati — quattro occorrenze in quattro note

Il locator è verificabile e va verificato; questi quattro non reggono il riscontro.

| Nota | Locator scritto | Cosa c'è davvero |
|---|---|---|
| `areas\questione-codice-allarme-pkm-450.md` | «pag. **3**, §"8. RICERCA GUASTI"» | Il §8 del manuale PKM-450 è a **pag. 5**. La pag. 3 porta il §4 e il §5 |
| `entities\entita-pakmatic.md` | «pag. **3**, §"8. RICERCA GUASTI" (recapiti dell'assistenza)» | Idem: **pag. 5** |
| `data\kpi-shelf-life-af-sn-0450.md` | «riga **17**, "al limite sensoriale, nota di lieve cartone"» | È la **riga 18** (P02, 25 °C, giorno 90) |
| `data\kpi-shelf-life-af-sn-0450.md` e `concepts\concetto-shelf-life.md` | «riga **26**, "prova accelerata"» | È la **riga 27** (P04, 38 °C, giorno 0) |

Il contenuto citato esiste in tutti e quattro i casi: è il puntamento a essere sbagliato.
Tutti gli altri locator del lotto che ho ricontrollato — righe 3, 55, 56, 57, 68, 71, 73,
132, 148, 156, 173 e 174 del CSV shelf life; righe 2, 4, 16, 20, 21, 22, 26, 34, 35, 37, 39,
73, 89, 90, 111, 112 del CSV manutenzione; le celle e i fogli dell'`.xlsx` del piano; le
pagg. 1, 2, 4, 5 e 6 del manuale PKM-450; le pagg. 1, 2, 3, 4 della scheda tecnica — sono
**corretti**. È un errore isolato, non un metodo sbagliato.

**Cosa andrebbe fatto.** Correggere i quattro numeri. L'errore sulla pag. 3 è propagato su
due note e va cercato ovunque si citi quel manuale.

---

### A6 · Annotazioni di hub e `_index` stantie, che contraddicono la nota linkata

metodo_03 §7.1 clausola 4 e il riquadro di §3.3 sono espliciti: «Se un'annotazione dice
qualcosa che la nota linkata non dice, **l'errore è dell'`_index`**». Il lotto ha esteso tre
questioni aggiungendo gambe nuove e **non ha aggiornato le annotazioni che le presentano**.

| Dove | Cosa dice l'annotazione | Cosa dice la nota linkata |
|---|---|---|
| `areas\_index-areas.md` r.40 | allarme PKM-450: «non è lo stesso **sui due documenti**» | **Tre** codifiche: `E-214 GAS`, `AL-217`, `A031` |
| `areas\_index-areas.md` r.41 | «**due codici** per lo stesso kit valvola» | **Quattro** codici |
| `areas\_index-areas.md` r.42 | «tre attribuzioni per **la stessa** guarnizione» | **Sei** attribuzioni su **due pezzi diversi** |
| `entities\_index-entities.md` r.54 | allarme: solo `AL-217` e `E-214 GAS` | tre codifiche |
| `entities\_index-entities.md` r.58 | «due codici» | quattro |
| `areas\area-manutenzione.md`, «Questioni aperte» | allarme «diverso sui due documenti»; ricambio «due codici» | tre; quattro |
| `entities\macchina-pkm-450.md`, corpo | «Il codice del ricambio **non è lo stesso nei due documenti** che lo nominano» | quattro documenti |
| `entities\macchina-pkm-450.md`, «Questioni aperte» | «due codici»; «tre attribuzioni per la guarnizione montata il 10/05» | quattro; sei su due pezzi |

Bene invece `_index-entities` r.59, che è già aggiornata («tre materiali per la provvisoria e
tre per l'originale»), e `area-manutenzione` sulla stessa riga: la correzione è stata fatta a
macchia di leopardo, ed è la firma di una propagazione incompleta (§9.5 passo 4).

**Di contorno:** `entities\macchina-pkm-450.md` e `entities\macchina-pt-104.md` portano
`data_nota: 2026-08-16` pur essendo state modificate in questo lotto. Se `data_nota` è
«quando la nota è stata scritta», una nota riscritta ha una data nuova; se non lo è, va
deciso una volta e scritto nel manuale — oggi due note del lotto dicono una cosa e il resto
del lotto un'altra.

---

### A7 · Meta di progetto dentro il vault

metodo_03 §9.6: nel vault non entra nessun documento di metodo né nulla che racconti **come
il vault è stato costruito**; §7 spiega il perché in termini di misura (materiale che il
retrieval dovrà scartare a ogni interrogazione). Sei note di contenuto raccontano invece la
canonizzazione:

| Nota | Frase |
|---|---|
| `areas\fatto-quaderno-capoturno-linea1.md` | «È il documento che **il gate della Sessione 2** aspettava… le **tre gambe mancanti dei conflitti tracciati**» |
| `data\questione-pezzi-prodotti-l26130.md` | «La terza riga della tabella entra con **il lotto 1A della canonizzazione integrale**» |
| `areas\fatto-fermo-pkm-450-l26130.md` | «Il quaderno di linea, **entrato in archivio con il lotto successivo di canonizzazione**» |
| `areas\questione-codice-allarme-pkm-450.md` | «L'estratto del manuale…, **entrato in archivio con il lotto 1A**» |
| `entities\prodotto-af-sn-0450.md` | «non erano attestati dalle fonti disponibili **alla prima stesura di questa scheda**»; «fonti **non ancora canonizzate**» |
| `docs\doc-scheda-tecnica-af-sn-0450.md` | «la seconda gamba di quel confronto **non è in questo lotto**» |

Nessuna di queste frasi risponde a una domanda su Aurora, e «il lotto 1A» dentro un archivio
in cui «lotto» significa `L26130-L1-T2` è per giunta ambiguo. Lo stesso vale per
`areas\fatto-operatori-ccp3-linea1-maggio.md`: «Nessun documento **di questo lotto** le
associa a un nome» — dove «questo lotto» è il perimetro di canonizzazione, e per di più
restringe indebitamente un'affermazione di assenza (vedi A8).

**Cosa andrebbe fatto.** Riscrivere le frasi in termini di archivio: «il quaderno del
capoturno aggiunge una terza versione», «il manuale del costruttore introduce una terza
codifica». Il fatto resta, il ponteggio sparisce. Le occorrenze in `code\` e in
`workspace\_index-workspace.md` sono invece legittime e non vanno toccate: quelle cartelle
documentano il progetto per mandato.

---

### A8 · Due dichiarazioni d'assenza fuori regola

metodo_03 §10.12-bis: «Non dichiarare un'ASSENZA senza averla cercata su tutto `sources\`…
L'assenza verificata **si data e si riferisce al manifest**».

- `areas\fatto-allarme-acustico-md-3200-basso.md`: «⚠️ **Nessuna fonte in archivio** dice
  come il volume sia stato sistemato, né se l'intervento sia stato registrato altrove: il
  quaderno del capoturno di quel giorno non ne parla, e la scheda di manutenzione non porta
  una voce corrispondente.» — nessuna data, nessun manifest, e il perimetro dichiarato sono
  due file, non `sources\`.
- `areas\fatto-operatori-ccp3-linea1-maggio.md`: «Nessun documento **di questo lotto** le
  associa a un nome» — perimetro sbagliato: le sigle `DB` ed `EC` vanno cercate su tutto
  `sources\` prima di dire che non si sciolgono. (La seconda affermazione d'assenza della
  stessa nota, sulla squadra nominativa del 10/05, è invece formulata **correttamente**.)

**Cosa andrebbe fatto.** Eseguire davvero la ricerca su tutto `sources\` e riscrivere le due
frasi nella forma già usata correttamente in altre otto note del lotto («verificato su tutto
`sources\`, manifest v1.1, alla `data_nota` di questa nota»). Se `DB` o `EC` si sciolgono
altrove, la nota cambia di conseguenza.

---

### A9 · `kpi-manutenzioni-arretrate-2026`: due numeri di contorno che non reggono

- **«La scheda censisce 22 sigle di macchina».** Le 22 dello script comprendono un campo
  **vuoto** e la stringa letterale **«Macchina»**, che è l'intestazione ripetuta a metà file.
  Le sigle vere sono **20**. Un conteggio che ingoia l'artefatto del file è proprio ciò che
  §5.4 chiede di evitare dichiarando il criterio.
- **La tabella non chiude.** Dichiara «righe di dato **112**», «di cui `OK` 92», «`SCADUTO`
  11», «`RIMANDATO` 7»: 92 + 11 + 7 = **110**. Le due righe mancanti sono l'intestazione
  ripetuta e una riga con stato vuoto, e la nota non lo dice. Un lettore che somma trova un
  buco e non sa se sia suo o della nota.

**Cosa andrebbe fatto.** Portare a 20 le sigle escludendo intestazione e vuoto (dichiarando
il criterio), e aggiungere in tabella la riga che rende conto delle altre due — è essa stessa
un'informazione sul file, non un dettaglio.

---

### A10 · Citazioni non testuali fra virgolette basse

`areas\questione-verifiche-ccp3-10-05-tre-versioni.md`, tabella delle versioni, righe 15:00 e
16:00, cita «saltata verifica ore 15 … x fermo!!!» e «saltata verifica … e 16 x fermo!!!».
Nel quaderno la frase è **una sola e intera**: «CCP3 tasselli: saltata verifica ore 15 e 16 x
fermo!!!» (pag. 44). Le due stringhe fra virgolette basse **non esistono testualmente nel
file**; §2.3 chiede che esistano, e la suite di provenance le ha infatti segnalate (pur
attribuendole per errore al `.jpg`).

La sostanza è corretta e il blocco `## Fonti` della stessa nota riporta la citazione intera e
giusta. È la forma in tabella a essere fuori regola.

**Cosa andrebbe fatto.** Riportare la frase intera una volta, o togliere le virgolette basse
dalle celle e parafrasare.

---

## B — Contraddizioni non registrate nel canone

Tutte verificate sui grezzi. **Nove su dieci hanno già la loro nota-questione nel vault**, ed
è la parte migliore di questo lotto: quello che manca è la riga nel canone, in una sezione
datata, come prescrive §9.5. Nessun grezzo è stato toccato.

⚠️ Per B3, B4 e B5 il canone elenca già la divergenza **con meno gambe**. Vale il precedente
che il canone stesso ha fissato il 16/08 con «Misura del frammento: la terza lettura»: la
gamba nuova si registra come riga nuova, il canone si accresce e non si riscrive.

### B1 · Limite dell'ossigeno residuo in confezione: 1,0 % contro 2 %

- `Scheda_tecnica_prodotto_AF-SN-0450_rev4.pdf`, pag. 2 §3: O2 residuo **obiettivo < 0,7 %,
  massimo 1,0 %**.
- `appunti_capoturno_quaderno_linea1_OCR.txt`, pag. 43, ven 8/5: «gas MAP: contr0llo residuo
  O2 su confez: O,8% 0k **(lim 2%)**».

**Valore da preferire: la scheda tecnica**, che è il documento contrattuale verso il cliente.
Ma il 2 % è il limite **effettivamente applicato in linea** per decidere se andare avanti, e
nessun documento dell'archivio contiene quel valore. Nota: `data\questione-limite-o2-residuo.md`
(ben fatta: osserva che quel venerdì la conclusione non cambia, ma per la ragione sbagliata).

### B2 · Attività dell'acqua e umidità dello stesso prodotto, in due ordini di grandezza

- Scheda tecnica, pag. 2 §3: **aw 0,93** (tolleranza 0,92-0,95), **umidità 32 g/100 g**
  (max 34), pH 5,8.
- `test_shelf_life_accelerata_confezione_MAP_snack.csv`, riga 3 e seguenti: **aw 0,31**,
  **umidità 5,6 %**, pH 5,71 — e su tutte le 171 righe l'aw non supera mai 0,39.

**Nessuno dei due, e non è un refuso.** Il pH coincide, il che prova che le due fonti parlano
dello stesso prodotto. I valori della scheda descrivono un prodotto morbido, quelli delle
prove un prodotto secco; da aw dipende la classificazione microbiologica dichiarata al
cliente e all'autorità. Nota: `data\questione-aw-umidita-af-sn-0450.md`.

### B3 · Materiale della guarnizione **originale** della valvola azoto: PTFE, FKM o EPDM

- `R_ricambio_valvola_iniezione_azoto_PKM450_URGENTE.eml`: «guarnizioni **PTFE** alimentari».
- `manuale_uso_manutenzione_PKM450_estratto.pdf`, pag. 2 §3.5 e pag. 5 §7: «guarnizione a
  labbro… (**FKM** nera)», «la mescola **FKM** del ricambio originale».
- `scheda_manutenzione_ordinaria_forni_industrial.csv`, riga 26: cod. `PKM-4471-**EPDM**
  (orig. Pakmatic)`.

**Nessuno.** Il canone del 16/08 registra come dato l'affermazione dell'officina secondo cui
il kit originale monta guarnizioni **in PTFE**: quella premessa ha ora due fonti contro. E la
posta in gioco è precisa: **l'EPDM non è un fluoropolimero**, quindi se l'originale fosse in
EPDM non potrebbe produrre lo spettro misurato dal laboratorio sul frammento, e l'argomento
difensivo dell'officina cade. Nota: `areas\questione-materiale-guarnizione-pkm-450.md`, che
la tiene bene e distingue i due pezzi.

### B4 · Codice del ricambio della valvola azoto: da due sigle a quattro

Alle due già registrate — `PK45-VN2-08` (MOD-PR-04) e `PKV-088-N2` / `PKV-088-KIT` (mail
Pakmatic) — il lotto ne aggiunge due:

- manuale PKM-450: valvola completa **`PK-45.0770`**, guarnizione a labbro **`PK-45.0771`**
  (l'unica fonte che distingue i due articoli);
- scheda di manutenzione, riga 26: **`PKM-4471-EPDM (orig. Pakmatic)`**.

**Da riconciliare, e la spiegazione registrata non regge più.** Il canone attribuisce la
divergenza a «codice interno contro codice di catalogo»: con quattro sigle, **due delle quali
provengono dal costruttore stesso** e non coincidono fra loro, quella spiegazione va tolta
dal novero delle plausibili. Nota: `areas\questione-codice-ricambio-valvola-pkm-450.md`.

### B5 · Codice dell'allarme PKM-450: la terza codifica

Alla coppia registrata `E-214 GAS` (foto pannello) / `AL-217` (MOD-PR-04) il manuale aggiunge
**`A031` «allarme pressione gas»**, causa «pressione ingresso sotto 1,8 bar» (pag. 5, §8):
descrive esattamente il guasto del 10/05 e **non coincide con nessuno dei due**.

**Resta: nessuno.** Il manuale non scioglie, aggiunge un lato. Va però registrato un fatto
nuovo e utile: il colophon dichiara che l'elenco allarmi completo sta nel manuale integrale di
184 pagine, **che in archivio non c'è** — l'assenza da supposta diventa verificata. Nota:
`areas\questione-codice-allarme-pkm-450.md`.

### B6 · Il tassello AISI 316 non rilevato al primo colpo: 05/05 o 07/05?

- `checklist_metal_detector_manuale_operaio.txt`, 05/05 turno 2, ore 17:00: «inox nn passato
  al 1° colpo?? rifatto -> ok», nota «tassello AISI messo storto, riprovato x2 ok».
- `appunti_capoturno_quaderno_linea1_OCR.txt`, pag. 42, gio 7/5: «MD32OO h 18 tassello inox NN
  pasato prima volta… forse tassello mese male segnato su mod cmq».
- Lo stesso modulo, 07/05 ore 18:00: esito **regolare**, nessuna annotazione.

**Nessuno.** Stesso episodio con la stessa spiegazione, datato a due giorni e due ore di
distanza; oppure due episodi, di cui uno mai finito sul modulo di un CCP. La seconda lettura
è la grave. Nota: `areas\questione-tassello-inox-non-passato.md`.

### B7 · La Linea 1 ha prodotto una domenica che il piano non le assegnava

- `piano_produzione_settimanale_sett19_21.xlsx`, foglio «Sett 19», righe 42-43: per dom 10/05
  **due sole righe, entrambe Linea 2**. La Linea 1 non compare.
- Stesso foglio, riga 48, a penna: «il 10/05 turno 2 linea 1 SALTATO dalle 15 - confezionatrice
  ferma. Recupero lunedì» — la Linea 1 della domenica esiste solo qui.
- `checklist_metal_detector_manuale_operaio.txt`, FOGLIO 8: **tre turni** di Linea 1 il 10/05.
- Quaderno, pag. 44, e foglio OEE riga 145: idem.

**Nessuno.** Divergenza fra pianificato ed eseguito, con conseguenza sul perimetro delle
domeniche lavorate a maggio — che è già una contraddizione registrata sul solo versante della
Linea 2. Nota: `areas\questione-linea1-domenica-10-05-fuori-piano.md`.

### B8 · Ora di arrivo dell'officina al fermo del 10/05: 15:25 o 15:50

- `report_fermo_macchina_confezionatrice_MAP.txt`, §2: constatazione del capo officina alle
  **15:25**.
- Quaderno, pag. 44: «ariva ore **15.5O circa**».

**Nessuno.** Non cambia la durata del fermo, cambia il **tempo di risposta della
manutenzione** — venti minuti o quarantacinque, di domenica, sono due giudizi diversi sullo
stesso presidio. Nota: `areas\questione-arrivo-officina-fermo-pkm-450.md`.

### B9 · Le verifiche CCP3 del 10/05 esistono in tre versioni documentali

- `MOD-QA-07_10-05-26_L1_T2_scansione.jpg` (verificata a occhio dal revisore): 8 righe orarie,
  **5 eseguite**, 15:00 «macchina ferma», **16:00 e 17:00 barrate con un tratto rosso e vuote**,
  seconda firma su **una sola riga** (`MF` alle 19:55), campo «Verifica di fine turno
  (capoturno)» **in bianco**, nota a piè di modulo firmata `IP`.
- `checklist_metal_detector_manuale_operaio.txt`, FOGLIO 8 retro: **8 righe eseguite e
  conformi**, comprese le 16:00, 17:00 e 18:00, operatore `SV` — con la trascrittrice che
  annota di sua iniziativa che quelle righe «sembrano scritte tutte in una volta a fine
  serata» e che il capoturno ha risposto «le abbiamo fatte dopo».
- Quaderno, pag. 44: «saltata verifica ore 15 e 16 x fermo!!! · riprese ore 17 0k 18 0k 19 0k».

**Nessuno.** Il canone registra la NC 1 dell'audit e il caso registro cartaceo/datalogger sul
CCP2, ma **non** questa: due compilazioni cartacee dello stesso turno che non coincidono, su
fogli destinati alla cartella evidenze per la risposta al cliente entro 48 ore. Nota:
`areas\questione-verifiche-ccp3-10-05-tre-versioni.md`.

### B10 · TMC proposto a sei mesi contro i 45 giorni della scheda tecnica in vigore

- Scheda tecnica pag. 3: **shelf life 45 giorni**, residua garantita 2/3.
- `test_shelf_life_accelerata_confezione_MAP_snack.csv`, riga 173, nota R&D del 02/07:
  «proposta: **TMC 6 mesi** a T ambiente, da confermare con 90 gg reali».

**Vale la scheda**, ed è la lettura che `data\kpi-shelf-life-af-sn-0450.md` dà — correttamente:
è una proposta contro una specifica in vigore, non due documenti che si contraddicono. Va in
canone comunque, perché è il tipo di divergenza su cui un sistema interrogato risponderà «sei
mesi» citando una fonte vera, e perché una modifica di quella portata tocca etichetta e
accordo col cliente.

### B11 · Il riepilogo della scheda di manutenzione non quadra col file che riepiloga

Vedi A3 per i numeri. La divergenza è reale e non elencata; è **intra-file**, quindi va scritta
come `atomica` e non come `conflitto` (§2.4), ma la riga nel canone serve lo stesso — è un
riepilogo che un lettore prende per buono senza contare.

*(Conteggio B: B1-B10 sono le dieci voci; B11 è contata in A3 perché il difetto primario è
l'omissione della nota, non la divergenza.)*

---

## C — Falsi allarmi: trappole volute, già registrate. **Non si tocca niente.**

Annotati perché non tornino al lotto dopo, e perché il decision log li assorba (§9.5 passo 7).

1. **Pezzi/cartone di AF-SN-0450: scheda tecnica 10 contro listino e accordo quadro 12.**
   Canone §4, primo gruppo: «conflitto reale mai risolto in azienda». Una gamba è in questo
   lotto, l'altra no: **non è un difetto del lotto**, e la divergenza nasce quando entra il
   listino. ⚠️ Il modo in cui è stata anticipata è però A1: il falso allarme riguarda il
   contenuto, non la citazione del canone.
2. **Velocità nominali 1.250/780/640 pz/h a piano contro 1.800 e 1.200 ricavabili dall'OEE.**
   Canone, terzo gruppo, «Da riconciliare». `questione-velocita-nominali-linee` fa la cosa
   giusta: dichiara che 1.800 e 1.200 sono **calcolati qui** (14.400 ÷ 8 e 9.600 ÷ 8),
   riscontra gli addendi, e non sceglie. Ricontato: torna.
3. **Pezzi del lotto L26130-L1-T2: 8.940 (mass balance) contro 5.580 (OEE).** Canone, terzo
   gruppo, «Nessuno dei due da solo». La nota non sceglie, e — punto di merito — non tratta i
   **4.100** del quaderno come una terza stima, perché il quaderno dichiara il proprio
   perimetro («solo 4.1OO pz oggi + quelo di T1»). È la lettura corretta.
4. **Domeniche di produzione: il piano assegna 10, 17 e 24/05 alla Linea 2 e annota «3a
   domenica consecutiva» sul 10/05.** Canone, terzo gruppo, «Domeniche lavorate a maggio»:
   libro unico due, consumi/budget/RSU tre, conferma d'ordine 26/04-03/05-10/05. Le altre
   gambe sono fuori lotto; `questione-linea1-domenica…` fa bene a segnalare la conseguenza
   sulle ore festive e a rimandare.
5. **Organico Linea 2: il piano presuppone 7 operai × 3 turni = 21.** Canone, terzo gruppo;
   libro unico e timbrature sono fuori lotto. Registrato correttamente come dato del piano.
6. **Separatore CSV incoerente (98 righe con `;`, 14 con `,`), tre formati di data nella stessa
   colonna, intestazione ripetuta a metà file, righe duplicate alla lettera.** Canone §6,
   caratteristiche volute. Le note le dichiarano e **non le uniformano**: corretto.
7. **Righe duplicate e «riga reinserita da export precedente, verificare doppioni» nel CSV
   shelf life.** Stessa famiglia. `kpi-shelf-life` la dichiara e conta 171 righe e 21 prove:
   ricontato, torna.
8. **Degradi OCR del quaderno** (`0`↔`O`, `l`↔`1`, `[macchia]`, `[pagina strappata a meta]`).
   Alias classe A e §10.10. Nessuna nota ricostruisce i passaggi perduti: corretto.
9. **`E-214 GAS` contro `AL-217`.** Alias classe C. La nota non sceglie, e il manuale non
   viene usato per chiudere il nodo: corretto. (La terza codifica è B5, cosa diversa.)
10. **Le sigle `DB` ed `EC` sulle seconde firme dei turni 1 e 3 non hanno un nome.** §10.10 e
    il precedente `RANZATO_F`/`CESTARO_L`: non si inventa e non si conclude che le persone non
    esistano. `fatto-operatori-ccp3-linea1-maggio` fa bene a lasciarle come sono. ⚠️ Ciò che è
    fuori regola lì è solo il **perimetro** della dichiarazione d'assenza (A8).
11. **`fatto-quaderno-capoturno-linea1` nomina `alias_entita.md` nel corpo.** Sembra materiale
    di metodo dentro il vault, e non lo è: **metodo_03 §3.1 fa esattamente la stessa cosa nel
    proprio esempio compilato**, che nel blocco `## Fonti` scrive «(Marchetti, identificata in
    `alias_entita.md` §A.2)». Non si tocca. ⚠️ Da non confondere con A7, che riguarda il
    racconto della canonizzazione, e con A1, che è la citazione del canone.

**Bonus, falso allarme della suite e non del revisore:** `qa_provenance` segnala che in
`questione-codice-ricambio-valvola-pkm-450` la fonte `scheda_manutenzione_…csv` «non aggancia
nessuna affermazione: rumore nel payload». È falso: la riga 26 sostiene il quarto codice
`PKM-4471-EPDM`, che è il perno della nota. L'avviso va chiuso a mano, non la nota corretta.

---

## Sovra-atomizzazione: **nessun rilievo**

Campione di **18 note** nate dai quattro documenti multi-fatto (richieste otto). Per ciascuna
la domanda plausibile di cui è la risposta migliore.

**Dal quaderno del capoturno**

| Nota | La domanda |
|---|---|
| `fatto-quaderno-capoturno-linea1` | «Che cos'è il quaderno del capoturno di Linea 1, che periodo copre e come si legge?» |
| `kpi-produzione-0450-linea1-maggio` | «Quanti pezzi di 0450 ha fatto il turno 2 ogni giorno della settimana della promo?» |
| `fatto-operatore-senza-formazione-haccp-l26130` | «Chi compilava il registro del CCP2 il 10/05, ed era formato?» |
| `fatto-prodotto-non-segregato-deviazione-ccp2` | «Che fine ha fatto il prodotto lavorato durante la deviazione del CCP2?» |
| `questione-arrivo-officina-fermo-pkm-450` | «Quanto ci ha messo la manutenzione ad arrivare al fermo del 10/05?» |
| `fatto-fermo-forno-ft-01-05-05` | «Il forno FT-01 ha avuto fermi nella settimana della promo, e per cosa?» |

**Dalla trascrizione del MOD-QA-07**

| Nota | La domanda |
|---|---|
| `doc-mod-qa-07` | «Cosa prescrive il MOD-QA-07: ogni quanto, con quali tasselli, con quale esito valido?» |
| `kpi-seconde-firme-ccp3-maggio` | «Quante seconde firme mancavano prima dell'11/05 e quante dopo?» — è **la domanda che la responsabile qualità pone per iscritto sul post-it del foglio 10** |
| `fatto-giro-di-vite-seconde-firme-ccp3` | «Da quando la seconda firma è diventata obbligatoria nei fatti, e perché proprio allora?» |
| `fatto-operatori-ccp3-linea1-maggio` | «Chi sta sui tre turni di Linea 1, e cosa significano le sigle DB ed EC?» |
| `fatto-allarme-acustico-md-3200-basso` | «L'allarme acustico del metal detector ha mai dato problemi?» — la più sottile del campione, ma regge: l'esito valido del CCP3 richiede l'allarme, quindi «suona ma poco» è un esito non pienamente soddisfatto |
| `questione-verifiche-ccp3-10-05-tre-versioni` | «Le verifiche del metal detector del 10/05 sono state fatte?» |

**Dalla scheda di manutenzione**

| Nota | La domanda |
|---|---|
| `kpi-manutenzioni-arretrate-2026` | «Quante manutenzioni sono arretrate, e quali?» |
| `fatto-manutenzioni-rimandate-per-promo` | «La promo Tosano ha fatto slittare manutenzioni? Chi lo dice?» |
| `fatto-sonde-pt-104-in-taratura` | «Le sonde del pastorizzatore erano tarate il 10/05?» — è la domanda dell'auditor, e regge l'arbitrato datalogger/cartaceo |
| `fatto-valvola-modulante-pt-104-revisione-rimandata` | «C'erano interventi arretrati sull'organo che regola la temperatura del CCP2?» |
| `fatto-convalida-md-1800-scaduta` | «Ci sono metal detector con la convalida scaduta?» |

**Dalla scheda tecnica**

| Nota | La domanda |
|---|---|
| `doc-limite-o2-residuo-af-sn-0450` | «Qual è il limite di O2 residuo in confezione per lo snack, e con che frequenza si misura?» |

Due accoppiate meritano una riga, perché a prima vista sembrano spezzatino e non lo sono:
`fatto-giro-di-vite-seconde-firme-ccp3` (evento) e `kpi-seconde-firme-ccp3-maggio` (numero)
sono lo spareggio `data` vs `areas` di §1.2 applicato correttamente; `fatto-microperdite-
saldatura-l26130` e `fatto-repliche-shelf-life-l26130-divergenti` rispondono a due domande
diverse — «il lotto aveva un difetto di tenuta?» e «riguardava tutte le confezioni?» — e la
seconda cambia la natura del problema, da difetto di processo a difetto intermittente.

**Il difetto opposto, invece, c'è: vedi A4.** Il rischio di questo lotto non è stato
frammentare troppo, è stato lasciare senza padrona un fatto che tre documenti attestano.

---

## Verifiche condotte, per il verbale

- **Copertura dei fatti chiave.** Filo rosso punti 2, 3, 4 e le contraddizioni dei tre gruppi
  che toccano i sette grezzi, una per una. Tutte coperte **tranne il punto 3** (A4). Le
  contraddizioni con una gamba fuori lotto sono elencate in C1, C4, C5.
- **Fughe di canone.** Grep su tutto il vault per `canone`, `canonico`, `03_valutazione`,
  `metodo_03`, `alias_entita`, `tassonomia_vault`, più lettura integrale delle 45 note nuove o
  modificate. **Una fuga trovata** (A1), con una propagazione attenuata; una seconda
  occorrenza è risultata legittima (C11).
- **Sovra-atomizzazione.** 18 note campionate sui quattro documenti multi-fatto. Zero rilievi.
- **Numeri ricontati dal revisore, indipendentemente dallo script del lotto:** 195 verifiche
  orarie / 128 senza seconda firma / 147-119 prima dell'11/05 / 48-9 dopo → tornano; 112 righe
  di dato, 11 `SCADUTO`, 7 `RIMANDATO`, 16 voci distinte, 3 duplicati → tornano; 171 righe e 21
  prove di shelf life → tornano; 14.400 ÷ 8 = 1.800 e 9.600 ÷ 8 = 1.200, scarti 44 % e 54 % →
  tornano; media 6.161 pz sulle cinque giornate regolari → torna; 8.940 − 5.580 = 3.360 →
  torna. Solo i due conteggi di contorno di A9 non reggono.
- **Riscontro visivo** su `MOD-QA-07_10-05-26_L1_T2_scansione.jpg` (le note che lo citano
  portano `verifica: visiva`): 8 righe orarie, 5 eseguite, 16:00 e 17:00 barrate in rosso,
  seconda firma `MF` alle sole 19:55, «Verifica di fine turno» in bianco, nota a piè di modulo
  firmata `IP`. **Le note lo descrivono correttamente**, riga per riga.
- **Locator ricontrollati:** 30 circa, su tutti e sette i grezzi. Quattro sbagliati (A5), il
  resto corretto.
