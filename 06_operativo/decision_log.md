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
- **2026-08-19** · S4, apertura del lotto 1B · **Il lotto 1B si spezza in 1B + 1C PRIMA di
  scrivere, e i lotti passano da 11 a 12** · applicazione di E21, approvata due giorni prima
  proprio su questo caso: il conteggio dei fatti in apertura ha proiettato **~41 note contro un
  budget di 22-30**, cioe' **+37 %** e una densita' di **6,8 note per grezzo** contro le 6,0 di
  1A. Decisione del titolare fra tre alternative. ⚠️ **Il criterio del taglio e' il suo, e vale
  come regola di mestiere: si spezza lungo le cuciture, mai attraverso le riconciliazioni.**
  La storia della cella `CF-02` resta intera in 1B — allarmi di aprile, arretrati di
  manutenzione gia' canonizzati in 1A, +49,7 % di consumo a maggio, contratto mai firmato — e
  1C prende parco strumenti, tarature e gas tecnici. Riassegnate in tabella di tracciamento:
  T18, T22, T30 a 1B; T17, T20, T25, T26, T32 a 1C.
- **2026-08-19** · S4, apertura del lotto 1B · **Gli obblighi F-gas restano in
  `area: manutenzione`, con il tag della dimensione trasversale** · decisione del titolare, con
  il motivo di fondo: **le note non traslocano** (metodo_03 §1.4), quindi l'assegnazione d'area
  e' permanente e si fa sull'area che governa i fatti **oggi**, non su quella di un assetto
  futuro. Un hub d'area non si apre vuoto per un'esigenza di archiviazione:
  `area-sicurezza-ambiente` nasce nel lotto 8 con i suoi fatti, come da matrice, e allora
  linkera' le note F-gas come **rimandi laterali** — il `related` principale resta l'hub di
  manutenzione (E11). L'impegno e' tracciato come **T34**, perche' un rimando promesso e non
  mantenuto e' esattamente cio' che la tabella esiste per impedire.
- **2026-08-19** · S4, apertura del lotto 1B · **`verifica_matrice_lotti.py` riconosce i lotti
  CHIUSI da un marcatore nell'elenco** · fix di codice, non emendamento. Il controllo 4 («nessun
  lotto contiene un grezzo gia' citato da una nota») esentava la sola fetta pilota, quindi
  diventava rosso a ogni lotto che si chiude: dopo 1A dichiarava 7 guasti che erano il lavoro
  fatto. Ora l'elenco di un lotto canonizzato porta `# CHIUSO <data>` in testa e il controllo lo
  salta, come per il pilota. **Il flag si aggiunge alla chiusura del lotto**, insieme agli altri
  gesti. Esito dopo il fix: 160 grezzi, 0 scoperti, 0 guasti, 13 elenchi.
- **2026-08-19** · S4 lotto 1B, chiusura · **La cella surgelati e' dentro il CCP4, e nessuna nota
  del lotto lo sapeva finche' non si e' fatta la riconciliazione con un grezzo di un altro
  lotto** · il manuale HACCP — canonizzato nel pilota — prescrive per `CF-02` limite critico
  −18 °C, soglia di allarme −16 °C e notifica a due responsabili nominati. Senza quella riga i
  sei allarmi di aprile sarebbero rimasti «anomalie d'impianto»; con quella riga sono
  **superamenti di un limite critico**. E' la prova che §5.1-bis va letto nella sua forma piu'
  larga: la riconciliazione non e' solo fra i grezzi del lotto, ma **fra il lotto e cio' che il
  vault gia' sa**.
- **2026-08-19** · S4 lotto 1B, chiusura · **Una famiglia di divergenze nuova per il canone:
  l'azione correttiva registrata che il dato non conferma** · tre casi nello stesso lotto, tutti
  trovati incrociando un registro compilato a mano con una registrazione automatica: NC-2026-017
  «spostato ciclo sbrinamento su fascia notturna» contro il log di aprile; NC-2026-114 «allarme
  porta ridotto a 5 min» contro il `LIM=00:05:00` gia' in vigore; NC-2026-067 che intesta al
  tunnel sbrinamenti che il log registra sulla cella. **Non sono divergenze fra due misure**: sono
  divergenze fra cio' che un registro dichiara di aver fatto e cio' che uno strumento ha
  registrato — ed e' il tipo di cosa che un sistema interrogato non trova mai citando una fonte
  sola. Le tre righe sono nel canone in sezione datata.
- **2026-08-19** · S4 lotto 1B, chiusura · **Il canone conteneva tre numeri vecchi, e le note
  avevano ragione** · sulla quadratura dei consumi energetici il canone dichiarava 59 / 137 /
  «165 su 165»; il riconteggio, fatto due volte in modo indipendente (script del lotto e
  revisore), da' **68 / 174 / 186 su 186**. Il 165 e' il numero delle righe con data `gg/mm/aa`:
  **l'analisi che ha prodotto quel numero saltava le 21 righe in formato ISO** dello stesso
  campo. Il divieto 36 vale anche per i numeri scritti nei documenti di metodo: il canone e'
  stato **accresciuto** con una riga datata che dichiara il riconteggio, e la vecchia sezione
  resta dov'e'. La conclusione qualitativa — sono arrotondamenti, non errori — e' confermata.
- **2026-08-19** · S4 lotto 1B, chiusura · **L'area `amministrazione` nasce nel lotto
  dell'energia, non nel lotto 6** · la matrice la assegnava al lotto 6 (bilancio e cassa), ma
  meta' dei grezzi di 1B sono governati dall'amministrazione — una fattura passiva, i contatori
  per centro di costo, un controllo di budget. Vale il criterio dato dal titolare lo stesso
  giorno: **l'area si assegna a chi governa i fatti oggi**, e **un hub non si apre vuoto per
  archiviare, ma nasce coi suoi fatti**. Qui i fatti c'erano. Il lotto 6 la estendera'.
- **2026-08-19** · S4 lotto 1B, chiusura · **Budget sforato di 8 note, e lo scostamento e' tutto
  post-revisione** · 38 di contenuto contro un tetto di 30. Le 29 della prima stesura stavano
  dentro; le nove in piu' vengono dai tre passaggi di controllo: una dal rilievo «due fatti in
  una nota», tre dalla promozione a questione di divergenze di categoria B, una da
  un'incoerenza intra-file, quattro dalle lacune di copertura trovate dal revisore. **Il revisore
  ha campionato dodici note contro le otto richieste e ha dichiarato zero sovra-atomizzazione.**
  Un budget rispettato tagliando fatti sarebbe stato peggio.
- **2026-08-19** · S4 lotto 1B, chiusura · **La terza gamba di una questione si TRACCIA, non si
  usa, se il suo grezzo appartiene a un lotto futuro** · il revisore ha segnalato che
  `elenco_interni_telefonici.txt` scrive «Frigotecnica Berica», terza fonte sulla questione del
  manutentore. Quel file e' del lotto 10, dove per metodo_03 §1.3 esempio 18 si spalma sulle
  schede senza fare nota propria. Citarlo ora avrebbe messo in rosso la verifica di
  disgiunzione della matrice e anticipato il lavoro di quel lotto: la gamba **resta in tabella di
  tracciamento** (T18) con l'obbligo esplicito per il lotto 10. Stessa disciplina applicata al
  terzo quasi-omografo Peruffo (T39): la riga «Da non confondere con» non puo' nascere prima
  delle note dei due revisori legali.
- **2026-08-19** · S4 lotto 1B, chiusura · **Errata sui numeri del lotto 1A** · lo stato
  dichiarava «105 note, di cui 11 `_index` e 6 note-strumento: 88 di contenuto», ma `qa_all.py`
  a chiusura di 1A contava **106** note. Il 105 escludeva `_index-sources` e sottraeva ugualmente
  tutti e undici gli `_index`: il numero corretto e' **89 di contenuto**. Corretto nello stato con
  l'errata visibile.
- **2026-08-19** · S4 lotto 1B, chiusura · **Il controllo «summary contiene piu' di una frase» ha
  un falso positivo sulle abbreviazioni, e NON e' stato corretto** · conta i punti fermi, quindi
  sbaglia su ogni riassunto che contenga `S.r.l.`, `prot.`, `art.`, `n.` — in questo corpus,
  ovunque. Due avvisi su sedici sono suoi. **Non l'ho toccato di mia iniziativa**: sarebbe un fix
  che *toglie* avvisi, cioe' allenta un controllo, mentre la regola del gate 1A ammette solo fix
  che *aggiungono* agganci. Portato al titolare come proposta, con la correzione in una riga.
- **2026-08-19** · S4 lotto 1B, chiusura · **E9 ha girato QUATTRO volte, e il metodo non dice
  quando smettere** · correggere riscrive, e riscrivere crea note nuove da giudicare: 1º giro 5
  rilievi su 29 note, 2º 4 su 37, 3º 4 su 10, 4º **1** su 6. ⚠️ **Nessuno dei quattordici ha mai
  riguardato un numero, una data o un codice** — quelli li prende lo strato deterministico:
  tutti riguardavano **la prosa che lega i fatti**, la frase che spiega, l'esempio che illustra,
  il ruolo attribuito a chi firma. E il rilievo del quarto giro era **nato da una correzione del
  terzo**, quindi non era prevedibile fermandosi prima. **Criterio con cui mi sono fermato,
  dichiarato nel rapporto:** l'ultimo giro ha prodotto un solo rilievo e la correzione applicata
  e' **soppressiva** — toglie un'attribuzione senza aggiungere niente — quindi non genera
  materiale nuovo da giudicare. Portato al coordinatore come **candidato chiarimento a §9.5
  passo 5**: si rigiudica finche' un giro non torna pulito, oppure finche' le correzioni non
  sono tutte soppressive, e il rapporto dichiara a quale giro ci si e' fermati e con quale dei
  due criteri.
- **2026-08-19** · S4 lotto 1B, chiusura · **Il terzo giro ha smontato un mio argomento, non solo
  una mia frase** · `questione-nc-067-sbrinamenti-tunnel` sosteneva che le due macchine «stanno su
  linee diverse» e che l'intestazione «Linea 3» della non conformita' pesasse a favore del tunnel.
  Il giudice ha fatto notare che **il registro intesta alla Linea 3 anche `NC-2026-017`, che
  riguarda la sonda della cella**: l'argomento non regge, e la nota ora lo dice. E' il tipo di
  errore che nessuno strato deterministico puo' prendere, perche' non e' un dato sbagliato: e' un
  ragionamento sbagliato su dati giusti.
- **2026-08-19** · S4 lotto 1B, gate · **`conta_stato.py` entra nella suite: i conteggi del vault
  si INCOLLANO, non si ricompongono** · fix di processo deliberato dal coordinatore, e nasce da
  **due sviste in due lotti**: nel rapporto 1A «46 note di contenuto» contro le 32 dello stesso
  documento, e nello stato «105 note, 88 di contenuto» quando `qa_all.py` ne contava 106 e 89.
  ⚠️ **Nessuno dei due era un errore di canonizzazione**: erano due sottrazioni fatte a mano su
  numeri veri, ed e' il modo piu' facile di perdere credibilita' su un lavoro corretto. Lo script
  emette un blocco markdown con note per cartella e per `type`, `_index`, note-strumento, note di
  diario, note di contenuto, questioni aperte, grezzi citati e restanti. **Da qui in poi stato e
  rapporti di lotto lo incollano verbatim**; se un numero non e' nel blocco, o lo produce un
  altro script, oppure non si dichiara.
- **2026-08-19** · S4 lotto 1B, gate · **Il pattern che ha rigenerato i rilievi ha un nome: IL
  CONTESTO IMPORTATO** · e' l'adempimento che E26 chiede quando il ciclo passa il terzo giro. La
  classe: *una frase scritta per rendere la nota leggibile — non per affermare un fatto nuovo —
  che porta dentro qualcosa che chi scrive sa dall'archivio ma che le fonti di quella nota non
  contengono*. Quattordici rilievi su quattordici erano di questa classe: «il foglio OEE», «il
  payback del tunnel», «il direttore di stabilimento», «il fornitore vede l'effetto», «in piena
  settimana di promo». ⚠️ **Si annida nelle sezioni «Perche' conta»**, cioe' dove si scrive per
  far capire, ed e' il prezzo di note che devono reggersi da sole come chunk del RAG. **Perche'
  il ciclo lo rigenerava:** ogni correzione riscrive quella frase, e la riscrittura e' ancora una
  frase di contesto — il difetto non stava nelle note, stava nel gesto di correggerle.
  **Antidoto, dal lotto 1C in poi:** prima del primo giudizio, rileggere ogni «Perche' conta» con
  davanti le sole fonti di quella nota.
- **2026-08-19** · S4 lotto 1B, gate · **Il terzo compito del PROMPT_GIUDIZIO v2 e' segnale poco
  piu' di una volta su due, e il rumore ha una forma sola** · 26 segnalazioni in quattro giri, 19
  distinte: **10 accolte, 9 respinte**. ⚠️ Il segnale e' massimo dove la nota **nomina un
  documento senza citarlo** (5 accolte su 5). Il rumore e' tutto della stessa specie: **il
  giudice non conosce il grafo del vault**, quindi segnala come lacuna cio' che ha una padrona
  altrove — sette respinte su nove. Taratura suggerita al gate finale, **non applicata**: dare al
  giudice l'elenco delle note del lotto coi loro `summary`. La classificazione una per una sta
  nell'appendice B del rapporto di lotto, come chiesto dal coordinatore.
- **2026-08-19** · Coordinatore · **Il rituale di chiusura passa da QUATTRO a CINQUE gesti:
  l'aggiornamento del passaggio di consegne entra nella FONTE, non solo nel prompt dei lotti**
  (E27) · l'obbligo esisteva già dal 19/08/2026, ma viveva in due soli posti: la §8 di
  `passaggio_di_consegne_coordinatore.md` (che dice *come* si scrive) e il §5 di
  `prompt/prompt_s4_lotti.txt`, cioè **un documento derivato e monouso**. ⚠️ **Un rituale scritto
  solo in un derivato prima o poi diverge dal rituale vero**: basta una sessione lanciata con un
  prompt diverso — S6, S7, o qualunque cosa non sia un lotto — e il gesto sparisce senza che
  nessuno se ne accorga, perché nessuna fonte lo reclama. Ora il **quando** ha i suoi padroni:
  **principio 5 della scaletta** (sorgente) e **`metodo_03` §9.5, nuovo passo 8** (E27), dove il
  commit slitta a 9 e il diagramma del ciclo diventa `stato → decision log → passaggio di
  consegne → commit`. La §8 del passaggio di consegne resta il padrone del **come**, e ora cita
  i due sorgenti. **Condizionalità fissata nel testo**, perché il gesto non diventi teatro: la
  §3 «dove siamo» si riscrive **sempre**, coi numeri incollati da `conta_stato.py`; §4, §5 e §6
  prendono una riga datata **solo se** la sessione ha fissato un criterio nuovo, versionato uno
  strumento, ratificato una prassi o pagato un errore nuovo. **Propagato alle tre copie derivate
  nello stesso turno** — regola d'oro 6 in `00_INIZIA_QUI.md` (e il suo elenco di igiene),
  `06_operativo/LEGGIMI.md`, §1 del passaggio di consegne: la voce del 15/08/2026 che istituì i
  quattro gesti resta a registro come storia, e questa la sostituisce. ⚠️ **Non toccati
  `prompt_s2_pilota.txt` e `prompt_s3_config_c.txt`**, che nominano ancora i quattro gesti: sono
  il verbale di ciò che quelle sessioni hanno davvero eseguito, e riscriverli falsificherebbe la
  storia del repo — se S2 o S3 si rieseguissero, il prompt si riallinea allora.
- **2026-08-19** · Coordinatore · **E27 approvato, e il numero resta: gli emendamenti li approva
  il COORDINATORE, non il gate** · avevo proposto di rinominarlo se la convenzione fosse stata
  «solo ai gate». Non lo è: il gate è l'occasione tipica, non la condizione. ⚠️ **E27 è però il
  primo emendamento nato FUORI da un gate**, su ordine diretto, e la cosa va detta o fra un anno
  un numero senza gate accanto sembra un numero senza padre. Da qui il **registro degli
  emendamenti** (`06_operativo/registro_emendamenti.md`): un **indice genealogico** dei 27 —
  numero, data, occasione, tipo, oggetto in una riga, sezione di `metodo_03`, dove sta il perché.
  **Non contiene il testo delle regole**, che resta di `metodo_03`: un registro che ricopia le
  regole è la prossima divergenza. **Tre buchi che l'indice ha fatto emergere**, e nessuno era
  noto: **E18 ed E19** non stanno nella tabella §9 del rapporto S2 (sono nati durante il gate,
  a rapporto già scritto — il decision log ne conta «diciannove», la tabella diciassette);
  **E26** non ha riga di registro da nessuna parte, perché il gate 1B non ha prodotto una tabella
  di emendamenti come S2 e 1A; **quattro emendamenti sono applicati senza marcatore inline**
  (E3, E4, E15, E16), e sono i refusi, che non lasciano cicatrice. Puntatori e marcatori sono
  verificati da script (`verifica_emendamenti.py`), non a occhio: 27 righe, 23 marcatori, verde.
- **2026-08-19** · Coordinatore · **Le due astensioni del turno diventano giurisprudenza: §4.18 e
  §4.19 del passaggio di consegne** · non erano scelte di giornata, e registrarle come tali le
  avrebbe fatte ridiscutere al primo caso simile. **(18) Un prompt già eseguito è un verbale, non
  uno strumento vivo:** documenta ciò che quella sessione ha fatto e non si riallinea alle regole
  venute dopo — si data. È la stessa regola del verbale di misura chiuso (§4.11) e della
  testimonianza del giudice (§4.10), estesa ai prompt. **I prompt ancora in uso sono strumenti
  vivi e si emendano**, ed è la riga che tiene separati `prompt_s2_pilota.txt` e
  `prompt_s3_config_c.txt` — che restano ai quattro gesti — da `prompt_s4_lotti.txt`, che gira
  ancora e porta i cinque. **(19) Una voce di decision log si sostituisce, non si cancella:** il
  registro è cronologia, non fotografia. ⚠️ Il corollario che rende la regola utilizzabile: vale
  per i **registri**, mentre i documenti-**fotografia** — la §3 del passaggio di consegne,
  `STATO`, i conteggi — si riscrivono. È la ragione per cui le due specie non convivono nello
  stesso file.
- **2026-08-19** · Coordinatore · **Titolarità del rituale fissata nella §8 del passaggio di
  consegne, e §7-bis «Protocollo di risposta del coordinatore»** · la §8 ora dice per iscritto
  che **il QUANDO del quinto gesto è di P5 e di `metodo_03` §9.5 passo 8, il COME è suo**, e che
  **il passaggio di consegne non è una terza fonte del rituale: è il manuale d'uso di sé stesso**.
  Serviva perché un file che prescrive un obbligo tende a diventare, col tempo, la fonte di
  quell'obbligo. La **§7-bis** raccoglie il protocollo del coordinatore, che finora viveva a metà
  nella §7 e a metà nella pratica: si delibera **sul pacchetto completo dei pannelli**, si legge
  **il documento vero sul disco** prima di approvare un gate (due errori del progetto trovati
  così), si ricontrollano **i numeri che non tornano** (due volte, due errori veri); la risposta
  ha tre parti ed è **un prompt esteso, non un ordine secco**, perché chi opera deve capire il
  perché per decidere nei casi non previsti; **ogni istruzione è classificata una tantum o
  permanente**, e se una cosa va ripetuta a ogni lotto si emenda **il prompt riutilizzabile**,
  non la si ripete. ⚠️ Quest'ultima riga è la stessa malattia che E27 ha curato. Perimetro:
  il coordinatore non tocca il vault, non apre `03_valutazione\`, non scrive nel repository
  mentre una sessione gira, e **verifica il push da sé** invece di fidarsi del rapporto. La §7
  è stata sfoltita a puntatore: il protocollo ha un padrone solo.
- **2026-08-19** · Coordinatore, apertura del lotto 1C · **E28 — la soglia di spezzamento di un
  lotto diventa doppia, e il difetto era nella grandezza misurata** · E21 spezzava sullo
  **scostamento percentuale** dal budget; il rischio che quella regola contiene è però il
  **carico di revisione**, che si misura in **note assolute**. ⚠️ **Le stime della matrice sono
  ferme alla densità del pilota (2,1 note per grezzo) contro il 9,5 misurato in 1B**: con quelle
  stime E21 sarebbe scattata a ogni lotto, e **una regola che scatta sempre viene scavalcata per
  prassi**. Nuova soglia: si spezza se la proiezione supera il budget di oltre il **25 % E** vale
  più di **30 note di contenuto**; sotto le 30 lo scostamento si **dichiara nel rapporto** e si
  procede; oltre le **40** si spezza sempre. **I tre numeri vengono dai consuntivi**, non da una
  stima: pilota 46 note in una sessione che costruiva anche la suite, 1A 42, **1B 38 con quattro
  giri di giudizio** — è 1B a fissare il tetto, perché sopra le quaranta il ciclo di revisione
  comincia a rigenerare rilievi invece di esaurirli. **Effetto immediato: il lotto 1C non si
  spezza** (23 note proiettate, +27,8 % sul budget alto), e lo scostamento va dichiarato nel
  rapporto. Registrato come giurisprudenza §4.20 del passaggio di consegne, in forma generale:
  **quando una soglia scatta sempre, il difetto è nella grandezza che misura.**
- **2026-08-19** · S4 lotto 1C, apertura · **Il registro degli emendamenti ha trovato un difetto
  invece di documentarlo: E3 era una regola nuova senza marcatore** · il coordinatore aveva
  ordinato di **non** aggiungere marcatori posticci ai quattro emendamenti che ne erano privi
  (E3, E4, E15, E16), sul principio che **un refuso corregge un testo sbagliato e non introduce
  una regola da marcare**. ⚠️ **Il presupposto era vero per tre su quattro:** E4, E15 ed E16 sono
  refusi, **E3 no** — è il divieto di dichiarare un'assenza senza averla cercata, cioè una regola
  nuova, e §10.12-bis la portava senza sigla pur portando quella di **E22**, che di quel divieto
  è solo il chiarimento sulla data. Applicare la ratio del coordinatore **nell'altro verso**
  significa dargli il marcatore, non toglierlo agli altri: fatto. Il controllo è ora in
  `verifica_emendamenti.py` come **implicazione in una direzione sola** — *ogni emendamento
  senza marcatore dev'essere un refuso* — e **non** come bicondizionale: **E14 ed E19 sono refusi
  e il marcatore ce l'hanno**, perché correggono un passaggio che senza spiegazione tornerebbe a
  sembrare sbagliato. Il bicondizionale avrebbe segnalato come difetti due emendamenti corretti.
- **2026-08-19** · S4 lotto 1C, apertura · **La matrice dichiarava 121 righe di strumento, lo
  script ne conta 120** · errata datata nel registro della matrice, vale il numero dello script
  (regola d'oro 5). ⚠️ Nello stesso conteggio è emerso che il file porta **due righe di
  intestazione**, la seconda a riga 64 **con nomi di colonna diversi dalla prima**: non è un
  difetto da aggirare in fase di parsing, è un **fatto dell'archivio** — il file nasce
  appiccicando due elenchi con schemi diversi — e come tale ha una nota nel vault, esattamente
  come il checksum fallito del datalogger e le revisioni non accettate del contratto frigo.
- **2026-08-19** · S4 lotto 1C, chiusura · **Una divergenza apparente che l'archivio scioglie e'
  un RISULTATO, e la tabella di tracciamento ora distingue tre esiti** · T17 sembrava una
  contraddizione — il quaderno del capoturno scrive «bomb0la n0rdgas cambiata alle 16» e la bolla
  dello stesso giorno consegna azoto **sfuso** in serbatoio e bombole di sola CO2 — e non lo era:
  l'inventario di magazzino, gia' nel vault dal pilota, registra **18 bombole di azoto «scorta
  rampa»** con nota «rampa emergenza PKM-450». Gli esiti possibili di una riga di tracciamento
  diventano quindi tre: *chiusa*, *aperta dichiarata* e **riconciliata**. ⚠️ Chi scrive una
  riconciliazione **dichiara l'inferenza**: che *quella* bombola venisse dalla rampa nessuna fonte
  lo afferma.
- **2026-08-19** · S4 lotto 1C, chiusura · **Il criterio di aggancio con cui 120 righe di strumento
  diventano 27 note, dichiarato come il titolare ha chiesto** · quattro classi, e nessuna riga ha
  una nota tutta sua: **(a)** lo strumento presidia un CCP o un impianto gia' canonizzato; **(b)**
  la riga porta uno stato anomalo dichiarato dal registro stesso; **(c)** la riga contraddice un
  documento gia' nel vault; **(d)** la riga dichiara una regola o un obbligo. Contate da script:
  **43 matricole su 120** sono nominate, in 22 note; le altre 77 vivono nei conteggi dell'hub.
  ⚠️ **Il campione al revisore non e' stato un campione: sono state tutte.** Il pacchetto del
  giudizio contiene tutte le note del lotto, quindi le 13 nate dal CSV sono state giudicate una
  per una, per tre giri, e nessuna e' stata segnalata come non agganciabile a una domanda.
- **2026-08-19** · S4 lotto 1C, chiusura · **Il ciclo di ri-giudizio ha girato TRE volte e si e'
  chiuso per E26, non per esaurimento: 27 rilievi, tutti accolti** · 12 al primo giro su 28 note,
  8 al secondo su 29, 7 al terzo su 29. ⚠️ **Nessuno dei 27 riguardava un numero, una data o un
  codice**: quelli li prende lo strato deterministico. **Il primo pattern lo ha nominato il giudice
  al secondo giro: «il corpo cautela, l'intestazione afferma».** Sei rilievi su sette, al terzo
  giro, stavano ancora nel `title` o nel `summary`, e in cinque casi il corpo della stessa nota
  era corretto. La causa e' meccanica: **il summary si scrive per primo e si corregge per ultimo**,
  quindi quando una correzione attenua il corpo l'intestazione resta com'era. Antidoto, dal lotto
  2: rileggere `title` e `summary` come note a se' **a ogni giro**, non una volta sola.
- **2026-08-19** · S4 lotto 1C, chiusura · **Il secondo pattern vale piu' del primo: LA FONTE
  TRASVERSALE NON CITATA** · delle quattordici lacune di copertura del terzo giro, **undici
  indicavano lo stesso documento**, il manuale HACCP. ⚠️ **In quattro casi conteneva esattamente
  cio' che la nota dichiarava mancante**: che l'`MD-1800` e' «gestito come CCP assimilato al CCP3»;
  che il pericolo «frammenti di plastica da organi macchina» **non e' rilevabile dal metal
  detector**; che la verifica del CCP3 e' **annuale, del costruttore**; che esiste un `PRP-03`
  «Manutenzione preventiva impianti e taratura strumenti». **Perche' e' successo:** chi canonizza
  un grezzo che *registra* cerca gli altri documenti che *registrano* la stessa cosa, e non pensa
  al documento che **prescrive** come quella cosa vada fatta. La riconciliazione incrociata ha
  funzionato in orizzontale e ha mancato la verticale. **Antidoto:** quando una nota tocca un CCP,
  una taratura, una frequenza di verifica o una responsabilita' di processo, il manuale HACCP si
  apre e si cita — o si dichiara perche' non serve. ⚠️ **Nel vault ci sono 30 note che nominano un
  CCP e non citano il manuale**: portato al titolare come decisione, perche' guardarle adesso costa
  molto meno che al gate finale.
- **2026-08-19** · S4 lotto 1C, chiusura · **Chi estende una nota vecchia la fa uscire dal
  perimetro che la controlla** · estendendo `fatto-convalida-md-1800-scaduta` e
  `fatto-cariche-f-gas-impianti-frigoriferi` ho introdotto **una data senza fonte e una nota oltre
  le 350 parole**: la QA a perimetro di lotto **non li ha visti**, perche' quelle note non citano
  i grezzi di 1C, e li ha presi solo la QA a perimetro vault, che non si lancia a ogni lotto.
  **Candidato emendamento a metodo_03 §7**: il perimetro di lotto deve comprendere le note
  **modificate** dal lotto, non solo quelle che citano i suoi grezzi. Secondo candidato, dello
  stesso genere: **il pacchetto per lo strato di giudizio si genera DOPO le correzioni
  pre-giudizio** — in questo lotto e' stato generato prima, e due rilievi su dodici del primo giro
  riguardavano testo che non esisteva piu'.
- **2026-08-19** · S4 lotto 1C, chiusura · **La ricalibrazione dei budget chiesta dal coordinatore
  ha prodotto un risultato che NON si puo' consegnare, e il perche' e' il risultato utile** ·
  proiettando la densita' misurata (8,2 note per grezzo dopo il pilota) sui 125 grezzi restanti si
  ottengono **903 note e 36 lotti**, con ogni lotto restante sopra il tetto di 40 note. ⚠️ **E' un
  artefatto, e i numeri lo dimostrano**: le note *per lotto* hanno dispersione del **50 %** (27-46),
  la densita' *per grezzo* del **147 %** (2,1-13,5). I grezzi per lotto sono passati **da 22 a 2**
  mentre le note restavano fra 46 e 27: **cio' che resta costante e' il lotto, non la densita'**.
  Tre cause plausibili e nessuna misurabile oggi: i lotti chiusi contengono i grezzi piu' densi,
  scelti per primi; il vault che sa di piu' produce piu' riconciliazioni (1C lo conferma: 4
  divergenze su 9 nate da documenti vecchi); il **costo fisso di apparato** — hub, entita', index —
  si spalma su meno grezzi quando il lotto e' piccolo (in 1C, 4 note su 27). **Proposta portata al
  titolare:** budget a **capacita'** (25-35 note per lotto), grezzi decisi in apertura contando i
  fatti, lotti 2-10 spezzati in pacchetti da 3-5 grezzi. Il piano passa da 12 a **28-30 lotti**, e
  **cambia il calendario delle Sessioni 4-5**. ⚠️ **Cio' che non ho fatto:** riscrivere le fasce dei
  lotti 2-10 coi numeri della proiezione. Una stima sbagliata sostituita da una peggiore non e' una
  ricalibrazione.
- **2026-08-19** · S4 lotto 1C, gate · **Cinque emendamenti approvati dal coordinatore e applicati
  a metodo_03: E29-E33** · **E29** la riconciliazione ha due direzioni e quella **verticale** va
  cercata apposta — chi tocca un CCP, una taratura, un limite o una responsabilita' di processo
  cita la fonte che lo **prescrive**, con l'**elenco delle fonti prescrittive** come strumento;
  **E30** `title` e `summary` si rileggono come note a se' **a ogni giro** di giudizio; **E31** il
  budget di lotto e' una **capacita'** di 25-35 note, provvisoria fino a dieci lotti chiusi;
  **E32** il perimetro di lotto comprende anche le note **modificate**, dichiarate in
  `qa\lotti\<lotto>_note.txt`; **E33** il pacchetto per lo strato di giudizio si genera **dopo**
  le correzioni pre-giudizio. Registrati in `registro_emendamenti.md` con occasione «gate del
  lotto 1C» e col caso reale che li ha generati.
- **2026-08-19** · S4 lotto 1C, gate · **E32 ed E33 non aspettano il gate finale perche' non sono
  migliorie: sono guasti del ciclo di controllo** · principio del coordinatore, ora §4.25 del
  passaggio di consegne: **un emendamento che corregge il perimetro o l'ordine di un controllo si
  applica subito; si rimandano al gate solo quelli che cambiano il modo di scrivere le note.**
  ⚠️ Un controllo che non copre cio' che deve coprire non si accumula per valutarne «l'effetto
  cumulato»: l'effetto cumulato e' che i lotti successivi ereditano lo stesso buco. **Entrambi
  hanno un difetto piantato nel collaudo** (`_collaudo/collaudo_suite.py`): una nota modificata e
  dichiarata ma che non cita i grezzi del lotto, e la verifica che il pacchetto del giudizio
  rifletta il testo corrente. ⚠️ **Provato che il difetto E32 non viene visto senza E32**:
  lanciando la suite senza `--note-toccate`, l'errore piantato non compare. Il collaudo passa a
  **7 difetti su 7** piu' i due controlli sul pacchetto.
- **2026-08-19** · S4 lotto 1C, gate · **La tabella di tracciamento ha TRE esiti, non due: chiusa,
  aperta dichiarata, RICONCILIATA** · decisione del coordinatore. ⚠️ **Una divergenza apparente
  che l'archivio scioglie non e' un pareggio: e' un risultato del vault**, ed e' esattamente cio'
  che la misura «dopo» dovra' saper mostrare — un archivio grezzo lascia la contraddizione dov'e',
  un archivio che ha capito il meccanismo la scioglie e lo dichiara. Le due righe riconciliate:
  **T22** (1B, gli arretrati della cella) e **T17** (1C, l'azoto che entra per due vie).
- **2026-08-19** · S4 lotto 1C, gate · **La ricalibrazione: adottata E31, ma i lotti 2-10 NON si
  ripacchettizzano adesso** · il coordinatore ha ratificato il rifiuto del calcolo lineare che lui
  stesso aveva ordinato, e ha aggiunto il vincolo che mancava: ridisegnare tutti i 28-30 lotti
  oggi sarebbe **di nuovo pianificazione a lungo raggio su dati scarsi**, cioe' lo stesso errore
  in un'altra forma. Quindi: ridisegnato in dettaglio **solo il tema 2** (2A lavaggio CIP · 2B
  autocontrollo di igiene · 2C materiali a contatto), gli altri marcati «da ripacchettizzare in
  apertura» con pacchetti indicativi di **3-5 grezzi** (contenuto) e **8-10** (rumore). **Le stime
  vecchie restano barrate, non cancellate.** ⚠️ **La stima complessiva — circa 28-30 lotti invece
  di 12 — e' stata scritta anche nella SCALETTA**, perche' cambia il calendario delle Sessioni 4-5
  e il titolare deve averla ora, non scoprirla a meta' strada.
- **2026-08-19** · S4 lotto 1C, gate · **Principio generale dalla ricalibrazione: quando un
  consuntivo smentisce una stima, non si sostituisce la stima con un'altra stima — si cambia la
  grandezza su cui si pianifica** · §4.24 del passaggio di consegne. Il segnale che si sta
  sbagliando grandezza: **la stima nuova e' piu' assurda della vecchia** (903 note, 36 lotti).
- **2026-08-19** · S4 lotto 1C, gate · **PROSSIMO ATTO: R1, il lotto di manutenzione della
  riconciliazione verticale. NON il lotto 2** · le 30 note che nominano un punto critico senza
  citare la fonte che lo prescrive **non sono incomplete: alcune affermano il falso** — quattro su
  undici, nel campione del lotto 1C, dichiaravano assente cio' che il manuale HACCP scrive per
  esteso. ⚠️ **Con quel tasso, lasciarle li' significa portarle dentro la Sessione 6**: la misura
  «dopo» girerebbe su un vault che nega cio' che l'archivio prescrive, e le predizioni
  pre-registrate riguardano proprio contraddizione e multi-hop, cioe' le domande che quelle note
  toccano. **R1 si esegue col ciclo di lotto completo** — elenco da script, QA, giudizio v2,
  revisione, ri-giudizio, re-QA, llms.txt, rapporto, commit dedicato — e vale come un lotto nel
  conteggio del ritmo. Dentro R1 nasce lo **strumento di E29**, l'elenco delle fonti prescrittive
  del corpus. **Perimetro:** solo le note su cui una fonte prescrittiva dice qualcosa; non e' un
  ripasso generale del vault. Il rapporto di R1 dichiara **quante note guardate, quante corrette e
  il tasso di difetto**: quel numero dira' se il ripasso va rifatto a fine corsa o se E29 in
  vigore basta.
- **2026-08-19** · manutenzione post-1C, coordinatore · **LIMITAZIONE RETROATTIVA DEL COLLAUDO
  DELLA SUITE: i numeri «5 su 5» e «7 su 7» valgono meno di quanto sembravano** · fino a oggi
  `_collaudo\collaudo_suite.py` invocava i quattro script **direttamente**, con `--note-toccate`
  esplicito. Quei collaudi provano che **i controlli funzionano**; NON provano che `qa_all.py` li
  chiami con gli argomenti giusti, ed è esattamente lì che si annidava il difetto trovato oggi
  (il flag non veniva inoltrato). ⚠️ **Non invalida nessun lotto chiuso**, e i due casi vanno
  tenuti separati perché sono diversi:
  **(a) il lotto 1C** — la via per convenzione **ha funzionato**, ed è verificabile su disco:
  `06_operativo\qa\2026-08-19_1c\qa_all.md` dichiara perimetro di lotto su **51 note** e riporta
  gli avvisi di lunghezza su `fatto-cariche-f-gas-impianti-frigoriferi` (346 parole) e
  `fatto-convalida-md-1800-scaduta` (320), cioè proprio le due note estese che senza E32 erano
  sfuggite;
  **(b) pilota, 1A e 1B** — la convenzione non li ha protetti perché **non esisteva**: E32 nasce
  al gate di 1C, e in `qa\lotti\` c'è un solo `_note.txt`. Le loro note modificate erano fuori
  perimetro, ed è il fatto **già registrato** che ha generato E32 — non una scoperta di oggi.
  Quello che restava scoperto è **ciò che sta fra il lanciatore e i figli**, ed è colmato dal
  requisito di §4.29. La stessa limitazione è scritta **nel docstring del collaudo**, accanto al
  conteggio dei difetti: la cifra e il suo limite devono viaggiare insieme, o «7 su 7 verdi»
  continua a significare più di quanto vale.
- **2026-08-19** · manutenzione post-1C, coordinatore fuori da un gate · **E34 in `metodo_03`
  §9.5, passo 5-bis: la nota-sessione entra nel rituale, e il blocco dei conteggi si genera DOPO
  di essa** · il blocco incollato nello stato e nel rapporto 1C dichiara **172** note (workspace
  5, sessione 2), `qa_all.py` dello **stesso giorno** ne conta **173** (workspace 6, sessione 3):
  la differenza è la nota di diario del lotto, scritta dopo il conteggio. Le note di contenuto
  restano **153** in entrambi, quindi nessuna decisione è stata presa su un numero sbagliato.
  ⚠️ Ma **uno strumento nato per finire le sviste di conteggio, generato nel punto sbagliato del
  rituale, è peggio di nessuno strumento**: dà l'autorità dello script a un numero vecchio. Il
  blocco è ora l'**ultimo numero prodotto prima del commit**.
- **2026-08-19** · manutenzione post-1C, coordinatore fuori da un gate · **E35 in `metodo_03` §7
  e §9.4-bis: esiste il LOTTO DI MANUTENZIONE** · quello che non canonizza grezzi nuovi ma
  **ripara note già scritte**, quando un gate scopre un difetto di classe che le attraversa. Il
  primo è R1. Regole proprie: perimetro di **sole note** (elenco grezzi vuoto con
  `# MANUTENZIONE` in testa, il perimetro vero è `qa\lotti\<lotto>_note.txt`); l'elenco delle
  note lo **genera uno script** e il criterio si scrive nel rapporto; **niente capacità 25-35**,
  perché un lotto di manutenzione non punta a produrre note; il rapporto dichiara **tre numeri**
  — note guardate, note corrette, tasso di difetto; vale come **un lotto** nel ritmo.
  ⚠️ **Con una GUARDIA, e va scritta**: zero grezzi si accettano **solo** se l'elenco delle note
  esiste e non è vuoto, e il report lo dichiara in chiaro. Un perimetro vuoto per errore di
  battitura deve restare un errore, altrimenti la via più rapida per una QA verde diventa
  cancellare l'elenco. Non è una deroga che allenta un controllo: è una modalità dichiarata che
  lo **estende** a un oggetto che prima non poteva essere controllato affatto.
- **2026-08-19** · manutenzione post-1C · **Quattro fix agli strumenti, tutti collaudati prima di
  dichiararli chiusi** · sono **fix di codice, non emendamenti** (precedente: il gate 1A, dove il
  falso positivo sulla fonte non agganciata fu classificato così), e tutti e quattro
  **AGGIUNGONO copertura senza toglierne** — verificato, non assunto: la QA a perimetro vault
  rilanciata dopo i fix produce report **identici byte per byte** a quelli committati, e il
  perimetro del lotto 1C rilanciato in una cartella di scarto è identico **sotto l'intestazione**.
  **FIX 1** — `qa_all.py` non inoltrava `--note-toccate` ai quattro figli: E32 reggeva **solo**
  perché ogni figlio si ricalcolava la convenzione da sé. Chi passava l'elenco esplicitamente se
  lo vedeva ignorare **in silenzio**, con la QA verde e le note modificate fuori perimetro.
  **FIX 2** — `leggi_perimetro` rifiutava l'elenco a zero grezzi: R1 non era **lanciabile
  affatto**. Ora lo accetta con la guardia di E35, e il report lo dichiara.
  **FIX 3** — il collaudo non esercitava il lanciatore, ed è il difetto che rendeva invisibili
  gli altri due (vedi la limitazione retroattiva qui sopra e §4.29).
  **FIX 4** — l'etichetta del lotto nei report: se `--lotto` non è passato e il perimetro è
  `@lotti\<nome>.txt`, l'etichetta prende `<nome>` invece del default `l26130`. ⚠️ **Il report di
  1C NON è stato rigenerato**: rifarlo oggi fotograferebbe un vault diverso da quello che il gate
  ha approvato. L'errata sta nel §5 del rapporto 1C.
- **2026-08-19** · manutenzione post-1C · **Il collaudo dichiara le VIE DI PRODUZIONE nel proprio
  docstring, e il verdetto è una tabella via per via, non un totale** · cinque vie più un caso
  negativo: V1 lotto per convenzione (i sette difetti sostanziali) · V2 `--note-toccate`
  esplicito · V3 `--pacchetto-giudizio` · V4 perimetro vault · V5 perimetro di manutenzione ·
  V-neg zero grezzi senza elenco, che **deve** uscire in errore. L'invocazione diretta dei figli
  **si tiene, dichiarata come via NON di produzione**: serve a isolare un guasto quando `qa_all`
  è rosso, non a dimostrare copertura. ⚠️ **Un totale aggregato tornerebbe a nascondere proprio
  ciò che questa riparazione ha scoperto**, cioè quale via non è esercitata da nessuno.
  Controprova eseguita: con gli strumenti **pre-fix**, V2 e V5 falliscono; disattivando il solo
  FIX 4, fallisce la sola verifica dell'etichetta. Un difetto che passa anche senza il suo fix
  non è un difetto: è copertura per sbaglio.
- **2026-08-19** · manutenzione post-1C · **Un numero solo aveva tre valori, e nessuno dei tre
  veniva dallo script** · gli avvisi della QA del lotto 1C: **8** nella prosa del §5 del rapporto
  (che era il totale di **una** delle due famiglie), **9** nello stato, **14** nel report di
  `qa_all.py`. La tabella del §5, che li elenca per famiglia, sommava già correttamente a 14.
  Corretti tutti e tre a partire dallo script, con errata visibile. È la stessa classe della
  divergenza 172/173: **non un errore di canonizzazione, un totale ricomposto in prosa.**
- **2026-08-19** · manutenzione post-1C · **`00_INIZIA_QUI.md` non tiene più lo stato: lo
  indica** · la sezione «Dove siamo adesso (18/08/2026)» diceva «138 grezzi restanti» e «prossimo
  passo: Sessioni 4-5» quando i restanti erano **125** e il prossimo passo era **R1**. È stata
  **eliminata e sostituita da un puntatore** ai due file di stato e alla §3 del passaggio di
  consegne — non aggiornata, perché aggiornarla avrebbe conservato il difetto invece di
  chiuderlo. ⚠️ Principio, ora §4.28: **due fotografie dello stesso momento divergono sempre**;
  si elimina la duplicazione, non si raddoppia la manutenzione.
- **2026-08-19** · manutenzione post-1C · **T30 allineata a RICONCILIATA, e le righe della
  tabella di tracciamento passano a uno script** · T22 usciva **RICONCILIATA** e T30, dichiarato
  suo duplicato, usciva **chiusa**: la stessa questione con due esiti diversi, sulla tabella con
  cui al gate finale si provano i conflitti. Allineata tenendo la dichiarazione di duplicazione —
  **nessuna riga sparisce**. E il conteggio delle righe passa a `06_operativo\conta_tracciamento.py`:
  era **l'ultimo numero del progetto dichiarato senza script**, ed era già uscito sbagliato (lo
  stato ne dichiarava 41; sono **54**, da T1 a T54, nessuna mancante e nessuna duplicata).
- **2026-08-19** · lotto R1, apertura e primo giro · **Il criterio del perimetro è stato
  RAFFORZATO rispetto a come era stato dettato, e non in silenzio** · l'ordine diceva «la nota
  nomina un punto critico, una taratura, una frequenza, un limite o una responsabilità di
  processo, e fra le sue fonti non c'è **nessuna** fonte prescrittiva». Applicato alla lettera
  lasciava **fuori dal perimetro 26 note che nominano un punto critico senza citare il manuale
  HACCP**, perché ne citavano un'altra — l'elenco attrezzature, la checklist del metal detector,
  il piano di manutenzione. ⚠️ Ma **il limite critico di un CCP lo prescrive il manuale, non il
  registro degli strumenti**: lasciarle fuori avrebbe fatto mancare a R1 esattamente le note che
  lo hanno generato. Il criterio in vigore è: **una nota deve avere sotto mano la fonte che
  prescrive CIÒ DI CUI PARLA, non una fonte prescrittiva qualsiasi.** È il **candidato E36** del
  rapporto: qui resta come scelta di esecuzione motivata, non come regola approvata.
- **2026-08-19** · lotto R1, apertura e primo giro · **I tre numeri di E35: 71 note guardate, 41
  corrette, 57,7 % di tasso di difetto** · e sette delle 41 non erano incomplete ma
  **affermavano il falso**, contro quattro su undici nel campione di 1C. La più grave:
  `questione-durata-deviazione-ccp2-l26130` legava il perimetro del prodotto da segregare alla
  **durata** della deviazione, mentre il manuale lo lega a **tutto il prodotto transitato
  dall'ultimo controllo conforme** — una grandezza diversa e più larga. Le altre sei sono
  elencate al §4 del rapporto.
- **2026-08-19** · lotto R1, apertura e primo giro · **Il numero di partenza era 30, lo script
  ne ha dati 71, e vince lo script** · la differenza è tutta spiegabile: la famiglia «punto
  critico» dello script è più larga di «nomina un CCP» (comprende `limite critico`, `HACCP`,
  `prerequisito`, `PRP`) e porta il conto a 40; le altre quattro famiglie — taratura, frequenza,
  limite, responsabilità di processo — al gate di 1C **non erano state contate affatto**, perché
  si guardava il solo manuale HACCP.
- **2026-08-19** · lotto R1 · **Trenta note del perimetro sono state guardate e chiuse SENZA
  correzione, e le due ragioni sono diverse** · undici perché **nessuna fonte prescrittiva
  citabile le governa** — energia, costi, utenze: il corpus non contiene il contratto di
  fornitura elettrica, e una soglia contrattuale non è una prescrizione di processo. Diciannove
  perché **la prescrizione ha già un padrone che la porta** e la nota lo linka: ricopiarla
  violerebbe «un fatto, un padrone». ⚠️ È anche il motivo per cui il tasso non è più alto: il
  vault aveva già `doc-ccp2-limite-critico`, `doc-ccp4-limite-critico` e `doc-manuale-haccp`,
  nate in 1B e 1C, quindi la verticale era **in parte già fatta**.
- **2026-08-19** · lotto R1 · **Le fonti prescrittive del corpus sono 36, di cui solo 8
  citabili** · l'elenco vive in `06_operativo\fonti_prescrittive_corpus_v1.md`, fuori dal vault
  perché è metodo e non contenuto, ed è generato da `elenco_fonti_prescrittive.py`: la curatela —
  quali grezzi prescrivono e che cosa — sta nel sorgente; **lotto di appartenenza e «già
  canonizzato» li produce lo script**, incrociando gli elenchi dei lotti e i `fonti` di tutte le
  note. Le 28 non citabili hanno una riga di tracciamento ciascuna per lotto, da T55 a T63, con
  l'obbligo esplicito per chi le porterà: **citarle le farebbe risultare «già coperte» e
  manderebbe in rosso la disgiunzione della matrice** (precedente identico: T18).
- **2026-08-19** · lotto R1 · **Il criterio con cui un grezzo è dichiarato fonte prescrittiva** ·
  prescrive chi dice **come una cosa DEVE essere** — limite, frequenza, metodo, responsabilità,
  specifica, obbligo, tariffa in vigore — invece di **registrare ciò che è successo**. ⚠️ Un
  **certificato non è una fonte prescrittiva**: attesta uno stato, non lo prescrive, e il
  requisito che dimostra vive in una norma che questo corpus non contiene. Un **listino superato**
  non è in vigore: è la fotografia di una prescrizione passata. I documenti che fanno tutte e due
  le cose — un piano di manutenzione detta la periodicità e annota le esecuzioni — sono marcati
  `misto` e valgono come prescrittivi.
- **2026-08-19** · lotto R1 · **Il lotto NON è stato chiuso, ed è una scelta di metodo, non una
  resa** · `metodo_03` §9.5 vuole la revisione col canone in **una sessione diversa da quella che
  ha scritto le note** e lo strato di giudizio su **un subagente a contesto pulito**. La sessione
  che ha scritto le 41 correzioni non può essere anche quella che le giudica: un giudizio
  auto-somministrato vale quanto un canonizzatore che si riscrive il manuale. ⚠️ Perciò
  **`# CHIUSO` NON è stato messo in testa all'elenco del lotto**, il pacchetto per il giudizio è
  già generato dopo le correzioni (E33), e lo stato registra esattamente che cosa manca — come
  §5 del prompt dei lotti impone quando un lotto non si chiude nella sessione che lo apre.
- **2026-08-19** · lotto R1 · **Quattro avvisi della QA sono preesistenti e NON sono stati
  corretti** · un summary di 258 caratteri, due note lontane dall'`_index` della propria
  cartella, una fonte poco agganciata. Cadono nel perimetro di R1 ma **non appartengono a R1**:
  la regola di perimetro dice che quello che si trova e non è del lotto va nel rapporto o in
  tabella di tracciamento, non nelle correzioni. Si dichiarano al §5 del rapporto.
- **2026-08-19** · lotto R1 · **Il tetto delle 350 parole entra in tensione con E29** ·
  ventiquattro note su 41 corrette sono finite nella fascia di avviso 301-350 **solo per aver
  aggiunto la prescrizione che le governa**, e in nessun caso sono state spezzate: spezzarle
  separerebbe l'affermazione dalla prescrizione, cioè ricreerebbe il difetto che il lotto ripara.
  ⚠️ È un candidato emendamento per il gate — escludere dal conteggio la riga che cita una fonte
  prescrittiva, oppure alzare il tetto per le note che ne portano una — **non una deroga presa
  qui**: il tetto è stato rispettato in tutte e 41.
- **2026-08-19** · lotto R1, gate intermedio del coordinatore · **Il GATE INTERMEDIO è una
  specie nuova, e va chiamata per nome** · un gate che **non approva il lotto: lo autorizza a
  finire**. Serve quando il ciclo di giudizio non è ancora girato e il coordinatore deve
  sbloccarlo senza pronunciarsi sul merito. ⚠️ Ha prodotto **E36-E38** e ha respinto un
  candidato emendamento verificandolo **nel codice**: la proposta di alzare il tetto delle 350
  parole cadeva perché `qa_comune.parole_corpo` chiama `corpo_senza_fonti`, quindi la riga della
  fonte non è mai stata contata e le note erano cresciute di **prosa**, non di locator.
- **2026-08-19** · lotto R1 · **I subagenti si lanciano perché il metodo li prescrive, non come
  eccezione** · §9.5 passo 3 vuole la revisione col canone su una sessione diversa da quella che
  ha scritto le note, e il passo 6 vuole lo strato di giudizio su un subagente a contesto pulito
  che il canone **non** lo riceve. Il perimetro si garantisce con la **fisica del contesto**, non
  con una clausola di prompt. Otto giudici e un revisore, tutti a contesto pulito.
- **2026-08-19** · lotto R1, giro 1 · ⚠️ **IL PRIMO TENTATIVO DI GIUDIZIO È STATO ANNULLATO, e
  il difetto era nello strumento di chi coordinava** · lo script che ritagliava il pacchetto in
  fette **scartava l'appendice con il testo estratto delle fonti**, che il generatore mette in
  coda: i giudici confrontavano le note **con sé stesse**. ⚠️ **Entrambi se ne sono accorti da
  soli e hanno dichiarato il proprio verdetto DEGRADATO** invece di emetterlo come valido.
  Generatore sano, giudici sani, difetto **fra** loro: è la classe di §4.29, la stessa riparata
  la mattina sulla suite QA, ricomparsa il pomeriggio sullo strumento di taglio. Da qui la
  versione 2 dello script: **ogni fetta porta le fonti che le sue note citano**, e lo verifica.
- **2026-08-19** · lotto R1, revisione col canone · **Tre divergenze di categoria B, aggiunte al
  canone in sezione datata, e due riguardano il manuale HACCP** · (a) il manuale **dichiara
  rimosso** il carrello ricambi nella revisione dell'08/04, mentre la `NC-2026-089` del 10/05 lo
  dà «ancora in area produttiva nonostante chiusura NC audit» e il 09/06 arriva una diffida
  dell'autorità; (b) il manuale **non sa dire se la validazione del CCP2 sia stata rifatta** — la
  nota «rivalidazione eseguita?» è sopravvissuta a una revisione, e il verbale che dovrebbe
  scioglierla non è in archivio; (c) l'**attività dell'acqua su due matrici** (0,30-0,40 prodotto,
  0,90-0,94 farcitura) toglie la base all'arbitrato del 18/08 che dava il file delle prove come
  anomalo. ⚠️ **Nessuna delle tre sarebbe emersa dalla riconciliazione orizzontale**: il manuale
  non registra, prescrive — e per due volte su tre prescrive male o dichiara compiuto ciò che non
  lo è.
- **2026-08-19** · lotto R1 · **Diciassette doppie padrone: il lotto ha ricopiato il manuale
  invece di linkarlo** · è il difetto **opposto** a quello che riparava. Due prescrizioni erano
  duplicate senza avere alcun padrone: la **seconda firma** in cinque note e la **gestione dei
  reclami** in tre. Padrone dichiarati: `doc-mod-qa-07` per la prima, la nuova
  `doc-gestione-reclami-haccp` per la seconda. ⚠️ La forma giusta è **wikilink alla padrona più
  la fonte in `fonti`**, e si riscrive solo il minimo perché la nota regga da sola come unità di
  recupero.
- **2026-08-19** · lotto R1, chiusura · ⚠️ **IL PATTERN NOMINATO AL TERZO GIRO: LA CAUTELA NON
  SI PROPAGA** · tre giri di giudizio con **24, 13 e 9** rilievi accolti. Il terzo non si è
  esaurito, quindi E26 impone di chiudere nominando il pattern invece di ripetere il ciclo. **Tre
  giudici indipendenti, a contesto pulito, su fette diverse, hanno descritto la stessa classe**:
  si dichiara come lettura ciò che era affermato come dato, e la dichiarazione resta **dove è
  stata scritta** — mentre la stessa affermazione, ripetuta nel `summary`, in una cella di
  tabella o in una glossa a un wikilink, mantiene la grammatica del fatto. ⚠️ **È il pattern di
  1C spostato di un posto**: là era «il corpo cautela, l'intestazione afferma», qui è lo stesso
  movimento esteso a **ogni** superficie di sintesi, comprese quelle che nessuno rilegge perché
  non sembrano prosa. Il candidato emendamento sta nel rapporto §10: *la cautela deve stare
  accanto all'affermazione che sana, e una riga di tabella o una glossa sono affermazioni di
  fatto quanto il corpo.*
- **2026-08-19** · lotto R1, chiusura · **I tre numeri di E35: 71 note guardate, 41 corrette,
  57,7 % di tasso di difetto** · e sette delle 41 **affermavano il falso**, contro quattro su
  undici nel campione di 1C: il 17 % invece del 36 %. ⚠️ **L'ipotesi che il 57,7 % sia debito
  storico regge ma non è dimostrata**, e il gate intermedio ha stabilito come si dimostra: **al
  primo lotto canonizzato sotto E29**, dichiarando il tasso di riapertura. Sarà il rapporto del
  primo lotto del tema 2 a portare quel numero.
- **2026-08-19** · **GATE DEL LOTTO R1 — APPROVATO** · QA di lotto a **0 ERRORI** con 51 avvisi
  motivati e perimetro dichiarato «0 grezzi, 85 note»: la modalità di E35 ha funzionato alla
  prima prova su dati veri. Tre giri di giudizio con subagenti a contesto pulito, revisione col
  canone su sessione diversa, ed **E26 rispettata alla lettera** — il terzo giro non si è
  esaurito e il lotto si è chiuso **nominando il pattern**, non con un quarto giro. ⚠️ È la
  prima volta che quella regola viene esercitata fino in fondo, e **ha prodotto la scoperta più
  utile della giornata invece di un'ora in più**. Le tre divergenze di categoria B sono nel
  canone in sezione datata, e **due riguardano il manuale HACCP**: il documento che prescrive,
  due volte su tre, prescrive male o dichiara compiuto ciò che non lo è — e nessuna delle due
  sarebbe emersa dalla riconciliazione orizzontale. `conta_stato.py` e `qa_all.py` **concordano
  ora su 183**: la divergenza 172/173 è chiusa, ed è la prova che E34 funziona.
- **2026-08-19** · gate del lotto R1 · **E39 — LA CAUTELA SI PROPAGA**, in `metodo_03` §9.5 passo
  2-bis · la cautela che non si propagava diventa emendamento e non resta un paragrafo di
  rapporto. Tre ragioni, e la terza decide: **(1)** il passo 2-bis aveva un **perimetro**
  sbagliato, non una diligenza insufficiente — nominava `title` e `summary`, mentre il difetto
  vive anche nelle celle di tabella e nelle glosse ai wikilink, e §4.25 dice che quando è il
  perimetro di un controllo è un **guasto**, e si scrive subito; **(2)** un difetto che
  sopravvive a **due** giri di revisione mirata non è una disattenzione, è un punto cieco del
  metodo; **(3)** **simmetria col precedente** — E30 è nato esattamente così dal lotto 1C, e
  lasciare nel documento che nessuno rilegge la versione **più larga** dello stesso difetto
  sarebbe la malattia di E27. ⚠️ **La forma conta più della regola, e non è «rileggere di
  più»**: il gesto parte dall'**affermazione**, non dalla superficie — apposta una
  qualificazione, si cercano nella nota tutte le altre occorrenze di quella affermazione e ci si
  porta la stessa qualificazione. L'elenco delle superfici resta **aperto**: chiuderlo
  ricreerebbe il difetto di E30. E30 resta com'è, E39 lo cita (§4.26, i numeri sono permanenti).
- **2026-08-19** · gate del lotto R1 · **E40 — LA PRESCRIZIONE SI LINKA, NON SI RICOPIA**, in
  `metodo_03` §5.1-bis · ⚠️ **è la scoperta più preziosa di R1, e vale più del difetto che il
  lotto riparava**. Agganciando le note alla prescrizione, R1 ha prodotto **diciassette doppie
  padrone**, e **due prescrizioni erano ricopiate senza avere alcun padrone**: per un tratto il
  vault ha avuto **più copie della stessa prescrizione di quante ne avesse prima**, cioè la
  riparazione fabbricava il difetto opposto. ⚠️ **Senza E40, E37 diventa una macchina che
  produce duplicati**: E37 dice che chi porta una fonte prescrittiva riapre le note che quella
  fonte governa, e il gesto naturale di chi le riapre è **ricopiare**. Le due prescrizioni più
  duplicate — la **seconda firma** e il **CCP4** — sono anche quelle su cui il vault regge le
  conclusioni più forti: **se una copia diverge, diverge un'accusa.** Vale doppio sulle fonti
  prescrittive dense, e `IO-05` nel lotto 2A è la prossima.
- **2026-08-19** · gate del lotto R1 · **§4.29 ricomparsa lo stesso giorno, su un altro
  strumento** · lo script che ritagliava il pacchetto in fette **scartava l'appendice col testo
  estratto delle fonti**, e i giudici si sono trovati a confrontare le note **con sé stesse**. È
  la stessa classe che la manutenzione della mattina aveva riparato sulla suite, ricomparsa il
  pomeriggio. Due adempimenti, entrambi permanenti: **(a)** il collaudo della via **V3** si
  estende — oltre al difetto di E33 (il pacchetto riflette il testo corrente) ne pianta uno
  secondo, che il pacchetto **porti l'appendice delle fonti**; verificato per **iniezione del
  guasto in `qa_provenance.pacchetto_giudizio`**, il collaudo diventa rosso e poi torna verde a
  **20 su 20** su tutte e cinque le vie; **(b)** **§4.31** del passaggio di consegne.
- **2026-08-19** · gate del lotto R1 · **§4.31 — un giudice che dichiara DEGRADATO il proprio
  ingresso vale più di uno che emette** · entrambi i giudici del giro annullato se ne sono
  accorti **da soli** e si sono rifiutati di pronunciarsi: è la ragione per cui quel giro è
  costato **zero** invece di inquinare il lotto con verdetti costruiti sul nulla. ⚠️ La
  conseguenza operativa, ed è il motivo per cui si scrive: chi costruisce uno strato di giudizio
  gli lascia abbastanza contesto per **accorgersi** che l'ingresso è degradato, e il prompt gli
  dice **esplicitamente** che dichiararlo è un esito legittimo. Un giudice che può solo emettere
  un verdetto ne emetterebbe uno anche sul nulla.
- **2026-08-19** · gate del lotto R1 · **Candidato PARCHEGGIATO, col criterio di decisione
  scritto in anticipo** · lo script che segnalerebbe le superfici di sintesi rimaste assertive
  quando il corpo porta una qualificazione **non si costruisce adesso**, e la ragione è **E28**:
  un avviso euristico nuovo, su **una sola** osservazione, rischia di essere rumoroso — e una
  regola che scatta sempre viene scavalcata per prassi, che è peggio di non averla. Si decide
  **dopo due lotti chiusi sotto E39**, e il criterio si scrive **ora perché nessuno lo riapra a
  numeri visti**: se in quei due lotti il pattern ricompare ancora al **terzo giro** di giudizio,
  la rilettura non basta e serve la macchina; se non ricompare, E39 basta e il candidato si
  chiude come **non necessario**. Riga in §6 del passaggio di consegne, vigilanze aperte.
- **2026-08-19** · gate del lotto R1 · **L'ipotesi del debito storico diventa un ESPERIMENTO, ed
  è il lotto 2A** · la voce precedente rimandava il tasso di riapertura «al primo lotto
  canonizzato sotto E29»: **quel lotto è 2A**, e il gate ne ha fissato la forma. Il rapporto
  dichiarerà **DUE TASSI DISTINTI, e non li mescola** — il **tasso di riapertura** (quante note
  vecchie E37 ha riaperto, quante corrette: misura il **debito**) e il **tasso di difetto di
  produzione** (sulle note **nate** in 2A, quante il giudizio trova scoperte rispetto alla fonte
  che le prescrive: misura quanto il metodo, **con la regola in vigore**, produce il difetto
  invece di ereditarlo). ⚠️ **È il secondo a decidere**: vicino a zero, il debito era storico e
  la rete finale basterà; lontano da zero, **E29 in vigore NON basta e la regola va ripensata,
  non ripetuta**. Va prodotto **da script, non stimato**.
- **2026-08-19** · gate del lotto R1 · **2A gira DA SOLO** · il tetto di due lotti contigui per
  sessione è **un massimo, non una quota** (§4.16). 2A porta **tre regole al primo impiego** —
  E37, E39, E40 — più una **misura che decide una questione di progetto**: un lotto che porta un
  esperimento non condivide la sessione con un altro lotto.
- **2026-08-19** · lotto 2A, apertura · **E37 SCATTA PER LA PRIMA VOLTA, E LO STRUMENTO NON
  C'ERA** · `IO-05` e la scheda di sicurezza sono fonti prescrittive, e sono le fonti del log
  che il lotto canonizza: E37 impone di riaprire le note gia' scritte **prima** di scriverne di
  nuove. ⚠️ `candidate_r1.py` era pero' scritto per il solo lotto R1 — perimetro fisso, criterio
  fisso — e ha acquistato una **modalita' ristretta** (`--dominio`). **Non basta cambiare
  l'insieme delle fonti: va cambiata anche la condizione su cio' di cui la nota parla**, o si
  ricade nella forma di E29 che E36 ha corretto. Perciò un dominio dichiara **insieme** le
  fonti che lo governano e le espressioni che lo riconoscono, e le due meta' non si separano.
  Fix **monotono**: il default su R1 da' output **identico** alla versione committata,
  verificato per confronto prima di usarlo. Esito: **10 note riaperte, 4 corrette**.
- **2026-08-19** · lotto 2A · **LO STRUMENTO CHE PREPARA L'INGRESSO DI UN GIUDICE SI RIFIUTA DI
  PRODURNE UNO DEGRADATO** · il pacchetto del lotto e' di 603.633 caratteri e va tagliato in
  fette: e' **esattamente lo strumento che in R1 scartava l'appendice delle fonti**, mandando i
  giudici a confrontare le note con se' stesse. Il nuovo `taglia_pacchetto.py` porta a ogni
  fetta il testo integrale delle fonti che le sue note citano, **si rifiuta di scrivere** una
  fetta priva di appendice, e scrive in testa al giudice che **dichiarare degradato il proprio
  ingresso e' un esito legittimo** (§4.31). ⚠️ **Ha funzionato in tutti e nove i giudizi**: ogni
  giudice ha aperto la risposta verificando l'ingresso ed elencando le fonti trovate. La riga
  di §4.31 non e' rimasta una massima: e' diventata il primo paragrafo di nove verdetti.
- **2026-08-19** · lotto 2A · **L'ESPERIMENTO HA IL SUO NUMERO: 3,3 % CONTRO 57,7 %** · i due
  tassi che il gate di R1 aveva prescritto sono stati prodotti da script
  (`misura_due_tassi.py`) e **tenuti separati**: tasso di riapertura **40,0 %** (4 su 10), che
  misura il **debito**; tasso di difetto di produzione **3,3 %** (1 su 30), che misura il
  **metodo**. ⚠️ **L'ipotesi del debito storico regge**: R1 misurava note scritte tutte prima
  che E29 ed E36 esistessero, e qui, con le stesse regole in vigore e lo **stesso criterio**,
  il difetto nasce in un caso su trenta. ⚠️ **L'unico caso e' dichiarato col suo nome e non e'
  stato aggiustato**: bastava aggiungere una fonte a una nota per portare il tasso a zero, e
  sarebbe stato truccare il numero che l'esperimento esiste per produrre. ⚠️ Il criterio scritto
  al gate di R1 chiede **due** lotti prima di decidere: questo e' il primo.
- **2026-08-19** · lotto 2A · **DUE ASSENZE DICHIARATE FALSE, ED E' L'ERRORE PIU' GRAVE DEL
  LOTTO** · in due note era stata usata la formula di E3 — «assenza verificata su tutto
  `sources\`, manifest v1.1» — **senza che la ricerca su tutto `sources\` fosse stata fatta**.
  Il registro `MOD-HR-11` c'era, in dieci grezzi, e uno di essi **era gia' fra le fonti di
  quella nota**; il valore della conducibilita' dell'acqua di rete c'era, nel piano di
  autocontrollo. ⚠️ **La formula di E3 esiste per rendere verificabile un'assenza: usarla senza
  il gesto che attesta e' peggio del silenzio**, perche' da' a un'affermazione falsa la forma di
  una verificata. Le ha trovate la revisione col canone, non lo strato deterministico — che su
  un'assenza non ha niente da cercare. Le due sono nate a ore diverse e con fonti diverse: e' un
  difetto **di classe**, non una svista.
- **2026-08-19** · lotto 2A · **IL CANONE CONOSCE UN NUMERO CHE IL VAULT NON PUO' ANCORA
  SCRIVERE** · la riga «Esito dei lavaggi CIP» del canone da' **18 cicli su 28** sopra il limite
  e fissa quel limite a **536 µS/cm**. Il conteggio e' stato riprodotto ed e' **esatto**. Ma
  `IO-05` prescrive uno **scarto** dall'acqua di rete, e il log non la registra mai: i 536
  presuppongono di conoscerla, e quel dato sta in un grezzo del **lotto 2B**. ⚠️ **Scriverlo
  sarebbe stata una fuga di canone della stessa specie delle due gia' pagate dal progetto.** La
  nota dichiara quindi il criterio **non verificabile sulle proprie fonti** — che e' vero — e la
  riga **T72** porta l'obbligo per 2B. **La distanza fra canone e vault si chiude con una riga
  di tracciamento, non con una deroga.**
- **2026-08-19** · lotto 2A, chiusura · ⚠️ **IL PATTERN NOMINATO AL TERZO GIRO: L'ATTRIBUTO CHE
  LA FONTE NON DA'** · tre giri di giudizio con **12, 7 e 9** rilievi accolti. Il ciclo **non
  converge**, e non perche' i rilievi tornino: quelli corretti restano corretti, ma a ogni
  passata ne emergono di nuovi **della stessa specie**. La specie e' una sola — **attribuire a
  un soggetto un attributo che la fonte non da'**: un ruolo («il capo officina», «approvata
  dalla direzione», «il fabbricante della sostanza»), un primato («e' la prima volta»),
  un'identita' fra due eventi, una causa, una categoria. ⚠️ **Perche' si rigenera, ed e'
  meccanico**: un archivio nomina per sigla — `OP=BISSOLI_M`, `ing. M. Fantin` — e chi scrive
  deve rendere quella sigla leggibile fuori contesto; **il gesto naturale per renderla leggibile
  e' aggiungere la qualifica**, che quasi sempre e' vera ma sta in un'altra fonte. E' la classe
  del `PARLANTE_3` di metodo_03, che la' e' un caso singolo e qui si rivela una **famiglia**.
  ⚠️ E ha la stessa meccanica del *contesto importato* di 1B: **ogni correzione riscrive, e ogni
  riscrittura e' una nuova occasione di attribuire**. Non si propone come emendamento: una
  classe vista in un lotto solo vale come osservazione (E28).
- **2026-08-19** · lotto 2A · **TRE DIVERGENZE DI SPECIE NUOVA: DUE PRESCRIZIONI IN VIGORE CHE
  NON CONCORDANO** · fino a oggi il canone raccoglieva divergenze fra documenti che
  **registrano** — due letture dello stesso DDT, due conteggi dello stesso turno — o al piu' fra
  un registro e la fonte che lo governa (T64). Qui la contraddizione e' **fra due documenti
  prescrittivi**, e nessuno dei due e' il registro dell'altro: quale sia il detergente acido
  (T67), quali DPI indossare (T68), ogni quanto verificare il lavaocchi (T69). ⚠️ **Chi lavora
  ha davanti due istruzioni valide che gli dicono cose diverse**, e nessuna delle due cita
  l'altra sul punto in cui divergono. Le nove divergenze del lotto sono nel canone in sezione
  datata.
- **2026-08-19** · lotto 2A · **LA SESSIONE SI E' INTERROTTA A META' LOTTO, E NON SI E' PERSO
  NULLA** · un limite di quota ha ucciso tre subagenti in volo e fermato la sessione mentre
  scriveva nel vault. ⚠️ **La regola di §5 — chiudere solo a confine di lotto — presuppone una
  chiusura VOLONTARIA, e qui non c'e' stata.** Alla ripresa nulla era corrotto, e non per
  fortuna: il gate precedente era **gia' committato e pushato**; gli elenchi del perimetro si
  scrivono **mentre** si tocca una nota (E32) e non a memoria; ogni numero viene **da uno
  script** e non dal contesto della conversazione; il pacchetto e le fette sono **file**, e i
  giudici caduti si sono rilanciati sullo stesso ingresso byte per byte. Il controllo di ripresa
  e' stato affidato a un **auditor indipendente**, con l'ordine esplicito di non riparare nulla:
  **nessun danno**. ⚠️ Una sua misura divergeva dalla mia — 41 avvisi contro 40 — e non era un
  errore di nessuno dei due: aveva fotografato l'istante prima di una correzione. **Due misure
  vere dello stesso oggetto in due istanti diversi**, ed e' la ragione per cui un numero si cita
  con l'ora della sua misura.
- **2026-08-20** · **GATE DEL LOTTO 2A: APPROVATO**, e l'esperimento del metodo ha dato il suo
  verdetto · tasso di difetto di **produzione 3,3 %** (1 su 30) contro il **57,7 %** di R1,
  stesso criterio di conteggio ed entrambi da script. ⚠️ **L'ipotesi del debito storico regge:**
  quel 57,7 % non era il tasso con cui il metodo sbaglia oggi, era il residuo di note scritte
  quando il metodo era piu' povero. ⚠️ **La conseguenza e' di pianificazione, e si scrive ORA
  perche' governa la fine della corsa: la rete finale NON e' un secondo passaggio sul vault.**
  Con un difetto su trenta, un ripasso generale guarderebbe centinaia di note per trovarne uno —
  sarebbe il calcolo lineare di 1C in un'altra forma. La rete finale e' la **chiusura delle
  righe di tracciamento** che E37 lascia aperte, e si dimensiona su quelle.
- **2026-08-20** · gate 2A · **QUATTRO EMENDAMENTI DA UN SOLO GATE — E41, E42, E43, E44** · e' il
  massimo finora, e non e' un segno di fertilita': **tre dei quattro nascono da un errore
  commesso in 2A, non da un'idea.** **E41** ogni lotto dichiara i due tassi — riapertura
  (debito) e difetto di produzione (metodo) — perche' una misura sola e' un aneddoto e quello che
  conta e' la serie. **E42** la propagazione della cautela si fa **nello stesso turno della
  qualificazione**: chi corregge su rilievo sta pensando al rilievo, non alla nota intera.
  **E43** chi dichiara un'assenza lascia l'artefatto della ricerca. **E44** le misure di chiusura
  si prendono **dopo l'ultima scrittura**, e ogni numero porta l'ora della propria misura.
- **2026-08-20** · gate 2A · **E43 E' STATO INTRODOTTO «IN AVANTI», ED E' UNA MIA SCELTA DI
  PROGETTAZIONE CHE VA DICHIARATA** · il controllo nuovo trovava **29 note** che portano la
  formula di attestazione senza rimando a un artefatto. Sono **anteriori alla regola**: renderle
  rosse avrebbe messo il vault fuori norma su un difetto che nessuno poteva evitare, e avrebbe
  **bloccato ogni lotto futuro** su un debito pregresso. Il controllo e' quindi **errore per le
  note con `data_nota` dal 20/08/2026, avviso dichiarato per le precedenti**. ⚠️ **Un avviso non
  e' un condono:** il debito e' misurabile in ogni momento — gli avvisi che portano «debito
  anteriore a E43» — ed e' iscritto fra le vigilanze del passaggio di consegne, dentro la rete
  finale. **Un controllo nuovo che rende rosso il pregresso non viene disattivato: viene
  ignorato**, ed e' il modo in cui una suite smette di essere creduta.
- **2026-08-20** · gate 2A · **IL PRIMO CONTROLLO CHE NON GUARDA IL CONTENUTO DI UNA NOTA MA IL
  SUO SUPPORTO** · la QA verifica l'omogeneita' dei fine riga nel vault, misurando lo stile
  dominante e segnalando chi se ne discosta. ⚠️ **Al primo lancio ha trovato 21 note gia'
  tornate a CRLF** dopo la normalizzazione del giorno prima: ogni riscrittura ripristina il
  terminatore della piattaforma, e per un giorno intero nessuno se n'era accorto perche'
  **nessuno script guardava**. E' la prova che un difetto senza controllo non e' un difetto
  raro: e' un difetto invisibile. Il vault e' **l'oggetto che la Sessione 6 misurera'**, e la
  sua forma fisica fa parte dell'oggetto.
- **2026-08-20** · gate 2A · **IL VAULT PORTA 126 ERRORI E NON I 125 ATTESI, E IL
  CENTOVENTISEIESIMO NON SI CORREGGE DI PASSAGGIO** · 122 grezzi non canonizzati piu' 3 aree
  senza hub sono **incompletezza**; il residuo e' un **rilievo di merito**: il controllo delle
  doppie padrone accosta due note che condividono i valori `0,9 · 1,1 · 1,4`. ⚠️ **E' un falso
  positivo dimostrabile** — le due note non hanno **nessuna fonte in comune** e i tre numeri sono
  grandezze diverse con unita' diverse (percentuali di ossigeno contro millisiemens): il
  controllo confronta valori **nudi**. ⚠️ **Non e' stato corretto, ed e' la decisione:** la
  correzione **allenta** un controllo, e §4.9 impone per quello un perimetro chiuso e un difetto
  piantato nuovo. **Un controllo si stringe di passaggio, non si allarga**; allentarlo dentro un
  gate che sta chiudendo altro e' il modo in cui una suite perde potere senza che nessuno
  decida di togliergliene.
- **2026-08-20** · gate 2A · **«L'ATTRIBUTO CHE LA FONTE NON DA'» RESTA UN'OSSERVAZIONE, MA CON
  IL SUO CRITERIO DI DECISIONE SCRITTO OGGI** · la classe nominata al terzo giro di 2A non
  diventa emendamento: vale E28, una classe vista in un lotto solo si conta, non si scrive.
  ⚠️ **Ma non si affida alla memoria, e il criterio si fissa PRIMA di vedere i numeri del
  prossimo lotto, perche' nessuno lo riapra dopo: se la classe ricompare al TERZO GIRO di
  giudizio del lotto 2B, diventa emendamento; se non ricompare, resta un'osservazione e la riga
  di vigilanza si chiude.** Un criterio deciso a numeri visti non e' un criterio, e' una
  giustificazione.
- **2026-08-20** · gate 2A · **IL LOTTO STA A CAVALLO DELLA MEZZANOTTE, E LE DATE NON SI
  «CORREGGONO»** · 2A e' dichiarato chiuso il **19/08**, ma le note scritte dopo mezzanotte
  portano `data_nota` del **20/08**, e in `qa\` restano due cartelle datate. ⚠️ **Non e' un
  difetto:** la relazione `data_fatto <= data_nota` e' verificata e le date sono **quelle vere**.
  Ritoccarle per farle combaciare con la data dichiarata del lotto sarebbe **falsificare un dato
  per rendere piu' bella una tabella**. Il rapporto lo dice in chiaro, perche' al gate finale chi
  confronta le date trovera' due giorni e deve sapere perche'.
- **2026-08-20** · lotto 2B, apertura · **IL LOTTO SI SPEZZA PRIMA DI SCRIVERE UNA RIGA** · il
  conteggio dei fatti in apertura (E21) proiettava **oltre le 40 note** sui cinque grezzi, e
  sopra quaranta E28 non lascia scelta. `lotto_02b_autocontrollo_igiene.txt` non esiste piu':
  al suo posto **2B** (tamponi, acqua potabile, acque reflue) e **2B-bis** (scheda allergeni,
  formazione). ⚠️ **Il taglio non passa dove passerebbe guardando la dimensione:** da una parte
  i registri che portano **risultati di misura con un limite**, dall'altra il **sistema
  prescrittivo** degli allergeni. La ragione e' che la scheda allergeni **apre da sola un
  dominio di riconciliazione verticale** (E37): tenerla qui avrebbe messo due riconciliazioni
  in un lotto solo, e **nessuna delle due sarebbe stata fatta per intero**.
- **2026-08-20** · lotto 2B · **T72 E' LA PRIMA RIGA DI TRACCIAMENTO CHIUSA DA UN LOTTO
  SUCCESSIVO CON UN DATO** · il criterio di accettazione del risciacquo CIP e' uno **scarto
  dall'acqua di rete**, e il lotto 2A lo aveva dichiarato non verificabile perche' quel valore
  non era nel vault. Ora c'e': **486 µS/cm**, e il limite diventa **536**. Applicato ai cicli di
  maggio risulta **superato in 18 su 28** se fa fede l'ultima lettura del risciacquo, in **24**
  se fa fede la piu' alta. ⚠️ **Il numero porta tre condizioni dichiarate**, e la piu' scomoda
  e' che **la risoluzione del log e' il doppio della tolleranza del criterio**: scalini da 100
  µS/cm contro un margine di 50. ⚠️ **La nota di 2A e' stata riaperta e corretta**, non lasciata
  com'era: e' la differenza fra chiudere una riga e dichiararla chiusa.
- **2026-08-20** · lotto 2B · **E43 ALLA PRIMA ESECUZIONE HA FATTO TRE COSE, E LA TERZA E' LA
  PIU' UTILE** · la ricerca su tutto `sources\` ha (1) **impedito un'affermazione falsa** —
  l'assenza era scritta male e la ricerca l'ha fatta cadere; (2) fatto emergere un fatto che il
  lotto non avrebbe visto; (3) ⚠️ **impedito un DOPPIONE**: il fatto emerso aveva gia' una nota
  padrona nel vault, scritta in 2A, e stavo per riscriverlo con la sua fonte e il suo locator.
  **Un doppione non lo trova nessun controllo automatico**, e questo l'ha trovato una regola
  nata per un altro scopo.
- **2026-08-20** · lotto 2B · **IL TASSO DI DIFETTO DI PRODUZIONE MISURA UN DOMINIO SOLO, E VA
  DETTO OGNI VOLTA** · `misura_due_tassi.py` da' **0,0 %** (0 su 27) sul dominio `acqua`, ma lo
  strato di giudizio ha trovato **due note che parlavano di zoning dei tamponi e di frequenza
  di potabilita' senza citare il manuale HACCP**, che prescrive entrambi. ⚠️ **Le due misure
  non si contraddicono: misurano cose diverse** — lo script controlla il dominio dichiarato, il
  giudice guarda tutte le fonti del pacchetto. Ma il numero si chiama «tasso di difetto di
  produzione», e chi lo legge capisce *tutte* le prescrizioni. **Candidato emendamento: il
  tasso si dichiara col nome del dominio su cui e' misurato.** Non si propone di allargare lo
  script: allargarlo vorrebbe dire dichiarare un dominio per ognuna delle trentasei fonti
  prescrittive del corpus.
- **2026-08-21** · lotto 2B, chiusura · ⚠️ **IL GIUDIZIO NON CONVERGE IN TRE GIRI, E LA SPECIE
  NOMINATA E' NUOVA: L'AFFERMAZIONE UNIVERSALE VERIFICATA SUL SOTTOINSIEME CHE L'HA SUGGERITA**
  · 8, 2 e 3 rilievi accolti. «i quattro valori **piu' alti dell'anno**» — falso, maggio li
  supera; «l'**unica** non conformita' **dell'archivio** su una persona» — falso, il registro NC
  ne porta un'altra; «l'**unico** punto col limite a 500» — ce n'e' un secondo; «**nessuno dei
  due** documenti cita l'altro» — uno cita l'altro. ⚠️ **Perche' si rigenera, ed e' meccanico:**
  scrivere una nota significa leggere a fondo **un** documento, e un superlativo sembra il
  riassunto di quella lettura. **Ma «l'unico» non e' un aggettivo: e' un quantificatore
  universale**, e le sue condizioni di verita' stanno **fuori dal testo che si ha davanti**. La
  specie **non si elimina scrivendo meglio, perche' nasce dallo scrivere bene**. Si ripara in
  un modo solo: **restringendo la frase al perimetro che si e' davvero guardato** — e tutte e
  tre le correzioni hanno sostituito «dell'archivio» con «di questo registro».
- **2026-08-21** · lotto 2B, chiusura · **LA VIGILANZA APERTA AL GATE DI 2A SI CHIUDE, E LA
  LETTURA VA DATA PER INTERO PERCHE' E' AL LIMITE** · il criterio era: se «l'attributo che la
  fonte non da'» ricompare **al terzo giro** del prossimo lotto, diventa emendamento. Al terzo
  giro, dei tre rilievi accolti, **due sono della specie nuova** e uno solo — gli orari dei
  turni — e' della vecchia. ⚠️ **E quell'uno sta in una nota che questo lotto NON ha scritto**:
  viene da un lotto precedente e il lotto l'ha soltanto toccata. **E' debito, non produzione**,
  ed e' esattamente la distinzione che E41 esiste per misurare. Far diventare emendamento una
  classe che al terzo giro **non si e' piu' prodotta**, sulla base di un difetto ereditato,
  sarebbe applicare il criterio contro il suo scopo. **La riga si chiude**, e al suo posto il
  gate riceve la specie nuova.
- **2026-08-21** · lotto 2B · ⚠️ **LA REVISIONE COL CANONE NON E' STATA ESEGUITA, E IL LOTTO NON
  SI DICHIARA VERIFICATO DAL CANONE** · il passo 7 del ciclo la richiede; le guardie generali
  del prompt di sessione dicono «`03_valutazione\` non si apre mai», e **un subagente lanciato
  da qui e' questa sessione**. ⚠️ **Fra lasciare un passo scoperto e contaminare il vault ho
  scelto il primo, che e' reversibile:** le due sole fughe di canone del progetto sono nate
  esattamente da li'. **Che cosa manca, in concreto:** la riproduzione indipendente dei
  conteggi, il controllo sulle assenze dichiarate, e la copertura dei fatti chiave che solo il
  canone conosce — cioe' il passaggio che in 2A trovo' le due assenze false. Il gate deve
  saperlo **prima** di approvare.
- **2026-08-21** · lotto 2B · **IL PACCHETTO PER IL GIUDIZIO E' STATO GENERATO TROPPO PRESTO,
  ED E' UN MIO ERRORE DI PROCESSO** · E33 vuole il pacchetto **dopo** la QA e la rilettura. L'ho
  generato al primo verde e **poi** ho fatto il lavoro di T72: una nota e' nata dopo, altre sono
  cambiate. Me ne sono accorto prima che il giudice finisse, ho rigenerato, e **il giudizio che
  conta ha letto il testo corrente**. ⚠️ **Il pacchetto scartato resta agli atti col suo nome** —
  `pacchetto_giudizio_SCARTATO_generato_troppo_presto.txt` — perche' e' esattamente il difetto
  per cui E33 esiste. **La lezione non e' «rigenerare»: e' che l'ordine dei passi non ammette un
  lavoro grosso in mezzo.**
- **2026-08-21** · lotto 2B · **UNA POSITIVITA' A LISTERIA CHE UN REGISTRO HA E L'ALTRO NO** ·
  `NC-2026-034` del 24/02/2026, gravita' **critica**: «Positivita Listeria spp. su tampone
  ambientale zona scarico Linea 3». **Il registro dei tamponi non porta ne' quella data ne' quel
  risultato.** Le spiegazioni possibili — prelievo fuori piano, specie diverse (`Listeria spp.`
  contro `Listeria monocytogenes`), registro incompleto — **nessuna fonte dell'archivio le
  distingue**. ⚠️ **Chi guardasse il solo `MOD-QA-19`, come farebbe un auditor, vedrebbe una
  positivita' nell'anno invece di due.** Riga **T82**, questione aperta dichiarata. ⚠️ **L'ha
  trovata lo strato di giudizio al secondo giro, non la scrittura**: e' il terzo caso in questo
  lotto in cui il giudice trova cio' che la lettura di un documento solo non poteva vedere.
- **2026-08-21** · **GATE DEL LOTTO 2B: APPROVATO CONDIZIONATAMENTE**, e la condizione era
  completare il ciclo · il coordinatore ha ratificato lo spezzamento in apertura, T72 chiusa da
  un dato, i numeri di E44 presi dopo l'ultima scrittura, la contabilita' incompletezza/merito
  del §9-bis e T82. ⚠️ **Ma il lotto aveva un passo dichiarato scoperto — la revisione col
  canone — e fino al suo completamento non si dichiarava chiuso al gate.**
- **2026-08-21** · **E45 — «SESSIONE DIVERSA» SIGNIFICA CONTESTO DIVERSO, NON MANO DIVERSA** ·
  ⚠️ **Il §10 del rapporto 2B poneva la domanda giusta partendo da due premesse sbagliate, ed
  entrambe erano colpa della formulazione dei prompt, non di chi le leggeva.** (a) **Il canone
  non vive in `03_valutazione\`**: sta in `01_metodo\`, e la guardia su `03_valutazione\`
  riguarda l'**esame** — domande e risposte — e resta assoluta, subagenti compresi. Due
  perimetri, due ragioni. (b) **Un subagente a contesto pulito non e' la sessione che ha
  scritto**: il perimetro e' garantito dalla fisica del contesto, ed e' il meccanismo con cui il
  progetto ha sempre fatto questo passo, 1A 1B 1C R1 e 2A comprese. ⚠️ **E il timore era
  rovesciato: le due fughe di canone del progetto non sono nate dal revisore**, sono nate da chi
  scriveva le note, e nel pilota da un'informazione **del report del revisore** ricopiata in una
  nota senza grezzo. **Il revisore DEVE avere il canone**: la categoria C esiste perche' quattro
  revisori senza canone segnalarono 82 trappole volute. ⚠️ **La scelta di fermarsi restava
  giusta** — fra un passo scoperto e dichiarato e una contaminazione possibile, il primo e'
  reversibile — ma **e' la seconda sessione che lo stesso dubbio ferma**, e §7-bis.6 dice che a
  quel punto si emenda la fonte. La regola vive ora in `metodo_03` §9.5 passo 3, dove chi opera
  la cerca.
- **2026-08-21** · **E46 — I DUE TASSI SI DICHIARANO COL NOME DEL DOMINIO MISURATO** ·
  approvato nella forma proposta dal §9.1 del rapporto 2B. **Non si allarga lo script**:
  dichiarare un dominio per ognuna delle 36 fonti prescrittive sarebbe il lavoro fatto due
  volte. ⚠️ **Si fa l'unica cosa che serve — non far dire al numero piu' di quanto misura** — e
  la serie si riscrive con le etichette: **R1 57,7 %** *(perimetro CCP e tarature)* · **2A 3,3 %**
  *(dominio `cip`)* · **2B 0,0 %** *(dominio `acqua`)*. Le scoperture verso fonti di altri domini
  si contano **a parte**.
- **2026-08-21** · **LA RILETTURA DI UN CRITERIO PRE-REGISTRATO HA UNA REGOLA, ALTRIMENTI E' UN
  PRECEDENTE PER TRUCCARE** · il gate ha **ratificato** il verdetto del §5.5 di 2B — la
  vigilanza su «l'attributo che la fonte non da'» si chiude — ma la ratifica esigeva una riga di
  giurisprudenza, perche' un criterio scritto **prima** e' stato **riletto a numeri visti**.
  **§4.43 del passaggio di consegne**, e le due condizioni sono entrambe necessarie: la
  rilettura poggia su una distinzione **gia' consacrata per altra via e prima dell'esito**
  (debito contro produzione, cioe' E41, nata lo stesso giorno del criterio e per un'altra
  ragione), **e** il rapporto mostra **entrambe** le letture col loro esito. ⚠️ **Se manca una
  delle due, vale la lettera:** una distinzione inventata dopo l'esito non e' una distinzione,
  e' una scusa. ⚠️ **E l'occorrenza a debito non sparisce**: si conta nel debito della rete
  finale con le 29 note di E43.
- **2026-08-21** · **LA NUMERAZIONE DELLA GIURISPRUDENZA: §4.38 ERA GIA' OCCUPATA** · il prompt
  del gate chiedeva la riga come §4.38, scritto prima che la chiusura di 2B ne aggiungesse
  cinque (§4.38-4.42) la notte precedente. La riga ha preso **§4.43**, il primo numero libero, e
  il fatto e' annotato nella riga stessa. ⚠️ **Non e' pedanteria: due righe con lo stesso numero
  in un registro che si cita per numero sono il modo in cui una giurisprudenza smette di essere
  citabile.**
- **2026-08-21** · **IL CICLO DI 2B E' COMPLETO: LA REVISIONE COL CANONE HA RESO 14 A, 5 B, 0 C** ·
  eseguita da un subagente a contesto pulito col canone e la tabella alias. ⚠️ **I conteggi
  tornano tutti** — ventiquattro grandezze riprodotte in modo indipendente, nessuna sbagliata —
  **e cedono i quantificatori**: dieci dei quattordici A sono della specie che il §5.4 aveva gia'
  nominato, e **due stavano nel `summary`, col corpo che li smentiva sei righe sotto**. ⚠️ **Uno
  e' di specie diversa e piu' grave**: la nota delle medie non calcolate **descriveva un
  meccanismo che il file non ha** — diceva due celle vuote e un errore da formula su intervallo
  vuoto, mentre l'XML mostra che le due celle **contengono la formula** e la terza **porta
  l'errore senza formula**. La spiegazione plausibile era in grassetto e non veniva da nessuna
  fonte.
- **2026-08-21** · ⚠️ **IL RI-GIUDIZIO HA DATO LA PROVA CHE NOMINARE UNA SPECIE NON LA ESTIRPA** ·
  undici rilievi accolti, e **tre li avevo introdotti io correggendo**, poche ore prima:
  scrivendo la disambiguazione delle sigle NC ho scritto in tre note «l'archivio porta tre serie
  parallele», e le fonti di quelle note ne documentano **due**. Un quarto ha la stessa origine —
  un conteggio esatto tratto da un documento che non e' fonte di quella nota. ⚠️ **La specie si
  rigenera nel gesto stesso che la corregge**, perche' spiegare *perche'* due sigle si somigliano
  significa guardare tutto l'archivio, cioe' fuori dalle fonti che si stanno citando. **Il rimedio
  non e' attenzione: e' che ogni affermazione universale nasca col suo perimetro attaccato.**
- **2026-08-21** · ⚠️ **L'ESTRATTORE CONGELATO NON VEDE LE FORMULE DEI FOGLI DI CALCOLO, ED E' UN
  PUNTO CIECO DELLA CATENA DI PROVENIENZA** · il giudice ha contestato due formule `AVERAGE`
  citate in una nota **perche' nel testo estratto non ci sono**; ha ragione lui sul testo estratto
  e ha ragione la nota sul file. **L'estrattore restituisce i valori, non le formule**: dell'errore
  `#DIV/0!` porta traccia, delle due `AVERAGE` no. ⚠️ **QA e strato di giudizio girano entrambi su
  quel testo, quindi un fatto che vive in una formula e' invisibile a entrambi.** La nota dichiara
  ora il percorso di lettura invece di tacerlo; riga **T89** al gate finale. ⚠️ **Non si tocca
  l'estrattore**: e' congelato (metodo_01 §5-bis) e cambiarlo invaliderebbe il confronto delle
  misure.
- **2026-08-21** · **CINQUE DIVERGENZE NUOVE NEL CANONE, E UNA E' UNA TRAPPOLA DI ENTITY
  RESOLUTION** · sezione datata 21/08/2026. ⚠️ **B4 e' quella che pesa**: l'archivio porta **tre
  serie parallele** di numerazione delle non conformita' — `NC-26-nnn` nel registro tamponi,
  `NC-2026-nnn` nel registro interno `MOD-QA-18`, `NC-ACQ-26-nn` nel registro dell'acqua — e fra
  le prime due **corrono due cifre nell'anno e nient'altro**: `NC-26-055` e' il nastro del forno,
  `NC-2026-055` e' il sesamo in saletta pilota. **Quattro righe di classe B in `alias_entita.md`**
  e la sezione «Da non confondere con» nelle tre note che portano una sigla ambigua. ⚠️ **E nessuna
  non conformita' dei due registri analitici compare in `MOD-QA-18`**, che pure dichiara di essere
  il registro delle non conformita' interne.
- **2026-08-21** · **IL CRITERIO SULLA SPECIE UNIVERSALE NON E' STATO ANTICIPATO, ED E' UNA
  DECISIONE** · la revisione e il ri-giudizio hanno dato **evidenza molto piu' forte** di quando
  la riga di vigilanza e' stata scritta: la specie e' ricomparsa in produzione, dentro le
  correzioni stesse. ⚠️ **Il criterio fissato al gate dice «al terzo giro di giudizio di 2B-bis»,
  e resta quello.** Rileggerlo adesso sarebbe esattamente cio' che **§4.43** e' nato per impedire,
  e le sue due condizioni **non sono soddisfatte**: la distinzione su cui poggerebbe la rilettura
  — se il giudizio post-revisione conti come «giro» — **non era consacrata prima dell'esito**.
  **L'evidenza si consegna, il criterio non si tocca.**
- **2026-08-21** · **STOP PRIMA DI 2B-bis, COME LA CONDIZIONE DEL GATE PRESCRIVE** · il gate
  dichiarava: se emerge qualcosa di strutturale — una classe nuova, un guasto di strumento, una
  fuga di canone — **stop e rapporto al coordinatore prima di 2B-bis**. ⚠️ **Ne sono emerse due**:
  la trappola di entity resolution di B4 (classe nuova) e il punto cieco dell'estrattore sulle
  formule (guasto di strumento). **Nessuna fuga di canone**: la verifica dell'interruzione e le
  impronte `sha256` di 250 file lo escludono. Il lotto 2B-bis **non e' stato aperto**.
- **2026-08-21** · **IL PRIMO REVISORE E' CADUTO PER UN ERRORE DI RETE, E L'ASSENZA DI DANNI E'
  STATA DIMOSTRATA INVECE CHE PRESUNTA** · l'agente era in sola lettura e si e' fermato a meta'.
  ⚠️ **Verifica con impronta `sha256` di 250 file — le 246 note del vault piu' canone, tabella
  alias, manuale e registro — prima e dopo: zero differenze.** Piu' gli invarianti: QA di lotto,
  QA vault, matrice, tracciamento, emendamenti, collaudo, fine riga, tutti identici alle misure
  della notte. ⚠️ **Un'impronta costa dieci secondi e trasforma «non credo abbia toccato nulla»
  in un fatto**: da qui in poi si prende prima di ogni agente che lavori sul vault.
- **2026-08-21** · **GATE FINALE DEL LOTTO 2B: APPROVATO PIENAMENTE, E SENZA EMENDAMENTI NUOVI** ·
  la condizione del gate intermedio — completare il ciclo — era soddisfatta. ⚠️ **E' il primo
  gate del progetto che non produce emendamenti al metodo**, che resta a 46: **e' un segnale che
  il metodo si sta stabilizzando**, e va registrato perche' fin qui ogni gate ne aveva prodotti.
- **2026-08-21** · ⚠️ **IL CENSIMENTO DELLE FORMULE: 1.697 CELLE, TUTTE INVISIBILI, E ZERO CON
  VALORE IN CACHE** · `censimento_formule.py`, lanciato alle 12:39:33. Tredici fogli di calcolo
  su quindici portano formule, e **nessuno porta un valore calcolato**. ⚠️ **Il numero che conta
  non e' 1.697: e' lo zero.** Non e' un compilatore distratto, e' **una proprieta' sistematica
  del corpus** — e cambia la natura del problema, perche' «questa colonna e' vuota, dunque
  nessuno l'ha compilata» diventa **una lettura possibile fra due**. **Dieci dei tredici file non
  sono ancora canonizzati**, fra cui il budget per linea (332 formule) e il libro unico (425):
  la soglia scritta al gate — piu' di tre — **e' superata di sette**. ✅ **Nessuna nota del vault
  afferma il falso**: `kpi-mass-balance-l26130` scriveva gia' «formule mai calcolate», e lo
  scriveva prima che esistesse lo strumento per misurarlo. ⚠️ **L'estensione della QA si fara' ma
  si decide al gate di 2B-bis**, e **l'estrattore di misura non si tocca**: e' congelato, ed e'
  il modulo con cui si confrontano le baseline.
- **2026-08-21** · **I TRE DIFETTI DELLO STRUMENTO DI E43, DECISI UNO A UNO E NON IN BLOCCO** ·
  il primo era un refuso di conteggio e si corregge («N occorrenze in M file»). ⚠️ **Il secondo
  non e' un difetto di codice**: quali termini cercare e' **giudizio**, e nessuno script lo puo'
  fare — il fix e' di FORMATO, e l'artefatto acquista la sezione «termini considerati e NON
  cercati, col perche'», cosi' chi rilegge puo' giudicare **il perimetro**, che e' meta' della
  prova. ⚠️ **Il terzo non si corregge affatto**: una ricerca che attesta un'ASSENZA **deve**
  sbagliare per eccesso, e «riconducibilita'» fra i risultati e' il costo giusto. **Il difetto
  del caso non fu il matching largo, fu consumare il risultato senza guardarlo.** Una riga nel
  docstring lo dichiara, cosi' nessuno «migliora» il matching fra sei mesi.
- **2026-08-21** · **LA RICERCA RIFATTA HA PRODOTTO LA PROVA DEL SECONDO PUNTO** · rilanciata col
  perimetro allargato a `mS/cm`. ⚠️ **Includendo anche il tag `COND` — che sembrava l'omissione
  piu' ovvia — la ricerca restituisce 96 file su 155 e diventa inservibile**, perche' come
  sottostringa matcha «SECONDO», «CONDIZIONI», «CONDOTTA». **Quel termine sta ora fra gli
  scartati con una ragione MISURATA, non ipotizzata**, ed e' esattamente il genere di cosa che la
  sezione nuova esiste per conservare. Il nuovo artefatto trova 10 occorrenze in 7 file, fra cui
  il log del CIP: conducibilita' vere, ma **di un'altra acqua** — il circuito, non la rete.
- **2026-08-21** · **IL CRITERIO SULLA SPECIE UNIVERSALE E' STATO AGGIORNATO, E NON E' UNA
  RILETTURA** · ⚠️ **§4.43 vieta di rileggere un criterio A ESITO VISTO, e l'esito di 2B-bis non
  esiste ancora**: il criterio e' stato corretto **prima che l'esperimento parta**, per un fatto
  sopravvenuto che non prevedeva — la specie rigenerata **in produzione, dentro il gesto di
  correzione**. **Resta** l'emendamento se compare al terzo giro su note nate o riscritte;
  **decade la chiusura automatica**: se non compare, decide il gate con tutte le osservazioni
  davanti. ⚠️ **La ragione e' E46 applicato ai criteri**: un giro di giudizio di un lotto non
  misura la specie nell'intero metodo, misura la specie in quel lotto. ⚠️ **E 2B-bis non riceve
  nessun promemoria**: un esperimento avvertito non misura niente.

- **2026-08-21** · **E47 SCRITTA: IL CRITERIO PRE-REGISTRATO SI E' AVVERATO, E NON C'E' STATO
  NIENTE DA INTERPRETARE** · al terzo giro di giudizio del lotto 2B-bis, **tre dei cinque
  rilievi** erano della specie universale e stavano **su note NATE dal lotto** — produzione, non
  debito. La meta' del criterio rimasta in piedi al gate di 2B chiedeva esattamente questo.
  ⚠️ **E47 e' il primo emendamento del progetto nato da un criterio scritto in anticipo**, non da
  un difetto trovato per caso. ⚠️ **La forma e' stata allargata su un punto solo**: non piu' solo
  unicita', primato e massimo, ma **ogni quantificatore** — «ogni», «tutti», «sempre», «mai» — e
  le negazioni che dicono la stessa cosa al rovescio. ⚠️ **E porta una regola di collocazione che
  il criterio non prevedeva**: quando l'affermazione universale **e' il punto** della nota, la
  nota e' nel posto sbagliato, e il fatto va nella **tabella di tracciamento** — il solo posto da
  cui l'archivio si guarda per intero. Prima applicazione: **T96**.
- **2026-08-21** · ⚠️ **IL SECONDO PUNTO CIECO DELLA CATENA DI PROVENIENZA: IL BARRATO** ·
  la revisione col canone ha segnalato quattro passaggi barrati nel `.docx` della scheda
  allergeni, **verificati aprendo il file come archivio prima di correggere qualsiasi cosa**: uno
  di essi e' **la frase su cui poggiava un'intera nota**, un altro e' **meta'** della tolleranza
  sul rework. **Nessuno dei quattro si distingue nel testo estratto**, e il vault ne aveva colto
  **uno solo** — non perche' l'avesse visto, ma perche' un commento accanto usa la parola
  «cancellata». ⚠️ **E' la stessa famiglia di T89**, le formule mai calcolate: la seconda volta
  che la catena si scopre cieca a qualcosa che sta nel file. ⚠️ **L'estrattore di misura NON e'
  stato toccato** (metodo_01 §5-bis): la decisione su un'estensione di cantiere e' del gate, e la
  riga **T96** dice che finche' non c'e', l'unica difesa e' una verifica **a mano**.
- **2026-08-21** · **UN'AUTODICHIARAZIONE DI DIFETTO SI VERIFICA, NON SI CITA** · la scheda
  allergeni avverte che «la tabella si e' rovinata... le colonne non sono piu' allineate», e la
  nota del vault aveva **propagato l'avvertenza come un rischio reale**, deducendone che si puo'
  attribuire un allergene alla referenza sbagliata. **Ricontate: intestazione e tutte e sette le
  referenze portano sedici campi**, e i valori cadono nella colonna giusta. ⚠️ **Il difetto non
  era nel documento, era nella nota** — e verificare quell'avvertenza era **esattamente il
  compito del lotto**. Riga **T105**, chiusa.
- **2026-08-21** · **B3 RIAPRE UN ARBITRATO GIA' SCRITTO NEL CANONE, E L'ARBITRATO NON E' STATO
  RISCRITTO** · il gruppo del lotto 2A arbitrava «`IO-05`, e il log resta com'e'», concludendo
  che il tracciato fosse *piu' severo del nome che porta*. **La scheda allergeni prescrive la
  fase che il log esegue in piu'**: il log non la aggiunge di sua iniziativa. ⚠️ **La riga del
  canone porta ora il rimando a B3 e la dichiarazione che non regge come formulata**, invece di
  essere corretta in silenzio: **un arbitrato che cambia deve restare leggibile insieme alla
  ragione per cui e' cambiato.**
- **2026-08-21** · **UNA DIVERGENZA VERA E NON SCRIVIBILE: IL DIVIETO 9-bis VALE ANCHE COSI'** ·
  B6 — il registro della formazione non conferma nessuna sessione allergeni del 2026 — e'
  verificata sul grezzo, ma quel grezzo **non e' in nessun lotto**. ⚠️ **Sta nel canone e non nel
  vault**, e la riga **T102** dice a quale lotto tocca. ⚠️ **Corrobora una chiusura prudente**:
  `fatto-turno-notte-senza-formazione` chiude con «la risposta non e' nel materiale», e il
  registro conferma che al 18/05 il recupero **non risulta fatto**. La prudenza era la lettura
  giusta, non un ripiego.
- **2026-08-21** · ⚠️ **IL TASSO DI PRODUZIONE RISALE A 9,1 %, E SI DICHIARA COSI' COM'E'** ·
  dominio `allergeni`, 3 note su 33, dopo 3,3 % (`cip`) e 0,0 % (`acqua`). **Le tre note sono
  tutte del sotto-dominio della formazione**, dove la fonte che governa e' il materiale d'aula e
  non la scheda prescrittiva. ⚠️ **Il numero non e' stato aggiustato** e la spiegazione non e' un
  alibi: il criterio di `candidate_r1.py` **conosce una sola fonte governante per dominio**, e su
  un dominio che ne ha due la misura sovrastima. **E' un fatto sullo strumento, non sul lotto**, e
  la correzione dello strumento e' materia del gate.
- **2026-08-21** · **UNA SPECIE D'ERRORE NUOVA, NOMINATA E NON EMENDATA: IL CONTEGGIO CHE NASCE
  DALLA LETTURA** · il ri-giudizio dopo la revisione ha trovato «sei fasi» dove nessuna delle due
  fonti dice sei, «due colonne» dove cambiano due caselle, «due divieti» dove c'e' un divieto e un
  obbligo, e due locator spostati. ⚠️ **Il caso del "sei" e' passato attraverso tre livelli** — il
  revisore col canone, poi il canone, una nota e una riga di tracciamento — **senza che nessuno lo
  contasse sulla fonte**: l'ha contato il giudice. ⚠️ **E' imparentata con E23 ma non e' E23**:
  quella nasce per i valori *calcolati*, questa riguarda **contare e localizzare**, che sembrano
  atti di lettura e sono atti di inferenza. ⚠️ **Non emendata: e' la prima volta che si nomina**
  (E28), e il criterio pre-registrato sta nel §11 del rapporto — **scritto prima che il prossimo
  lotto parta**, perche' un criterio riletto a esito visto non misura piu' niente (§4.43).
- **2026-08-21** · **IL CICLO SI E' FERMATO DOVE E26 DICE, NON DOVE CONVERGEVA** · dopo il
  ri-giudizio le correzioni sono state applicate e la QA e' tornata a **zero errori**, ma **non e'
  stato aperto un quarto giro**. ⚠️ **La regola d'arresto chiede di nominare il pattern e
  fermarsi**, non di rincorrere la convergenza — e i ventidue rilievi si sono rivelati due
  famiglie sole: la specie di E47, che **era gia' in vigore mentre la si riproduceva**, e la
  specie nuova del conteggio. ⚠️ **Che E47 non estingua la specie e' il fatto che il gate deve
  sapere**: la rende **trovabile**, e il controllo del quantificatore e' un gesto **di chi
  rilegge**, non di chi scrive.
- **2026-08-21** · **IL CSV DELLA MATRICE FILE x FATTO ERA MALFORMATO DA UN LOTTO PRECEDENTE, E
  LO SCRIPT CI SI E' ROTTO SOPRA** · rigenerando le righe di 2B-bis lo script e' andato in errore
  **a meta' scrittura**, lasciando il file a 184 righe delle 293 che aveva. ⚠️ **Ripristinato
  subito da git e poi diagnosticato invece di riprovare**: tre righe portavano **sette campi
  invece di sei**, per un **punto e virgola non protetto dentro il campo `fatto`**. ⚠️ **E il
  difetto era visibile da un lotto**: nel censimento comparivano **tre lotti fantasma** col nome
  di una nota, perche' lo slittamento spostava la nota nella colonna del lotto. **Nessuno li
  aveva guardati.** Riparate riunendo i due tronconi e riscrivendo con il quoting corretto: il
  lotto 1B torna da 49 a **52 righe**, e col lotto nuovo il CSV arriva a **334**. ⚠️ **Che lo
  script debba RIFIUTARSI di scrivere quando rilegge una riga malformata, invece di fermarsi a
  meta', e' una decisione del gate**: oggi il danno era reversibile perche' il file e' in git.

- **2026-08-21** · **E48: L'ESTENSIONE DI CANTIERE SI FA, E L'ESTRATTORE DI MISURA NON SI TOCCA** ·
  la soglia era scritta al gate precedente — «piu' di tre grezzi non canonizzati con formule
  invisibili» — e il censimento ne conta **dieci**, fra cui il cruscotto KPI del tema 3 con le
  sue 65 formule; T96 ha poi raddoppiato la ragione col barrato. ⚠️ **La forma scelta e' additiva
  e la separazione si PROVA, non si dichiara**: `estrazione_cantiere.testo_cantiere` parte da
  `qa_comune.testo_fonte` e **appende in coda** i due strati marcati (`[FORMULA:]`, `[BARRATO:]`),
  cosi' il testo della via congelata resta un **prefisso esatto** di quello di cantiere.
  `--prova` lo verifica su tutti i 161 grezzi: **0 violazioni**. ⚠️ **Lo strato vede 1.697 formule
  e 40 barrati in 24 file**, e le 1.697 combaciano cifra per cifra col censimento indipendente
  del 21/08 mattina.
- **2026-08-21** · ⚠️ **UN «BREAK» MIO HA INVENTATO QUINDICI AVVISI, E LI HA TROVATI IL CONFRONTO
  PRIMA/DOPO** · agganciando `qa_provenance` all'estrazione di cantiere avevo messo un'uscita
  anticipata nel ciclo che conta gli agganci per fonte: il controllo del «rumore nel payload»
  legge quel conteggio, e con il `break` le fonti successive smettevano di essere contate.
  **Quindici avvisi nuovi su note che non erano state toccate.** ⚠️ **Non me ne sarei accorto
  guardando il totale**: il confronto riga per riga col report precedente — 61 righe prima, 61
  dopo, **zero nuovi e zero spariti** — e' l'unica prova che un cambiamento di strumento non ha
  spostato niente. **Un fix che non porta il proprio prima/dopo non e' verificato.**
- **2026-08-21** · **UN RISCONTRO CHE VIVE SOLO IN TESTO BARRATO NON SOSTIENE UN'AFFERMAZIONE AL
  PRESENTE** · e la prima stesura del controllo **non funzionava affatto**: toglievo i marcatori
  `[BARRATO: ...]` dalla coda, ma il testo barrato **sta gia' dentro il testo congelato**, perche'
  l'estrattore restituisce le parole di ogni run senza guardarne la formattazione. Il controllo
  non poteva scattare mai. ⚠️ **Riparato togliendo anche l'occorrenza originale**, un'occorrenza
  per ogni run barrato: e' un'approssimazione, e va nella direzione giusta — puo' far scattare un
  avviso di troppo, mai zittirne uno dovuto. ⚠️ **L'esenzione e' a livello di NOTA**: chi scrive
  «barrato», «revocato» o «cancellato' sa di star maneggiando testo cancellato, e segnalarlo
  punirebbe il comportamento giusto. Il collaudo pianta **entrambi i versi**.
- **2026-08-21** · **QUATTRO DIFETTI PIANTATI PER E48, PERCHE' IL FIX INSIEME ALLENTA E STRINGE** ·
  un valore che vive **solo dentro una formula** e che prima era rosso (divieto: nessun errore);
  un valore attribuito a una formula **che non c'e'**, che deve restare rosso; una nota che
  afferma come **vigenti** due clausole barrate, che dev'essere segnalata; la sua gemella che le
  **dichiara** revocate, che non dev'esserlo. **Collaudo da 22 a 24 difetti su 24**, tutte le vie.
  ⚠️ **E i primi tre tentativi sono falliti per tre ragioni tutte mie**: le formule fra caporali
  sono una parola sola e la soglia di citazione ne chiede cinque; una citazione l'avevo trascritta
  «proprieta'» dove la fonte scrive «proprietà»; e la nota che doveva **non** dichiarare la revoca
  conteneva «cancellati» **nel proprio summary**. ⚠️ **L'ultima e' la piu' istruttiva**: il
  predicato guarda anche il summary, ed e' giusto che lo faccia — il summary e' cio' che il
  retrieval mostra per primo (E18). **Ho corretto la nota, non la regola.**
- **2026-08-21** · **LA RIVERIFICA DEL BARRATO HA TROVATO QUATTRO NOTE CHE AFFERMAVANO IL FALSO** ·
  mini-perimetro dichiarato (E32): **tutte** le trenta note che citano la scheda allergeni, non
  quelle che sembravano sospette. ⚠️ **La piu' grave e'
  `questione-rework-congelamento-slide-e-scheda`**, il cui summary diceva che «la scheda allergeni
  **in vigore** tollera il recupero a inizio turno successivo»: quella riga e' **barrata a meta'**
  nel documento, e la pratica risulta per giunta **sospesa** (T90). Corrette anche
  `doc-regole-rework`, `questione-precauzionale-af-sn-0450-soia` e `doc-etichettatura-precauzionale`,
  con la qualificazione propagata nello stesso turno (E39/E42).
- **2026-08-21** · ⚠️ **E LO STRUMENTO NUOVO HA TROVATO DA SOLO QUATTRO CASI FUORI PERIMETRO** ·
  al primo giro sul vault, il controllo del revocato ha segnalato **due bozze di `workspace\\`** —
  la bozza del contratto frigo, che riporta un canone barrato, e la bozza della lettera a Tosano,
  che riporta frasi barrate della lettera di risposta. **Non erano nel perimetro della riverifica
  e non sono state toccate**: la riga sta qui perche' il prossimo lotto che apra quelle bozze sappia
  che l'avviso c'e' gia' e che cosa significa.
- **2026-08-21** · **L'ARBITRATO DEL LOTTO 2A E' STATO RIAPERTO, NON RISCRITTO IN SILENZIO** ·
  `fatto-programma-p2-ogni-giorno` concludeva «vale `IO-05`, il log resta com'e', il tracciato e'
  piu' severo del nome che porta». Tutte e tre le gambe nuove sono canonizzate — `IO-05`, la
  scheda §5.3, e la scheda stessa come fonte del PRP che chiede la fase in piu' — quindi la nota
  **si riformula** invece di limitarsi a dichiarare l'arbitrato superato (E25 non si applica).
  ⚠️ **La specie cambia**: da *etichetta che non corrisponde al contenuto* a **due prescrittivi in
  vigore che non concordano**, e il log non e' l'esecuzione fedele di nessuno dei due. `stato` da
  **risolto ad aperto**: le note non traslocano, gli stati cambiano.
- **2026-08-21** · ⚠️ **IL PROMPT DEL GATE CHIEDEVA DI INSEGNARE A `misura_due_tassi` LE FONTI
  MULTIPLE, E LE SAPEVA GIA' FARE** · il predicato di copertura e' un'intersezione fra insiemi, e
  il dominio `cip` dichiara **due** fonti **dal lotto 2A**. ⚠️ **L'affermazione contraria sta nel
  rapporto di 2B-bis, l'ho scritta io ed e' stata ratificata in buona fede**: e' un fatto sullo
  strumento ricavato **guardando il risultato invece di leggere il codice**, cioe' un'altra istanza
  della specie del §11. **Il difetto vero era nella dichiarazione del dominio `allergeni`**, che
  elencava una fonte sola. Aggiunto il materiale di formazione, con perimetro chiuso e i due versi
  piantati. ⚠️ **La serie non si riscrive**: il 9,1 % resta il numero misurato con lo strumento di
  allora (E46), e il prossimo lotto dichiara la versione che usa.
- **2026-08-21** · **IL CSV SI RIFIUTA DI NASCERE MALFORMATO** · la guardia sta **in scrittura** e
  non in lettura, ed e' il punto: un controllo in lettura arriva sempre dopo il danno. Se una riga
  contiene il separatore, un a capo o una virgoletta nuda, **non si scrive niente** e sul disco
  resta il file vecchio e integro. ⚠️ **E a ogni chiusura il CSV dichiara righe e campi per riga
  con l'ora** (E44): 334 righe, 6 campi, nessun lotto fantasma.
- **2026-08-21** · **IL TEMA 3 E' STATO RIPACCHETTATO IN APERTURA, E LA SCRITTURA NON E' STATA
  APERTA** · tredici grezzi diventano **cinque pacchetti** lungo le cuciture documentali, non
  tematiche: il cruscotto KPI non e' un documento a se' — si intitola «riesame direzione» e
  dichiara «target definiti nel riesame del 12/03/2026» — ed e' il dato di ingresso del §5 del
  verbale, quindi sta con lui. ⚠️ **I pacchetti sono da 2-4 grezzi e non da 3-5, e il criterio e'
  E28: il CONTEGGIO DEI FATTI, non il numero dei file.** I grezzi di questo tema sono molto piu'
  densi di quelli dei temi 1 e 2 — il solo verbale porta **45 sezioni numerate** — e tre insieme
  avrebbero superato le quaranta note che impongono lo spezzamento comunque.
  ⚠️ **LA SCRITTURA DI 3A NON E' STATA APERTA, ed e' la PARTE 3 del prompt del gate ad averlo
  previsto**: la PARTE 2 e' stata una manutenzione piena — E48 con l'estensione di cantiere e i
  suoi collaudi, E49, la riverifica di trenta note, un arbitrato riaperto e richiuso, due righe
  di canone ribaltate, tre suite di collaudo — e **il prompt dice esplicitamente che il
  ripacchettamento e' esso stesso lavoro di apertura**. ⚠️ **Aprire il ciclo di 3A qui avrebbe
  significato cominciare un lotto sapendo di non chiuderlo nella stessa finestra**, e il ritmo
  della PARTE 4.4 chiede «un pacchetto per sessione, **chiusura piena**». **Un lotto aperto e non
  chiuso e' esattamente cio' che questo progetto evita.**
- **2026-08-21** · ⚠️ **L'ESTRAZIONE DI CANTIERE HA GIA' PAGATO SE' STESSA, PRIMA DI ESSERE USATA
  IN UN LOTTO** · aprendo il tema 3 per il conteggio dei fatti, lo strato del barrato ha mostrato
  che **il nono impegno della politica per la qualita' e' cancellato**: «perseguire la crescita
  del fatturato quale obiettivo primario dell'organizzazione», in un documento che dichiara la
  sicurezza alimentare. ⚠️ **Nel testo estratto e' indistinguibile dagli altri otto**, e senza lo
  strato sarebbe entrato nel vault come impegno vigente **senza che nessun controllo lo
  fermasse**. Riga **T107**. ⚠️ E `PRO-QA-08`, che e' fonte prescrittiva, ne porta **tre**, di cui
  due sono cancellazioni mute: riga **T108**.
- **2026-08-21** · **GATE DEL TEMA 3: DUE CONTRADDIZIONI AL PROMPT RATIFICATE, E NESSUN
  EMENDAMENTO NUOVO** · secondo gate consecutivo che non tocca il modo di scrivere le note: il
  registro resta a **E49**. ⚠️ **La ratifica piu' istruttiva e' quella su 2.4**: l'ordine di
  riformulare l'arbitrato CIP discendeva da B3 **com'era scritta**, e B3 era essa stessa un caso
  E49 — una conclusione entrata nel canone senza riaprire il file. Verificata la riga sulla fonte
  prima di eseguire, l'arbitrato ne e' uscito **confermato e piu' preciso**. ⚠️ **Se l'ordine
  fosse stato eseguito alla lettera, un errore del canone sarebbe entrato nel vault con la firma
  del gate** — cioe' con l'unica autorita' che avrebbe potuto fermarlo. Da qui **§4.44**, che il
  coordinatore ha dettato nel contenuto lasciando il numero a chi lo conta: le voci di §4
  arrivavano a **43**.
- **2026-08-21** · **IL «161 GREZZI» ERA UN'ETICHETTA IMPROPRIA, NON UN ERRORE DI CONTO** ·
  `prova_invarianza` enumerava `sources\` per intero, che porta i 160 grezzi **piu'
  `_index-sources.md`**. ⚠️ **La prova sui 160 e' identica prima e dopo**, ma un numero che cambia
  fra due run deve avere la spiegazione scritta accanto: lo script ora esclude i `.md` come fanno
  `conta_stato` e `verifica_matrice_lotti`, e **stampa nel report il passaggio 161 → 160 con il
  perche'**, cosi' il prossimo lettore non cerca un guasto che non c'e'.
- **2026-08-21** · **LA CIFRA DEL COLLAUDO VIAGGIA CON LA SUA COMPOSIZIONE** · «24 su 24»
  sommava due nature diverse: **difetti che devono scattare** e **controlli di NON-scatto**. Ora
  sono **18 e 9**, dichiarati separati e non sommati. ⚠️ **Dei quattro difetti piantati per E48,
  due sono scatti e due sono non-scatti** — ed e' proprio la struttura del fix, che insieme
  allenta e stringe. ⚠️ **E' lo stesso difetto del «7 difetti su 7» del gate 1C**: una
  contabilita' non sbagliata ma **muta**, che faceva credere a sette controlli che scattano.
- **2026-08-21** · **IL CONFRONTO RIGA PER RIGA DOPO UN FIX ALLA SUITE DIVENTA PRASSI SCRITTA** ·
  sta ora nel docstring del collaudo: dopo ogni modifica alla suite si rilancia il perimetro
  vault, si prende il report precedente da git e si confrontano gli esiti **riga per riga**.
  ⚠️ **Un esito che cambia dove nessuno ha toccato e' un difetto del fix** — e il caso e' il
  `break` del 21/08, che produsse quindici avvisi fantasma dove il totale li avrebbe raccontati
  come «lo strato nuovo vede di piu'».
- **2026-08-21** · **LA TERZA SPECIE HA IL SUO CRITERIO PRIMA DELL'ESPERIMENTO, NON DOPO** ·
  «l'affermazione che si smentisce dentro la nota stessa» era stata nominata e rimandata a
  «quando ricompare», e su questo il rapporto di 2B-bis **era rimasto un passo indietro** rispetto
  alla disciplina consolidata. ⚠️ **Il criterio precede l'esperimento, sempre**: diventa
  emendamento se ricompare al terzo giro di **3A** su note nate dal lotto, e se non ricompare la
  riga **non si chiude da sola**. Nessun promemoria a 3A.
- **2026-08-22** · **E50 ED E51: DUE CRITERI PRE-REGISTRATI SI SONO AVVERATI NELLO STESSO GIRO** ·
  al terzo giro di giudizio del lotto 3A entrambe le specie sorvegliate compaiono **su note nate
  dal lotto**, che era la condizione scritta in anticipo. ⚠️ **E50 — il conteggio che la fonte non
  enuncia**: il dato che ne ha deciso la forma e' che al terzo giro **le cinque cifre marcate
  `(contate)` erano tutte esatte e quelle sbagliate erano tutte non marcate**. La marca non
  certifica il numero: **dichiara che va ricontato**. ⚠️ **E51 — l'affermazione smentita dalla nota
  che la contiene**: nasce dal CORREGGERE, non dallo scrivere, ed e' per questo che sopravvive ai
  giri di giudizio che la producono. ⚠️ **La sua istanza piu' istruttiva non e' in una nota ma in
  un documento di metodo**: la motivazione del pacchetto 3A diceva che il cruscotto fosse «il dato
  di ingresso del riesame» **e** che «i suoi target vengono da li'».
- **2026-08-22** · ⚠️ **LA RICONCILIAZIONE VERTICALE NON SI DECIDE SULLA NATURA DEL DOCUMENTO, MA
  SU CHE COSA IL DOCUMENTO FA** · l'apertura di 3A dichiaro' che E37 non scattava perche' ne' il
  verbale ne' il cruscotto sono fonti prescrittive. **L'argomento era formalmente corretto e la
  conclusione sbagliata**: il verbale **cita un criterio prescrittivo e lo cambia** — il mock
  recall, che il manuale HACCP fissa a «≥ 99% entro 4 h» e il registro delle NC registra come
  dentro quel limite, il riesame lo dichiara **NON conforme** contro un obiettivo di 2 h.
  ⚠️ **Il costo e' misurabile**: e' la divergenza piu' pesante del lotto, e il lotto se l'era
  preclusa per iscritto.
- **2026-08-22** · **LE NOTE NATE DALLA REVISIONE HANNO UN TASSO DI DIFETTO MOLTO PIU' ALTO DI
  QUELLE NATE DAL CICLO** · il ri-giudizio dopo la revisione ha prodotto **43 rilievi e 16 errori**,
  piu' del terzo giro, e **quasi tutti sulle quattro note nate dalla revisione**. ⚠️ **Nascono da
  una divergenza gia' trovata da qualcun altro, si scrivono in fretta per non perderla, e non
  passano i tre giri che le altre hanno passato.** ⚠️ **Il caso peggiore**: la questione sul mock
  recall citava `PRO-QA-14` **cinque volte senza averlo letto**, e quel documento e' nel corpus.
  **E' un pattern nuovo e non ha ancora una regola.**
- **2026-08-22** · **LA GUARDIA DEL CSV HA RIFIUTATO LA PRIMA SCRITTURA LEGITTIMA CHE HA
  INCONTRATO** · vietava che un campo CONTENESSE il separatore, e sbagliava bersaglio: `csv.DictWriter`
  **quota da se'**, e il punto e virgola dentro un summary e' punteggiatura italiana, presente in
  decine di note. ⚠️ **Il difetto vero non era la forma del campo: era la PERDITA nel giro di andata
  e ritorno** — le tre righe rotte del 21/08 erano state scritte senza quoting da un percorso
  diverso. La guardia ora **scrive su un temporaneo, rilegge e confronta cella per cella**: e' un
  controllo **piu' forte**, perche' guarda l'effetto invece della forma.
- **2026-08-22** · **`qa_frontmatter` VIETAVA LA FORMA CHE E48 PRESCRIVE** · il campo
  `verifica: strutturale` era impossibile: il controllo lo rifiutava su qualunque nota senza
  `.jpg`. ⚠️ **Una regola in vigore che lo strumento rende inapplicabile e' una regola che non
  esiste**, e nessuno se n'era accorto perche' nessun lotto aveva ancora avuto un fatto letto da
  formula. Corretto a perimetro chiuso: `strutturale` e' ammesso **solo se almeno una fonte porta
  davvero uno strato di cantiere**.
- **2026-08-22** · **IL LOTTO 3A HA SFORATO IL PROPRIO PATTO DI APERTURA, E LO DICHIARA** ·
  conteggio dichiarato prima di scrivere **36 note**, scritte **38**, e **quattro** aggiunte dalla
  revisione: **42**, oltre la soglia dei 40 di E28. ⚠️ **Il patto diceva «se sfora si spezza in
  corsa» e non e' stato fatto**: le quattro oltre il tetto sono nate **dalla revisione**, a lotto
  gia' giudicato tre volte, e spezzare li' avrebbe significato rifare il ciclo su due lotti.
  ⚠️ **Ma la regola non distingue fra sforare SCRIVENDO e sforare per divergenze trovate DOPO**, e
  quella distinzione spetta al gate. Riga **T117**.
- **2026-08-22** · **E52, E53 ED E54 AL GATE DI 3A, E NESSUNO DEI TRE NASCE DA UN DIFETTO DELLE
  NOTE** · **E52** viene da **due consuntivi di pianificazione** (1B e 3A) e ratifica lo sforamento:
  le soglie governano la proiezione e la scrittura del ciclo, **le note post-revisione ne sono
  fuori** ma si dichiarano sempre come gruppo con esiti separati — ed e' quel numero che il gate
  guarda. **T117 si chiude qui.** ⚠️ **E53** viene da un'affermazione **del coordinatore**: il
  dominio si verifica **da script** in apertura, mai sulla parola di chi coordina. ⚠️ **E54** viene
  da un documento che stava nel corpus e che nessuno aveva aperto.
- **2026-08-22** · ⚠️ **L'ERRORE DEL §3 DI 3A E' DEL COORDINATORE, E LO DICE LUI** · la frase «E37
  non scatta su 3A — ne' il verbale ne' il cruscotto sono fonti prescrittive» stava nella PARTE 3.3
  del prompt del gate precedente. ⚠️ **E' il terzo caso in tre gate in cui un'affermazione del
  coordinatore era sbagliata nel merito** — B3, il multi-fonte, questo — **e il primo in cui
  l'esecutore non poteva contraddirla**: nei due precedenti c'era un **ordine da verificare**, qui
  c'era un'**esenzione**, che non si presenta come un ordine ma **come un lavoro che non c'e' da
  fare**. ⚠️ **Non esiste il gesto di "verificare un lavoro che non si deve fare"**, e per questo
  la risposta non poteva essere la diligenza: doveva essere uno script. E' E53.
- **2026-08-22** · **LA SERIE ACCETTA IL BUCO, DICHIARATO, E NON SI RETRO-MISURA** · misurare i due
  tassi di 3A **adesso** darebbe un tasso di produzione **gia' ripulito dalle correzioni della
  revisione**: un numero incomparabile con gli altri quattro, che misurano il lotto **come il ciclo
  l'ha prodotto**. ⚠️ **Un punto di serie misurato con un metro diverso e' peggio di un punto
  mancante**, perche' il punto mancante si vede. Il quinto punto e' «**NON MISURATO — dominio non
  dichiarato in apertura per errore del gate**», scritto cosi'.
- **2026-08-22** · **IL FALSO POSITIVO DELLE DOPPIE PADRONE E' CHIUSO, E LE CONDIZIONI SONO DUE** ·
  il gate di 2A lo lascio' rosso «finche' non avra' il suo turno», e il turno e' arrivato quando da
  **1 e' passato a 4** — tutti contro `kpi-indicatori-mensili-2026`, una tabella che porta
  **cinquanta decimali piccoli in una nota sola**. ⚠️ **Verificate le quattro coppie: tutte con
  ZERO fonti in comune, compresa quella originaria di 2A** — era un falso positivo dal principio.
  ⚠️ **Il fix aggiunge DUE condizioni, entrambe necessarie**: **fonte condivisa** — due note sono
  padrone dello stesso fatto solo se il fatto viene dallo stesso grezzo — e **valori identificanti**,
  almeno tre cifre significative, perche' «0,9» in questo archivio e' rumore di sfondo. ⚠️ **Nessuna
  delle due basta da sola**, e il collaudo lo esercita nei due versi a perimetro chiuso (§4.9):
  la doppia padrona vera scatta, i decimali di sfondo tacciono, e tacciono anche tre valori
  identificanti se le fonti sono disgiunte. **Vault da 122 a 118 errori: 115 grezzi + 3 hub, zero
  di merito.**
- **2026-08-22** · **LE SETTE `C` DELLA REVISIONE DEL LOTTO 3C, perche' non tornino al lotto
  dopo** · ⚠️ **C1 — il vendor rating in archivio contiene i tre fornitori che l'osservazione n. 5
  da' per mancanti, e NON e' una contraddizione**: `vendor_rating_fornitori_2026.xlsx` porta
  `F0031`, `F0044` e `F0090`, ma e' la valutazione **2026**, «approvato nel riesame della
  direzione del 12/03/2026», con la nota «peso alzato dopo l'audit» — **e' il vendor rating
  ESTESO che l'ente registra fra le evidenze del 02/04**. L'osservazione parla del **2025**.
  ⚠️ **C2 — la scheda tecnica dello snack riporta il certificato BRCGS e non viola la condizione
  2**: la condizione vieta il logo «sul prodotto o sul suo imballo primario destinato al
  consumatore finale», e **una scheda tecnica e' comunicazione business-to-business**. Nessun
  documento del corpus mostra il riferimento su una confezione. ⚠️ **C3 — «in scadenza il
  28/07/2026» della mail dell'11 marzo non e' un errore del lotto**: precede di un mese
  l'emissione dell'edizione 3, e `questione-scadenza-certificato-luglio-o-aprile` lo dichiara.
  ⚠️ **C4 — le `data_fatto` disomogenee fra 17/02 e 18/02 non sono un errore**: il rapporto non
  data i singoli rilievi, e giorno dell'ispezione e giorno della riunione di chiusura sono
  entrambi difendibili. ⚠️ **C5 — il bonifico CSQA compare due volte nell'estratto conto e non
  sono due pagamenti**: le righe 59 e 60 sono identiche **saldo progressivo compreso**
  (99.840,45), quindi e' una riga duplicata nel file. **Non toccare la quadratura.** ⚠️ **C6 —
  «Reclami 2025: n. 41 totali» del rapporto coincide col verbale di riesame §4.1**: e' una
  **conferma esterna di un dato interno**, e vale la pena saperlo. ⚠️ **C7 — non e' un errore di
  nota ma la tabella alias e' superata**: `alias_entita.md` avverte «il nome per esteso lo da'
  UNA fonte sola» per Chiara Vicentini, e il rapporto d'audit §2 la scrive per esteso. **Le
  fonti ora sono due, e l'avvertenza va aggiornata, non cancellata.**
- **2026-08-22** · ⚠️ **UNA RICERCA RISTRETTA SUL TEMA INVECE CHE SULL'OGGETTO PRODUCE
  UN'ASSENZA FALSA** · verificando la settima voce di T116 — «i neoassunti senza formazione
  allergeni sono quattro, **non tre**» — la prima ricerca chiedeva righe che nominassero
  **insieme** un numero, la formazione e gli allergeni: **non trovo' nulla**, e stavo per
  scrivere nella matrice che il «tre» non esisteva. ⚠️ **Esiste**: `NC-2026-015` del 28/01/2026
  dice «registro formazione MOD-HR-11 non aggiornato per **3 neoassunti Linea 2**» — **e la
  parola «allergeni» in quella riga non c'e'.** ⚠️ **Un'assenza dichiarata su una ricerca
  ristretta e' peggio di un dubbio**, perche' si presenta come un fatto verificato. E3 chiede la
  ricerca su TUTTO `sources\`; questo caso aggiunge che **anche i TERMINI vanno presi larghi**,
  e che si cerca **l'oggetto** — il registro, il modulo, la linea — non il tema.
- **2026-08-22** · **IL DOMINIO `certificazione` E' PROBABILMENTE DICHIARATO TROPPO LARGO, E IL
  NUMERO LO DICE** · il tasso di difetto di produzione di 3C e' **38,7 %**, il piu' alto della
  serie — ma **otto delle dodici note contate come scoperte citano un'altra fonte prescrittiva**
  che governa cio' di cui parlano davvero, e delle quattro restanti **tre hanno la prescrizione
  fuori dal corpus**. ⚠️ **Le ESPRESSIONI del dominio riconoscono le note che parlano
  dell'AUDIT, mentre le sue FONTI governano il TITOLO e gli obblighi verso l'ente**: e' l'errore
  che E36 corresse per le note, ricomparso nella dichiarazione di un dominio. ⚠️ **Il numero non
  e' stato aggiustato** (E41), e le quattro correzioni verticali vere del lotto — `MOD-PR-04`,
  `PRP-05`/`PRP-12`, `PRP-02`, `PRP-04` — **non lo toccano affatto**, perche' sono di un altro
  dominio. **Decide il gate.** T129.
- **2026-08-22** · **LOTTO 3C CHIUSO — E53 AL PRIMO IMPIEGO, E IL DOMINIO SI E' VERIFICATO IN
  VENTI SECONDI** · quattro grezzi dell'ente di certificazione, **38 note nuove**, QA di lotto a
  **zero errori**, vault da 118 a **114** — e i quattro in meno sono esattamente i quattro grezzi
  canonizzati. ⚠️ **La domanda che il lotto 3A non aveva potuto porsi ha avuto risposta prima di
  scrivere una riga**: `verifica_dominio.py` ha trovato **sette fonti prescrittive citate per
  sigla** dentro i grezzi, quattro citabili. **E53 funziona.**
- **2026-08-22** · ⚠️ **UNO SCRIPT CHE TACE NON E' UNO SCRIPT CHE ASSOLVE** · il primo
  `verifica_dominio.py` chiudeva `RX_SIGLA` con un **confine di parola**, e fra la `I` di
  `CPI_certificato_...` e l'underscore **quel confine non c'e'**, perche' l'underscore e' un
  carattere di parola: **ogni sigla del corpus veniva scartata in
  silenzio**, e restavano i soli riscontri deboli. ⚠️ **L'ha tradito un NUMERO — 28 fonti su 36
  «nominate» — non una rilettura del codice**: un elenco che dice quasi sempre di si' non e' una
  verifica. Da li' le **due classi di forza**, sigla e parola comune, che non si sommano mai.
- **2026-08-22** · **IL CERTIFICATO STAVA NELLA CARTELLA SBAGLIATA, E IL METODO LO DICEVA CON UN
  ESEMPIO SVOLTO SU QUEL FILE** · `metodo_03` §5, riga 3 della tabella: «Certificato BRCGS →
  `self\` → `self-certificazioni.md`. **Scartata `docs`**: in `docs` vanno i documenti che Aurora
  **scrive e applica**, non gli attestati che riceve». ⚠️ **L'errore l'ha trovato l'INDICE DELLA
  CARTELLA al momento di aggiornarlo**, non chi scriveva: la riga era sotto gli occhi allora, e
  non un minuto prima. ⚠️ **`self\` si apre con questo lotto**, dopo quattro mesi di vuoto.
- **2026-08-22** · ⚠️ **IL SUPERLATIVO SULL'ARCHIVIO: LA CLASSE D'ERRORE CHE HA CHIUSO IL CICLO
  DI GIUDIZIO** · i due soli rilievi del secondo giro avevano la stessa forma, la forma e' stata
  **nominata**, e al terzo giro — partito con l'istruzione di cercarla — ne sono usciti **altri
  tre**. ⚠️ **Il terzo giro ha trovato piu' rilievi del secondo, e non e' un peggioramento: e'
  che gli e' stato detto che cosa cercare.** ⚠️ **La regola NON e' «niente superlativi»**: dei
  quattordici verificati, **dieci reggono** — tutti quelli il cui soggetto e' **un documento
  citato**. **Il discrimine e' il SOGGETTO, non la forma**: un superlativo sull'archivio non e'
  verificabile da nessuna nota, perche' **nessuna nota ha l'archivio fra le proprie fonti**. E'
  la stessa specie di E36 un gradino piu' su. **Candidato emendamento, T142.**
- **2026-08-22** · **IL CRITERIO PRE-REGISTRATO SUL GRUPPO POST-REVISIONE E' STATO ESERCITATO E
  NON HA SCATTATO** · gruppo: **4 note, 0 rilievi al secondo giro**; ciclo: **51 note, 2
  rilievi**. **E54 e' bastato**, nessun mini-ciclo. ⚠️ **E' la prima volta in questo progetto che
  un criterio scritto PRIMA viene esercitato e si chiude senza discussione**, e funziona proprio
  perche' era stato scritto quando non si sapeva come sarebbe andata. ⚠️ **Ma il gruppo e'
  cresciuto dopo**: i ritrovamenti del terzo giro hanno prodotto **due note che non sono passate
  dal giudizio** — la regola d'arresto E26 ha la precedenza sul ri-giudizio. **T141.**
- **2026-08-22** · ⚠️ **DUE RITROVAMENTI HANNO CORRETTO COSE SCRITTE IN QUESTO STESSO LOTTO** ·
  il **«sedici giorni» NON era un refuso del vault**: `NC-2026-061` del registro interno dice
  «con **16 gg di ritardo**», quindi **Aurora conta sedici in due documenti** ed e' coerente con
  se' stessa; l'ente conta quindici perche' il termine e' suo e lo fissa al 18/03. **T126 e'
  stata riscritta dentro lo stesso lotto**, e dice che cosa diceva prima. ⚠️ **E il vendor
  rating**: i tre fornitori che l'audit da' per mancanti dal 2025 sono **classificati nel riesame
  di marzo**, con un indizio — «bobina fuori spessore 10/02/26» — che punta a una valutazione
  ritoccata dopo l'audit. **T140.**
- **2026-08-23** · **GATE DEL LOTTO 3C: APPROVATO, con E56, E57 ed E58** · tre emendamenti da un
  gate solo, per la seconda volta dopo 3A, e **nessuno dei tre da un difetto delle note**. **E56**
  — la dichiarazione del dominio e' una **coppia espressioni-fonti che si giustificano a
  vicenda**, e viene da **due consuntivi opposti**: 2B-bis troppo stretto (9,1 %), 3C troppo largo
  (38,7 %). **E57** — il **discrimine e' il soggetto** del superlativo, e viene dal pattern che
  E26 impone di nominare al terzo giro invece di inseguirlo. **E58** — **E26 ferma il ciclo, non
  la prima esposizione**, e viene da un debito che l'esecutore aveva dichiarato invece di lasciar
  passare (T141).
- **2026-08-23** · **IL 38,7 % DI 3C NON SI RIMISURA, e la scelta e' del gate** · la
  dichiarazione del dominio era sbagliata e la regola che la corregge esiste da oggi, ma **la
  serie fotografa le dichiarazioni come sono state fatte**: rimisurare darebbe sei punti tutti
  prodotti con la regola dell'ultimo gate, cioe' una serie che non puo' piu' mostrare il proprio
  miglioramento. **Il numero resta, con la riserva scritta accanto** (E46). **T129 chiusa.**
- **2026-08-23** · ⚠️ **IL GIUDIZIO DEDICATO DI E58, AL PRIMO IMPIEGO, HA TROVATO DIFETTI IN
  ENTRAMBE LE NOTE MAI GIUDICATE — due su due `afferma_oltre`** · ed e' il dato che giustifica la
  regola meglio di qualsiasi argomento: se il debito di T141 fosse stato formale, il giudizio
  sarebbe tornato pulito. **La prima** attribuiva all'ente conteggi e contenuti che la sua unica
  fonte non riporta, e il titolo diceva «le chiude in una settimana» mentre `NC-2026-049` va dal
  17/03 al 02/04; **la seconda** chiudeva con «l'archivio non scioglie» — **la classe di E57, in
  una nota nata due giorni prima che E57 esistesse** — e con un «nessuno lo ha contestato»
  mentre il rapporto d'audit registra «Azione correttiva proposta... Stato: APERTA».
  **Al secondo giro dedicato entrambe tornano `pulita`.**
- **2026-08-23** · ⚠️ **IL GIUDIZIO DEDICATO HA TIRATO FUORI UN DIFETTO PIU' GRANDE DI QUELLO
  CHE CERCAVA, E CORREGGE UNA RATIFICA DI QUESTO STESSO GATE** · `fatto-evidenze-audit-oltre-termine`
  era entrata nel perimetro solo per una correzione soppressiva (portava una fonte **due volte**
  in `fonti`); giudicata, e' tornata `afferma_oltre`. **Il verbale di riesame non porta ne'
  «sedici» ne' «16»** — verificato riga per riga — e **nessuna fonte dell'ente conta i giorni di
  ritardo**: ne' il rapporto, ne' le due mail. **Il solo conteggio SCRITTO in una fonte del corpus
  e' il «16 gg» di `NC-2026-061`, piu' il «(un giorno)» con cui il rapporto d'audit §6 misura il
  ritardo sul sollecito del 01/04.** ⚠️ **QUESTA VOCE SUPERA QUELLA DEL 22/08 qui sopra**, che
  diceva «Aurora conta sedici in due documenti»: il secondo documento non esiste. ⚠️ **Quindi
  «due contatori veri, di due titolari diversi» —
  la formula con cui il gate aveva ratificato T126 — e' sbagliata: il contatore e' UNO, e il
  quindici e' aritmetica del vault.** La sostanza regge (due termini, due conti possibili), la
  lettura no. **T126 alla terza stesura, e tutte e tre sono cadute sullo stesso punto: un
  conteggio attribuito a una fonte che non lo enuncia** — la classe di E49 e di E50. I due numeri
  ora portano la marca `(contati)`.
- **2026-08-23** · **IL CENSIMENTO DI E57 SI E' DOVUTO SPEZZARE IN DUE, e il primo numero era
  ingannevole** · `censimento_superlativi.py` al primo giro dava **42 note e 47 occorrenze**, e
  quel numero mescolava due regimi: accanto ai superlativi c'erano gli **esistenziali negativi**
  — «nessun documento dell'archivio riporta X» — che sono **assenze dichiarate** e le governano
  gia' **E3 ed E43**, con la ricerca su tutto `sources` e il suo artefatto. **Le due classi non si
  sommano**: **9 note di classe `superlativo`** (le sole scoperte) e **31 di classe `assenza`**.
  ⚠️ **Pubblicare 42 avrebbe ripetuto in piccolo l'errore del 38,7 %**: un numero vero con un
  nome che promette piu' di quanto misura. ⚠️ **E la classificazione dipendeva dall'ORDINE delle
  parole** finche' la finestra e' rimasta la frase intera: stretta a sessanta caratteri intorno al
  termine di perimetro, come E23. **T142.**
- **2026-08-23** · ⚠️ **QUINTO ORDINE DEL COORDINATORE CORRETTO DALLA VERIFICA, e stavolta e' un
  conteggio** · il prompt del gate chiede di riscrivere la §3 del passaggio di consegne con
  «undici lotti chiusi». **I lotti chiusi sono DIECI**: nove di canonizzazione — il pilota
  `l26130` piu' `1A`, `1B`, `1C`, `2A`, `2B`, `2B-bis`, `3A`, `3C` — piu' `R1`, il solo lotto di
  manutenzione. Contati da script sui marcatori `# CHIUSO` degli elenchi (nove file) piu' il
  pilota, che elenco non ne ha perche' e' anteriore alla matrice. ⚠️ **`riverifica_barrato` non
  e' un lotto chiuso**: e' un mini-perimetro dentro il gate di 2B-bis, e nessun documento lo
  dichiara altrimenti. ⚠️ **La §3 gia' portava lo stesso scarto prima di questo gate** —
  «sette lotti chiusi» sopra un elenco di otto — e la riscrittura lo chiude. **I precedenti sono
  quattro: B3, il multi-fonte, l'esenzione E37 di 3A, il «sedici giorni».**
- **2026-08-23** · ⚠️ **UN CONTROLLO BACATO TROVATO IN APERTURA DI 3B, E RIPARATO SUBITO (§4)** ·
  l'insieme dei lotti canonizzati di `verifica_dominio.py` era **una lista di nomi scritta a
  mano**, cioe' una copia di un fatto il cui padrone e' altrove, e si era disallineata in
  silenzio: portava `lotto_02b_autocontrollo_igiene`, **nome morto dal 20/08** quando il lotto 2B
  si spezzo' in apertura, e **non portava** `lotto_02b_autocontrollo_analitico`,
  `lotto_03c_certificazione_audit` ne' `r1_riconciliazione_verticale`, tutti CHIUSI.
  ⚠️ **Il costo, se non fosse stato visto**: in apertura di 3B lo script dichiarava
  `Certificato_BRCGS_Food_Issue9_Aurora_2026.pdf` **NON CITABILE** il giorno dopo che 3C lo aveva
  canonizzato — una fonte governante tenuta fuori dalla dichiarazione del dominio, cioe' il
  verso «troppo stretto» di E56 che in 2B-bis costo' un 9,1 % gonfiato. ⚠️ **E' la seconda
  volta che QUESTO script mente in silenzio**: la prima fu il `\b` in coda alla sigla, il
  22/08. **Il fix legge l'insieme dal marcatore `# CHIUSO` in testa all'elenco**, che e' lo
  stesso dato che `verifica_matrice_lotti.py` gia' pretende e non puo' invecchiare
  separatamente. ⚠️ **Il fix ALLENTA un controllo** — rende citabili fonti prima rifiutate —
  **quindi ha il suo difetto piantato** (§4.9): `collaudo_dominio_canonizzati.py`, cinque casi
  nei due versi, e il caso 2 e' il difetto piantato — un lotto senza `# CHIUSO` deve restare
  NON CITABILE. **Sei collaudi su sei alle 16:56.**
- **2026-08-23** · ⚠️ **E56 HA COLTO IL PROPRIO AUTORE AL PRIMO IMPIEGO** · il dominio
  `formazione` di 3B — **il primo dichiarato sotto la regola della coppia** — e' nato **troppo
  largo**, nello stesso verso di 3C: l'espressione `\bformazion` riconosceva **la parola**, e con
  essa la struttura del registro, chi lo estrae, la sua intestazione ripetuta e l'indicatore
  delle ore. Le fonti del dominio governano **l'obbligo di formare e registrare**, non un file e
  non un KPI. **Tasso col primo taglio: 63,6 % su 22.** ⚠️ **La prova e' per ESPRESSIONE, non
  per numero**: `\bformazion` da sola pescava **tutte e quattordici** le scoperte. Stretta la
  coppia, **36,4 % (8 su 22)**, ed e' il numero dichiarato. ⚠️ **Ci si e' fermati dopo UNA
  stretta**, e il residuo si dichiara: cinque delle otto le pesca `registro (?:della )?formazion`,
  che riconosce la MENZIONE del registro e non l'obbligo. **Continuare a restringere a numero
  visto sarebbe il trucco che E41 vieta, spostato di un piano** (§4.43). ⚠️ **E il tasso non e'
  stato rimisurato dopo aver corretto le tre lacune vere**: E41 lo vieta. **T148.**
- **2026-08-23** · **DUE CONTEGGI MIEI ERANO SBAGLIATI, E LI HA PRESI IL RICONTEGGIO, NON UNA
  RILETTURA** · il primo censimento del registro della formazione dava **101 righe di dato, 57
  dipendenti, 16 corsi, 7 enti**: includeva le **quattro righe di coda** e **un'intestazione
  ripetuta a meta' file**. I numeri veri sono **96 · 52 · 14 · 6**. ⚠️ **E la differenza cambiava
  una conclusione**: la divergenza con le «50 persone» della politica passava da **sette** a
  **due**, e con i tre nomi fuori perimetro si chiude quasi. ⚠️ **E' la specie di E50 applicata
  a chi scrive il metodo**, non alle note: un conteggio ottenuto guardando, non marcato, e
  sbagliato. **L'intestazione ripetuta e' diventata essa stessa una nota** — integrita' del file
  come contenuto (metodo_03 §5.5).
- **2026-08-23** · ⚠️ **UN SECONDO CONTROLLO BACATO, TROVATO DALLA REVISIONE COL CANONE E NON
  DALLA SUITE** · `qa_link_integrity.py` cercava i wikilink rotti chiamando `Nota.wikilink()`,
  che per contratto legge **il solo CORPO**: **il campo `related` restava fuori**, e `related`
  porta il rimando **spoke → hub**, cioe' il link piu' importante che una nota scriva.
  ⚠️ **Il buco non era teorico: il vault ne portava DUE e la QA dava 0 ERRORI.** Uno l'ha
  scritto il lotto 3B — `doc-scadenzario-formazione-2026` puntava a `entita-francesca-sartori`,
  **un nome proprio inventato**, lo stesso errore che la tabella alias registra per Vicentini —
  e **l'altro stava li' da un lotto precedente**. ⚠️ **E' la stessa specie di E32**: un
  controllo il cui perimetro non copre cio' che deve, quindi per §4 **un guasto, non un
  candidato**, riparato subito col difetto piantato (`collaudo_related_rotto.py`, 5 casi nei due
  versi). ⚠️ **Il punto che vale oltre il caso**: un nome che non esiste **non richiede
  giudizio, richiede un confronto con un elenco** — e a trovarlo e' stato un revisore, non uno
  script. **Due guasti di perimetro in un giorno solo**, contando quello di `verifica_dominio`.
- **2026-08-23** · ⚠️ **IL TERZO GIRO DI GIUDIZIO DI 3B HA CHIUSO IL CICLO NOMINANDO UN PATTERN
  NUOVO: LA CORREZIONE E' UNA SCRITTURA, E NESSUNO LA GIUDICA COME TALE** · giri a 18, 10 e 12
  rilievi su 31 note; **al terzo, almeno SETTE dei dodici cadono su frasi che al secondo non
  c'erano: le ha scritte la correzione**. Due forme: la prima gia' nota — l'intestazione rimasta
  indietro (E30, E51) — e la seconda nuova, **la frase scritta correggendo che afferma essa
  stessa oltre le fonti**. Quattro casi, e il peggiore: «la foto decisiva non compare in nessuno
  dei due elenchi» era la correzione di una frase vaga, **e il §6 della fonte la elenca** — la
  correzione ha reso FALSA una frase che prima era soltanto imprecisa. ⚠️ **E30, E39, E42 ed
  E51 guardano tutte all'affermazione VECCHIA e a dove sopravvive; nessuna guarda alla frase
  NUOVA.** Candidato emendamento al gate.
- **2026-08-23** · **LA REVISIONE COL CANONE DI 3B: 2 A, 13 B, 5 C, e una diagnosi che ribalta
  la domanda del passo 7** · non c'e' sovra-atomizzazione: c'e' **il contrario**. Un fatto con
  **tre padroni** (le righe di coda del registro, descritte in tre note) e **cinque righe del
  registro senza nessuna nota**, fra cui **un'addetta alla squadra di emergenza col primo
  soccorso scaduto da tre mesi** e l'unico «SUBITO» di tutto il file. ⚠️ **E la diagnosi vera**:
  *il lotto ha letto benissimo i due grezzi COME DOCUMENTI e quasi mai uno contro il vault* —
  **sette delle otto divergenze scrivibili nascono dall'accostamento col verbale di riesame**,
  canonizzato il giorno prima. **La riconciliazione orizzontale (E2) e' il passo che questo lotto
  ha fatto peggio**, e dentro un grezzo denso si conta invece di leggere.
- **2026-08-23** · ✅ **GATE DEL LOTTO 3B: E59, E60 ed E61, e il lotto e' approvato** · terza
  volta che tre emendamenti escono da un gate solo (dopo 3A e 3C), ma questi tre hanno una cosa
  in comune che i gruppi precedenti non avevano: ⚠️ **nessuno introduce una regola nuova sul
  CONTENUTO delle note. Tutti e tre danno un APPIGLIO MECCANICO a una regola gia' in vigore che
  veniva affidata alla diligenza** — e in tutti e tre i casi il consuntivo dice che la diligenza
  aveva gia' fallito. **E59**: E56 chiedeva la corrispondenza fra le due meta' del dominio, e la
  prima dichiarazione scritta sotto quella regola e' nata larga lo stesso — **tre dichiarazioni
  su tre sbagliate**, quindi la dichiarazione si COLLAUDA da script prima della misura. **E60**:
  E2 e' la regola piu' redditizia del metodo e per **due lotti di fila** l'ha eseguita il
  revisore invece del ciclo, quindi artefatto d'apertura (grandezze condivise, da script) e passo
  pre-giudizio (rilettura contro le note vicine del vault). **E61**: E30, E39, E42 ed E51
  guardano tutte all'affermazione vecchia, **nessuna alla frase nuova che la correzione scrive**.
- **2026-08-23** · **LA VIGILANZA DELLA CORREZIONE-SCRITTURA SI CHIUDE PRIMA DELLA SCADENZA, ED
  E' UNA DECISIONE CHE VA MOTIVATA PERCHE' NON DIVENTI UN PRECEDENTE LASCO** · il criterio
  pre-registrato chiedeva la ricomparsa al terzo giro del lotto **successivo**; il gate lo assorbe
  in E61 senza aspettare. ⚠️ **Non e' §4.43**, che vieta di rileggere un criterio **a esito
  visto**: l'esperimento **non era partito**, e si sta chiudendo il criterio prima del fischio
  d'inizio, non dopo il gol. ⚠️ **E le osservazioni erano GIA' DUE quando il criterio fu
  scritto**: i tre rilievi introdotti correggendo nel completamento di **2B** sono la stessa
  famiglia dei sette di **3B**, e la sessione che scrisse il criterio non li aveva davanti.
  **Con due consuntivi il conteggio di E28 e' completo**: la vigilanza era ridondante rispetto
  alla storia.
- **2026-08-23** · 🚨 **IL CENSIMENTO DELLE SUPERFICI HA TROVATO IL BUCO PIU' VECCHIO DELLA
  SUITE, E NON ERA `related`: `qa_provenance` NON GUARDAVA `title` E `summary`** · un numero, una
  data o un codice inventati nell'intestazione passavano la QA a **verde**. ⚠️ **Cinque
  emendamenti dichiarano l'intestazione portante** — E18, E30, E39, E42, E51 — e **nessuno dei
  cinque aveva uno strato deterministico dietro**; e' la superficie su cui il progetto trova piu'
  difetti di ogni altra (nel lotto 1C, al terzo giro, **sei rilievi su sette** stavano li' col
  corpo gia' corretto). ⚠️ **La ragione per cui e' durato tanto e' la sua FORMA, ed e' la parte
  che diventa giurisprudenza**: `qa_provenance` e `metodo_03` §7.1 **concordavano** — entrambi
  dicevano «dal corpo della nota». **Non c'era nessuna divergenza fra codice e manuale da
  trovare**: la lacuna stava fra due dichiarazioni del progetto che nessuno aveva mai messo una
  accanto all'altra. **Un difetto che non e' una contraddizione non si trova rileggendo: si
  trova facendo l'elenco.** ⚠️ **Nel vault ce n'erano QUATTORDICI**, quasi tutti della stessa
  specie — **date scritte con l'anno dove la fonte non lo scrive**: `05/05/2026` nel titolo,
  `5/5` nel quaderno OCR che ne e' la fonte, col **corpo corretto** nella grafia della fonte
  (E24). Riparato, con debito §4.35 (**T158**) e difetto piantato in `collaudo_intestazione.py`.
  ⚠️ **E il fix ha tolto DUE falsi positivi**: due avvisi «rumore nel payload» stavano su fonti
  che agganciano un'affermazione della nota — che vive nel summary. **Non ha allargato niente:
  ha visto di piu'.**
- **2026-08-23** · **IL CENSIMENTO DELLE COPIE DI STATO: DUE SPECIE, DUE CURE OPPOSTE** · passata
  su tutti i **38** script di `06_operativo\` e `qa\`. Lo **stato derivabile** (elenchi,
  conteggi, percorsi) non si controlla: **si cancella**, e lo strumento legge dal padrone — tre
  sostituzioni, piu' le due riparate il 22-23/08. I **vocabolari chiusi del manuale** (aree,
  prefissi, `type`, cartelle) **non potevano diventare una lettura a runtime**: far leggere a
  `qa_comune` un manuale in prosa manderebbe rossa tutta la suite al primo titolo riformattato, e
  §4.35 dice gia' che il difetto prevedibile e' che il controllo venga **disattivato**. Quindi la
  copia resta dove serve e **`verifica_copie_stato.py` la confronta col padrone**. ⚠️ **La copia
  peggiore era la piu' silenziosa**: `ricalibra_budget.py` teneva due tabelle a mano **ferme al
  19/08** — diceva quattro lotti chiusi, cinque lotti dopo — **e nessuno lo lanciava**. E' la
  forma peggiore di §4.47: uno strumento che non mente mai a voce alta perche' non parla mai.
- **2026-08-23** · ⚠️ **IL CONTEGGIO DEI LOTTI CHIUSI PASSA DA UN'ARITMETICA A UNO SCRIPT, E IL
  PRIMO RICONOSCIMENTO DEL MARCATORE ERA GIA' SBAGLIATO** · il numero viveva a mano nei prompt
  del coordinatore ed e' uscito **«undici» dove i marcatori `# CHIUSO` erano DIECI** (9 di
  canonizzazione + R1; la fetta pilota non ha marcatore e non e' della matrice). Ora lo stampa
  `verifica_matrice_lotti.py` e la §3 lo **incolla**. ⚠️ **E il riconoscimento scritto lo stesso
  giorno faceva `startswith` su una riga di prosa**: il lotto **1B**, di canonizzazione,
  risultava di manutenzione per una riga che va a capo su «*manutenzione* mai firmato». **Un
  conteggio nato per togliere l'aritmetica dalle mani di qualcuno ha sbagliato alla prima
  misura, e per la stessa ragione che stava riparando** — un riscontro **debole** preso per
  forte (E56). Difetti piantati nei due versi in `collaudo_lotti_chiusi.py`.
- **2026-08-23** · ⛔ **SESTA CORREZIONE AL COORDINATORE: I GREZZI COL BARRATO SONO UNDICI, NON
  TRE** · lo scrivono il §2.6 del prompt di questo gate e la riga **T157**. Misurato con
  `estrazione_cantiere.testo_cantiere` su tutti i 160 grezzi: **11 grezzi, 40 passaggi, 6 gia'
  canonizzati**. ⚠️ **I «tre» erano i tre che la revisione aveva davanti** — la politica, la
  scheda allergeni, il contratto frigo — ed e' **esattamente la specie che E47 descrive e che E57
  ha appena normato**: un'affermazione il cui soggetto e' **l'archivio**, verificata sul
  sottoinsieme che l'ha suggerita. La riga del canone porta il numero **contato** (E49), e T157
  si chiude **con l'errata dentro**. ⚠️ **Seconda volta in due gate che un numero composto a mano
  dal coordinatore arriva sbagliato, e sono gli unici due numeri di questo gate che nessuno
  script produceva.**
- **2026-08-24** · ✅ **LOTTO 3D CHIUSO — i reclami: 3 grezzi, 35 note di contenuto, QA di lotto
  a ZERO ERRORI** · e' il primo lotto che gira con E59, E60 ed E61 in vigore. ⚠️ **Due dei tre
  strumenti che quelle regole prescrivono NON esistevano**, e sono stati costruiti in apertura:
  `grandezze_condivise.py` (l'artefatto d'apertura di E2 che E60 impone) e `collauda_dominio.py`
  (la prova di E59). **Una regola che prescrive uno strumento inesistente e' una regola che si
  applica a mano** — cioe' esattamente cio' che quel gate stava correggendo.
- **2026-08-24** · ⚠️ **IL LOTTO 3D SI E' SPEZZATO PER LA SOGLIA DI E37, NON PER QUELLA DI E28**
  · la riconciliazione verticale arretrata sul dominio `reclami` ha riaperto **65 note** contro
  le **35** che il ciclo ha prodotto: **le riaperte superano le nuove**, e la regola impone di
  dichiararlo e di spezzare in canonizzazione piu' manutenzione. Nasce **R2**, e il suo perimetro
  **si rigenera all'apertura**: con `PRO-QA-08` ormai canonizzata, l'insieme sara' diverso, e la
  differenza misura quanto 3D ha gia' sanato. ⚠️ **E' la prima volta che quella soglia scatta**:
  le altre volte il lotto si e' spezzato sulla proiezione delle note nuove.
- **2026-08-24** · ⚠️ **E59 AL PRIMO IMPIEGO HA TROVATO UN DIFETTO DEL PROPRIO COLLAUDO, NON
  DEL DOMINIO** · la prima stesura di `collauda_dominio.py` respingeva **sei espressioni su
  nove**, fra cui la sigla del modulo che la procedura istituisce — l'espressione piu' specifica
  che quel dominio possa avere. ⚠️ **La ragione e' strutturale: la fonte del dominio la stava
  portando quel lotto**, quindi nessuna nota poteva citarla e la colonna «dentro» era zero **per
  costruzione**. ⚠️ **E c'era di peggio**: contare come «governata altrove» una nota che parla
  di reclami citando il manuale HACCP e' **il contrario del vero** — quella nota e' **scoperta**,
  cioe' cio' che il tasso di E41 esiste per contare. Applicata cosi', la prova avrebbe respinto
  le espressioni giuste e lasciato passare le sbagliate. **Lo strumento e' stato riscritto in due
  prove che non si sommano**: la **specificita'** (sempre applicabile, ed e' quella che 3B ha
  fatto a mano) e il **dentro/fuori** (applicabile solo se la fonte del dominio e' gia' citata).
  ⚠️ **E una sospetta non si scarica cambiando la soglia**: si scarica con `--motivata`, che la
  registra in chiaro, **e con una ragione scritta nel rapporto**.
- **2026-08-24** · ⚠️ **LA META' DI E59 CHE IN APERTURA NON SI PUO' FARE, ALLA CHIUSURA SI FA** ·
  a lotto chiuso `PRO-QA-08` e' citata da 22 note, la prova B diventa applicabile, e **il dominio
  la supera su tutte e nove le espressioni** — la piu' larga a 0,39 contro una soglia di 0,50.
  ⚠️ **E `campione reso`, che in apertura non riconosceva NESSUNA nota, alla chiusura ne
  riconosce cinque e tutte e cinque citano il dominio**: quota fuori **0,00**. **Non e' un
  emendamento che il lotto propone: e' un'osservazione con un consuntivo**, per il gate.
- **2026-08-24** · ⛔ **IL DOCUMENTO CHE L'ARCHIVIO DICHIARAVA DI NON AVERE ERA IN `sources\`
  DALL'INIZIO — E3 PAGATO PER LA QUINTA VOLTA, CON UNA FORMA NUOVA** ·
  `questione-data-apertura-rec-2026-011`, scritta il 19/08, elencava fra le cose che sarebbero
  servite «la mail automatica di notifica della segnalazione, **che l'archivio non contiene**».
  L'archivio la contiene, ed e' il primo grezzo del lotto 3D. ⚠️ **Il grezzo esisteva fin
  dall'inizio, in un lotto non ancora canonizzato — e E3 chiede la ricerca su TUTTO `sources\`,
  non sui lotti chiusi.** ⚠️ **E il controllo di E43 non poteva prenderla**: quella nota non usa
  la formula di attestazione, dichiara l'assenza dentro un elenco di «cosa servirebbe per
  chiuderla». **La superficie in cui un'assenza si nasconde e' piu' larga della formula che la
  dichiara**, ed e' la stessa scoperta che il gate 3B ha fatto sull'intestazione, un piano piu'
  in la'. **T161**.
- **2026-08-24** · ⛔ **IL DOCUMENTO ARRIVA E LA DIVERGENZA SI ALLARGA: TRE ORE PER LO STESSO
  ARRIVO** · la notifica del form dichiara `2026-05-12 18:23:47 CEST` e la riunione concorda; **ma
  la prima mail interna sul reclamo, delle 14:33 dello stesso pomeriggio, dice che era arrivato
  ALLE 13:05 dal form**. ⚠️ **La difficolta' non e' quale ora sia giusta: e' che la mail e'
  ANTERIORE alla notifica** — descrive la segnalante, il prodotto, il lotto letto dalla foto e il
  punto vendita quasi quattro ore prima che il messaggio esistesse. **T5 non si chiude: si
  allarga**, e ha una padrona.
- **2026-08-24** · ⛔ **TRE QUALIFICAZIONI PER LO STESSO RECLAMO, E FORSE DUE SCALE DIVERSE** ·
  la scheda dice **Classe 2**, il registro degli indicatori **CRITICO**, la prima mail interna
  **GRAVE**. ⚠️ **Ma la scoperta non e' la terza qualificazione: e' che la scheda NON dichiara
  di applicare `PRO-QA-08`** — attribuisce la scala al **par. 4 di un'altra procedura**, e lo
  scrive due volte. **Non e' detto che le fonti stiano leggendo la stessa scala in due modi:
  potrebbero applicarne due diverse.** ⚠️ **L'ha trovata la TERZA DOMANDA del prompt di
  giudizio**, quella sulla lacuna di copertura che il metodo descrive come segnale «poco piu' di
  una volta su due». Divieto 9-bis rispettato: il vault registra che la scheda cita quella
  procedura e **non dice nulla di cio' che contiene**. **T159**, obbligo esplicito per 3E.
- **2026-08-24** · ⚠️ **IL RILIEVO CHE NESSUN ALTRO STRATO PUO' VEDERE: IL NOME DEL FILE** · al
  primo giro un giudice ha preso il **titolo** di una nota che affermava «rincorse **a voce**»,
  dove la fonte dice solo «finora l'ho rincorsa io»; la correzione ha sistemato titolo, summary
  e corpo. ⚠️ **Al secondo giro lo stesso rilievo e' tornato, e sul NOME DEL FILE.** ⚠️ **E'
  E30 un gradino piu' in la': lo slug si scrive PRIMA del titolo e non si corregge MAI**, ed e'
  l'unica superficie che nessuna rilettura del testo tocca. **La QA non la guarda** — non e'
  un'affermazione per nessun controllo — **ma il giudice la vede**, perche' il nome della nota e'
  la prima cosa che il pacchetto gli mette davanti. Nota rinominata.
- **2026-08-24** · ⚠️ **E61 IN FLAGRANZA TRE VOLTE, E DUE DENTRO UNA RICONCILIAZIONE: QUANDO
  SI AGGIUNGE UNA FONTE, VA RILETTA ANCHE LA FRASE VECCHIA** · E61 dice di rileggere la frase
  **nuova** che la correzione scrive. ⚠️ **Due casi di questo lotto mostrano il verso
  opposto**: aggiungere una fonte a `questione-data-apertura-rec-2026-011` ha reso **falsa** una
  frase che c'era gia' («il termine di 48 ore non e' di nessuna delle fonti di questa nota» — e
  la fonte aggiunta lo contiene), e la riconciliazione di E60 su
  `questione-nc-interne-registrate-su-mod-qa-31` ha attribuito un contenuto al manuale HACCP, che
  **quella nota non ha fra le fonti** (la gemella si', e li' la stessa frase regge). **Una
  correzione che AGGIUNGE UNA FONTE cambia il perimetro di verita' della nota intera**, e le
  frasi che c'erano prima vanno rilette contro il perimetro nuovo. Osservazione per il gate.
- **2026-08-24** · ⚠️ **E39: LA CAUTELA E' STATA PROPAGATA DENTRO LA NOTA E NON FRA LE NOTE** ·
  il primo giro ha corretto «rincorse a voce» in una nota; **la stessa affermazione stava nella
  nota sorella `doc-indicatori-reclami`, e li' e' rimasta** — l'ha presa il secondo giro. E39
  chiede tutte le altre occorrenze **dell'affermazione**, ed E42 di cercarle **nello stesso
  turno**: la ricerca e' stata fatta **dentro** la nota e non **fra** le note.
