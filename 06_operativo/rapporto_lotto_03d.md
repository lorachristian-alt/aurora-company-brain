# Rapporto del lotto 3D — i reclami

> **Che cos'è** · Il consuntivo del quarto pacchetto del tema 3, eseguito fra il 23 e il
> 24/08/2026 secondo il ciclo di `prompt_s4_lotti.txt` §3, dalla PARTE 5 di
> `prompt\prompt_gate_3b_lotto_3d.txt`.
> **È il primo lotto che gira con E59, E60 ed E61 in vigore**, e due dei tre strumenti che
> quelle regole prescrivono **non esistevano**: sono stati costruiti in apertura.
> **Misure** · tutte da script, ognuna con la sua ora (E44).

---

## 1. L'apertura

### 1.1 I tre grezzi, e il censimento dei fatti (E21)

| Grezzo | Che cos'è | Fatti contati |
|---|---|---|
| `PRO-QA-08_gestione_reclami_cliente_rev2.docx` | la **procedura** che governa il ciclo del reclamo: 12 paragrafi, 5 tabelle, **3 passaggi barrati**, **11 annotazioni di revisione** lasciate nel testo *(contate)* | **18** |
| `segnalazione_qualita_cliente_privato_corpo_estraneo.txt` | la **catena della segnalazione**: 6 messaggi dal 12 al 15/05, dalla notifica automatica del form alla decisione sul ritiro | **10** |
| `Fwd_Fwd_Fwd_ATTENZIONE_richiamo_prodotto_concorrente_RASFF.eml` | la **catena dell'allerta**: 4 messaggi in 22 ore, dalla circolare dell'associazione alla verifica interna | **5** |

**Proiezione: 33-38 note di contenuto.** Consuntivo: **35**. La capacità di E31 è 25-35: la
proiezione cade sul bordo alto e **non supera le 40** — non si spezza per E28.

### 1.2 ⚠️ IL LOTTO SI SPEZZA, MA PER L'ALTRA SOGLIA — quella di E37

La riconciliazione verticale arretrata sul dominio `reclami` ha riaperto **65 note**, contro
le **35** che il ciclo proietta di produrre. **Le riaperte superano le nuove**, e la regola è
esplicita: il lotto si dichiara e si spezza in uno di canonizzazione più uno di manutenzione.

| | |
|---|---|
| **`lotto_03d_reclami`** | canonizzazione: i tre grezzi e le note che il lotto tocca |
| **`r2_reclami_verticale`** | **nuovo**, manutenzione: le 65 note riaperte dalla verticale |

⚠️ **Il perimetro di R2 si rigenera alla sua apertura, non si eredita.** Con `PRO-QA-08` ormai
canonizzata, `candidate_r1.py --dominio reclami` restituirà un insieme diverso, e **la
differenza misura quanto 3D ha già sanato**. Gli elenchi della matrice passano da 27 a 28; R2
vale un lotto nel ritmo e resta **fuori dalla serie della capacità** (E38).

### 1.3 ⚠️ DUE STRUMENTI CHE E60 ED E59 PRESCRIVONO E CHE NON ESISTEVANO

Il gate del lotto 3B ha scritto due regole che chiedono uno script, e nessuno dei due script
era stato costruito. **Sono stati scritti in apertura di questo lotto**, perché una regola che
prescrive uno strumento inesistente è una regola che si applica a mano — cioè la cosa che quel
gate stava correggendo.

| Strumento | Che cosa fa | Perché serviva |
|---|---|---|
| **`grandezze_condivise.py`** | l'**artefatto d'apertura di E2**: le grandezze che compaiono in più di un grezzo, quelle che una nota del vault già porta, e le entità del vault nominate dai grezzi | E60 lo prescrive e il prompt dei lotti lo dà per esistente |
| **`collauda_dominio.py`** | il **collaudo di E59**: ogni espressione del dominio provata da script, prima della misura | E59 lo prescrive e non c'era |

⚠️ **La grammatica delle grandezze non è nuova, ed è deliberato**: `grandezze_condivise.py`
riusa `qa_provenance.estrai_affermazioni`, cioè **la stessa definizione di affermazione
verificabile con cui la QA boccia una nota**. Una seconda definizione divergerebbe in un mese,
e per giunta farebbe guardare a chi apre il lotto cose diverse da quelle su cui verrà giudicato.

### 1.4 E53 — il dominio si verifica, e c'è

`verifica_dominio.py --lotto lotto_03d_reclami`, misura delle **23:30:41 del 23/08/2026**:
**8 fonti prescrittive citate per sigla** nei tre grezzi, di cui **5 citabili**; 22 fonti con
i soli riscontri deboli, che non contano.

### 1.5 E56 — la coppia, e ciò che è stato lasciato fuori

**Fonte del dominio: una sola, `PRO-QA-08`.** Governa il ciclo per intero — ricezione e
protocollo (§6.1), classi e tempi (§5, §6.3), verifiche immediate (§6.2), causa radice (§7.1),
campione reso (§7.3), comunicazione (§8), azioni correttive (§9), indicatori (§10),
archiviazione (§11).

**Le nove espressioni, e la fonte che ciascuna chiama in causa:**

| Espressione | Che cosa la giustifica |
|---|---|
| `\breclam` | il nome dell'oggetto che la procedura governa |
| `\bREC-20\d\d-\d{3}\b` | il protocollo che il §6.1 istituisce |
| `\bMOD-QA-31\b` | il modulo che il §6.1 istituisce e il §11 conserva |
| `\bPRO-QA-08\b` | la sigla della fonte stessa |
| `corpo estrane` | l'esempio di classe 1 del §5, e il caso del lotto |
| `causa radice` | il §7.1, obbligatorio per le classi 1 e 2 |
| `campione reso` | il §7.3, la locuzione con cui la procedura nomina l'oggetto |
| `blocco cautelativ` | il §6.2, punto 3 |
| `consumatore final` | il §8.2, la metà di cui la procedura è padrona |

⚠️ **Ciò che è stato lasciato fuori, e il motivo — perché un dominio si legge anche da
quello**, ed è qui che 3C aveva sbagliato:

| Fuori | Perché |
|---|---|
| `ritiro`, `richiamo` | li governa **un'altra procedura**, che `PRO-QA-08` **richiama senza contenere** |
| `azione correttiva` | la governa `PRO-QA-05`, che nel corpus non c'è |
| `non conformità`, `NC-\d` | sono di tutto l'archivio: è la parola che al primo taglio di 3C riapriva **due note del vault su cinque** |
| `campione` da solo | la campioteca la prescrive **anche** il manuale HACCP |
| `metal detector`, `CCP3` | il §6.2 dice di **riesaminare** quelle registrazioni; a prescriverle è il manuale |

### 1.6 ⚠️ E59 AL PRIMO IMPIEGO, E IL COLLAUDO HA TROVATO UN DIFETTO DEL COLLAUDO

Il primo `collauda_dominio.py` respingeva **sei espressioni su nove**, fra cui `\bMOD-QA-31\b`
— **la sigla del modulo che la procedura istituisce**, cioè l'espressione più specifica che
questo dominio possa avere.

⚠️ **Non era il dominio a essere sbagliato: era la prova.** La prova che E59 descrive confronta
le note che **citano le fonti del dominio** con quelle che non le citano. Ma **la fonte di
questo dominio la stava portando questo lotto**: nessuna nota poteva citarla, la colonna
«dentro» era zero **per costruzione**, e ogni espressione risultava generica.

⚠️ **E c'era di peggio, ed è la parte che conta**: contare come «governata altrove» una nota
che parla di reclami citando il manuale HACCP **è esattamente il contrario del vero** — quella
nota è **scoperta**, cioè ciò che il tasso di E41 esiste per contare. La prova, applicata così,
avrebbe respinto le espressioni giuste e lasciato passare quelle sbagliate.

**Lo strumento è stato riscritto in due prove che non si sommano:**

| Prova | Che cosa misura | Quando si può fare |
|---|---|---|
| **A — la specificità** | quante note ogni espressione riconosce **in esclusiva**, e che quota dell'unione del dominio copre **da sola** | **sempre** |
| **B — dentro e fuori** | quante riconosciute citano una fonte del dominio, quante solo altre prescrittive | **solo se la fonte del dominio è già citata da qualche nota** |

⚠️ **La prova A è quella che 3B ha eseguito a mano**: `\bformazion` copriva il **100 %** del
dominio da sola. E una sospetta **non si scarica cambiando la soglia**: si scarica con
`--motivata <espressione>`, che la registra in chiaro nell'uscita, **e con una ragione scritta
nel rapporto**.

**L'esito, in apertura (prova B non applicabile, dichiarata tale):** nove espressioni su nove
superano la prova A. `\breclam` copre l'83 % dell'unione con 31 note in esclusiva — sotto la
soglia di 0,90. `campione reso` non riconosce **nessuna** nota del vault: è una locuzione che
il vault non aveva ancora usato, e il fatto è stato dichiarato invece di ignorato.

**E l'esito a lotto chiuso, quando la prova B diventa applicabile:**

| Espressione | Riconosce | cita il dominio | solo altre prescrittive | quota fuori |
|---|---|---|---|---|
| `\breclam` | 79 | 22 | 31 | **0,39** |
| `\bREC-20\d\d-\d{3}\b` | 21 | 4 | 10 | 0,48 |
| `\bMOD-QA-31\b` | 15 | 8 | 5 | 0,33 |
| `\bPRO-QA-08\b` | 21 | 17 | 3 | 0,14 |
| `corpo estrane` | 14 | 7 | 4 | 0,29 |
| `causa radice` | 13 | 5 | 5 | 0,38 |
| **`campione reso`** | **5** | **5** | **0** | **0,00** |
| `blocco cautelativ` | 7 | 1 | 3 | 0,43 |
| `consumatore final` | 3 | 2 | 1 | 0,33 |

⚠️ **Tutte sotto la soglia, e `campione reso` — muta in apertura — a lotto chiuso riconosce
cinque note e tutte e cinque citano il dominio.** ⚠️ **È un dato per il gate**: la metà di E59
che in apertura non si può fare **si può fare alla chiusura**, e a quel punto misura qualcosa
di reale. Non è un emendamento che questo lotto propone: è un'osservazione con un consuntivo.

### 1.7 E60 — l'artefatto d'apertura, e che cosa ha trovato

`grandezze_condivise.py --lotto lotto_03d_reclami`, misura delle **23:32:29 del 23/08/2026**:

| | In apertura | A lotto chiuso |
|---|---|---|
| grandezze condivise **fra i grezzi** | **8** | 8 |
| grandezze del lotto **già nel vault** | **39** su 61 | **58** su 61 |
| **entità** del vault nominate dai grezzi | **23** | 24 |

⚠️ **L'artefatto porta rumore, e va detto**: fra le 61 grandezze estratte ci sono un prefisso
telefonico, un CAP e due identificativi di form. **Non è un difetto da correggere allargando
la grammatica**: è la stessa grammatica con cui la QA giudica le note, e chi apre il lotto
filtra. Un'estrazione più «intelligente» sarebbe una seconda definizione.

---

## 2. I due tassi (E41), col nome del dominio (E46)

| | Punto **DICHIARATO** | Rimisurato a fine ciclo |
|---|---|---|
| **Tasso di riapertura** *(debito)* | ⚠️ **non misurato in 3D**: le 65 riaperte sono andate a **R2** con lo spezzamento, e il tasso è suo | — |
| **Tasso di difetto di produzione** *(metodo)* | **20,0 %** — 7 su 35, dominio `reclami` | 14,3 % — 5 su 35 |

⚠️ **Il punto della serie è 20,0 %, e il 14,3 % non lo sostituisce** (E41): il secondo è quello
che lo script restituisce **dopo** le correzioni del giudizio, e rimisurarlo farebbe sparire
proprio ciò che la misura esiste per mostrare.

⚠️ **Delle sette scoperte, DUE erano lacune vere e cinque no**, e il residuo si dichiara invece
di sparire:

| Nota | Verdetto |
|---|---|
| `fatto-segnalazione-dal-form-12-05` | ⚠️ **lacuna vera**: usava il §2 e il §6.1 senza citarli. **Corretta** |
| `questione-ora-di-arrivo-della-segnalazione` | ⚠️ **lacuna vera**: invocava i termini del §6.1 e del §6.3. **Corretta** |
| `fatto-secondo-reclamo-rec-2026-012` | ⚠️ **lacuna vera**, trovata dal tasso: l'apertura di una pratica è l'adempimento del §6.1. **Corretta** |
| `fatto-due-segnalazioni-rendono-il-ritiro-non-rimandabile` | ⚠️ **lacuna vera**: la valutazione del ritiro sta nel §4 e nel §6.2. **Corretta** |
| `fatto-frammento-non-e-film-map` | **residuo dichiarato**: descrive un reperto, e `PRO-QA-08` non governa che cosa un frammento sia |
| `fatto-ccp3-non-in-causa-sul-frammento` | **residuo dichiarato**: parla del CCP3, e la fonte che lo governa è il **manuale HACCP** — che le è stata aggiunta (E36) |
| `questione-referenza-del-secondo-reclamo` | **residuo dichiarato**: quale referenza sia colpita non è materia della procedura |

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
| **3D** | **`reclami`** | **20,0 %** su 35 — ⚠️ **primo punto con la dichiarazione COLLAUDATA** |

⚠️ **È il primo punto della serie prodotto da un dominio che ha superato una prova
meccanica**, ed è il più basso dei tre del tema 3. **Un punto non fa una tendenza**, e la
prova B non era applicabile in apertura: il numero va letto con quella riserva.

---

## 3. Che cosa il lotto ha trovato

### 3.1 ⛔ IL DOCUMENTO CHE L'ARCHIVIO DICHIARAVA DI NON AVERE

`questione-data-apertura-rec-2026-011`, scritta il 19/08, elencava fra le cose che sarebbero
servite per chiuderla **«la mail automatica di notifica della segnalazione, che l'archivio non
contiene»**. ⚠️ **L'archivio la contiene**, ed è il primo grezzo di questo lotto.

⚠️ **È E3 pagato per la QUINTA volta in sette lotti**, e con una forma nuova: il grezzo
esisteva in `sources\` fin dall'inizio, in un lotto non ancora canonizzato — **e E3 chiede la
ricerca su TUTTO `sources\`, non sui lotti chiusi**.

⚠️ **E il controllo di E43 non poteva prenderla**: quella nota non usa la formula di
attestazione, dichiara l'assenza dentro un elenco di «cosa servirebbe per chiuderla». **La
superficie in cui un'assenza si nasconde è più larga della formula che la dichiara** — ed è la
stessa scoperta che il gate 3B ha fatto sull'intestazione, un piano più in là. **T161**.

### 3.2 ⛔ IL DOCUMENTO ARRIVA E LA DIVERGENZA SI ALLARGA

| Fonte | A che ora è arrivata la segnalazione |
|---|---|
| notifica automatica del form | **`2026-05-12 18:23:47 CEST`** |
| riunione di direzione, [00:00:37] | «ieri sera alle 18 e 23» |
| ⚠️ **mail interna del 12/05, ore 14:33** | «e' arrivato **alle 13:05** dal form "contatti" del sito» |

⚠️ **La difficoltà non è quale ora sia giusta: è che la mail delle 14:33 è ANTERIORE alla
notifica.** Se la segnalazione fosse partita alle 18:23, la comunicazione interna che la
descrive — col nome della segnalante, il prodotto, il lotto letto dalla foto e il punto vendita
— sarebbe stata scritta quasi quattro ore prima che il messaggio esistesse. **T5 non si chiude:
si allarga**, e ha una padrona.

### 3.3 ⛔ TRE QUALIFICAZIONI, E FORSE DUE SCALE DIVERSE

| Fonte | Che cosa dice |
|---|---|
| scheda del reclamo | **Classe 2**, e la attribuisce al **par. 4 di un'ALTRA procedura** |
| registro degli indicatori | **CRITICO** |
| mail interna del 12/05, 14:33 | «classifico come **GRAVE**» |

⚠️ **La scoperta non è la terza qualificazione: è che la scheda non dichiara di applicare
`PRO-QA-08`.** Non è detto che le fonti stiano leggendo la stessa scala in due modi:
potrebbero applicarne **due diverse**. ⚠️ **Il divieto 9-bis vale per intero** — il vault
registra che la scheda cita quella procedura e **non dice nulla di ciò che contiene**.
**Obbligo esplicito per il lotto che la porta: T159.**

⚠️ **L'ha trovata la TERZA DOMANDA del prompt di giudizio**, quella sulla lacuna di copertura,
che il metodo descrive come segnale «poco più di una volta su due».

### 3.4 Le altre divergenze e i ritrovamenti

- **Il secondo reclamo è registrato su una referenza e un lotto che nessuna fonte conferma**:
  il registro dice `AF-SN-0450` lotto `L26130-L1-T2`, la qualità lo attribuisce alla
  `AF-SN-0455` **dichiarandolo come inferenza**, e il segnalante scrive di **non ricordare il
  lotto**. **T160**.
- **Il frammento del secondo caso è ancora dal segnalante**, e l'archivio non dice se sia mai
  stato ritirato né analizzato — mentre la procedura prescrive la richiesta del reperto e il
  ritiro a cura dell'azienda. **T162**.
- **Il punto critico non ha fallito, e il piano lo diceva**: l'analisi dei pericoli del manuale
  porta «frammenti di guarnizioni/plastiche da organi macchina» con la nota che il metal
  detector non li rileva e che la misura di controllo è **preventiva**.
- **`T146` si chiude, e l'obbligo esplicito è stato eseguito**: ciò che la politica attribuisce
  a `PRO-QA-08` e ciò che la procedura prescrive **corrispondono** — ⚠️ ma la procedura **non
  nomina il «miglioramento»** fra i propri scopi: quello è la lettura che la politica ne dà.

---

## 4. Il ciclo di giudizio

### 4.1 I due giri, e i numeri

| Giro | Note giudicate | Rilievi accolti | Di che specie |
|---|---|---|---|
| **primo** | 40 (4 fette) | **17** | 4 affermazioni universali false, 3 contenuti attribuiti a fonti non dichiarate, 6 citazioni non testuali, 1 fonte duplicata, 3 giudizi non formulati dalla fonte |
| **secondo** | 43 (4 fette) | **5** | 1 nome di file, 1 universale falsa, 1 presupposto non dichiarato, 1 contenuto attribuito a una fonte non dichiarata, 1 cautela non propagata |

⚠️ **Ogni fetta ha portato l'appendice completa delle fonti**, e i quattro giudici di ogni giro
lo hanno verificato per primo: §4.31 e §4.29 al lavoro.

### 4.2 ⚠️ IL RILIEVO CHE NESSUN ALTRO STRATO PUÒ VEDERE: IL NOME DEL FILE

Al primo giro un giudice ha preso il **titolo** di una nota che affermava «rincorse **a
voce**», dove l'annotazione della fonte dice solo «finora l'ho rincorsa io» — senza indicare
alcun canale. La correzione ha sistemato **titolo, summary e corpo**.

⚠️ **Al secondo giro lo stesso rilievo è tornato, e sul NOME DEL FILE**, che continuava a dire
`fatto-confezioni-vendute-rincorse-a-voce`.

⚠️ **È E30 un gradino più in là, e vale la pena dirlo per esteso.** E30 dice che `title` e
`summary` sono note a sé perché si scrivono per primi e si correggono per ultimi. **Lo slug si
scrive prima del titolo e non si corregge mai**: è la superficie che si scrive per prima in
assoluto, e l'unica che nessuna rilettura del testo tocca. **La QA non la guarda** — non è
un'affermazione per nessun controllo — **ma il giudice la vede**, perché il nome della nota è
la prima cosa che il pacchetto gli mette davanti. Nota rinominata e wikilink aggiornati.

### 4.3 ⚠️ E61 IN FLAGRANZA, TRE VOLTE, E DUE DENTRO UNA RICONCILIAZIONE

E61 è entrato in vigore ieri, e questo lotto ne ha prodotto tre istanze pulite:

| Caso | Che cosa è successo |
|---|---|
| `questione-data-apertura-rec-2026-011` | aggiungere una fonte ha reso **falsa** una frase che c'era già: «il termine di 48 ore non è di nessuna delle fonti di questa nota» — e la fonte aggiunta lo contiene |
| `questione-nc-interne-registrate-su-mod-qa-31` | la riconciliazione di E60 ha attribuito un contenuto al manuale HACCP, che **quella nota non ha fra le fonti** — la nota gemella sì, e lì la stessa frase regge |
| `questione-data-apertura-rec-2026-011`, secondo giro | la correzione del primo giro ha scritto un'universale falsa: «l'intera catena interna del 12/05 sta prima delle 18:23» — il messaggio delle 22:40 no |

⚠️ **Le prime due sono la stessa cosa vista da due lati**: una correzione che **aggiunge una
fonte** cambia il perimetro di verità della nota intera, e le frasi che c'erano prima vanno
rilette **contro il perimetro nuovo**. E61 dice di rileggere la frase nuova; **questi due casi
dicono che va riletta anche la vecchia, quando è il perimetro a muoversi.**

### 4.4 ⚠️ E39 IN FLAGRANZA: LA CAUTELA NON È ARRIVATA ALLA NOTA SORELLA

Il primo giro ha corretto «rincorse a voce» in `fatto-confezioni-vendute-rincorse-dalla-qualita`.
⚠️ **La stessa affermazione stava in `doc-indicatori-reclami`, e lì è rimasta** — l'ha presa il
secondo giro. E39 chiede di cercare **tutte le altre occorrenze dell'affermazione**, ed E42 di
farlo **nello stesso turno**: la ricerca è stata fatta **dentro** la nota e non **fra** le note.

### 4.5 Le segnalazioni di copertura respinte, e perché

| Segnalazione | Perché respinta |
|---|---|
| `fatto-esempio-cinque-perche…` ← la guarnizione azzurra del 14/05 | ⚠️ **Costruirebbe l'identificazione che la nota si rifiuta di fare.** La procedura dichiara l'esempio **didattico**, e le due annotazioni discutono se somigli troppo al caso: aggiungere la fonte del caso trasformerebbe una somiglianza discussa in un nesso affermato |
| `doc-*` ← la trascrizione della riunione, il `MOD-QA-31`, il cruscotto | ⚠️ **Sono note DOCUMENTARIE: dicono che cosa la procedura prescrive, non che cosa è successo.** Aggiungere le fonti dell'applicazione le trasformerebbe in note di fatto, e i fatti hanno già le loro padrone |
| `area-qualita` ← `PRO-QA-08` e il verbale di riesame | ⚠️ **È un hub**: si verifica contro le note che elenca (§7.1 clausola 4), non contro le fonti di quelle note |
| `fatto-evidenze-nc1-partite-il-02-04` ← il rapporto d'audit e il registro NC | ⚠️ **Accolta in parte**: il fatto ha già tre padrone nel vault, e la nota vi rimanda. Ricopiarne le fonti sarebbe E40 al rovescio |

---

## 5. La revisione col canone: 10 A, 7 B, 7 C — e un obbligo del canone che non avevo eseguito

Subagente a contesto pulito, col canone e la tabella alias alla mano (E45). Ha letto il canone
integrale, i tre grezzi con l'estrazione di cantiere, le 47 note del lotto e le note collegate.

### 5.1 ⛔ IL RILIEVO PIÙ GRAVE: UN OBBLIGO ESPLICITO DEL CANONE, NON ESEGUITO

Il canone, alla riga **D4** scritta al gate del lotto 3C, dice testualmente che
`PRO-QA-08` §7.4 porta la coppia di clausole `BRCGS 9 cl. 2.10.2 / IFS 5.1.2` e che **«alla
canonizzazione di 3D quella riga va aggiunta alla nota»**.

⚠️ **Non l'avevo fatto.** La nota `questione-clausola-della-nc1-in-due-versioni` non era stata
toccata, non aveva `PRO-QA-08` fra le fonti, e continuava a dare la combinazione mista per **un
solo documento** — il registro delle non conformità.

⚠️ **E il rilievo non è formale, perché cambia la lettura della questione.** Quella nota diceva
che la combinazione che nessun documento dell'ente contiene «è proprio quella con cui Aurora ha
archiviato la non conformità a sistema» — cioè un incrocio nato dentro un registro. **Adesso la
stessa combinazione compare in un prescrittivo approvato**, redatto, verificato e approvato da
tre persone diverse: non è una svista di registro, è una coppia che l'azienda ha scritto due
volte.

⚠️ **Perché nessuno degli altri strati poteva prenderlo.** La QA non legge il canone; il
giudice non lo riceve per costruzione (E45), e giudica una nota contro **le sue** fonti — non
contro un obbligo scritto altrove. **L'obbligo del canone lo può verificare solo chi ha il
canone**, ed è la ragione per cui il passo 7 esiste.

### 5.2 Le altre nove A

| | Rilievo | Esito |
|---|---|---|
| **A1** | «sei annotazioni di revisione» — **sono undici** *(contate con l'estrazione di cantiere)* | corretto, col marcatore del derivato |
| **A3** | `doc-indicatori-reclami` rimandava a un confronto «altrove» **che nel vault non esisteva** | scritta la questione, e il rimando adesso porta a una nota |
| **A4** | `doc-verifiche-immediate-reclamo` diceva che il documento sul ritiro «non è nel perimetro»: la sigla è di **un file su 160**, e il manuale ne usa un'altra | corretto, e ne è nata una questione |
| **A5** | `fatto-fantin-approva-le-azioni-correttive` **irraggiungibile dal proprio hub d'area** | elencata in `area-direzione` |
| **A6** | `doc-pro-qa-08` diceva «stanno nelle note collegate» **e non le collegava** | nove wikilink aggiunti |
| **A7** | la sigla `PRO-ACQ-03` dichiarata conosciuta **e mai scritta** | scritta |
| **A8** | `alias_entita.md` **non esteso dal lotto** | quattro righe di classe A, due di classe C, riga nel registro |
| **A9** | «riga 8» usato per il **reclamo n. 8** | corretto |
| **A10** | riga di fonte duplicata | già corretta al secondo giro di giudizio |

⚠️ **A5 è la stessa specie che il gate 3B ha censito**: la QA di lotto valuta gli orfani **nel
sottografo del lotto**, e una nota raggiungibile da un'altra nota del lotto non risulta orfana
anche se **nessun hub la elenca**. Il difetto non è nel controllo: è nel perimetro in cui gira.

### 5.3 Le sette B, e come sono state trattate

| | Divergenza | Trattamento |
|---|---|---|
| **B1a** | **la procedura di ritiro ha due codici**: `PRO-QA-11` (procedura) contro `PRO-QA-14` rev. 3 (manuale HACCP) | ✍️ **questione scritta**, entrambe le gambe canonizzate — **T163** |
| **B1b** | **`PRO-QA-08` designa due procedure**: i reclami e la rintracciabilità del `PRP-09` | ✍️ **questione scritta** — **T164**, e classe C della tabella alias |
| **B1c** | la scheda classifica **citando l'altra procedura** | 🚫 **parziale**: divieto 9-bis, obbligo esplicito per 3E — **T159** |
| **B2** | il grezzo **non concorda con sé stesso** su quanti turni del 10/05 siano in gioco | ✍️ scritta in `fatto-perimetro-stimato-del-ritiro` |
| **B3** | la **richiesta dell'auditor** sulle allerte non è nel rapporto d'audit | ✍️ **questione scritta** — **T166** |
| **B4** | il **«riesame trimestrale HACCP»** non esiste in nessun'altra fonte | ✍️ **questione scritta** — **T165** |
| **B5** | «l'ho vista solo adesso»: la **gamba soggettiva** sull'arrivo della segnalazione | ✍️ scritta nella questione dell'ora |
| **B6** | il **suffisso del lotto**: letto dalla foto in una fonte, illeggibile in un'altra, **stessa foto** | ✍️ scritta in `fatto-segnalazione-dal-form-12-05` |
| **B7** | la **quinta lettura** della misura del frammento, 7-9 mm, e l'unica che dà un intervallo | ✍️ scritta in `questione-misura-frammento-strumentale` |

### 5.4 ⚠️ IL CONTRARIO DELLA SOVRA-ATOMIZZAZIONE, PER LA SECONDA VOLTA IN DUE LOTTI

Alla domanda del passo 7 il revisore risponde che **le dodici note del prescrittivo mappano
dodici paragrafi numerati** e reggono ognuna una domanda che qualcuno in azienda pone davvero.
**Non c'è sovra-atomizzazione.**

⚠️ **C'è il problema opposto, ed è il secondo lotto di fila che lo mostra** (in 3B erano cinque
righe di registro senza nessuna nota):

| Paragrafo senza padrona | Che cosa conteneva |
|---|---|
| **§9 «Azioni correttive e verifica di efficacia»** | ⚠️ **la definizione di reclamo chiuso** — «risposta definitiva inviata, azioni correttive attuate, verifica di efficacia pianificata» — e l'escalation all'Amministratore Delegato oltre la delega di spesa |
| **§3 «Riferimenti»** | l'art. 19 del Reg. (CE) 178/2002, le clausole dei due standard, e **la sigla della procedura di ritiro** |

⚠️ **La prima è la più pesante**: è il criterio con cui si risponde a «questa pratica è chiusa?»,
e il vault trattava quella domanda nell'hub del progetto **senza avere il criterio**. Nate
`doc-chiusura-di-un-reclamo` e `doc-riferimenti-pro-qa-08`.

**E altri tre fatti dei grezzi che nessuna nota copriva:** i **quattro clienti GDO nominati per
esteso** dalla procedura, con le **48 ore di Tosano già scritte in procedura dal 14/03** — cioè
prima che il cliente le attivasse; l'annotazione **«è successo»**, l'unica delle undici che
registra un evento; e il fatto che la copia conservata **non è la copia controllata**, con
annotazioni fino al 12/05 e il numero di copia in bianco.

### 5.5 Le C, e perché non ci si torna sopra

| | Perché non è un problema |
|---|---|
| il file rinominato durante la revisione | **una nota sola**, e il rinomino è coerente anche nell'elenco del lotto: non è una doppia padrona |
| l'esempio dei cinque perché | la nota fa la cosa giusta: dichiara che è **didattico per parola della fonte** e si rifiuta di trattarlo come registrazione dell'evento |
| «Classe 2 / CRITICO / GRAVE» | la questione è ben costruita e dichiara l'inferenza; ciò che le mancava riguarda **quale procedura** governi la scala, non la scala |
| «un uomo di Sona» | inferenza dal nome, innocua, e coerente con la prudenza usata altrove sugli anonimizzati |
| `BRCGS 3.10 / IFS 5.8` contro `2.10.2 / 5.1.2` | **due riferimenti a cose diverse**: il capitolo che governa i reclami, e la clausola della non conformità |
| il barrato usato al presente | **verificato riga per riga: mai** |

### 5.6 ⚠️ E UNA PROVA DI SOLIDITÀ DEL CANONE, CHE NESSUNA NOTA AVEVA COLTO

La consumatrice dichiara la scadenza **24/06/2026** su un prodotto del lotto `L26130`, cioè del
**10/05/2026**: sono **45 giorni** *(contati)*, **esattamente la shelf life della scheda tecnica
in vigore**. ⚠️ **Un dato scritto da una persona senza alcun accesso ai documenti dell'azienda
cade sul valore prescritto.** Registrata a canone come prova di solidità, non come rilievo.

## 6. Il giudizio dedicato di E58, e come il ciclo si è fermato

Le **dieci note nate dalla revisione col canone** non avevano mai visto un giudice. Hanno
ricevuto un **giudizio dedicato** (E58) — non un giro nuovo sul lotto — insieme alle quattro
note del vault che le correzioni della revisione avevano riscritto in modo sostanziale.

| Giro dedicato | Note | Rilievi accolti |
|---|---|---|
| **primo** | 14 | **7** |
| **secondo**, sulle sole note in cui la correzione **aggiungeva** un'affermazione | 2 | **1** |

⚠️ **Il secondo giro dedicato è stato fatto su due note e non su quattordici**, ed è la regola
di E58 applicata alla lettera: cinque delle sette correzioni erano **soppressive** — toglievano
un'affermazione — e per quelle il criterio del lotto 1B dice che si applicano senza riaprire
il ciclo. Solo due **aggiungevano**, e solo quelle sono tornate al giudice.

### 6.1 ⚠️ IL RILIEVO CHE VALE PIÙ DEGLI ALTRI: LA FOTOGRAFIA SBAGLIATA

Scrivendo la quinta lettura della misura del frammento avevo attribuito il «7-9 mm» della mail
del 13/05 **alla fotografia col riferimento metrico**. ⚠️ **La mail dice un'altra cosa**: la
sua stima viene dalla **foto caricata dal form dalla segnalante**, non da quella scattata il
giorno dopo. **Sono due immagini diverse**, e confonderle avrebbe fatto sembrare incoerenti due
letture prese su oggetti fotografici distinti.

⚠️ **E il secondo giro dedicato ha trovato che il problema era più vecchio della mia
correzione**: la nota portava **da prima** frasi come «è l'unica immagine del frammento prima
dell'invio» e «la fonte su cui la scheda del reclamo dichiara di essersi basata» — affermazioni
che le sue tre fonti non sorreggono, perché **la scheda del reclamo non è fra le sue fonti**.
**Toccare una nota vecchia l'ha portata sotto un giudice che non l'aveva mai vista** (E32), e
il giudice ha preso ciò che c'era già.

### 6.2 Gli altri sei rilievi del giro dedicato

| Nota | Rilievo | Correzione |
|---|---|---|
| `fatto-nessuno-risponde-a-voce-al-consumatore` | «l'unica delle undici che registra un EVENTO» — **altre due riferiscono fatti accaduti** | ristretta: l'unica che **fa discendere una prescrizione** da un episodio |
| `fatto-pro-qa-08-copia-di-lavoro` | «il giorno in cui il reclamo arriva» — la fonte dice solo «il caso del 12/05» | soppressiva |
| `doc-riferimenti-pro-qa-08` | la glossa sull'art. 19 non è nel §3 | soppressiva |
| `doc-seconda-firma-indagine` | «la combinazione che nessun documento dell'ente contiene» — non è nelle sue fonti | soppressiva, con rimando alla padrona |
| `questione-due-codici-per-la-procedura-di-ritiro` | il caso di maggio non è nelle sue fonti | soppressiva |
| `questione-pro-qa-08-reclami-o-rintracciabilita` | la politica non era fra le fonti | ✅ **aggiunta la fonte**, ed è l'unica additiva |

⚠️ **E una nota di calibrazione del giudice ha smontato un'affermazione che davo per sicura**:
avevo scritto che la procedura, del 14/03/2026, è «il documento più recente dei due». ⚠️ **Non
si può dire**: quale revisione del manuale HACCP sia in vigore è **a sua volta una questione
aperta del vault**, e l'estratto porta tre indicazioni diverse. Frase corretta e rimando alla
questione.

---

## 7. I numeri di chiusura (E44), tutti da script e con l'ora

**Misure fra le 01:09 e le 01:10 del 24/08/2026**, dopo l'ultima scrittura e dopo la
nota-sessione.

| Misura | Valore | Strumento | Ora |
|---|---|---|---|
| **QA, perimetro lotto** | **0 ERRORI, 65 avvisi** — esito **GIALLO** | `qa_all.py` | 01:09 |
| note controllate | **61** — 16 toccate + 45 nate | `conta_perimetro_lotto.py` | 01:09 |
| **QA, perimetro vault** | **108 ERRORI, 344 avvisi** | `qa_all.py` | 01:10 |
| di cui grezzi non ancora canonizzati | **106** | | |
| di cui aree senza hub | **2** — `ricerca-sviluppo`, `sicurezza-ambiente` | | |
| di cui **rilievi di merito** | **0** | | |
| **Collaudi** | **10 su 10** | `_collaudo\` | 01:10 |
| **Emendamenti** | registro e manuale **concordano a 61** | `verifica_emendamenti.py` | 01:10 |
| **Copie di stato** | **4 su 4 concordi col padrone** | `verifica_copie_stato.py` | 01:10 |
| **Matrice** | completa e disgiunta — **lotti chiusi: 11** | `verifica_matrice_lotti.py` | 01:10 |
| **Tracciamento** | **167 righe**, da T1 a T167 | `conta_tracciamento.py` | 01:10 |
| **CSV file × fatto** | **55 righe** per il lotto 3D, 534 in tutto | `genera_matrice_file_fatto.py` | 01:09 |
| **Vault** | **432 note**, di cui **395 di contenuto** | `conta_stato.py` | 01:10 |
| **Grezzi canonizzati** | **54 su 160** — ne restano **106** | `conta_stato.py` | 01:10 |
| **Questioni aperte** (`type: conflitto`) | **61** | `conta_stato.py` | 01:10 |

⚠️ **Il vault scende da 111 a 108 errori, ed è esattamente ciò che il lotto ha fatto**: tre
grezzi canonizzati. **Zero rilievi di merito introdotti.**

### 7.1 ⚠️ IL GRUPPO DELLE NOTE POST-REVISIONE, DICHIARATO COME E52 IMPONE

| | |
|---|---|
| note nate dal **ciclo** | **35** — è il denominatore del tasso dichiarato |
| note nate dalla **revisione col canone** | **10** — fuori dalla soglia di spezzamento (E52) |
| **totale nate nel lotto** | **45** |

⚠️ **Il tasso ricalcolato su 45 note darebbe 8,9 %. Non si usa**, per due ragioni che si
sommano: E41 vieta di rimisurare a correzioni fatte, ed E52 tiene le note post-revisione fuori
dal conto del ciclo. **Il punto della serie resta 20,0 % su 35.**

⚠️ **E gli esiti di giudizio del gruppo vanno letti separati, perché sono diversi**: le 35 note
del ciclo hanno preso **22 rilievi in due giri** (17 + 5); le 10 note della revisione ne hanno
presi **8 in due giri dedicati** (7 + 1), su un gruppo tre volte e mezzo più piccolo. **La
densità di difetto del gruppo post-revisione è più alta**, come in 3A — e la ragione è la
stessa: sono note scritte in fretta, per chiudere un rilievo, senza il giro di rilettura che il
ciclo prevede.

---

## 8. Gli adempimenti di chiusura, eseguiti

- ✅ **Tabella di tracciamento**: **T146 e T161 chiuse**, **T5 e T6 riscritte** con l'esito nuovo, **nove righe nuove** — T159-T167. Integra a **167**.
- ✅ **CSV `matrice_corpus_v1.csv`**: **55 righe** file × fatto per il lotto 3D.
- ✅ **`# CHIUSO il 24/08/2026`** in testa all'elenco del lotto.
- ✅ **Canone accresciuto** in sezione datata: **dieci divergenze** (F1-F10), di cui una non scrivibile per intero e una che è una **prova di solidità**.
- ✅ **`alias_entita.md`**: quattro righe di **classe A**, due di **classe C** — e le due di classe C sono **sigle di procedura**, non nomi propri: è la prima volta.
- ✅ **`registro_emendamenti.md`**: nessun emendamento nuovo da questo lotto.
- ✅ **Nota-sessione** nel journal, e **solo dopo** il blocco dei conteggi (E34).
- ✅ **Misure di chiusura** dopo l'ultima scrittura, ognuna con la sua ora (E44).

---

## 9. Che cosa il lotto lascia al gate

| | |
|---|---|
| **1. La metà di E59 che in apertura non si può fare, alla chiusura si fa** | La prova B è inapplicabile quando il lotto porta lui la fonte del dominio. **A lotto chiuso è applicabile, e il dominio la supera su tutte e nove le espressioni.** Non è un emendamento che questo lotto propone: è un'osservazione con un consuntivo |
| **2. Una correzione che AGGIUNGE UNA FONTE cambia il perimetro di verità della nota intera** | E61 dice di rileggere la **frase nuova**. ⚠️ **Tre casi di questo lotto mostrano il verso opposto**: aggiungere una fonte ha reso **false** frasi che c'erano già. **La rilettura va fatta anche all'indietro, quando è il perimetro a muoversi** |
| **3. Lo SLUG è una superficie, e nessun controllo la guarda** | Il nome del file ha continuato ad affermare «a voce» dopo che titolo, summary e corpo erano stati corretti. **Si scrive prima del titolo e non si corregge mai**; la QA non lo legge come affermazione, **ma il giudice lo vede** |
| **4. E39 va cercata anche FRA le note, non solo dentro** | La cautela apposta a una nota non è arrivata alla sorella che ripeteva la stessa affermazione |
| **5. Un obbligo del canone lo può verificare solo chi ha il canone** | D4 chiedeva a 3D di aggiungere una riga a una nota, e non era stato fatto: **né la QA né il giudice potevano prenderlo**, per costruzione |
| **6. Il contrario della sovra-atomizzazione, per il secondo lotto di fila** | Due paragrafi numerati di un prescrittivo **senza nessuna nota**, uno dei quali conteneva la **definizione di reclamo chiuso** |
| **7. Il debito che resta** | **T159** (obbligo esplicito per 3E), **T160**, **T162**, **T163-T167**: otto righe aperte dichiarate. E **R2**, il lotto di manutenzione che nasce con lo spezzamento |
| **8. `PRO-QA-11` compare in un file su 160** | E il documento che governa il ritiro **ne usa un altro**. È la divergenza più profonda del lotto, e per metà non è scrivibile finché 3E non apre |
