# Verbale della mini-misura di fumo — Sessione 2, fetta pilota L26130

⚠️ **NUMERI NON UFFICIALI.** Non entrano nel README, non sostituiscono la misura «dopo»
delle Sessioni 6-7 e non sono confrontabili con esse. Servono a una domanda sola: **il
design della canonizzazione regge su una fetta?**

**Data di esecuzione:** 16/08/2026 · **Perimetro misurato:** vault `aurora-cervello`,
esclusa `.obsidian\` · **Domande:** 30, selezionate da `prepara_fumo.py` come quelle le cui
fonti attese ricadono tutte dentro la fetta.

---

## Condizioni della misura

| | |
|---|---|
| **Modello del rispondente** | **`claude-opus-5`** |
| **Modello della baseline A** (14/08/2026) | **`claude-opus-5`** — **stesso modello**: il confronto non è inquinato dal cambio di modello |
| **Blocchi** | **un solo blocco da 30 domande**, senza suddivisione |
| **Perimetro del rispondente** | radice sul vault, `--add-dir` solo su `04_misurazioni\`; canone ed eval set **fisicamente fuori** dal filesystem montato |
| **Giudice** | sessione separata, con accesso a `03_valutazione\`; non è chi ha risposto |

⚠️ **Due asimmetrie rispetto alla baseline, entrambe a favore della fumo, da dichiarare
ogni volta che questi numeri si citano.**

1. **Un blocco solo contro dieci.** Il P1 della baseline ha girato dieci volte su 282
   domande, e il verbale di metodo_02 documenta un degrado dei tempi per blocco da 7m 23s a
   31m 30s dovuto al costo di riemettere il file di output. La fumo non ha questo effetto.
2. **Trenta domande su duecentottantadue.** Una differenza di due o tre esiti non è
   significativa. Il campione dice se il design regge, non quanto rende.

---

## Esiti — ricontati da `06_operativo\qa\conta_fumo.py`

| Esito | Fumo (vault canonizzato) | Baseline A (corpus grezzo), stessi 30 id | Delta |
|---|---|---|---|
| corretta | **28** (93,3%) | 23 (76,7%) | **+5** |
| parziale | 2 (6,7%) | 6 (20,0%) | −4 |
| sbagliata | 0 (0%) | 1 (3,3%) | −1 |
| allucinata | 0 | 0 | 0 |
| **fonti corrette** | **30/30** | 27/30 | **+3** |

**5 migliorati · 0 peggiorati · 25 invariati.** Tutti e 30 gli id della fumo sono presenti
anche nella baseline A: nessuna esclusione dal confronto.

### I cinque migliorati

| id | Baseline A | Fumo | Cosa è cambiato |
|---|---|---|---|
| **Q074** | parziale | corretta | riporta insieme il «detectabile: no credo» dell'officina e il materiale dichiarato genericamente |
| **Q132** | sbagliata | corretta | il lotto L26131 quadra (7.620 contro 4.260+980+2.380+0) e viene tenuto distinto dal L26130, che non quadra |
| **Q138** | parziale | corretta | 24 min 30 s contati sulle righe del log, riportando anche i 27 min del riepilogo |
| **Q199** | parziale | corretta | collega la dimensione oltre i 7 mm e i bordi netti al rischio di lesione e alla procedura di classificazione |
| **Q238** | parziale | corretta | distingue i due canali invece di sceglierne uno: 68,9 al cuore e 68,6 di `TT_02` |

**Zero peggioramenti** è il dato più importante dei sei: significa che la canonizzazione non
ha nascosto né deformato nulla che nel grezzo si trovasse.

### Dove il vault ha aiutato, secondo il rispondente

`llms.txt` è stato la porta d'ingresso: l'elenco delle questioni aperte in testa ha
funzionato da indice dei conflitti, orientando la ricerca prima ancora di aprire una nota.
I locator delle note sono risultati accurati a ogni verifica sul grezzo.

Il principio dichiarato dal rispondente — **«la nota orienta, il grezzo decide»** — è anche
la ragione per cui ha trovato cinque conflitti che le note non registrano: chi si fosse
fermato al livello delle note non li avrebbe visti.

---

## Materiali

| File | Cosa contiene |
|---|---|
| `domande_fumo.jsonl` | le 30 domande, portate dentro il perimetro senza le risposte attese |
| `fumo_risposte.jsonl` | 30 righe, una per domanda |
| `fumo_valutazione.jsonl` | 30 righe di giudizio, con esito, fonti corrette e motivazione |
| `rispondente_rapporto.md` | il verbale del rispondente: metodo, fonti aperte, conflitti trovati, anomalie del datalogger |

⚠️ **`giudice_rapporto.md` non è stato salvato su disco.** Il verbale del giudice esiste
quindi solo nella forma riga-per-riga del `.jsonl`. Le sue due voci discusse al gate — Q019
e Q237 — sono state lette da lì.

---

## Rilievo sul verbale del giudice: Q019

Il giudice descrive come «documento del canone» una fonte citata dal rispondente che è in
realtà **una nota del vault** (`docs\doc-ccp2-limite-critico.md`). Il canone era fisicamente
fuori dal perimetro montato e non è stato né aperto né apribile.

**Il testo del giudice resta com'è**: è testimonianza di come un valutatore che vede solo i
nomi dei file interpreta un percorso `docs/….md`. La correzione di interpretazione sta nel
rapporto di gate e nel decision log.

Ne discende una decisione da prendere **in pre-registrazione, prima della Sessione 6**: come
conta `fonti_corrette` quando la risposta cita una nota invece del grezzo. Nella misura
«dopo» il perimetro è l'intero vault, quindi il caso sarà frequente.
