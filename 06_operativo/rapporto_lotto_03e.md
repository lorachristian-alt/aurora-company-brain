# Rapporto del lotto 3E — la crisi e il ritiro dal mercato

> **Che cos'è** · Il consuntivo del quinto pacchetto del tema 3, eseguito il 24/08/2026 secondo
> il ciclo di `prompt_s4_lotti.txt` §3, dalla PARTE 5 di `prompt\prompt_gate_3d_lotto_3e.txt`.
> **È il primo lotto che gira con E62 ed E63 in vigore e con le quattro estensioni del gate 3D**
> — lo slug come terza intestazione (E30), la ricerca fra le note (E39), la metà B a lotto
> chiuso (E59), la rilettura all'indietro quando il perimetro si muove (E61).
> ⚠️ **E il lotto si è spezzato in due prima di scrivere una riga**: il tema 3 non chiude più
> con 3E, chiude con **3F**.
> **Misure** · tutte da script, ognuna con la sua ora (E44).

---

## 1. L'apertura

### 1.1 ⛔ IL LOTTO SI SPEZZA PER LA SOGLIA DI E28, E IL TEMA NON CHIUDE PIÙ CON LUI

La conta dei fatti in apertura (E21) dà **62 fatti** sui due grezzi:

| Grezzo | Che cos'è | Fatti contati |
|---|---|---|
| `procedura_ritiro_prodotto_CRISI_GDO.txt` | la **`PRO-QA-14` rev. 3**: 11 paragrafi numerati *(contati da script)*, due tabelle, due bozze, la matrice delle revisioni, più una **annotazione manoscritta** del 14/05 e un **blocco sul perimetro** delle 18:05 dello stesso giorno | **38** |
| `notifica_ATS_ispezione_programmata_igiene.txt` | il **preavviso di ispezione ATS** del 25/05, con i 12 capitoli del Reg. 852/2004, i 14 documenti richiesti, e la catena di **due mail interne** che ne fa un piano di lavoro | **24** |

**La proiezione supera le quaranta note che impongono lo spezzamento COMUNQUE** (E28). Il lotto
si dichiara e si spezza **prima di scrivere una riga**:

| | |
|---|---|
| **`lotto_03e_crisi_ritiro`** | la procedura di ritiro e il caso di maggio — **questo lotto** |
| **`lotto_03f_controllo_pubblico_ats`** | il preavviso di ispezione e i quindici giorni che lo precedono. ⚠️ **Chiude il tema 3** |

⚠️ **La cucitura è documentale, non tematica** (E31): una **procedura interna dell'azienda** e un
**atto di un'autorità pubblica** sono due soggetti, e le **grandezze condivise fra i due grezzi
erano zero** *(misurate da `grandezze_condivise.py`)*.

⚠️ **L'elenco vecchio si chiamava `lotto_03e_crisi_ispezioni` ed è stato RINOMINATO**, non
riusato: un nome che dice «ispezioni» su un elenco che le ispezioni non contiene più afferma
ciò che lo spezzamento ha smentito. **È E30 esteso applicato a un elenco invece che a una nota**,
ed è la prima volta che quella regola esce dal vault.

⚠️ **Il prompt del gate diceva che 3E era l'ultimo pacchetto del tema.** È stata la misura a
cambiarlo, non una scelta di comodo — ed è la disciplina di E53: mai sulla parola di chi
coordina.

### 1.2 ⚠️ E37 SCATTA ANCHE QUI, MA NON NASCE UN TERZO LOTTO DI MANUTENZIONE

`candidate_r1.py --dominio ritiro` riapre **35 note**, contro una proiezione di 30-35 nuove: la
soglia di E37 è raggiunta e le riaperte **escono dal lotto di canonizzazione**.

⚠️ **Vanno a R2, e la decisione è MISURATA**: **14 delle 35** stanno già nel perimetro di R2
*(misurato il 24/08/2026)*, e due elenchi di manutenzione che si contendono le stesse quattordici
note sarebbero **due padroni dello stesso lavoro**. `PRO-QA-08` e `PRO-QA-14` sono le due metà
dello stesso ciclo. **R2 si apre con due domini rigenerati** — `reclami` e `ritiro` — e resta in
coda al tema, cioè dopo 3F.

### 1.3 E53 — il dominio si verifica, e c'è

`verifica_dominio.py --lotto lotto_03e_crisi_ritiro`, misura delle **13:37:10 del 24/08/2026**:
**8 fonti prescrittive citate per sigla** nei grezzi, di cui **6 citabili**; 22 fonti con i soli
riscontri deboli, che non contano.

### 1.4 E56 — la coppia, e ciò che è stato lasciato fuori

**Fonte del dominio: una sola, `PRO-QA-14`.** Governa il ciclo della crisi per intero:
definizioni (§3), classificazione della gravità (§4), team e reperibilità (§5), le sei fasi coi
loro tempi (§6 e §7), i modelli di comunicazione (§8), la modulistica e il dossier (§9), il mock
recall (§10).

⚠️ **La notifica ATS resta FUORI dalle fonti del dominio, ed è una decisione**: è l'atto di
un'autorità che prescrive **per un evento** — l'ispezione del 09/06 — non una regola permanente
dell'azienda, e non è nell'elenco delle fonti prescrittive. Le sue espressioni — `ispezione`,
`controllo ufficiale`, `ULSS`, `SIAN` — sarebbero **espressioni senza una fonte del dominio che
le governi**, cioè la metà scoperta che E56 vieta.

⚠️ **Ciò che è stato lasciato fuori delle espressioni, e il motivo:**

| Fuori | Perché |
|---|---|
| `\britir` e `\brichiam` **da soli** | «ritiro» è anche il ritiro del **reperto**, che `PRO-QA-08` §7.3 governa, e «richiamo» è anche il **richiamo annuale** della formazione. Sono le due parole del titolo del documento, ed è la trappola di `\bformazion` in 3B: **la parola non è la cosa** |
| `classe 1|2|3` | la scala delle classi ce l'ha anche `PRO-QA-08` §5, ed è precisamente la materia di T159 |
| `causa radice`, `\bMOD-QA-31\b`, `\breclam` | sono del dominio `reclami`. `PRO-QA-14` li **usa**, ma a prescriverli è l'altra procedura |
| `\bCCP\b`, `metal detector` | li governa il manuale HACCP |

### 1.5 ⚠️ E59 — LA METÀ B, ESEGUITA A LOTTO CHIUSO, RESPINGE UN'ESPRESSIONE

**In apertura** *(misura delle 13:39:22)*: **dieci espressioni**, prova A superata da tutte e
dieci; **prova B dichiarata NON APPLICABILE**, perché la fonte del dominio la portava il lotto
stesso. **Due espressioni mute** — `team di crisi` e `dossier di crisi` — dichiarate tali invece
che ignorate.

**A lotto chiuso** *(misura delle 14:24:19)*, come l'estensione del gate 3D adesso impone:

| | |
|---|---|
| espressioni provate | **10** |
| respinte dalla prova B | **1** — `\bPRO-QA-11\b`, quota fuori **0,57** |
| le due mute in apertura | **`team di crisi` 6 note, `dossier di crisi` 3**: a lotto chiuso riconoscono |

⚠️ **La ragione della respinta è di merito**: `PRO-QA-11` è la sigla che **`PRO-QA-08`** usa, e
un'espressione su di essa pesca le note del dominio `reclami`. Delle 7 note che riconosce,
**quattro citano solo altre prescrittive**.

⚠️ **E NON è una stretta a numero visto** (§4.43), e c'è la prova: **il tasso non è cambiato** —
era 0,0 % prima della stretta ed è 0,0 % dopo. **A decidere è stata la prova, non il numero.**

⚠️ **È la prima volta che la metà B respinge qualcosa**, e senza l'estensione scritta stamattina
quella respinta non sarebbe mai avvenuta: in apertura la prova non era applicabile, e il lotto
si sarebbe chiuso con un'espressione generica dentro la dichiarazione.

### 1.6 E60 — l'artefatto d'apertura, e i confronti fatti

`grandezze_condivise.py --lotto lotto_03e_crisi_ritiro`, misura delle **13:43:58**:

| | |
|---|---|
| grandezze condivise **fra i grezzi** | **0** — ⚠️ il lotto ha **un grezzo solo** dopo lo spezzamento: **nessuna riconciliazione orizzontale interna**, e si dichiara |
| grandezze del lotto **già nel vault** | **33** su 57 |
| **entità** del vault nominate dal grezzo | **14** |

**I confronti col vault, uno per uno, come E60 impone:**

| Grandezza | Contro quali note | Esito |
|---|---|---|
| **`99,6`** | `fatto-mock-recall-marzo-2026`, `questione-mock-recall-due-ore-o-quattro` | ⛔ **divergenza scritta**: due esercitazioni, e la procedura ne dichiara ultima quella che il riesame non conosce |
| `8.400` · `5.100` · `31.500` | `fatto-blocco-cautelativo-lotti`, `kpi-mass-balance-l26130` | ✅ **concordano**, e il blocco aggiunge la ripartizione per finestra oraria che il vault non aveva |
| `18:45` · `15:05` | `fatto-fermo-pkm-450-l26130`, `fatto-riparazione-guarnizione-non-originale` | ⚠️ **sembravano divergere, e non divergono**: v. §4.3 |
| `14:18` · `14:47` | `fatto-deviazione-ccp2-l26130` | ✅ concordano: è la stessa deviazione del `PT-104` |
| `MOD-QA-31` | `questione-nc-interne-registrate-su-mod-qa-31` | ✅ il modulo è condiviso fra le due procedure, e la nota lo dichiara senza attribuirlo |
| `AF-CR-0212` | `fatto-referenze-nello-scope-del-certificato` | ✅ il lotto sfida del mock recall è una referenza reale |
| `L26132` | `kpi-produzione-0450-linea1-maggio` | ✅ l'estensione del blocco nomina lotti che il vault conosce |
| `28/11/2025` | `fatto-datalogger-dl-001-in-taratura` | ⚠️ **coincidenza di data, oggetti diversi**: rumore, dichiarato |

**Otto confronti, due divergenze scrivibili.**

---

## 2. I due tassi (E41), col nome del dominio (E46)

| | Punto **DICHIARATO** |
|---|---|
| **Tasso di riapertura** *(debito)* | ⚠️ **non misurato in 3E**: le 35 riaperte sono andate a **R2** con lo spezzamento, e il tasso è suo |
| **Tasso di difetto di produzione** *(metodo)* | **0,0 %** — 0 su **30**, dominio `ritiro` *(misura delle 14:25:38)* |

⚠️ **Lo zero va letto con la sua riserva, e la riserva è strutturale**: il lotto ha **un grezzo
solo**, e quel grezzo **è la fonte del dominio**. Ogni nota nata cita `PRO-QA-14` per
costruzione, quindi **nessuna può risultare scoperta**. ⚠️ **Il numero è vero e il suo potere
discriminante è nullo**: un lotto mono-fonte non può produrre un tasso diverso da zero sul
dominio che quella fonte governa.

**La serie, con questo punto:**

| Lotto | Dominio | Difetto di produzione |
|---|---|---|
| R1 | perimetro CCP e tarature | **57,7 %** |
| 2A | `cip` | **3,3 %** |
| 2B | `acqua` | **0,0 %** su 27 |
| 2B-bis | `allergeni` | **9,1 %** su 33 |
| 3A | — | ⚠️ **NON MISURATO** |
| 3C | `certificazione` | **38,7 %** su 31 — con riserva |
| 3B | `formazione` | **36,4 %** su 22 — con riserva |
| 3D | `reclami` | **20,0 %** su 35 — primo punto collaudato |
| **3E** | **`ritiro`** | **0,0 %** su 30 — ⚠️ **con la riserva del lotto mono-fonte** |

⚠️ **La riserva del punto di 3D, invece, È STATA SCIOLTA**: la metà B di E59, eseguita a lotto
chiuso su `reclami` al gate, passa **nove espressioni su nove**.

---

---

## 3. Che cosa il lotto ha trovato

### 3.1 ⛔ DUE RICOSTRUZIONI DELLO STESSO EVENTO, DELLO STESSO GIORNO, CHE NON CONCORDANO SU NIENTE

Il **blocco del perimetro** è del **14/05/2026 alle 18:05**; il **mass balance** è «compilato in
emergenza il **14/05/2026** da S. Pozzato su richiesta di E. Marchetti». **Stessa funzione,
stesso giorno, tre numeri che non tornano** — e il vault aveva **entrambe le gambe canonizzate
da agosto senza averle mai messe una di fronte all'altra**.

| Grandezza | Blocco del perimetro | Mass balance | Scarto |
|---|---|---|---|
| giacenza bloccata di `L26130-L1-T2` | **3.290** per la finestra 18:45-22:00 | **1.180** per **tutto** il turno | **2.110** *(calcolato)*, e **impossibile in un verso solo**: la finestra è un sottoinsieme del turno |
| la quota di **5.100** | attribuita a `L26131-L1-T2` | è lo **spedito di `L26130-L1-T2`** a Tosano, col suo DDT | la lettura alternativa che il vault aveva ipotizzato — «il totale dei tre sotto-lotti» — è **smentita**: quello vale **11.780** *(calcolato)* |
| prodotto coinvolto | **~ 8.400** su tre sotto-lotti | **9.360** comunicati a Tosano il **14/05 alle 09:15** | **il perimetro comunicato al cliente la mattina è più largo di quello definito la sera** |

⚠️ **È il numero che finisce nella relazione di 48 ore che quel cliente ha chiesto.**

### 3.2 ⛔ UN CLIENTE IN RICHIAMO MENTRE LA CLASSIFICAZIONE DICE RITIRO

Il mass balance marca la consegna a Rossetto Trade **`RICHIAMATO`** e registra un «**richiamo
autorizzato**» il **15/05 alle 08:05**. L'annotazione del giorno prima classifica «**Classe 2 per
ora (ritiro, non richiamo)**», e `PRO-QA-14` §4 assegna il richiamo alla **classe 1**, con
notifica all'Autorità entro 24 ore.

⚠️ **Le due letture non sono equivalenti**: o è uso corrente della parola in un foglio di lavoro
— nel documento con cui la rintracciabilità si dimostra a un cliente e a un ente — o è un
richiamo autorizzato **fuori dalla classe dichiarata**, e allora mancano l'avviso al consumatore
e la notifica. **Nessuna fonte le distingue.** **T172**.

### 3.3 ⚠️ DUE ORE CHE SEMBRAVANO DIVERGERE, E NON DIVERGONO

Il blocco fissa il perimetro alle **18:45** in una riga e alle **15:05** in un'altra, e il lotto
ci aveva scritto sopra una divergenza. ⛔ **Non è una divergenza**: il `MOD-PR-04` n. 2026/087 —
**già canonizzato, e non fra le fonti di quella nota** — porta «Ora chiamata: **15:05**» e «Fermo
produzione: **DALLE 15:05 ALLE 18:45**». Le due ore sono **l'inizio e la fine dello stesso
fermo**, e in mezzo la linea non confezionava.

⚠️ **La nota è stata riscritta e RINOMINATA** — `fatto-due-orari-per-il-confine-del-perimetro`
→ `fatto-il-perimetro-si-apre-al-riavvio-delle-18-45` — perché lo slug affermava ciò che la
correzione ha smentito: **E30 esteso, applicato lo stesso giorno in cui è stato scritto.**

⚠️ **E l'errore si era propagato a due altre note**, che lo ripetevano come acquisito. **L'ha
preso il revisore, non io**, e la lezione è E39 esteso: la ricerca va fatta **fra** le note.

### 3.4 Le altre divergenze

- **`PRO-QA-14` non recepisce l'obbligo di notifica all'ente** che il certificato BRCGS impone per richiami, ritiri, allerte e provvedimenti dell'Autorità: la fase 3 elenca **tre destinatari** e l'ente non c'è. **Non manca la registrazione: manca la prescrizione.** **T174**.
- **Il turno 3 ha 1.480 confezioni bloccate e non esiste nel mass balance**: gamba nuova e più pesante di F6 del lotto 3D. **T173**.
- **La revisione 3 del 10/09/2025 riporta fatti del 07/11 e del 28/11/2025**, e la matrice delle revisioni non registra nulla dopo la rev. 3.
- **Due esercitazioni di richiamo**, e la procedura dichiara ultima quella che il verbale di riesame non conosce — con lo stesso **99,6 %** in entrambe.
- **Quattro sigle per due procedure**: `PRO-QA-11`/`PRO-QA-14` per il ritiro, `PRO-QA-08`/`PRO-QA-13` per i reclami. **T163 aggiornata**, e la terza sigla è nuova.
- **Il prefisso 049 dello studio della consulente** contro la Verona che due fonti le attribuiscono, in una tabella che al legale veronese dà il 045. **Forza media, dichiarata.** **T175**.

### 3.5 ✅ T159 SI CHIUDE, E LA RISPOSTA È CHE LE SCALE SONO DUE

L'obbligo esplicito chiedeva tre cose. `PRO-QA-14` §4 porta **una scala propria** — ma **della
gravità dell'evento di crisi**, non del reclamo — con **tre** classi contro le **quattro** di
`PRO-QA-08` §5, e col discrimine del corpo estraneo **«tagliente»** contro **«pericoloso»**.

⚠️ **E la ragione per cui nessuno se n'era accorto è che sul caso concreto le due scale danno lo
STESSO NUMERO per criteri diversi**: non pericoloso e non tagliente portano entrambi alla classe
2. **La coincidenza del numero nascondeva la differenza del criterio.**

⚠️ **Quale delle due governi resta aperto**, ed è ora la forma giusta della questione:
`PRO-QA-08` §6.1 manda al proprio §5, la scheda applica il §4 dell'altra, e **nessuna dichiara di
cedere il passo.**

---

## 4. Il ciclo di giudizio

### 4.1 I tre giri, e i numeri

| Giro | Note giudicate | Rilievi accolti | Di che specie |
|---|---|---|---|
| **primo** | 39 (4 fette) | **18** | affermazioni su documenti fuori dalle proprie `fonti`, giudizi di conformità, un'attribuzione |
| **secondo** | 39 (4 fette) | **7** | ⚠️ **due erano `title` e `summary` che le correzioni del primo giro avevano lasciato indietro** |
| **terzo** | 40 (4 fette) | **13**, e **6 respinte motivate** | la frase di raccordo verso un'altra nota, e un conteggio sbagliato |

⚠️ **Il terzo giro ha trovato più del secondo, e non è un peggioramento**: gli era stato detto
che cosa cercare — le due classi che i primi due avevano isolato. È la stessa cosa successa in
3C, e va letta così.

### 4.2 ⚠️ IL PATTERN CHE IL TERZO GIRO NON HA ESAURITO, NOMINATO COME E26 IMPONE

Il terzo giro produce ancora rilievi, quindi **il lotto si chiude solo dopo aver nominato la
classe che li rigenera**. È una, e i giudici l'hanno descritta da tre fette diverse:

> **LA FRASE DI RACCORDO VERSO UN'ALTRA NOTA, CHE PER REGGERE DEVE ASSERIRE QUALCOSA DI
> QUELL'ALTRA NOTA.**

Non è la glossa che rimanda — «v. `[[questione-x]]`» sta in piedi da sola — è quella che
**descrive** ciò che l'altra nota contiene, o ciò che le sue fonti dicono: «è la stessa tensione
che `[[…]]` registra dall'altro lato», «come la scala dei reclami di `[[…]]`», «la divergenza con
l'obiettivo di due ore del verbale di riesame», «le due letture concordano».

⚠️ **Nasce dal buon proposito di tessere il grafo**, ed è per questo che sopravvive ai giri: chi
scrive sta collegando, non affermando — **ma il lettore la legge come un'affermazione, e il
giudice pure.** È E36 applicato al wikilink invece che alla citazione.

⚠️ **La cura non è togliere i rimandi**: è che **il rimando nomini la nota e non il suo
contenuto** — «la questione ha le sue fonti e sta in `[[…]]`» invece di «`[[…]]` dice che…».

### 4.3 ⚠️ E61 IN FLAGRANZA, TRE VOLTE, E SEMPRE SU CORREZIONI MIE

| Dove | Che cosa è successo |
|---|---|
| `doc-mass-balance-nella-crisi` | la correzione del **primo** giro ha scritto «la divergenza con l'obiettivo di due ore **del verbale di riesame**» — un documento che quella nota non ha fra le fonti. **Presa al terzo giro** |
| `area-direzione` | la correzione del primo giro ha scritto «il riesame ne è l'appuntamento ricorrente», e la trascrizione non nomina il riesame. **Presa al secondo** |
| `doc-riesame-post-crisi` | la correzione del **secondo** giro ha scritto «la procedura ne offre due e lascia la scelta», e la fonte scrive solo «metodo 5 perché / Ishikawa». **Presa al terzo** |

⚠️ **Tre correzioni su tre giri hanno introdotto il difetto che stavano chiudendo**, ed è
esattamente ciò che E61 descrive. **La rete ha funzionato**: ogni volta il giro dopo l'ha presa.

### 4.4 Le sei segnalazioni respinte, e perché

Il terzo giro ha segnalato **sei hub** — `area-qualita`, `area-commerciale`, `area-direzione`,
`area-logistica`, `area-manutenzione`, `area-amministrazione` — perché le loro glosse descrivono
il contenuto di documenti che gli hub non hanno fra le proprie `fonti`.

⚠️ **Respinte nella classificazione**: metodo_03 §7.1 **clausola 4** dice che l'annotazione di
mezza riga accanto a un wikilink **si verifica nello spoke**, e se lo spoke è verificato
l'annotazione lo è. **Il giudice non conosce il grafo**, ed è il rumore documentato del suo
ruolo.

⚠️ **Ma sotto c'era un difetto vero, e la stessa clausola lo prevede** — «se l'annotazione dice
qualcosa che lo spoke non dice, è un ERRORE, sull'hub». **Tre glosse dicevano ciò che le
correzioni avevano tolto dagli spoke**: i «tre destini», le «due ore che non coincidono», i
«quattro in reperibilità». **È E39 esteso ed E42 applicati alle glosse degli hub**, e senza la
segnalazione respinta non le avrei guardate.

---

## 5. La revisione col canone: 2 A, 7 B, 3 C

Subagente a contesto pulito, col canone integrale e la tabella alias (E45). Ha letto il canone,
il grezzo con l'estrazione di cantiere, le 30 note nate, le 4 toccate e le note del vault
collegate.

### 5.1 ⛔ LE DUE A, E LA SECONDA SI ERA PROPAGATA

| | Rilievo | Esito |
|---|---|---|
| **A1** | `doc-team-di-crisi` diceva **quattro** ruoli in reperibilità 24/7, e i contrassegnati `(*)` sono **tre** — ⚠️ **con la tabella della nota stessa che ne marca tre**: la nota si smentiva da sola, e il numero sbagliato stava nel titolo e nel summary | corretto in quattro punti |
| **A2** | `fatto-due-orari-per-il-confine-del-perimetro` costruiva una divergenza su due ore che sono i due capi dello stesso fermo — ⚠️ **e la parola «riavvio», nella frase stessa che la nota citava, presuppone un fermo** | nota **riscritta e rinominata**, e **due note che ripetevano l'errore corrette** |

⚠️ **A2 è il rilievo più istruttivo del lotto**: l'errore non era in una fonte mal letta, era in
una **spiegazione scelta male fra due possibili** — guarnizione contro valvola invece di inizio
contro fine — e la nota era pure onestamente cauta. **La cautela non salva da una lettura
sbagliata**, e a prenderla è stato l'unico strato che aveva il documento di un'altra area.

### 5.2 Le sette B, e come sono state trattate

| | Divergenza | Trattamento |
|---|---|---|
| **B1-B3** | il **blocco del perimetro contro il mass balance**: giacenza, quota spedita, prodotto comunicato al cliente | ✍️ **questione scritta** — **T171**, canone **G1-G3** |
| **B4** | un cliente in **`RICHIAMATO`** con la classificazione a **classe 2** | ✍️ **questione scritta** — **T172**, canone **G4** |
| **B5** | il **turno 3** bloccato in un documento e assente nell'altro | ✍️ **fatto scritto** — **T173**, canone **G5** |
| **B6** | `PRO-QA-14` non recepisce l'obbligo di **notifica all'ente** | ✍️ **questione scritta** — **T174**, canone **G6** |
| **B7** | il **prefisso 049** dello studio contro la Verona di due fonti | ✍️ **questione scritta**, forza **media** — **T175**, canone **G7** |

⚠️ **Cinque delle sette nascono dallo stesso accostamento**, e nessuna dal ciclo: **le ha trovate
la revisione col canone**, che è lo strato con il canone davanti. È il terzo lotto di fila in
cui E2 orizzontale la fa il revisore.

### 5.3 Le tre C, e perché non ci si torna sopra

| | Perché non è un problema |
|---|---|
| il lotto sfida `L25311-**L3**-T1` col suffisso di Linea 3 | è la trappola già a canone: `AF-CR-0212` è croissanteria ma il piano la assegna alla Linea 3. ⚠️ **Ed è anzi una prova di solidità**: `311` è il **7 novembre 2025** *(calcolato)*, la data che il §10.3 dichiara — **la regola del codice di lotto regge su un altro anno, un'altra referenza e un'altra linea** |
| `PRO-QA-08` = rintracciabilità e `PRO-QA-13` = reclami | è la trappola già a canone (F1, F2 del lotto 3D). Il lotto l'ha trattata bene: **non ha unito le sigle** |
| il perimetro di 8.400 che non torna con la somma dei due lotti | lo dice già `fatto-blocco-cautelativo-lotti` dal 19/08. ⚠️ **Restano nuovi i tre scarti puntuali**, che quella nota non poteva avere |

### 5.4 E63 — la copertura verificata al contrario

**Undici paragrafi numerati** *(contati da script)*, più testata, annotazione e blocco del
perimetro. **Uno solo senza nota: il §8.1**, la bozza di comunicazione al cliente.

⚠️ **Il revisore lo dichiara accettabile — è un modulo — e poi mostra che non lo è del tutto**:
il §8.1 chiede al cliente **tre cose** *(contate)*, e la seconda — «**quantificare le giacenze
presso CE.DI. e punti vendita**» — è **l'atto da cui dipende il perimetro reale del ritiro**.
**Nota scritta**: `doc-bozza-comunicazione-al-cliente`.

⚠️ **E il rilievo più serio non era il §8.1 ma il §7**, che il revisore trova senza padrona: è
l'unico posto in cui le tempistiche sono dichiarate **«(vincolanti)»**, e porta una riga —
«**Convocazione team di crisi: immediata per Classe 1-2**» — **che nessun'altra parte del
documento contiene**. **Nota scritta**: `doc-tempistiche-vincolanti-della-crisi`.

⚠️ **È il terzo lotto di fila in cui E63 trova qualcosa**, e la prima volta che a trovarlo è la
regola invece del caso.

### 5.5 Gli obblighi del canone verso questo lotto: due, entrambi eseguiti

**O1 — F8 / T159**: eseguito, e **T159 si chiude**. ⚠️ Il revisore segnala che l'argomento era
incompleto sul punto decisivo — `PRO-QA-14` §4 **rivendica per sé lo stesso modulo `MOD-QA-31`**,
quindi la scheda non usa il modulo di un'altra procedura: fa ciò che il §4 le prescrive, mentre
`PRO-QA-08` §6.1 le prescrive il contrario. **Recepito nella nota.**

**O2 — F1 / T163**: eseguito, metà chiusa, terza sigla aperta.

⚠️ **E un obbligo che questo lotto non aveva, ma la cui gamba scrivibile aveva in mano**: **D8**
del lotto 3C metteva sul lotto 5 la gamba Tosano dell'obbligo di comunicazione. **La gamba del
certificato era canonizzata e nessuno l'aveva usata**: è **B6**.

---

## 6. Il giudizio dedicato di E58, e il gruppo post-revisione

Le **sette note nate dalla revisione** non avevano mai visto un giudice. Hanno ricevuto un
**giudizio dedicato** (E58), non un giro nuovo sul lotto.

| Giro dedicato | Note | Rilievi accolti |
|---|---|---|
| **primo** | 7 (2 fette) | **5** |

⚠️ **Cinque su sette al primo colpo, e sono errori miei, non del revisore.** Il più grave è
un'affermazione **invertita**: avevo scritto che il termine dell'ente — tre giorni lavorativi —
fosse «il più stretto dei tre» contro le ventiquattro ore dell'Autorità. **È il più largo**, e la
questione cambia forma: non è un problema di tempi, **è un problema di destinatario**.

⚠️ **E un secondo errore è entrato anche nel CANONE**: la riga B ancorava alla clausola 1.1.10
l'obbligo sugli eventi gravi, mentre il punto 3 del certificato porta **due** obblighi e la
clausola è citata a proposito **del primo**. **Corretto nello stesso turno nella nota e nel
canone**, perché una riga B sbagliata si propaga a tutti i lotti futuri (E49).

⚠️ **Il gruppo post-revisione ha una densità di difetto molto più alta del ciclo** — cinque
rilievi su sette note contro i tredici su quaranta del terzo giro — **e la ragione è la stessa di
3A e 3D**: sono note scritte in fretta, per chiudere un rilievo, senza il giro di rilettura che
il ciclo prevede.

### 6.1 ⚠️ IL GRUPPO POST-REVISIONE, DICHIARATO COME E52 IMPONE

| | |
|---|---|
| note nate dal **ciclo** | **30** — è il denominatore del tasso dichiarato, misurato alle **14:25:38** |
| note nate dalla **revisione col canone** | **7** — fuori dalla soglia di spezzamento (E52) |
| **totale nate nel lotto** | **37** |
| note **toccate** (E32) | ~~**4**, più i sei hub d'area~~ → **12** *(v. errata sotto)* |

> ⛔ **ERRATA del 31/08/2026, scritta al gate del lotto 3F.**
>
> **I numeri del perimetro di questo rapporto erano stati composti A MANO**, e sono
> sbagliati. Quelli veri, incollati da `conta_perimetro_lotto.py` dopo la riparazione:
>
> | Voce | Diceva | È |
> |---|---|---|
> | note **nate** nel lotto | 37 | **37** — confermato |
> | note **toccate** (E32) | **4**, più i sei hub d'area | **12** |
> | **note controllate nel perimetro** | **58** | **49** |
>
> ⚠️ **La causa non è una svista di conteggio: è uno strumento che dava un numero
> impossibile e che nessuno ha dichiarato guasto.** `conta_perimetro_lotto.py` divide il
> perimetro leggendo due stringhe nei commenti dell'elenco delle note, e la seconda è
> `note NATE in questo lotto`; l'elenco di 3E scriveva «note NATE nel lotto», quindi il
> parser non cambiava mai sezione e **stampava «note nate: 0 — nessuna» su un lotto che
> ne aveva scritte trentasette**.
>
> ⚠️ **La prassi dello strumento dice «si incolla VERBATIM, i numeri del perimetro non si
> ricompongono a mano»**, ed è scritta nell'intestazione del suo stesso output. Comporre a
> mano non è solo meno affidabile: **ha nascosto il guasto dello strumento che avrebbe
> dovuto sostituire**, e il guasto è arrivato fino a 3F, che ne aveva copiato
> l'intestazione. **Un controllo che dà un numero impossibile si dichiara, non si aggira.**
>
> ⚠️ **Riparati i DATI, non lo strumento**: i due elenchi si sono allineati alla stringa
> che lo strumento dichiara — gli altri undici la portavano già. Allargare il parser a
> due forme sarebbe stato **allentare** un controllo.


⚠️ **Il tasso non si rimisura sulle 37** (E41), e non si rimisura affatto dopo le correzioni: il
punto della serie resta **0,0 % su 30**, con la riserva del lotto mono-fonte scritta accanto.

### 6.2 Il secondo giro dedicato, e come il ciclo si è fermato

Delle cinque correzioni, **quattro AGGIUNGEVANO** un'affermazione — un conteggio, un'attribuzione,
una distinzione di clausola — e sono tornate al giudice, come E58 prescrive. La quinta era
correttiva e si è applicata senza riaprire il ciclo (criterio 1B).

| Giro dedicato | Note | Rilievi accolti |
|---|---|---|
| **primo** | 7 | **5** |
| **secondo**, sulle sole note in cui la correzione **aggiungeva** | 4 | **0** |

⚠️ **Il ciclo si chiude qui**, al primo giro che torna con zero rilievi accolti (E26).

⚠️ **E il secondo giro ha lasciato due osservazioni sotto soglia, entrambe accolte**: il locator
del certificato diceva `pag. 1` e le condizioni stanno a **pag. 3** *(verificato sul file)*; e la
parola «immediata» ricorre altrove nella procedura, quindi «sta solo qui» valeva per il termine
di convocazione, non per la parola. **La prima è stata corretta**, la seconda era già scritta
così.

---

## 7. I numeri di chiusura (E44), tutti da script e con l'ora

**Misure fra le 15:16 e le 15:19 del 24/08/2026**, dopo l'ultima scrittura e dopo la
nota-sessione (E34).

| Misura | Valore | Strumento | Ora |
|---|---|---|---|
| **QA, perimetro lotto** | **0 ERRORI, 78 avvisi** — esito **GIALLO** | `qa_all.py` | 15:15 |
| note controllate nel perimetro | ~~**58** — 37 nate + 4 toccate + gli hub~~ → **49** — 37 nate + 12 toccate, incollato da `conta_perimetro_lotto.py` *(errata del 31/08, §6.1)* | `conta_perimetro_lotto.py` | 25/08, 09:17 |
| **QA, perimetro vault** | **107 ERRORI, 426 avvisi** | `qa_all.py` | 15:17 |
| di cui grezzi non ancora canonizzati | **105** | | |
| di cui aree senza hub | **2** — `ricerca-sviluppo`, `sicurezza-ambiente` | | |
| di cui **rilievi di merito** | **0** | | |
| errori per controllo | copertura **107** · frontmatter **0** · provenance **0** · link **0** | | 15:17 |
| **Collaudi** | **11 su 11** | `_collaudo\` | 15:19 |
| **Emendamenti** | registro e manuale **concordano a 63** | `verifica_emendamenti.py` | 15:17 |
| **Copie di stato** | **4 su 4** concordi col padrone | `verifica_copie_stato.py` | 15:17 |
| **Matrice** | completa e disgiunta — **160 grezzi, 33 elenchi**, guasti **0** | `verifica_matrice_lotti.py` | 15:17 |
| **lotti chiusi** | **12** — **11 di canonizzazione** + 1 di manutenzione, pilota escluso | `verifica_matrice_lotti.py` | 15:17 |
| **Tracciamento** | **175 righe**, da T1 a T175 | `conta_tracciamento.py` | 15:17 |
| **CSV file × fatto** | **41 righe** per il lotto 3E, **575** in tutto | `genera_matrice_file_fatto.py` | 15:16 |
| **Vault** | **470 note**, di cui **432 di contenuto** | `conta_stato.py` | 15:16 |
| **Grezzi canonizzati** | **55 su 160** — ne restano **105** | `conta_stato.py` | 15:16 |
| **Questioni aperte** (`type: conflitto`) | **67** | `conta_stato.py` | 15:16 |

⚠️ **Il vault scende da 108 a 107 errori** *(un grezzo canonizzato)*, e gli avvisi salgono da 425
a 426. **Zero rilievi di merito introdotti.**

⚠️ **Gli avvisi del perimetro di lotto sono 78, e vanno motivati** (§3.4 del prompt dei lotti):
**sedici sono summary oltre i 250 caratteri** su note che portano un confronto a più gambe — la
soglia esiste per il retrieval, e un summary che tace una delle due letture di una questione
sarebbe peggio del summary lungo; **due sono corpi fra 301 e 350 parole**, entrambi su questioni
che mettono a confronto due documenti riga per riga. **Il resto sono avvisi di provenance e di
link ereditati dal vault**, non introdotti da questo lotto.

---

## 8. Gli adempimenti di chiusura, eseguiti

- ✅ **Tabella di tracciamento**: **T159 chiusa**, **T163 aggiornata**, **cinque righe nuove** — T171-T175. Integra a **175**.
- ✅ **CSV `matrice_corpus_v1.csv`**: **41 righe** file × fatto per il lotto 3E.
- ✅ **`# CHIUSO il 24/08/2026`** in testa all'elenco del lotto.
- ✅ **Canone accresciuto** in sezione datata: **sette divergenze** (G1-G7), tutte scrivibili, più una **prova di solidità**. ⚠️ **Una riga B è stata corretta dal giudizio dedicato nello stesso turno**: la cl. 1.1.10 era mal ancorata.
- ✅ **`alias_entita.md`**: **classe A** `PRO-QA-14` e `MOD-MAG-02`; **classe B** i due Bertoldi del team di crisi; **classe C** `PRO-QA-13`, la terza sigla della famiglia.
- ✅ **`registro_emendamenti.md`**: nessun emendamento nuovo da questo lotto.
- ✅ **Nota-sessione** nel journal, e **solo dopo** il blocco dei conteggi (E34).
- ✅ **Misure di chiusura** dopo l'ultima scrittura, ognuna con la sua ora (E44).
- ✅ **`llms.txt`** rigenerato dopo l'ultima scrittura.

---

## 9. Che cosa il lotto lascia al gate

| | |
|---|---|
| **1. Il tema 3 non chiude con 3E** | La conta dei fatti ha spezzato il pacchetto in due, e **`3F` — il controllo pubblico ATS — è l'ultimo**. ⚠️ **Il prompt del gate diceva il contrario, e a cambiarlo è stata la misura**: è E53 applicato a una pianificazione invece che a un dominio |
| **2. La metà B di E59 ha respinto al primo impiego** | Eseguita a lotto chiuso come l'estensione di stamattina impone, ha tolto `\bPRO-QA-11\b` con quota fuori 0,57. ⚠️ **E il tasso non è cambiato**, il che prova che non era una stretta a numero visto. **Senza l'estensione, quell'espressione sarebbe rimasta dentro la dichiarazione** |
| **3. Il tasso di questo lotto è degenere, e va detto** | **0,0 % su 30**, ma il lotto ha **un grezzo solo** e quel grezzo **è la fonte del dominio**: ogni nota nata lo cita per costruzione, e **nessuna può risultare scoperta**. ⚠️ **Un lotto mono-fonte non può produrre un tasso diverso da zero sul dominio che quella fonte governa** — il numero è vero e il suo potere discriminante è nullo. **Il gate decida se un punto così entri nella serie o vi entri con una riserva** |
| **4. Il pattern che il terzo giro non ha esaurito** | **La frase di raccordo verso un'altra nota, che per reggere deve asserire qualcosa di quell'altra nota.** Nominata al §4.2. ⚠️ **Non è E36 sulla citazione: è E36 sul wikilink**, e nasce dal buon proposito di tessere il grafo |
| **5. Le glosse degli hub restano indietro come le intestazioni** | Tre glosse dicevano ciò che le correzioni avevano tolto dagli spoke, e **la clausola 4 di §7.1 le rende un ERRORE sull'hub**. ⚠️ **Nessuno le guarda quando corregge una nota**: è E39 esteso ed E42 applicati a una superficie che nessuna delle due nomina |
| **6. E61 ha colto tre correzioni mie su tre giri** | Ogni volta il giro dopo l'ha presa, quindi la rete funziona. ⚠️ **Ma il conto è tre su tre**, e il gate dovrebbe chiedersi se serva un appiglio meccanico per la frase nuova come ce n'è uno per il blocco `Fonti` |
| **7. Il debito che resta** | **T171-T175**, cinque righe aperte dichiarate. E **R2**, che ora copre **due domini** e si apre dopo `3F` |
| **8. Un lotto solo ha prodotto cinque righe B dallo stesso accostamento** | Il perimetro del blocco contro il mass balance. ⚠️ **Il vault aveva entrambe le gambe da agosto**, e a metterle una di fronte all'altra è stata la revisione col canone, non il ciclo: **è il terzo lotto di fila** |
