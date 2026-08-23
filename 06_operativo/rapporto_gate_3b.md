# Rapporto del gate del lotto 3B — E59-E61, il censimento delle copie e delle superfici

> **Che cos'è** · L'esito del gate del lotto 3B, eseguito il 23/08/2026 su
> `06_operativo\prompt\prompt_gate_3b_lotto_3d.txt`. Contiene ciò che il prompt del gate
> chiede al §2.3: **l'elenco delle sostituzioni** del censimento delle copie di stato e
> **l'elenco dei difetti piantati nuovi**.
> **Chi lo legge** · Il coordinatore. Le regole che ne nascono vivono in `metodo_03`, non qui.
> **Misure** · tutte da script, ognuna con la sua ora (E44), prese fra le **23:20 e le 23:23**
> del 23/08/2026.

---

## 1. Le decisioni del gate, in una tabella

| Punto del §7 di `rapporto_lotto_03b.md` | Decisione | Dove vive adesso |
|---|---|---|
| **1.** la correzione è una scrittura | ✅ **E61**, e assorbe la vigilanza di §6 | `metodo_03` §9.5 passo 5 · registro |
| **2.** il 36,4 % regge? | ✅ **regge**, con la storia dichiarata e senza rimisurarlo (E41). Ma il dato vero è un altro → **E59** | `metodo_03` §9.5 passo 5-ter · **T148 chiusa** |
| **3.** ci sono altre copie di stato? | ✅ **censite tutte**, due specie e due cure → §3 di questo rapporto | `verifica_copie_stato.py` · §4.49 |
| **4.** E2 è il passo fatto peggio | ✅ **E60**: artefatto d'apertura e passo pre-giudizio | `metodo_03` §5.1-bis e §9.5 passo 2-bis |
| **5.** `MOD-HR-11` (T149) | ✅ **ratificato**: obbligo esplicito per il lotto del corso sicurezza | **T149 resta tracciata** |
| **6.** il barrato nel canone (T157) | ✅ **scritta**, in sezione datata — ⛔ **con un'errata sul conteggio** | `canone_aurora.md` §6 · **T157 chiusa** |
| **7.** il debito verso 3D, 8 e il corso sicurezza | ✅ **T146, T147, T149, T156 restano dove il tracciamento le ha messe** | matrice, tabella di tracciamento |

---

## 2. ⛔ LA SESTA CORREZIONE AL COORDINATORE, E VIENE DAL PROMPT DI QUESTO GATE

Il prompt del gate scrive, al §2.6: *«tre grezzi lo portano»*, parlando del barrato. La riga
**T157**, scritta dal lotto 3B, dice la stessa cosa e nomina i tre.

**Misurato sul corpus il 23/08/2026 con `estrazione_cantiere.testo_cantiere` su tutti i 160
grezzi** — cioè con lo strumento che E48 ha costruito apposta:

| | |
|---|---|
| grezzi che portano almeno un passaggio barrato | **11** |
| passaggi barrati in tutto | **40** |
| di quegli 11, già canonizzati | **6** |

**I tre nominati da T157** — la politica, la scheda allergeni, il contratto frigo — **erano i
tre che la revisione aveva davanti.** Gli altri otto: `IO-05`, `PRO-QA-08`, il brief
dell'agenzia packaging (**otto** passaggi), la job description del responsabile di produzione,
la lettera a Tosano (**nove**, il massimo del corpus), la nota del commercialista, il materiale
d'aula allergeni, il verbale di CdA sul tunnel.

⚠️ **Non è un dettaglio di conteggio: è la specie che il progetto ha appena finito di
normare.** Un'affermazione il cui soggetto è **l'archivio**, verificata sul **sottoinsieme che
l'ha suggerita**, è E47 — e il suo test operativo è E57, deciso al gate precedente. **La riga
del canone porta il numero contato** (E49), e T157 si chiude **con l'errata dentro**, perché
una riga di tracciamento che si corregge in silenzio è una riga che non insegna niente.

⚠️ **È anche la seconda volta in due gate che un numero composto a mano dal coordinatore
arriva sbagliato**, dopo i «lotti chiusi». Non è una coincidenza: **sono gli unici due numeri
di questo gate che nessuno script produceva.**

---

## 3. IL CENSIMENTO DELLE COPIE DI STATO (§2.3a) — l'elenco delle sostituzioni

**Perimetro: tutti i 38 script** di `06_operativo\`, `06_operativo\qa\` e
`06_operativo\qa\_collaudo\`, cercando liste e valori scritti a mano che duplicano stato
ricavabile da una fonte.

### 3.1 Il censimento ha trovato DUE SPECIE, e si curano in modo opposto

| Specie | Che cos'è | Cura | Quante |
|---|---|---|---|
| **stato derivabile** | un elenco, un conteggio, un percorso il cui padrone cambia da solo | la copia **si cancella**, lo strumento **legge dal padrone** | **3** (più le 2 già riparate il 22-23/08) |
| **vocabolario chiuso del manuale** | aree, prefissi, `type`, cartelle | la copia **resta e si CONFRONTA** col padrone, da script | **4** |
| **copia deliberata** | l'`assert` sulle 160 voci del manifest | **resta**: è un allarme, non una fonte | **1** |
| **curatela dichiarata** | `elenco_fonti_prescrittive.FONTI`, `candidate_r1.DOMINI` | **resta**: è un giudizio scritto (E56), non uno stato ricavabile | **2** |

⚠️ **Perché la seconda specie non è diventata una lettura a runtime**, ed è la sola decisione
del censimento che si discosta dalla lettera dell'ordine: far leggere a `qa_comune` un manuale
in prosa a ogni lancio manderebbe **rossa tutta la suite** il giorno in cui qualcuno riformatta
un titolo — un controllo che si rompe per una ragione estranea a ciò che controlla viene
disattivato, e §4.35 dice già che quello è il difetto prevedibile. **Ma una copia non
controllata mente in silenzio, sempre** (§4.47). La copia resta dove serve e **uno script la
confronta col padrone**: il fatto ha un padrone solo, e la copia non può più divergere senza
che qualcosa diventi rosso.

### 3.2 L'ELENCO DELLE SOSTITUZIONI

| # | Dove | La copia | Il padrone, adesso | Che cosa diceva di sbagliato |
|---|---|---|---|---|
| **1** | `ricalibra_budget.CHIUSI` | i **lotti chiusi** e i loro consuntivi, scritti a mano | gli elenchi in `qa\lotti\` (marcatori) **+ il vault** per le note | **ferma al 19/08**: diceva **quattro** lotti chiusi, cinque lotti dopo |
| **2** | `ricalibra_budget.RESTANTI` | i **lotti restanti** con le loro **fasce** | gli elenchi ancora aperti; le fasce **non esistono più** (E31) | copiava numeri di un padrone **morto**, e il tema 3 vi compariva ancora come un lotto solo |
| **3** | `verifica_matrice_lotti` | *(assente)*: il conteggio dei lotti chiusi **non esisteva** e si faceva a mano nei prompt | i marcatori `# CHIUSO`, stampati come **«lotti chiusi: N»** | **«undici» invece di dieci**, nella §3 del passaggio di consegne |
| *(4)* | `verifica_dominio.CANONIZZATI` | i lotti canonizzati, lista a mano | *(già riparata il 23/08, lotto 3B)* | un nome morto dal 20/08, tre lotti chiusi mancanti |
| *(5)* | `qa_link_integrity` | il perimetro dei wikilink rotti | *(già riparata il 23/08, lotto 3B)* | `related` fuori: **due link rotti col vault a zero errori** |

### 3.3 ⚠️ IL CASO PEGGIORE ERA IL PIÙ SILENZIOSO

`ricalibra_budget.py` teneva **due** tabelle a mano e **nessuno lo lanciava**. È la forma
peggiore della malattia di §4.47: **uno strumento che non mente mai a voce alta perché non
parla mai**, e che al primo rilancio avrebbe dato numeri di cinque lotti fa con l'aria di darli
di oggi. I due controlli riparati il 22-23/08 almeno **giravano**, ed è per questo che qualcuno
li ha presi.

**Riscritto**: legge i lotti dai marcatori, le note dal vault, e **dichiara lo scarto che il
conteggio porta con sé** — «note che citano un grezzo del lotto» non è «note che il lotto ha
prodotto», e una nota estesa da un lotto successivo (E32) viene contata in entrambi. **Lo
scarto è misurato: 133 note su 512 appartengono a più di un lotto chiuso**, e il numero si
stampa invece di essere aggiustato (E46 — un numero dice su che cosa è misurato).

### 3.4 ⚠️ E IL PRIMO CONTEGGIO NUOVO ERA GIÀ SBAGLIATO, SCRITTO LO STESSO GIORNO

Il riconoscimento del marcatore faceva `startswith("MANUTENZIONE")` sulla riga di commento
ripulita, e l'elenco del lotto **1B** — un lotto di **canonizzazione** — risultava di
manutenzione, per via di una riga che va a capo su «*manutenzione* mai firmato».

⚠️ **Un conteggio nato per togliere l'aritmetica dalle mani di qualcuno ha sbagliato alla prima
misura, e per la stessa ragione che stava riparando**: un riscontro **debole** preso per forte
— che è E56, le due classi di forza, applicate a un marcatore invece che a una sigla. Da qui
il collaudo `collaudo_lotti_chiusi.py`, coi difetti piantati **nei due versi**.

### 3.5 Nove byte di controllo, e stavano proprio dove il progetto discute `\b`

La passata ha trovato **nove occorrenze del byte `0x08`** (backspace) in sei file: sono i punti
in cui un autore ha scritto `` `\bformazion` `` o `` il `\b` in coda alla sigla `` e l'editor ha
mangiato la sequenza. **Nessuna è dentro una regex viva** — la più vicina è in un commento di
`verifica_dominio.py` — ma **è l'espressione su cui poggia tutto il §1.4 del rapporto 3B**, e
chi la copiasse da lì otterrebbe un'espressione diversa da quella misurata. Riparate tutte e
nove, senza toccare i fine riga dei file.

---

## 4. IL CENSIMENTO DELLE SUPERFICI (§2.3b) — e ha trovato il buco più vecchio della suite

**Metodo**: per ogni controllo, l'elenco delle superfici che **dichiara** di coprire, contro le
superfici che il collaudo **esercita con un difetto piantato**. Le superfici non si sono
dedotte dal codice: si sono **sondate**, piantando un'affermazione inventata in ciascuna e
guardando se il controllo scattava.

### 4.1 L'esito della sonda su `qa_provenance`, prima del fix

| Superficie | Difetto piantato | Il controllo |
|---|---|---|
| corpo | numero inventato | **SCATTA** |
| cella di tabella nel corpo | numero inventato | **SCATTA** |
| H1 del corpo | numero inventato | **SCATTA** |
| **campo `title`** *(con H1 pulito)* | numero inventato | ⛔ **TACE** |
| **campo `summary`** | numero, data, codice inventati | ⛔ **TACE** |
| glossa nel blocco `## Fonti` | numero inventato | **TACE** *(e va bene: vedi §4.4)* |

### 4.2 ⚠️ PERCHÉ È IL BUCO PIÙ VECCHIO, E PERCHÉ NESSUNO L'AVEVA TROVATO

**Cinque emendamenti dichiarano l'intestazione portante**, e nessuno dei cinque aveva uno
strato deterministico dietro:

| | |
|---|---|
| **E18** | se la nota stabilisce una regola decisionale, **il `summary` la enuncia** |
| **E30** | `title` e `summary` si rileggono **come note a sé**, a ogni giro — nel lotto 1C, al terzo giro, **sei rilievi su sette** stavano lì col corpo già corretto |
| **E39 · E42** | la cautela si propaga a `summary`, `title`, celle, glosse — **nello stesso turno** |
| **E51** | una nota non può essere smentita dalla propria intestazione |
| **E61** *(oggi)* | la frase nuova scritta correggendo si verifica come una di prima stesura |

⚠️ **La ragione per cui il buco è durato tanto è la sua forma, ed è la parte che diventa
giurisprudenza (§4.49): `qa_provenance` e `metodo_03` §7.1 CONCORDAVANO.** Entrambi dicevano
«dal corpo della nota». **Non c'era nessuna divergenza da trovare fra codice e manuale**: la
lacuna stava fra **due dichiarazioni del progetto che nessuno aveva mai messo una accanto
all'altra** — «l'intestazione è portante» ed «il controllo guarda il corpo». **Un difetto che
non è una contraddizione non si trova rileggendo: si trova facendo l'elenco.**

### 4.3 Il fix, e che cosa ha trovato nel vault

Lo strato deterministico di `qa_provenance` estrae adesso le affermazioni **dal corpo più
`title` e `summary`**, con un'affermazione già presente nel corpo verificata **una volta sola**.

| Misura sul vault | Prima | Dopo |
|---|---|---|
| errori di provenance | 0 | **0** |
| avvisi di provenance | 79 | **91** |
| di cui **debiti dell'intestazione** | — | **+14** |
| di cui **falsi positivi rimossi** | — | **−2** |

⚠️ **I quattordici sono debito vero, e quasi tutti della stessa specie: date scritte con l'anno
dove la fonte non lo scrive.** `fatto-fermo-forno-ft-01-05-05` dichiara `05/05/2026` nel titolo
e nel summary; il quaderno OCR che ne è la fonte scrive **`5/5`**, e l'anno non compare in
nessuna delle sue pagine. **Il corpo era corretto** — scrive «martedì 5 maggio», nella grafia
della fonte (E24). **È E30 alla lettera: il corpo si corregge, l'intestazione resta.**

⚠️ **I due falsi positivi rimossi provano che il fix non ha allargato niente, ha visto di
più.** Erano due avvisi «rumore nel payload»: `entita-elena-marchetti` con
`MOD-QA-31_reclamo_REC-2026-011.pdf` e `entita-ivano-dal-maso` con la mail della valvola azoto.
**Quelle due fonti agganciano un'affermazione della nota — che vive nel summary.** Il controllo
le dichiarava inutili perché non guardava dove la nota le usava.

⚠️ **Il pregresso resta debito, non diventa rosso** (§4.35, come per E43): ERRORE per le note
nate dal **23/08/2026**, **AVVISO dichiarato** per le altre, con la coda «debito anteriore alla
superficie dell'intestazione». **Le quattordici occorrenze hanno il loro nome e il loro conto
in T158**, e entrano nella rete finale.

### 4.4 Le superfici che restano fuori, e sono decisioni

| Superficie | Fuori perché |
|---|---|
| i **numeri del locator** nel blocco `## Fonti` | `riga 12`, `§3`, `pag. 4` sono **coordinate**, non affermazioni sul mondo: verificarle come fatti fabbricherebbe un rilievo su ogni nota corretta. Che il locator punti davvero lì lo controlla il suo controllo |
| il **corpo degli hub** nella reciprocità hub/spoke | un hub elenca i propri spoke **nel corpo**: è la convenzione di E11, non una dimenticanza |

**Ora sono scritte in `metodo_03` §7.1**, dove prima non c'erano: una superficie esclusa per
decisione e una esclusa per dimenticanza si somigliano troppo, finché nessuno le distingue.

### 4.5 La superficie ESERCITATA e non DICHIARATA — il verso opposto

Il fix di `related` del 23/08 ha allargato il grafo dei wikilink, ma **`metodo_03` §7.2
continuava a descrivere il grafo del solo corpo** — «da ogni nota, i wikilink uscenti del suo
CORPO» — per due giorni, pseudocodice compreso. ⚠️ **È E30 applicato a un manuale invece che a
una nota**: il controllo si corregge, la sua dichiarazione resta com'era. Riparata, e §7.2
porta adesso **la tabella delle proprie superfici**, una per una, con chi le esercita.

---

## 5. I DIFETTI PIANTATI NUOVI

| Collaudo | Casi | Il difetto piantato | Il controllo di non-scatto |
|---|---|---|---|
| **`collaudo_intestazione.py`** | **8** | numero, codice e data inventati **solo** in `title`/`summary` | intestazione **riscontrata** (tace) · **valore derivato marcato** E23 (tace) · nota **anteriore** al 23/08 (avviso, **non** errore) · stesso numero nel corpo e nell'intestazione (**un rilievo solo**) |
| **`collaudo_lotti_chiusi.py`** | **8** | prosa che va a capo su «**manutenzione** mai firmato» · prosa che va a capo su «**chiuso** il contratto» | le due grafie vere di `# CHIUSO` · `# MANUTENZIONE` da solo e con la coda · elenco senza marcatori · **il conteggio stampato contro gli elenchi veri** |
| **`collaudo_copie_stato.py`** | **5** | una voce **in più** nella copia · una voce **in meno** · ⚠️ **il padrone che non si legge** | il censimento com'è oggi · i quattro padroni non vuoti |

⚠️ **Il caso che conta di più è il terzo difetto di `collaudo_copie_stato`: il padrone che non
si legge non deve assolvere.** Un controllo di **confronto** muore così — non rompendosi, ma
confrontando contro l'insieme vuoto, che è verde per costruzione. È il difetto **muto** di
`verifica_dominio.py`, dove `\b` scartava in silenzio ogni sigla del corpus: **uno script che
tace non è uno script che assolve.**

⚠️ **`collaudo_intestazione` chiama `qa_provenance.controlla`**, cioè la via che la produzione
usa, non una copia della sua logica: è §4.29, e va detto perché **due dei collaudi esistenti
rifanno il pezzo di codice che vogliono provare** invece di chiamarlo. Non è stato cambiato
oggi — non è il lavoro di questo gate — ma è la prossima cosa da guardare in quella famiglia.

---

## 6. I NUMERI DI CHIUSURA (E44), tutti da script e con l'ora

**Misure fra le 23:20 e le 23:23 del 23/08/2026.** ⚠️ **Questo gate non ha toccato nessuna
nota**: il vault è identico a quello con cui 3B ha chiuso, e le uniche differenze sono negli
strumenti e nei registri.

| Misura | Valore | Strumento | Ora |
|---|---|---|---|
| **QA, perimetro vault** | **111 ERRORI, 298 AVVISI** — esito **ROSSO** | `qa_all.py` | 23:20 |
| di cui grezzi non ancora canonizzati | **109** | | |
| di cui aree senza hub | **2** — `ricerca-sviluppo`, `sicurezza-ambiente` | | |
| di cui **rilievi di merito** | **0** | | |
| ⚠️ avvisi: **286 → 298** | **+14** debiti dell'intestazione, **−2** falsi positivi | | |
| **Collaudi** | **10 su 10** — i tre nuovi sono `intestazione` (8 casi), `lotti_chiusi` (8), `copie_stato` (5) | `_collaudo\` | 23:19 |
| **Emendamenti** | registro e manuale **concordano a 61** | `verifica_emendamenti.py` | 23:23 |
| **Copie di stato** | **4 su 4 concordi col padrone** | `verifica_copie_stato.py` | 23:23 |
| **Matrice** | completa e disgiunta: **160 grezzi, 27 elenchi** | `verifica_matrice_lotti.py` | 23:23 |
| **lotti chiusi** | **10** — 9 di canonizzazione + 1 di manutenzione, **pilota escluso** | `verifica_matrice_lotti.py` | 23:23 |
| **Tracciamento** | **158 righe**, da T1 a T158 — 7 riconciliate · 73 aperte dichiarate · **19 chiuse** · 59 tracciate | `conta_tracciamento.py` | 23:23 |
| **Vault** | **386 note**, di cui **350 di contenuto** | `conta_stato.py` | 23:23 |
| **Grezzi canonizzati** | **51 su 160** — ne restano **109** | `conta_stato.py` | 23:23 |

---

## 7. Che cosa questo gate lascia aperto

| | |
|---|---|
| **1. E61 non ha ancora un consuntivo** | Dice *che cosa* fare e non ha un appiglio meccanico. ⚠️ **Se al terzo giro del prossimo lotto ricompaiono rilievi su frasi introdotte dalle correzioni, il difetto non è più l'assenza della regola: è che la regola non si applica da sola**, e servirà un appiglio come quelli che E59 ed E60 hanno dato a E56 e a E2 |
| **2. E60 chiede uno SCRIPT che non esiste ancora** | L'artefatto delle **grandezze condivise** in apertura è prescritto da E60 e dal prompt dei lotti. **Va costruito prima di aprire 3D**, che è il primo lotto che deve usarlo |
| **3. Il censimento non si accorge di una copia NUOVA** | `verifica_copie_stato.py` conosce quattro copie perché quattro ne ha trovate il censimento, e **nessuno script può accorgersi di una copia che una persona scrive domani**. La vigilanza che resta non è «quante ce ne sono» ma **«quando ne nasce una, chi la aggiunge al censimento»**: da chiedere a ogni gate che tocchi uno strumento |
| **4. Due collaudi rifanno la logica invece di chiamarla** | `collaudo_related_rotto` e parte di `collaudo_suite` reimplementano il controllo che provano. **È §4.29 al contrario** — una via equivalente invece della via di produzione — e va guardato, non oggi |
| **5. I 14 debiti dell'intestazione** | **T158**, aperta dichiarata. Entrano nella rete finale o nel lotto che tocca ciascuna nota |
| **6. Il debito verso 3D, 8 e il corso sicurezza** | **T146, T147, T149, T156**: quattro righe con obbligo esplicito, tutte confermate dal gate |
