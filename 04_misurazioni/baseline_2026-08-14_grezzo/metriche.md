# Metriche di valutazione — misura A vs misura B

**Data:** 14/08/2026
**Fonti:** `valutazione.jsonl` (564 righe), `eval_set.jsonl` (282 domande), risposte in
`misuraA_risposte.jsonl` + `misuraA.1_risposte.jsonl` (210+72 = 282) e `misuraB_risposte.jsonl` (282).

**Integrità dei dati:** 282 id per misura, nessun duplicato, nessun id mancante o estraneo su
entrambe le misure. Nessuna riga malformata.

---

## ⚠️ Una nota sulla metrica 1, prima dei numeri

**Il campo `esito` non contiene il valore `allucinata`.** I soli valori presenti in tutte e 564 le
righe sono `corretta`, `parziale`, `sbagliata`. Il tasso di allucinazione non è quindi calcolabile
come richiesto senza una convenzione, e la convenzione l'ho scelta così — dichiarandola:

> **Allucinazione = esito `sbagliata` su domanda di tipo `non_rispondibile`**, cioè il sistema non
> si è astenuto e ha asserito qualcosa di falso.

È la lettura più stretta e più fedele all'intento. Le `parziale` su `non_rispondibile` **non** sono
allucinazioni: verificate una per una, tutte e 10 (4 in A, 6 in B) arrivano alla conclusione giusta
— «il dato non c'è» — e sono declassate solo per la motivazione incompleta o per un riferimento
mancante. Nessuna di esse inventa un dato.

Sotto questa definizione il risultato è netto, e va letto con la riserva che segue: **A = 3,2%
(1 caso su 31), B = 0,0% (0 su 31).** L'unico caso di A, per giunta, non è un'invenzione ma una
**falsa negazione** (nega un fatto documentato). Con 31 domande per misura, la differenza fra 1 e 0
casi non è un divario misurabile: entrambe le misure si astengono bene, e su questo asse sono
sostanzialmente pari. **Il vero fallimento non è l'invenzione, è altrove** — lo dicono le metriche 3 e 4.

---

## 1. Tasso di allucinazione — tipo `non_rispondibile` (n = 31 per misura)

| Misura | corretta | parziale | sbagliata | **Tasso di allucinazione** | Astensione corretta |
|---|---|---|---|---|---|
| **A** | 26 | 4 | 1 | **3,2%** | 83,9% |
| **B** | 25 | 6 | 0 | **0,0%** | 80,6% |

Se si contasse come fallimento qualunque esito non `corretta` (metrica più severa e a mio parere
meno onesta, perché punisce motivazioni imprecise su conclusioni giuste): A = 16,1%, B = 19,4%.

**L'astensione è la cosa che entrambe le misure fanno meglio di tutto il resto.** In B è l'unico
tipo che chiude al 100% di `corretta + parziale`.

## 2. Riconoscimento dei conflitti — tipo `contraddizione` (n = 14 per misura)

| Misura | corretta | parziale | sbagliata | **% corretta** | % corretta + parziale |
|---|---|---|---|---|---|
| **A** | 7 | 4 | 3 | **50,0%** | 78,6% |
| **B** | 8 | 3 | 3 | **57,1%** | 78,6% |

**È l'unico tipo in cui B batte A** (+7,1 punti), ed è anche il tipo in cui A è più debole rispetto
alla sua media. Con n = 14 il vantaggio di B vale una domanda sola: non è un divario, è un pareggio.
Il dato che conta è un altro: **su metà delle contraddizioni nessuna delle due misure vede il
conflitto**, e i tre fallimenti duri (Q233/Q235, Q241, Q242) sono in gran parte gli stessi.

## 3. Accuratezza per tipo

### Misura A

| Tipo | n | corretta | corretta + parziale | c / p / s |
|---|---|---|---|---|
| **lookup** | 86 | **82,6%** | 93,0% | 71 / 9 / 6 |
| **multi_hop** | 74 | **52,7%** | 81,1% | 39 / 21 / 14 |
| aggregazione | 28 | 67,9% | 82,1% | 19 / 4 / 5 |
| calcolo | 24 | 79,2% | 91,7% | 19 / 3 / 2 |
| temporale | 18 | 83,3% | 100,0% | 15 / 3 / 0 |
| contraddizione | 14 | 50,0% | 78,6% | 7 / 4 / 3 |
| metadato | 7 | 42,9% | 71,4% | 3 / 2 / 2 |
| non_rispondibile | 31 | 83,9% | 96,8% | 26 / 4 / 1 |

### Misura B

| Tipo | n | corretta | corretta + parziale | c / p / s |
|---|---|---|---|---|
| **lookup** | 86 | **61,6%** | 79,1% | 53 / 15 / 18 |
| **multi_hop** | 74 | **31,1%** | 68,9% | 23 / 28 / 23 |
| aggregazione | 28 | 10,7% | 25,0% | 3 / 4 / 21 |
| calcolo | 24 | 37,5% | 75,0% | 9 / 9 / 6 |
| temporale | 18 | 27,8% | 77,8% | 5 / 9 / 4 |
| contraddizione | 14 | 57,1% | 78,6% | 8 / 3 / 3 |
| metadato | 7 | 0,0% | 42,9% | 0 / 3 / 4 |
| non_rispondibile | 31 | 80,6% | 100,0% | 25 / 6 / 0 |

### Il divario lookup → multi_hop

| Misura | lookup | multi_hop | **divario** | divario su corretta + parziale |
|---|---|---|---|---|
| **A** | 82,6% | 52,7% | **−29,9 pt** | −11,9 pt |
| **B** | 61,6% | 31,1% | **−30,5 pt** | −10,2 pt |

**Il divario è identico nelle due misure (~30 punti) e non dipende dal recupero.** È il risultato
più solido di tutta la valutazione: qualunque cosa cambi fra A e B, il costo di attraversare più di
un documento resta lo stesso. Il crollo, però, è quasi tutto da `corretta` a `parziale`, non a
`sbagliata` (il divario si dimezza a ~11 punti sulla metrica permissiva): sui multi-hop il sistema
**arriva quasi in fondo e si ferma a un hop dalla risposta** — trova il primo documento, manca
l'ultimo collegamento. Non sbaglia strada, si ferma prima.

### Il confronto A vs B, tipo per tipo (su `corretta`)

| Tipo | A | B | Δ (B − A) |
|---|---|---|---|
| lookup | 82,6% | 61,6% | −21,0 |
| multi_hop | 52,7% | 31,1% | −21,6 |
| **aggregazione** | 67,9% | 10,7% | **−57,2** |
| **temporale** | 83,3% | 27,8% | **−55,5** |
| **metadato** | 42,9% | 0,0% | **−42,9** |
| calcolo | 79,2% | 37,5% | −41,7 |
| contraddizione | 50,0% | 57,1% | **+7,1** |
| non_rispondibile | 83,9% | 80,6% | −3,3 |

⚠️ **B collassa dove la risposta richiede di vedere tutte le righe insieme** — aggregazione
(10,7%), metadato (0,0%), temporale (27,8%). La motivazione ricorrente nelle sue valutazioni è
letteralmente «recupero fallito»: il retrieval a chunk consegna qualche riga, non l'insieme, e su una
domanda che chiede *quante* o *quali tutte* qualche riga vale zero. Su `metadato` B non prende un
solo punto pieno su 7.

## 4. Precisione delle fonti (`fonti_corrette: true`)

| Misura | totale | lookup | multi_hop | aggregaz. | calcolo | temporale | contraddiz. | metadato | non_risp. |
|---|---|---|---|---|---|---|---|---|---|
| **A** | **91,8%** (259/282) | 90,7% | 93,2% | 85,7% | 91,7% | 100,0% | 92,9% | 57,1% | 100,0% |
| **B** | **80,5%** (227/282) | 76,7% | 86,5% | 71,4% | 70,8% | 83,3% | 92,9% | 14,3% | 100,0% |

**Le fonti sono sistematicamente più affidabili della risposta.** A cita bene nel 91,8% dei casi
ma risponde bene nel 70,6%; B cita bene nell'80,5% e risponde bene nel 44,7%. In B lo scarto è di
36 punti: **trova il documento giusto e poi sbaglia lo stesso la risposta** — il che sposta il
sospetto dal recupero all'estrazione, almeno per la parte di errori che non sono «recupero fallito».
Su `non_rispondibile` la precisione è 100% in entrambe (non citare nulla è banalmente corretto).

## Totale complessivo e conteggio grezzo

| Misura | n | corretta | parziale | sbagliata | % corretta | % corretta + parziale | % sbagliata |
|---|---|---|---|---|---|---|---|
| **A** | 282 | **199** | 50 | 33 | **70,6%** | 88,3% | 11,7% |
| **B** | 282 | **126** | 77 | 79 | **44,7%** | 72,0% | 28,0% |
| **Totale** | 564 | 325 | 127 | 112 | 57,6% | 80,1% | 19,9% |

**A vince di 25,9 punti sulla metrica stretta e di 16,3 su quella permissiva.** B ha più che
raddoppiato le risposte sbagliate (79 contro 33).

⚠️ **Un avvertimento sul confronto, e non è un dettaglio.** Le motivazioni dei fallimenti di A e di
B descrivono due patologie diverse e non direttamente confrontabili:

- **A fallisce sui formati binari.** «`.xlsx` binario», «`.docx` binario» compare in gran parte
  delle sue valutazioni negative — Q008, Q032, Q039, Q053, Q088, Q101, Q107, Q114, Q132, Q161,
  Q165, Q179, Q188, Q192, Q198, Q203, Q213, Q216, Q217, Q220, Q224, Q227, Q242, Q259. **A non
  legge Excel e Word.** Dove i documenti sono testuali, va forte.
- **B fallisce sul recupero.** «Recupero fallito» è la formula ricorrente: legge i formati, ma il
  chunk giusto non arriva in contesto.

Quindi **il 70,6% di A non è la sua accuratezza sul corpus reale, è la sua accuratezza sul
sottoinsieme testuale** — con un errore quasi automatico su ogni domanda che tocca un foglio di
calcolo. Se il confronto serve a scegliere un'architettura, va rifatto su A con un estrattore
per binari, altrimenti si sta misurando un parser mancante, non un metodo di recupero.

---

# Cinque casi di fallimento, commentati

## Allucinazione 1 — A / **Q259** (`non_rispondibile`, difficoltà 4)

**Domanda:** *UniCredit ha concesso l'ampliamento dell'anticipo fatture a 500.000 euro?*

**Risposta data (misura A, confidenza `alta`):**
> «Non ricavabile, e **nessun documento menziona una richiesta di ampliamento a 500.000 euro**. Il
> plafond documentato è 400.000, come dichiarano sia Trentin in riunione sia il titolare […]»

**Perché è sbagliata.** La risposta attesa è che **la richiesta esiste ed è documentata** — il
previsionale di cassa riporta l'annotazione di Trentin «chiesto a UniCredit ampliamento anticipo a
500.000. Risposta attesa entro il 20/06» — e che manca solo **l'esito**. A non ha potuto leggere il
previsionale perché è `.xlsx` binario, e ha trasformato «non lo vedo» in «non esiste», con
**confidenza alta**. È l'errore più insidioso della serie: le note di valutazione avvertivano che
«inventare un esito è l'errore tipico», e A ha fatto il contrario — ha negato la premessa. Un
utente che legge questa risposta chiude la pratica invece di sollecitare la banca il 20/06.
**È l'unico fallimento su 31 non-rispondibili, e non è un'invenzione: è un falso negativo prodotto
da un file non letto.**

## Allucinazione 2 — A / **Q127** (`calcolo`, difficoltà 3)

**Domanda:** *Quanto vale l'IVA sulla bolletta della luce di marzo e come si arriva al totale?*

**Risposta data (misura A, confidenza `media`):**
> «IVA **4.863,00** su imponibile **22.104,55**, totale 26.967,55 (Veneta Energia V26/01544,
> energia marzo). **Verificato: 22.104,55 × 0,22 = 4.863,00, quindi 22%.** […] sulle bollette
> energia lo scadenzario RIBA e la fattura elettronica di marzo applicano IVA al 10% […] Le due
> aliquote non sono conciliabili.»

**Perché è sbagliata.** I numeri veri sono imponibile **25.854,65**, IVA al **10%** = **2.585,47**,
totale **28.440,12**, fattura Veneta Energia n. 2026-EE-1188041, con l'addebito riscontrabile
sull'estratto conto. A ha preso **un documento diverso** (un riepilogo costi, per giunta in un
blocco che il file stesso segnala come corrotto — «colonne saltate, sistemare») e ci ha costruito
sopra **una verifica aritmetica che torna**: 22.104,55 × 0,22 fa davvero 4.863,00. È il meccanismo
tipico dell'allucinazione plausibile — **il calcolo è corretto, la premessa è di un'altra bolletta**
— e il ricalcolo autoprodotto fa da conferma apparente. Che poi la risposta segnali da sé
l'esistenza di un'aliquota al 10% inconciliabile rende il caso peggiore, non migliore: aveva in mano
l'indizio del proprio errore e ha tenuto il numero sbagliato.

## Conflitto non riconosciuto 1 — A / **Q241** (`contraddizione`, difficoltà 5)

**Domanda:** *Quali sono le dimensioni di ingombro del tunnel Criotech CR-SP180?*

**Risposta data (misura A, confidenza `media`):**
> «8,4 × 6,2 m di pianta e 4,9 m di altezza […] con altezza sottotrave della sala Linea 3 misurata
> in 5,35 m e **giudicata "ok con margine"**. È **l'unica fonte leggibile** che riporta le quote:
> il preventivo PDF documenta capacità 1.800 kg/h […] ma non l'ingombro.»

**Perché è sbagliata.** Le fonti sono **due e discordi**: l'offerta del costruttore indica
**13.400 × 8.200 × h 6.100 mm**, la mail di Fantin dice 8,4 × 6,2 × 4,9 m. Con i 6.100 mm
dell'offerta **l'impianto non passa sotto i 5,35 m di sottotrave**: il conflitto è un rischio di
progetto aperto, e la nota di valutazione lo dice esplicitamente — «un sistema che cita solo una
delle due misure non ha visto il problema». A cita una fonte sola, dichiara l'altra priva del dato,
ed **eredita da Fantin il giudizio di compatibilità**, trasformando un rischio non risolto in un via
libera. La confidenza `media` non basta a segnalarlo. **Fallimento da 250.000 € potenziali: si
scopre in fase di montaggio.**

## Conflitto non riconosciuto 2 — B / **Q242** (`contraddizione`, difficoltà 5)

**Domanda:** *In quali domeniche di maggio 2026 ha lavorato la Linea 2?*

**Risposta data (misura B, confidenza `alta`):**
> «Domeniche **3, 10 e 17 maggio 2026**. Il dato è affermato due volte nel verbale della
> contestazione sindacale […] Il piano di produzione conferma direttamente due di quelle tre date […]
> per il 3 maggio non c'è riga di piano. Da segnalare una nota che sembra contare diversamente:
> nell'estratto del libro unico Trentin scrive che "il costo del mese è sopra la media per via delle
> **due** domeniche" — riferimento a due sole domeniche, non tre, **che i passaggi non riconciliano**.»

**Perché è sbagliata.** Le domeniche lavorate sono **due, 10 e 17**; la terza (24/05) era programmata
e sospesa. Il **libro unico** — il documento con le ore individuali autorizzate, e quindi la fonte
che prevale — lo dice esplicitamente, e i cedolini lo confermano con 16 ore di straordinario festivo,
cioè due giornate da otto. Il verbale sindacale **si contraddice al proprio interno**: ordine del
giorno «3, 10 e 17», corpo del punto 2 «10 e 17, con la terza programmata il 24». B ha letto solo
l'intestazione del verbale e l'ha presa per buona due volte.

⚠️ **Il punto interessante è che B aveva già in mano tutti gli elementi per risolverlo**: si accorge
che il 3 maggio non ha riga di piano, cita la nota di Trentin sulle «due domeniche», e chiude
scrivendo che «i passaggi non riconciliano» — poi **tiene la risposta a tre e la marca confidenza
alta**. Non è un problema di recupero: è che il conflitto viene rilevato e non pesato. Manca la
regola «fra due fonti discordi prevale quella con valore probatorio», che qui avrebbe dato la
risposta giusta. **Lo stesso errore lo fa A** su Q242, per la ragione opposta (libro unico `.xlsx`
non letto): due strade diverse, identico risultato sbagliato.

## Attraversamento fallito — A / **Q217** (`multi_hop`, difficoltà 4)

**Domanda:** *Sullo snack multicereali esiste un rischio di contaminazione da sesamo?*

**Risposta data (misura A, confidenza `alta`):**
> «**Sullo snack in produzione no**: la ricetta dice "AF-SN-0450 NON ha sesamo". Il sesamo entra nel
> prototipo AF-SN-0470 v12 all'8% del peso […] Misure: 250 kg in area segregata (B-04-04), consegna
> separata, regola "sesamo SOLO in laboratorio". Precedente reale: NC-2026-055 del 25/03, sesamo
> lavorato in pilota senza segregazione completa, gravità alta […] Le due referenze insistono sulla
> stessa Linea 1 e **la matrice allergeni è binaria**.»

**Perché è sbagliata.** La risposta è **sì, da aprile 2026**: nella **matrice allergeni rev. 6 del
21/04/2026** l'AF-SN-0450 e l'AF-SN-0455 hanno il sesamo classificato **PC (può contenere)**, proprio
perché sono partite le prove del prototipo AF-SN-0470 sulla stessa linea.

**È l'anatomia esatta del fallimento multi-hop, ed è il caso più istruttivo dei cinque.** A percorre
i primi tre hop **correttamente** — trova il prototipo, ne quantifica il sesamo all'8%, individua
la NC-2026-055 come precedente reale di contaminazione, e nota da sé che *le due referenze insistono
sulla stessa Linea 1*. Poi manca **l'ultimo hop**, la matrice allergeni rev. 6, perché è `.docx`
binaria — e invece di sospendere il giudizio **conclude in negativo**, con confidenza alta, su una
domanda di sicurezza alimentare. Il sistema si è portato fino a un centimetro dalla conclusione e ha
poi affermato il contrario di ciò che i suoi stessi indizi suggerivano.

Vale la pena notare che il fallimento è **doppio**: al dato mancante si somma la scelta di
rispondere «no» invece di «non concludibile» — la stessa scelta di Q259. **Quando A non riesce a
leggere un file, non si astiene: nega.** È il pattern di rischio più serio emerso dalla misura A, e
riguarda il comportamento in caso di dato mancante più del parser.

---

## Riga per la tabella dei risultati del README

```
| A | 14/08/2026 | 3.2% | 50.0% | 82.6% | 52.7% | 91.8% |
| B | 14/08/2026 | 0.0% | 57.1% | 61.6% | 31.1% | 80.5% |
```

Legenda delle colonne: misura · data · tasso di allucinazione (`sbagliata` su `non_rispondibile`) ·
riconoscimento conflitti (`corretta` su `contraddizione`) · accuratezza `lookup` (`corretta`) ·
accuratezza `multi_hop` (`corretta`) · precisione fonti (`fonti_corrette: true` sul totale).
