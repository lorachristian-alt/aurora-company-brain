# Passaggio di consegne — il ruolo di coordinatore

> **Cos'è** · Il documento che permette a una NUOVA chat di coordinamento (Cowork) di
> riprendere il progetto senza perdere nulla di ciò che è stato deciso, e soprattutto
> senza perdere i CRITERI con cui è stato deciso.
> **Perché esiste** · Il repository conserva le decisioni; questo file conserva la
> giurisprudenza — il modo di giudicare che nei documenti non è scritto perché viveva
> nella conversazione.
> **Data** · 19/08/2026, dopo il **gate del lotto 1C** (commit `eb8f035`) e la sessione di
> manutenzione che ne è seguita. ⚠️ L'intestazione diceva ancora «dopo la chiusura del lotto
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
| 4 | `01_metodo/metodo_03_canonizzazione.md` | il manuale supremo della canonizzazione (E1-E35 inclusi) |
| 4-bis | `06_operativo/registro_emendamenti.md` | l'indice genealogico dei **35** emendamenti: chi li ha approvati, quando, dove vivono. ⚠️ Il numero **non si legge a occhio**: lo dà `verifica_emendamenti.py`, che controlla anche che ogni riga punti a una sezione esistente |
| 5 | `06_operativo/matrice_lotti_corpus_v1.md` | il piano dei 12 lotti + registro modifiche + tabella di tracciamento |
| 6 | gli stati: canonizzazione e RAG di produzione | dove siamo, due linee di lavoro, due file |
| 7 | `06_operativo/rapporto_gate_s2.md`, `rapporto_gate_s3.md`, `rapporto_lotto_1a.md`, `rapporto_lotto_1b*` | la storia dei gate |
| 8 | `01_metodo/metodo_02_misurazione.md` (+ addendum) e i verbali in `04_misurazioni/` | i numeri e come sono stati fatti |

**Regola**: se questo file e i documenti divergono, vincono i documenti. Questo file non
crea regole: spiega come si sono applicate.

---

## 3. Dove siamo (19/08/2026)

- **Corpus v1 congelato**: 160 file, manifest SHA-256 v1.1. Intoccabile.
- **Baseline misurate sul grezzo**, stesse 282 domande:
  A (agentico, opus-5) 70,6% · B (RAG semplice, Chroma) 44,7% · C (RAG produzione locale,
  3B su hardware minimo) 14,5% complessivo **e 7,6% sulle 251 rispondibili** — i due
  numeri **non si citano mai separati**.
- **Config C congelata** (`d36d7ce`, impronta `afb58939…`): intoccabile fino a fine S6,
  difetti di formato compresi.
- **Canonizzazione — quattro lotti chiusi**: pilota L26130 (22 grezzi) + 1A (7) + 1B (4) +
  1C (2) = **35 grezzi su 160**. I conteggi, incollati da `conta_stato.py` il 19/08/2026:

<!-- CONTEGGI DEL VAULT — generati da `06_operativo\qa\conta_stato.py` il 2026-08-19.
     Si incollano VERBATIM: non si ricompongono a mano, non si riscrivono in prosa. -->

| Grandezza | Valore |
|---|---|
| Note nel vault | **173** |
| di cui `_index` | 11 |
| di cui note-strumento del progetto | 6 |
| di cui note di diario (`sessione`, `daily`) | 3 |
| **di cui note di contenuto** | **153** |
| Note per cartella | areas 93 · entities 22 · data 22 · projects 8 · docs 7 · code 7 · workspace 6 · concepts 5 · self 1 · outputs 1 · sources 1 |
| Note per `type` | atomica 93 · conflitto 32 · entita 18 · hub 12 · index 11 · concetto 4 · sessione 3 |
| Questioni aperte (`type: conflitto`) | 32 |
| Grezzi in `sources\` | 160 |
| Grezzi citati da almeno una nota | **35** |
| Grezzi restanti | **125** |

- **QA a perimetro vault**: frontmatter, link e provenance a **zero errori**; la copertura è
  rossa solo per **incompletezza** — 125 grezzi non ancora canonizzati e 3 aree senza hub.
  Nessun errore residuo è un difetto delle note che esistono.
- **Pianificazione**: **E31 adottata al gate del lotto 1C** — il budget di lotto è una
  **capacità** (25-35 note di contenuto), non una stima da densità, ed è **provvisoria fino a
  dieci lotti chiusi**. Il piano vale **circa 28-30 lotti**, non dodici; i temi 3-10 si
  ripacchettizzano in apertura, solo il tema 2 è già ridisegnato in 2A/2B/2C.
- **Metodo a 35 emendamenti** (`verifica_emendamenti.py`): E34 — la nota-sessione entra nel
  rituale di chiusura e il blocco dei conteggi si genera dopo di essa — ed E35 — esiste il
  **lotto di manutenzione** — sono entrati il 19/08/2026, per ordine diretto del coordinatore.
- **PROSSIMO: l'apertura del lotto R1, la riconciliazione verticale.** ⚠️ Non «una decisione»,
  che era vero prima del gate 1C e non lo è più: **la decisione è presa, e il gate l'ha
  presa.** Nel vault ci sono 30 note che nominano un CCP senza citare il manuale HACCP che lo
  prescrive, e in 1C quattro su undici **dichiaravano mancante ciò che il manuale contiene**:
  non sono incomplete, affermano il falso, e la misura «dopo» girerebbe su quelle. R1 è il
  primo **lotto di manutenzione** (E35): perimetro di sole note generato da script, tre numeri
  nel rapporto — note guardate, note corrette, tasso di difetto — e il rapporto va al
  coordinatore **prima** che il titolare approvi, perché quel tasso decide se il ripasso va
  rifatto a fine corsa.
- **Poi**: il tema 2, il resto della matrice, quindi S6 (misura «dopo» sul vault, con
  `predizioni.md` pre-registrato) e S7 (pubblicazione).

---

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

---

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
| Il prompt riutilizzabile rimasto indietro di sedici emendamenti | 1A, 1B e 1C hanno girato con le regole nel testo incollato invece che nello strumento: chi opera **segnala** lo scostamento, chi istruisce lo **colma** (§4.27, 19/08/2026) |

---

## 6. Vigilanze aperte (da tenere d'occhio al prossimo gate)

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
