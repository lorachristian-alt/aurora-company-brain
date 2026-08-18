# Decision log — Aurora Food Group (simulazione)

Formato: data · decisione · motivo. Si aggiunge in coda, non si riscrive.

- **2026-08-14** · Baseline A (agentico) e B (RAG a embedding) misurate sul corpus
  grezzo a 159 file · ultima finestra utile prima di organizzare l'archivio.
- **2026-08-15** · Corpus v1 CONGELATO con manifest SHA-256
  (`06_operativo/manifest_corpus_v1.json`) · ogni numero deve essere vincolato a un
  corpus verificabile.
- **2026-08-15** · Espansione dell'archivio RINVIATA a corpus v2 · prima si chiude il
  ciclo end-to-end sui 159: una variabile alla volta.
- **2026-08-15** · Ciclo end-to-end sul corpus v1 come primo deliverable ·
  verticale prima di orizzontale; il metodo si valida su una fetta completa.
- **2026-08-15** · Documenti-strumento ristrutturati SENZA toccare prompt congelati e
  valori verificati; divulgazione affidata a guide e LEGGIMI · leggibilità senza
  rischio metodologico.
- **2026-08-15** · Dataset di valutazione intoccabile nel contenuto · ogni risposta è
  verificata fatto per fatto; riscriverla invaliderebbe il test.
- **2026-08-15** · Naming e guide in italiano, abstract inglese nel README · il
  destinatario che firma è il titolare di PMI italiana.
- **2026-08-15** · Chroma = metro (config B, congelata), Qdrant = motore (config C di
  produzione) · non si cambia strumento a metà esperimento.
- **2026-08-15** · Notion solo come fonte IN ENTRATA (inbound) · coerenza col pitch
  GDPR «i dati entrano, non escono»; fatti nuovi solo da corpus v2.
- **2026-08-15** · Baseline C sul corpus grezzo PRIMA della canonizzazione · ultima
  finestra utile; permetterà il confronto prima/dopo su tre configurazioni.
- **2026-08-15** · Riorganizzazione del repository in tassonomia numerata 00-06 ·
  ordine professionale e comprensibile a distanza di un anno; mappa dei nomi storici
  in `00_INIZIA_QUI.md`.
- **2026-08-15** · Modello di lavoro: Cowork = cervello, terminale = mani · le sessioni
  operative girano solo in Claude Code, aperte nella cartella giusta.
- **2026-08-15** · Perimetro della misura «dopo» fissato in anticipo (addendum in
  metodo_02): si misura l'intero vault esclusa `.obsidian\`, grezzi copiati compresi;
  indice B nuovo, estrattore di testo invariato · il perimetro si definisce prima che
  esista l'oggetto, non al momento.
- **2026-08-15** · Ogni cartella del vault avrà una nota `_index` (porta della
  cartella, frontmatter `type: index`): ogni nota deve restare raggiungibile lungo
  llms.txt → `_index` → hub → nota; gli `_index` sono esentati dalla regola degli
  orfani e non contano nel minimo di wikilink · elimina strutturalmente le note
  orfane e dà all'AI un percorso completo verso qualsiasi documento; regola
  vincolante per metodo_03 (Sessione 1).
- **2026-08-15** · `.gitattributes` in radice con `* -text`: git non converte i line
  ending su nessun file · `core.autocrlf=true` avrebbe riscritto LF→CRLF al checkout,
  cambiando i byte dei grezzi in `02_corpus/` e mandando fuori sincrono gli SHA-256 del
  manifest. Il corpus è congelato byte per byte, non riga per riga.
- **2026-08-15** · Postazione di lavoro: Antigravity (IDE) come plancia, con Claude
  Code nel terminale integrato; la chat Cowork resta il cervello · l'agente nativo
  dell'IDE non scrive mai su repo o vault (spettatore); il perimetro resta la
  cartella del terminale; format-on-save disattivato per proteggere corpus e
  verbali di misura dagli auto-ritocchi dell'editor.
- **2026-08-15** · Remote git agganciato: repository PRIVATO
  `github.com/lorachristian-alt/aurora-company-brain` (push di main + tag) ·
  backup fuori macchina da subito; visibilità pubblica solo in Sessione 7, a
  misure completate.
- **2026-08-16** · Sessione 1 chiusa: `metodo_03_canonizzazione.md` approvato al gate,
  con allegato `alias_entita.md` · il manuale governa le Sessioni 2 e 4-5; nessuna nota
  scritta, il vault non è stato toccato.
- **2026-08-16** · `tassonomia_vault.md` è il PADRONE del criterio di appartenenza delle
  11 cartelle; metodo_03 decide solo gli spareggi e non ridefinisce le cartelle · un
  fatto, un padrone: due descrizioni delle stesse cartelle divergerebbero in un mese.
- **2026-08-16** · Naming delle note: `<prefisso-di-dominio>-<slug>` in kebab-case ASCII,
  senza date, nomi unici in tutto il vault · il prefisso dice il dominio del soggetto e
  `type` dice il genere di nota, così non serve un prefisso `hub-`.
- **2026-08-16** · Campo `fonti`: nomi file esatti nel frontmatter (chiave macchina,
  validata contro il manifest) + locator puntuale nel corpo con **grammatica chiusa**,
  una forma per formato · senza grammatica il controllo «il locator punta davvero lì»
  non è scrivibile; con locator generico la provenance deve rileggere file interi.
- **2026-08-16** · Vocabolario `area` a DIECI valori, più fine delle sette aree-cartella
  della tassonomia, chiuso e validato come ERRORE bloccante, con tabella
  valore→raggruppamento→hub · il filtro macchina ha bisogno di grana più fine della
  vetrina; `sicurezza-ambiente` e `direzione` hanno documenti e domande proprie nel
  corpus e in `amministrazione` renderebbero quel filtro cieco. `direzione` è hub
  autonomo in `areas\` e non un aggancio a `self\`: il riesame della direzione è una
  cadenza obbligata da BRCGS/IFS, cioè una responsabilità che non finisce.
- **2026-08-16** · Campo `stato` con vocabolario per posizione: `attivo|chiuso` sulla
  nota-progetto (`type: hub` in `projects\`), `risolto|aperto` su tutto il resto ·
  identificare la nota-progetto da cartella+type evita di aggiungere un nono `type`.
- **2026-08-16** · Soglia della nota atomica: 300 parole obiettivo, 350 tetto duro ·
  un tetto secco a 300 costringerebbe a spezzare fatti che stanno in 320, producendo
  note-frammento che il retrieval fatica a interpretare.
- **2026-08-16** · DIVERGENZA CONSAPEVOLE dalla specifica: minimo wikilink per nota = **2**,
  non 3 · a 3, su note brevi il terzo link si inventa pur di far tacere la QA, e un link
  falso costa più di un link mancante. Resta un AVVISO, mai un errore bloccante.
- **2026-08-16** · DIVERGENZA CONSAPEVOLE: il confronto col canone NON sta dentro
  `qa_all.py` · richiede di leggere il canone (che nel vault non entra) e di giudicare
  se una nota «copre» un fatto: è un verdetto del revisore indipendente, non un exit
  code. Un fatto chiave senza padrona resta bloccante come un ERRORE, ma per mano di una
  persona. Regola d'oro 5: nessun numero dichiarato senza uno script che l'ha ricontato.
- **2026-08-16** · Showcase FUORI dal vault (`06_operativo\showcase\`), llms.txt unico
  derivato dentro · le 11 cartelle sono fisse e il perimetro della misura «dopo» è
  fissato da metodo_02: un derivato che contiene l'esito della QA e i fatti del canone
  coperti, dentro l'archivio misurato, misurerebbe un archivio con parte delle risposte.
- **2026-08-16** · Sorgenti degli strumenti in `06_operativo\qa\`, in `code\` solo le note
  che li documentano · centinaia di righe di Python dentro il perimetro misurato sono
  rumore che il retrieval deve scartare a ogni interrogazione.
- **2026-08-16** · Le note NON traslocano: chi cambia natura cambia `stato` e passa il
  testimone con un wikilink; unica eccezione la promozione da `workspace\`, mai per il
  journal · percorso stabile = fonte stabile: uno spostamento rompe i wikilink, cambia
  llms.txt, lascia il payload Qdrant su un percorso morto e rende la storia git illeggibile.
- **2026-08-16** · La QA riporta e non corregge; controlli `--perimetro lotto | vault` ·
  senza il perimetro di lotto la fetta pilota fallirebbe sempre sui controlli globali, e
  la reazione naturale sarebbe ammorbidire la QA — che lo stop-loss vieta per nome.
- **2026-08-16** · CATEGORIA B registrata nel canone (sezione datata 16/08): data della
  riunione di direzione (convocata 12/05 ore 9:30, tenuta 13/05 secondo tre segnali
  interni concordi) e data di apertura di REC-2026-011 (12/05 sulla scheda, 13/05 secondo
  mail e trascrizione) · divergenze reali non elencate nei tre gruppi, trovate scrivendo
  il manuale. Grezzi intoccati.
- **2026-08-16** · WATCH-ITEM per la Sessione 2: la frase che decodifica il formato del
  lotto («giorno giuliano 130 del 2026») nell'hub `lotto-l26130` dovrà passare la
  provenance · se nessun grezzo spiega la regola di composizione del codice, va
  riformulata come inferenza dichiarata. Lo verifica il pilota.
- **2026-08-17** · **Sessione 2 CHIUSA: fetta pilota L26130 canonizzata, design validato.**
  22 grezzi → 63 note (46 di contenuto, 11 `_index`, 6 note-strumento), QA di lotto verde
  (0 errori, 33 avvisi motivati), copertura 22/22, suite QA collaudata (5 difetti piantati su
  5 trovati, 0 falsi positivi), giudizio di provenance su tutte le 46 note candidate (42
  pulite), revisione indipendente col canone (13 A · 5 B · 10 C, tutte chiuse) · **il design
  regge: si può industrializzare nelle Sessioni 4-5.**
- **2026-08-17** · S2 · Mini-misura di fumo su 30 domande, numeri NON ufficiali: **28/30
  corrette contro 23/30 della baseline A sugli stessi id, fonti 30/30 contro 27/30, zero
  peggioramenti** · stesso modello (`claude-opus-5`) e un solo blocco contro dieci, quindi due
  asimmetrie a favore della fumo, entrambe dichiarate nel verbale. Il campione dice che il
  design regge, non quanto rende.
- **2026-08-17** · S2, chiusura · **Il giudizio di provenance rieseguito su tutto ha trovato
  una fuga di canone**: una nota affermava una divergenza sui pezzi per cartone che nessuna
  sua fonte conteneva, e che veniva dal report del revisore — l'unico ruolo che il canone lo
  riceve · rimossa. È la prova che E9 (rigiudicare le note nate dalle correzioni) non è
  burocrazia: quella nota era stata scritta dopo il primo giro di giudizio.
- **2026-08-17** · S2, chiusura · **Il pass `--perimetro vault` è rosso e si lascia rosso**:
  138 grezzi non ancora canonizzati e note-strumento staccate dal grafo · un lotto si chiude
  con il perimetro di lotto verde; il vault verde è il traguardo delle Sessioni 4-5.
  **Da decidere in S4:** agganciare le note-strumento al grafo o escludere `code\` dal
  controllo di componente unica come `workspace\` e `sources\`.
- **2026-08-17** · S2, gate · **Diciannove emendamenti a metodo_03 approvati e applicati.**
  Tre regole nuove (E1 esenzione da `fonti` per le note-strumento; E2 riconciliazione
  incrociata dei numeri fra fonti del lotto; E3 divieto di dichiarare un'assenza senza
  ricerca su tutto `sources\`), cinque refusi (E4 grammatica `.xlsx`, E14 coerenza interna
  sugli orari, E15 e E16 due esempi compilati che non corrispondevano ai file, E19 il piè di
  pagina di un `.log` non era puntabile) e undici chiarimenti · il pilota è servito
  esattamente a questo: far emergere dove la specifica non regge all'uso.
- **2026-08-17** · S2, gate · **E1 vale per la NOTA-STRUMENTO, non per la cartella `code\`.**
  Il discrimine è il prefisso `script-`: una nota che documenterà un'automazione aziendale —
  OCR dei documenti di trasporto, integrazione EDI-ERP — parla di un fatto di Aurora, ha
  grezzi che la attestano e resta a schema pieno · senza questa distinzione l'esenzione
  diventerebbe una porta aperta su un'intera cartella. Nel corpo della nota-strumento va il
  percorso del sorgente nel repository; queste note restano fuori dallo strato di giudizio e
  si rivedono a occhio a ogni gate.
- **2026-08-17** · S2, gate · **E18 — se una nota stabilisce una regola decisionale, il
  `summary` la enuncia.** ⚠️ **Origine della regola:** la riserva del giudice su Q237 nella
  misura di fumo, che ha notato come la prevalenza del datalogger sul registro cartaceo fosse
  applicata nella conclusione ma non enunciata · **applicata come regola generale di vault a
  tutte le note in cui ricorre, non come ritocco alla singola nota che una domanda della fumo
  ha toccato**: adattare l'archivio alle domande viste sarebbe adattare l'oggetto misurato
  alla misura. Il `summary` è ciò che il retrieval mostra per primo: una regola che vive solo
  nel corpo non arriva a chi legge la risposta.
- **2026-08-17** · S2, gate · **Il budget di un lotto si misura sulle note di CONTENUTO** —
  esclusi gli `_index`, che nascono per cartella toccata, e le note-strumento — **e si fissa
  lotto per lotto nel prompt di quel lotto**, non una volta per tutte nel manuale · dipende da
  quanti fatti portano i grezzi scelti, che è cosa diversa dal loro numero. Densità misurata
  sul pilota: **41 note di contenuto su 22 grezzi**, poco meno di due note per documento.
- **2026-08-16** · S2 · **DA DECIDERE IN PRE-REGISTRAZIONE, PRIMA DELLA SESSIONE 6: come
  conta `fonti_corrette` quando la risposta cita una NOTA del vault invece del grezzo.**
  Nella misura di fumo è successo una volta (Q019: citati insieme il manuale HACCP e
  `docs\doc-ccp2-limite-critico.md`). Nella misura «dopo» il perimetro è l'intero vault, quindi
  il caso sarà frequente, mentre nella baseline A esistevano solo grezzi: se la nota conta
  come fonte corretta, i due numeri misurano cose diverse · **proposta da discutere: la fonte
  che conta resta il grezzo, la nota è navigazione e non provenienza.** Non è una decisione
  presa: va presa prima di misurare, non dopo aver visto i numeri.
- **2026-08-16** · S2 · Nel verbale del giudice della fumo, la citazione di Q019 è descritta
  come «documento del canone»: **è invece una nota del vault**, e il canone era fisicamente
  fuori dal perimetro montato del rispondente (`--add-dir` solo su `04_misurazioni\`) ·
  l'interpretazione è corretta nel rapporto di gate e qui; **il testo del giudice NON è stato
  toccato** e resta testimonianza di come un valutatore che vede solo i nomi dei file
  interpreta un percorso `docs\….md`.
- **2026-08-16** · S2 · Q237 riesaminata a occhio al gate, come previsto: esito **corretta**
  confermato. La riserva del giudice — «la prevalenza è applicata nella conclusione ma non
  enunciata come regola» — è fondata ma riguarda la forma, non la sostanza · vale però come
  segnale: la regola di prevalenza datalogger/cartaceo è scritta nel corpo di
  `fatto-registro-cartaceo-mod-qa-12` e non è arrivata nella risposta, quindi va portata nel
  `summary`, che è ciò che il retrieval mostra per primo.
- **2026-08-16** · S2 · **Nessuna modifica al prompt del rispondente per la Sessione 6 sulla
  base degli esiti della fumo** · fra «prima» e «dopo» cambia solo la forma dell'archivio:
  toccare lo strumento di misura dopo aver visto i numeri rende i due lati non confrontabili.
  Il P1 resta quello congelato in metodo_02.
- **2026-08-16** · S2 · I cinque conflitti non registrati trovati dal rispondente sono stati
  classificati con script sulle gambe di ciascuno: **due sono buchi di canonizzazione** (tutte
  le gambe in fetta — scarti al riavvio 348 contro 330; NC-2026-102 che scrive «conferma
  origine interna» mentre il laboratorio dichiara di non attribuire l'origine) e **tre vanno
  in lista di tracciamento per S4-S5** (almeno una gamba fuori fetta) · il quaderno del
  capoturno `appunti_capoturno_quaderno_linea1_OCR.txt` è la gamba mancante di tutti e tre:
  va messo in cima al lotto che tocca la Linea 1.
- **2026-08-16** · S2 · Categoria C del revisore, annotate perché non tornino al lotto dopo:
  8.940 contro 5.580 pezzi; i 1.000 pezzi non rendicontati con gli addendi dichiarati; la
  finestra 14:20:07-14:44:37 contro le 14:18-14:47 della NC; il «74,5 conforme» lasciato agli
  atti; `E-214 GAS` contro `AL-217`; la data della riunione 13/05 col nome del file 12_05; il
  codice di lotto parziale `L26130` del reclamo; le due coppie di duplicati assorbite in una
  nota sola; il `-999.9` con flag `FAULT` trattato come sonda guasta e non come temperatura;
  gli straordinari di Linea 2, le cui fonti padrone sono fuori dal perimetro del lotto.
- **2026-08-15** · Il rituale di chiusura di ogni sessione diventa di QUATTRO gesti:
  stato, decision log, commit, `git push` · la Sessione 1 ha committato senza pushare
  e il lavoro è rimasto su un solo disco; il push entra nel principio 5 della scaletta
  (sorgente) ed è propagato a metodo_03 §9.5, 00_INIZIA_QUI e LEGGIMI operativo.
- **2026-08-17** · Il **vault sotto git privato SLITTA a fine progetto, prima della v2** ·
  decisione del titolare. Registrata qui perché non venga riaperta a ogni sessione: fino
  ad allora il vault vive fuori dal versionamento, con il backup zip di fine sessione
  previsto dalle Sessioni 4-5.
- **2026-08-17** · S3 · **Configurazione C congelata e PUSHATA prima di costruire
  l'indice** (`config_c.json`, impronta `afb5893936f27a8a6c0a276e34206a9d87b9052b21ba59f8f8f8e3817e61b0e8`,
  commit `d36d7ce` delle 12:44) · la pre-registrazione vale solo se è verificabile da
  fuori: l'impronta è dentro il manifest dell'indice e dentro ognuna delle 282 tracce.
- **2026-08-17** · S3 · **La prosa si corregge, il config no** · durante la costruzione
  dell'indice stavo aggiungendo a `config_c.json` un'avvertenza di solo commento: ogni
  byte entra nell'impronta, e l'indice in costruzione avrebbe smesso di corrispondere al
  config che dichiarava di averlo prodotto. Revocata (`git diff` a zero); l'avvertenza è
  finita in `metodo_04`. **Il meccanismo di congelamento ha funzionato contro chi
  l'aveva scritto**, che è l'unico collaudo che conta.
- **2026-08-17** · S3 · Scostamenti da `metodo_04` decisi PRIMA del congelamento, con il
  motivo accanto al valore: reranker `bge-reranker-large` → **`bge-reranker-v2-m3`** (il
  large è inglese/cinese, e il reranker è il pezzo che deve far vincere C su B su un
  archivio italiano); **dedup dei chunk disattivato** (i duplicati sono contenuto,
  metodo_01 §11); **canone e tabella alias fuori dai metadati** (sarebbe un archivio già
  in parte organizzato, cioè ciò che la S6 deve misurare dopo); **niente ramo OCR per i
  PDF** (sonda su tutti e 27: nessuna scansione cieca, sarebbe codice non esercitato).
- **2026-08-17** · S3 · **Il runner scrive TUTTE le fonti citate, anche quelle
  inventate** · filtrarle era banale e disonesto: in A e B il giudice vede le fonti come
  il modello le ha scritte, e ripulire quelle di C le avrebbe dato meno allucinazioni
  **per costruzione**. Costa a C (76 risposte su 282 citano un file fuori contesto) e si
  tiene.
- **2026-08-17** · S3 · **Il generatore misurato è di classe 3B, dichiarato come
  PAVIMENTO prima di misurare** · la macchina ha 7,8 GB di RAM e nessuna GPU, sotto la
  fascia minima che `metodo_04` §8 dichiara per sé. La config di **riferimento** (8B su
  16-32 GB) è documentata e **non è mai stata misurata**: non si racconta come se lo
  fosse, finché qualcuno non la conta.
- **2026-08-17** · S3 · **Il runner si lancia STACCATO dalla shell** (`Start-Process` con
  output su file) · i processi agganciati al terminale muoiono col terminale. Provato sul
  campo: la finestra si è chiusa a metà passata 2 e il processo ha finito da solo — un
  solo avvio nel log, una sola riga di rapporto, fine meno durata = lancio a 21 secondi di
  scarto. La riprendibilità con `fsync` era progettata contro un rischio teorico; il
  rischio si è presentato in forma diversa e la difesa ha retto senza interventi.
- **2026-08-18** · S3, gate · **Baseline C: 14,5% corrette sulle 282 e 7,6% sulle 251
  rispondibili — i due numeri NON si citano mai separati** · delle 41 corrette, 22
  vengono da domande la cui risposta giusta è «il dato non c'è», e il modello ci arriva
  perché **si astiene sempre**, non perché sappia distinguere. Il solo dato complessivo
  racconta una capacità che il sistema non ha. Regola estesa al README e a ogni materiale
  commerciale (scaletta, Sessione 7).
- **2026-08-18** · S3, gate · **La diagnosi: il collo di bottiglia è il generatore, non
  il recupero** · 70,2% di fonti giuste contro 14,5% di risposte giuste, 55,7 punti di
  scarto: nel 70% dei casi il sistema aveva il documento in mano e ha sbagliato lo stesso
  (Q089, Q170, Q209 negano un dato che sta nel file che stanno citando). **Sostituire il
  generatore lasciando la pipeline invariata è l'unico intervento che può spostare questi
  numeri.**
- **2026-08-18** · S3, gate · **Il rischio dominante non sono le allucinazioni: sono le
  75 `parziale`** · vere e non verificabili, il triplo delle 25 allucinazioni. Sulle
  `contraddizione` è sistematico — 14 domande, 11 parziali, **zero corrette**: dà il
  valore giusto e non si accorge mai che nell'archivio ne esiste un altro. **Per
  un'azienda alimentare è il difetto peggiore**: consegna un numero verificabile e chiude
  un'indagine che andava aperta.
- **2026-08-18** · S3, gate · **Rischio-tipo per l'audit: la fattura Pakmatic da 4.912 €
  inventata IDENTICA in Q193 e Q265** · riproducibile a temperatura 0, plausibile, e
  coerente con sé stessa: chi incrociasse le due risposte troverebbe una conferma. È lo
  scenario peggiore davanti a un auditor, ed è anche la prova migliore dell'argomento che
  si vende — si apre la traccia e in trenta secondi si vede che il numero non c'è. **Si
  vende la tracciabilità, non la correttezza.**
- **2026-08-18** · S3, gate · **I guasti di formato della config C sono DIFETTI NOTI
  DELLO STRUMENTO CONGELATO e NON si correggono prima della Sessione 6** · risposta
  vuota, segnaposto letterale, degenerazione in loop, campo `fonti` che esplode in
  frammenti, difetto padrone/derivato del retrieval. Sarebbero tutti banali da sistemare:
  **fra «prima» e «dopo» cambia solo la forma dell'archivio, i bug dello strumento
  compresi**, e un runner migliorato produrrebbe un delta che mescola due cause. Le
  correzioni sono materiale per la config di **riferimento**, dopo S6. La lista di lavoro
  è il §13 del verbale.
- **2026-08-18** · S3, gate · **Tasso di allucinazione: definizione ufficiale =
  `allucinata` + `sbagliata` su `non_rispondibile`**, fissata in `metodo_02` (addendum
  del 18/08) · il giudice del 14/08 non usò MAI il campo `allucinata` (zero righe su 564)
  e ripiegò su `sbagliata`; quello di C l'ha usato. Con due definizioni la colonna non si
  parla. La somma concilia i casi e **dove `allucinata` è vuoto coincide col ripiego: le
  righe A e B non cambiano di una cifra** (A 1/31 = 3,2% · B 0/31 · C 6/31 = 19,4%).
- **2026-08-18** · S3, gate · **`fonti_corrette` nella misura «dopo»: conta il GREZZO, la
  nota è navigazione** · fissata in `metodo_02` (addendum del 18/08). Chiude la questione
  aperta il 16/08 in Sessione 2 (Q019 della mini-misura di fumo). Nella baseline
  esistevano solo grezzi: se la nota contasse come fonte, i due lati del confronto
  misurerebbero cose diverse.
- **2026-08-18** · S3, gate · **`predizioni.md` è OBBLIGATORIO e si committa PRIMA che la
  misura «dopo» parta** · con dentro: `contraddizione` e `multi_hop` attesi in salita,
  `aggregazione` e `calcolo` attesi piatti (**un balzo lì si indaga, non si festeggia**),
  sparizione del difetto padrone/derivato, e il richiamo alle due definizioni sopra. Un
  delta raccontato a posteriori non è una previsione, è una giustificazione.
- **2026-08-18** · S3, gate · **Ordine dei lavori dopo il ciclo: prima la Sessione 6, poi
  la config di riferimento 8B su hardware adeguato** · registrata come **lavoro
  post-ciclo CANDIDATO, non come impegno**. Motivo: cambiare generatore *e* forma
  dell'archivio insieme renderebbe illeggibile il delta di sei sessioni. Una variabile
  alla volta.
- **2026-08-18** · S3, chiusura · **Ogni comando di sistema toccato da un run si dichiara
  al titolare, e si ripristina a fine run** · nato dall'episodio `powercfg`: sospensione e
  ibernazione erano state disattivate per il run notturno e i valori originali non erano
  stati annotati prima di cambiarli, quindi il ripristino è dovuto passare dal titolare.
  Regola e checklist di ripristino scritte nel runbook di `metodo_04` §9. Chi cambia
  l'impostazione spesso non è chi userà la macchina domani.

- **2026-08-18** · S4, gate della matrice · **Matrice dei lotti approvata e congelata prima
  di eseguirla**: i 138 grezzi restanti in **dieci lotti tematici**, ognuno in esattamente
  uno, verificato da `verifica_matrice_lotti.py` (160 su disco, 160 nella matrice, zero
  scoperti, zero doppi) · la pianificazione si congela prima di eseguirla, come il config C
  in S3. Il numero del lotto **e'** l'ordine di esecuzione; il lotto 1 e' imposto dal
  prompt e dal gate S2 §6.2 (il quaderno del capoturno in cima), il lotto 10 e' ultimo
  perche' `kpi-composizione-archivio` dichiara i conteggi del vault.
- **2026-08-18** · S4, gate della matrice · **Due file spostati di lotto dopo averli
  aperti, e il nome ingannava in entrambi i casi** · `Nuova cartella di lavoro.xlsx` non e'
  un file vuoto (contiene «prova estrazione ore», un appunto sulle timbrature e una `SUM`
  mai calcolata): dal lotto rumore al lotto persone. `bolletta_VenetaEnergia_maggio2026.pdf`
  e' la gamba di riconciliazione del costo dell'energia: dal lotto rumore al lotto 1, con i
  consumi dei forni. **Classificare un grezzo dal nome e' lo stesso errore di dichiarare
  un'assenza senza cercarla** (E3).
- **2026-08-18** · S4, gate della matrice · **E20 — le NOTE-STRUMENTO DEL PROGETTO sono
  fuori dal controllo di componente unica**, come gia' erano fuori da `fonti` (E1) e dallo
  strato di giudizio · chiude la decisione lasciata aperta dal gate S2. ⚠️ **Come per E1,
  l'esenzione e' della CLASSE, non della cartella `code\`**: le note di contenuto —
  automazioni aziendali, OCR dei DDT, EDI-ERP — restano dentro il controllo, e se sono
  staccate dal grafo e' un difetto vero. La classe e' **definita una volta sola** in
  metodo_03 §2.4 e in `qa_comune.e_nota_strumento`, e tutte e tre le esenzioni si
  riferiscono a quella: due definizioni della stessa classe divergono in un mese.
  **Scartato** agganciare le note-strumento al grafo: nessuna nota di Aurora ha ragione di
  citare `script-qa-provenance`, e il link sarebbe tappezzeria (divieto 25). **Scartato**
  rimandare al gate finale: le regole QA non si decidono sotto la pressione della chiusura.
- **2026-08-18** · S4, gate della matrice · **Aritmetica di E20, non un'esenzione in piu':
  un `_index` partecipa alla componente unica solo se la sua cartella ha almeno una nota
  valutabile** · escludere le note-strumento lasciava `_index-code` come vertice isolato, e
  lo stesso vale per `_index-outputs` finche' `outputs\` e' vuota. Segnalarli
  significherebbe chiamare difetto il fatto che una cartella e' vuota. Rientrano da soli
  appena la cartella riceve una nota. **Effetto misurato:** `qa_link_integrity --perimetro
  vault` passa da 1 errore a **0 errori, 0 avvisi** sul vault del pilota.
- **2026-08-18** · S4, gate della matrice · **Tabella di tracciamento VIVA delle questioni
  trasversali**, obbligo del titolare · una questione che un lotto apre e un altro completa
  e' il modo piu' facile di perdere un conflitto: nel lotto che la apre sembra lavoro
  finito, in quello che dovrebbe chiuderla nessuno si ricorda che esiste. Vive in
  `matrice_lotti_corpus_v1.md`, si aggiorna alla chiusura di ogni lotto prima del commit, e
  **al gate finale «conflitti chiusi / aperti dichiarati» si prova con quella tabella, non a
  memoria**. Una riga esce solo come `chiusa` o come `aperta dichiarata`; nessuna sparisce.
  Seme iniziale: 16 righe, dalle tre del gate S2 alle divergenze che la matrice prevede.
- **2026-08-18** · S4, gate della matrice · **Il CSV file × fatto di metodo_03 §9.3 si
  compila lotto per lotto e si committa a ogni chiusura di lotto**, non in blocco
  all'apertura di S4 · compilarlo per 138 grezzi significherebbe leggerli tutti prima di
  canonizzarne uno, cioe' fare il lavoro due volte. Lo scostamento e' dichiarato nella
  matrice; a fine corsa il file e' completo come la scaletta lo chiede.
- **2026-08-18** · S4 · **Ritmo delle sessioni di canonizzazione: uno o al massimo DUE
  lotti tematicamente contigui per sessione, mai tre, qualunque cosa dica il contesto** ·
  decisione del titolare. Motivo: la revisione col canone si esegue solo a mente fresca, ed
  e' il pezzo che al pilota ha trovato la fuga di canone. **Il tetto di due non si
  rinegozia.** Il lotto 1 gira da solo, ed e' anche il collaudo del rituale industriale: la
  sua chiusura registra nello stato durata, note prodotte contro budget, esiti di giudizio e
  revisione, contesto residuo. Da li' in poi il ritmo si decide all'apertura su quei dati.

- **2026-08-18** · S4 lotto 1A, chiusura · **I tre conflitti tracciati dal gate S2 sono chiusi,
  e nessuno dei tre si risolve: escono tutti come APERTI DICHIARATI** · il quaderno del
  capoturno ha portato la gamba mancante di tutti e tre, e in nessun caso l'archivio da' un
  vincitore. Verifiche CCP3 del 10/05, pezzi del turno e ora di arrivo dell'officina hanno ora
  la loro nota-questione con tutte le gambe citate.
- **2026-08-18** · S4 lotto 1A · **La scansione del MOD-QA-07 e la sua trascrizione non
  raccontano lo stesso turno** · sull'originale le righe delle 16:00 e delle 17:00 sono barrate
  e vuote, sulla trascrizione destinata alla cartella evidenze per il cliente risultano eseguite
  e conformi, e i due documenti non concordano nemmeno sull'operatore. La trascrizione si mette
  in dubbio da sola. **Trovato rileggendo a occhio l'immagine**, non da uno script: le fonti
  `.jpg` restano il punto cieco dell'estrattore congelato, e il riscontro visivo va fatto ogni
  volta che una nota le cita.
- **2026-08-18** · S4 lotto 1A · **Lo strato di giudizio ha trovato 8 note su 46 che
  affermavano oltre le fonti, tutte e otto fondate** · fra queste due gravi: il metal detector
  dato «a valle del confezionamento» quando la scheda tecnica lo colloca prima, e una
  dichiarazione di assenza falsa sul limite del 2 % di ossigeno residuo — **lo stesso errore che
  il pilota aveva pagato al gate S2 con PRP-09**. Il 2 % e' scritto due volte nel registro delle
  non conformita': la questione ne esce piu' forte, non piu' debole.
- **2026-08-18** · S4 lotto 1A · **Il revisore col canone ha trovato una FUGA DI CANONE** ·
  `doc-scheda-tecnica-af-sn-0450` scriveva «il canone del progetto registra che listino e
  accordo quadro ne dichiarano 12», nominando il canone e portando nel vault un valore che
  nessuna fonte citata contiene. Cancellata, insieme alla versione attenuata in
  `prodotto-af-sn-0450`. **Seconda fuga di canone in due lotti**: non e' un incidente, e' il
  modo tipico in cui chi canonizza sapendo troppo anticipa una divergenza che non ha ancora le
  gambe. ⚠️ **Regola operativa che ne discende: finche' la seconda gamba non e' nel vault, di
  una divergenza non si scrive nulla — nemmeno che esiste.**
- **2026-08-18** · S4 lotto 1A · **Mancava la nota padrona di un fatto del filo rosso**: la
  decisione dell'08/05 di proseguire con la valvola che perdeva, presa in riunione, motivata
  con la promo e **senza verbale**. Viveva come capoverso dentro la nota del fermo del 10/05.
  Ora ha la sua nota, con tre fonti · il test di §5.1 e' netto: a «chi ha deciso di andare
  avanti, quando e perche'?» si risponde con quel fatto **al posto** del fermo, non insieme.
- **2026-08-18** · S4 lotto 1A · **Categoria C, annotate perche' non tornino al lotto dopo**:
  pezzi/cartone 10 contro 12 (una gamba fuori lotto); velocita' nominali 1.250 contro 1.800
  ricavati; 8.940 contro 5.580 contro i 4.100 del quaderno, che pero' dichiara il proprio
  perimetro e non e' una terza stima; domeniche di produzione con le altre gambe fuori lotto;
  organico Linea 2 a 21 persone solo nel piano; separatore CSV incoerente, tre formati di data
  nella stessa colonna, intestazione ripetuta e righe duplicate alla lettera; «riga reinserita
  da export precedente» nel CSV shelf life; degradi OCR del quaderno mai ricostruiti; `E-214
  GAS` contro `AL-217`; le sigle `DB` ed `EC` senza nome. ⚠️ E una undicesima: citare
  `alias_entita.md` nel corpo di una nota **non e' metodo dentro il vault** — metodo_03 §3.1 fa
  esattamente lo stesso nel proprio esempio compilato.
- **2026-08-18** · S4 lotto 1A · **Zero rilievi di sovra-atomizzazione** su 18 note campionate
  dai quattro documenti multi-fatto, contro le otto richieste · la guardia chiesta dal titolare
  al gate della matrice ha dato esito negativo: le note nate dai documenti densi sono tutte
  agganciabili a una domanda plausibile. La densita' di 5,7 note per grezzo e' dei documenti,
  non del metodo.
- **2026-08-18** · S4 lotto 1A · **I fine riga si preservano quando si riscrive un file con uno
  script** · riscrivendo il canone e la matrice con Python su Windows i `
` sono diventati
  `
`, e un file con 285 righe invariate e' comparso come interamente modificato. Il repo ha
  `.gitattributes` con `* -text` proprio perche' i byte contano. **Verifica adottata:** dopo ogni
  riscrittura da script, `diff` contro la copia precedente sulle righe preesistenti, e ripristino
  dei file cambiati nei soli fine riga.

- **2026-08-18** · S4 lotto 1A · **Il RI-GIUDIZIO ha trovato altre 8 note che affermavano
  oltre le fonti, e tutte e otto avevano lo stesso difetto**: conoscenza vera dell'archivio
  scritta in una nota che **non citava il documento che la porta** · registro NC, MOD-PR-04,
  piano di produzione, trascrizione della riunione. Non e' invenzione, e' provenienza mancante
  — ed e' indistinguibile, per la QA, da un fatto senza fonte. **Sedici rilievi in due giri
  sulle stesse note**: E9 non e' burocrazia, e il primo giro da solo avrebbe lasciato passare
  la meta' esatta dei difetti.
- **2026-08-18** · S4 lotto 1A · **Il ri-giudizio ha ribaltato una nota-questione** · su aw e
  umidita' dello snack la nota diceva che scheda tecnica e prove di stabilita' si
  contraddicono, lasciando intendere che la scheda fosse la fonte dubbia. Il **rapporto di
  prova del laboratorio accreditato** misura lo stesso lotto con metodo normato e dichiara
  **conformi** i valori della scheda: le fonti che concordano sono due, e l'anomalia sta nel
  **file delle prove di shelf life** — che e' la base della proposta di portare il TMC a sei
  mesi. ⚠️ La riga corrispondente nella sezione datata del canone e' stata **corretta nello
  stesso turno in cui era stata scritta**, prima di qualunque gate: non e' una riscrittura del
  canone, e' il completamento di una voce che nasceva sbagliata. Fuori da questo caso la
  regola resta: il canone si accresce e non si riscrive.
- **2026-08-18** · S4 lotto 1A · **La lacuna di copertura si chiude nel lotto che la trova,
  anche se il grezzo appartiene a un lotto gia' chiuso** · le prove chimico-fisiche del
  rapporto di laboratorio non erano canonizzate dal pilota. Aspettare un lotto futuro
  significherebbe non chiuderla mai: nessun lotto rivede i grezzi degli altri.
- **2026-08-18** · S4 lotto 1A · **Un secondo ruolo aggiunto di fatto allo strato di
  giudizio: la LACUNA DI COPERTURA** · il prompt congelato chiede due cose, e il giudice ne ha
  segnalata una terza fuori verdetto — una fonte del pacchetto che misura la stessa grandezza
  di una nota e che la nota non cita. E' stato il rilievo piu' utile del secondo giro.
  **Candidato emendamento al prompt di giudizio**, da valutare al gate: il prompt e' congelato
  e non si tocca a meta' lotto.

- **2026-08-18** · S4 lotto 1A, gate · **Cinque emendamenti approvati dal coordinatore e
  applicati a metodo_03: E21-E25** · E21 il budget si controlla PRIMA di scrivere e oltre il
  +25% il lotto si spezza; E22 la data di verifica di un'assenza rimanda a `data_nota` invece
  di essere riscritta nel corpo; E23 il marcatore di un valore derivato va accanto al numero,
  entro sessanta caratteri, e divisioni e medie non sono riconosciute come formule; E24 date e
  orari si riportano nella grafia della fonte; **E25 non si anticipa una divergenza di cui una
  sola gamba e' canonizzata**. Classificati nel registro del rapporto di lotto, §13.
- **2026-08-18** · S4 lotto 1A, gate · **E25 e' il divieto che chiude la causa radice delle due
  sole fughe di canone del progetto** · S2 e 1A hanno il movente identico: chi canonizza ha
  letto il canone, sa che la divergenza esiste, e non resiste a segnalarla anche quando la
  seconda gamba non e' ancora nel vault. **La gamba futura vive solo nella tabella di
  tracciamento**, che sta fuori dal vault. Serviva un divieto, non un richiamo alla prudenza.
- **2026-08-18** · S4 lotto 1A, gate · **`PROMPT_GIUDIZIO` passa alla v2, datata, e non e'
  retroattiva** · terzo compito in coda ai due esistenti, che restano intatti alla lettera:
  segnalare fuori verdetto una fonte del pacchetto che misura la stessa grandezza di una nota
  e che la nota non cita. **Vale dal lotto 1B; il lotto 1A e' stato giudicato con la v1**, e
  ogni rapporto di lotto dichiara la versione usata. ⚠️ **Il congelamento intoccabile riguarda
  gli strumenti di MISURA** — P1, P3, config C — dove la confrontabilita' prima/dopo e' il
  prodotto; **lo strato di giudizio e' una rete interna di QA ed evolve con versioni
  dichiarate**, esattamente come metodo_03. Distinzione fissata dal coordinatore.
- **2026-08-18** · S4 lotto 1A, gate · **Il falso positivo della suite sulla fonte non
  agganciata e' un FIX DI CODICE, non un emendamento** · il conteggio degli agganci si basava
  sulle sole affermazioni che una regex sa estrarre, e dichiarava «rumore nel payload» una
  fonte che sorreggeva la nota con un codice di forma non prevista (`PKM-4471-EPDM`). Ora
  contano anche i token che la nota marca come identificatori fra apici inversi: **puo' solo
  aggiungere agganci, mai toglierne**. Collaudo rieseguito dopo il fix: 5 difetti piantati su
  5 trovati, 0 falsi positivi.
- **2026-08-18** · S4 lotto 1A, gate · **Le chiusure a mano degli avvisi si registrano SEMPRE
  con motivazione scritta, mai in silenzio** · regola del titolare. Nel lotto 1A l'unico avviso
  chiuso a mano e' poi diventato un fix di codice, ed entrambi i passaggi sono scritti nel
  rapporto §11 e qui.
- **2026-08-18** · S4 lotto 1A, gate · **Un numero dichiarato che si corregge lascia
  un'errata datata e visibile** · la §11 del rapporto dichiarava 32 avvisi con famiglie che ne
  sommavano 46: avevo contato le righe su `qa_all.md`, che ripete al proprio interno i quattro
  report figli. Il rilievo e' del titolare. Ricontato dai figli, tre avvisi corretti invece che
  motivati e uno chiuso dal fix: **totale finale 30, famiglie disgiunte che sommano al totale**.
  L'errata resta nel rapporto: il rapporto di lotto non e' un verbale di misura, ma la
  correzione deve restare leggibile.
