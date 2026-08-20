# Passaggio di consegne — il ruolo di coordinatore

> **Cos'è** · Il documento che permette a una NUOVA chat di coordinamento (Cowork) di
> riprendere il progetto senza perdere nulla di ciò che è stato deciso, e soprattutto
> senza perdere i CRITERI con cui è stato deciso.
> **Perché esiste** · Il repository conserva le decisioni; questo file conserva la
> giurisprudenza — il modo di giudicare che nei documenti non è scritto perché viveva
> nella conversazione.
> **Data** · **21/08/2026, dopo la chiusura del lotto 2B** — l'autocontrollo analitico, il
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
| 4 | `01_metodo/metodo_03_canonizzazione.md` | il manuale supremo della canonizzazione (E1-E44 inclusi) |
| 4-bis | `06_operativo/registro_emendamenti.md` | l'indice genealogico dei **44** emendamenti: chi li ha approvati, quando, dove vivono. ⚠️ Il numero **non si legge a occhio**: lo dà `verifica_emendamenti.py`, che controlla anche che ogni riga punti a una sezione esistente |
| 5 | `06_operativo/matrice_lotti_corpus_v1.md` | il piano dei 12 lotti + registro modifiche + tabella di tracciamento |
| 6 | gli stati: canonizzazione e RAG di produzione | dove siamo, due linee di lavoro, due file |
| 7 | `06_operativo/rapporto_gate_s2.md`, `rapporto_gate_s3.md`, `rapporto_lotto_1a.md`, `rapporto_lotto_1b*` | la storia dei gate |
| 8 | `01_metodo/metodo_02_misurazione.md` (+ addendum) e i verbali in `04_misurazioni/` | i numeri e come sono stati fatti |

**Regola**: se questo file e i documenti divergono, vincono i documenti. Questo file non
crea regole: spiega come si sono applicate.

---

## 3. Dove siamo (21/08/2026)

- **Corpus v1 congelato**: 160 file, manifest SHA-256 v1.1. Intoccabile.
- **Baseline misurate sul grezzo**, stesse 282 domande:
  A (agentico, opus-5) 70,6% · B (RAG semplice, Chroma) 44,7% · C (RAG produzione locale,
  3B su hardware minimo) 14,5% complessivo **e 7,6% sulle 251 rispondibili** — i due
  numeri **non si citano mai separati**.
- **Config C congelata** (`d36d7ce`, impronta `afb58939…`): intoccabile fino a fine S6,
  difetti di formato compresi.
- **Canonizzazione — sei lotti chiusi**: pilota L26130 (22 grezzi) + 1A (7) + 1B (4) + 1C (2)
  + 2A (3) + **2B (3)** = **41 grezzi su 160**, più il lotto di manutenzione R1. I conteggi,
  incollati da `conta_stato.py` il 21/08/2026 **dopo la nota-sessione** (E34) e dopo l'ultima
  scrittura (E44):

<!-- CONTEGGI DEL VAULT — generati da `06_operativo\qa\conta_stato.py` il 2026-08-21.
     Si incollano VERBATIM: non si ricompongono a mano, non si riscrivono in prosa. -->

| Grandezza | Valore |
|---|---|
| Note nel vault | **246** |
| di cui `_index` | 11 |
| di cui note-strumento del progetto | 14 |
| di cui note di diario (`sessione`, `daily`) | 6 |
| **di cui note di contenuto** | **215** |
| Note per cartella | areas 129 · data 29 · entities 25 · docs 22 · code 15 · workspace 9 · projects 8 · concepts 6 · self 1 · outputs 1 · sources 1 |
| Note per `type` | atomica 152 · conflitto 39 · entita 20 · hub 13 · index 11 · sessione 6 · concetto 5 |
| Questioni aperte (`type: conflitto`) | 39 |
| Grezzi in `sources\` | 160 |
| Grezzi citati da almeno una nota | **41** |
| Grezzi restanti | **119** |

- **QA a perimetro vault — misurata il 21/08/2026 alle 00:01:20**, dopo l'ultima scrittura del
  lotto 2B (E44): **123 errori, 193 avvisi**. Frontmatter, link e provenance a **zero errori**;
  la copertura porta tutti e 123 — **119 grezzi non ancora canonizzati, 3 aree senza hub e 1
  rilievo di merito**, il falso positivo delle doppie padrone descritto in §6. ⚠️ **Il totale
  scende per la seconda volta consecutiva** — 128 → 126 → 123 — e scende ogni volta
  **esattamente dei grezzi che il lotto ha canonizzato**. ⚠️ Fra gli avvisi resta il **debito
  dichiarato di E43**, note anteriori alla regola che attestano un'assenza senza artefatto.
- **Il collaudo della suite**: **22 difetti piantati su 22**, su tutte e cinque le vie di
  produzione più il caso negativo, 0 falsi positivi. I due difetti nuovi del gate — l'assenza
  senza artefatto e il fine riga difforme — sono esercitati sulla **via V1**, che ora ne conta
  nove.
- **Pianificazione**: **E31 adottata al gate del lotto 1C** — il budget di lotto è una
  **capacità** (25-35 note di contenuto), non una stima da densità, ed è **provvisoria fino a
  dieci lotti chiusi**. Il piano vale **circa 28-30 lotti**, non dodici; i temi 3-10 si
  ripacchettizzano in apertura, solo il tema 2 è già ridisegnato in 2A/2B/2C.
- **Metodo a 44 emendamenti** (`verifica_emendamenti.py`, non a occhio). Al **gate del lotto
  2A**, il 20/08/2026, ne sono entrati **quattro in un colpo solo** — il massimo finora da un
  singolo gate: **E41** ogni lotto dichiara i due tassi · **E42** la cautela si propaga nello
  stesso turno della qualificazione · **E43** chi dichiara un'assenza lascia l'artefatto della
  ricerca · **E44** le misure di chiusura si prendono dopo l'ultima scrittura e ogni numero
  porta l'ora della propria misura. ⚠️ **Tre dei quattro nascono da un errore commesso, non da
  un'idea**: E42 da una cautela che non ha raggiunto il summary, E43 da due assenze attestate
  senza ricerca, E44 da un numero dichiarato su una misura vecchia di due ore e mezza.
- **Il lotto R1 è APPROVATO** (gate del 19/08/2026). Il rapporto è
  `06_operativo/rapporto_lotto_r1.md`. **Che cosa ha prodotto**, in una riga per tipo: 71 note
  guardate, **41 corrette**, tasso di difetto **57,7 %**, di cui **7 affermavano il falso**;
  tre giri di giudizio (24, 13 e 9 rilievi accolti) e una revisione col canone (**7 A · 3 B ·
  0 C** più **17 doppie padrone**); **tre divergenze nuove nel canone**, due delle quali sul
  manuale HACCP; **dodici righe** di tracciamento nuove; cinque note di contenuto e quattro
  note-strumento nate; lo strumento di E29 con le **36 fonti prescrittive** del corpus.
  ⚠️ **Si è chiuso NOMINANDO un pattern, non con un quarto giro** (E26): è la prima volta che
  quella regola viene esercitata fino in fondo, e ha prodotto la scoperta più utile della
  giornata invece di un'ora in più. Il pattern — **«la cautela non si propaga»** — è ora E39.
- **Il lotto 2A è CHIUSO** (19/08/2026), e il suo rapporto è `06_operativo/rapporto_lotto_02a.md`.
  3 grezzi, **30 note di contenuto** dentro la capacità, QA **0 ERRORI**, **10 note riaperte da
  E37** di cui 4 corrette, **tre giri di giudizio** (12, 7 e 9 rilievi accolti), revisione col
  canone **6 A · 9 B · 0 C**, **nove divergenze nuove nel canone**, **cinque righe** di
  tracciamento nuove e due chiuse.
- **Il lotto 2A è APPROVATO** (gate del 20/08/2026). ⚠️ **L'esperimento ha dato il suo
  verdetto**: tasso di difetto di **produzione 3,3 %** (1 su 30) contro il **57,7 %** di R1,
  stesso criterio, entrambi da script — **l'ipotesi del debito storico REGGE**. ⚠️ Ne discende
  una scelta di pianificazione che il coordinatore ha fissato al gate: **la rete finale non è
  un secondo passaggio sul vault**, è la chiusura delle righe di tracciamento che E37 lascia
  aperte, e si dimensiona su quelle. Con un tasso del 3 % un ripasso generale guarderebbe
  centinaia di note per trovare l'errore in una su trenta: sarebbe il calcolo lineare di 1C in
  un'altra forma.
- **Il lotto 2B è CHIUSO** (20-21/08/2026), ed è arrivato al gate con **tre grezzi su cinque**:
  si è **spezzato in apertura** (E28) perché il conteggio dei fatti proiettava oltre le 40 note,
  e gli allergeni sono passati a **2B-bis**. ⚠️ **Il taglio non passa dove passerebbe guardando
  la dimensione**: la scheda allergeni apre **da sola** un dominio di riconciliazione verticale,
  e tenerla nello stesso lotto del piano dell'acqua avrebbe messo due riconciliazioni in un
  lotto solo. **27 note di contenuto**, dentro la capacità di E31.
- ✅ **T72 è chiusa, ed è la prima riga di tracciamento del progetto chiusa da un lotto
  successivo CON UN DATO** e non con una decisione: l'acqua di rete misura **486 µS/cm**, il
  limite del risciacquo CIP diventa **536**, e risulta **superato in 18 cicli su 28** (ultima
  lettura) o **24** (lettura più alta). ⚠️ **Il numero porta tre condizioni dichiarate**, e la
  più scomoda è che **la risoluzione del log è il doppio della tolleranza del criterio**.
- ⚠️ **E41, terzo punto della serie**: difetto di **produzione 0,0 %** (0 su 27), riapertura
  **60,0 %** (3 su 5). La serie del metodo è ora **57,7 % → 3,3 % → 0,0 %**, e il criterio
  scritto al gate di R1 — «due lotti prima di decidere» — è **soddisfatto**.
- ⚠️ **PROSSIMO: il GATE del lotto 2B**, e porta tre cose da pesare. **(1)** Il giudizio **non
  converge in tre giri** (8, 2 e 3 rilievi accolti) e il rapporto **nomina la specie** invece di
  fare un quarto giro: *l'affermazione universale verificata sul sottoinsieme che l'ha
  suggerita*. **(2)** ⚠️ **La revisione col canone NON è stata eseguita** e il lotto **non si
  dichiara verificato dal canone** — vedi §6. **(3)** Un candidato emendamento sul tasso di
  difetto di produzione. Dopo l'approvazione: **2B-bis**, gli allergeni, col dominio già
  dichiarato e **5 note candidate già misurate**.
- **Poi**: 2B e 2C, il resto della matrice, quindi S6 (misura «dopo» sul vault, con
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
    applicato a se stesso.

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
| Il pacchetto per il giudizio tagliato in fette **senza le fonti** | i giudici confrontavano le note con sé stesse e hanno dichiarato da soli il verdetto **degradato**: il difetto stava fra generatore e giudice, non dentro nessuno dei due (§4.29, lotto R1) |
| Il manuale HACCP **ricopiato invece che linkato** in diciassette note | mentre si agganciavano le note alla fonte che le prescrive, il vault ha guadagnato copie della stessa prescrizione: **wikilink alla padrona più la fonte in `fonti`**, e si riscrive solo il minimo perché la nota regga da sola (lotto R1) |
| Il prompt riutilizzabile rimasto indietro di sedici emendamenti | 1A, 1B e 1C hanno girato con le regole nel testo incollato invece che nello strumento: chi opera **segnala** lo scostamento, chi istruisce lo **colma** (§4.27, 19/08/2026) |
| **Due assenze dichiarate con la formula di E3 senza aver fatto la ricerca** | il registro dato per assente stava in dieci grezzi, uno dei quali era già fonte di quella nota; il valore dato per ignoto stava nel piano di autocontrollo. Le ha trovate la **revisione col canone**, non la QA: su un'assenza lo strato deterministico non ha nulla da cercare (§4.32, lotto 2A) |
| **Una sostituzione di testo fallita in silenzio, e nessuno se ne è accorto** | una correzione del secondo giro non è andata a segno; la QA resta verde su una frase sbagliata che è ancora lì, e l'ha ripresa il giudice al giro dopo. **Chi corregge a programma verifica che la correzione sia entrata**, o la corregge due volte credendo di averla fatta una (lotto 2A) |
| **Il pacchetto del giudizio generato prima della fine delle correzioni** | sei note su quaranta sono state modificate dopo la generazione del primo pacchetto: E33 dice che si genera **per ultimo**, e qui non lo è stato. Nessun rilievo è caduto su testo morto, ma la regola esiste per non doverlo verificare a posteriori (lotto 2A) |

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
- ⚠️ **LA SPECIE NOMINATA AL TERZO GIRO DI 2B: «L'AFFERMAZIONE UNIVERSALE VERIFICATA SUL
  SOTTOINSIEME CHE L'HA SUGGERITA».** «l'unico», «il primo», «il più alto», «nessun altro».
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
  si nomina. **Criterio di decisione, fissato ORA perché nessuno lo riapra a numeri visti: se
  la specie ricompare al TERZO GIRO di giudizio del prossimo lotto — 2B-bis — diventa
  emendamento; se non ricompare, la riga si chiude.** La forma che avrebbe è nel §5.4 del
  rapporto 2B.
- ⚠️ **LA REVISIONE COL CANONE È SCOPERTA DA UN LOTTO, ed è una decisione da prendere al
  gate.** Il passo 7 del ciclo la richiede; le guardie del prompt di sessione dicono
  «`03_valutazione\` non si apre mai», e un subagente lanciato dalla sessione **è** la
  sessione. Il lotto 2B **non si dichiara verificato dal canone**. ⚠️ **Non è una questione di
  diligenza ma di chi ha il permesso**: se il coordinatore vuole che il passo 7 sia eseguito
  dalla sessione operativa, la guardia va riscritta esplicitamente; altrimenti la revisione va
  affidata a una sessione che il coordinatore lancia. **Finché la contraddizione resta, ogni
  lotto chiuderà con quel passo scoperto** — e in 2A quel passo aveva trovato le due assenze
  false, cioè il difetto che nessuno strato deterministico vede.
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
