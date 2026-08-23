# Rapporto del lotto 3B — la politica e la formazione

> **Chiuso il** 23/08/2026 · **Grezzi** 2 · **Tema** 3, sistema qualità · **Terzo pacchetto**,
> dopo 3A e 3C. ⚠️ **È il primo lotto che dichiara un dominio sotto E56** — e la regola ha colto
> il proprio autore al primo impiego.

---

## 1. L'apertura

### 1.1 I due grezzi, e il censimento dei fatti (E21)

| Grezzo | Righe | Che cosa porta |
|---|---|---|
| `politica_qualita_e_sicurezza_alimentare_2026.docx` | 119 | `DOC-QA-01` rev. 8: otto impegni **più un nono barrato**, quattro impegni di cultura, food defense e food fraud, nove obiettivi misurabili, comunicazione, riesame, e **quattro annotazioni a margine firmate** |
| `registro_presenze_corsi_HACCP_scaduti.csv` | 105 | lo scadenzario della formazione al 18/05/2026: **96 righe di dato**, 52 dipendenti, 14 corsi, 6 enti formatori, più quattro righe di coda e **un'intestazione ripetuta** |

**Censimento delle 16:11 del 23/08/2026**, dopo l'unione fra i due grezzi: **48 date · 18 nomi
di corso · 6 percentuali · 5 clausole di schema · 3 sigle di documento**, più la struttura del
`.csv` — 96 righe, 52 dipendenti, 30 mansioni, 14 corsi, 6 enti.

⚠️ **I due grezzi non si commentano a vicenda come in 3C: si guardano.** Uno dice che cosa
l'azienda vuole, l'altro se le persone che devono attuarlo siano formate. **È la ragione per cui
il ripacchettamento li ha messi insieme**, e il lotto produce riconciliazioni orizzontali che
nessuno dei due porterebbe da solo.

### 1.2 ⚠️ Un controllo bacato, trovato in apertura e riparato subito (§4)

`verifica_dominio.py` teneva l'insieme dei lotti canonizzati in una **lista di nomi scritta a
mano** — una copia di un fatto il cui padrone è altrove. Si era disallineata **in silenzio**:

| Difetto | Da quando |
|---|---|
| `lotto_02b_autocontrollo_igiene`, **nome morto**: il file fu rinominato `..._analitico` quando 2B si spezzò | **20/08** |
| mancava `lotto_02b_autocontrollo_analitico` | 20/08 |
| mancava `lotto_03c_certificazione_audit` | **22/08, il giorno prima** |
| mancava `r1_riconciliazione_verticale` | 19/08 |

⚠️ **Il costo, se non fosse stato visto**: in apertura di 3B lo script dichiarava
`Certificato_BRCGS_Food_Issue9_Aurora_2026.pdf` **NON CITABILE** il giorno dopo che 3C lo aveva
canonizzato. **Una fonte governante tenuta fuori dalla dichiarazione del dominio è il verso
«troppo stretto» di E56**, che in 2B-bis è costato un 9,1 % gonfiato.

⚠️ **È la seconda volta che questo script mente in silenzio**, e il primo caso è di ieri: il
`\b` in coda alla sigla, che scartava ogni sigla del corpus. **Uno strumento che riconosce testo
si sbaglia sui bordi, non sul centro.**

**Il fix legge l'insieme dal marcatore `# CHIUSO`** in testa all'elenco — lo stesso dato che
`verifica_matrice_lotti.py` già pretende, che non può invecchiare separatamente. ⚠️ **Allenta un
controllo, quindi ha il suo difetto piantato** (§4.9): `collaudo_dominio_canonizzati.py`, **5
casi su 5 nei due versi**, e il caso 2 è il difetto piantato — un lotto senza `# CHIUSO` deve
restare NON CITABILE.

### 1.3 E53: il dominio si verifica, e c'è

**Esito delle 16:03:32 del 23/08/2026**, dopo il fix: **7 fonti citate per sigla nei grezzi, 4
citabili**.

| Fonte citata **per sigla** | Dove | Citabile |
|---|---|---|
| `manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt` | **entrambi** i grezzi | **sì** |
| `Certificato_BRCGS_Food_Issue9_Aurora_2026.pdf` | politica, righe 7 e 16 | **sì** *(dopo il fix)* |
| `IO-05_istruzione_operativa_lavaggio_CIP.docx` · `scheda_sicurezza_detergente_acido_lavaggio_CIP.txt` | politica, riga 108 — la sigla `CIP` dell'obiettivo idrico | **sì** |
| `PRO-QA-08_gestione_reclami_cliente_rev2.docx` | politica, riga 20 | no — lotto 3D · **T146** |
| `procedura_ritiro_prodotto_CRISI_GDO.txt` · `listino_prezzi_canale_GDO_fresco_v3.csv` | registro, riga 97 — la sigla `GDO` | no |

### 1.4 ⚠️ E56 al primo impiego, e la coppia è nata sbagliata

**La dichiarazione del dominio è stata costruita come coppia**, dichiarando anche che cosa
restava fuori: la formazione antinfortunistica *(la governa il `DVR`, lotto 8, non citabile —
**T147**)*, la validità triennale HACCP *(procedura non in archivio)*, gli impegni della
politica *(nessuna fonte del corpus prescrive che cosa una politica debba contenere)*.

⚠️ **E non è bastato.** Col primo taglio il tasso di difetto di produzione dava **63,6 % su 22
note**, il più alto della serie. **La prova del difetto è per ESPRESSIONE, non per numero**, ed
è il test che E56 prescrive:

| Espressione | Che cosa riconosce | Quale fonte del dominio lo governa |
|---|---|---|
| `\bformazion` | **la parola** — e con essa la struttura del registro, chi lo estrae, l'intestazione ripetuta, l'indicatore delle ore | ⚠️ **nessuna**: le fonti governano l'**obbligo** di formare e registrare, non un file e non un KPI |
| `HACCP base` · `HACCP avanzato` | **nomi di corso** del registro | ⚠️ **nessuna**: la loro validità viene dalla «procedura interna (3 anni)» che il corpus non ha |
| `ore/addetto` · `ore per addetto` | l'indicatore | ⚠️ **nessuna**: lo governa la tabella degli obiettivi della politica, che non è prescrittiva |

⚠️ **`\bformazion` da sola pescava TUTTE E QUATTORDICI le scoperte.** Stretta la coppia alle
espressioni che nominano l'obbligo, il punto scende a **36,4 % (8 su 22)**.

⚠️ **E ci si è fermati lì, dopo UNA stretta.** Delle otto residue **tre sono lacune vere** e
cinque le pesca `registro (?:della )?formazion`, che riconosce la **menzione** del registro e non
l'obbligo. **Continuare a restringere a numero visto sarebbe il trucco che E41 vieta, spostato di
un piano** (§4.43): il residuo si dichiara invece di sparire. **T148.**

### 1.5 La riconciliazione verticale arretrata (E37), e il perimetro che si è ristretto con la coppia

| | |
|---|---|
| Riaperte col primo taglio | **15** |
| Riaperte con la coppia stretta | **8** — le sette che cadono restano scritte nell'elenco, commentate |
| **Corrette** agganciando la prescrizione | **1** — `questione-tre-o-quattro-neoassunti-senza-formazione` |

⚠️ **Un perimetro che si stringe senza lasciar traccia non è verificabile**, e le sette cadute
sono elencate nel file con il loro motivo.

### 1.6 La proiezione, e la soglia

| | |
|---|---|
| Note **nuove** proiettate | **~26** |
| Note **riaperte** (E37) | **8** — non contano nella capacità |
| Capacità attesa | 25-35 |
| Tetto di spezzamento (E28) | 40 |
| **Decisione** | **non si spezza** |
| **Note nuove EFFETTIVE** | **22** |

---

## 2. Che cosa il lotto ha trovato

### 2.1 ✅ T107: il nono impegno era barrato, e adesso è registrato come proposta ritirata

L'obbligo scritto in apertura del tema 3 è stato eseguito alla lettera:
`fatto-politica-otto-impegni-e-il-nono-ritirato` scrive **otto** impegni in vigore *(contati)* e
registra il nono — «perseguire la crescita del fatturato quale obiettivo primario
dell'organizzazione» — come **proposta ritirata**, con l'annotazione di chi ne ha chiesto la
rimozione.

⚠️ **È la prova su dati veri che E48 non era un adempimento formale**: nel testo dell'estrattore
congelato il punto 9 sta in fila con gli altri otto, e **nessun controllo deterministico lo
avrebbe fermato** — non c'è niente di sbagliato in una riga che dice quello che dice.

### 2.2 ✅ T102: chiusa, ma non dal lotto che la riga si aspettava

La riga aspettava `registro_presenze_corsi_HACCP_scaduti.csv` **dal tema 7**; il ripacchettamento
lo ha messo qui, accanto alla politica. **Entrambe le gambe sono ora canonizzate e la divergenza
è scritta.**

### 2.3 ⚠️ Le ore di formazione hanno due valori per il 2025 e due obiettivi per il 2026 (T143)

| Documento | Valore **2025** | Obiettivo **2026** |
|---|---|---|
| Politica `DOC-QA-01` rev. 8, **12/01/2026** | **4,2** | **≥ 6** |
| Verbale di riesame, **12/03/2026**, §5.1 e §10.1 | **6,2** | **>= 8** |

⚠️ **La spiegazione ovvia — un dato aggiornato fra gennaio e marzo — non regge**: se il
consuntivo fosse stato corretto al rialzo, l'obiettivo si sarebbe alzato con lui o sarebbe
rimasto fermo. **Invece i due si muovono in direzioni opposte.**

### 2.4 ⚠️ Il registro non dichiara di essere il `MOD-HR-11` (T145)

Il prerequisito `PRP-04` del manuale e il §9.1 della scheda allergeni nominano `MOD-HR-11` come
registro della formazione. **La sigla non compare in nessuna delle 96 righe di questo file.**

⚠️ **È un limite che pesa su tre note del lotto, e ognuna lo dichiara invece di aggirarlo**:
finché quel legame non è scritto, **l'assenza di una riga in questo estratto non prova che la
formazione non sia registrata dove deve**.

### 2.5 Le altre divergenze e i ritrovamenti

| | |
|---|---|
| **T144** | **50 persone** nella politica, **52 nomi distinti** nel registro; tolti cessata, agente e tirocinante restano **49** *(calcolato)* |
| `fatto-in-scadenza-cinque-o-sei` | il file dichiara **5** in scadenza e la colonna ne marca **6**: ⚠️ **il totale ha ragione** — la sesta scade il 18/11, fuori dai novanta giorni — **e la colonna no**. E l'avvertenza «conteggio a mano, verificare» sta sull'**altro** totale, che torna |
| `fatto-diciassette-titoli-scaduti-al-18-05` | 17 titoli su 17 persone diverse; **dieci sono l'HACCP base della stessa sessione del 20/04/2023**, scaduta in blocco |
| `fatto-registro-formazione-intestazione-ripetuta` | l'intestazione ripetuta alla **riga 79** e le quattro righe di coda dentro la tabella |
| `fatto-formazione-allergeni-registrata-biennale` | cinque righe, tutte del 09/10/2025, **registrate a due anni dove la scheda ne prescrive uno** |

### 2.6 ⚠️ Due conteggi miei erano sbagliati, e li ha presi il riconteggio

Il primo censimento del registro dava **101 righe · 57 dipendenti · 16 corsi · 7 enti**: includeva
le quattro righe di coda **e l'intestazione ripetuta**. I numeri veri sono **96 · 52 · 14 · 6**.

⚠️ **E la differenza cambiava una conclusione**: la divergenza con le «50 persone» della politica
passava da **sette** a **due**. ⚠️ **È la specie di E50 applicata a chi scrive il metodo**, non
alle note: un conteggio ottenuto guardando, non marcato, e sbagliato.

---

## 3. L'area `risorse-umane` nasce con questo lotto

Fino al 23/08/2026 il vocabolario chiuso portava `risorse-umane` **senza che nessuna nota lo
usasse**. **L'hub nasce pieno**: dodici note, non una cartella aperta per comodità di
archiviazione. Restano senza hub `sicurezza-ambiente` e `ricerca-sviluppo`.

⚠️ **E la formazione non è solo di quest'area**: è il prerequisito `PRP-04` del sistema HACCP,
quindi ogni nota ha una gamba in `area-qualita`.

---

## 4. I tre giri di giudizio, e il pattern che li ha chiusi

**Tre fette per giro, tre giudici indipendenti a contesto pulito, nessuno col canone.** Il
pacchetto rigenerato ogni volta dopo le correzioni (E33), con l'appendice delle fonti (§4.29).

| Giro | Note | `pulita` | `afferma_oltre` |
|---|---|---|---|
| 1º | 31 | 13 | **18** |
| 2º | 31 | 21 | **10** |
| 3º | 31 | **19** | **12** |

⚠️ **Il terzo giro non e' andato meglio del secondo**, e il ciclo si chiude per E26 **dopo aver
nominato il pattern**, non ripetendo un quarto giro.

### 4.1 I quattro errori di FATTO del primo giro

| Nota | Che cosa diceva | Che cosa dice la fonte |
|---|---|---|
| `questione-ore-formazione-due-valori-per-il-2025` | «i due si muovono in **direzioni opposte**» | ⚠️ **falso**: il target passa da «≥ 6» a «>= 8», **sale** come il consuntivo. **Era l'argomento centrale della nota** |
| `entita-federica-sartori` | «il ruolo **non e' dichiarato in nessuna delle due fonti**» | ⚠️ **falso**: il registro la porta due volte come «**HR e segreteria**» |
| `fatto-squadra-emergenza-antincendio-in-scadenza` | «**le tre righe** `Antincendio livello 2`» | ⚠️ **sono quattro**: la quarta vale fino al **2029** |
| `questione-tre-o-quattro-neoassunti` *(nota preesistente)* | «azione correttiva **scadeva** il 20/02», «non ancora chiusa» | ⚠️ **falso**: e' `Data_chiusura`, e lo `Stato` e' **CHIUSA**. La citazione **troncava la riga** prima di quei campi |

⚠️ **E un ritrovamento che ha riscritto una questione**: il pacchetto conteneva il §7.1 del
verbale, «Organico al 28/02/2026: **50 unita'** (38 produzione, 12 uffici)». **Due documenti
concordano sul cinquanta**, ed e' il registro a censire un'altra cosa. **T144 riscritta.**

### 4.2 ⚠️ Una correzione non era mai entrata, e il secondo giro l'ha ripresa

`area-produzione` e' tornata col **medesimo rilievo**: la correzione era stata scritta, ma lo
script che la applicava **si era fermato su una nota precedente**. ⚠️ **E' il caso pagato in
2A, alla lettera** — *la QA resta verde su una frase sbagliata che e' ancora li'*, perche' la QA
non sa che cosa doveva cambiare. Da li' in poi ogni sostituzione verifica di essere entrata.

### 4.3 ⚠️ IL PATTERN: LA CORREZIONE E' UNA SCRITTURA, E NESSUNO LA GIUDICA COME TALE

**Dei dodici rilievi del terzo giro, almeno SETTE cadono su frasi che al secondo giro non
c'erano: le ha scritte la correzione.** In due forme.

**Forma 1 — la correzione lascia indietro l'intestazione.** Gia' nota: e' E30 piu' E51. Quattro
casi, fra cui un titolo di sezione che concludeva cio' che il corpo dichiara di non sapere.

**Forma 2 — LA CORREZIONE STESSA AFFERMA OLTRE LE FONTI.** ⚠️ **Questa e' nuova**, e sono
quattro casi:

| La frase scritta correggendo | Perche' non regge |
|---|---|
| «Le periodicita' il registro non le enuncia» | la **riga 3** le enuncia: «le scadenze HACCP seguono la procedura interna (3 anni)» |
| «la foto decisiva **non compare in nessuno dei due elenchi**» | il §6 la elenca. ⚠️ **La correzione ha reso FALSA una frase che prima era solo vaga** |
| «le `Note` portano «agg. annuale»» | sta nella colonna **`Scadenza`** |
| «Solo per la prima il registro data l'assenza» | contraddiceva la frase che la precedeva, scritta nello stesso turno |

⚠️ **E30, E39, E42 ed E51 guardano tutte all'affermazione VECCHIA e a dove sopravvive.
Nessuna guarda alla frase NUOVA che la correzione scrive** — e la Forma 2 e' esattamente
quella: nasce nel gesto di correggere, non passa da nessuna rilettura perche' e' appena stata
scritta con attenzione, e afferma oltre le fonti.

**Candidato emendamento**, nella forma che il consuntivo suggerisce:

> *Una correzione e' una scrittura, e vale per lei cio' che vale per la nota: prima di
> applicarla si guarda la fonte che dovrebbe sorreggerla. La rilettura del passo 2-bis si fa
> sul testo CORRETTO, non su quello che si stava correggendo.*

⚠️ **Perche' non basta «rileggere di piu'»**, ed e' la stessa ragione di E39: chi scrive la
correzione **sta pensando al rilievo**, e la frase che scrive gli sembra la risposta al rilievo,
non un'affermazione nuova da verificare.

### 4.4 Le segnalazioni respinte, e perche'

| Segnalazione | Perche' respinta |
|---|---|
| le **lacune di copertura** verso documenti del pacchetto — una trentina fra i tre giri | ⚠️ **il giudice non conosce il grafo** (§9.5 passo 5). Accolte le due che portavano un DATO che nessuna nota aveva — l'organico del §7.1 e il §9.5 in cui il verbale nomina la politica. Le altre avrebbero prodotto **doppie padrone**, il difetto che R1 pago' diciassette volte |
| «l'artefatto di ricerca non e' fra le fonti» | **E43 prescrive quella forma**: l'assenza lascia l'artefatto, e la nota vi rimanda |
| «l'hub non cita i documenti che i figli citano» | il giudice stesso lo qualifica non-difetto: **un hub delega col wikilink** |

---

## 5. La revisione col canone: 2 A, 13 B, 5 C — e una diagnosi che ribalta la domanda

Subagente a contesto nuovo col canone e la tabella alias (E45), coi due grezzi aperti per
verificare le A prima di dichiararle.

### 5.1 Le due A, e la prima e' un difetto della SUITE prima che della nota

| | |
|---|---|
| **A1** | `doc-scadenzario-formazione-2026` puntava a **`[[entita-francesca-sartori]]`**: **un nome proprio inventato** — la scheda si chiama `entita-federica-sartori`. ⚠️ **E' lo stesso errore che la tabella alias registra per Vicentini** |
| **A2** | «cinque mansioni distinte *(contate)*»: sono **sei**. Il cinque esce fondendo «Linea 1» e «Linea 1 notte», cosa che la nota non fa per «manutentore notte» |

⚠️ **A1 SI E' RIVELATO UN GUASTO DEL CONTROLLO, non della nota**: `qa_link_integrity` cercava i
wikilink rotti chiamando `Nota.wikilink()`, che per contratto legge **il solo CORPO**. **Il
campo `related` restava fuori** — e `related` porta il rimando **spoke → hub**, cioe' il link
piu' importante che una nota scriva.

**Misurato**: il vault ne portava **due**, e la QA dava **0 ERRORI**. Il secondo,
`fatto-ts-01-fine-vita-dismissione` → `[[fatto-potenza-impegnata-e-preventivo-tunnel]]`, stava
li' **da un lotto precedente**: due note vere fuse in un titolo che non esiste.

⚠️ **Per §4 un controllo bacato non e' un candidato: e' un guasto**, riparato subito. Il fix
aggiunge agganci e ha comunque il suo difetto piantato —
`_collaudo\collaudo_related_rotto.py`, **5 casi su 5 nei due versi**, e il caso 1 e' il
piantato. ⚠️ **A trovarlo e' stata la revisione col canone, non la suite**, e questo e' il
punto: un nome che non esiste non richiede giudizio, richiede un confronto con un elenco.

### 5.2 Le tredici B: otto scrivibili, cinque bloccate dal 9-bis

**Scritte nel canone**, sezione datata 23/08/2026:

| | |
|---|---|
| **E1** | reclami per milione: **9,4 su confezioni** contro **0,89 su pezzi**, e la conversione **non chiude** — col rapporto 10,56 *(calcolato)* il target della politica varrebbe 0,76, non 0,85. ⚠️ **C3 di 3A dava questa gamba per non scrivibile: la politica la rende scrivibile oggi** |
| **E2** | **due tabelle di obiettivi 2026 che non si mappano** — due soli indicatori in comune, e su entrambi i valori divergono — mentre il verbale riconferma la politica «senza modifiche». **E' C4 di 3A con un terzo documento** |
| **E3** | il **97,32 %** come «Valore 2025» in un documento **emesso il 12/01/2026**, quando l'audit e' del **17-18/02** |
| **E4** | «la riunione di riesame **di gennaio**», che nell'archivio si tiene **a marzo** tutte e tre le volte |
| **E5** | il registro **non porta nessuna riga del 2026**: zero su 96, e **si contraddice da solo** annotando nelle `Note` un aggiornamento «fatto 03/2026» |
| **E6** | la sessione di recupero HACCP ha **tre date**: 21/05 nell'azione `A9`, 21/05 «tenuta» nella scheda, **09/06 «prenotata»** nel registro, estratto tre giorni prima della scadenza **dalla stessa responsabile** |
| **E7** | «Attestati HACCP in scadenza: **n. 5**» dichiarato alla direzione, contro i **dieci** del registro — e **da quel cinque discende `A9`**, dimensionata sulla meta' del problema |
| **E8/E13** | l'organico, e il quarto quasi-omografo **Peruzzi** |

🚫 **Cinque restano bloccate**, e una e' pesante: **il `MOD-HR-11` ESISTE in archivio, ed e' un
altro documento** — `verbale_formazione_sicurezza_lavoratori_accordo_stato_regioni.txt` porta
«MOD-HR-11 rev.2 - registro formazione» **e** chiama «scadenzario formazione MOD-HR-11» proprio
il file di questo lotto. ⚠️ **Il legame che TRE note di 3B dichiarano «non affermato da nessuna
fonte» E' affermato**, da un grezzo che il 9-bis rende non citabile. **T149.**

### 5.3 ⚠️ La diagnosi: non sovra-atomizzazione, il contrario

Il revisore ha risposto alla domanda del passo 7 e l'ha ribaltata. **Sulla politica la
spezzatura e' giusta** — sei note per un documento di sei parti, ognuna con una domanda vera
dietro. **Sul registro no, e in due modi:**

- **un fatto con tre padroni**: le quattro righe di coda erano descritte in **tre note diverse**
  senza che una fosse la padrona. Riparato: la padrona e'
  `fatto-registro-formazione-intestazione-ripetuta`, le altre due la citano;
- ⚠️ **cinque righe del registro non avevano nessuna nota**, e la piu' grave e' una **addetta
  alla squadra di emergenza col primo soccorso scaduto da tre mesi** e un «SUBITO» scritto dal
  compilatore — **l'unico di tutto il file** *(contato)*. Nata
  `fatto-tre-righe-del-registro-con-un-obbligo-non-chiuso`, che raccoglie quella, il divieto di
  guida al magazziniere e l'addestramento «DA REGISTRARE».

⚠️ **E la diagnosi vera e' quella che il revisore mette in coda**: *il lotto ha letto benissimo
i due grezzi COME DOCUMENTI, e quasi mai uno contro il vault che aveva intorno.* **Sette delle
otto divergenze scrivibili nascono dall'accostamento col verbale di riesame**, canonizzato il
giorno prima. **La riconciliazione orizzontale (E2) e' il passo che questo lotto ha fatto peggio**,
e non e' un caso: il grezzo e' denso, e dentro un file denso si conta invece di leggere.

---

## 6. I numeri di chiusura (E44), tutti da script e con l'ora

**Misure fra le 18:39 e le 18:42 del 23/08/2026, dopo l'ultima scrittura e dopo la nota-sessione.**

| Misura | Valore | Strumento |
|---|---|---|
| **QA, perimetro lotto** | **0 ERRORI, 43 avvisi** — esito **GIALLO** | `qa_all.py` |
| **QA, perimetro vault** | **111 ERRORI, 286 avvisi** | `qa_all.py` |
| di cui grezzi non ancora canonizzati | **109** | |
| di cui aree senza hub | **2** — ricerca-sviluppo, sicurezza-ambiente | |
| di cui **rilievi di merito** | **0** | |
| **Collaudi** | **7 su 7**: suite 18+9, due tassi 5, CSV 7, doppie padrone 3, locator eml 3, **dominio canonizzati 5**, **related rotto 5** | `_collaudo\` |
| **Emendamenti** | registro e manuale **concordano a 58** | `verifica_emendamenti.py` |
| **Matrice** | **completa e disgiunta**: 160 grezzi, 27 elenchi | `verifica_matrice_lotti.py` |
| **Tracciamento** | **157 righe**, da T1 a T157 — 7 riconciliate · 74 aperte dichiarate · 17 chiuse · 59 tracciate | `conta_tracciamento.py` |
| **Vault** | **386 note**, di cui **350 di contenuto** | `conta_stato.py` |
| **Grezzi canonizzati** | **51 su 160** — ne restano **109** | `conta_stato.py` |
| **Questioni aperte** (`type: conflitto`) | **53** | `conta_stato.py` |

⚠️ **Il vault scende da 114 a 111 errori, e la differenza e' esattamente cio' che il lotto ha
fatto**: due grezzi canonizzati piu' **l'hub `area-risorse-umane`**, che chiude una delle tre
aree scoperte. **Nessun rilievo di merito introdotto, e i due link rotti che c'erano sono stati
tolti** — uno era di un lotto precedente.

### 6.1 ⚠️ I due tassi, e perche' il punto della serie non e' quello che lo script da' oggi

| | Punto DICHIARATO | Rimisurato a fine ciclo |
|---|---|---|
| **Tasso di riapertura** *(debito)* | **12,5 %** — 1 corretta su 8 riaperte | invariato |
| **Tasso di difetto di produzione** *(metodo)* | **36,4 %** — 8 su 22 | 26,1 % — 6 su 23 |

⚠️ **Il punto della serie e' 36,4 %, e il 26,1 % non lo sostituisce.** Il secondo numero e'
quello che lo stesso script restituisce **dopo** le correzioni del giudizio e della revisione:
tre note hanno ricevuto la fonte governante perche' la discutevano davvero (E29), e una nota
nuova e' nata. **Ma E41 e' esplicito**: il tasso di produzione misura il lotto **come il ciclo
lo ha prodotto**, e rimisurarlo a correzioni fatte significherebbe far sparire proprio cio' che
la misura esiste per mostrare.

**La serie, con questo punto:**

| Lotto | Dominio | Difetto di produzione |
|---|---|---|
| R1 | perimetro CCP e tarature | **57,7 %** |
| 2A | `cip` | **3,3 %** |
| 2B | `acqua` | **0,0 %** su 27 |
| 2B-bis | `allergeni` | **9,1 %** su 33 |
| 3A | — | **NON MISURATO** |
| 3C | `certificazione` | **38,7 %** su 31 — con riserva |
| **3B** | **`formazione`** | **36,4 %** su 22 — ⚠️ **con la riserva del §1.4** |

---

## 7. Che cosa il gate deve decidere

| | |
|---|---|
| **1. Il candidato emendamento: la correzione e' una scrittura** | ⚠️ **E' il pattern con cui il terzo giro si e' chiuso** (E26), e ha **quattro casi misurati** piu' **tre nel ciclo dedicato**. E30, E39, E42 ed E51 guardano tutte all'affermazione VECCHIA e a dove sopravvive; **nessuna guarda alla frase NUOVA che la correzione scrive**. Forma proposta: *una correzione e' una scrittura, e vale per lei cio' che vale per la nota: prima di applicarla si guarda la fonte che dovrebbe sorreggerla*. ⚠️ **E' una regola sul MODO DI SCRIVERE**, quindi per §4 va al coordinatore prima di entrare in `metodo_03` |
| **2. Il 36,4 % regge come punto della serie?** | Il dominio e' stato **stretto una volta** su una prova per espressione, e poi ci si e' fermati. Delle otto scoperte residue **tre erano lacune vere** e cinque le pesca un'espressione che riconosce la menzione del registro. ⚠️ **Il numero non e' stato rimisurato dopo le correzioni** (E41). **T148** |
| **3. Due controlli bacati in un giorno, e nessuno trovato da uno script** | `verifica_dominio.py` teneva i lotti canonizzati in **una lista scritta a mano**; `qa_link_integrity.py` cercava i wikilink rotti **solo nel corpo**, e il vault ne portava **due** con la QA a zero. ⚠️ **Entrambi sono copie o perimetri**, non logiche sbagliate: **la domanda per il gate e' se ci siano altre copie di stato dentro la suite**. Entrambi riparati con difetto piantato |
| **4. La diagnosi della revisione: E2 e' il passo fatto peggio** | ⚠️ **Sette delle otto divergenze scrivibili nascono dall'accostamento col verbale di riesame**, canonizzato il giorno prima — non dai due grezzi. E **cinque righe del registro non avevano nessuna nota**, fra cui un'addetta alla squadra di emergenza col titolo scaduto. **Il gate decida se serva un passo esplicito**: *prima di chiudere, rileggere il lotto contro le note che il vault ha gia' sullo stesso tema* |
| **5. Il `MOD-HR-11` esiste, ed e' un altro documento** | 🚫 **T149.** Tre note di 3B dichiarano che «nessuna fonte afferma» il legame fra lo scadenzario e il `MOD-HR-11`: **corretto sul loro perimetro, falso sul corpus**. Obbligo esplicito per il lotto che porta il registro del corso sicurezza |
| **6. Il barrato come tratto del corpus** | **T157.** `E48` ha dato lo strumento; **il §6 del canone non ha ancora la riga** che dice a chi legge di aspettarselo. Tre grezzi lo portano |
| **7. Il debito verso i lotti 3D, 8 e quello del corso sicurezza** | **T146** *(PRO-QA-08 nominato dalla politica)*, **T147** *(la formazione antinfortunistica governata dal DVR)*, **T149** e **T156**: quattro righe con obbligo esplicito |

---

## 8. Gli adempimenti di chiusura, eseguiti

- ✅ **Tabella di tracciamento**: T102 e T107 **chiuse**, T126 alla terza stesura, **quindici righe nuove** — T143-T157. Integra a 157.
- ✅ **CSV `matrice_corpus_v1.csv`**: **23 righe** file × fatto per il lotto 3B, stato `fatta`.
- ✅ **`# CHIUSO il 23/08/2026`** in testa all'elenco del lotto.
- ✅ **Canone accresciuto** in sezione datata: **tredici divergenze**, ogni citazione verificata testualmente sulla fonte (E49).
- ✅ **`alias_entita.md`**: classe B, il quarto quasi-omografo Peruzzi; e la riga del registro delle aggiunte, che **dichiara l'errore del nome inventato**.
- ✅ **`registro_emendamenti.md`**: nessun emendamento nuovo da questo lotto — il candidato del §7.1 e' **del gate**, non del lotto.
- ✅ **Nota-sessione** nel journal, e **solo dopo** il blocco dei conteggi (E34).
- ✅ **Misure di chiusura** dopo l'ultima scrittura, ognuna con la sua ora (E44).
