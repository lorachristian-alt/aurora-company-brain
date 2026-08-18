# Rapporto del lotto 1A — Linea 1: il turno, i CCP e la confezionatrice

> **Cos'è** · Il rapporto di chiusura del primo lotto della canonizzazione integrale, da
> portare al titolare per l'approvazione (metodo_03 §9.5, passo 7).
> **Quando si usa** · Una volta, alla chiusura di questo lotto. Poi resta come storia.
> **Cosa non contiene** · Nessuna regola: le regole stanno in `metodo_03`, il piano in
> `matrice_lotti_corpus_v1.md`, lo stato in `stato_canonizzazione.md`.

---

## 1. Il lotto, in una tabella

| | |
|---|---|
| Grezzi del lotto | **7** (ricontati da `inventario_grezzi.py`: 7 righe, 7 nomi distinti, 0 mancanti, 0 già coperti, 0 doppi) |
| Budget dichiarato | **34-42** note di contenuto |
| Note di contenuto prodotte | **42** — dentro il budget, al suo estremo alto |
| Note esistenti estese | **18**: 6 note-padrone del pilota, 4 schede entità, 3 hub d'area, 4 `_index`, più la nota-strumento della link integrity per l'emendamento E20 |
| Note nel vault, prima → dopo | **63 → 105** (contate da `qa_all.py`) |
| Note di contenuto nel vault, prima → dopo | **46 → 88** |
| Densità del lotto | **6,0 note di contenuto per grezzo**, contro 2,1 del pilota |
| QA di lotto | **0 ERRORI, 31 AVVISI** — verde, dopo due giri di giudizio e uno di revisione |
| Collaudo della suite, rieseguito | 5 difetti piantati su 5 trovati, 0 falsi positivi |

### Le 42 note nuove, per cartella

| Cartella | Note nuove | Cosa sono |
|---|---|---|
| `areas\` | 24 | i fatti del turno, le manutenzioni arretrate, le prove di stabilità, 5 questioni aperte |
| `data\` | 7 | quattro serie contate e tre divergenze fra valori |
| `entities\` | 5 | l'hub della Linea 1, tre macchine, il capoturno, il costruttore della confezionatrice |
| `docs\` | 3 | il modulo del CCP3, la scheda tecnica del prodotto, il limite di ossigeno residuo |
| `concepts\` | 3 | punto critico di controllo, atmosfera protettiva, shelf life |

## 2. I tre conflitti tracciati dal gate S2: tutti e tre chiusi

Il lotto era obbligato perché portava dentro `appunti_capoturno_quaderno_linea1_OCR.txt`,
la gamba mancante di tre conflitti. **Tutti e tre sono stati ripresi, e nessuno dei tre si
risolve**: si chiudono come *aperti dichiarati*, che è l'esito corretto quando l'archivio
non dà un vincitore.

| Conflitto | Cosa ha portato il quaderno | Esito |
|---|---|---|
| **MOD-QA-07, verifiche CCP3 del 10/05** | «saltata verifica ore 15 e 16 x fermo!!!» contro le sei righe della trascrizione | Nuova nota `questione-verifiche-ccp3-10-05-tre-versioni`. ⚠️ **La scoperta più grave del lotto**: rileggendo a occhio la scansione del modulo originale, le righe delle 16:00 e delle 17:00 sono **barrate e vuote**, mentre la trascrizione destinata alla cartella evidenze per il cliente le registra **eseguite e conformi**. I due documenti non concordano nemmeno su chi fosse l'operatore |
| **Pezzi del turno L26130-L1-T2** | «0450: solo 4.1OO pz oggi + quelo di T1» | `questione-pezzi-prodotti-l26130` estesa a tre fonti. Il terzo numero **non è una terza stima**: è l'unica delle tre fonti che **dichiara il proprio perimetro**, ed è questo il suo contributo |
| **Arrivo dell'officina al fermo** | «ariva ore 15.5O circa» contro le 15:25 del rapporto | Nuova nota `questione-arrivo-officina-fermo-pkm-450`. Lo scarto non cambia la durata del fermo: cambia il **tempo di risposta della manutenzione**, cioè il dato con cui si giudica il presidio della domenica |

## 3. Cosa il lotto ha trovato che nessuno cercava

Sono i fatti che il quaderno, il manuale e il piano di manutenzione portano e che **nessun
documento del pilota conteneva**. Li elenco perché sono la ragione per cui questo lotto
valeva il doppio del budget previsto.

1. **La manutenzione della guarnizione della valvola azoto era scaduta dal 12/01/2026**, e
   il guasto è del 10/05: quattro mesi meno due giorni, con la voce ferma per mancanza del
   ricambio. Nessuna fonte dichiara un nesso causale, e la nota non lo afferma.
2. **Il manuale del costruttore avverte che una guarnizione non originale può frammentarsi
   nella sede** e non garantisce l'idoneità al contatto con alimenti. Era in azienda dal
   2018. Non prova nulla sul frammento del reclamo — prova che il rischio era documentato.
3. **La revisione della valvola modulante del vapore del pastorizzatore era rimandata due
   volte**, con annotate «oscillazioni in regolazione», scaduta dal 10/04. Un mese dopo il
   capoturno scrive che il `PT-104` «ballava».
4. **Il registro cartaceo del CCP2 del 10/05 lo compilava un neoassunto senza corso HACCP**,
   formato dal capoturno in dieci minuti. Il corso lo ha fatto il giorno dopo.
5. **Il prodotto uscito durante la deviazione — 800-900 pezzi stimati — non risulta
   segregato**, e la domanda del capoturno («ANDAVA MESO DA PARTE ????») è rimasta senza
   risposta in archivio.
6. **Le prove di shelf life misurano il difetto del lotto del reclamo**: ossigeno residuo da
   0,9 % a 14,0 % in novanta giorni contro 1,9 % del lotto sano, e una prova in vasca con
   blu di metilene che trova **3 microperdite su 10 buste** della saldatura longitudinale.
7. **Le seconde firme del CCP3 passano dall'81 % di mancanti al 19 %** il giorno dopo
   l'incidente: la misura correttiva della non conformità di audit di febbraio comincia a
   essere applicata l'11 maggio, non prima.
8. **Sedici voci di manutenzione arretrate su 112**, di cui tre rinviate per iscritto «per
   produzione Tosano».
9. **La Linea 1 ha prodotto su tre turni una domenica che il piano non le assegnava**, e
   l'archivio non dice chi l'abbia deciso.

## 4. Le divergenze di categoria B trovate in questo lotto

Sono divergenze reali del corpus che il canone non elencava. Per ciascuna: entrambe le
gambe con locator, nessun vincitore forzato dove il metodo non lo dà, e una riga da
aggiungere al canone in sezione datata.

| # | Cosa diverge | Trattamento |
|---|---|---|
| B1 | Verifiche CCP3 del 10/05: modulo scansionato, sua trascrizione e quaderno | nota nuova, `stato: aperto` |
| B2 | Arrivo dell'officina: 15:25 contro «ariva ore 15.5O circa» | nota nuova, `stato: aperto` |
| B3 | Limite di O2 residuo: max 1,0 % in scheda tecnica contro «lim 2%» in linea | nota nuova, `stato: aperto` |
| B4 | aw e umidità di AF-SN-0450: scheda tecnica **e laboratorio accreditato** contro il file delle prove di stabilità | nota nuova, `stato: aperto` |
| B5 | Materiale della guarnizione **originale**: PTFE, FKM ed EPDM in tre documenti | questione del pilota **estesa** |
| B6 | Codice del ricambio della valvola: da due sigle a **quattro**, due dal costruttore | questione del pilota **estesa** |
| B7 | Linea 1 in produzione domenica 10/05 fuori dal piano | nota nuova, `stato: aperto` |
| B8 | Velocità nominali delle linee: 1.250 pz/h a piano contro 1.800 ricavabili dall'OEE | nota nuova, `stato: aperto` |
| B9 | Tassello inox non rilevato al primo colpo: datato 05/05 dal modulo, 07/05 dal quaderno | nota nuova, `stato: aperto` |
| B10 | TMC proposto a sei mesi contro i 45 giorni della scheda tecnica in vigore | registrata dentro `kpi-shelf-life-af-sn-0450`: è una proposta contro una specifica, non due documenti che si contraddicono |
| B11 | Il riepilogo interno della scheda di manutenzione non quadra con le righe che riepiloga | nota nuova `fatto-riepilogo-manutenzione-non-quadra`: incoerenza **intra-file**, quindi `atomica` e non `conflitto` (§2.4) |

⚠️ **Su B5 e B6 si è estesa la questione esistente invece di aprirne una nuova**: «un fatto,
un padrone» vale anche per le questioni, e le gambe nuove riguardano lo stesso oggetto.

## 5. La verifica di assenza più importante del lotto

`questione-codice-allarme-pkm-450` aspettava dal pilota la tabella allarmi della macchina.
**Non c'è.** La ricerca è stata fatta su **tutti e 160 i file del manifest v1.1** con
l'estrattore di testo congelato: due sole occorrenze in tutto l'archivio, e nessuna delle
due è una tabella. L'estratto del manuale dichiara nel colophon che l'elenco allarmi
completo sta nel manuale integrale, 184 pagine, che in archivio non esiste.

Il manuale porta invece una **terza codifica**: `A031` per la pressione gas, che descrive
esattamente il guasto del 10/05 e non coincide né con `E-214 GAS` della foto né con
`AL-217` del rapporto.

## 6. Gli avvisi della QA

Trentuno, tutti motivati: l'elenco per famiglia sta al §11, dopo i tre passaggi di
revisione, perché è su quei numeri finali che vanno letti. ⚠️ La prima stesura del §11 ne
dichiarava 32 con famiglie che sommavano 46: l'errata è dichiarata lì.

## 7. Il perimetro vault, che non era chiesto ma è cambiato

Il lotto si chiude con `--perimetro lotto` verde, come prescrive il metodo. Ma vale la pena
registrare dove sta il **perimetro vault**, perché è migliorato per la prima volta da quando
esiste:

| Controllo | Errori sul vault |
|---|---|
| `qa_frontmatter` | **0** |
| `qa_link_integrity` | **0** |
| `qa_provenance` | **0** |
| `qa_copertura` | 135 — **131 grezzi non ancora canonizzati e 4 aree senza hub** |

Cioè: **tutti gli errori residui del vault sono la sua incompletezza**, e nessuno è un
difetto delle note che esistono. Tre controlli su quattro sono verdi su tutto.

## 8. Candidati emendamento e chiarimento

1. **Regola di apertura del lotto** (già scritta nella matrice, da portare in `metodo_03`
   §9): i fatti si contano **prima** di scrivere, e oltre il +25 % sul budget il lotto si
   spezza. Nasce dal fatto che questo lotto, non spezzato, sarebbe valso ~62 note contro un
   budget di 26-36.
2. **La data di verifica di un'assenza è un metadato della nota, non un fatto dell'archivio**
   (chiarimento a §10.12-bis). §10.12-bis chiede di datare l'assenza; §7.1 segnala come
   errore ogni data non presente nelle fonti. Le due regole si scontrano per costruzione. La
   soluzione adottata — e proposta come chiarimento — è che il corpo **rimandi a `data_nota`**
   invece di riscrivere la data: un fatto, un padrone, applicato alla data della nota stessa.
3. **I numeri contati vogliono il marcatore accanto al numero, non la spiegazione nel
   paragrafo** (chiarimento a §5.4 / E7). Lo strato deterministico esenta un valore derivato
   solo se trova `(contat…)`, `(calcolat…)`, `(derivat…)` entro 60 caratteri, oppure una
   formula `a + b = c`. Le divisioni e le medie non sono riconosciute come formule: vanno
   marcate. Vale la pena scriverlo nel manuale, perché è la differenza fra una nota che passa
   e una che fallisce per una regola che nessuno aveva enunciato.
4. **Le date e gli orari si riportano nella grafia della fonte.** Un file che scrive
   `20-mar-26`, `2026-01-12` e `20/04/26` nella stessa colonna non si uniforma: uniformare è
   correggere il grezzo. Discende da §10.3 e conviene renderlo esplicito.

## 9. Cosa resta aperto per scelta

- Le **31 righe della tabella di tracciamento** in `matrice_lotti_corpus_v1.md`, di cui
  **9 chiuse come *aperte dichiarate*** in questo lotto e le altre in attesa della gamba
  mancante.
- **T17 e T18** hanno la gamba in 1A ma la nota nascerà in 1B: `metodo_03` §2.4 pretende
  almeno due file diversi per una nota `conflitto`, e in 1A ce n'è uno solo.
- Le **quattro aree senza hub** — amministrazione, risorse umane, sicurezza-ambiente,
  ricerca-sviluppo — che nasceranno con i lotti 6, 7, 8 e 9.

---

## 10. Giudizio di provenance, revisione col canone, ri-giudizio

Tre passaggi di controllo indipendenti, tutti a contesto pulito e tutti su note che non
avevano scritto loro. **Sedici rilievi in due giri di giudizio, dieci dal revisore.**

| Passaggio | Note viste | Esito |
|---|---|---|
| Giudizio di provenance, primo giro | 46 | 38 pulite · **8 «afferma oltre le fonti»** · 0 fonti inutili |
| Revisione indipendente col canone | 57 + hub e `_index` | **10 A · 10 B · 11 C · 0 sovra-atomizzazione** su 18 note campionate |
| Giudizio di provenance, secondo giro (E9) | 48 | 40 pulite · **8 «afferma oltre le fonti»** · 0 fonti inutili |

**Tutti i rilievi sono stati verificati sui grezzi prima di essere accolti**, e tutti sono
risultati fondati. Nessuno è stato archiviato come falso allarme del giudice.

### I tre rilievi che valevano da soli i tre passaggi

1. **Una fuga di canone.** Una nota scriveva «il canone del progetto registra che listino e
   accordo quadro ne dichiarano 12»: il canone nominato dentro il vault, e un valore che
   nessuna fonte citata contiene. Cancellata, insieme alla versione attenuata in una seconda
   nota. **È la seconda fuga in due lotti**, con lo stesso movente: anticipare una divergenza
   che non ha ancora entrambe le gambe.
2. **Una dichiarazione di assenza falsa.** La nota sul limite dell'ossigeno residuo affermava
   che il valore del 2 % «non compare in nessun documento in archivio». Compare due volte,
   nel registro delle non conformità, e una delle due voci è del 4 maggio e porta la sigla
   dello stesso capoturno che quattro giorni dopo scrive «lim 2%». **È lo stesso errore che
   il pilota aveva pagato al gate S2 con PRP-09**: dichiarare un'assenza cercandola dove ci
   si aspetta di trovarla.
3. **Una questione rovesciata.** Il ri-giudizio ha segnalato, fuori verdetto, che il rapporto
   di prova del laboratorio accreditato misura aw e umidità sullo stesso lotto e li dichiara
   **conformi** alla scheda tecnica. La nota presentava la divergenza come «scheda tecnica
   contro prove di stabilità», lasciando intendere che la scheda fosse la fonte dubbia: sono
   invece **due fonti concordi contro una**, e l'anomalia sta nel file delle prove — che è la
   base della proposta di portare il TMC a sei mesi.

### Cosa dice il secondo giro sul metodo

Le otto note del secondo giro avevano **tutte lo stesso difetto**, ed è un difetto che il
primo giro non poteva vedere perché nasce dalle correzioni: **conoscenza vera dell'archivio
scritta in una nota che non cita il documento che la porta.** Non è invenzione, è provenienza
mancante — e per la QA è indistinguibile da un fatto senza fonte.

**Metà esatta dei difetti di questo lotto sarebbe passata senza E9.**

### Un ruolo nuovo, emerso dai fatti

Il prompt di giudizio è congelato e chiede due cose. Il giudice del secondo giro ne ha
segnalata una terza, fuori verdetto: **una fonte del pacchetto che misura la stessa grandezza
di una nota, e che la nota non cita.** È stato il rilievo più utile del giro, ed è la
lacuna di copertura vista dal lato della provenienza. Candidato emendamento al prompt, da
valutare al gate — il prompt non si tocca a metà lotto.

---

## 11. Gli avvisi residui, motivati

> **⚠️ ERRATA del 18/08/2026.** La prima stesura di questa sezione dichiarava **32 avvisi** e
> ne descriveva quattro famiglie che sommavano **46**. La somma non quadrava, ed era un errore
> di conteggio mio: avevo contato le righe su `qa_all.md`, che **ripete al proprio interno i
> quattro report figli**, raddoppiando due famiglie. Il rilievo è del titolare. La sezione è
> riscritta qui sotto con i numeri ricontati dai soli report figli, e **tre avvisi che erano
> correggibili sono stati corretti** invece di essere motivati: il totale scende da 32 a 31.
> L'errata resta visibile: la correzione di un numero dichiarato non si fa in silenzio.

**31 avvisi**, ricontati dai quattro report figli — `qa_frontmatter` 9 · `qa_link_integrity`
0 · `qa_provenance` 22 · `qa_copertura` 0 — e **la somma delle famiglie quadra con il
totale**:

| Famiglia | Avvisi | Perché non si corregge |
|---|---|---|
| «`summary` e `title` si sovrappongono per meno del 20 %» | **10** | Sono le note il cui titolo è una domanda e il cui riassunto è la risposta: le parole non si ripetono per costruzione, ed è ciò che si vuole |
| «corpo fra 301 e 350 parole: si motiva o si spezza» | **9** | Si motivano. Portano una tabella di confronto o una citazione lunga, e spezzarle separerebbe il dato dal suo contesto. Nessuna supera il tetto dei 350 |
| Riscontro visivo sulle due immagini del lotto | **11** | 4 orari, 3 codici, 2 citazioni e 2 segnalazioni di fonte immagine, tutti sulla scansione del `MOD-QA-07` e sulla foto del pannello. **Entrambe lette a occhio**, e la prima ha prodotto la scoperta più importante del lotto. L'estrattore congelato è cieco sulle immagini per costruzione |
| «fonte che non aggancia nessuna affermazione» | **1** | ⚠️ **Falso positivo della suite, non difetto della nota** — vedi sotto |
| **totale** | **31** | |

⚠️ **Un avviso può ricadere in una sola famiglia**: le righe qui sopra sono disgiunte, e
questa è la differenza rispetto alla prima stesura.

### La chiusura a mano dell'avviso residuo, registrata

L'unico avviso non riconducibile a una famiglia motivabile è su
`questione-codice-ricambio-valvola-pkm-450`: `qa_provenance` dichiara che la fonte
`scheda_manutenzione_ordinaria_forni_industrial.csv` «non aggancia nessuna affermazione
della nota: rumore nel payload».

**È falso.** La riga 26 di quel file porta il codice `PKM-4471-EPDM (orig. Pakmatic)`, che è
**il quarto codice e il perno stesso della nota**: senza quella fonte la nota non esisterebbe.
Il rilievo è del revisore indipendente, e la chiusura a mano è registrata qui e nel decision
log con la sua motivazione — **una chiusura a mano non è mai silenziosa**.

Il difetto è dello strumento, non della nota, e si corregge come **fix di codice** in
`qa_provenance.py`, non come emendamento al metodo.

## 12. Cosa chiedo al titolare

1. **Approvazione del lotto 1A**, con i numeri qui sopra.
2. **Presa d'atto dei quattro candidati emendamento** del §8, più il quinto emerso dal
   ri-giudizio (il terzo ruolo del prompt di giudizio). Nessuno è stato applicato: il metodo
   non si emenda in silenzio, e il prompt di giudizio non si tocca a metà corsa.
3. **Una decisione sul ritmo**, alla luce del consuntivo: questo lotto è costato tre passaggi
   di revisione e sedici rilievi accolti, su sette grezzi. Il tetto di due lotti per sessione
   regge, ma il lotto 1B va aperto contando i fatti prima di scrivere, come la regola di
   apertura ora prescrive.
