# Rapporto del lotto 3F — il controllo pubblico ATS, e la chiusura del tema 3

> **Che cos'è** · L'esito del lotto 3F, l'ultimo del tema 3, eseguito il 24/08/2026 secondo il
> ciclo di `06_operativo\prompt\prompt_s4_lotti.txt` §3 e la PARTE 5 di
> `prompt\prompt_gate_3e_lotto_3f.txt`.
> **Chi lo legge** · Il titolare, e poi il coordinatore. ⚠️ **Questo rapporto contiene cinque
> cose strutturali, e per §4 del prompt dei lotti va al coordinatore PRIMA
> dell'approvazione** — sono raccolte in §10: un guasto della suite riparato in corsa, un buco
> della QA sulle date derivate, due candidati sulla misura e sul superlativo, e **il pattern
> che E26 ha imposto di nominare al terzo giro**.
> **Il lotto si è lavorato il 24/08/2026 e si è chiuso il mattino del 25**: le misure di
> chiusura portano la data e l'ora in cui sono state prese.
> **Misure** · tutte da script, ognuna con la sua ora (E44).

---

## 1. L'apertura

### 1.1 Un grezzo, e la conta dei fatti

**Un solo grezzo**: `notifica_ATS_ispezione_programmata_igiene.txt` — 13.186 byte, 249 righe.
Non è un documento solo: è **una PEC che incapsula un atto dell'autorità** più **due mail
interne** che di quell'atto fanno un piano di lavoro.

L'apertura di 3E aveva contato **24 fatti**. La conta rifatta qui ne dà **33 proiettati**, e la
differenza sta tutta nelle due mail: l'atto porta quindici fatti, le mail diciotto — dieci voci
di preparativi più la catena, la riunione, la pre-verifica e l'esclusione del nesso col reclamo.

⚠️ **Proiezione 33 note di contenuto: dentro la fascia 25-35 confermata al gate di 3E, sotto il
tetto dei 40 di E28. Il lotto non si spezza**, e lo scostamento dal conto d'apertura di 3E
(+9) si dichiara qui.

### 1.1-bis Il perimetro a consuntivo, incollato verbatim

<!-- PERIMETRO DEL LOTTO — generato da `06_operativo\conta_perimetro_lotto.py`
     il 2026-08-25. Si incolla VERBATIM nella tabella §1 del rapporto di lotto.
     I numeri del perimetro non si ricompongono a mano. -->

| Voce | Valore |
|---|---|
| Specie del lotto | **lotto di canonizzazione** |
| Grezzi nell'elenco | **1** |
| Note **candidate** dallo script di apertura | **0** |
| Note **toccate** in corso di lotto (E32) | **11** |
| Note **nate** nel lotto | **36** — 36 contenuto |
| **Note controllate in tutto** | **47** |
| Esito della suite | **0 ERRORI, 44 AVVISI** |

| Famiglia di avviso | Quanti |
|---|---|
| summary di N caratteri (tetto N) | **11** |
| dichiara l'hub [[area-qualita]] come proprio in related, ma quell'hub non la elenca nel corpo | **7** |
| dichiara l'hub [[lotto-lN]] come proprio in related, ma quell'hub non la elenca nel corpo | **6** |
| summary e title si sovrappongono per meno del N%: da ispezionare | **5** |
| summary contiene piu' di una frase | **4** |
| corpo di N parole: fra N e N, si motiva o si spezza | **3** |
| dichiara l'hub [[progetto-gestione-reclamo-rec-N-N]] come proprio in related, ma quell'hub non la elenca nel c | **3** |
| dichiara l'hub [[macchina-cip-N]] come proprio in related, ma quell'hub non la elenca nel corpo | **2** |
| dichiara l'hub [[area-direzione]] come proprio in related, ma quell'hub non la elenca nel corpo | **1** |
| dichiara l'hub [[area-logistica]] come proprio in related, ma quell'hub non la elenca nel corpo | **1** |
| dichiara l'hub [[area-risorse-umane]] come proprio in related, ma quell'hub non la elenca nel corpo | **1** |

⚠️ **La proiezione diceva 33, il consuntivo dice 36**: +3, e vengono tutti dagli strati di
controllo — uno dal giudizio (§7.3) e tre dalla revisione (§8.2), meno uno perso nella fusione
delle due note sugli attestati. **Dentro la fascia 25-35 c'era la proiezione, il consuntivo la
supera di uno**, ed è il quarto lotto di fila in cui lo scostamento sta tutto dopo la prima
stesura — che E52 tiene già fuori dalla soglia.

### 1.2 ⚠️ E37 NON SCATTA, e la ragione è misurata

Il lotto porta **zero fonti prescrittive**: `elenco_fonti_prescrittive.py` ne censisce **38**, e
la notifica ATS non è fra loro. **Nessuna riconciliazione verticale arretrata da riaprire.**

⚠️ **Che l'atto di un'autorità non sia una «fonte prescrittiva del corpus» è una scelta di
perimetro, e va detta**: il preavviso prescrive per **un evento** — che cosa tenere pronto il 9
giugno — non in permanenza. L'elenco delle fonti prescrittive raccoglie i documenti che
governano un processo, non gli atti che lo controllano una volta.

### 1.3 E53 — il dominio si verifica da script, e c'è

`verifica_dominio.py`, misura delle **21:40**: **tre fonti prescrittive citate PER SIGLA** nel
grezzo, tutte e tre citabili perché già canonizzate —

| Fonte | Sigla trovata | Dove |
|---|---|---|
| `manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt` | `HACCP` | l'art. 5 e il punto 3 dell'elenco richiesto |
| `IO-05_istruzione_operativa_lavaggio_CIP.docx` | `IO-05`, `CIP` | la riga dei preparativi sull'istruzione affissa |
| `scheda_sicurezza_detergente_acido_lavaggio_CIP.txt` | `CIP` | la stessa riga |

**Dominio dichiarato: `cip`** — ed è l'unico dominio dichiarato del progetto di cui il grezzo
cita **entrambe** le fonti per sigla. Le altre 17 fonti hanno solo riscontri deboli, che per
E56 non contano.

⚠️ **E la scelta non è comoda: è meccanica.** Il lotto tocca per contenuto almeno tre domini —
`acqua`, `formazione`, `cip` — e il criterio di E53 guarda **che cosa i grezzi fanno**, cioè
quali sigle citano, non di che cosa il lotto parli di più.

### 1.4 E59 — il collaudo respinge due espressioni, e non sono di questo lotto

`collauda_dominio.py --dominio cip`, misura delle **21:46**: **prova A superata**, **prova B
FALLITA su due espressioni**.

| Espressione | Riconosce | cita il dominio | quota fuori | Esito |
|---|---|---|---|---|
| `pulizi` | 21 | 3 | **0,57** | ⛔ **respinta** |
| `\bigien` | 14 | **1** | **0,71** | ⛔ **respinta** |

⚠️ **Sono parole comuni travestite da dominio**, ed è la specie che ha prodotto il 38,7 % di 3C
e il 63,6 % di 3B al primo taglio. `\bigien` prendeva quattordici note e **una sola** citava
IO-05 o la scheda di sicurezza.

⚠️ **Il dominio `cip` è nato al lotto 2A, il 19/08, PRIMA che E56 ed E59 esistessero**, e le due
espressioni generiche stavano lì da allora. **Il punto 2A della serie — 3,3 % — NON si
rimisura**: la serie fotografa le misure come sono state prese (§4.45). Da qui in avanti vale
la dichiarazione collaudata, e le due espressioni sono uscite da `candidate_r1.DOMINI` con la
ragione scritta accanto.

⚠️ **`tampon[ei] superfic` resta MUTA** anche a lotto chiuso: non riconosce nessuna nota del
vault. Va guardata al prossimo gate — se non riconosce niente, non stava riconoscendo niente.

⚠️ **La metà B era applicabile in apertura**, perché la fonte del dominio è già citata da note
del vault: nessuna dichiarazione differita, a differenza di 3E.

### 1.5 E60 — l'artefatto d'apertura, e l'accostamento per evento al primo impiego

`grandezze_condivise.py`, misura delle **21:41**:

| | |
|---|---|
| grandezze condivise **dentro** il lotto | **zero** — il lotto ha un grezzo solo, e la riconciliazione orizzontale interna non esiste per costruzione |
| grandezze del lotto **già nel vault** | **12 su 25** |
| entità del vault nominate dal grezzo | **11** |

⚠️ **E la data `09/06/2026` è fra le dodici**, portata da otto note del vault. **È l'aggancio
che ha innescato l'accostamento per evento** — l'estensione di E60 scritta al gate poche ore
prima: il **preavviso** e il **verbale dell'ispezione** registrano lo stesso evento, e il
verbale era nel vault dalla fetta pilota, canonizzato in S2.

**Sei confronti fatti, uno per uno:**

| # | Che cosa è stato accostato | Esito |
|---|---|---|
| 1 | il **protocollo e la data** del preavviso, nei due atti | ⛔ **divergono** — `0058214/2026` del 25/05 contro «nota prot. n. `0045821` del 27/05» |
| 2 | l'**obbligo di presenza** del titolare contro i presenti a verbale | ⛔ **divergono** — «intera durata» contro «dalle 11:30» su un controllo iniziato alle 09:15 |
| 3 | i **capitoli annunciati** contro quelli verificati | **dodici contro sei**, e la differenza la dichiara il verbale |
| 4 | i **quattordici documenti richiesti** contro la documentazione visionata | **cinque voci su quattordici** compaiono; due documenti visionati non erano stati chiesti |
| 5 | le **dieci voci dei preparativi** contro i tre rilievi | due rilievi non erano nella mail; **uno era nel sopralluogo interno del 27/05** |
| 6 | l'**ora di inizio** | annunciata alle 09:00, verbalizzata alle 09:15 |

⚠️ **Cinque dei sei confronti hanno prodotto una nota, e due una questione aperta.** Nessuno di
essi sarebbe stato fatto senza l'artefatto: il verbale non è un grezzo di questo lotto, e chi
apre non sa quali note di tre settimane fa parlino dello stesso giorno.

---

## 2. I due tassi (E41), col nome del dominio (E46)

`misura_due_tassi.py --lotto lotto_03f_controllo_pubblico_ats --dominio cip --corrette 0`
— **misura di chiusura delle 00:02 del 25/08/2026** (E44), dopo il terzo giro e la revisione.
⚠️ **Il lotto si è lavorato il 24/08 e si chiude dopo la mezzanotte**: le misure di chiusura
portano la data del giorno in cui sono state prese, le note quella del giorno in cui sono
nate.

| Tasso | Valore | Che cosa misura |
|---|---|---|
| **di riapertura** | **non applicabile** — zero note riaperte | il lotto non porta fonti prescrittive: E37 non scatta |
| **di difetto di produzione** | **8,3 %** — 3 su 36, dominio `cip` | il metodo |

### 2.1 ⚠️ IL PUNTO NON È DEGENERE, E LA CLAUSOLA DI E41 ESTESO SI È FERMATA DA SÉ

Il prompt del gate diceva: *«3F è mono-fonte come 3E, e la dichiarazione DEGENERE di E41 esteso
si scrive in apertura **se il conto la conferma**»*. **Il conto non la conferma.**

E41 esteso dichiara degenere un lotto **mono-fonte il cui unico grezzo È la fonte che governa il
dominio**. Qui il grezzo è mono, ma **non è una fonte prescrittiva del corpus**: le due fonti
del dominio `cip` sono altri due documenti, canonizzati altrove. **Nessuna nota di 3F cita
IO-05 per costruzione**, e infatti tre risultano scoperte.

⚠️ **È la clausola condizionale che lavora.** Scritta all'indicativo — «3F è degenere» — avrebbe
prodotto una dichiarazione falsa in apertura; scritta col condizionale della misura ha
obbligato a contare, e il conto ha detto no. **È §4.50 applicato a una regola invece che a una
pianificazione.**

### 2.2 ⚠️ I TRE CASI RESIDUI SONO TUTTI DELLA STESSA SPECIE, E NON SI AGGIUSTANO

| Nota | Che cosa fa scattare l'espressione |
|---|---|
| `doc-documentazione-richiesta-dall-ats` | la voce 5 dell'elenco dell'autorità: «procedure e registrazioni di **sanificazione**» |
| `fatto-la-lista-dei-preparativi-e-dichiarata-incompleta` | l'elenco delle dieci voci, che nomina «istruzione operativa del **CIP**» |
| `questione-ultima-potabilita-completa-2023-o-2026` | l'inciso «due ripetizioni... una dopo **sanificazione** del produttore di ghiaccio» |

⚠️ **In tutti e tre i casi la nota ENUMERA o CITA, non AFFERMA sul dominio.** Nessuna delle tre
dice qualcosa sul lavaggio CIP che l'istruzione operativa dovrebbe sorreggere: la prima
trascrive un elenco di un atto pubblico, la seconda elenca i titoli dei preparativi, la terza
riporta il motivo di una ripetizione di analisi.

⚠️ **NON si aggiustano.** Aggiungere `IO-05` alle tre note per portare il tasso a zero sarebbe
esattamente il trucco che E41 vieta: la fonte entrerebbe **per muovere il numero**, non perché
prescriva ciò di cui la nota parla (E36). **Il caso residuo si dichiara col suo nome, e questo
è il suo nome.**

⚠️ **CANDIDATO EMENDAMENTO — l'unità della misura.** `testo_della_nota` esclude già il blocco
`## Fonti` (E36 applicato allo strumento), ma resta l'intero corpo: **un elenco di titoli e una
citazione contano come «la nota parla del dominio» quanto un'affermazione.** Su un lotto che
canonizza un atto pubblico — cioè un documento fatto di elenchi — la specie è sistematica:
**tre casi su tre**. Il gate decida se la misura debba distinguere l'affermazione
dall'enumerazione, o se il caso residuo dichiarato basti.

### 2.3 La serie, con questo punto

| Lotto | Dominio | Difetto di produzione |
|---|---|---|
| R1 | perimetro CCP e tarature | **57,7 %** |
| 2A | `cip` | **3,3 %** ⚠️ *misurato prima di E56/E59, con due espressioni oggi respinte* |
| 2B | `acqua` | **0,0 %** su 27 |
| 2B-bis | `allergeni` | **9,1 %** su 33 |
| 3A | — | ⚠️ **NON MISURATO** |
| 3C | `certificazione` | **38,7 %** su 31 — con riserva |
| 3B | `formazione` | **36,4 %** su 22 — con riserva |
| 3D | `reclami` | **20,0 %** su 35 — riserva sciolta |
| 3E | `ritiro` | **0,0 %** su 30 — degenere, mono-fonte sulla fonte del dominio |
| **3F** | **`cip`** | **8,3 %** su 36 — ⚠️ **tre casi residui, tutti enumerazioni** |

---

## 3. E63 — la copertura verificata al contrario

Il grezzo porta **due strutture numerate** e una lista puntata. Ognuna è stata scorsa, e ogni
voce senza nota si dichiara col suo motivo.

### 3.1 I quattordici documenti richiesti

**Tutti e quattordici sono nominati da almeno una nota.** Sette hanno una nota propria — 4, 5,
6, 7, 10, 12, 13 — e sette vivono nella padrona `doc-documentazione-richiesta-dall-ats`: **1**
registrazione sanitaria, **2** visura e planimetria, **3** manuale di autocontrollo, **8**
rintracciabilità, **9** reclami e ritiro, **11** idoneità sanitarie, **14** temperature.

⚠️ **Il motivo per cui non hanno una nota propria è lo stesso per tutte e sette**: l'atto le
**elenca** e basta. Che cosa Aurora abbia per ciascuna non sta in questo grezzo, e scriverne
una nota vorrebbe dire scrivere sul contenuto di documenti che questo lotto non porta.

### 3.2 Le undici voci dei capitoli

Coperte dalla nota `fatto-dodici-capitoli-annunciati-undici-elencati`, che le porta tutte in
tabella. ⚠️ **Nessuna voce ha una nota propria, e non deve averla**: sono le voci di un elenco
di attenzione, non fatti dell'azienda.

### 3.3 Le dieci voci dei preparativi

⚠️ **Dieci su dieci hanno una nota**, e otto ne hanno una dedicata. Le altre due — le
registrazioni CCP e l'analisi dell'acqua — sono diventate **questioni aperte**, perché su
entrambe l'archivio porta una divergenza.

### 3.4 Le sezioni dell'atto, e l'unica senza nota

⚠️ **`INFORMATIVA PRIVACY` non ha nessuna nota, ed è deliberato**: è la formula standard degli
artt. 13-14 GDPR, identica per ogni atto di quell'ufficio, e non porta nessun fatto di Aurora.
Tutte le altre sezioni — oggetto, visti, comunicazione, documentazione, obblighi, avvertenze,
responsabile del procedimento, firma — hanno almeno una nota.

---

## 4. Che cosa il lotto ha trovato

### 4.1 ⛔ IL VERBALE RICHIAMA UN PREAVVISO CHE NON È QUELLO RICEVUTO — **T176**

| | Il preavviso sulla PEC | Il preavviso richiamato dal verbale |
|---|---|---|
| protocollo | `0058214/2026` | `0045821` |
| data | `25/05/2026` | `27/05/2026` |
| destinatario, oggetto, ufficio | coincidono | coincidono |

⚠️ **Il numero richiamato dal verbale è più BASSO pur portando una data posteriore di due
giorni** — osservazione, non prova: che i protocolli di quell'ufficio siano progressivi
nell'anno nessuno dei due documenti lo dice.

⚠️ **Il protocollo `0045821` non compare in nessun altro documento del corpus**: assenza
verificata su tutto `sources\`, artefatto
`ricerche_assenza\secondo-preavviso-ats-0045821_2026-08-24.md`. Le due sole occorrenze stanno
nel verbale, cioè nel documento che lo cita.

**Tre letture, e nessuna fonte sceglie**: due atti distinti, un errore di trascrizione nel
verbale, due numerazioni dello stesso ente. ⚠️ **Non è un dettaglio formale**: il verbale è
l'atto che documenta il controllo e il preavviso è il presupposto che vi richiama — **se i due
non si agganciano per numero e data, la catena non si chiude sui documenti**.

### 4.2 ⛔ «I MODULI CI SONO TUTTI MA VANNO RIVISTI UNO PER UNO» — **T179**

La riga più pesante del lotto, scritta **quindici giorni prima di un controllo ufficiale** e
**sei giorni prima della scadenza dell'azione correttiva** che di quella prassi doveva
verificare l'efficacia:

> «registrazioni CCP ultimi 12 mesi: i moduli MOD-QA-12 e MOD-QA-07 ci sono TUTTI ma vanno
> RIVISTI uno per uno, e sappiamo tutti perché. La seconda firma di verifica a fine turno
> **deve risultare sistematica da aprile in poi**»

| Fonte | Che cosa dice della seconda firma |
|---|---|
| la disposizione del **25/05** | deve **risultare** sistematica **da aprile in poi** |
| `NC-2026-068` del **13/04** | **assente** su `MOD-QA-12`, «prassi non ancora assimilata» |
| la nota a margine siglata `EM` del **07/05** | «ancora 2^ firme mancanti. la NC scade, NON si puo andare avanti cosi» |
| la trascrizione del modulo, **04-10/05** | **119 su 147** senza *(contate)* — 81 % |
| la stessa, **11-12/05** | **9 su 48** — 19 %, dopo il giro di vite |
| `NC-2026-106` del **26/05**, il giorno dopo | **19 su 21** con la seconda firma, stato `IN CORSO` |
| il **verbale ATS** del 09/06 | campiona entrambi i moduli sul solo periodo **`01/05-31/05/2026`** |

⚠️ **«Rivedere» ammette due letture, e nessuna fonte sceglie**: *controllare che ci sia tutto*,
oppure *far risultare* ciò che il verbo «risultare» chiede — integrando a posteriori le firme
mancanti. **La seconda è la grave, e la frase non la esclude**: chiede a registrazioni già
chiuse di risultare in un certo modo, non a un comportamento futuro di esserlo.

⚠️ **E il periodo che l'autorità ha campionato è esattamente il mese su cui la revisione stava
lavorando.**

### 4.3 ⛔ IL CARRELLO DATO PER RIMOSSO DUE VOLTE, E TROVATO IN LINEA DUE VOLTE — **T180**

Il giudizio ha trovato, **dentro una fonte che la questione già citava**, due frasi che nessuno
aveva usato:

- **13/05, ore 14:52** — il capo officina: «el careto intanto **lo go porta fora dala linea**, adeso el xe in oficina»;
- lo stesso messaggio, poco sopra: «el careto **sta li da quando ghe son mi, 11 ani**, e nissun ga mai dito gnente fin a febraro».

⚠️ **La seconda CHIUDE una delle due letture aperte da agosto**: ad aprile il carrello non era
mai stato rimosso, quindi la chiusura della non conformità di aprile **e** la nota del manuale
di autocontrollo dicono il falso — e il manuale è il documento che si esibisce all'ente di
certificazione e all'autorità.

⚠️ **E la prima ne apre una più stretta**: il 13/05 la rimozione è dichiarata compiuta, il
**25/05** la qualità ordina «VA TOLTO», il **09/06** l'autorità lo trova a bordo della
confezionatrice. **Fra il 13/05 e il 25/05 nessun documento registra un rientro.**

⚠️ **Undici anni di prassi, e il primo rilievo è di febbraio.**

### 4.4 ⛔ IL SOPRALLUOGO INTERNO DEL 27/05, E LA CASSA COME CAUSA DICHIARATA — **T181**

`NC-2026-107`, gravità **alta**, reparto **Direzione**, **APERTA** senza data di chiusura:

> «Preavviso ispezione ATS/ULSS 9 del 09/06 su requisiti strutturali Reg. CE 852/2004 All. II:
> sopralluogo interno evidenzia **4 punti critici** (pavimento zona forni, zanzariere,
> spogliatoio L3, **intonaco cella CF-01**)»
> — causa radice: «manutenzione strutturale **rinviata per priorità di cassa**» — **8.500,00 €**

⚠️ **Due dei quattro punti diventano rilievi dell'autorità tredici giorni dopo**, e uno di essi
porta una prescrizione a trenta giorni. ⚠️ **Il preavviso non ha scoperto quei punti: li ha
resi urgenti.**

⚠️ **E il «piano vero con le responsabilità» annunciato dalla qualità per il giorno dopo
esiste, in questa forma.** La prima stesura di questo lotto dichiarava che non fosse nel
corpus: **era falso, e l'ha trovato il giudizio.**

### 4.5 ⛔ L'ULTIMA POTABILITÀ COMPLETA: 2023 O 2026 — **T178**

Segreteria e responsabile qualità danno l'ultima analisi completa al **novembre 2023**. Il
registro dei rapporti di prova ne porta **due nel 2026** — 15/01 e 16/04 — e quella di aprile
ha **tre righe `NON CONFORME`**: coliformi e carica batterica sul produttore di ghiaccio, ferro
al lavabo degli spogliatoi, con due ripetizioni rientrate il 24/04 e una verifica supplementare
il 19/05 **richiesta dalla stessa responsabile qualità**.

⚠️ **Due letture, e nessuna fonte sceglie**: «completa» significa più di ciò che il registro
contiene, oppure la ricerca è stata fatta altrove — o l'affermazione è sbagliata. ⚠️ **Il
perimetro di parametri di una «potabilità completa» non lo dà nessun documento**: il manuale
prescrive la **frequenza**, non l'elenco.

### 4.6 ⚠️ Le altre due divergenze, e i confronti che non hanno prodotto nulla

- **T177** — l'obbligo di presenza del titolare contro le due ore e un quarto iniziali. ⚠️ **Il verbale non muove rilievo sul punto**, e il silenzio di un verbale non è un'attestazione.
- **Dodici capitoli annunciati, sei verificati**, e la differenza la dichiara l'autorità: un preavviso vincola poco il controllo che annuncia.
- **Cinque delle quattordici voci richieste** compaiono fra i documenti visionati, e **due documenti visionati non erano stati chiesti**. ⚠️ **Il perimetro dell'affermazione è dichiarato**: che una voce non compaia al §2 significa che il verbale non la registra, non che il documento non sia stato esibito.
- **L'ora di inizio**: annunciata alle 09:00, verbalizzata alle 09:15. Nessuna conseguenza in nessuna fonte, e nessuna nota propria.

---

## 5. ⛔ UN GUASTO DELLA SUITE, TROVATO E RIPARATO IN CORSA — E10 sul secondo delimitatore

**Il pacchetto del giudizio arrivava ai giudici con la fonte principale del lotto troncata al
5 %.** Il guasto è stato visto prima di lanciare il primo giro, e riparato subito: §4 del
prompt dei lotti dice che **un controllo bacato non è un candidato, è un guasto**.

### 5.1 Che cosa succedeva

`qa_provenance.pacchetto_giudizio` separava le fonti dell'appendice con `--- <nome> ---`, e
`taglia_pacchetto.spezza` le rileggeva con `^--- (.+) ---$`.

⚠️ **Quella forma compare DENTRO i grezzi.** La notifica ATS ne porta due nel proprio testo —
`--- TESTO DELL'ATTO ALLEGATO ---` e `--- FINE TESTO DELL'ATTO ---` — e lo splitter le ha
lette come inizio di altre due fonti.

| | |
|---|---|
| la fonte principale del lotto, nell'appendice | **638 caratteri su 13.186** — il **5 %** |
| le due mail interne, che sono metà del lotto | **assenti da due fette su tre** |
| che cosa dichiarava la guardia | **«completa»**, per tutte e tre le fette |

⚠️ **La guardia non poteva prenderlo**: verificava che l'appendice **contenesse qualcosa**
(più di 200 caratteri), non che portasse la fonte **intera**. È §4.49 — un controllo copre le
superfici che il suo collaudo esercita, non quelle che il suo docstring dichiara.

### 5.2 Perché è E10, e perché è rimasto scoperto per undici lotti

⚠️ **Il commento di `pacchetto_giudizio` spiegava già la stessa cosa per le NOTE**: «delimitatore
che non può comparire dentro un grezzo. Con "NOTA:" il conteggio delle note inviate si
falsava, perché quella stringa compare anche nel testo del manuale HACCP». **La stessa medicina
non era stata applicata alle FONTI.**

⚠️ **E il corpus, scandito per intero, ha DUE grezzi che scrivono una riga di quella forma**:
la notifica ATS di questo lotto e `budget_2026_vs_consuntivo_per_linea.xlsx`, che appartiene al
tema 6 e **non è ancora canonizzato**. **Nessun giudizio passato è stato degradato**, e il
secondo caso sarebbe arrivato al tema 6.

### 5.3 La riparazione, e il difetto piantato

- Il delimitatore delle fonti prende la forma di quello delle note: **`>>>>> FONTE: <nome>`**, un prefisso che un grezzo non scrive.
- **La guardia confronta i caratteri, non la presenza**: ogni fonte dev'esserci **per intero**, com'è nel pacchetto.
- **Difetto piantato**: `qa\_collaudo\collaudo_taglio_fonti.py`, cinque casi, di cui **due difetti piantati** e **una premessa** — che il grezzo finto porti davvero la riga insidiosa. Senza la premessa il caso passerebbe per il motivo sbagliato.
- **Collaudi: 12 su 12**, il nuovo compreso.

⚠️ **La via vecchia è l'unico pezzo di logica che il collaudo reimplementa, ed è deliberato**:
non esiste più in produzione, quindi non si può chiamare. La via nuova si chiama sempre
(`T170`).

### 5.4 ⚠️ E il pacchetto rifatto ha cambiato il verdetto

Il primo giro ha girato **sul pacchetto riparato**. ⚠️ **Non c'è un controfattuale**: non si sa
che cosa avrebbero detto i giudici sul pacchetto mutilato, e non si è voluto scoprirlo — un
giudizio su fonti troncate è ciò che §4.31 chiama **ingresso degradato**, e vale zero.

---

## 6. ⚠️ UN BUCO DELLA QA, DICHIARATO E NON RIPARATO — la data derivata

`qa_provenance` esenta un **numero** dichiarato derivato — `RE_DERIVATO` cerca
`(calcolat|contat|derivat|somma|differenza)` entro sessanta caratteri — **ma l'esenzione vale
solo per `genere == "numero"`**. Una **data** derivata non ha esenzione.

⚠️ **Il caso di questo lotto**: la riunione di preparazione è convocata per «Domani mattina»
in una mail del 25/05. Il **26/05** è un valore derivato, esatto e marcabile, e la QA lo
respinge comunque.

⚠️ **La conseguenza è che la nota ha dovuto TOGLIERE la data dal corpo**, e con essa lo slug è
stato rinominato — `fatto-riunione-di-preparazione-del-26-maggio` →
`fatto-riunione-di-preparazione-il-mattino-dopo` (E30 esteso, coi wikilink nello stesso turno).
**Il vault è meno preciso di quanto potrebbe essere, per un buco dello strumento.**

⚠️ **E la via d'uscita facile è un trucco**: scrivere «il ventisei maggio» in lettere passa il
controllo e dice la stessa cosa. **Non è stato fatto**, ed è la ragione per cui il punto va al
gate invece di essere aggirato.

⚠️ **CANDIDATO EMENDAMENTO**: E50 dice che «un numero che la fonte non enuncia è un valore
derivato ANCHE QUANDO SI OTTIENE CONTANDO». **Una data ottenuta da «domani» più la data della
mail è esattamente quello**, e la marca dovrebbe valere per lei come per un numero. **Il fix è
di perimetro di un controllo** (§4), quindi si applicherebbe subito — ma tocca lo strato
deterministico della provenance, e questa sessione non lo ha toccato di propria iniziativa.

---

## 7. Il ciclo di giudizio

### 7.1 I giri, e i numeri

Strato di giudizio con `PROMPT_GIUDIZIO` **v2** (congelato 2026-08-18), subagenti a **contesto
pulito**, mai il canone. Il pacchetto è stato tagliato in **tre fette**, una per giudice, con
l'appendice completa verificata carattere per carattere dalla guardia riparata (§5).

| Giro | Note giudicate | Rilievi accolti | Che cosa hanno colto |
|---|---|---|---|
| **1** | **38** — 13 + 13 + 12 | **10** | 9 `afferma_oltre` e 1 `entrambi` |
| **2** | **39** | **5** | §7.4 |
| **3** | **42** — 14 + 14 + 14 | **4** | §7.6, e il pattern in §7.7 |

### 7.2 ⚠️ CHE COSA HA COLTO IL PRIMO GIRO, ED È DI DUE SPECIE SOLE

**Sei rilievi su dieci sono affermazioni universali sbagliate**, e la cosa notevole è che
**cinque di esse hanno il soggetto DENTRO la fonte**, non l'archivio:

| Nota | L'affermazione | Perché cade |
|---|---|---|
| bancali di Linea 3 | «l'**unico** dei preparativi che riguarda lo stato dei luoghi» | le voci fisiche sono **tre** |
| DoC film MAP | «l'**unica** voce che dipende da un terzo» | sono **tre** |
| planimetria esche | «il ritardo **non è del fornitore**» | proprietà, imputazione e intenzione non hanno riscontro |
| moduli CCP | ««sappiamo tutti perché» è la **sola** motivazione scritta» | la riga prosegue «com'è da procedura post-audit» |
| moduli CCP | «**aprile non è documentato** da nessuna fonte» | `NC-2026-068` del 13/04 lo documenta |
| MD-3200 | «afferma il contrario... **senza riscontro**» | è una conclusione di chi scrive |

⚠️ **E57 dice che un superlativo col soggetto-DOCUMENTO regge, perché si verifica sulla fonte.
Questi si verificavano sulla fonte, e la fonte li ha smentiti.** Non erano non verificabili:
erano **verificabili e falsi**. È una specie diversa da quella di E47, e la distinzione conta:
E47 protegge da ciò che nessuno può controllare, **qui il controllo si poteva fare e non era
stato fatto**.

**Gli altri quattro sono contesto importato o conclusioni giuridiche**: la regola generale sul
controllo senza preavviso, «distinte e **cumulabili**», «Fantin e Marchetti **dall'inizio**»
dedotto dal silenzio, «esiti **Conforme**» su una campagna che ne porta tre non conformi.

### 7.3 ⛔ LA TERZA DOMANDA HA PRODOTTO PIÙ DELLA SECONDA

Il terzo compito di `PROMPT_GIUDIZIO v2` — la lacuna di copertura — è **segnale poco più di una
volta su due**, e questo lotto è l'eccezione: **ha prodotto una nota nuova e ha ribaltato due
note esistenti.**

| Segnalazione | Esito |
|---|---|
| `non_conformita_interne_registro_2026.csv` **NC-2026-107** | ⛔ **accolta** — nasce `fatto-sopralluogo-interno-del-27-maggio-quattro-punti-critici`, e due note vanno riscritte |
| `NC-2026-068` (13/04) e `NC-2026-106` (26/05) | ⛔ **accolte** — due gambe nuove alla questione dei moduli CCP, e la frase «aprile non è documentato» cade |
| `report_fermo_macchina` — le due frasi di Dal Maso del 13/05 | ⛔ **accolta** — la questione del carrello cambia di segno |
| verbale §1.1, «n. 24 postazioni esca» | ✅ accolta — il totale che la nota dava per non ricavabile |
| manuale HACCP §10.3, l'Autorità competente | ✅ accolta — gamba della scheda dell'ente |
| verbale §1.8 e §1.5 sugli spogliatoi | ✅ accolta — la voce che l'azienda temeva è passata |
| verbale §2, la separata istruttoria sul reclamo | ✅ accolta |
| gli hub d'area che «non citano gli atti ATS» | ⛔ **respinte** — il giudice non conosce il grafo: un hub linka gli spoke, non le loro fonti |
| le fonti «della stessa grandezza» già possedute da un'altra nota | ⛔ **respinte** — un fatto, un padrone: la gamba vive nella sua nota, e il rimando la nomina |
| `NC-2026-107` come terza gamba sulla **data del preavviso** | ⛔ **respinta** — la riga è **datata** 27/05 e registra il preavviso; il «del 09/06» che porta si riferisce all'**ispezione**, non all'atto. **Il giudice ha inferito una gamba che la riga non dà** |

⚠️ **Il rumore della terza domanda ha la forma nota — il giudice non conosce il grafo — e una
forma nuova: l'inferenza sulla data.** Va nominata, perché è la prima volta che la terza
domanda produce un'affermazione sbagliata invece di una segnalazione inutile.

### 7.4 Il secondo giro, e il pattern che si ripete

| Giro | Note giudicate | Rilievi accolti | Per fetta |
|---|---|---|---|
| **1** | **38** | **10** | 3 · 4 · 3 |
| **2** | **39** | **5** | 1 · 4 · **0** |

⚠️ **Una fetta su tre è tornata pulita al secondo giro**, e le altre due hanno prodotto la metà
dei rilievi del primo.

### 7.5 ⛔ IL PATTERN CHE E26 IMPONE DI NOMINARE: IL SUPERLATIVO SULL'ELENCO

**Tre occorrenze, su tre note diverse, in due giri.**

| Giro | Nota | L'affermazione |
|---|---|---|
| 1 | bancali di Linea 3 | «l'**unico** dei preparativi che riguarda lo stato dei luoghi» — sono **tre** |
| 1 | DoC film MAP | «l'**unica** voce che dipende da un terzo» — sono **tre** |
| 2 | pre-verifica | «l'**unico** dei preparativi che compra tempo di qualcun altro» — smentito dalla stessa mail |

⚠️ **Il soggetto di questi superlativi non è l'archivio: è UN ELENCO CHE STA NELLA FONTE.** Per
**E57** un superlativo con soggetto-documento **regge**, perché si verifica sulla fonte. **E
qui la fonte, verificata, li smentisce tutti e tre.**

⚠️ **La specie non è quella di E47.** E47 protegge da ciò che nessuna nota può controllare —
«l'unico documento dell'archivio». **Questi erano controllabili in dieci secondi, contando le
righe di una mail, e non sono stati controllati.**

⚠️ **CANDIDATO EMENDAMENTO — E57 classifica, non obbliga.** La regola dice quale superlativo
regge e quale no; **non dice che quello che regge va CONTATO**. Per i numeri l'obbligo c'è —
E50: il valore contato porta la marca, e la marca «dichiara che va ricontato». **Per il
superlativo su un elenco citato non c'è nessuna marca e nessun obbligo di conta**, e la specie
è ricomparsa tre volte in un lotto solo, due volte dentro correzioni scritte per chiuderla.

**Forma proposta**: *un'affermazione universale il cui soggetto è un elenco della fonte porta
il conto, come un valore derivato porta la marca — «tre su dieci (contate)», non «l'unica»*.

### 7.6 Il terzo giro, e la conta dei tre

| Giro | Note giudicate | Rilievi accolti | Per fetta |
|---|---|---|---|
| **1** | **38** | **10** | 3 · 4 · 3 |
| **2** | **39** | **5** | 1 · 4 · **0** |
| **3** | **42** | **4** | 2 · 2 · **0** |

⚠️ **Il terzo giro ha giudicato quarantadue note, tre in più del secondo**, e sono le note
nate dalla revisione: **E58 è soddisfatto**, ogni nota del lotto ha visto lo strato di giudizio
almeno una volta. ⚠️ **E la terza fetta è tornata pulita due giri di fila.**

### 7.7 ⛔ E26 CHIEDE IL PATTERN, E IL PATTERN C'È: IL PERIMETRO DELL'AFFERMAZIONE ECCEDE IL PERIMETRO DELLE FONTI

Il terzo giro ha prodotto ancora rilievi accolti. Per **E26** il lotto non si chiude ripetendo
il ciclo: **si chiude nominando la classe d'errore che li rigenera.** Eccola, coi quattro
rilievi del giro più le due code che la revisione della copertura ha fatto emergere nello
stesso passaggio.

| Nota | L'affermazione | Di che specie è |
|---|---|---|
| rischio medio-alto | «una classe di rischio non si guadagna né si perde con la conformità» | **regola generale importata**: l'atto motiva **questa** classificazione, e non dice come una classe si formi |
| carrello (ispezione ATS) | «è la **prima volta** che la ricambistica a bordo linea viene contestata da un'autorità pubblica» | **primato sull'archivio** — specie di **E47** |
| ispezione attesa dal 13/05 | «ed è **la ragione per cui** il preavviso viene letto come una novità» | **nesso causale** che nessuna fonte stabilisce |
| pre-verifica simulata | «le affida **la formazione dell'anno**» | **estensione su un elenco della fonte**: il §7.3 le attribuisce **una** delle voci — specie di §7.5 |
| Vicentini (coda) | «è il **primo documento dell'archivio** che le attribuisce un incarico ricorrente» | **primato sull'archivio** — specie di **E47** |
| riunione del mattino dopo (coda) | «e **l'archivio** possiede il primo e non il secondo» | **assenza sull'archivio** senza artefatto — specie di **E3/E43** |

⚠️ **Sei affermazioni, sei perimetri diversi, e nessuna delle sei sta dentro il perimetro
delle proprie fonti.** Non è un difetto di lettura — le fonti erano lette bene — **è un difetto
di perimetro**: chi scrive dice una cosa vera **di ciò che ha davanti** e la enuncia **di ciò
che non ha davanti**.

⚠️ **E la classe non ha una regola: hanno una regola le sue specie.** **E47** governa il
primato sull'archivio, **E3/E43** l'assenza sull'archivio, **E57** classifica il superlativo su
un elenco. **Nessuna regola dice la cosa semplice che le tiene insieme** — *un'affermazione
vale nel perimetro delle fonti che la nota cita, e per uscirne serve un artefatto o un
rimando*. ⚠️ **È la ragione per cui la classe ricompare a ogni giro pur avendo già tre
emendamenti addosso**: ogni emendamento ne chiude una porta e la classe entra dall'altra.

⚠️ **La regola generale importata e il nesso causale non hanno nemmeno la loro porta**, e sono
le due specie che nessun controllo deterministico può vedere: non contengono numeri, non
contengono superlativi, non contengono negazioni. **Le vede solo un lettore che confronti la
frase col perimetro** — ed è quello che lo strato di giudizio ha fatto tre volte.

**Il pattern è nominato. Per E26 il lotto si chiude.**

## 8. La revisione contro il canone (E45), e le cinque divergenze nuove

La revisione gira in **sessione diversa** e riceve il canone; il giudizio no. Ha prodotto due
raccolti distinti, e vanno tenuti distinti perché costano cose diverse:

| | Che cos'è | Quante | Dove sono finite |
|---|---|---|---|
| **rilievi A** | errori DENTRO le note già scritte | **sei**, tutti accolti | corretti nel turno, nelle note |
| **sovra-atomizzazione** | due note per un fatto solo | **una** | le due note sugli attestati fuse in `questione-due-attestati-mancanti-o-due-assenti-al-corso` |
| **righe B** | divergenze NUOVE fra il grezzo e il vault | **cinque**: quattro scritte, **una tracciata** | note nuove, gambe nuove, la sezione datata del canone — e **T182-T186** |

### 8.1 I sei rilievi A, e la specie che ricorre

| | Che cosa diceva la nota | Che cosa dicono le fonti |
|---|---|---|
| 1 | «**tre** voci portano un periodo» | **quattro** *(contate)* |
| 2 | gli annunciati e non verificati sono **cinque** | **sei**: mancava il Capitolo III |
| 3 | la glossa dell'hub restava a valle di una correzione già fatta nella nota | E39 esteso, colto in flagranza |
| 4 | tabella di confronto a metrica mista | le due colonne contavano cose diverse |
| 5 | `area-qualita` non elencava una nota che la dichiara | reciprocità dell'hub |
| 6 | locator a `pag. 2` | la sezione sta a **pag. 3** |

⚠️ **Quattro rilievi su sei sono conti sbagliati su elenchi che stanno nelle fonti**, ed è la
stessa specie che il giudizio ha colto tre volte con i superlativi (§7.5). **La specie non è
del giudizio né della revisione: è della scrittura**, e il candidato emendamento di §7.5 la
prende per intero.

### 8.2 Le cinque righe B, e da dove nascono

**Quattro nascono dallo stesso accostamento**: il verbale del 09/06 contro ciò che l'azienda
aveva già scritto altrove — nel registro delle non conformità, nel manuale esibito quel
giorno, nella comunicazione al personale. ⚠️ **La quinta è di segno opposto: è l'atto
dell'autorità a non mantenere ciò che l'atto dell'autorità aveva promesso.**

| | La divergenza | Dove è finita |
|---|---|---|
| **B1** | l'ispezione era attesa **dodici giorni prima della PEC**, con l'oggetto giusto, per canale informale | nota nuova `fatto-l-ispezione-attesa-dal-13-maggio-per-via-della-consulente` |
| **B2** | **8.500,00 €** per quattro punti contro i **«diciotto mila»** del solo pavimento della zona forni | nota nuova `questione-la-stima-e-il-preventivo` |
| **B3** | il termine **08/08** scade **nove giorni prima** della chiusura **17/08** in cui i lavori sono promessi | ⏳ **tracciata a T184**, non scritta — e la sola gamba di 3F in `fatto-il-titolare-promette-i-lavori-alla-chiusura-estiva` |
| **B4** | il titolare dichiara a verbale che la procedura è «in revisione», e il manuale esibito lo stesso giorno la dà per applicata | gamba nuova su `questione-carrello-ricambi-dichiarato-rimosso` |
| **B5** | il preavviso rimanda al verbale per le modalità del riesame, e il verbale non le porta | gamba nuova su `doc-obblighi-dell-osa-durante-il-controllo` |

### 8.3 ⛔ B3 NON SI SCRIVE, E A FERMARLA È STATO UN CONTROLLO, NON UNA LETTURA

La divergenza era scritta, la nota esisteva, la QA del lotto era verde. ⚠️ **A fermarla è
stato `verifica_matrice_lotti.py`**, che ha alzato *GIA' COPERTO
`comunicazione_chiusura_estiva_2026.txt` — in `lotto_07_persone` ma già citato da una nota*.
**La seconda gamba della divergenza è il grezzo di un lotto futuro.**

⚠️ **La regola c'era già, e ha cinque giorni**: *la terza gamba di una questione si TRACCIA,
non si usa, se il suo grezzo appartiene a un lotto futuro* — lotto 1B, 19/08/2026, applicata
allora a T18 e T39. ⚠️ **Nessuna lettura di questo lotto l'aveva richiamata**: né la
scrittura, né il giudizio — che non può vederla, perché confronta la nota contro le fonti che
la nota dichiara — né la revisione, che la divergenza l'ha **prodotta**.

⚠️ **È il caso che mostra a che cosa serve la verifica di disgiunzione**: non a tenere in
ordine una tabella, ma a impedire che un lotto consumi il materiale di un altro. E il costo
di non averla eseguita sarebbe stato invisibile — una nota corretta, verde, e un lotto 07 che
più avanti trova il suo grezzo già mezzo canonizzato da qualcun altro.

⚠️ **Ciò che resta scritto è la gamba di 3F, e non è poco**: la dichiarazione del §5 — **mai
canonizzata prima** — il termine dell'08/08, e il fatto che **l'atto non fissa le date della
chiusura estiva**, quindi da sé non consente di dire se la promessa lo rispetti. **La
differenza di nove giorni vive in tabella, a T184, con l'obbligo esplicito per il lotto 07.**

### 8.4 ⚠️ B1 e B2 SONO LO STESSO ANTECEDENTE, E CAMBIANO LA STORIA DEL LOTTO

**Il lotto era stato scritto come una reazione in quindici giorni**: preavviso il 25/05,
ispezione il 09/06, e in mezzo la corsa dei preparativi. ⚠️ **B1 sposta l'inizio a dodici
giorni prima della PEC**, e in quell'antecedente il difetto strutturale che l'autorità
contesterà è già sul tavolo **col suo costo**. **La causa radice che l'azienda scriverà il
27/05 — «manutenzione strutturale rinviata per priorita di cassa» — nella riunione del 13/05
si vede accadere.**

### 8.5 ⚠️ IL TETTO DI PAROLE HA IMPOSTO UNA SCELTA, E LA SCELTA ERA GIUSTA

B2 era entrata come **gamba** dentro la nota del sopralluogo interno. Con la gamba, il corpo
saliva a **403 parole**: oltre il tetto di 350, **errore di QA**. ⚠️ **Il tetto non ha chiesto
di tagliare: ha chiesto di dividere**, e diviso il fatto si è rivelato una divergenza a sé,
con due fonti proprie e un `type: conflitto` che regge. **La nota nuova non è un ripiego del
budget: è ciò che il budget ha fatto vedere.**

---

## 9. ⚠️ IL QUADRO DEL TEMA 3, CHE QUESTO LOTTO CHIUDE

### 9.1 I sei lotti, e i tredici grezzi

| Lotto | Grezzi | Note di contenuto | Giri | Chiuso il |
|---|---|---|---|---|
| **3A** — riesame della direzione e cruscotto | 2 | **42** *(38 ciclo + 4 revisione)* | 3 | 22/08 |
| **3C** — certificazione e audit | 4 | **38** | 3 | 22/08 |
| **3B** — politica e formazione | 2 | **22** | 3 | 23/08 |
| **3D** — i reclami | 3 | **45** *(35 ciclo + 10 revisione)* | 2 + 2 dedicati | 24/08 |
| **3E** — la crisi e il ritiro | 1 | **37** *(30 ciclo + 7 revisione)* | 3 | 24/08 |
| **3F** — il controllo pubblico ATS | 1 | **36** *(32 dal ciclo, 1 dal giudizio, 3 dalla revisione)* | 3 | 24/08 |
| **totale** | **13** | | | |

⚠️ **Il tema è stato ripacchettato in apertura il 21/08 in cinque pacchetti, ed è finito in
sei**: `3E` si è spezzato il 24/08 per la soglia dura di E28, 62 fatti contati. **Il piano
scritto valeva cinque, la misura ne ha fatti sei.**

⚠️ **E l'ordine di esecuzione non è quello alfabetico**: `3C` è stato anticipato su `3B` al gate
del 22/08, perché il rapporto d'audit portava correzioni a cose già scritte nel vault.

### 9.2 La serie dei tassi del tema, coi domini e le riserve

| Lotto | Dominio | Tasso | Riserva |
|---|---|---|---|
| 3A | — | **non misurato** | ⚠️ esenzione dettata dal prompt del gate, **sbagliata nel merito** — da qui **E53** |
| 3C | `certificazione` | **38,7 %** su 31 | dominio troppo largo — da qui **E56** |
| 3B | `formazione` | **36,4 %** su 22 | dominio largo anche sotto E56 — da qui **E59** |
| 3D | `reclami` | **20,0 %** su 35 | primo punto collaudato, riserva **sciolta** al gate |
| 3E | `ritiro` | **0,0 %** su 30 | **degenere**: mono-fonte sulla fonte del dominio |
| 3F | `cip` | **8,3 %** su 36 | **tre casi residui, tutti enumerazioni** |

⚠️ **Cinque punti su sei portano una riserva, e quattro di esse hanno prodotto una regola.** Il
tema 3 è il tema in cui la misura dei due tassi ha imparato a misurare: E53, E56, E59 e le due
estensioni di E41 nascono tutte qui.

⚠️ **La serie del tema NON si somma e non si media**: i domini sono diversi, i denominatori
sono diversi, e due punti su sei portano una riserva strutturale. **È E46 applicato a una
serie invece che a un numero.**

### 9.3 Il debito che il tema lascia in tabella

| | |
|---|---|
| righe nate nei lotti del tema 3 | **72**, da **T109** a **T186** *(contate sulla colonna «aperta da» della tabella di tracciamento; il totale delle righe — 186 — lo dà `conta_tracciamento.py`, misurato alle 23:52)* |
| **aperte dichiarate** | **49** — divergenze con entrambe le gambe canonizzate, che aspettano un documento che il corpus non ha |
| **tracciate** | **17** — obblighi verso lotti futuri e debiti di strumento: **T168**, **T170**, **T181**, **T182**, **T186** fra gli altri |
| **chiuse** | **5** — e una **riconciliata** |
| chiusa da 3F | **T51**, che aspettava proprio la notifica ATS |

⚠️ **Il debito più pesante che il tema lascia non è una riga: è `R2`**, il lotto di
manutenzione che copre **due domini** — `reclami` e `ritiro` — e che si apre in sessione nuova
col perimetro rigenerato da entrambi, **senza `\bPRO-QA-11\b`** fra le espressioni salvo prova
nuova.

## 10. Che cosa torna al coordinatore

**Cinque voci, e nessuna è una richiesta di permesso**: tre sono candidati emendamento che il
gate decide, la quarta è un guasto già riparato che chiede soltanto di essere registrato come
regola invece che come toppa.

| | Voce | Stato | Che cosa chiede al gate |
|---|---|---|---|
| **1** | **il secondo delimitatore** — E10 protegge il delimitatore dei grezzi, non quello delle fonti dentro il pacchetto (§5) | ✅ **riparato in corsa**, col difetto piantato in `_collaudo` | se E10 debba dirsi di **ogni** delimitatore della catena, e non del solo grezzo |
| **2** | **la data derivata** — `RE_DERIVATO` esenta solo `genere == "numero"` (§6) | ⚠️ **dichiarato, non riparato**: tocca lo strato deterministico | se E50 valga per una data come per un numero, e con essa l'esenzione |
| **3** | **il superlativo sull'elenco** — E57 classifica, non obbliga a contare (§7.5) | ⚠️ **candidato**, tre occorrenze in un lotto solo | se un'affermazione universale col soggetto-elenco debba portare il conto, come un derivato porta la marca |
| **5** | ⛔ **il perimetro dell'affermazione** — E47, E3/E43 ed E57 governano tre specie, e la classe che le contiene non ha regola (§7.7) | ⛔ **candidato, ed è il pattern che E26 ha imposto di nominare**: sei occorrenze al terzo giro | se valga, scritta una volta sola, *un'affermazione vale nel perimetro delle fonti che la nota cita, e per uscirne serve un artefatto o un rimando* |
| **4** | **l'unità della misura dei due tassi** — enumerare vale quanto affermare (§2.2) | ⚠️ **candidato**, tre casi residui su tre | se la misura debba distinguere l'affermazione dall'enumerazione, o se il caso residuo dichiarato basti |

⚠️ **E la voce 5 contiene la 3.** Il superlativo sull'elenco è **una** delle sei specie che il
terzo giro ha prodotto; le altre cinque — primato sull'archivio, assenza sull'archivio, regola
generale importata, nesso causale, estensione su un elenco — stanno tutte sotto la stessa
frase. ⚠️ **Il gate può accogliere la 3 e lasciare aperta la 5, ma non il contrario**: la 5,
se passa, rende la 3 un esempio invece che una regola.

⚠️ **Le voci 3 e 4 sono la stessa malattia vista da due strati.** La 3 la vede nella
**scrittura** — chi scrive dice «l'unico» senza contare l'elenco che ha sotto gli occhi. La 4
la vede nella **misura** — lo strumento conta come «parlare del dominio» un elenco che il
dominio si limita a nominare. **Sotto c'è un fatto solo: un elenco citato non è un'affermazione,
e né la regola né lo strumento oggi lo distinguono.**

⚠️ **E la voce 2 è l'unica che costa qualcosa a lasciarla aperta**, perché ogni lotto che
canonizza una mail con «domani» paga lo stesso prezzo: o la nota perde la data, o chi scrive
impara ad aggirare il controllo scrivendola in lettere. **La seconda è peggiore della prima**,
ed è la ragione per cui questo lotto ha scelto la prima e l'ha scritta qui.

## 11. La chiusura, e le misure con la loro ora (E44)

⚠️ **Il lotto si è lavorato il 24/08/2026 e si è chiuso il mattino del 25.** Il marcatore
dell'elenco porta la data del lavoro — `# CHIUSO il 24/08/2026` — **le misure portano la data e
l'ora in cui sono state prese**, che è l'unica cosa che E44 chiede.

| Misura | Valore | Strumento | Quando |
|---|---|---|---|
| note **nate** nel lotto | **36**, tutte di contenuto | `conta_perimetro_lotto.py` | 25/08, **09:21** |
| note **toccate** (E32) | **11** | `conta_perimetro_lotto.py` | 25/08, **09:21** |
| **note controllate nel perimetro** | **47** | `conta_perimetro_lotto.py` | 25/08, **09:21** |
| esito della suite, perimetro lotto | **0 ERRORI, 44 avvisi** | `qa_all.py` | 25/08, **09:20** |
| tasso di **riapertura** | **non applicabile** — zero note riaperte | `misura_due_tassi.py` | 25/08, **09:16** |
| tasso di **difetto di produzione** | **8,3 %** — 3 su 36, dominio `cip` | `misura_due_tassi.py` | 25/08, **09:16** |
| tabella di tracciamento | **186 righe**, da T1 a T186, integra | `conta_tracciamento.py` | 25/08, **09:20** |
| matrice dei lotti | **completa e disgiunta**: 160 grezzi, 33 elenchi | `verifica_matrice_lotti.py` | 25/08, **09:19** |
| mappatura file × fatto | **610 righe**, di cui **35** del lotto 3f | `genera_matrice_file_fatto.py` | 25/08, **09:19** |
| emendamenti | **64 marcatori inline**, registro e manuale concordano | `verifica_emendamenti.py` | 25/08, **09:20** |
| note nel vault | **507**, di cui **468 di contenuto** | `conta_stato.py` | 25/08, **09:21** |
| grezzi citati su 160 | **56** · restanti **104** | `conta_stato.py` | 25/08, **09:21** |

### 11.1 ⚠️ UNO STRUMENTO CHE DAVA ZERO, E DUE LOTTI CHE NON SE NE ERANO ACCORTI

`conta_perimetro_lotto.py` divide il perimetro in tre sezioni leggendo due stringhe nei
commenti dell'elenco delle note: `note toccate in corso di lotto` e **`note NATE in questo
lotto`**. ⛔ **L'elenco di 3E scriveva «note NATE nel lotto», e 3F ne aveva copiato
l'intestazione**: la seconda stringa non corrispondeva, il parser non cambiava mai sezione, e
**tutto finiva in «toccate»**.

⚠️ **Il risultato era «note nate: 0 — nessuna» su un lotto che ne aveva scritte trentasei.**
Il rapporto di 3E non se n'era accorto perché aveva composto i suoi numeri a mano da altre
fonti — che è esattamente ciò che l'intestazione dello strumento vieta: *si incolla VERBATIM,
i numeri del perimetro non si ricompongono a mano*.

⚠️ **Riparato allineando i due elenchi alla stringa che lo strumento cerca** — 3F e, come
pregresso, 3E, che ora si ricontano correttamente: **37 nate, 12 toccate, 49 controllate**.
**Gli altri undici elenchi portavano già la stringa giusta**: la deriva nasce con 3E e muore
qui.

⚠️ **Non è stato toccato lo strumento**, e la ragione è la disciplina del gate 1A: si
aggiungono agganci, non se ne allentano. **Cambiare il parser perché accetti due forme sarebbe
stato allargare il controllo; allineare i dati alla forma dichiarata è rispettarlo.**

### 11.2 Che cosa il lotto NON lascia

| | |
|---|---|
| emendamenti nuovi | **nessuno.** Il registro resta a **64** |
| grezzi spostati | **nessuno** |
| righe T chiuse | **una**, `T51`, che aspettava proprio la notifica ATS |
| debito verso `R2` | invariato: due domini rigenerati, **senza** `PRO-QA-11` salvo prova nuova |
| debito verso il **lotto 07** | ⚠️ **nuovo**: `T184`, con l'obbligo esplicito di aprire la divergenza alla canonizzazione di `comunicazione_chiusura_estiva_2026.txt` |
