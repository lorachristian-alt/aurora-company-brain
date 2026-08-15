# metodo_01 — Generazione dell'archivio simulato

> **Cos'è** · Il metodo con cui è stato costruito l'archivio grezzo (i 160 file di
> `02_corpus/` e del corpus congelato sul Desktop): regole di generazione, realismo
> tecnico, controlli automatici e revisione.
> **Quando si usa** · Per replicare il progetto su un'altra azienda, e per l'espansione
> a corpus v2 (`06_operativo/prompt/prompt_corpus_v2_espansione.txt`).
> **Cosa non toccare** · Regole e snippet: sono il SORGENTE del metodo. Una modifica qui
> si propaga rigenerando i documenti derivati (misurazione, canonizzazione).
> **Nota di riorganizzazione (15/08/2026)** · File rinominato (ex `metodo_01_generazione_archivio.md`).
> In questo progetto canone e registro delle contraddizioni sono UNITI in
> `canone_aurora.md`; dove il testo cita `canone.md` e `contraddizioni.md` come file
> separati, leggi quel file unico. Mappa completa dei nomi storici in `00_INIZIA_QUI.md`.

**Prompt operativo.** Leggi tutto prima di scrivere un solo file. Esegui nell'ordine.
Sostituisci `<SETTORE>` con il settore che ti viene indicato (alimentare, edilizia,
impianti, manutenzioni, rifiuti, meccanica) e `<AZIENDA>` con la ragione sociale inventata.
Dove trovi un numero fra parentesi quadre è una scala: adattala alla dimensione richiesta,
mantenendo le proporzioni.

Il risultato è l'archivio grezzo di una PMI simulata, più il test che ne misura
l'indicizzabilità. È il **primo step** di un second brain: la canonizzazione in markdown
avviene dopo, in un'altra sessione, e non è oggetto di questo documento.

---

## Regola d'ingaggio: chiedi, e chiedi presto

**Usa `AskUserQuestion` il più possibile.** Ogni scelta che non è già scritta qui dentro va
chiesta, non indovinata. Un'opzione si sceglie in due secondi; un archivio da [160] file
costruito sull'assunzione sbagliata si rifà in due giorni.

**Prima di scrivere un solo file**, chiedi con giri di domande:

- **settore e dimensione** dell'azienda, e se ha una sede sola o più unità locali
- **il filo rosso**: proponi due o tre eventi possibili che attraversano i reparti (un
  guasto che diventa reclamo, una verifica di un ente che scopre una prescrizione mai
  chiusa, una trattativa che stringe i margini sotto il costo) e fatti dire quale
- **la scala**: quanti file, quanti mesi di cronologia, quante persone
- **quanto sporco**: se l'archivio deve essere ordinato con qualche crepa, o davvero
  caotico come un file server mai potato
- **i nomi reali**: se controparti, enti e banche possono essere organizzazioni realmente
  esistenti (più immersivo, coperto dal disclaimer) o tutto inventato (più prudente)
- **a cosa serve il test**: solo baseline prima della canonizzazione, o anche misura
  ripetuta dopo — cambia quante domande sui metadati ha senso includere

**Durante il lavoro**, fermati e chiedi ogni volta che:

- due letture ragionevoli della stessa istruzione porterebbero a due archivi diversi
- stai per prendere una decisione difficile da annullare (la struttura della cronologia, il
  perimetro del filo rosso, la scelta di quale fonte prevale in una contraddizione)
- scopri un conflitto fra due cose che ti sono state chieste
- una correzione che stai per applicare distruggerebbe una contraddizione voluta

**Come si costruiscono le opzioni.** Due-quattro alternative davvero distinte, e in ogni
descrizione **il compromesso dichiarato**: cosa guadagni e cosa perdi scegliendola. Metti
per prima quella che consiglieresti e segnala che la consigli. Domande in prosa solo quando
nessun insieme di opzioni sarebbe onesto — per esempio quando ti serve un dato che solo chi
ti ha commissionato il lavoro possiede.

Poche domande per volta: meglio due giri da tre domande che un giro da otto.

---

## 0. Cosa devi produrre

| Artefatto | Dove | Cosa contiene |
|---|---|---|
| Archivio grezzo | `sources/` | [160] file nei formati nativi di un file server, mai in markdown |
| Avvertenza di finzione | dentro `sources/` | Un `.txt` che dichiara che tutto è simulato |
| Canone | fuori dal vault | Chiave di lettura: entità, cronologia, contraddizioni volute |
| Domande | fuori dal vault | [282] domande di verifica |
| Risposte | fuori dal vault | Le risposte con le fonti e le note di valutazione |
| Eval set | fuori dal vault | Lo stesso contenuto in JSONL, per la valutazione automatica |
| README | radice del repo | Disclaimer pubblico e composizione dell'archivio |
| Documento di misura | accanto al canone | Il protocollo coi cinque prompt: **lo generi tu**, vedi §14 |

**Nel vault indicizzato va solo `sources/`.** Tutto il resto vive in una cartella sorella.

### Come consegni

Crea questo layout esatto, e alla fine dimmi i percorsi assoluti:

```
Desktop\<progetto>\                     <-- il repository: tutto il pacchetto
├── README.md                           <-- disclaimer pubblico e risultati
├── 00_INIZIA_QUI.md                    <-- guida d'orientamento
├── 01_metodo\                          <-- questo documento, misurazione, canone
├── 02_corpus\                          <-- i [160] file grezzi. NIENT'ALTRO qui dentro
│   └── _QUESTO_ARCHIVIO_E_SIMULATO.txt
├── 03_valutazione\                     <-- domande, risposte, eval set: MAI indicizzare
├── 04_misurazioni\                     <-- risultati delle misure, una cartella per data
├── 05_rag_produzione\                  <-- pipeline RAG di produzione (config C)
└── 06_operativo\                       <-- scaletta, manifest, decision log, prompt
```
Il vault Obsidian dell'azienda vive FUORI dal repository (es. `Desktop\<azienda>-cervello\`).

Il vault e `03_valutazione\` non stanno mai nello stesso perimetro: una ricerca
ricorsiva lanciata dal vault non deve poter raggiungere le risposte.

---

## 1. Prima di generare: il canone

Non scrivere nessun documento prima di aver fissato il canone. Se generi prima e concili
dopo, i documenti si contraddicono in modo casuale e non saprai più distinguere un errore
da una trappola.

Fissa e scrivi su file, prima di tutto:

- **Anagrafica**: ragione sociale, forma giuridica, sede, P.IVA, REA, capitale, PEC,
  codice destinatario SDI, telefono, IBAN. Ogni codice deve superare il suo algoritmo (§5).
- **[20] persone** con nome, ruolo, reparto, interno telefonico, cellulare, e **un registro
  linguistico assegnato**: chi scrive in maiuscolo senza punteggiatura, chi cita sempre la
  norma, chi passa al dialetto sotto pressione, chi mette note fra parentesi. Il registro
  va rispettato in ogni documento in cui quella persona compare.
- **[14] controparti**: clienti, fornitori, enti, consulenti, con anagrafica completa.
- **Impianti e macchine** con sigle, matricole, anni di installazione.
- **Formato dei lotti/commesse**, con la regola di composizione, e [10] lotti reali già
  calcolati con la loro data.
- **Cronologia**: una finestra di [5] mesi con **un filo rosso** — un evento che attraversa
  reparti diversi e genera documenti in cascata (un guasto che produce un difetto che
  genera un reclamo che attiva un blocco merce, una verifica, una lettera al cliente e
  un'ispezione). È ciò che rende l'archivio interrogabile in profondità.
- **Un anno di riferimento**, e il giorno della settimana del 1° gennaio. Ogni data che
  scriverai va verificata contro questo.

---

## 2. Struttura dell'archivio

Proporzioni verificate su un caso reale, da mantenere:

```
   .txt    verbali, mail interne, appunti, procedure, note, rumore d'ufficio
   .csv    registri, inventari, listini, timbrature, log di reparto
   .pdf    contratti, certificati, verbali di enti, fatture, bollette, visure
   .xlsx   budget, previsionali, KPI, tracciabilità, libro unico
   .eml    mail vere con header completi, 8 con allegati in base64
   .docx   procedure, istruzioni operative, lettere in bozza, job description
   .jpg    foto da telefono e scansioni da multifunzione
   .pptx   presentazioni commerciali, organigrammi, business case
   .log    tracciati di datalogger e pannelli di controllo
   .xml    fatture elettroniche a tracciato
   .p7m    una busta di firma
```

**Mai markdown.** Un file server non contiene markdown.

Regole di composizione:
- **Un terzo dei file non deve avere nulla a che fare col filo rosso.** Menu della mensa,
  preventivo di tinteggiatura non accettato, convenzione palestra, verbale di condominio,
  newsletter inoltrata. Un archivio in cui tutto è rilevante non è un archivio, è un caso di
  studio. Verifica: nessun tema deve comparire in più del 62% dei file.
- **Nomi di file realisticamente cattivi**: `Scansione_20260518_0003.pdf`,
  `doc 2 (1).pdf`, `img20260428_09241055.txt`, `listino v2 VECCHIO non usare.csv`,
  `Nuova cartella di lavoro.xlsx`, `~$ttera_risposta_BOZZA_v3.docx` (lock file di Word, 162
  byte, formato binario reale: lunghezza nome + nome ANSI + lunghezza + nome UTF-16LE).
- **[4] coppie di duplicati** con nomi diversi e contenuto identico, di cui almeno tre con
  nome generato da scanner o browser.
- **[6] file di testo in cp1252 con terminatori CRLF**, il resto UTF-8. Devono contenere
  caratteri accentati, altrimenti la differenza non è verificabile.
- **[5] documenti in OCR degradato**: sostituzioni coerenti con lo scanner (`0`↔`O`,
  `l`↔`1`, `S`↔`5`), macchie `#####`, `[illeggibile]`, spaziature irregolari.
  **I codici sotto il degrado devono restare validi una volta decodificati.**
- **[8] allegati segnaposto** da 60-90 byte con la sola riga
  `%PDF-1.4 % documento archiviato - <nome>`: nei file server reali sono ovunque.
- Almeno **tre file con estensione mendace**: un `.pdf` che è testo, un `.xlsx` che è un
  PDF, un allegato il cui nome contraddice il contenuto.

---

## 3. Regole di generazione

**Un solo generatore per file.** Se due script scrivono lo stesso file, uno dei due
riporterà indietro le correzioni dell'altro senza che te ne accorga. Tieni un registro
`chi_genera_cosa.txt` e consultalo prima di scrivere.

**Salva ogni [15] file.** Se la sessione si interrompe, riprendi da lì invece di rigenerare.

**Se lavori con agenti in parallelo**: ognuno scrive solo nella propria sottocartella di
lavoro, e nessuno tocca l'archivio. Le collisioni su file condivisi sono già costate un
giro intero.

**Ogni documento porta le tracce di chi lo ha scritto**: annotazioni a margine, correzioni
barrate, commenti fra parentesi quadre, una firma sbagliata, un campo lasciato in bianco,
una riga aggiunta a penna dopo la stampa. Un documento perfetto è un documento falso.

**Numeri non tondi.** Ma i totali devono restare la somma dei loro addendi: se perturbi un
importo, ricalcola il totale. Non fare il contrario.

---

## 4. Il registro delle contraddizioni volute

**Questa è la parte che distingue un archivio utile da un archivio sporco.**

Mentre generi, tieni un file `contraddizioni.md` e scrivi ogni divergenza che introduci
di proposito, con: cosa diverge, in quali due file, quale valore deve prevalere e perché.
Punta a [25-30] contraddizioni, distribuite fra:

- lo stesso dato in due sistemi (gestionale vs listino vs contratto)
- una versione superata che resta in circolazione accanto a quella valida
- un documento che cita un articolo di contratto sbagliato
- una presentazione commerciale che arrotonda un dato di bilancio
- un registro che conta cinque casi e un verbale sindacale che ne conta sei
- una misura verbalizzata che non coincide con la foto da cui è stata presa
- un allegato che non è quello che il corpo della mail annuncia

**Se non registri una contraddizione mentre la crei, in fase di revisione la troverai e la
correggerai, distruggendo il valore del test.** È successo: quattro revisori senza il
registro hanno segnalato 82 problemi, di cui buona parte erano trappole.

Distingui e tieni separati:
- **contraddizione voluta** → va nel registro, non si tocca
- **errore vero** → si corregge
- **realismo che sembra errore** → va nel registro con la spiegazione (esempio: un registro
  consumi in cui le colonne sono arrotondate all'intero e il costo è calcolato sui decimali
  reali: una verifica ingenua trova centinaia di righe «sbagliate» e sono tutte corrette)

---

## 5. Realismo tecnico: i codici devono superare gli algoritmi

Dichiaralo nell'avvertenza e rendilo vero. Snippet da usare così come sono:

```python
def piva_valida(s):                       # partita IVA italiana
    if len(s) != 11 or not s.isdigit(): return False
    t = 0
    for i, c in enumerate(s[:10]):
        n = int(c)
        if i % 2:
            n *= 2
            if n > 9: n -= 9
        t += n
    return (10 - t % 10) % 10 == int(s[10])

def gs1_valido(s):                        # EAN-13, ITF-14, EAN-8
    c = s[:-1][::-1]
    t = sum(int(d) * (3 if i % 2 == 0 else 1) for i, d in enumerate(c))
    return (10 - t % 10) % 10 == int(s[-1])

def iban_valido(s):                       # MOD-97
    s = s.replace(" ", "").upper()
    r = s[4:] + s[:4]
    return int("".join(str(int(ch, 36)) for ch in r)) % 97 == 1

CF = {'A':(1,0),'B':(0,1),'C':(5,2),'D':(7,3),'E':(9,4),'F':(13,5),'G':(15,6),'H':(17,7),
      'I':(19,8),'J':(21,9),'K':(2,10),'L':(4,11),'M':(18,12),'N':(20,13),'O':(11,14),
      'P':(3,15),'Q':(6,16),'R':(8,17),'S':(12,18),'T':(14,19),'U':(16,20),'V':(10,21),
      'W':(22,22),'X':(25,23),'Y':(24,24),'Z':(23,25),'0':(1,0),'1':(0,1),'2':(5,2),
      '3':(7,3),'4':(9,4),'5':(13,5),'6':(15,6),'7':(17,7),'8':(19,8),'9':(21,9)}
def cf_valido(s):                         # carattere di controllo del codice fiscale
    t = sum(CF[c][0] if i % 2 == 0 else CF[c][1] for i, c in enumerate(s[:15]))
    return chr(ord('A') + t % 26) == s[15]
```

Per l'IBAN serve anche il **CIN italiano** (la lettera dopo le due cifre di controllo):
calcolalo, non inventarlo.

**Il codice dentro un file OCR deve decodificarsi in un codice valido.** Un controllo che
cerca `\d{11}` è cieco su `O39847lOZ3O`: scrivi il verificatore che prima applica la mappa
di sostituzione inversa e poi valida. Questo errore è sfuggito a 89 controlli automatici.

Altre cose che devono essere vere e non verosimili: i giorni della settimana contro il
calendario reale; le scadenze calcolate (fine mese + N giorni, N giorni data documento);
le durate (fine meno inizio); i riferimenti normativi realmente esistenti e pertinenti al
punto in cui sono citati; i CAP corrispondenti al comune.

---

## 5-bis. Attrezzatura

```
pip install reportlab pypdf openpyxl python-docx python-pptx Pillow piexif
```
`email`, `zlib`, `os`, `datetime` sono di libreria standard.

| Formato | Come si produce | Trappola |
|---|---|---|
| `.pdf` | `reportlab` (canvas). Per le scansioni: ruota di 0,3-0,8°, aggiungi grana e rumore sale-pepe con `Pillow`, poi incorpora l'immagine | `pypdf` **legge** ma non riscrive gli stream ASCII85: vedi snippet sotto |
| `.xlsx` | `openpyxl` con formule vere (`=SUM(...)`), più fogli, celle a errore volute | Le formule non sono calcolate finché non apri in Excel: `data_only=True` restituisce `None`. Non fondare i controlli su quei valori |
| `.docx` | `python-docx`. Il barrato è `run.font.strike`, **mai** `~~testo~~` | La numerazione automatica usa **un contatore per documento**: se un elenco ha anche numeri battuti a mano esce «1,1,3,4,2». Usa numeri espliciti come testo |
| `.pptx` | `python-pptx`, con note del relatore in `slide.notes_slide` | Le note lunghe vanno troncate a mano: se le spezzi male la coda finisce stampata nella slide |
| `.eml` | `email.message.EmailMessage`, allegati con `encode_base64`, `Received` = `Date` + 20-35 s | Se generi il `Date` e non il `Received`, o li disallinei, la mail è tecnicamente impossibile |
| `.jpg` | `Pillow` per l'immagine, `piexif` per Make/Model/DateTimeOriginal | L'EXIF deve essere coerente con la cronologia, non solo col dispositivo |
| `.p7m` | busta PKCS#7 `SignedData` costruita in DER a mano | Dichiara nel canone che è un contenitore, non una firma valida |

**La fattura elettronica ha un tracciato che si valida davvero**, e sbagliarlo è l'unico
modo per farsi bocciare un file da chiunque lo apra con un validatore:

- radice `FatturaElettronica` con `versione="FPR12"`, nome file `IT<piva>_<progressivo>.xml`
  (progressivo alfanumerico, non solo cifre)
- l'ordine degli elementi **non è libero**: è una `sequence` dello schema. Rispetta
  `DatiTrasmissione` → `CedentePrestatore` → `CessionarioCommittente` → `DatiGeneraliDocumento`
  → `DatiOrdineAcquisto` → `DatiDDT` → `DettaglioLinee` → `DatiRiepilogo` → `DatiPagamento`
  → `DettaglioPagamento`
- **nessun elemento facoltativo vuoto**: i tipi stringa hanno `minLength=1`, quindi un
  `<CodiceCUP></CodiceCUP>` lasciato lì per simmetria fa fallire la validazione. Se non hai
  il dato, ometti l'elemento
- codici che devono essere reali: `TD01` fattura, `RF01` regime ordinario, `MP05` bonifico,
  `MP12` RIBA, `TP02` pagamento completo, `EsigibilitaIVA` I/D/S, `SocioUnico` SU/SM,
  `StatoLiquidazione` LN/LS
- i prezzi ammettono 5 decimali; `ImportoTotaleDocumento` deve quadrare con la somma dei
  `DatiRiepilogo`, e imponibile × aliquota deve dare l'imposta al centesimo

**Il lettore multi-formato è il pezzo più importante di tutta l'attrezzatura**, perché ogni
controllo passa da lì: se è cieco su un formato, tutti i controlli su quel formato passano
senza aver verificato nulla. Il ramo `.eml` è quello che si dimentica.

```python
def text_of(p):
    e = p.rsplit(".", 1)[-1].lower()
    if e in ("txt", "csv", "log", "xml", "md", "p7m"):
        raw = open(p, "rb").read()
        for enc in ("utf-8", "cp1252"):
            try: return raw.decode(enc)
            except UnicodeDecodeError: pass
        return raw.decode("latin-1")
    if e == "pdf":
        from pypdf import PdfReader
        return "\n".join((pg.extract_text() or "") for pg in PdfReader(p).pages)
    if e == "docx":
        from docx import Document
        d = Document(p)
        return "\n".join([q.text for q in d.paragraphs] +
                         [c.text for t in d.tables for r in t.rows for c in r.cells])
    if e == "xlsx":
        from openpyxl import load_workbook
        wb = load_workbook(p, data_only=True)
        return "\n".join(" ".join(str(c) for c in row if c is not None)
                         for ws in wb.worksheets for row in ws.iter_rows(values_only=True))
    if e == "pptx":
        from pptx import Presentation
        out = []
        for sl in Presentation(p).slides:
            for sh in sl.shapes:
                if sh.has_text_frame: out.append(sh.text_frame.text)
                if sh.has_table:
                    out += [c.text for r in sh.table.rows for c in r.cells]
            if sl.has_notes_slide: out.append(sl.notes_slide.notes_text_frame.text)
        return "\n".join(out)
    if e == "eml":                      # senza questo ramo i controlli sulle mail sono ciechi
        from email import policy
        from email.parser import BytesParser
        m = BytesParser(policy=policy.default).parse(open(p, "rb"))
        parti = ["%s: %s" % (h, m[h]) for h in
                 ("From", "To", "Cc", "Subject", "Date", "Message-ID") if m[h]]
        b = m.get_body(preferencelist=("plain", "html"))
        if b is not None: parti.append(b.get_content())
        parti += ["[allegato] %s" % a.get_filename()
                  for a in m.iter_attachments() if a.get_filename()]
        return "\n".join(parti)
    return ""
```

**Correggere un PDF già generato** senza rigenerarlo (serve sempre, perché i difetti si
scoprono dopo):

```python
def edita_pdf(path, coppie):            # coppie = [(vecchio, nuovo), ...]
    import zlib
    from pypdf import PdfWriter
    from pypdf.generic import ArrayObject, NameObject, NumberObject
    w = PdfWriter(clone_from=path)
    for pg in w.pages:
        c = pg["/Contents"]
        for s in (c if isinstance(c, ArrayObject) else [c]):
            s = s.get_object()
            d = s.get_data(); o = d
            for a, b in coppie:
                d = d.replace(a.encode("latin-1"), b.encode("latin-1"))
            if d != o:                  # reportlab usa ASCII85+Flate: si ricomprime in Flate
                comp = zlib.compress(d, 9)
                s._data = comp
                s[NameObject("/Filter")] = NameObject("/FlateDecode")
                s[NameObject("/Length")] = NumberObject(len(comp))
    with open(path, "wb") as f: w.write(f)
```

**Il lock file di Word** (rumore realistico, non cancellarlo mai in fase di pulizia):

```python
b = bytearray(162); nome = "Nome Cognome"
b[0] = len(nome); b[1:1+len(nome)] = nome.encode("cp1252")
for i in range(1 + len(nome), 54): b[i] = 0x20
b[54] = len(nome); b[56:56 + 2*len(nome)] = nome.encode("utf-16-le")
open("~$nomedocumento.docx", "wb").write(bytes(b))
```

**Le date del filesystem** si impostano con `os.utime(p, (ts, ts))`. Tienile in un unico
script con una tabella `pattern del nome → data`, e non spargerle: è l'ultimo passo di ogni
giro e va rieseguibile in un comando.

---

## 6. Ordine delle operazioni

**Vincolante. Invertirlo è l'errore che ho commesso più volte.**

```
1. contenuti          genera e correggi i file
2. metadati           /Author /Producer /CreationDate dei PDF, docProps di Office,
                      EXIF dei JPEG, Message-ID delle mail — coerenti con l'emittente
3. date del filesystem  mtime coerente con la data interna di ogni documento
```

Ogni volta che tocchi un contenuto, **rifai 2 e 3**. Se esegui i metadati dopo le date, i
file portano la data di generazione; se esegui le date prima delle correzioni, i file
corretti portano l'ora in cui li hai corretti.

Regole per il passo 3:
- nessun file con la data in cui stai lavorando
- massimo [3] file nello stesso minuto
- le date coprono almeno tre anni diversi
- **un registro non può avere una data anteriore alla sua ultima riga**

---

## 7. Verifica: le prospettive da coprire

Scrivi i controlli come script rieseguibili, non come ispezioni una tantum. Ogni difetto
che trovi diventa un test permanente. Obiettivo: [89] controlli automatici.

1. **Integrità tecnica** — ogni file si apre con la libreria del suo formato; nessuno
   danneggiato; gli allegati delle mail si decodificano; i duplicati sono ancora identici.
2. **Codici verificabili** — §5, applicato a *tutti* i codici che una regex trova nei file,
   non a un elenco atteso.
3. **Aritmetica** — scopri da solo le relazioni fra colonne (a×b=c, a+b=c) che valgono
   sulla maggioranza delle righe, poi segnala le righe che le violano. Ricalcola ogni
   totale dichiarato dalla somma dei suoi addendi.
4. **Cronologia** — ogni «giorno della settimana + data» contro il calendario; nessun
   documento cita al passato un fatto posteriore alla propria data; nelle mail nessun
   messaggio citato è più recente dell'header `Date`, nemmeno nelle citazioni annidate;
   il `Received` non precede mai il `Date`.
5. **Plausibilità statistica** — indici di bilancio dentro le forchette del settore;
   distribuzioni non uniformi; nessun tema in più del 62% dei file.
6. **Riferimenti normativi** — esistono, sono in vigore alla data del documento, e sono
   pertinenti al punto in cui sono citati.
7. **Riferimenti incrociati** — ogni codice interno (modulo, procedura, non conformità,
   lotto, matricola) esiste dove è citato e ha lo stesso significato ovunque.
8. **Concordanza dei numeri** — lo stesso dato in file diversi coincide, oppure è nel
   registro delle contraddizioni.
9. **Qualità del testo** — nessun segnaposto non sostituito, nessun `None`/`nan`, nessun
   carattere di sostituzione, nessuna sequenza markdown (`**`, `~~`) stampata dentro un
   documento Office, nessun marcatore di lavorazione (`@@TABLE`, `[[COMMENT:`) visibile.
10. **Fogli di calcolo** — nessun riferimento circolare (Excel li rifiuta), nessuna formula
    che punta a una cella vuota, nessuna numerazione automatica di Word che si somma a
    numeri battuti a mano.

---

## 8. Revisione

Quando l'archivio è completo, fai rileggere **ogni file da un revisore indipendente**,
diviso per blocchi di formato omogeneo.

**Ogni revisore deve ricevere il canone e il registro delle contraddizioni**, e deve
classificare quello che trova in tre categorie:

- **A — errore vero**: nessun documento lo giustifica e il registro non lo dichiara
- **B — contraddizione non registrata**: plausibile e interessante, va aggiunta al registro
- **C — falso allarme**: il registro la dichiara; elencala in una riga per dimostrare di
  averla riconosciuta

Senza questa tripartizione i revisori ti riporteranno le trappole come difetti e tu le
correggerai.

**Dopo ogni correzione, propagala.** Se sposti un evento nel tempo, cerca *tutti* i
documenti che lo citano: una modifica giusta lasciata a metà genera più danno dell'errore
che risolveva. Verifica sempre che la correzione non ne rompa un'altra: sostituire un
numero che compare in due punti — uno giusto e uno sbagliato — li rompe entrambi.

**Non fidarti del primo esito di un controllo.** Prima di correggere, prova l'ipotesi
alternativa che il dato sia giusto e sia il controllo a essere ingenuo.

---

## 9. Il dataset di test

**Genera le domande sull'archivio finale**, non su uno snapshot intermedio: se aggiungi
file dopo, le domande sui metadati diventano false.

[282] domande, composizione verificata:

| Tipo | Quota | Cosa misura |
|---|---|---|
| Ricerca diretta | 30% | il retrieval di base |
| Aggregazione | 10% | leggere una tabella intera, non un frammento |
| Calcolo | 10% | ragionare sul dato recuperato |
| Ricostruzione temporale | 10% | mettere in fila eventi da fonti sparse |
| Attraversamento | 15% | collegare documenti che non si citano fra loro |
| Conflitto | 5% | segnalare la contraddizione invece di scegliere a caso |
| Non rispondibile | 11% | resistere all'allucinazione: il dato **non** è in archivio |
| Metadato | 3% | domande sulla forma dell'archivio |

Per ogni voce: `id`, `domanda`, `risposta`, `fonti`, `tipo`, `difficolta`,
`note_valutazione`. Per le non rispondibili aggiungi `verifica_assenza`: la prova che hai
cercato il dato e non c'è.

Verifica **severa** prima di consegnare:
- ogni fatto affermato è riscontrabile nelle fonti citate
- ogni citazione fra virgolette esiste testualmente nel file citato
- ogni fonte elencata contribuisce davvero, e nessuna fonte usata manca
- le voci di tipo conflitto hanno i valori divergenti in **file diversi**
- le non rispondibili sono davvero senza risposta
- la risposta risponde alla domanda posta (verifica meccanica: sovrapposizione di parole
  chiave fra domanda e risposta; sotto il 20% ispeziona a mano)
- nessuna risposta si contraddice al suo interno

**Genera i tre file da un'unica sorgente.** Il JSONL è il padrone; i due markdown si
producono da lì con uno script. Se li scrivi separatamente divergeranno, e te ne accorgerai
solo quando qualcuno noterà che la domanda 95 ha due testi diversi.

---

## 10. I file di supporto

**README** — prima cosa che chiunque legge. Deve dichiarare in apertura che l'archivio è
una simulazione dimostrativa, che nessuna organizzazione nominata ha redatto, firmato o
ricevuto alcuno di quei documenti, e che codici e recapiti non corrispondono a soggetti
reali. Poi la composizione dell'archivio, i formati, e come si usa il test.

**Avvertenza dentro `sources/`** — un `.txt` con lo stesso contenuto in forma breve, perché
viaggia con l'archivio anche se qualcuno copia solo quella cartella. Ogni sua affermazione
deve essere vera: se dichiari che i recapiti sono inventati, non lasciare numeri di
pubblica utilità reali senza dichiarare l'eccezione.

**Canone** — la chiave di lettura: valori canonici, contraddizioni volute con la fonte che
prevale, e cosa *non* esiste in archivio.

Nel README e nel canone **ogni numero dichiarato va ricontato da uno script**, non scritto
a memoria: conteggi per formato, peso, numero di domande, quante mail hanno allegati.

---

## 11. Errori da non ripetere

- Partire senza aver chiesto: settore, filo rosso, scala e livello di sporcizia decidono
  tutto il resto, e indovinarli costa la riscrittura dell'archivio.
- Generare prima di aver fissato il canone.
- Non registrare le contraddizioni mentre le crei.
- Mandare i revisori senza il canone.
- Due script che scrivono lo stesso file.
- Metadati dopo le date, o date prima delle correzioni.
- Correggere un evento e non propagare la correzione a tutti i documenti che lo citano.
- Sostituzioni globali su un valore che compare in più punti con significati diversi.
- Regex di sostituzione applicate al codice sorgente degli script (una `\b153\b` ha
  trasformato `newline="\n"` in un a capo vero e ha rotto il generatore).
- Controlli sui codici che ignorano le versioni degradate dall'OCR.
- Correggere al primo esito di un controllo senza provare l'ipotesi alternativa.
- Cancellare rumore realistico scambiandolo per residuo: i lock file di Word, i
  `Nuova cartella di lavoro.xlsx`, i duplicati con nomi da scanner sono contenuto.
- Generare il dataset su un archivio che poi cambia.
- Scrivere i tre file del dataset separatamente.
- Dichiarare nel README numeri non ricontati.

---

## 12. Consegna e passo successivo

Prima di dichiarare finito, esegui in quest'ordine e allega gli esiti:

```
1. contenuti finali
2. metadati
3. date
4. le tre suite di controlli automatici        → devono passare tutte
5. verifica dei file di supporto               → zero problemi
6. coerenza dataset/archivio                   → nessun valore superato, nessuna fonte inesistente
7. integrità binaria di tutti i formati        → zero file danneggiati
```

Riporta con onestà: se restano rilievi aperti, elencali in un file con posizione e
correzione proposta, invece di dichiarare una perfezione che non puoi dimostrare.

**Poi, prima di canonizzare in markdown:**

1. **Misura la baseline.** Indicizza `sources/` così com'è e fai girare le [282] domande.
   Questo numero si può ottenere una volta sola: dopo la canonizzazione è perduto per
   sempre, e senza di esso il second brain non ha nulla con cui confrontarsi.
2. **Escludi esplicitamente** la cartella con le risposte dalla configurazione
   dell'indicizzatore. Non basta che stia fuori dal vault: il primo `**/*.md` ricorsivo se
   la riprende, e un test le cui risposte sono state viste dal modello è bruciato.
3. Solo allora canonizza in markdown nelle cartelle tematiche, con frontmatter e
   backlink, e rimisura.

Nota per chi costruirà il grafo: Obsidian tratta come note solo i `.md`, e i file di altri
formati compaiono nel grafo **solo se una nota markdown li collega**. Il grafo nasce dalle
note canonizzate, non dai file grezzi; e va acceso «Detect all file extensions», altrimenti
i `.txt` restano invisibili nel vault.

---

## 13. Il sanity check prima della canonizzazione

Quando l'archivio e' finito, **prima di organizzarlo in markdown**, si misura. E' l'unico
momento in cui si puo' ottenere la baseline: dopo l'organizzazione quel numero e' perduto
per sempre, e senza di esso il second brain resta un'affermazione invece di una
dimostrazione.

La procedura completa - le due configurazioni congelate, i cinque prompt da copiare alla
lettera, dove tenere la cartella con le risposte, quali file nascono e quante volte si
lancia ciascun prompt - sta in **`metodo_02_misurazione.md`**, il documento gemello di questo.

In sintesi: tre sessioni separate (preparazione, esecuzione, valutazione); chi risponde non
vede mai le risposte attese; chi valuta non e' chi ha risposto; due configurazioni in
parallelo - un retrieval agentico e un RAG a embedding - entrambe congelate perche' la
misura successiva dovra' cambiare **una sola variabile**, la forma dell'archivio.

Quattro metriche, in ordine di quanto dicono: tasso di allucinazione sulle domande non
rispondibili, riconoscimento dei conflitti, divario fra ricerca diretta e attraversamento,
precisione delle fonti.

---

## 14. Genera anche il documento di misura

Alla fine del lavoro scrivi `eval\metodo_02_misurazione.md`. Serve perché chi eseguirà la misura
— fra settimane o mesi, in un'altra sessione — deve trovare la procedura completa senza
dover ricostruire nulla.

**Gerarchia, e non si inverte.** Questo blueprint è il **sorgente**; il documento di misura
è un **prodotto** che ne discende. In testa al file che generi scrivi:
`> Generato da metodo_01_generazione_archivio.md §14. Se una regola va cambiata, si cambia lì e si
rigenera questo file.` Così non nascono due versioni della stessa procedura.

### Struttura del documento da generare

1. Cosa stai misurando, e le due configurazioni a confronto
2. **Regola d'ingaggio**: i prompt chiedono con `AskUserQuestion` quale blocco elaborare,
   contando le righe gia' presenti nel file di output e proponendo il successivo. E la parte
   in negativo, che serve almeno quanto l'altra: **i parametri delle configurazioni non si
   chiedono mai**. `top_k`, dimensione dei pezzi, modello, temperatura, domande per blocco
   sono congelati — una domanda premurosa tipo «preferisci top_k 8 o 12?» rende i due numeri
   non confrontabili, ed e' l'unico errore della procedura che non si corregge dopo.
3. Prima di cominciare: separare le risposte, creare `Desktop\misure_<progetto>\`
4. Le due tabelle di configurazione immutabile (copiale da §13)
5. Tabella dei file prodotti e **quante volte si lancia ciascun prompt**, con le tre
   avvertenze qui sotto
6. **Tabella «dove si esegue ogni passo»**: per ciascun passo, in quale cartella si apre il
   terminale, cosa il modello riesce a vedere da li', cosa scrive. E' il pezzo che rende i
   perimetri una conseguenza fisica invece che una promessa nel prompt — i passi dal quarto
   in poi si aprono in `Desktop\misure_<progetto>\`, da dove il vault **non e' raggiungibile**,
   e per questo il modello puo' leggersi da solo i file di contesto senza poter barare.
7. I sette passi, ciascuno con: spiegazione in parole semplici → prompt → come si capisce
   che e' andata bene. Il passo dell'esecuzione dello script va chiarito bene: **si lancia in
   PowerShell, non «dentro» l'agente** — con la verifica `python --version`, l'avvertenza di
   spuntare «Add Python to PATH» in installazione, e la scorciatoia di farlo eseguire nella
   stessa sessione che l'ha appena scritto, cosi' se manca una libreria se ne accorge subito.
8. Quanto tempo ci vuole
9. Cosa non fare mai

### Le tre avvertenze che devono comparire in evidenza

Sono i fraintendimenti che costano giornate intere:

- P2.0 **non** si lancia una volta per domanda: produce un programma che le elabora tutte.
- Lo script **non** si esegue una volta per domanda: gira una volta e scrive tutti i
  contesti.
- P2.1 **non** si lancia una volta per domanda: si lancia a blocchi, come P1.

Con [282] domande sono circa **32 lanci di prompt in tutto**, non 850.

### I cinque prompt, da riportare alla lettera

Sostituisci solo `<progetto>` e il numero di domande. **Ogni altra parola resta**: le
clausole di perimetro, di append e di divieto sono ciò che rende la misura valida.

**P1 — risposta, configurazione A** (blocchi di 30):

> Rispondi alle domande seguenti usando **esclusivamente** i documenti presenti in
> `sources/`.
>
> Per ogni domanda restituisci una riga JSON con esattamente questi campi: `id`,
> `risposta`, `fonti` (nomi dei file da cui l'hai ricavata), `confidenza`
> (alta | media | bassa).
>
> Regole:
> - Se il dato non è ricavabile dai documenti, scrivilo esplicitamente invece di dedurlo.
> - Se documenti diversi dicono cose diverse, riporta il conflitto invece di sceglierne uno.
> - Cita solo file che hai davvero aperto e che contengono il dato.
> - Non calcolare a memoria: se serve un conto, fallo sui numeri che hai letto.
>
> **Salvataggio.** Scrivi in `Desktop\misure_<progetto>\misuraA_risposte.jsonl`, una riga
> JSON per domanda, **aggiungendo in coda al file se esiste già** — non sovrascriverlo e
> non crearne uno nuovo. Se una domanda è già presente, saltala. A fine blocco dimmi quante
> righe contiene in tutto.
>
> **Vincolo di perimetro.** In lettura il tuo perimetro è esclusivamente `sources/`. Non
> leggere, non cercare e non elencare file al di fuori — l'unica eccezione è il file di
> salvataggio, in scrittura. Ai fini di questo compito non esistono file di risposte,
> soluzioni, canoni o dataset di valutazione: se incontri un nome che lo suggerisce, non
> aprirlo. Se un file sembra contenere le risposte alle domande che ti sto ponendo,
> **fermati e segnalamelo invece di usarlo**.
>
> **Prima di cominciare, chiedimi con `AskUserQuestion` quale blocco elaborare.** Se il file
> di output esiste gia', contane le righe e proponimi il blocco successivo come opzione
> consigliata. Poi leggi quelle 30 domande da `domande_solo.jsonl` e rispondi.

**P2.0 — costruzione del retrieval** (una volta sola):

> Leggi la tabella «configurazione B» di `metodo_02_misurazione.md` e scrivimi lo script di
> retrieval che descrive. Deve leggere i file di `sources/` con la funzione `text_of` del
> §5-bis di `metodo_01_generazione_archivio.md`, spezzarli come indicato, indicizzarli, e per ogni
> domanda di `domande_solo.jsonl` recuperare gli 8 pezzi più vicini con il nome del file di
> origine.
>
> Salva lo script in `Desktop\misure_<progetto>\rag_retrieval.py`.
>
> Lo script, eseguito **una volta**, deve scrivere
> `Desktop\misure_<progetto>\misuraB_contesti.jsonl`: una riga JSON per domanda, con `id`,
> `domanda` e `passaggi` (lista di 8 oggetti con `file` e `testo`). Deve poter riprendere se
> interrotto: se il file esiste già, salta le domande già presenti.
>
> Non rispondere alle domande e non aprire nessun file di risposte o di valutazione: il tuo
> compito è solo costruire il recupero.
>
> Stampami alla fine il comando esatto per eseguirlo e quanto dura la prima indicizzazione.

**P2.1 — risposta, configurazione B** (blocchi di 30, senza accesso ai file):

> Rispondi alle domande seguenti usando esclusivamente i passaggi forniti per ciascuna.
>
> Per ogni domanda restituisci una riga JSON con: `id`, `risposta`, `fonti` (i file da cui
> provengono i passaggi che hai usato), `confidenza` (alta | media | bassa).
>
> Regole:
> - Se i passaggi non contengono il dato, rispondi che non è ricavabile. **Non integrare con
>   conoscenza tua**: puoi usare solo i passaggi di queste righe.
> - **Non aprire nessun altro file**, e in particolare nessun documento dell'archivio: il
>   solo file che puoi leggere è `misuraB_contesti.jsonl`.
> - Se i passaggi si contraddicono, riporta il conflitto invece di sceglierne uno.
> - Cita solo i file dei passaggi che hai effettivamente usato.
>
> **Salvataggio.** Scrivi in `Desktop\misure_<progetto>\misuraB_risposte.jsonl`, una riga
> per domanda, **in coda al file se esiste già**. Salta le domande già presenti. A fine
> blocco dimmi quante righe contiene.
>
> **Prima di cominciare, chiedimi con `AskUserQuestion` quale blocco elaborare.** Conta le
> righe gia' presenti in `misuraB_risposte.jsonl` e proponimi il blocco successivo come
> opzione consigliata. Poi leggi quelle 30 righe di `misuraB_contesti.jsonl` e rispondi
> usando i passaggi che ciascuna riga si porta dietro.

**P3 — valutazione** (20 giri: 10 per la misura A, 10 per la B):

> Valuti risposte date da un sistema documentale. Non devi rispondere alle domande: devi
> giudicare le risposte ricevute.
>
> Per ogni voce ti do: `id`, domanda, risposta attesa, criterio di valutazione, fonti
> corrette, risposta ricevuta, fonti citate.
>
> Assegna esattamente un esito:
> - `corretta` — soddisfa il criterio
> - `parziale` — dato giusto ma incompleto, o manca la contraddizione che andava segnalata
> - `sbagliata` — dato errato, ma ricavato da un documento reale
> - `allucinata` — dato inventato, **oppure** fonte citata che non contiene quel dato
>
> Restituisci una riga JSON per voce con: `id`, `misura` (A o B), `esito`,
> `fonti_corrette` (true/false), `motivazione` (una riga).
>
> Non essere generoso: se la risposta non contiene ciò che il criterio richiede, non è
> corretta anche se è ben scritta.
>
> **Salvataggio.** Scrivi in `Desktop\misure_<progetto>\valutazione.jsonl`, **in coda al
> file se esiste già**. A fine blocco dimmi quante righe contiene e quante per ciascun esito.
>
> **Prima di cominciare, chiedimi con `AskUserQuestion` due cose:** quale misura sto
> valutando (A o B) e quale blocco elaborare — contando le righe gia' presenti in
> `valutazione.jsonl` per quella misura e proponendomi il successivo come consigliato.
>
> Poi prendi quelle 30 voci: domanda, risposta attesa, criterio e fonti stanno in
> `eval_set.jsonl`; risposta ricevuta e fonti citate stanno nel file di risposte della
> misura indicata, accoppiate per `id`.

**P4 — metriche** (una volta sola):

> Leggi `Desktop\misure_<progetto>\valutazione.jsonl` e `eval_set.jsonl` (che contiene il
> campo `tipo` di ogni domanda) e calcolami le metriche, separatamente per la misura A e
> per la misura B.
>
> 1. **Tasso di allucinazione** — percentuale di esiti `allucinata` sulle sole domande di
>    tipo `non_rispondibile`.
> 2. **Riconoscimento dei conflitti** — percentuale di `corretta` sulle sole domande di tipo
>    `contraddizione`.
> 3. **Accuratezza per tipo** — percentuale di `corretta` (e separatamente di
>    `corretta + parziale`) per ciascun tipo, con in evidenza il divario fra `lookup` e
>    `multi_hop`.
> 4. **Precisione delle fonti** — percentuale di voci con `fonti_corrette: true`.
>
> Aggiungi il totale complessivo e il conteggio grezzo dei quattro esiti.
>
> Poi estraimi **cinque casi di fallimento commentati**: due allucinazioni, due conflitti
> non riconosciuti, un attraversamento fallito — con domanda, risposta data e perché è
> sbagliata.
>
> **Salvataggio.** Scrivi tutto in `Desktop\misure_<progetto>\metriche.md`, e in fondo
> mettimi la riga già formattata in markdown da incollare nella tabella dei risultati del
> README, nel formato:
> `| <misura> | <data> | <allucinazione>% | <conflitti>% | <lookup>% | <multi_hop>% | <fonti>% |`

### Cosa adattare al progetto, e cosa no

**Adatta**: il nome del progetto nei percorsi, il numero di domande e quindi di blocchi, il
nome del modello se nel frattempo è cambiato (e allora dichiaralo: il confronto con misure
precedenti decade).

**Non toccare**: le clausole di perimetro, l'istruzione di scrivere in append, il divieto in
P2.1 di aprire documenti dell'archivio, la richiesta di citare solo fonti realmente aperte,
la definizione dei quattro esiti, e l'istruzione di chiedere il blocco invece di riceverlo.
Sono le parti che rendono il numero credibile invece che gentile.

**E soprattutto**: nel documento che generi, i parametri delle due configurazioni non devono
mai diventare oggetto di domanda. L'agente che eseguira' la misura deve chiedere l'operativita'
— quale blocco, quale misura, quali percorsi — e mai la configurazione.

---

## Appendice A — prompt per gli agenti generatori

Un agente per blocco tematico (qualità, produzione, commerciale, HR, amministrazione,
logistica, rumore d'ufficio). Copia questo testo sostituendo le parti fra parentesi.

> Leggi `canone_aurora.md` (canone + registro delle contraddizioni) prima di scrivere: contiene anagrafica,
> persone con il loro registro linguistico, macchine, lotti, cronologia e il filo rosso.
> Ogni dato che riguarda quelle entità **deve** venire da lì, mai inventato.
>
> Scrivi in `sources/` i seguenti file: (elenco con nome esatto e formato).
> Non toccare nessun altro file. Non usare markdown.
>
> Regole: nomi di file come li scriverebbe un impiegato di fretta; ogni documento porta
> tracce di chi lo ha scritto (annotazioni, correzioni, campi in bianco, una firma
> mancante); numeri non tondi ma con i totali che restano la somma degli addendi; date
> verificate contro il calendario (1/1/(anno) è (giorno)); i codici devono superare i
> rispettivi algoritmi.
>
> Le contraddizioni che introduci **volutamente** vanno aggiunte a `contraddizioni.md`
> con: cosa diverge, in quali file, quale valore prevale e perché. Se non la registri,
> qualcuno la correggerà.
>
> Salva ogni 15 file e riporta a che punto sei. Lavora solo nella tua sottocartella per i
> file temporanei. Alla fine elenca i file prodotti e le contraddizioni registrate.

## Appendice B — briefing per i revisori

Ogni revisore prende un blocco di formati omogenei ([30] file circa), non un blocco
tematico: così legge con lo stesso strumento e non salta nulla.

> Leggi per primo `canone_aurora.md` (canone + registro delle contraddizioni).
>
> **L'archivio contiene contraddizioni volute: sono la cosa che il test misura, non
> difetti.** Il tuo compito è distinguerle da ciò che è sbagliato davvero.
>
> Blocco assegnato: (elenco). Leggili tutti dalla prima all'ultima riga. Le immagini
> guardale, non limitarti agli EXIF. Per i fogli apri ogni scheda, sia con le formule sia
> con i valori.
>
> Verifica **per calcolo, non a occhio**: checksum, aritmetica riga per riga, giorni della
> settimana, durate come fine meno inizio, somme dichiarate contro somme ricalcolate,
> riferimenti normativi esistenti e pertinenti, codici interni che esistono dove sono
> citati.
>
> Riporta in tre sezioni:
> **A. Errore vero** — nessun documento lo giustifica e il registro non lo dichiara. Per
> ognuno: file, posizione, testo esatto, perché è un errore, correzione proposta.
> **B. Contraddizione non registrata** — i due valori, i due file, quale dovrebbe
> prevalere e perché.
> **C. Falso allarme** — ciò che il registro dichiara, una riga ciascuno, per dimostrare
> che l'hai riconosciuto.
>
> Chiudi con «cosa ho verificato e risulta corretto», con i numeri che hai ricalcolato.
> Se non hai trovato errori veri in un blocco, dillo esplicitamente.
>
> Scrivi solo nella tua sottocartella. **Non modificare nessun file dell'archivio.**
> Salva risultati parziali ogni 15 file.

## Appendice C — sequenza operativa

L'ordine che ha funzionato, con i punti in cui è giusto fermarsi:

```
1  chiedi (§ regola d'ingaggio)                    → poi scrivi canone e contraddizioni
2  genera per blocchi, in parallelo                → agenti separati, cartelle separate
3  metadati → date                                 → primo giro completo
4  controlli automatici (§7)                       → codifica ogni difetto come test
5  revisione integrale (Appendice B)               → un revisore per blocco di formato
6  correggi, PROPAGA, riverifica                   → ogni correzione ne può rompere altre
7  ricontrolla con strumenti NUOVI                 → vedi sotto
8  genera il dataset sull'archivio finale (§9)
9  file di supporto con numeri ricontati (§10)
10 consegna (§12)                                  → poi baseline, poi canonizzazione
```

**Il passo 7 è quello che nessuno prevede e che vale più di tutti gli altri.** Quando i
controlli passano tutti, non hai finito: hai finito di misurare ciò che già sapevi di dover
misurare. Scrivi allora due o tre controlli con logica diversa da quelli che hai — cerca
tutti i codici che una regex trova invece di quelli che ti aspetti, scopri le relazioni fra
colonne invece di verificarle, confronta la data di ogni file con la sua ultima riga. In
questo progetto quel passo, eseguito quando 89 controlli erano verdi, ha trovato tre partite
IVA non valide dentro i file OCR, cinque registri più vecchi del loro contenuto e un difetto
che i controlli precedenti avevano dichiarato inesistente.

---

# Appendice D — promemoria personale

*Questa parte non è per l'agente: è per me, quando riaprirò il documento e non ricorderò
più nulla.*

## Cosa devo fare, in ordine, prima di canonizzare

I passi sono questi cinque. **Il come, con i prompt da copiare, sta in
`metodo_02_misurazione.md`**: qui tengo solo la sequenza, per ricordarmi l'ordine.

1. **Metto al sicuro le risposte** - la cartella di valutazione esce dal percorso di lavoro.
2. **Misura A** - Claude Code sull'archivio, dieci giri da trenta domande.
3. **Misura B** - un solo script costruisce il recupero, poi dieci giri di risposte sui
   passaggi che lo script ha estratto. La risposta la scrive comunque lo stesso modello:
   cosi' l'unica differenza fra i due numeri e' *come sono stati trovati i documenti*.
4. **Valuto** - terza sessione, che non e' quella che ha risposto.
5. **Scrivo i numeri** nella tabella del README. Due righe su quattro.

**Poi, e solo poi, canonizzo.**

## Perché mi serve, nel tempo

**Per me.** Il second brain personale è questo: appunti, contratti, note di chiamata,
interrogabili invece che ricordati. Vale da subito e cresce con me.

**Per i clienti.** È il prodotto che venderò. Una PMI di trenta persone ha migliaia di
documenti e nessuno che sappia dove sono: il capo officina che cerca la scheda tecnica di
due anni fa è tempo pagato a vuoto, ogni settimana. Un archivio interrogabile è vendibile
perché il problema lo sentono già, senza che glielo spieghi io.

**E qui c'è la cosa che vale davvero.** Montare un sistema del genere è un pomeriggio: di
tutorial ne è pieno il mondo. Ma quando un titolare chiede «e funziona?», la risposta
normale è «provalo». La mia è un numero, misurato su domande verificate una per una, con
accanto quante volte il sistema inventa quando la risposta non c'è.

Quello che ho costruito qui non è un archivio finto. È **un metro**. L'archivio serviva a
tararlo.

**Quanto dura davvero.** Non è un pomeriggio. Su un archivio da [160] file l'ordine di
grandezza è **otto-dieci sessioni di lavoro**, distribuite così:

| Passi | Sessioni | Nota |
|---|---|---|
| 1 — domande e canone | 1, breve | è la mezz'ora che ne fa risparmiare due giorni |
| 2 — generazione | 2-3, lunghe | agenti in parallelo; mettine in conto uno che si interrompe |
| 3-4 — metadati, date, controlli | 1 | qui nascono gli script che riuserai per sempre |
| 5 — revisione integrale | 1 + attesa | ogni revisore impiega 20-40 minuti sul suo blocco |
| 6-7 — correzioni e strumenti nuovi | 1-2 | la fase più lunga: ogni correzione va propagata |
| 8-9 — dataset e file di supporto | 1-2 | la verifica severa scarta il 10% delle domande |
| 10 — baseline | 1 per configurazione, + 1 per la valutazione | |

Se hai un limite di crediti o di durata di sessione, **scrivi lo stato su disco a ogni
passo** — un file con cosa è fatto, cosa manca, quali difetti sono aperti. Riaprire una
sessione e ritrovare il punto esatto vale più di qualunque ottimizzazione.
