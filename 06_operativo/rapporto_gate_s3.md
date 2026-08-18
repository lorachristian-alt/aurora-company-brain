# Rapporto di gate — Sessione 3: pipeline RAG di produzione e baseline C

**Al titolare, che lo porta al coordinatore.** 18/08/2026.
Verbale completo: `04_misurazioni/baseline_c_2026-08-17_grezzo/verbale_baseline_c.md`
(chiuso). Ogni numero qui sotto è ricontato da script dai jsonl; nessuno è trascritto dal
rapporto del giudice.

---

## In una riga

**La pipeline è costruita, congelata, misurata e documentata; il numero è basso e la
causa è identificata: il generatore, non il recupero.**

---

## 1. Il numero, e si cita sempre doppio

> ## **14,5% corrette sulle 282 · 7,6% sulle 251 rispondibili**

Delle 41 corrette, **22 vengono da domande la cui risposta giusta è «il dato non c'è»**, e
il modello ci arriva perché **si astiene sempre** — non perché sappia distinguere. Lo
stesso riflesso produce decine di astensioni false su domande a cui una risposta esisteva.

⚠️ **Chi riporta il 14,5% senza il 7,6% racconta una capacità che il sistema non ha.**

| Esito | A — agentico | B — RAG semplice | C — RAG produzione |
|---|---:|---:|---:|
| corretta | 199 (70,6%) | 126 (44,7%) | **41 (14,5%)** |
| parziale | 50 (17,7%) | 77 (27,3%) | 75 (26,6%) |
| sbagliata | 33 (11,7%) | 79 (28,0%) | 141 (50,0%) |
| allucinata | 0 | 0 | 25 (8,9%) |
| fonti corrette | 259 (91,8%) | 227 (80,5%) | 198 (70,2%) |
| **corrette sulle 251 rispondibili** | 68,9% | 40,2% | **7,6%** |

**C è ultima su ogni riga, e di molto.** Non c'è modo di addolcirlo e non si prova.

---

## 2. Cosa è stato costruito

Una pipeline RAG ibrida interamente locale, eseguibile da riga di comando, con traccia di
audit per ogni interrogazione:

```
ingestione 11 formati (OCR compreso, con cache)
  -> Qdrant, una collezione, denso bge-m3 + sparso BM25 scritto a mano
  -> RRF calcolata in Python (per poterla tracciare)
  -> cross-encoder bge-reranker-v2-m3
  -> llama3.2:3b via Ollama, temperatura 0
  -> traccia di audit completa
```

Più: `docker-compose.yml` per la produzione, `requirements.txt` pinnate, runbook per 1-2
figure IT, e cinque script che ricontano (verifica corpus, verifica run, conteggi, metriche).

**Numeri di costruzione, tutti da script:** corpus 160/160 contro il manifest · 1.902
chunk · indice 1.902 punti · BM25 25.541 termini · collaudo 8/9 attesi consegnati, 9/9
nella fusione · tutti e 11 i formati raggiungibili.

---

## 3. Le tre cose che rendono questa misura credibile

**1. La pre-registrazione è reale e verificabile.** Config scritta, committata e
**pushata** (`d36d7ce`, 17/08 ore 12:44) *prima* che l'indice esistesse e *prima* di
vedere un solo risultato. L'impronta `afb58939…` è dentro il manifest dell'indice e dentro
ognuna delle 282 tracce.

**2. Il meccanismo di congelamento ha funzionato su di me.** Durante la costruzione stavo
per aggiungere al config un'avvertenza — di solo commento. L'impronta sarebbe cambiata e
l'indice si sarebbe rifiutato di riprendere. Revocato, `git diff` a zero. Da lì la regola
scritta in `metodo_04`: **la prosa si corregge, il config no.**

**3. Estrazione identica a B, provata da un conteggio indipendente.** L'ingestione ha
prodotto **1.897 chunk `nativa` — esattamente i 1.897 della configurazione B**. La
differenza fra le due misure è l'architettura, non l'estrattore.

---

## 4. Dove C batte B, e dove no

**Dove no: ovunque, sul risultato.** 14,5% contro 44,7%; quattro tipi su otto a zero
(`aggregazione`, `temporale`, `contraddizione`, `metadato`).

**⚠️ Ma il confronto C/B misura i generatori, non le architetture,** e va detto ogni volta:
B scrive con `claude-opus-5`, C con un 3B quantizzato su un portatile da 8 GB. Per
confrontare le architetture servirebbe C con lo stesso modello di B — **non è stato
fatto**, e finché non si fa nessuno può dire quale architettura sia migliore.

**Dove C mostra un vantaggio misurabile — sul recupero, non sulla risposta:**

| | |
|---|---:|
| Passaggi consegnati che vengono **solo dal ramo BM25** | **22,6%** |
| solo dal ramo denso | 30,3% |
| da entrambi | 47,1% |

**Quasi un quarto di ciò che il generatore ha visto era invisibile alla ricerca
semantica.** È la giustificazione quantitativa dell'ibrido, misurata su questo archivio.
B, che ha solo il ramo denso, quel 22,6% non lo vedrebbe mai.

**Un numero che sembra un merito e non lo è:** il divario `lookup`/`multi_hop` è 14,7
punti in C contro ~30 in A e B. Non significa che C attraversi meglio: parte da 17,4% e
non ha spazio per cadere. Effetto pavimento.

---

## 5. Cosa il run ha insegnato

### 5.1 Il collo di bottiglia è il generatore — ed è il risultato più utile

| | |
|---|---:|
| Risposte che citano il documento **giusto** | 198/282 = **70,2%** |
| Risposte **corrette** | 41/282 = **14,5%** |
| **Scarto** | **55,7 punti** |

Nel 70% dei casi il sistema **aveva il documento in mano e ha sbagliato lo stesso**. In
decine di casi la risposta **nega un dato che sta nel file che sta citando**: Q089
(«non determinabile» un conteggio che il file scrive come `TOTALE SCADUTI: 17`), Q170
(non sa dire chi guidi senza abilitazione citando il registro che scrive «NON ABILITATO
ALLA GUIDA»), Q209 (rifiuta di rispondere perché il dato è espresso come «circa»).

**Conseguenza: sostituire il generatore lasciando la pipeline invariata è l'unico
intervento che può spostare questi numeri.**

### 5.2 Il rischio dominante non è quello atteso

**Non le 25 allucinazioni: le 75 `parziale`** — più di una risposta su quattro, il triplo
delle allucinazioni. Sono sì/no giusti e nudi: «Sì, era già stato contestato», «No, non
aveva la formazione HACCP». **Vere e inutilizzabili**: nessuna data, nessun codice,
nessun importo. Chi legge non ha nulla da verificare.

**E sulle contraddizioni diventa sistematico: 14 domande, 11 `parziale`, zero corrette.**
Il modello dà il valore giusto e non si accorge mai che nell'archivio ne esiste un altro.
Q241 dà le dimensioni del tunnel senza vedere che con quell'altezza l'impianto non passa
sotto la trave: un rischio di progetto da 290.000 €.

> **Per un'azienda alimentare è il difetto peggiore.** Un sistema che consegna un numero
> verificabile e tace che il dato è contestato **chiude un'indagine che andava aperta**.
> È più pericoloso di uno che si astiene. A ne riconosce metà, B poco più, **C nessuna**.

### 5.3 Un'allucinazione da segnalare come rischio-tipo

**Q193 e Q265: una fattura Pakmatic da 4.912 €, numero inesistente, identico in due punti
del giro.** È riproducibile (temperatura 0), plausibile, e **coerente con sé stesso**: chi
incrociasse le due risposte troverebbe una conferma. Davanti a un auditor è lo scenario
peggiore — un errore evidente si scarta, un numero inventato coerente entra nel verbale.

⚠️ **È anche la prova migliore dell'argomento che vendiamo:** si apre la traccia e si vede
in trenta secondi che 4.912 non c'è. **Si vende la tracciabilità, non la correttezza.**

### 5.4 La resilienza è stata collaudata sul campo, per caso

La finestra del terminale si è chiusa **durante** la passata 2. Il runner girava staccato
dalla shell: ha finito da solo. Continuità dimostrata — un solo avvio nel log, una sola
riga di rapporto, e fine meno durata = lancio a **21 secondi di scarto**.

---

## 6. Cosa NON è stato fatto, deliberatamente

| Non fatto | Perché |
|---|---|
| Corretti i guasti di formato (risposta vuota, segnaposto, loop, fonti esplose) | fra «prima» e «dopo» cambia **solo la forma dell'archivio**, i bug dello strumento compresi. Un runner migliorato produrrebbe un delta che mescola due cause. Sono materiale per la config di riferimento, **dopo** la Sessione 6 |
| Corretto il difetto padrone/derivato del retrieval | idem — ed è anzi la previsione più falsificabile che consegniamo alla S6 |
| Misurata la configurazione di riferimento (8B) | non c'è l'hardware. **E non si racconta come se fosse stata misurata** |
| Costruito il connettore Notion | nel corpus v1 non c'è contenuto Notion: sarebbe codice non esercitato. Documentato come punto di estensione |

---

## 7. Proposte per la Sessione 6

| Proposta | Perché |
|---|---|
| C «dopo» gira su **questo config, byte per byte** | vincolo del metodo; `AURORA_LOCALE` dà l'indice nuovo, cambia solo `--corpus` |
| Riusare la **cache di estrazione** | garantisce testo identico anche se tesseract cambia |
| Scrivere in `predizioni.md`: guadagno atteso su **`contraddizione` e `multi_hop`** | sono i tipi che la canonizzazione tocca: la nota-conflitto rende esplicita la divergenza che C non vede mai |
| Attendersi **poco** su `aggregazione` e `calcolo` | dipendono dal saper contare: è il generatore. Un balzo lì sarebbe da indagare, non da festeggiare |
| Verificare se il difetto **padrone/derivato** sparisce | previsione netta e falsificabile |
| ⚠️ **Decidere prima** come conta `fonti_corrette` se la risposta cita una nota del vault | aperta dal 16/08 e ancora non decisa. Proposta: **la fonte che conta resta il grezzo** |
| ⚠️ **Fissare prima** la definizione del tasso di allucinazione | il giudice del 14/08 non usò mai `allucinata`; quello di C sì. Proposta: **`allucinata + sbagliata` su `non_rispondibile`**, che dove il campo è vuoto coincide col ripiego e **lascia A e B invariate** |

---

## 8. Le decisioni che chiedono approvazione

1. **Chiudere la Sessione 3** e la baseline C così com'è.
2. **Adottare la riga README** con la definizione conciliante del tasso di allucinazione:
   ```
   | Baseline — grezzo, RAG Advanced (C) | 17/08/2026 | 19.4% | 0.0% | 17.4% | 2.7% | 70.2% |
   ```
   Con questa scelta **le righe A e B non cambiano di una cifra**.
3. **Confermare che nulla della config C si tocca** fino a Sessione 6 conclusa, difetti di
   formato compresi.
4. **Registrare nel decision log** la voce del titolare del 17/08: *il vault sotto git
   privato slitta a fine progetto, prima della v2*.

---

## 9. Domanda aperta per il coordinatore

**La configurazione C così com'è non è vendibile, e il verbale lo dice.** Ma la misura ha
prodotto l'informazione che serviva: **il recupero funziona, la scrittura no**, e la leva
è una sola. Le opzioni, in ordine di costo:

1. **Misurare la config di riferimento (8B) su hardware adeguato** — chiude la domanda «di
   quanto migliora». Costo: una macchina che qui non c'è.
2. **Aspettare la Sessione 6** — dice quanto vale la canonizzazione a strumento invariato,
   che è la domanda originale del progetto. Costo: zero, è già in piano.
3. **Entrambe, in quest'ordine**: prima la 6 (una variabile alla volta), poi l'8B.

⚠️ La 3 è l'unica che non rompe il principio «una variabile alla volta». Cambiare
generatore *e* forma dell'archivio insieme renderebbe illeggibile il delta di tutte e sei
le sessioni precedenti.
