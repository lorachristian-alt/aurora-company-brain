# Passaggio di consegne — il ruolo di coordinatore

> **Cos'è** · Il documento che permette a una NUOVA chat di coordinamento (Cowork) di
> riprendere il progetto senza perdere nulla di ciò che è stato deciso, e soprattutto
> senza perdere i CRITERI con cui è stato deciso.
> **Perché esiste** · Il repository conserva le decisioni; questo file conserva la
> giurisprudenza — il modo di giudicare che nei documenti non è scritto perché viveva
> nella conversazione.
> **Data** · **24/08/2026, sera — dopo il GATE del lotto 3E, che lo ha APPROVATO.** Ne escono
> **E64** — *il rimando nomina, non asserisce* — e **quattro estensioni** dentro E39, E41, E60 ed
> E61: il manuale è a **64**. ⚠️ **E la REVISIONE DELLA CAPACITÀ è ESEGUITA**: la fascia 25-35 è
> **confermata come grandezza di progetto**, e la vigilanza si sposta sulla densità del gruppo
> post-revisione e sulla costanza dei tre giri. ⚠️ **Il gate ha anche riconciliato un numero che
> il rapporto di 3E dichiarava senza l'ora del primo termine** — gli avvisi non salgono «da 425 a
> 426»: **il 425 non è mai stato misurato**, e il passaggio vero è **369 → 426**.
> Prima, nella stessa giornata: la **chiusura del lotto 3E**, che si è spezzato in apertura per la
> soglia di E28 e ha lasciato il tema 3 da chiudere a **3F**; e il **gate del lotto 3D**, da cui
> E62, E63 e quattro estensioni.
> ⚠️ **Il 21/08, al gate finale del lotto 2B — il primo gate del progetto che non produce
> emendamenti nuovi** — il manuale era a 46.
> Prima, nella stessa giornata, il completamento del ciclo e la chiusura del lotto 2B — l'autocontrollo analitico, il
> primo lotto che **si è spezzato in apertura prima di scrivere una riga** e il primo che
> **chiude una riga di tracciamento con un dato** invece che con una decisione. Prima, il
> 20/08, il **GATE del lotto 2A**, che lo ha APPROVATO e ha prodotto **E41-E44** — quattro
> emendamenti da un solo gate, il massimo finora. Prima ancora, il 19/08, la **chiusura del
> lotto 2A** — il lavaggio CIP, primo lotto
> del tema 2 e primo **esperimento** del metodo. Prima, nella stessa giornata, il **GATE del
> lotto R1**, che lo ha APPROVATO. Nella stessa giornata, e sono occasioni diverse: il gate
> del lotto 1C (commit `eb8f035`), la sessione di manutenzione che ne è seguita, il **gate
> intermedio** che l'ha autorizzata a finire, il gate di merito di R1 e la chiusura di 2A.
> ⚠️ L'intestazione diceva ancora «dopo la chiusura del lotto
> 1B (commit `d54ffb3`)» mentre il file conteneva già la giurisprudenza del gate 1C: è la
> data del documento, e sbagliata fa credere vecchio ciò che è nuovo.

---

## 1. Il modello operativo (non cambiarlo)

- **La chat Cowork è il cervello**: strategia, revisione ai gate, scrittura dei prompt.
  Non esegue mai le sessioni operative e non scrive nel vault.
- **Il terminale (Claude Code) è le mani**: ogni sessione si apre in una cartella precisa
  e incolla un prompt preciso. La cartella del TERMINALE è il perimetro.
- **Antigravity / VS è la plancia**: l'IDE si apre dove serve, l'agente nativo dell'IDE
  resta spettatore.
- Il titolare (Christian) fa da ponte: incolla i prompt nel terminale e riporta in chat
  ciò che il terminale risponde. Il coordinatore risponde con **quale opzione scegliere**
  e con **il testo esatto da incollare** (di solito nel campo note, tasto `n`).
- Ogni sessione operativa chiude con **cinque gesti**: stato, decision log, **questo
  file** (§8), commit, `git push`. Nei lotti si aggiunge lo **zip del vault** fuori dal
  repository.

---

## 2. Dove sta la verità (ordine di lettura per la nuova chat)

Repository: `C:\Users\buulo\Desktop\.eval_do_not_index\Aurora_Food_Group_SRL`
(remote privato `github.com/lorachristian-alt/aurora-company-brain`, pubblico solo in S7).
Vault Obsidian: `C:\Users\buulo\Desktop\aurora-cervello` (fuori dal repo, NON sotto git
per decisione del titolare: ci andrà a fine progetto, prima del corpus v2).

| Ordine | File | Cosa dà |
|---|---|---|
| 1 | `00_INIZIA_QUI.md` | mappa, modello operativo, regole d'oro, glossario |
| 2 | `06_operativo/scaletta_end_to_end.md` | le sessioni S0-S7, i principi, gli stop-loss |
| 3 | `06_operativo/decision_log.md` | ogni decisione, datata, col motivo |
| 4 | `01_metodo/metodo_03_canonizzazione.md` | il manuale supremo della canonizzazione, **con tutti gli emendamenti già dentro** |
| 4-bis | `06_operativo/registro_emendamenti.md` | l'indice genealogico degli emendamenti: chi li ha approvati, quando, dove vivono. ⚠️ **Il numero non si scrive qui**, e le due copie che stavano su questa riga e su quella sopra erano ferme a **44** da tre giorni: lo dà `verifica_emendamenti.py`, che controlla anche che ogni riga punti a una sezione esistente e che ogni marcatore del manuale abbia la sua riga |
| 5 | `06_operativo/matrice_lotti_corpus_v1.md` | il piano dei lotti + registro modifiche + tabella di tracciamento. ⚠️ **Non sono più 12**: i temi 3-10 si ripacchettizzano in apertura (E31), e il conto degli elenchi lo dà `verifica_matrice_lotti.py` |
| 6 | gli stati: canonizzazione e RAG di produzione | dove siamo, due linee di lavoro, due file |
| 7 | `06_operativo/rapporto_gate_s2.md`, `rapporto_gate_s3.md`, `rapporto_lotto_1a.md`, `rapporto_lotto_1b*` | la storia dei gate |
| 8 | `01_metodo/metodo_02_misurazione.md` (+ addendum) e i verbali in `04_misurazioni/` | i numeri e come sono stati fatti |

**Regola**: se questo file e i documenti divergono, vincono i documenti. Questo file non
crea regole: spiega come si sono applicate.

---

## 3. Dove siamo (31/08/2026 — dopo il lotto **R2**: il tema 3 è chiuso, E65 è in vigore)

- **Corpus v1 congelato**: 160 file, manifest SHA-256 v1.1. Intoccabile.
- **Baseline misurate sul grezzo**, stesse 282 domande:
  A (agentico, opus-5) 70,6% · B (RAG semplice, Chroma) 44,7% · C (RAG produzione locale,
  3B su hardware minimo) 14,5% complessivo **e 7,6% sulle 251 rispondibili** — i due
  numeri **non si citano mai separati**.
- **Config C congelata** (`d36d7ce`, impronta `afb58939…`): intoccabile fino a fine S6.

### Canonizzazione: DODICI lotti di canonizzazione chiusi, DUE di manutenzione, il TEMA 3 È CHIUSO

⚠️ **Questo numero non si conta: si INCOLLA**, da `verifica_matrice_lotti.py`. **Vale anche per
il coordinatore.**

```
lotti chiusi: 14
   di cui di canonizzazione ... 12 (lotto_01a_linea1_turno_ccp, lotto_01b_freddo_energia,
                                    lotto_01c_metrologia_gas, lotto_02a_cip,
                                    lotto_02b_autocontrollo_analitico, lotto_02b_bis_allergeni,
                                    lotto_03a_riesame_direzione, lotto_03b_politica_formazione,
                                    lotto_03c_certificazione_audit, lotto_03d_reclami,
                                    lotto_03e_crisi_ritiro, lotto_03f_controllo_pubblico_ats)
   di cui di manutenzione ..... 2 (r1_riconciliazione_verticale,
                                  r2_reclami_verticale)
   elenchi ancora aperti ...... 19
   FUORI dal conteggio: la fetta pilota (22 grezzi), anteriore alla matrice e
                        senza marcatore `# CHIUSO`. Canonizzata in S2.
```

⚠️ **I «19 elenchi aperti» comprendono i pacchetti di giudizio** (`giudizio_*`), che portano zero
grezzi: **i lotti veri ancora aperti sono undici**, e sono tutti di canonizzazione — `R2` è
chiuso.

✅ **IL TEMA 3 È CHIUSO, e lo ha chiuso `3F`.** Sei lotti, tredici grezzi: `3A` riesame della
direzione (2), `3B` politica e formazione (2), `3C` certificazione e audit (4), `3D` reclami
(3), `3E` crisi e ritiro (1), `3F` controllo pubblico ATS (1). ⚠️ **Il tema era stato
ripacchettato in cinque ed è finito in sei**: a cambiarlo è stata la conta dei fatti in
apertura di 3E — 62 sui due grezzi, sopra il tetto dei quaranta di E28 — e il gate di 3E ne ha
tratto **§4.50**: una pianificazione scritta in un prompt porta il condizionale della misura.

⚠️ **R2 copre DUE domini**, `reclami` e `ritiro`, e la decisione è misurata: E37 è scattato anche
su 3E (35 riaperte contro 30-35 nuove), e **14 delle 35 stavano già nel perimetro di R2**. **R2
è il PROSSIMO ATTO dopo il gate di 3F**, col perimetro rigenerato da entrambi i domini — e **senza `\bPRO-QA-11\b`
fra le espressioni del dominio `ritiro`**, salvo prova nuova (recepimento del gate, scritto in
testa all'elenco di R2).

**56 grezzi su 160, ne restano 104.**

### La serie dei due tassi (E41/E46): DIECI punti

| Lotto | Dominio | Difetto di produzione |
|---|---|---|
| R1 | perimetro CCP e tarature | **57,7 %** |
| 2A | `cip` | **3,3 %** |
| 2B | `acqua` | **0,0 %** su 27 |
| 2B-bis | `allergeni` | **9,1 %** su 33 |
| 3A | — | ⚠️ **NON MISURATO** |
| 3C | `certificazione` | **38,7 %** su 31 — con riserva |
| 3B | `formazione` | **36,4 %** su 22 — con riserva |
| 3D | `reclami` | **20,0 %** su 35 — primo punto collaudato, **riserva SCIOLTA al gate** |
| **3E** | **`ritiro`** | **0,0 %** su 30 — ⚠️ **DEGENERE: lotto mono-fonte sulla fonte del dominio** |
| **3F** | **`cip`** | **8,3 %** su 36 — ⚠️ **tre casi residui, tutti enumerazioni**, dichiarati e non aggiustati |

⚠️ **Il punto di 3E ENTRA nella serie, e porta la dicitura accanto — è E41 esteso al gate.** Il
lotto ha **un grezzo solo**, e quel grezzo **è la fonte del dominio**: ogni nota nata lo cita per
costruzione, quindi **nessuna può risultare scoperta**. **Il numero è vero e il suo potere
discriminante è nullo.** Entra perché la serie fotografa **le misure come sono state prese**
(stessa disciplina del 38,7 % di 3C); porta la dicitura perché **uno `0,0 %` nudo si legge come
un successo del metodo**, e lì il metodo non è stato messo alla prova.

✅ **E su `3F` la dichiarazione degenere NON si è scritta, perché il conto non la conferma.**
3F è mono-fonte, ma E41 esteso dichiara degenere il lotto mono-fonte **il cui unico grezzo è la
fonte che governa il dominio** — e la notifica ATS **non è una fonte prescrittiva del corpus**
(`elenco_fonti_prescrittive.py`). ⚠️ **È §4.50 applicato a una REGOLA invece che a una
pianificazione**: il condizionale del prompt del gate è ciò che ha impedito una dichiarazione
falsa in apertura.

⚠️ **Il dominio `cip` è stato ristretto prima di misurare**: `pulizi` e `\bigien` sono state
respinte dalla prova B di E59 (quota fuori 0,57 e 0,71). **Il punto 2A — 3,3 % — NON si
rimisura**: la serie fotografa le misure come sono state prese.

⚠️ **Questa tabella è il PADRONE della serie.** La copia che viveva in `metodo_03` §9.5 si era
fermata a **tre punti su nove** ed è stata tolta al gate di 3E: il manuale porta **la forma** del
punto, i punti stanno qui. È la seconda malattia della famiglia di **T39** — l'indice che resta
indietro.

### Il metodo: **65 emendamenti**, e le cinque voci di 3F tutte decise

✅ **IL GATE DEL LOTTO 3F HA PRODOTTO E65 E TRE ESTENSIONI**, applicate a `metodo_03` e al
registro nello stesso turno. `verifica_emendamenti.py`: **registro e manuale concordano a
65**.

| | |
|---|---|
| **E65** | **un'affermazione vale nel perimetro delle fonti che la nota cita, e per uscirne serve un artefatto o un rimando** — §9.5, passo 5 |
| **E10** esteso | **la proprietà del delimitatore vale per OGNI delimitatore della catena**: grezzo, note, fonti del pacchetto, e ogni delimitatore futuro |
| **E50** esteso | **il derivato è derivato qualunque sia il genere** — e il fix dell'esenzione è stato fatto **subito**, con il collaudo |
| **E57** esteso | **il superlativo con soggetto-elenco porta IL CONTO**: «tre su dieci (contate)», non «l'unica» |

**Come sono state decise le cinque voci del §10 di 3F:**

| | Voce | Decisione del gate |
|---|---|---|
| **1** | il secondo delimitatore | ✅ **E10 ESTESO**. Il fix era già fatto; il gate ne ratifica **la forma in ogni parte** — il prefisso che un grezzo non scrive, la guardia che confronta i **caratteri** e non la presenza, e **la PREMESSA nel collaudo**, che impedisce al caso di passare per il motivo sbagliato |
| **2** | la data derivata | ✅ **E50 ESTESO, e il fix fatto SUBITO** — è di perimetro di un controllo (§4). Difetti piantati nei due versi, non-scatto di regressione sul numero, **confronto riga per riga sul fuori perimetro: 116 righe prima, 116 dopo, zero differenze**. Poi la data del **26/05 è RIENTRATA** nel corpo della nota con la marca. **Lo slug resta**: «il mattino dopo» non afferma il falso, e un rinomino senza necessità è churn |
| **3** | il superlativo sull'elenco | ✅ **ACCOLTA DENTRO E65** — ma **con la sua regola operativa che resta**, come **E57 esteso**: il gesto concreto chiude la porta specifica da cui la specie è entrata tre volte |
| **4** | l'unità della misura dei due tassi | ⛔ **LO STRUMENTO NON SI TOCCA.** I tre residui dichiarati col loro nome **sono** la forma giusta: cambiare unità a numeri visti romperebbe la comparabilità della serie (§4.45) e sarebbe un fix che allenta (§4.9). **Criterio pre-registrato in §6** |
| **5** | il perimetro dell'affermazione | ✅ **E65 NASCE, ED È IL CAPPELLO.** E47, E3/E43, E57 ed E64 restano le porte delle loro specie: E65 non le sostituisce, **le contiene** — e dà per la prima volta una regola alla **regola generale importata** e al **nesso causale**, le due specie senza porta deterministica |

⚠️ **La ragione per cui E65 non è una regola in più ma una regola SOPRA**: ogni emendamento
della famiglia chiudeva una porta e la classe entrava dall'altra. **Ora la classe ha il suo
nome sopra la porta**, e le due specie che nessun controllo deterministico può vedere — non
hanno numeri, superlativi o negazioni — hanno finalmente una regola di scrittura.

⚠️ **Il gate del lotto 3E aveva prodotto E64 e quattro estensioni**, tutte applicate nello
stesso turno in cui sono state scritte:

| | |
|---|---|
| **E64** | **il rimando nomina, non asserisce** — §4.2, richiamato nel passo 2-bis di §9.5 |
| **E41** esteso | **il punto degenere si dichiara**, e non si inventa un dominio artificiale per ottenere un numero utile |
| **E39** esteso (2ª volta) | **gli hub sono superfici della ricerca**: chi corregge uno spoke apre gli hub che lo linkano |
| **E60** esteso | **l'accostamento per evento**: le grandezze condivise non bastano |
| **E61** esteso (2ª volta) | **la frase nuova porta il suo riscontro nel turno** — fonte e locator, come una riga B |

### ⚠️ LA CAPACITÀ 25-35 È CONFERMATA, e la vigilanza si sposta

**La revisione a dieci lotti, rinviata dal gate di 3D, è ESEGUITA** (§6, riga del 24/08/2026).
La fascia è **una grandezza di progetto** — serve al taglio dei pacchetti in apertura — e a
spezzare restano i **tetti duri di E28**. ⚠️ **Non si sostituisce la fascia con un'altra fascia**:
la densità va da **7,0 a 25,5**, cioè ciò che si mantiene costante è **il lotto**, e ricalibrare
ripeterebbe l'errore che E31 ha già corretto. ⚠️ **La domanda vera era «che cosa consuma il
rischio, le note o i giri?», e la risposta è che non sono le note**: tre giri in **sette** lotti su
dieci. Si guardano ora **la densità del gruppo post-revisione** e **la costanza dei tre giri**.

### I conteggi, incollati da `conta_stato.py` (25/08/2026 alle 09:21)

<!-- CONTEGGI DEL VAULT — generati da `06_operativo\qa\conta_stato.py` il 2026-08-25.
     Si incollano VERBATIM: non si ricompongono a mano, non si riscrivono in prosa. -->

| Grandezza | Valore |
|---|---|
| Note nel vault | **507** |
| di cui `_index` | 11 |
| di cui note-strumento del progetto | 15 |
| di cui note di diario (`sessione`, `daily`) | 13 |
| **di cui note di contenuto** | **468** |
| Note per cartella | areas 285 · docs 71 · data 56 · entities 34 · projects 18 · code 16 · workspace 16 · concepts 7 · self 2 · outputs 1 · sources 1 |
| Note per `type` | atomica 363 · conflitto 73 · entita 26 · hub 15 · sessione 13 · index 11 · concetto 6 |
| Questioni aperte (`type: conflitto`) | 73 |
| Grezzi in `sources\` | 160 |
| Grezzi citati da almeno una nota | **56** |
| Grezzi restanti | **104** |

⚠️ **Il lotto 3F si è lavorato il 24/08 e si è chiuso il mattino del 25**: il marcatore
dell'elenco porta la data del lavoro, **le misure portano la data e l'ora in cui sono state
prese**, che è l'unica cosa che E44 chiede. ⚠️ **Il vault è cresciuto di 37 note e di un
grezzo citato**: 470 → 507, 55 → 56.

### Le altre misure di chiusura, ognuna con la sua ora (E44)

| Misura | Valore | Quando |
|---|---|---|
⚠️ **Tutte del 25/08/2026**, il mattino dopo la lavorazione.

| Misura | Valore | Quando |
|---|---|---|
| **Emendamenti** | registro e manuale **concordano a 65** — E65 e le tre estensioni del gate | 31/08, 18:05 |
| **Copie di stato** | **ogni copia concorda col suo padrone** | 09:29 |
| **Matrice** | completa e disgiunta — **160 grezzi, 33 elenchi**, guasti 0 | 09:19 |
| **lotti chiusi** | **13** — 12 di canonizzazione + 1 di manutenzione, pilota escluso | 09:19 |
| **Tracciamento** | **186 righe**, da T1 a T186 — 7 riconciliate · 95 aperte dichiarate · 23 chiuse · 61 tracciate | 09:20 |
| **Perimetro del lotto 3F** | **36 nate + 11 toccate = 47 controllate**, QA **0 errori, 44 avvisi** | 09:21 |
| **Vault** | **507 note**, di cui **468 di contenuto** · **56/160** grezzi | 09:21 |
| **Collaudi** | **12 su 12** · `collaudo_suite` **18 difetti su 18 e 9 non-scatto su 9**, su tutte e cinque le vie | 09:28 |
| **QA a perimetro vault** | **106 ERRORI, 444 avvisi** — gli errori sono i **104 grezzi non canonizzati** più 2 aree senza hub, **0 rilievi di merito** | 09:29 |

⚠️ **Il dodicesimo collaudo è nuovo**: `collaudo_taglio_fonti.py`, nato dal guasto del
delimitatore riparato durante il lotto — cinque casi, **due difetti piantati** e una premessa.

### ⛔ IL 425 NON È MAI ESISTITO — un confronto riconciliato dal gate

Il rapporto di 3E scrive che *«gli avvisi salgono da 425 a 426»*. **Il 425 non compare in nessuna
misura del progetto.** Le tre misure del vault del 24/08, lette dai `qa_all.md` versionati:

| Quando | Errori | Avvisi | Note | Commit |
|---|---|---|---|---|
| chiusura del lotto **3D** | 108 | **344** | 432 | `12a41aa` |
| **gate 3D**, 13:27 | 108 | **369** | 432 | `beb91f0` |
| chiusura del lotto **3E**, 15:17 | 107 | **426** | 470 | `babc743` |

**Il passaggio vero è 369 → 426, cioè +57**: **+35** link integrity (30 «lontana dall'`_index`»,
3 hub `lotto-l…`, 2 `progetto-gestione-reclamo-…`) · **+16** frontmatter (14 summary oltre il
tetto, 2 con più di una frase, 1 corpo 301-350, −1 assenza riparata) · **+6** provenance (5
`summary`/`title` sotto soglia, 1 fonte che non aggancia). ⚠️ **Zero rilievi di merito in tutte e
tre le misure**: cambia il numero dichiarato, non il merito del lotto. **Ma «+1» diceva che il
lotto non aveva mosso il vault, e il lotto lo ha mosso di cinquantasette** — §5.

### ⚠️ Che cosa questa sessione ha prodotto, in una tabella

| | |
|---|---|
| ✅ **Il gate di 3D** | **E62** e **E63**, più **quattro estensioni** dentro E30, E39, E59 ed E61 |
| ⛔ **E3 pagato la SESTA e la SETTIMA volta, lo stesso giorno** | Il controllo di E43 esteso alla classe `assenza` ha preso **quattro casi in flagranza** sulle note di 3D, e **due affermazioni erano FALSE**. Pregresso **25 note**: **T169** |
| ⛔ **Il lotto 3E si è spezzato, e il tema chiude con 3F** | 62 fatti contati, oltre il tetto di E28 |
| ⛔ **Cinque righe B da un accostamento solo** | Il perimetro del blocco contro il mass balance dello stesso pomeriggio: **T171-T175**. ⚠️ **Il vault aveva entrambe le gambe da agosto**, ed è **il terzo lotto di fila** in cui la E2 vera l'ha fatta il revisore — da cui **E60 esteso** |
| ✅ **Il gate di 3E** | **E64** e **quattro estensioni**; **la capacità confermata**; il **425 riconciliato**; **due refusi riparati** (due puntatori a un file che non esiste, uno dei quali era un byte di controllo dentro un documento) |
| ⚠️ **Due criteri pre-registrati chiusi in due giorni senza aspettare l'esperimento** | E61 il 23/08, E64 il 24/08. **In entrambi i casi le osservazioni erano già plurime quando il criterio fu scritto**, quindi non è §4.43. ⚠️ **Ma è la seconda volta di fila**, e vale la pena guardarla: un criterio pre-registrato che viene chiuso al gate successivo per «osservazioni già sufficienti» è un criterio che **non andava scritto in quella forma** |
| ✅ **Il lotto 3F, e il TEMA 3 CHIUSO** | **36 note nate, 11 toccate, 47 controllate**, QA **0 errori**; **undici righe nuove**, T176-T186, e **T51 chiusa**. **Nessun emendamento nuovo** |
| ⛔ **Un guasto della suite trovato PRIMA di giudicare, non dopo** | Il delimitatore delle fonti del pacchetto di giudizio compariva **dentro il grezzo**: la fonte principale arrivava al giudice **troncata a 638 caratteri su 13.186**, e la guardia diceva «completa». **E10 sul secondo delimitatore.** Riparato in corsa, con difetto piantato — e il pacchetto rifatto **ha cambiato il verdetto** |
| ⛔ **Una divergenza vera NON è entrata in vault** | La sua seconda gamba è il grezzo di `lotto_07_persone`: **divieto 9-bis**, si traccia invece di usarla — **T184**. ⚠️ **A fermarla è stato `verifica_matrice_lotti.py`, non una lettura**: la QA era verde e la nota era corretta. ⚠️ **La regola aveva sei giorni** (lotto 1B, T18 e T39) **e nessuno strato l'ha richiamata** |
| ⛔ **E26 ha chiesto il pattern, al terzo giro** | **Il perimetro dell'affermazione eccede il perimetro delle fonti**: sei occorrenze, sei specie — primato sull'archivio, assenza sull'archivio, regola generale importata, nesso causale, due estensioni su un elenco. **E47, E3/E43 ed E57 ne governano tre; la classe non ha regola** |
| ✅ **Il gate di 3F** | **E65** — il cappello del perimetro dell'affermazione — e **tre estensioni** dentro E10, E50 ed E57. ⚠️ **L'esenzione della data derivata riparata SUBITO**, con difetti piantati nei due versi e il confronto riga per riga sul fuori perimetro: **116 righe prima, 116 dopo, zero differenze**. ⚠️ **La voce 4 respinta**: lo strumento dei due tassi non si tocca, e la decisione ha un **criterio pre-registrato** in §6 |
| ⚠️ **Uno strumento che dava zero, e due lotti che non se n'erano accorti** | `conta_perimetro_lotto.py` dichiarava «note nate: 0» su 3E e 3F, perché i due elenchi scrivevano il separatore in una forma che il parser non cerca. ⚠️ **3E non se n'era accorto perché aveva composto i numeri a mano**, che è esattamente ciò che l'intestazione dello strumento vieta. **Riparati i dati, non lo strumento** |

### PROSSIMO ATTO: il GATE di `R2`, e poi il ripacchettamento del TEMA 4

✅ **`R2` è chiuso**, e il suo rapporto è `06_operativo\rapporto_lotto_r2.md`. ⚠️ **Porta
tre cose strutturali e sei righe che aspettano di essere scritte**, e per §4 del prompt dei
lotti va letto PRIMA di approvare.

| | Che cosa aspetta il gate |
|---|---|
| **1** | ⛔ **L'estrazione di cantiere mette le tabelle del `.docx` IN CODA al documento**, non nel punto in cui stanno — e R2 ci è cascato dentro, scrivendo un'affermazione falsa che la tabella smentiva. **T195, tracciata e non riparata**: tocca l'estrattore |
| **2** | ⚠️ **Il tetto delle 350 parole non ha margine in un lotto di manutenzione**: otto correzioni su ventuno lo hanno superato al primo tentativo, il margine più stretto era di **cinque parole**. La domanda è se la manutenzione debba stare sotto lo stesso tetto |
| **3** | ⚠️ **La riconciliazione verticale VA RIFATTA A FINE CORSA**: il tasso è **20,6 %**, e il perimetro **cresce più in fretta di quanto lo si sani** — 2 note uscite contro 23 entrate |
| **4** | ⛔ **Sei divergenze nuove tracciate e NON scritte in vault** — **T187-T194** — fra cui **due scale che assegnano il ritiro a classi diverse** (risponde a F8 del lotto 3D) e il **secondo codice della procedura dei reclami** (`PRO-QA-13`, gemella di F1). Il gate decide se aprire un lotto per scriverle |

**Poi il ripacchettamento del TEMA 4 in apertura (E31)**, al gate di R2 e non prima.

<!-- ciò che segue è il piano con cui R2 è stato eseguito, tenuto come verbale -->

I punti che lo distinguevano da un lotto di canonizzazione:

| | |
|---|---|
| **perimetro** | **RIGENERATO, non ereditato**: `candidate_r1.py --dominio reclami` e `--dominio ritiro`, coi domini nello stato in cui i gate li hanno lasciati — **senza `\bPRO-QA-11\b`** (respinta dalla prova B al gate di 3E, salvo prova nuova) e senza le espressioni espunte da 3F |
| **elenco** | `qa\lotti\r2_reclami_verticale_note.txt`, con l'elenco dei grezzi **vuoto** e `# MANUTENZIONE` in testa |
| **il numero che il progetto aspetta da tre lotti** | la **differenza** rispetto alle **65 + 35** note degli spezzamenti: misura quanto 3D, 3E e 3F hanno già sanato |
| **i censimenti** | le occorrenze di **T142** (superlativi), **T158** (intestazioni) e **T169** (assenze) che cadono nel perimetro **si riparano qui**, col conto dichiarato: «censite nel perimetro: N, riparate: M» |
| **i tre numeri del §3-bis** | note guardate, note corrette, **tasso di difetto** — che qui è il tasso di **riapertura** dei due domini, quello che gli spezzamenti hanno rimandato a R2 |
| **capacità** | **nessuna**: R2 vale UN lotto nel ritmo e resta **fuori dalla serie della capacità** (E38). Sopra le 30 note nuove valgono comunque le soglie di E28 |

⚠️ **E65 ed E64 sono in vigore dal primo turno**, con E61 e le sue due estensioni, E39 sugli
hub, l'estrazione di cantiere per i grezzi. **Le correzioni sono scritture**: il perimetro E32
si tiene **mentre** si lavora, non a memoria a fine lotto.

⚠️ **DOPO R2 viene il ripacchettamento del TEMA 4** in apertura (E31) — al gate di R2, non
prima.

## 4. La giurisprudenza — i criteri con cui si giudica ai gate

⚠️ **I numeri sono permanenti, l'ordine è di servizio** (§4.26, 19/08/2026). Queste regole si
citano per numero — «§4.18», «§4.25» — dentro e fuori da questo file. Riordinare l'elenco è
lecito e utile; **rinumerarlo no**, perché romperebbe ogni citazione esistente. Il 19/08/2026
le voci 22-25 sono state rimesse in ordine fisico tenendo ciascuna il proprio numero.

Sono i principi che hanno deciso i casi difficili. Riusarli è ciò che rende il progetto
coerente.

1. **Nessun numero senza script.** Vale anche per i totali dello stato e dei rapporti:
   si incolla l'output di `conta_stato.py`, non si ricompongono somme in prosa. (Nato da
   due sviste di conteggio a mano.)
2. **Congelato di misura ≠ attrezzatura di cantiere.** Intoccabili senza appello: P1, P3,
   config C — ciò che produce il confronto prima/dopo. Evolvono con versione dichiarata,
   solo a confine di lotto e solo in avanti: metodo_03, suite QA, prompt di giudizio
   (oggi `PROMPT_GIUDIZIO_V2`).
3. **Le esenzioni si danno per CLASSE, mai per cartella.** Le note-strumento del progetto
   (prefisso `script-` in `code\`) sono esenti da `fonti`, dallo strato di giudizio e
   dalla componente unica; le note di contenuto della stessa cartella no. La classe è
   definita una volta sola e le regole la citano.
4. **Le note non traslocano mai.** L'area si assegna sull'area che governa i fatti OGGI,
   non su un assetto futuro. Un hub d'area non nasce vuoto per comodità di archiviazione.
5. **Si spezza lungo le cuciture, mai attraverso le storie.** Un lotto si divide dove non
   si rompe una riconciliazione (E21: fatti contati prima di scrivere; la soglia è quella
   di E28, vedi 20).
6. **Il budget non comanda sul contenuto.** Un budget rispettato tagliando fatti è peggio
   di uno sforato e dichiarato.
7. **Una divergenza con una sola gamba canonizzata non si scrive in nessuna nota** (E25):
   vive solo nella tabella di tracciamento. È la causa radice delle due sole fughe di
   canone del progetto.
8. **Un'assenza affermata è un fatto**: si verifica su tutto `sources\`, si data e si
   riferisce al manifest (E3). Errore pagato due volte (PRP-09 nel pilota, ossigeno
   residuo in 1A).
9. **I fix agli strumenti devono essere monotoni o collaudati.** Un fix che AGGIUNGE
   agganci si accetta; un fix che ALLENTA un controllo si accetta solo con perimetro
   chiuso e un difetto piantato nuovo che dimostri che il buco non si apre.
10. **La testimonianza non si riscrive.** Il testo di un giudice o di un rispondente resta
    com'è; le correzioni di interpretazione vivono nel rapporto e nel decision log.
11. **Un verbale di misura chiuso non si ritocca.** Ciò che cambia dopo va in appendice
    datata o in errata visibile.
12. **Chi genera, canonizza o risponde non apre mai `03_valutazione\`**; chi valuta è
    sempre una sessione diversa da chi ha risposto. Il perimetro si garantisce con la
    fisica (cartella del terminale), non con una clausola di prompt.
13. **Il canone guida, non appare**: mai citato come fonte, mai copiato nel vault. Le
    divergenze di categoria B si REGISTRANO nel canone in sezione datata — il canone si
    accresce, non si riscrive.
14. **Riconciliazione incrociata** (E2, poi §5.1-bis): non solo fra i grezzi del lotto,
    ma fra il lotto e ciò che il vault già sa. È la regola più redditizia: rende di più
    a ogni lotto che passa.
15. **Il ciclo di ri-giudizio ha una regola d'arresto** (E26): si ferma al primo giro con
    zero rilievi accolti, e comunque al terzo; se il terzo produce ancora rilievi, il
    lotto si chiude solo dopo che il rapporto ha NOMINATO il pattern che li rigenera.
16. **Ritmo**: massimo due lotti tematicamente contigui per sessione, mai tre — la
    revisione col canone si esegue a mente fresca. Il tetto è un massimo, non una quota.
17. **Onestà commerciale**: si vende la TRACCIABILITÀ, non la correttezza. Il determinismo
    si garantisce sul retrieval; i costi si dichiarano, mai «zero»; i numeri di C si
    citano sempre doppi e sempre come pavimento (hardware minimo).
18. **Un prompt già eseguito è un verbale, non uno strumento vivo**: documenta ciò che quella
    sessione ha fatto, e **non si riallinea alle regole venute dopo** — si data. È la stessa
    regola del verbale di misura chiuso (11) e della testimonianza del giudice (10), estesa
    ai prompt. I prompt **ancora in uso** sono invece strumenti vivi e si emendano.
    (19/08/2026, E27: `prompt_s2_pilota.txt` e `prompt_s3_config_c.txt` continuano a nominare
    i quattro gesti e restano così; `prompt_s4_lotti.txt`, che gira ancora, porta i cinque.)
19. **Una voce di decision log si sostituisce, non si cancella.** Il registro è cronologia,
    non fotografia: la voce superata resta a verbale, e quella nuova la supera dicendolo.
    (19/08/2026: la voce del 15/08 che istituì i quattro gesti è rimasta, superata da E27.)
    ⚠️ Vale per i **registri**; i documenti-fotografia — la §3 di questo file, `STATO`, i
    conteggi — si **riscrivono**, ed è la ragione per cui le due specie non convivono nello
    stesso file.
20. **Una soglia si mette sulla grandezza che il rischio consuma, non su una stima** (E28,
    19/08/2026). E21 spezzava un lotto sullo **scostamento percentuale** da un budget
    preventivato; ma ciò che il rischio consuma è il **carico di revisione**, e quello si
    misura in **note assolute**. Con le stime della matrice ferme a 2,1 note per grezzo e la
    densità misurata a 9,5, quella soglia sarebbe scattata a ogni lotto: **una regola che
    scatta sempre viene scavalcata per prassi, e allora non protegge più niente.** Ora si
    spezza sopra il +25 % **e** sopra le 30 note, sempre sopra le 40. ⚠️ Il criterio
    generale, che vale oltre questo caso: **quando una soglia scatta sempre, il difetto è
    nella grandezza che misura, non nel lavoro che segnala.**
21. **Una divergenza apparente che l'archivio scioglie è un RISULTATO, non un pareggio**
    (19/08/2026, lotto 1C). La tabella di tracciamento distingue tre esiti, non due:
    *chiusa* — la gamba è arrivata e la nota lo dice; *aperta dichiarata* — l'archivio non
    la chiude; e **riconciliata** — la contraddizione apparente sparisce perché una terza
    fonte la spiega. Il caso: il quaderno dice «bombola nordgas cambiata», la bolla dello
    stesso giorno consegna azoto sfuso, e l'inventario registra 18 bombole a scorta su una
    rampa di emergenza. ⚠️ Chi scrive una riconciliazione **dichiara l'inferenza**: che la
    bombola venisse da quella rampa nessuna fonte lo afferma.
22. **Chi estende una nota vecchia la fa uscire dal perimetro che la controlla**
    (19/08/2026, lotto 1C). La QA a perimetro di lotto guarda le note che citano i grezzi
    **del lotto**: due note estese in 1C — una data senza fonte, una nota oltre le 350
    parole — sono passate indenni e le ha prese solo la QA a perimetro vault, che non si
    lancia a ogni lotto. ⚠️ **Non è più un candidato: è E32**, in vigore in `metodo_03` §7 dal
    gate del lotto 1C. *(Riga aggiornata il 19/08/2026: diceva ancora «candidato emendamento».)*
23. **La fonte che PRESCRIVE non si cerca da sola: va cercata** (19/08/2026, lotto 1C).
    La riconciliazione incrociata funziona in orizzontale — si confrontano i documenti che
    *registrano* la stessa grandezza — e manca la verticale: il documento che **prescrive**
    come quella grandezza vada misurata. Nel lotto 1C **undici note** discutevano CCP,
    tarature e frequenze senza citare il **manuale HACCP**, e in quattro casi quel manuale
    conteneva esattamente ciò che la nota dichiarava mancante. ⚠️ **Regola operativa:** se una
    nota tocca un punto critico, una taratura, una frequenza di verifica o una responsabilità
    di processo, **il manuale HACCP si apre e si cita, o si dichiara perché non serve.**
24. **Quando un consuntivo smentisce una stima, non si sostituisce la stima con un'altra
    stima: si cambia la grandezza su cui si pianifica** (19/08/2026, gate 1C). La matrice
    pianificava sulla **densità** note/grezzo; i consuntivi l'hanno smentita quattro volte
    su quattro. La reazione giusta non era ricalcolare le fasce con una densità nuova — che
    avrebbe dato 903 note e 36 lotti — ma accorgersi che **l'invariante è il lotto** e
    pianificare su quello (E31). ⚠️ Il segnale che si sta sbagliando grandezza: la stima
    nuova è più assurda della vecchia.
25. **Un emendamento che corregge il PERIMETRO o l'ORDINE di un controllo si applica
    subito; si rimandano al gate solo quelli che cambiano il modo di scrivere le note**
    (19/08/2026, gate 1C). ⚠️ **Un controllo bacato non è un candidato: è un guasto.** E32
    ed E33 hanno lasciato passare quattro cose in un lotto solo — due difetti indenni per
    il perimetro, due rilievi sprecati su testo che non esisteva più — e accumularli per
    valutarne «l'effetto cumulato» significa solo far ereditare lo stesso buco ai lotti
    successivi. **Chi li applica pianta anche il difetto nel collaudo**, o il buco si
    riapre in silenzio.
26. **I numeri sono permanenti, l'ordine è di servizio** (19/08/2026). Un elenco numerato che
    si riordina **non si rinumera**: le regole si citano per numero, e rinumerare rompe le
    citazioni di tutti i documenti che le richiamano — comprese quelle fuori da questo file,
    che nessuno può censire. L'ordine di un elenco è comodità di lettura; il numero è
    l'identificatore. (Caso: la §4 di questo stesso file, che dopo il gate 1C usciva
    20-21-24-25-23-22 ed è stata rimessa in ordine **tenendo ogni voce il suo numero**.)
27. **Un artefatto che ISTRUISCE una sessione non lo scrive la sessione** (19/08/2026). Il
    prompt riutilizzabile è del coordinatore: una sessione che riscrive le proprie istruzioni
    è il canonizzatore che si riscrive il manuale, ed è la stessa ragione per cui il giudice
    non riceve il canone. ⚠️ **Chi opera SEGNALA lo scostamento; chi istruisce lo COLMA** — e
    l'obbligo di segnalare va scritto dentro l'artefatto, o non scatta. (Caso:
    `prompt_s4_lotti.txt` è rimasto a **19 emendamenti su 35 per tre lotti**, cioè 1A, 1B e 1C
    hanno girato su regole che viaggiavano solo nel testo incollato di volta in volta: la
    stessa malattia che E27 aveva curato altrove.)
28. **Due fotografie dello stesso momento divergono sempre** (19/08/2026). Quando due
    documenti descrivono lo *stato di oggi*, uno dei due diventa un **puntatore**: si elimina
    la duplicazione, non si raddoppia la manutenzione. Non è una regola di stile — è
    aritmetica del lavoro: due copie richiedono due gesti a ogni chiusura, e il secondo è
    quello che si salta. (Caso: «Dove siamo adesso» di `00_INIZIA_QUI.md` diceva 138 grezzi
    restanti e «prossimo passo: Sessioni 4-5» quando i restanti erano 125 e il prossimo passo
    era R1, contro la §3 di questo file e i due file di stato.)
29. **Il collaudo esercita la VIA che la produzione usa, non una via equivalente**
    (19/08/2026). Un test che invoca i componenti direttamente mentre la produzione passa dal
    lanciatore verifica un percorso che nessuno percorre: i componenti risultano sani e resta
    scoperto **tutto ciò che sta FRA loro** — l'inoltro degli argomenti, i default, l'ordine
    di chiamata. ⚠️ **È la classe di difetto che nessun test di unità vede per costruzione**,
    perché non vive dentro nessuna unità. **Requisito operativo, non consiglio:** almeno un
    difetto piantato **per ogni via realmente in uso**, e **l'elenco delle vie sta scritto nel
    docstring del collaudo**, così la copertura si legge invece di presumerla. Un test che non
    si sa a quale via appartiene conta come copertura per sbaglio. (Caso: `qa_all.py` non
    inoltrava `--note-toccate` ai figli, e un collaudo che chiamava i figli direttamente — con
    il flag esplicito — non poteva vederlo. «7 difetti su 7» era vero e non provava ciò che
    sembrava provare.)
30. **Un GATE INTERMEDIO non approva un lotto: lo autorizza a finire** (19/08/2026, lotto R1).
    Specie nuova, e va chiamata per nome perché fra un anno «gate del lotto R1» e «gate
    intermedio del lotto R1» non sembrino la stessa occasione. Serve quando il ciclo di
    giudizio non è ancora girato e il coordinatore deve sbloccarlo **senza pronunciarsi sul
    merito**: fissa gli emendamenti che il lotto ha già dimostrato necessari, detta le guardie
    per la parte che resta, e rinvia il verdetto al rapporto finale. ⚠️ Ha anche mostrato come
    si respinge un candidato emendamento: **verificandolo nel codice**. La proposta di alzare
    il tetto delle 350 parole è caduta perché `parole_corpo` chiama `corpo_senza_fonti`, quindi
    la riga della fonte non era mai stata contata — le note erano cresciute di **prosa**.
31. **Un giudice che dichiara DEGRADATO il proprio ingresso, invece di emettere un verdetto,
    vale più di uno che emette** (19/08/2026, lotto R1). Lo script che ritagliava il pacchetto
    in fette scartava l'appendice col testo estratto delle fonti, e i due giudici di quel giro
    si sono trovati a confrontare le note **con sé stesse**. Se ne sono accorti **da soli** e
    si sono rifiutati di pronunciarsi: è la ragione per cui quel giro è costato **zero** invece
    di inquinare il lotto con verdetti costruiti sul nulla. ⚠️ **La conseguenza operativa, ed è
    il motivo per cui questa riga esiste: chi costruisce uno strato di giudizio gli lascia
    abbastanza contesto per ACCORGERSI che l'ingresso è degradato, e il prompt gli dice
    esplicitamente che dichiararlo è un ESITO LEGITTIMO.** Un giudice che può solo emettere un
    verdetto ne emetterebbe uno anche sul nulla — e quel verdetto sarebbe indistinguibile da
    uno vero. ⚠️ Il difetto stesso è la classe di §4.29 ricomparsa **lo stesso giorno** su un
    altro strumento: la mattina riparata sulla suite, il pomeriggio ritrovata sullo strumento
    di taglio. Il collaudo della via V3 ora pianta anche quel difetto.

32. **La formula che attesta una verifica non si scrive senza aver fatto la verifica**
    (19/08/2026, lotto 2A). E3 dà all'assenza una forma verificabile — «cercata su tutto
    `sources\`, manifest v1.1» — e in due note di questo lotto quella formula è comparsa
    **senza che la ricerca fosse stata fatta**: il registro dichiarato assente stava in dieci
    grezzi, e uno era già fra le fonti di quella nota. ⚠️ **Una formula di attestazione usata a
    vuoto è peggio del silenzio**, perché dà a un'affermazione falsa la forma di una
    verificata, e nessun controllo automatico può accorgersene: su un'assenza lo strato
    deterministico non ha niente da cercare. **Il criterio generale**: dove una regola prescrive
    una *forma* per attestare un *gesto*, la forma non va mai scritta prima del gesto — vale per
    E3 come per ogni futura formula di attestazione.
33. **Quando il canone sa un numero che il vault non può ancora scrivere, vince il vault e si
    apre una riga** (19/08/2026, lotto 2A). Il canone fissa il limite del risciacquo CIP a 536
    µS/cm e conta 18 cicli su 28 sopra soglia; il conteggio è esatto, ma quel limite presuppone
    un dato che sta in un grezzo di un lotto **non ancora canonizzato**. ⚠️ Le due tentazioni
    sono opposte e sbagliate entrambe: **scrivere il numero** è una fuga di canone della specie
    già pagata due volte; **tacere del limite** lascerebbe la nota a dichiarare verificabile ciò
    che non lo è. Si fa la terza cosa: la nota dichiara il criterio **non verificabile sulle
    proprie fonti**, e una riga di tracciamento porta l'obbligo al lotto che avrà la gamba.
34. **Un giudizio che non converge non chiede un altro giro: chiede di guardare il gesto che lo
    rigenera** (19/08/2026, lotto 2A). Tre giri hanno dato 12, 7 e 9 rilievi accolti, e i
    rilievi non erano gli stessi che tornavano — quelli corretti restavano corretti. ⚠️ **Ne
    nascevano di nuovi della stessa specie perché correggere significa riscrivere, e ogni
    riscrittura è una nuova occasione di commettere lo stesso genere di errore.** È la stessa
    meccanica del *contesto importato* di 1B, che E26 aveva già codificato come regola d'arresto:
    qui se ne vede la ragione, e conferma che il quarto giro sarebbe stato lavoro sprecato.
35. **Un controllo nuovo non rende rosso il pregresso: lo dichiara debito, e il debito si
    programma** (20/08/2026, gate 2A). Il controllo di E43 trovava **29 note anteriori alla
    regola** che attestano un'assenza senza artefatto. Renderle errore avrebbe messo il vault
    fuori norma su un difetto che nessuno poteva evitare quando quelle note sono nate, e
    avrebbe **bloccato ogni lotto futuro** dietro un lavoro di sanatoria. ⚠️ **Il difetto
    prevedibile non è che il controllo resti giallo: è che venga disattivato**, e una suite da
    cui si disattiva un controllo scomodo smette di essere creduta su tutti gli altri. Quindi:
    **errore per ciò che nasce dopo la regola, avviso dichiarato e misurabile per ciò che
    nasceva prima**, e il debito entra nella rete finale con un nome e un conto.
36. **Un controllo si stringe di passaggio, non si allarga** (20/08/2026, gate 2A). Il
    centoventiseiesimo errore del vault è un **falso positivo** del controllo delle doppie
    padrone, ed è dimostrabile. ⚠️ **Correggerlo era tecnicamente banale e non è stato fatto**,
    perché la correzione **allenta** un controllo: §4.9 impone per quei fix un perimetro chiuso
    e un difetto piantato nuovo. **Restringere un controllo dentro un gate che sta chiudendo
    altro è il modo in cui una suite perde potere senza che nessuno abbia deciso di
    toglierglielo** — e il rilievo resta rosso, visibile, con la sua diagnosi scritta, finché
    non ha il suo turno.
37. **La forma fisica del vault fa parte dell'oggetto che si misura** (20/08/2026, gate 2A). I
    fine riga sono il primo difetto del progetto che non riguarda il contenuto di una nota ma
    il suo supporto, ed erano stati corretti **a mano** il giorno prima. ⚠️ **Al primo lancio
    del controllo, 21 note ci erano già tornate**: ogni riscrittura ripristina il terminatore
    della piattaforma, e per un giorno intero nessuno se n'era accorto perché **nessuno script
    guardava**. Un difetto che l'occhio trova una volta e la seconda no non è raro: è
    invisibile. **Ciò che la Sessione 6 misurerà è il vault come file, non come idea.**
38. **Uno spezzamento si decide sul lavoro che il lotto deve fare, non sul numero di note**
    (20/08/2026, lotto 2B). La soglia di E28 dice *quando* spezzare; **non dice dove**. Il
    taglio è passato fra i registri che **misurano** e il sistema **prescrittivo** degli
    allergeni, e la ragione è che quest'ultimo **apre da solo un dominio di riconciliazione
    verticale**: ⚠️ **due riconciliazioni verticali in un lotto solo significano che nessuna
    delle due viene fatta per intero.** Un taglio che dividesse per dimensione — tre grezzi di
    qua, due di là — sarebbe stato aritmeticamente identico e metodologicamente sbagliato.
39. **Una riga di tracciamento si chiude con un dato, non con una decisione** (20/08/2026,
    lotto 2B, T72). Per un lotto intero il criterio del risciacquo CIP è rimasto dichiarato
    *non verificabile*, invece di essere stimato o taciuto. Quando il dato è arrivato, la nota
    vecchia è stata **riaperta e corretta**. ⚠️ **È il primo caso del progetto in cui la
    disciplina di E25 — non scrivere nulla di una divergenza con una gamba sola — mostra il suo
    ritorno**: aver taciuto è ciò che ha reso possibile scrivere adesso.
40. **Un numero che il rapporto dichiara deve dire anche su che cosa è stato misurato**
    (21/08/2026, lotto 2B). Il tasso di difetto di produzione dava **0,0 %** mentre il giudizio
    trovava due note scoperte rispetto a una fonte prescrittiva **di un altro dominio**. ⚠️ **Le
    due misure non si contraddicono: misurano cose diverse**, ma il nome del numero promette più
    di quanto misura. **Un indicatore va letto col suo denominatore accanto**, e quando il
    denominatore è un perimetro va scritto qual è.
41. **La specie d'errore che nasce dallo scrivere bene** (21/08/2026, lotto 2B). Il giudizio non
    converge in tre giri, e la specie nominata è **l'affermazione universale verificata sul
    sottoinsieme che l'ha suggerita**: «l'unico», «il più alto», «nessun altro». ⚠️ **Non è
    disattenzione:** chi scrive una nota ha letto a fondo **un** documento, e un superlativo
    sembra il riassunto di quella lettura — mentre è un **quantificatore** le cui condizioni di
    verità stanno fuori dal testo che si ha davanti. **Non si ripara citando una fonte in più:
    si ripara restringendo la frase al perimetro davvero guardato.**
42. **Un lotto che dichiara scoperto un proprio controllo vale più di uno che lo dà per fatto**
    (21/08/2026, lotto 2B). La revisione col canone non è stata eseguita, perché le guardie
    della sessione vietano di aprire `03_valutazione\` e **un subagente lanciato dalla sessione
    è la sessione**. ⚠️ **Fra lasciare un passo scoperto e contaminare il vault si è scelto il
    primo, che è reversibile**: le due sole fughe di canone del progetto sono nate da lì. È §4.31
    applicato a se stesso. ⚠️ **Ratificato al gate: la scelta era corretta, le premesse no** —
    il canone non vive in `03_valutazione\` e un subagente a contesto nuovo non è la sessione
    che ha scritto. **E45** lo chiarisce nel manuale, ed è lì che doveva stare.
43. **Un criterio pre-registrato si può rileggere a numeri visti solo a due condizioni**
    (21/08/2026, gate 2B). ⚠️ **Il caso è quello di §5.5 del rapporto 2B**, e senza una regola
    diventerebbe il precedente con cui truccare ogni criterio futuro: una vigilanza era stata
    parcheggiata con la sua condizione di scioglimento scritta **prima**, e al momento di
    applicarla la si è letta in un modo che la lettera non prevedeva. **Le due condizioni sono
    entrambe necessarie:**

    | | La condizione |
    |---|---|
    | **1** | la rilettura poggia su una distinzione che il progetto aveva **già consacrato per altra via e PRIMA** dell'esito — qui *debito contro produzione*, cioè **E41**, nata lo stesso giorno del criterio e per un'altra ragione |
    | **2** | il rapporto mostra **ENTRAMBE** le letture — quella alla lettera e quella applicata — **col loro esito**, così che chi legge veda che cosa si sarebbe deciso in ciascuna |

    ⚠️ **Se manca anche una sola delle due, vale la lettera.** Una distinzione inventata dopo
    l'esito non è una distinzione, è una scusa; e una rilettura che mostra un solo ramo non è
    una rilettura, è una conclusione.

    ⚠️ **E l'occorrenza a debito non sparisce**: l'unica ricomparsa della classe vecchia al terzo
    giro di 2B sta in una nota ereditata, e **si conta nel debito della rete finale** insieme
    alle 29 note di E43. Assolvere la produzione non condona il pregresso.

    *(Il prompt del gate la chiamava §4.38; quel numero era già occupato dalle cinque righe che
    la chiusura di 2B ha scritto la notte prima, e la riga prende il primo libero.)*

44. **Un ordine di gate che discende da una riga di registro eredita la provenienza di quella
    riga** (21/08/2026, gate del tema 3). Chi lo esegue **verifica la riga sulla fonte prima
    del ribaltamento**, e un ordine eseguito contro la fonte non è obbedienza: **è un errore
    importato dall'alto**.

    ⚠️ **Il caso: B3 e l'arbitrato CIP.** Il coordinatore ordinò di riformulare l'arbitrato del
    lotto 2A perché il canone lo dichiarava indebolito. **Ma B3 era essa stessa un caso E49** —
    una conclusione entrata nel canone senza riaprire il file. L'esecutore ha verificato prima
    di eseguire, trovato che §5.3 **confina il sanificante dentro l'`L3`** e che il log **non
    dichiara mai il tipo di lavaggio**, e ha **richiuso** l'arbitrato più preciso di prima: il
    tracciato è più severo **di entrambi** i prescrittivi.

    ⚠️ **Se l'ordine fosse stato eseguito alla lettera, un errore del canone sarebbe entrato nel
    vault CON LA FIRMA DEL GATE** — cioè con l'unica autorità che avrebbe potuto fermarlo.

    ⚠️ **Perché non è disobbedienza, ed è la parte che conta**: l'ordine non è stato ignorato,
    è stato **eseguito fino al punto in cui la fonte lo contraddiceva**, e la contraddizione è
    stata riportata al gate con le righe in mano. **La catena di comando regge; è la catena di
    provenienza a non poter essere scavalcata da nessuno dei due.**

45. **UN NUMERO GIA' MISURATO NON SI RIMISURA QUANDO LA REGOLA CHE LO PRODUCE CAMBIA**
    (23/08/2026, gate del lotto 3C). La serie fotografa le **dichiarazioni come sono state
    fatte**: il punto resta al suo posto, e accanto gli si scrive la riserva.

    ⚠️ **Il caso: il 38,7 % di 3C.** Il dominio `certificazione` era dichiarato troppo largo,
    E56 lo dice, e rimisurare avrebbe dato un numero più basso e più giusto. **Non si è fatto**,
    ed è la stessa ragione per cui il buco di 3A non si è retro-misurato: una serie i cui punti
    sono tutti prodotti con la regola dell'ultimo gate **non può più mostrare il proprio
    miglioramento**, ed è esattamente ciò che a S7 la serie deve dimostrare.

    ⚠️ **La forma generale**: quando un emendamento cambia **lo strumento di misura**, i punti
    vecchi si annotano, non si rifanno. Quando cambia **il modo di scrivere le note**, le note
    vecchie si riparano nel lotto che le tocca. **Due regimi diversi, e confonderli costa in
    entrambi i versi.**

46. **UN CRITERIO PRE-REGISTRATO PUÒ MISURARE BENE E GUARDARE NEL POSTO SBAGLIATO**
    (23/08/2026, gate del lotto 3C). È il primo criterio del progetto che si esercita e si
    chiude **senza discussione** — e proprio per questo vale la pena dire che cosa gli è
    sfuggito.

    ⚠️ **Il caso: il gruppo post-revisione di 3C.** Il criterio chiedeva se il tasso di rilievi
    del **gruppo** fosse ancora più del doppio di quello del ciclo: **0,0 % contro 3,9 %**, non ha
    scattato, E54 è bastato. **Il conto era giusto.** ⚠️ **Ma il difetto non stava nel gruppo:
    stava nelle DUE note nate DOPO il gruppo**, ai ritrovamenti del terzo giro, che il criterio
    non guardava perché guardava un tasso. **Giudicate al gate, sono risultate difettose
    entrambe.**

    ⚠️ **La lezione non è «scrivere criteri più larghi»**, che li renderebbe non falsificabili.
    È che **un criterio chiuso su una popolazione va riletto quando la popolazione cambia sotto
    di lui**: il gruppo di 3C è cresciuto **dopo** che il criterio era stato scritto, e nessuno
    ha rifatto la domanda sulla parte nuova. La risposta strutturale è **E58**, che non guarda
    tassi: guarda se **ogni singola nota** ha visto il giudizio almeno una volta.

---


47. **UNA COPIA DI STATO DENTRO UNO STRUMENTO SI DISALLINEA IN SILENZIO, E LO FA SEMPRE**
    (23/08/2026, lotto 3B). Se un dato ha un padrone, lo strumento lo **legge**; se lo
    **ricopia**, prima o poi mente.

    ⚠️ **Due casi in un giorno solo, e nessuno dei due trovato da uno script.**
    `verifica_dominio.py` teneva i lotti canonizzati in una **lista di nomi scritta a mano**:
    portava un nome morto dal 20/08 e non portava tre lotti chiusi, e **dichiarava non citabile
    un certificato canonizzato il giorno prima**. `qa_link_integrity.py` cercava i wikilink
    rotti **solo nel corpo**, e il vault ne portava **due con la QA a zero errori** — uno da un
    lotto precedente.

    ⚠️ **Nessuno dei due era una logica sbagliata: erano una COPIA e un PERIMETRO**, cioè le due
    forme in cui uno strumento smette di dire il vero senza rompersi. **Per §4 sono guasti, non
    candidati**, e si riparano subito col difetto piantato.

    ⚠️ **E la domanda che lasciano vale più dei due fix**: *quante altre copie di stato ci sono
    dentro la suite?* Un controllo che ricopia va cercato, non aspettato.

48. **LA CORREZIONE È UNA SCRITTURA, E NESSUNO LA GIUDICA COME TALE** (23/08/2026, terzo giro
    del lotto 3B). ⚠️ **Candidato emendamento, non ancora regola**: sta qui perché è il modo di
    decidere che il gate deve valutare.

    **Dei dodici rilievi del terzo giro, almeno sette cadono su frasi che al secondo non
    c'erano: le ha scritte la correzione.** Due forme:

    | Forma | Stato |
    |---|---|
    | la correzione attenua il corpo e **lascia indietro l'intestazione** | **già nota**: E30 più E51 |
    | ⚠️ **la frase scritta correggendo afferma essa stessa oltre le fonti** | **nuova** |

    ⚠️ **Il caso che la rende urgente**: «la foto decisiva non compare in nessuno dei due
    elenchi» era la correzione di una frase vaga, **e il §6 della fonte la elenca**. La
    correzione ha reso **falsa** una frase che prima era soltanto imprecisa.

    ⚠️ **Perché le regole che ci sono non bastano**: E30, E39, E42 ed E51 guardano tutte
    all'affermazione **vecchia** e a dove sopravvive. **Nessuna guarda alla frase nuova.** E la
    ragione per cui non basta «rileggere di più» è quella di E39: chi scrive la correzione **sta
    pensando al rilievo**, e la frase che scrive gli sembra la risposta al rilievo, non
    un'affermazione da verificare.

    ⚠️ **E si riproduce dentro le correzioni fatte per chiuderla**: nel ciclo dedicato di E58 la
    stessa forma è ricomparsa al primo e al secondo giro, ed è sparita solo al terzo — quando la
    verifica è stata fatta **delimitazione per delimitazione, cella per cella**.

49. **UN CONTROLLO COPRE LE SUPERFICI CHE IL SUO COLLAUDO ESERCITA, NON QUELLE CHE IL SUO
    DOCSTRING DICHIARA** (23/08/2026, gate del lotto 3B). È §4.29 esteso **dalle vie alle
    superfici**: là il collaudo esercitava una via equivalente invece della via di produzione,
    qui esercita una parte della superficie e la dichiarazione parla di tutta.

    ⚠️ **La forma del difetto è sempre la stessa, e ha due versi che si somigliano solo da
    lontano:**

    | Verso | Che cosa succede | Il caso |
    |---|---|---|
    | superficie **dichiarata e mai esercitata** | il controllo tace dove nessuno guarda, e il silenzio si legge come assoluzione | `qa_link_integrity` cercava i rotti nel solo corpo: **due link rotti nel vault con la QA a zero** |
    | superficie **esercitata e non dichiarata** | il manuale descrive un controllo più piccolo di quello che gira, e chi legge il manuale si fida della descrizione | dopo il fix, §7.2 continuava a dire «i wikilink uscenti del suo **CORPO**» per due giorni |

    ⚠️ **Il censimento che ne è nato ha trovato il buco più vecchio della suite, e non era
    `related`:** lo strato deterministico di `qa_provenance` non guardava **`title` e
    `summary`**. **Cinque emendamenti dichiarano l'intestazione portante** — E18, E30, E39,
    E42, E51 — e **nessuno dei cinque aveva uno strato deterministico dietro**: un numero, una
    data o un codice inventati lì passavano la QA a **verde**, e il vault ne portava
    **quattordici**.

    ⚠️ **La ragione per cui il buco è durato tanto è la sua forma, ed è quella che rende utile
    la regola:** `qa_provenance` e `metodo_03` §7.1 **concordavano** — entrambi dicevano «dal
    corpo della nota». **Non c'era nessuna divergenza da trovare fra codice e manuale**: la
    lacuna stava fra due dichiarazioni del progetto che nessuno aveva mai messo una accanto
    all'altra — «l'intestazione è portante» (E30) e «il controllo guarda il corpo» (§7.1).
    **Un difetto che non è una contraddizione non si trova rileggendo: si trova facendo
    l'elenco.**

    ⚠️ **E il conteggio dei lotti chiusi è la stessa specie a un altro piano**: viveva a mano
    nei prompt del coordinatore, ed è uscito «undici» dove i marcatori `# CHIUSO` erano
    **dieci**. Ora lo stampa `verifica_matrice_lotti.py` e la §3 lo **incolla**. ⚠️ **Il primo
    riconoscimento del marcatore, scritto lo stesso giorno, era già sbagliato**: `startswith`
    su una riga di prosa faceva risultare il lotto **1B** di manutenzione. **Un conteggio nato
    per togliere l'aritmetica dalle mani di qualcuno ha sbagliato alla prima misura**, ed è la
    ragione per cui anche lui ha il suo collaudo.

    **Operativamente, e vale da qui in poi:** chi tocca un controllo **elenca le superfici che
    dichiara di coprire** e le mette accanto a quelle che il collaudo esercita con un difetto
    piantato. Dove manca il difetto, si pianta; dove manca la dichiarazione, si scrive. Un
    docstring non è una prova di copertura: è un'intenzione.

50. **UNA PIANIFICAZIONE SCRITTA IN UN PROMPT PORTA IL CONDIZIONALE DELLA MISURA**
    (24/08/2026, gate del lotto 3E). Il prompt del gate precedente scriveva «la chiusura di 3E
    è la chiusura del tema 3»; la conta dei fatti in apertura ha dato **62 fatti**, il lotto si
    è spezzato, e **il tema chiude con 3F**.

    ⚠️ **NON è una settima correzione al coordinatore, e la distinzione è sostanziale.** Le sei
    correzioni contate finora riguardano affermazioni **che al momento in cui furono scritte
    erano verificabili e sbagliate**. Qui il conto di E21 **non esisteva ancora**: non c'era
    nulla da verificare, e la frase era una previsione ragionevole.

    ⚠️ **Ma la FORMA era sbagliata, e la forma è ciò che si corregge.** Una pianificazione si
    scrive col suo condizionale — « **ultimo pacchetto, salvo il conto di E21** » — perché
    **un'apertura può sempre smentire un piano, ed è fatta apposta per poterlo fare**. Una
    previsione scritta all'indicativo arriva alla sessione come un'istruzione, e chi la legge
    deve scegliere fra eseguire il piano e obbedire alla misura.

    ⚠️ **È E53 applicato a una pianificazione invece che a un dominio**: là «nessun dominio» non
    si accetta sulla parola di chi coordina e si verifica da script; qui «questo è l'ultimo
    lotto» non si accetta sulla parola e si verifica contando i fatti. **La stessa regola, un
    piano più su.**

    ⚠️ **E vale nei due sensi**: chi opera **non compensa a mano** un piano smentito — lo
    dichiara, spezza, e scrive nel registro della matrice che cosa è cambiato e perché. Il lotto
    3E l'ha fatto, ed è il motivo per cui la smentita è costata una riga di registro e non un
    lotto da rifare.

## 5. Errori già pagati — non ripeterli

| Errore | Lezione, ora scritta |
|---|---|
| `core.autocrlf` avrebbe riscritto i grezzi al checkout | `.gitattributes` con `* -text` prima del primo commit |
| Sessione S1 committò senza pushare | il push è l'**ultimo** gesto del rituale, sempre (quinto da E27) |
| Conteggi a mano sbagliati (46 vs 32; 105 vs 89) | `conta_stato.py`, output incollato verbatim |
| Nucleo del pilota contato 16 invece di 17 | gli elenchi si generano da script, mai a mano |
| Due fughe di canone, stesso movente | E25 |
| Assenza dichiarata senza cercare ovunque | E3 |
| Otto note nate dalle correzioni mai ri-giudicate | E9, poi E26 |
| `powercfg` cambiato per il run e non ripristinato | annotare i valori PRIMA, dichiarare ogni comando di sistema |
| Finestra del terminale chiusa durante un run | i runner girano staccati e riprendibili riga per riga |
| Pacchetto per il giudice generato PRIMA delle correzioni pre-giudizio | due rilievi su dodici su testo che non esisteva più: il pacchetto si genera **dopo** (1C) |
| Architettura inventata su un registro che non la dichiara | «la catena di riferibilità si chiude su `TS-REF`»: il registro dice `TS-005`, e nessuna riga mette `TS-REF` a monte di nulla (1C) |
| Undici note su CCP e tarature senza il manuale HACCP | la fonte che prescrive va cercata apposta: quattro di quelle note dichiaravano mancante ciò che il manuale contiene (1C) |
| Il `summary` corretto per ultimo, quando il corpo era già stato attenuato | title e summary si rileggono come note a sé **a ogni giro** di giudizio, non una volta sola (1C) |
| Blocco dei conteggi generato PRIMA della nota-sessione | 172 contro 173 nello stesso giorno, e la differenza era la nota di diario: il blocco è l'**ultimo** numero prodotto prima del commit (E34, 19/08/2026) |
| Il pacchetto per il giudizio tagliato in fette **senza le fonti** | i giudici confrontavano le note con sé stesse e hanno dichiarato da soli il verdetto **degradato**: il difetto stava fra generatore e giudice, non dentro nessuno dei due (§4.29, lotto R1) |
| Il manuale HACCP **ricopiato invece che linkato** in diciassette note | mentre si agganciavano le note alla fonte che le prescrive, il vault ha guadagnato copie della stessa prescrizione: **wikilink alla padrona più la fonte in `fonti`**, e si riscrive solo il minimo perché la nota regga da sola (lotto R1) |
| Il prompt riutilizzabile rimasto indietro di sedici emendamenti | 1A, 1B e 1C hanno girato con le regole nel testo incollato invece che nello strumento: chi opera **segnala** lo scostamento, chi istruisce lo **colma** (§4.27, 19/08/2026) |
| **Due assenze dichiarate con la formula di E3 senza aver fatto la ricerca** | il registro dato per assente stava in dieci grezzi, uno dei quali era già fonte di quella nota; il valore dato per ignoto stava nel piano di autocontrollo. Le ha trovate la **revisione col canone**, non la QA: su un'assenza lo strato deterministico non ha nulla da cercare (§4.32, lotto 2A) |
| **Una sostituzione di testo fallita in silenzio, e nessuno se ne è accorto** | una correzione del secondo giro non è andata a segno; la QA resta verde su una frase sbagliata che è ancora lì, e l'ha ripresa il giudice al giro dopo. **Chi corregge a programma verifica che la correzione sia entrata**, o la corregge due volte credendo di averla fatta una (lotto 2A) |
| **UN SUPERLATIVO SULL'ARCHIVIO, che nessuna nota può reggere** | quattro note del lotto 3C affermavano «è la sola parte dell'archivio in cui…», «è il solo documento dell'archivio a nominarla», «è il termine più stretto che questo archivio conosca», «è l'unico riscontro in archivio». ⚠️ **Nessuna fonte citata può reggere un'affermazione così, perché parla di ciò che l'archivio contiene ALTROVE** — e nessuna nota ha l'archivio fra le proprie fonti. ⚠️ **Ma la regola non è «niente superlativi»**: il terzo giro ne ha verificati **quattordici** e ne ha confermati **dieci**, tutti quelli il cui soggetto è **un documento citato**. **Il discrimine è il SOGGETTO, non la forma.** ⚠️ **È la stessa specie di E36, un gradino più su**: là l'affermazione eccedeva il documento, qui eccede il **perimetro**. ⚠️ **E uno dei quattro era una nota del lotto 1B**: la classe non è nata in 3C, ci è stata solo trovata. **Candidato emendamento, T142** |
| **Un'ESENZIONE dettata dall'alto, che nessuno poteva verificare** | il prompt del gate scriveva «E37 non scatta su 3A — né il verbale né il cruscotto sono fonti prescrittive». Era **formalmente corretto e sbagliato nel merito**: il verbale **cita** il criterio del mock recall e **lo cambia**, quindi il dominio c'era. ⚠️ **È il terzo caso in tre gate in cui un'affermazione del coordinatore era sbagliata nel merito, e il primo in cui l'esecutore non poteva contraddirla**: nei due precedenti — B3 e il multi-fonte — c'era un **ordine da verificare**; **un'esenzione non si presenta come un ordine**, si presenta come un lavoro che non c'è da fare. ⚠️ **Il costo è misurato: il quinto punto della serie dei due tassi.** La risposta strutturale è **E53** — il dominio si verifica **da script** in apertura, mai sulla parola di chi coordina |
| **Un conteggio mai fatto sulla fonte, creduto da quattro presidi in fila** | un «sei fasi» **contato da chi scriveva** ha attraversato il revisore col canone, il canone, una nota e una riga di tracciamento senza che nessuno riaprisse il file; la fonte diceva «5 fasi» sopra un elenco di **sei voci**, e lo scarto vero era un altro — la scheda **omette il prerisciacquo** e **include la sanificazione**. ⚠️ **Ognuno ha creduto a quello prima**: il conteggio *sembra* un atto di lettura ed *è* un atto di inferenza. Da qui **E49** — la riga B è una nota senza cartella — e la vigilanza del §6 sulle note |
| **Il pacchetto del giudizio generato prima della fine delle correzioni** | sei note su quaranta sono state modificate dopo la generazione del primo pacchetto: E33 dice che si genera **per ultimo**, e qui non lo è stato. Nessun rilievo è caduto su testo morto, ma la regola esiste per non doverlo verificare a posteriori (lotto 2A) || **Una guardia formulata male, e due lotti fermi** | ⚠️ **L'errore è del testo del coordinatore, non di chi lo leggeva.** I prompt portavano «`03_valutazione\` non si apre mai» **senza l'eccezione del revisore**, e il canone non vive lì: sta in `01_metodo\`. R1 si è fermato a chiedere l'autorizzazione, **2B si è fermato dichiarando il passo scoperto** e ha chiuso senza revisione col canone. **Due sessioni, lo stesso dubbio, e la risposta viveva solo nel testo incollato di un gate.** Riparato con **E45**, che lo scrive in `metodo_03` §9.5 passo 3 — cioè dove chi opera lo cerca. ⚠️ **La lezione è §7-bis.6: quando la stessa domanda ferma due sessioni, si emenda la fonte, non si risponde una terza volta.** |

| **DUE NOTE CHIUSE SENZA AVER MAI VISTO UN GIUDICE, e difettose entrambe** | le due note nate dai ritrovamenti del terzo giro di 3C hanno passato QA e controllo delle citazioni e sono uscite dal lotto con la regola d'arresto E26 invocata a copertura. ⚠️ **Giudicate al gate del 23/08, sono tornate `afferma_oltre` tutte e due**: una attribuiva all'ente conteggi che la sua unica fonte non riporta e diceva nel titolo «le chiude in una settimana» dove il registro porta sedici giorni; l'altra chiudeva con «l'archivio non scioglie». ⚠️ **La QA verifica la FORMA, il giudizio verifica che la nota non affermi oltre le proprie fonti**: nessuno dei due sostituisce l'altro, e una nota che ha visto solo il primo è una nota mai giudicata. Riparato con **E58** |
| **UN CONTEGGIO ATTRIBUITO A UNA FONTE CHE NON LO ENUNCIA — per la terza volta sulla stessa riga** | T126 diceva che «Aurora conta sedici in DUE documenti, il verbale e il registro», e il gate lo aveva ratificato come «due contatori veri, di due titolari diversi». ⚠️ **Il verbale non porta né «sedici» né «16»**: fissa la scadenza al 17/03, che del sedici è la premessa. ⚠️ **E il «quindici» non lo scrive nessuno: nessuna fonte dell'ente conta i giorni.** Il solo conteggio scritto in una fonte è il «16 gg» di `NC-2026-061`; l'altro numero è **aritmetica del vault**, e ora porta la marca `(contati)`. ⚠️ **La sostanza reggeva** — due termini diversi, due conti possibili — **ed è questo che l'ha resa invisibile a due revisioni**: la riga era vera nel merito e falsa su chi lo dicesse. È la classe di **E49** e di **E50**, e l'ha presa il **giudizio dedicato di E58**, non una rilettura |
| **UN CENSIMENTO CHE MESCOLAVA DUE REGIMI, e il numero era il doppio abbondante** | il primo giro di `censimento_superlativi.py` dava **42 note e 47 occorrenze**, e dentro c'erano gli esistenziali negativi — «nessun documento dell'archivio riporta X» — che sono **assenze dichiarate**, governate da **E3 ed E43** e verificabili con la ricerca e il suo artefatto. Le occorrenze scoperte davvero sono **9**. ⚠️ **Pubblicare 42 avrebbe ripetuto in piccolo l'errore del 38,7 %**: un numero vero, con un nome che promette più di quanto misura. ⚠️ **E la classificazione dipendeva dall'ORDINE delle parole** finché la finestra è rimasta la frase intera |

| **UN NOME PROPRIO INVENTATO IN UN WIKILINK, E LA QA CHE NON GUARDAVA DOVE STAVA** | `doc-scadenzario-formazione-2026` puntava a `[[entita-francesca-sartori]]`: la scheda si chiama **Federica**. ⚠️ **È lo stesso errore che la tabella alias registra per Vicentini**, e la QA dava **0 ERRORI** perché `Nota.wikilink()` legge il solo CORPO e `related` restava fuori. ⚠️ **Nel vault ce n'erano due, e il secondo stava lì da un lotto precedente**. **A trovarlo è stata la revisione col canone, non la suite** — e un nome che non esiste non richiede giudizio: richiede un confronto con un elenco |
| **IL PRIMO DOMINIO DICHIARATO SOTTO E56 È NATO SBAGLIATO, NELLO STESSO VERSO DI 3C** | l'espressione `\bformazion` riconosceva **la parola**, e con essa la struttura del registro, chi lo estrae e l'indicatore delle ore — mentre le fonti del dominio governano **l'obbligo di formare e registrare**. Tasso col primo taglio **63,6 %**, col secondo **36,4 %**. ⚠️ **La prova è per ESPRESSIONE, non per numero**: `\bformazion` da sola pescava tutte e quattordici le scoperte. ⚠️ **E ci si è fermati dopo UNA stretta**: continuare a restringere a numero visto sarebbe il trucco di E41 spostato di un piano (§4.43) |
| **UNA SOTTRAZIONE SBAGLIATA INTRODOTTA CORREGGENDO** | «52 meno due fa 51» in una nota riscritta per chiudere un rilievo: **fa cinquanta**, ed è il numero che gli altri due documenti dichiarano. ⚠️ **L'errore non era nella nota originale: l'ha portato la correzione**, ed è il caso più piccolo e più chiaro del pattern del §4.48 |
| **DUE NUMERI SCRITTI A MEMORIA DAL COORDINATORE, ED ERANO GLI UNICI DUE SBAGLIATI** | Al gate del lotto 3B: «undici lotti chiusi» quando erano dieci, e «tre grezzi» col barrato quando erano **undici, con 40 passaggi**. ⚠️ **Erano gli unici due numeri del gate che nessuno script produceva**, e sono usciti sbagliati entrambi. **LA REGOLA, da qui in avanti**: dove il numero è verificabile nel repo con uno strumento che esiste, il coordinatore **lo verifica prima di scriverlo — o non lo scrive, e ordina la misura**. ⚠️ I lotti chiusi si **incollano** da `verifica_matrice_lotti.py`, che dal 23/08 li stampa dai marcatori |
| **UNA COPIA DI STATO NELLA TESTATA DEL PROMPT DEL COORDINATORE, FERMA A VENTISEI EMENDAMENTI PRIMA** | `prompt_s4_lotti.txt` portava **due** righe di allineamento: quella in coda, che è il padrone dichiarato, e una **seconda riga in testata** ferma a «E35» — più tre numeri a mano nello stesso blocco, «trentacinque volte», «quattro lotti», «i 61 emendamenti». ⚠️ **Il controllo di scostamento che quel file prescrive confronta la riga IN CODA col registro: la testata non la guardava nessuno**, e chi apriva il prompt leggeva per primo il numero sbagliato. ⚠️ **L'ha trovata il censimento delle copie applicato allo strumento di chi coordina**, non a quelli del progetto: è §4.47 in casa propria — una copia non controllata mente in silenzio, sempre. Rimossa: **l'allineamento vive in coda sola** (gate del lotto 3D, 24/08/2026) |
| **UNA DIVERGENZA FABBRICATA SU DUE ORE CHE SONO I DUE CAPI DELLO STESSO FERMO** | Il blocco del perimetro del lotto 3E delimita l'insieme alle **18:45** in una riga e alle **15:05** in un'altra, e ci ho scritto sopra una questione. ⚠️ **Non e' una divergenza**: il `MOD-PR-04` n. 2026/087, gia' canonizzato da mesi, porta «Ora chiamata: 15:05» e «Fermo produzione: DALLE 15:05 ALLE 18:45» — sono l'inizio e la fine dello stesso guasto, e in mezzo la linea era ferma. ⚠️ **La parola "riavvio", nella frase stessa che la nota citava, presupponeva un fermo**: l'indizio era dentro la citazione. ⚠️ **E la nota era onestamente cauta** — «le fonti di questa nota non lo dicono» — **ma aveva scelto la spiegazione sbagliata fra due possibili**: la cautela non salva da una lettura sbagliata. ⚠️ **L'errore si era propagato a due altre note**, che lo ripetevano come acquisito, e a prenderlo e' stata **la revisione col canone**, l'unico strato che aveva davanti un documento di un'altra area (lotto 3E) |
| **UN CONFRONTO DICHIARATO SENZA L'ORA DEL PRIMO TERMINE, e il primo termine non esisteva** | Il rapporto del lotto 3E scrive che *«gli avvisi salgono da 425 a 426»*. ⚠️ **Il 425 non compare in nessuna misura del progetto**: non nei report di QA, non nei commit, non nei documenti. Le tre misure del vault del 24/08 sono **344** (chiusura 3D), **369** (gate 3D, 13:27) e **426** (3E, 15:17), tutte leggibili dai `qa_all.md` versionati. ⚠️ **Il passaggio vero è 369 → 426, cioè +57**, non +1: **+35** link integrity (30 «lontana dall'`_index`»), **+16** frontmatter (14 summary oltre il tetto), **+6** provenance. ⚠️ **Il 425 è coerente con un numero ottenuto ALL'INDIETRO**, sottraendo da 426 l'unità che il lotto credeva di aver aggiunto — cioè **il gesto che E44 vieta**, nella forma più difficile da vedere: il termine «prima» sugli **errori** (108) era giusto, e la riga sembrava una misura sola. ⚠️ **Il merito non cambia — zero rilievi di merito in tutte e tre le misure** — ma «+1» diceva che il lotto non aveva mosso il vault, e il lotto lo ha mosso di **cinquantasette**. **Un confronto dichiara l'ora di ENTRAMBI i termini, o non si dichiara** (gate del lotto 3E) |
| **UN'AFFERMAZIONE INVERTITA, IN UNA NOTA NATA DA UNA REVISIONE E FINITA NEL CANONE** | «Il termine dell'ente e' il **piu' stretto** dei tre»: tre giorni lavorativi contro ventiquattro ore e' il piu' **largo**. ⚠️ **E la stessa nota ancorava alla clausola 1.1.10 l'obbligo sbagliato**: il punto 3 del certificato ne porta **due**, e la clausola e' citata a proposito del primo. ⚠️ **L'errore era entrato anche nella riga B del canone**, e li' un errore si propaga a tutti i lotti futuri (E49): corretto nella nota e nel canone **nello stesso turno**. ⚠️ **L'ha preso il GIUDIZIO DEDICATO di E58 alla prima esposizione** — cinque rilievi su sette note — ed e' il terzo lotto di fila in cui il gruppo post-revisione ha una densita' di difetto molto piu' alta del ciclo (lotto 3E) |
| ⛔ **UNA DIVERGENZA SCRITTA USANDO IL GREZZO DI UN LOTTO NON ANCORA APERTO** | Il verbale prescrive il ripristino della pavimentazione entro il **08/08/2026** e il titolare promette i lavori «alla chiusura estiva di agosto»; `comunicazione_chiusura_estiva_2026.txt` fissa quella chiusura dal **17 agosto**. ⚠️ **Quel file è di `lotto_07_persone`**, e la regola esisteva dal 19/08: *la terza gamba di una questione si TRACCIA, non si usa, se il suo grezzo appartiene a un lotto futuro* (lotto 1B, T18 e T39). ⚠️ **Nessuno strato del lotto l'ha richiamata**: non la scrittura, non il giudizio — che confronta la nota contro le fonti **che la nota dichiara**, quindi non può vederla — non la revisione, che la divergenza l'ha **prodotta**. ⚠️ **A fermarla è stato `verifica_matrice_lotti.py` con un guasto di disgiunzione**: la QA era verde, le fonti c'erano, la nota era corretta. **La verifica di disgiunzione non tiene in ordine una tabella: impedisce che un lotto consuma il materiale di un altro** — e il costo di saltarla sarebbe stato invisibile. Riscritta sulla sola gamba di 3F; la divergenza vive a **T184** (lotto 3F) |
| ⚠️ **UNO STRUMENTO CHE DAVA «ZERO» SU DUE LOTTI, E IL RAPPORTO CHE NON SE N'ERA ACCORTO PERCHÉ CONTAVA A MANO** | `conta_perimetro_lotto.py` divide il perimetro leggendo due stringhe nei commenti dell'elenco delle note; l'elenco di 3E scriveva la seconda in una forma diversa da quella cercata, 3F ne aveva copiato l'intestazione, e **il parser non cambiava mai sezione**: «note nate: 0 — nessuna» su lotti che ne avevano scritte trentasei e trentasette. ⚠️ **Il rapporto di 3E dichiarava numeri giusti perché li aveva composti a mano da altre fonti**, che è esattamente ciò che l'intestazione dello strumento vieta — *si incolla VERBATIM, i numeri del perimetro non si ricompongono a mano*. **Comporre a mano non è solo meno affidabile: nasconde il guasto dello strumento che avrebbe dovuto sostituire.** ⚠️ **Riparati i DATI, non lo strumento**: allargare il parser a due forme sarebbe stato **allentare** un controllo, e la disciplina del gate 1A ammette solo fix che aggiungono agganci. ⛔ **RATIFICATO AL GATE DI 3F, e con una qualificazione che vale da precedente: è LA STESSA MALATTIA DEI NUMERI A MANO, comparsa stavolta DENTRO una sessione.** Il gate del lotto 3B l'aveva pagata sul coordinatore — due numeri scritti a memoria, e sbagliati entrambi; qui la paga un rapporto di lotto, che aveva lo strumento a disposizione e ha scritto lo stesso a mano. ⚠️ **E la differenza è tutta a sfavore del secondo caso**: i numeri a mano del coordinatore erano solo sbagliati, questi erano **giusti** — ed è esattamente per questo che hanno nascosto il guasto per un lotto intero. **Un controllo che dà un numero impossibile si dichiara guasto, non si aggira** (§4.25). ADEMPIUTO: errata datata nel rapporto di 3E, §6.1, coi numeri ricontati — **37 nate · 12 toccate · 49 controllate** (lotto 3F, gate 31/08/2026) |

---

## 6. Vigilanze aperte (da tenere d'occhio al prossimo gate)

- ✅ **CRITERIO PRE-REGISTRATO, scritto al gate del lotto 3F (25/08/2026): QUANDO LA MISURA
  DEI DUE TASSI DEVE CAMBIARE UNITÀ.** Il lotto 3F ha chiuso con **tre casi residui su tre**
  che erano tutti **enumerazioni**, non affermazioni: la nota trascriveva un elenco di un atto
  pubblico, elencava i titoli dei preparativi, riportava il motivo di una ripetizione di
  analisi. **Nessuna delle tre diceva qualcosa sul dominio misurato**, e tutte e tre
  risultavano «scoperte».

  ⛔ **LA DECISIONE DEL GATE È STATA: LO STRUMENTO NON SI TOCCA.** I tre residui dichiarati
  col loro nome **sono** la forma giusta — cambiare l'unità della misura **a numeri visti**
  romperebbe la comparabilità della serie (§4.45) e sarebbe un fix che allenta (§4.9), su tre
  casi di **un solo lotto**, e di un lotto fatto di elenchi **per natura**.

  **IL CRITERIO, e si decide sui consuntivi, non su un'impressione:**

  > **SE in DUE lotti futuri i residui-enumerazione sono la metà o più delle scoperte del
  > tasso**, la distinzione affermazione/enumerazione **si meccanizza** con la disciplina di
  > §4.9 — perimetro chiuso, difetti piantati nei due versi — e **la serie annota il cambio
  > d'unità dal punto in cui vale**, senza rimisurare i punti anteriori (§4.45).
  >
  > **Se non accade, il residuo dichiarato basta**, e questa riga si chiude.

  ⚠️ **Che cosa guardare, concretamente**: nei rapporti di `R2` e del lotto successivo, la
  riga dei casi residui del tasso di produzione — quante scoperte, e quante di quelle sono
  enumerazioni o citazioni invece che affermazioni sul dominio.

- ⛔ **IL PERIMETRO DELL'AFFERMAZIONE, che è la classe di cui E47, E3/E43 ed E57 governano tre
  specie.** Nominata al **terzo giro del lotto 3F**, come E26 impone quando il terzo giro produce
  ancora rilievi. **Sei affermazioni, sei perimetri diversi, nessuna dentro il perimetro delle
  proprie fonti**: un primato sull'archivio, un'assenza sull'archivio, una regola generale
  importata, un nesso causale non dichiarato, due estensioni su un elenco della fonte.

  ⚠️ **Non è un difetto di lettura: le fonti erano lette bene.** Chi scrive dice una cosa vera
  **di ciò che ha davanti** e la enuncia **di ciò che non ha davanti**.

  ⚠️ **Due delle sei specie non hanno né regola né controllo**: la regola generale importata e
  il nesso causale non dichiarato. **Nessun controllo deterministico può vederle** — non hanno
  numeri, superlativi o negazioni — e le vede solo un lettore che confronti la frase col
  perimetro. **È esattamente ciò che lo strato di giudizio ha fatto, tre volte.**

  **Forma proposta al gate**: *un'affermazione vale nel perimetro delle fonti che la nota cita,
  e per uscirne serve un artefatto o un rimando*. ⚠️ **Il gate può accogliere il candidato più
  stretto sul superlativo-elenco e lasciare aperto questo, non il contrario**: se passa questo,
  quello diventa un esempio invece che una regola.

  ⚠️ **Che cosa guardare al prossimo gate**: se `R2` — che è di manutenzione e riscrive note
  già giudicate — ne produce ancora. **Un lotto che corregge è il terreno naturale della
  specie**, perché chi qualifica una frase tende ad allargarne il soggetto.

- ⚠️ **LA CORREZIONE CHE AFFERMA OLTRE LE FONTI, E IL SUO CRITERIO SCRITTO ORA.** Nominata al
  terzo giro del lotto 3B, dove **almeno sette dei dodici rilievi cadono su frasi che la
  correzione del giro precedente aveva scritto**. Due forme: l'intestazione rimasta indietro
  *(già coperta da E30 ed E51)* e **la frase nuova che afferma oltre le fonti** *(scoperta)*.

  ✅ **CRITERIO DI DECISIONE, scritto PRIMA del lotto che lo verificherà.**

  | | |
  |---|---|
  | **diventa emendamento** | se al **terzo giro** di giudizio del prossimo lotto almeno **due** rilievi cadono su frasi **introdotte dalle correzioni dei giri precedenti**, e non su testo della prima stesura |
  | **forma proposta** | *una correzione è una scrittura, e vale per lei ciò che vale per la nota: prima di applicarla si guarda la fonte che dovrebbe sorreggerla* |
  | **non decade da sola** | se non compare, la riga **non si chiude automaticamente**: decide il gate con le osservazioni davanti |

  ⚠️ **Il prossimo lotto NON riceve alcun promemoria** oltre alle regole in vigore: un
  esperimento avvertito non misura niente. ⚠️ **E il criterio si scrive adesso**, non «quando
  ricompare», perché è la disciplina che questo progetto ha consolidato dal gate di 2B-bis.

  ✅ **CHIUSA IL 23/08/2026, AL GATE DEL LOTTO 3B: ASSORBITA DA E61.** Il criterio qui sopra
  chiedeva la ricomparsa al terzo giro del lotto successivo. **Non si aspetta, e la ragione va
  detta con cura perché non diventi un precedente lasco.**

  | | |
  |---|---|
  | **non è §4.43** | §4.43 vieta di rileggere un criterio **a esito visto**, e qui l'esito non esiste: **l'esperimento non era partito**. Si sta chiudendo il criterio prima del fischio d'inizio, non dopo il gol |
  | **le osservazioni erano GIÀ DUE quando il criterio fu scritto** | i **tre** rilievi introdotti correggendo nel completamento di **2B** sono la stessa famiglia dei **sette** di **3B**. La sessione che scrisse il criterio non li aveva davanti; il gate sì |
  | **con due consuntivi il conteggio di E28 è completo** | la vigilanza chiedeva una terza osservazione per una specie che ne aveva già due, ed era quindi **ridondante rispetto alla storia** |

  ⚠️ **E una cosa il lotto 3B l'ha già mostrata, che è entrata in E61 e vale più del criterio**:
  nel ciclo dedicato di E58 la forma è ricomparsa al **primo** e al **secondo** giro **dentro le
  correzioni fatte per chiuderla**, ed è sparita solo al **terzo** — quando la verifica è stata
  fatta **delimitazione per delimitazione, cella per cella**. **Il rimedio che funziona non è
  rileggere: è verificare ogni frase contro il file**, e in particolare ogni frase **negativa**.

  ⚠️ **Che cosa resta da guardare al prossimo gate, ora che la regola c'è**: E61 dice *che cosa*
  fare e non ha ancora un consuntivo. **Se al terzo giro del prossimo lotto ricompaiono rilievi
  su frasi introdotte dalle correzioni, il difetto non è più l'assenza della regola: è che la
  regola non si applica da sola**, e allora servirà un appiglio meccanico come quelli che E59 ed
  E60 hanno dato a E56 e a E2.

- ✅ **QUANTE ALTRE COPIE DI STATO CI SONO DENTRO LA SUITE? — CENSITE IL 23/08/2026, AL GATE
  DEL LOTTO 3B.** La domanda nasce dai due controlli riparati il 22-23/08, nessuno dei quali
  aveva una logica sbagliata: uno teneva **una copia a mano**, l'altro aveva **un perimetro**
  che non copriva ciò che doveva. **Entrambi mentivano in silenzio, e nessuno dei due è stato
  trovato da uno script.** La passata è stata fatta su tutti i 38 script di `06_operativo\` e
  `qa\`, e ha trovato **due specie**, che si curano in modo opposto:

  | Specie | Che cos'è | Cura |
  |---|---|---|
  | **stato derivabile** | un elenco, un conteggio, un percorso il cui padrone cambia da solo | la copia **si cancella** e lo strumento legge dal padrone |
  | **vocabolario chiuso del manuale** | aree, prefissi, `type`, cartelle: un validatore deve averli per validare | la copia **resta e si CONFRONTA** col padrone, da script |

  ⚠️ **La seconda specie non poteva diventare una lettura a runtime**, e la ragione è
  strutturale: far leggere a `qa_comune` un manuale in prosa manderebbe **rossa tutta la
  suite** il giorno in cui qualcuno riformatta un titolo. **Ma una copia non controllata mente
  in silenzio, sempre** (§4.47). Da qui `verifica_copie_stato.py`, che le confronta e che ha
  il suo collaudo nei due versi — compreso il caso che conta: **il padrone che non si legge
  non deve assolvere**, perché un confronto contro l'insieme vuoto è verde per costruzione.

  ⚠️ **La copia peggiore non era nella suite: era in `ricalibra_budget.py`**, che teneva i
  lotti chiusi e i lotti restanti in due tabelle scritte a mano e **ferme al 19/08**. Cinque
  lotti dopo diceva che i chiusi erano quattro. ⚠️ **Nessuno se n'era accorto perché nessuno
  lo lanciava**, ed è la forma peggiore della malattia: uno strumento che non mente mai a voce
  alta perché non parla mai, e che al primo rilancio avrebbe dato numeri di cinque lotti fa
  con l'aria di darli di oggi. **Riscritto: legge tutto, e dichiara lo scarto che il conteggio
  porta con sé.**

  ⚠️ **Che cosa resta da guardare**: `verifica_copie_stato.py` conosce **quattro** copie
  perché quattro ne ha trovate il censimento. **Non si accorge di una copia nuova**, e nessuno
  script può: la copia nuova la scrive una persona. La vigilanza che resta è quindi diversa da
  quella che si chiude — non «quante ce ne sono» ma **«quando ne nasce una, chi la aggiunge
  al censimento»**. Da chiedere a ogni gate che tocchi uno strumento.
- **Densità crescente**: 2,1 (pilota) → 6,0 (1A) → 9,5 (1B) → **13,5 (1C)** note di
  contenuto per grezzo. ⚠️ **Alla chiusura di 1C la lettura è cambiata**: le note *per
  lotto* sono molto più stabili (27-46, dispersione 50 %) della densità *per grezzo*
  (2,1-13,5, dispersione 147 %). Non è il corpus che diventa più denso: è il lotto che si
  è rimpicciolito. Proiettare con la densità dà 903 note e 36 lotti, ed è un artefatto.
- **Il secondo sito non ha una nota padrona** (T40): il magazzino di Via Palù 3/A ha tre
  strumenti su tre con taratura scaduta e un verbale che lo chiama unità locale separata,
  ma nessun grezzo finora lo descrive. Da tenere d'occhio nei lotti 2 e 3.
- **`MD-1800`, metal detector di Linea 3**: un registro lo dà con la convalida scaduta dal
  03/04/26, l'altro conforme fino al 19/08/2026. È l'unica divergenza del lotto 1C con una
  conseguenza operativa a calendario.
  Le stime della matrice per i lotti 2-10 sono sistematicamente basse: **ricalibrare**
  alla chiusura di 1C.
- **Questioni aperte in crescita** (**32**, dal blocco dei conteggi — la riga diceva 24): al
  gate finale ognuna deve essere «aperta dichiarata» con la sua ragione, non semplicemente
  rimasta aperta. Il numero si legge dal blocco, non si aggiorna a mente.
- ⚠️ **«La cautela non si propaga»**, il pattern nominato alla chiusura di R1: si dichiara come
  lettura ciò che era affermato come dato, e la dichiarazione resta dove è stata scritta —
  mentre `summary`, celle di tabella e glosse ai wikilink restano in modalità assertiva. **È
  sopravvissuto a due giri di revisione mirata**, e un difetto che sopravvive a due revisioni
  non è una disattenzione: è un punto cieco del metodo. ✅ **Deciso al gate di R1 (19/08/2026):
  è diventato E39**, in `metodo_03` §9.5 passo 2-bis. Tre ragioni, e la terza ha deciso: il
  passo 2-bis aveva un **perimetro** sbagliato, non una diligenza insufficiente (§4.25 — quando
  è il perimetro di un controllo è un guasto, e si scrive subito); un difetto che sopravvive a
  due giri mirati è un punto cieco del metodo; e **simmetria col precedente** — E30 è nato
  esattamente così dal lotto 1C, e lasciare la regola più larga in un paragrafo di rapporto
  sarebbe la malattia di E27.
- ⚠️ **L'ESPERIMENTO DI 2A HA DATO IL SUO NUMERO, e ne serve un secondo.** Tasso di difetto
  di **produzione** **3,3 %** (1 su 30) contro il **57,7 %** di R1, stesso criterio, prodotto da
  script. **L'ipotesi del debito storico regge**: con E29 ed E36 in vigore il metodo eredita il
  difetto, non lo produce. ⚠️ **Ma è un lotto solo**, e il criterio del gate di R1 ne chiede
  **due**: il secondo sarà 2B. Se anche lì il tasso resta a una cifra, la rete finale di fine
  corsa può essere dimensionata sulle sole righe di tracciamento, come già previsto.
- ⚠️ **IL PATTERN DI 2A: «l'attributo che la fonte non dà» — PARCHEGGIATO AL GATE, COL SUO
  CRITERIO DI DECISIONE.** Un ruolo («il capo officina»), un primato («è la prima volta»),
  un'identità fra due eventi, una causa. Si rigenera per una ragione meccanica: un archivio
  nomina **per sigla**, chi scrive deve rendere la sigla leggibile fuori contesto, e **il gesto
  naturale per farlo è aggiungere la qualifica** — che quasi sempre è vera, ma sta in un'altra
  fonte. È la classe del `PARLANTE_3` di metodo_03, che lì è un caso singolo e qui si rivela
  una famiglia.
  ✅ **CHIUSA il 21/08/2026, col criterio che era stato scritto in anticipo.** Il criterio
  chiedeva la ricomparsa **al terzo giro** di giudizio del lotto 2B. Al terzo giro, dei tre
  rilievi accolti, **due sono di una specie nuova** e uno solo — gli orari dei turni della
  Linea 1 — è di questa. ⚠️ **E quell'uno sta in una nota che 2B non ha scritto**: viene da un
  lotto precedente, e il lotto l'ha soltanto toccata. **È debito, non produzione**, ed è la
  distinzione che E41 esiste per misurare. Far diventare emendamento una classe che al terzo
  giro **non si è più prodotta**, sulla base di un difetto ereditato, applicherebbe il criterio
  contro il suo scopo. **La riga si chiude, e al suo posto subentra quella qui sotto.**
- ⚠️ **LA SPECIE NOMINATA AL TERZO GIRO DI 2B, COL CRITERIO DI DECISIONE FISSATO AL GATE:
  «L'AFFERMAZIONE UNIVERSALE VERIFICATA SUL SOTTOINSIEME CHE L'HA SUGGERITA».** «l'unico», «il primo», «il più alto», «nessun altro».
  Cinque casi in tre giri di giudizio, e il ciclo **non converge**. ⚠️ **Si rigenera per una
  ragione meccanica e scomoda: nasce dallo scrivere bene.** Chi scrive una nota ha letto a
  fondo **un** documento, e un superlativo sembra il riassunto onesto di quella lettura;
  invece è un **quantificatore universale**, e le sue condizioni di verità stanno **fuori dal
  testo che si ha davanti** — in tutte le righe che non si stanno guardando, o in tutti i
  documenti che non si stanno citando. ⚠️ **È una famiglia più grande di quella parcheggiata a
  2A, non la stessa**: là mancava **una** fonte e si riparava citandola; qui il dominio di
  verifica è **un insieme intero**, e si ripara **solo** restringendo la frase al perimetro
  davvero guardato — tutte e tre le correzioni hanno sostituito «dell'archivio» con «di questo
  registro». **Non si propone come emendamento adesso**, e vale E28: è la prima volta che la
  si nomina.
  ✅ **CRITERIO DI DECISIONE, aggiornato al gate finale del 21/08/2026 e scritto PRIMA che
  l'esperimento di 2B-bis parta.** Il criterio ha due metà, e solo una è cambiata:

  | | |
  |---|---|
  | **resta** | se la specie ricompare al **TERZO GIRO** di giudizio di 2B-bis **su note nate o riscritte dal lotto** — produzione, non debito — **diventa emendamento**, con la forma già scritta nel §5.4 del rapporto 2B: *un'affermazione di unicità, primato o massimo si scrive col perimetro su cui è stata verificata, e quel perimetro non è mai più largo delle fonti della nota* |
  | **decade** | **la chiusura automatica.** Se al terzo giro non compare, **la riga NON si chiude da sola**: il gate di 2B-bis decide con **tutte** le osservazioni davanti — 2B, il completamento, 2B-bis |

  ⚠️ **Perché è cambiata, e perché questo NON è §4.43.** Il completamento di 2B ha prodotto un
  **fatto sopravvenuto** che il criterio non prevedeva: la specie **rigenerata in produzione,
  dentro il gesto stesso di correzione** — tre casi più uno, con nomi e righe (§10.5 del
  rapporto 2B). ⚠️ **§4.43 vieta di rileggere un criterio A ESITO VISTO, e l'esito di 2B-bis
  non esiste ancora**: qui non si sta guardando il risultato dell'esperimento per decidere come
  leggerlo, si sta correggendo il criterio **prima** che l'esperimento parta. È la differenza
  fra cambiare le regole a partita in corso e cambiarle prima del fischio d'inizio.

  ⚠️ **E la ragione del cambiamento è E46 applicato ai criteri**: chiudere la riga su un
  esperimento pulito, ignorando tre casi di produzione documentati, sarebbe **far dire al
  criterio più di quanto misura**. Un giro di giudizio di un lotto non misura la specie
  nell'intero metodo: misura la specie in quel lotto.

  ⚠️ **2B-bis NON riceve alcun promemoria sulla specie** oltre alle regole già in vigore (E39,
  passo 2-bis). **Un esperimento avvertito non misura niente**, e un avvertimento che vivesse
  solo nel prompt sarebbe la malattia di E27.

  ✅ **CHIUSA il 21/08/2026: il criterio si è avverato, ed è diventato E47.** Al **terzo giro**
  di giudizio di 2B-bis, **tre dei cinque rilievi** sono di questa specie, e stanno **su note
  NATE dal lotto** — produzione, non debito. La metà del criterio che era rimasta in piedi
  chiedeva esattamente questo, e non c'è stato niente da interpretare.

  ⚠️ **E47 è il primo emendamento del progetto nato da un criterio pre-registrato che si è
  avverato**, invece che da un difetto trovato per caso. **La forma scritta è quella che il
  criterio annunciava**, allargata su un punto solo: non solo unicità, primato e massimo, ma
  **ogni quantificatore** — «ogni», «tutti», «sempre», «mai», e le negazioni che dicono la
  stessa cosa al rovescio.

  ⚠️ **E47 porta con sé una regola di collocazione che il criterio non prevedeva**: quando
  l'affermazione universale **è il punto** della nota e non un ornamento, **la nota è nel posto
  sbagliato** — un fatto che riguarda tutto l'archivio si scrive **nella tabella di
  tracciamento**, che è il solo posto da cui l'archivio si guarda per intero. **La prima
  applicazione è T96**, il punto cieco sul barrato.

  ⚠️ **La specie è ricomparsa anche DOPO E47**, nella revisione col canone dello stesso lotto —
  tre righe d'indice e una scomposizione (A2, A3, A5, A10). **Questo non riapre la vigilanza**:
  E47 è stata scritta **dopo** il terzo giro e **prima** della revisione, e la revisione ha
  fatto esattamente il lavoro che E47 le chiede di fare. ⚠️ **Ma dice una cosa che il prossimo
  gate deve sapere: E47 non estingue la specie, la rende TROVABILE.** Il controllo del
  quantificatore va fatto **da chi rilegge**, come si controlla una cifra — non da chi scrive.
- ⚠️ **IL CONTEGGIO CHE NASCE DALLA LETTURA E NON DALLA FONTE.** Un numero di elementi
  («sei fasi», «due colonne», «due divieti», «tre serie») o una posizione («§8.1», «colonna
  `logica FEFO`») che la nota ricava **guardando** e che la fonte **non enuncia**. Nominata al
  ri-giudizio del lotto 2B-bis, dove è una delle **due sole famiglie** in cui si sono divisi
  ventidue rilievi. ⚠️ **È imparentata con E23 e non è E23**: quella nasce per i valori
  *calcolati*, questa riguarda **contare e localizzare** — atti che sembrano di lettura e sono
  di inferenza. ⚠️ **E49 la copre nel canone; nelle note resta scoperta**, ed è per questo che
  ha un criterio.

  ✅ **CRITERIO DI DECISIONE, scritto al gate del 21/08/2026 PRIMA che il tema 3 parta.**

  | | |
  |---|---|
  | **diventa emendamento** | se ricompare al **TERZO GIRO** di giudizio del primo pacchetto del tema 3, **su note NATE dal lotto** — produzione, non debito |
  | **forma proposta** | *un numero che la fonte non enuncia è un valore derivato anche quando si ottiene contando, e si scrive col modo in cui è stato ottenuto — oppure non si scrive* |
  | **non decade da sola** | se al terzo giro non compare, la riga **non si chiude automaticamente**: decide il gate con tutte le osservazioni davanti |

  ⚠️ **Il tema 3 NON riceve alcun promemoria** oltre alle regole in vigore. Un esperimento
  avvertito non misura niente. ⚠️ **E al gate del 21/08 la specie ha già colpito una seconda
  volta**: il rapporto di 2B-bis affermava che `candidate_r1.py` «conosce una sola fonte
  governante per dominio», e il codice ne gestiva due **dal lotto 2A** — affermazione ricavata
  guardando il risultato invece di leggere il codice, e ratificata in buona fede.

  ✅ **CHIUSA il 22/08/2026: la specie è comparsa al terzo giro di 3A su note nate dal lotto, ed è
  diventata E50.** ⚠️ **Il dato che ha deciso la forma della regola**: al terzo giro **le cinque
  cifre marcate `(contate)` erano tutte esatte, e quelle sbagliate erano tutte non marcate**. **La
  marca non certifica il numero: dichiara che va ricontato**, ed è per questo che funziona.
- ⚠️ **L'AFFERMAZIONE CHE SI SMENTISCE DENTRO LA NOTA STESSA.** Non un'affermazione falsa
  contro la fonte — quella la prende il giudizio — ma una **la cui smentita sta nella stessa
  nota**: «non più X» sopra fatti elencati che dicono «non solo X»; «nessuno dei due cita
  l'altro» accanto alla citazione riportata tre righe sopra; un titolo che afferma ciò che il
  corpo dichiara di non sapere. Nominata al ri-giudizio del gate del 21/08/2026, dove è una
  delle **due sole famiglie** in cui si sono divisi diciannove rilievi.

  ⚠️ **Perché è una specie e non tre casi**: nasce dal **riscrivere per correggere**. Chi
  aggiunge una qualificazione in un punto lascia in piedi la frase che quella qualificazione
  contraddice, e il difetto **non è visibile leggendo la frase**: è visibile solo leggendo la
  nota intera. **È il difetto che una regex non può vedere e un lettore distratto nemmeno.**

  ✅ **CRITERIO DI DECISIONE, scritto ORA e non «quando ricompare».**

  | | |
  |---|---|
  | **diventa emendamento** | se ricompare al **TERZO GIRO** di giudizio del lotto **3A**, **su note nate dal lotto** — produzione, non debito |
  | **non decade da sola** | se al terzo giro non compare, la riga **non si chiude automaticamente**: decide il gate con le osservazioni davanti |

  ⚠️ **3A non riceve alcun promemoria** oltre alle regole in vigore. ⚠️ **E il criterio si scrive
  adesso perché il rapporto di 2B-bis, su questa specie, era rimasto un passo indietro**: l'aveva
  nominata e rimandata a «quando ricompare», che è esattamente ciò che la disciplina consolidata
  di questo progetto non fa. **Il criterio precede l'esperimento, sempre.**

  ✅ **CHIUSA il 22/08/2026: la specie è comparsa al terzo giro di 3A su quattro note, tutte nate
  dal lotto, ed è diventata E51.** ⚠️ **Quattro forme distinte**, tutte misurate: summary contro
  corpo, titolo contro corpo, frase contro la propria tabella, due metà che si escludono.
  ⚠️ **E l'istanza più istruttiva non stava in una nota ma in un documento di metodo** — la
  motivazione del pacchetto 3A, propagata in tre file prima che il giudizio la vedesse.
- ✅ **LA CAPACITÀ 25-35: REVISIONE ESEGUITA E CHIUSA IL 24/08/2026, AL GATE DEL LOTTO 3E.** La
  riga «provvisoria, da rivedere a dieci lotti chiusi» stava in `metodo_03` §9.4 dal 19/08 e nella
  §2 del prompt dei lotti; **la soglia è stata raggiunta e la revisione è stata fatta**, coi dieci
  consuntivi del §6 di `rapporto_gate_3d.md` davanti.

  | | |
  |---|---|
  | **esito** | **la fascia 25-35 è CONFERMATA come grandezza di PROGETTO** — serve al taglio dei pacchetti in apertura — e **i tetti duri di E28 restano le soglie che spezzano**, avendo spezzato giusto due volte (2B, 3E) |
  | **che cosa NON si è fatto** | **sostituire la fascia con un'altra fascia.** La densità va da **7,0 a 25,5**: ciò che si mantiene costante è **il lotto**, non la densità, e ricalibrare sui consuntivi ripeterebbe l'errore che **E31** ha già corretto, spostato di un piano |
  | **il consuntivo** | rispettata **4 volte su 10**, **SEI contando il solo ciclo** (E52 tiene già le post-revisione fuori dalla soglia) |

  ⚠️ **La domanda che il gate di 3D aveva riformulato — «che cosa consuma il rischio, le note o i
  giri?» — ha una risposta, e non sono le note**: i giri di giudizio sono **tre in SETTE lotti su
  dieci**, e il ciclo quasi mai si chiude per esaurimento. ⚠️ **Il §6.2 di `rapporto_gate_3d.md`
  scrive «otto», e la sua stessa tabella ne conta sette** — le eccezioni che quella riga elenca
  sono **tre**: 1A (due giri), 1B (quattro), 3D (due più due dedicati). **Il numero corretto è
  sette**, e non cambia la decisione: la cambierebbe solo se dicesse «tre giri quasi mai». ⚠️ **Quindi la vigilanza NON si chiude:
  si SPOSTA**, e da qui in poi guarda due grandezze diverse dal conteggio delle note del ciclo —
  **la densità di difetto del gruppo post-revisione** (la riga qui sotto, che resta aperta) e **la
  costanza dei tre giri**. **Se un lotto mostrerà che tre giri sistematicamente non bastano, la
  domanda si riapre sui GIRI.**

  ⚠️ **E la lezione di metodo dei consuntivi resta scritta dov'è, perché serve a chi li rilegge**:
  le tre serie di rilievi dei dieci lotti **non si sommano** — rilievi accolti, errori, note
  tornate `afferma_oltre` sono tre grandezze diverse — e chi legge quella colonna come una serie
  sola legge un numero che non esiste. **È E46 applicato a un consuntivo.**
- ⚠️ **IL GRUPPO POST-REVISIONE, E IL SUO CRITERIO.** Le note nate dalla revisione e dal
  ri-giudizio **non contano nella soglia di spezzamento** (E52) ma si dichiarano sempre come
  gruppo, con esiti separati.

  ✅ **CRITERIO DI DECISIONE, scritto al gate del 22/08/2026, PRIMA del prossimo lotto che
  produca note post-revisione.**

  | | |
  |---|---|
  | **il gruppo prende un mini-ciclo dedicato** | se al prossimo lotto che produce note post-revisione **il tasso di rilievi del gruppo è ancora più del doppio di quello del ciclo** |
  | **in che cosa consiste** | rilettura **2-bis con le fonti aperte davanti**, giudizio, e **un secondo giro se il primo trova errori** — come regola, non come diligenza |
  | **se non lo è** | **E54 è bastato**: il caso peggiore di 3A era una citazione non letta, e E54 ora la vieta |

  ⚠️ **Il numero di 3A, per confronto**: quattro note post-revisione, **43 rilievi**; trentotto
  note di ciclo, **16 rilievi** al terzo giro. Il gruppo era **un decimo delle note e più del
  doppio dei rilievi**.
- ⚠️ **LE NOTE NATE DALLA REVISIONE HANNO UN TASSO DI DIFETTO MOLTO PIÙ ALTO DI QUELLE NATE DAL
  CICLO.** Al lotto 3A il ri-giudizio dopo la revisione ha prodotto **43 rilievi e 16 errori** —
  più del terzo giro, che ne aveva 16 e 5 — **e quasi tutti sulle quattro note nate dalla
  revisione**, non sulle trentotto nate dal ciclo.

  ⚠️ **La ragione è strutturale, non di attenzione**: quelle note nascono da una divergenza che
  qualcun altro ha già trovato, si scrivono in fretta per non perderla, e **non passano i tre giri
  che le altre hanno passato**. ⚠️ **Il caso peggiore del lotto**: la questione sul mock recall
  citava `PRO-QA-14` **cinque volte senza averlo letto**, e quel documento è nel corpus.

  ✅ **ESERCITATO IN `3C`, E NON HA SCATTATO.** Gruppo post-revisione: **4 note, 0 rilievi al
  secondo giro (0,0 %)**; note del ciclo: **51, 2 rilievi (3,9 %)**. **E54 è bastato**, nessun
  mini-ciclo dedicato. ⚠️ **È la prima volta che un criterio pre-registrato di questo progetto
  viene esercitato e si chiude senza discussione**, e funziona perché era stato scritto quando
  non si sapeva come sarebbe andata. ⚠️ **Ma il gruppo è cresciuto dopo**: i ritrovamenti del
  **terzo** giro hanno prodotto altre due note, **che non sono passate dal giudizio** — la
  regola d'arresto E26 ha la precedenza. **Debito dichiarato: T141.**

  ✅ **CHIUSA il 23/08/2026, al gate del lotto 3C — ed è la PRIMA VOLTA che un criterio
  pre-registrato di questo progetto viene esercitato e si chiude senza discussione.** Non ha
  scattato: **0,0 % il gruppo, 3,9 % il ciclo**, e la metà del criterio che chiedeva «più del
  doppio» non c'è andata vicino. **E54 è bastato.** ⚠️ **Funziona perché era stato scritto
  quando non si sapeva ancora come sarebbe andata**: un criterio riletto a esito visto non è un
  criterio, è una spiegazione (§4.43).

  ⚠️ **La ragione STRUTTURALE, che E54 non toccava, l'ha chiusa E58, e per una via che questa
  riga non aveva previsto.** La vigilanza diceva: quelle note nascono da una divergenza già
  trovata, si scrivono per non perderla, e **non passano i tre giri che le altre hanno passato**.
  Il rimedio immaginato era un mini-ciclo dedicato **al gruppo**; il rimedio vero è più stretto e
  più forte — **ogni nota vede il giudizio almeno una volta**, e quelle nate dall'ultimo giro lo
  vedono in un giudizio dedicato solo a loro. ⚠️ **E il gruppo di 3C non era il problema: lo
  erano le DUE note nate DOPO il gruppo**, ai ritrovamenti del terzo giro, che il criterio non
  guardava perché guardava il tasso del gruppo. **Il criterio ha misurato bene e ha guardato
  nel posto sbagliato**, ed è il difetto che E58 chiude.
- ✅ **LA REVISIONE COL CANONE NON È PIÙ UNA VIGILANZA: È CHIUSA DA E45.** Il lotto 2B aveva
  dichiarato il passo scoperto credendo che la guardia su `03_valutazione\` coprisse il canone.
  **Non lo copre**: il canone sta in `01_metodo\`, la guardia riguarda l'esame, e un subagente
  a contesto pulito **è** la sessione diversa che il passo 3 chiede. ⚠️ **La regola è ora nel
  manuale** (E45, §9.5 passo 3) invece che nel testo incollato di un gate, ed è lì che chi opera
  la cerca. **Il ciclo di 2B è stato completato nella sessione del 21/08**: la revisione è stata
  eseguita, e il suo esito sta nel §10 del rapporto 2B.
- ⚠️ **IL TASSO DI DIFETTO DI PRODUZIONE MISURA UN DOMINIO SOLO.** In 2B dava 0,0 % mentre il
  giudizio trovava due note scoperte rispetto al manuale HACCP, che è una fonte prescrittiva di
  **un altro** dominio. Le due misure non si contraddicono, ma **il nome del numero promette
  più di quanto misura**. Candidato emendamento nel §9.1 del rapporto 2B: **il tasso si
  dichiara col nome del dominio su cui è misurato**. ⚠️ Non si propone di allargare lo script:
  vorrebbe dire dichiarare un dominio per ognuna delle **trentasei** fonti prescrittive del
  corpus.
- ⚠️ **UN FALSO POSITIVO DELLE DOPPIE PADRONE, e il conto del vault che non torna.** Alla
  misura finale del 20/08 il vault porta **126 errori**, non i 125 attesi: 122 grezzi non
  canonizzati più 3 aree senza hub sono **incompletezza**, ma il centoventiseiesimo è un
  **rilievo di merito** — `fatto-microperdite-saldatura-l26130` contro
  `kpi-conducibilita-risciacquo-cip-maggio`, aperto perché condividono i valori `0,9 · 1,1 ·
  1,4`. ⚠️ **È un falso positivo dimostrabile**: le due note non hanno **nessuna fonte in
  comune** e i tre numeri sono grandezze diverse con unità diverse — percentuali di ossigeno
  contro millisiemens. Il controllo confronta valori **nudi**. La via di correzione è
  restringerlo (per esempio: due candidate devono condividere almeno una fonte), ma **allenta
  un controllo** e §4.9 impone perimetro chiuso e difetto piantato nuovo: è un lavoro a sé, non
  una correzione di passaggio. **Da decidere prima del gate finale**, dove la QA a perimetro
  vault deve essere verde.
- ⚠️ **IL DEBITO DI E43: 29 note dichiarano un'assenza senza artefatto.** Sono anteriori alla
  regola, e il controllo le tratta come **avviso** invece che come errore — un controllo nuovo
  che rendesse rosso il pregresso bloccherebbe ogni lotto futuro su un difetto che nessuno
  poteva evitare. ⚠️ **Ma è debito, e come tale va programmato**: rientra nella rete finale di
  fine corsa, insieme alle righe di tracciamento, ed è misurabile in ogni momento rilanciando
  `qa_frontmatter --perimetro vault` e contando gli avvisi che portano «debito anteriore a
  E43».
- ⚠️ **CANDIDATO PARCHEGGIATO, col suo criterio di decisione scritto in anticipo** (19/08/2026,
  gate di R1). Si potrebbe scrivere uno script che segnali le **superfici di sintesi rimaste
  assertive quando il corpo porta una qualificazione**. ⚠️ **Non si costruisce adesso, e la
  ragione è E28**: un avviso euristico nuovo, su **una sola osservazione**, rischia di essere
  rumoroso — e una regola che scatta sempre viene scavalcata per prassi, che è peggio di non
  averla. **Si decide dopo DUE LOTTI CHIUSI SOTTO E39**, e il criterio è questo, scritto ora
  perché nessuno lo riapra a numeri visti: **se in quei due lotti il pattern «la cautela non si
  propaga» ricompare ancora al terzo giro di giudizio, la rilettura non basta e serve la
  macchina; se non ricompare, E39 basta e il candidato si chiude come non necessario.** Il
  primo dei due lotti è **2A**, ed è chiuso: ⚠️ **il pattern «la cautela non si propaga» è
  ricomparso, e per tre volte** — nel titolo e nelle glosse di una nota la cui cautela era nel
  corpo, in un summary che affermava ciò che il corpo sospendeva, e **in un summary rimasto
  indietro nel giro stesso in cui la cautela veniva apposta al corpo su rilievo del giudice**.
  ⚠️ Quest'ultimo è il caso che pesa: E39 dice *che cosa* fare, non *quando*, e la propagazione
  fatta a fine giro arriva tardi. Il secondo lotto sotto E39 sarà **2B**; se il pattern
  ricompare ancora al terzo giro, il criterio dice che la rilettura non basta.
- **Le due prescrizioni più duplicate del vault** — la seconda firma (§4.3.2.1) e il CCP4 —
  sono anche quelle su cui il vault regge le conclusioni più forti: se una copia diverge,
  diverge un'accusa. Padroni dichiarati in R1; da riverificare a ogni lotto che le tocca.
- **Il tasso di difetto della riconciliazione verticale** (57,7 % su 71 note, lotto R1): è il
  numero che decide se il ripasso vada rifatto a fine corsa o se E29 in vigore basti. ⚠️ Il
  difetto **si suppone storico** — tutte le 71 note sono state scritte prima che E29 esistesse
  — ma **finora è solo un'ipotesi**, perché quel 57,7 % misura note vecchie e non dice niente
  su quanto il metodo, con la regola in vigore, produca il difetto invece di ereditarlo.
  ✅ **Il gate di R1 l'ha trasformata in un ESPERIMENTO, ed è il lotto 2A**: primo lotto
  canonizzato sotto E29 ed E36, il cui rapporto dichiara **due tassi distinti e non li mescola**
  — il **tasso di riapertura** (quante note vecchie E37 riapre e quante ne corregge: misura il
  DEBITO) e il **tasso di difetto di produzione** (sulle note NATE in 2A, quante il giudizio
  trova scoperte rispetto alla fonte che le prescrive: misura la PRODUZIONE). ⚠️ **È il secondo
  a decidere**: vicino a zero, il debito era storico e la rete finale basterà; lontano da zero,
  **E29 in vigore NON basta e la regola va ripensata, non ripetuta**. Da pesare al gate di 2A,
  e va prodotto **da script, non stimato**.
- **Terzo compito di PROMPT_GIUDIZIO_V2**: 17 accolte su 26 al primo impiego; il rumore ha
  una forma sola (il giudice non conosce il grafo). Al gate finale si decide se resta, si
  tara o si toglie.
- **Tabella di tracciamento** delle questioni trasversali: è la prova, al gate finale, che
  nessuna gamba mancante è stata dimenticata.
- **Da fissare prima di S6** (già deciso, verificare che sia applicato): `predizioni.md`
  committato PRIMA della misura; `fonti_corrette` conta il grezzo (la nota è navigazione);
  tasso di allucinazione = `allucinata + sbagliata` su `non_rispondibile`.
- **Post-ciclo, candidato non impegno**: misurare la config di riferimento 8B su hardware
  adeguato, DOPO S6 (mai insieme alla canonizzazione: una variabile alla volta).

---

- ⚠️ **LA FRASE DI RACCORDO VERSO UN'ALTRA NOTA, E IL SUO CRITERIO SCRITTO ORA.** Nominata al
  terzo giro del lotto 3E, dove i giudici l'hanno descritta **da tre fette diverse**: non la
  glossa che rimanda — «v. `[[questione-x]]`» sta in piedi da sola — ma quella che **descrive**
  ciò che l'altra nota contiene o ciò che le sue fonti dicono. ⚠️ **Nasce dal buon proposito di
  tessere il grafo**, ed è per questo che sopravvive ai giri: chi scrive sta collegando, non
  affermando, **ma il lettore e il giudice la leggono come un'affermazione**. È **E36 applicato
  al wikilink** invece che alla citazione.

  ✅ **CRITERIO DI DECISIONE, scritto PRIMA del lotto che lo verificherà.**

  | | |
  |---|---|
  | **diventa emendamento** | se al **terzo giro** di giudizio del prossimo lotto almeno **due** rilievi cadono su **glosse di rimando** — frasi che nominano un'altra nota e ne descrivono il contenuto — e non su testo che afferma di suo |
  | **forma proposta** | *il rimando nomina la nota, non il suo contenuto: «la questione ha le sue fonti e sta in `[[…]]`», mai «`[[…]]` dice che…»* |
  | **non decade da sola** | se non compare, la riga **non si chiude automaticamente**: decide il gate con le osservazioni davanti |

  ⚠️ **E c'è una seconda superficie della stessa specie, già misurata**: le **glosse degli hub**,
  che la clausola 4 di §7.1 rende un ERRORE sull'hub quando dicono ciò che lo spoke non dice. In
  3E ne sono state trovate **tre**, tutte perché una correzione allo spoke non le aveva
  raggiunte. **È E39 esteso ed E42 su una superficie che nessuna delle due nomina.**

  ✅ **CHIUSA IL 24/08/2026, AL GATE DEL LOTTO 3E: DIVENTATA E64, SENZA ASPETTARE L'ESPERIMENTO.**
  Il criterio qui sopra chiedeva la ricomparsa al terzo giro del **prossimo** lotto. **Non si
  aspetta, ed è la stessa via con cui si chiuse la vigilanza di E61 il giorno prima** — la ragione
  va detta con cura perché non diventi un precedente lasco.

  | | |
  |---|---|
  | **non è §4.43** | §4.43 vieta di rileggere un criterio **a esito visto**, e qui l'esito non esiste: **l'esperimento non era partito**. Si chiude il criterio prima del fischio d'inizio, non dopo il gol |
  | **le osservazioni erano GIÀ TRE quando il criterio fu scritto** | il terzo giro di 3E ha nominato la specie **da tre fette indipendenti**, e la sessione ha scritto il criterio **dopo** averle avute davanti. Il gate le ha |
  | **con tre consuntivi il conteggio di E28 è più che completo** | la disciplina chiede **due** consuntivi perché una regola venga dai numeri e non da un principio. Qui sono tre, dentro un lotto solo |
  | **ed è la via di E50 ed E51** | entrambe scritte quando il terzo giro le ha nominate con casi plurimi. **Quando il terzo giro nomina una specie, il gate la scrive**: aspettare un lotto significa lasciarla scrivere in quel lotto |

  ⚠️ **La seconda superficie — le glosse degli hub — NON è entrata in E64: è diventata la seconda
  estensione di E39**, ed è la collocazione giusta. **E64 riguarda che cosa una frase di rimando
  può dire; l'estensione di E39 riguarda dove si va a cercare quando una correzione toglie
  qualcosa.** Sono due lacune diverse che si toccano su una superficie sola, e metterle sotto lo
  stesso numero avrebbe reso il numero inutilizzabile da entrambe le parti.

## 7. Come si lavora in chat (formato delle risposte)

Il terminale pone domande **a pannelli**, e il coordinatore non risponde mai a voce: la
risposta è **testo incollabile** nel campo note (tasto `n`), in un blocco di codice, perché
il titolare fa da ponte e non deve metterci niente di suo.

Che cosa quella risposta deve contenere, e che cosa il coordinatore fa **prima** di
scriverla, sta nella **§7-bis**, che è il padrone del protocollo.

---

## 7-bis. Protocollo di risposta del coordinatore

**Il coordinatore risponde sempre per intero, in un solo giro.** Una risposta a metà costa
un giro di conversazione al titolare, che nel frattempo tiene fermo un terminale.

**Prima di deliberare.**

1. **Se il terminale ha posto più pannelli, si chiede di vederli TUTTI**, e ci si pronuncia
   sul pacchetto completo: le decisioni di un pannello cambiano quelle degli altri, e
   deliberare sul primo significa vincolarsi al buio sul terzo.
2. **Prima di approvare un gate o una matrice si legge il documento vero sul disco,
   integralmente** — non il riassunto che ne ha fatto la sessione. **Due errori del
   progetto sono stati trovati così**, e nessuno dei due era visibile nel riassunto.
3. **Quando i numeri riportati non tornano, si ricontrollano prima di approvare.** È
   successo due volte, ed erano errori veri tutte e due: un numero che stona non è quasi
   mai una svista di trascrizione.

**La forma della risposta.**

4. Tre parti, sempre: **quale opzione**; **perché**, citando la regola o il precedente che
   la sostiene; **il testo esatto da incollare**.
5. Quel testo è **un prompt esteso, non un ordine secco**: porta il verdetto, le ragioni,
   gli adempimenti (registri da aggiornare, commit da fare, tabelle da allineare) e le
   guardie da rispettare. ⚠️ **Chi opera deve capire PERCHÉ, non solo cosa**: è l'unico
   modo perché sappia decidere nei casi che il prompt non prevede — e i casi non previsti
   sono metà di ogni lotto.
6. **Ogni istruzione è classificata: una tantum** (verdetti, propagazioni, correzioni)
   **oppure permanente.** ⚠️ Se una cosa va ripetuta a ogni lotto, il prompt riutilizzabile
   è incompleto: **si emenda LUI**, invece di ripeterla. È la stessa malattia che E27 ha
   curato — un obbligo che vive solo nel testo incollato è un obbligo che sparisce alla
   prima sessione lanciata con un prompt diverso.

**Il perimetro del coordinatore.**

7. **Non tocca mai il vault, non apre mai `03_valutazione\`, e non scrive nel repository
   mentre una sessione di terminale sta girando.** Due mani sullo stesso file sono un
   conflitto di merge nel caso migliore, e una regola persa nel caso peggiore.
8. **A fine sessione verifica da sé l'allineamento col remote**, invece di fidarsi del
   rapporto: il rapporto dice ciò che la sessione **credeva** di aver fatto.
   ⚠️ **SOLO comandi git di sola lettura**, e non è una preferenza di stile: `git log`,
   `git rev-list --left-right --count origin/main...main`, oppure
   `git --no-optional-locks status`. **Un `git status` normale lanciato dal ponte crea
   `.git\index.lock` e non riesce a cancellarlo**, e quel lock blocca il git del titolare al
   comando successivo. È successo il **19/08/2026**: due lock stantii, spostati fuori dal
   repository in `.eval_do_not_index\_to_delete\`, che il titolare può cancellare — **verificato a fine giornata: la cartella non c'è
   più**, quindi i due lock sono stati eliminati.
   *(Riga aggiornata il 19/08/2026: prima consigliava `git status -sb`, che è proprio il
   comando che lascia il lock.)*

**Ciò che il coordinatore non può contare da sé.**

9. ⚠️ **IL VAULT NON È NELLA CARTELLA CHE IL COORDINATORE VEDE.** `aurora-cervello` sta fuori
   dal repository e non è sotto git: **i numeri del vault si leggono SOLO dagli output
   committati** — il blocco di `conta_stato.py`, i report di `qa_all.py` in
   `06_operativo\qa\<data>_<lotto>\`. Non si stimano, non si deducono da un rapporto in
   prosa, non si chiedono a memoria.
   ⚠️ **Un coordinatore che non può contare da sé si fida degli script**, e per questo **gli
   script devono essere l'unica fonte dei numeri**: è un vincolo di posizione, non una
   preferenza metodologica. Ed è anche la ragione per cui la divergenza **172/173** è saltata
   fuori — due script, lo stesso giorno, numeri diversi, **entrambi nel repository**. Se i
   numeri fossero vissuti in prosa, nessuno avrebbe potuto accorgersene da qui.

---

## 8. Come questo file resta vivo (obbligo, non consiglio)

Un passaggio di consegne che invecchia è peggio di nessun passaggio di consegne: chi lo
legge crede di sapere e sa cose vecchie. Perciò l'aggiornamento non è affidato alla buona
volontà, ma al rituale di chiusura.

⚠️ **Titolarità del gesto, fissata il 19/08/2026 perché non si riapra.** Il **QUANDO** è di
**principio 5 della scaletta** e di **`metodo_03` §9.5, passo 8** (E27): sono loro a dire che il
gesto esiste e a che punto della chiusura cade. Il **COME** — chi scrive, in quale sezione, con
quale regola di scrittura — è di questa §8. **Questo file non è una terza fonte del rituale: è
il manuale d'uso di sé stesso.** Prima di E27 il gesto viveva solo nel §5 del prompt dei lotti,
cioè in un documento derivato e monouso: un rituale scritto in un solo posto derivato prima o
poi diverge da quello vero.

**Chi aggiorna, e quando.**

- **La sessione operativa**, come parte della chiusura, insieme a stato e decision log:
  se il gate ha fissato un criterio nuovo, ha versionato uno strumento, ha ratificato una
  prassi o ha pagato un errore nuovo, scrive **una riga** nella sezione giusta di questo
  file, con la data. È un gesto del rituale, non un compito extra.
- **Il coordinatore**, quando al gate enuncia un principio che prima non esisteva: lo
  detta nel testo da incollare, così arriva qui nello stesso giro in cui nasce.

**Dove va cosa.**

| Cosa è successo | Sezione |
|---|---|
| un criterio di giudizio nuovo, o un precedente che chiarisce come si applica | §4 |
| un errore commesso e la lezione che ne è uscita | §5 |
| una cosa da tenere d'occhio, o una decisione rimandata a un gate futuro | §6 |
| un cambio nel modo di lavorare fra chat, terminale e titolare | §1 o §7 |
| un avanzamento (grezzi, note, misure, prossimo passo) | §3, riscritta, non accumulata |

**Regole di scrittura.** Una riga per criterio, col caso che l'ha generato: un principio
senza il suo precedente non si sa più applicare. §3 si **riscrive** a ogni chiusura
(è una fotografia, non uno storico); §4, §5 e §6 si **accumulano**. I numeri qui dentro
sono copiati dall'output di `conta_stato.py`, mai ricomposti a mano — questo file non fa
eccezione alla regola d'oro 5.

**Perché è importante.** Le decisioni vivono nel decision log, le regole in metodo_03, i
numeri nei verbali. Solo la *giurisprudenza* — il modo di decidere — non ha altra casa che
questa. Se smette di essere aggiornata, il progetto torna a dipendere da una singola
conversazione: esattamente ciò che questo file esiste per impedire.
