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
