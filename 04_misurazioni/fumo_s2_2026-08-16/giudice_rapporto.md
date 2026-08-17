---
TRASCRIZIONE SALVATA A POSTERIORI
---

> ⚠️ **Questo file è una ricostruzione, non il verbale originale.** La sessione del giudice
> non ha salvato un rapporto in forma di documento: al momento della chiusura della Sessione 2
> nella cartella della misura esistevano `fumo_valutazione.jsonl` (30 righe di giudizio) e
> nient'altro. Il presente file è stato **ricomposto dai dati su disco** il 17/08/2026, in
> sede di chiusura, per non lasciare la misura senza il verbale del ruolo che l'ha valutata.
>
> **Cosa contiene di originale:** gli esiti, i valori di `fonti_corrette` e le **motivazioni
> integrali** del giudice, riga per riga, così come le ha scritte.
> **Cosa non contiene:** il testo discorsivo della sessione del giudice — introduzione,
> ragionamenti intermedi, note di metodo — che resta nella chat del coordinatore e può essere
> incollato qui sotto senza modificare nulla del resto.
>
> Le due voci discusse al gate (Q019 e Q237) sono commentate in coda, **senza toccare il testo
> del giudice**, che resta testimonianza.

# Verbale del giudice — mini-misura di fumo S2

**Misura:** `S2fumo` · **Voci valutate:** 30 · **Data:** 16/08/2026
**Perimetro del giudice:** cartella della misura più `03_valutazione\`; il vault non è stato
aperto. **Chi valuta non è chi ha risposto.**

⚠️ **Numeri non ufficiali**: non entrano nel README e non sostituiscono la misura «dopo».

## Conteggi

*(ricontati da `06_operativo\qa\conta_fumo.py`, non trascritti a mano)*

| Esito | Fumo | Baseline A, stessi 30 id |
|---|---|---|
| corretta | **28** (93,3%) | 23 (76,7%) |
| parziale | 2 (6,7%) | 6 (20,0%) |
| sbagliata | 0 | 1 (3,3%) |
| allucinata | 0 | 0 |
| **fonti corrette** | **30/30** | 27/30 |

**5 migliorati · 0 peggiorati · 25 invariati.**

## Le trenta voci

| id | Fumo | Baseline A | Fonti ok | Motivazione del giudice |
|---|---|---|---|---|
| Q001 | corretta | corretta | sì | Da TMC 24/06/2026 con lotto, linea e data di produzione, dalla scheda MOD-QA-31, con conferma indipendente dal rapporto di prova. |
| Q019 | corretta | corretta | sì | 72,0 gradi C per almeno 2 minuti, set point di esercizio 74,0-76,0 e monitoraggio con MOD-QA-12 ogni 60 minuti: criterio soddisfatto per intero. |
| Q020 | corretta | corretta | sì | Frequenza 60 minuti piu' inizio/fine turno e cambio prodotto, e i tre diametri 2,0 / 2,5 / 3,0 mm con MOD-QA-07 rev.5. |
| Q021 | corretta | corretta | sì | -18 gradi C al cuore entro 240 minuti, CF-02 <= -18 e soglia di allarme -16 gradi C con i destinatari della notifica. |
| Q025 | corretta | corretta | sì | 15:05, 18:45 e 3 h 40 min, con riscontro incrociato sul datalogger e segnalazione della sola divergenza sull'ora del sopralluogo. |
| Q026 | corretta | corretta | sì | 1.240,00 euro + IVA e consegna 15/05; il codice PK45-VN2-08 compare, con il rilievo che il costruttore usa una codifica diversa. |
| Q027 | corretta | corretta | sì | 348 confezioni scartate al riavvio, distinte dai 330 pezzi di scarto di turno del foglio OEE. |
| Q029 | corretta | corretta | sì | 9,2 x 4,1 x 1,8 mm e massa 0,081 g dal rapporto di prova, distinti dalle dimensioni dichiarate dal cliente in accettazione. |
| Q031 | corretta | corretta | sì | DON 218 ug/kg contro il limite 750 del Reg. (UE) 2023/915, esito conforme, con metodo, LOQ e le altre micotossine sotto soglia. |
| Q035 | corretta | corretta | sì | Riporta i ~9 x 4 mm con spessore 1,5 mm del MOD-QA-31 qualificandoli come prima stima da fotografia, e ricostruisce le altre letture divergenti. |
| Q066 | corretta | corretta | sì | Dice NO citando la nota (4) del manuale e la natura preventiva della misura di controllo (MOD-PR-04), non il CCP3. |
| Q073 | corretta | corretta | sì | Guarnizione piana azzurra 42x30x3 dal carrello ricambi scomparto 3, con il conflitto aperto sul materiale dichiarato. |
| Q074 | **corretta** | parziale | sì | Riporta il 'detectabile: no credo' e insieme il materiale dichiarato genericamente 'gomma' senza marca ne' datasheet ne' DoC MOCA. |
| Q076 | parziale | parziale | sì | Da' 68,9 al cuore e 68,6 di TT_02 alle 14:30:37 con ottime distinzioni, ma non riporta i 27 min di permanenza sotto soglia richiesti dal criterio. |
| Q077 | corretta | corretta | sì | SENSOR_FAULT 'T_CUORE OPEN_CIRCUIT' alle 16:10, valore -999,9 in FAULT, prima lettura valida di ripristino e campioni 12390/12293. |
| Q113 | corretta | corretta | sì | 49 letture T_CUORE in ALARM fra 14:20:37 e 14:44:37, con la distinzione fra campioni, eventi e altre grandezze. |
| Q120 | corretta | corretta | sì | 330 pezzi non conformi e qualita' 94,1% ricalcolata da 5.250/5.580, con i conflitti di perimetro dichiarati a parte. |
| Q132 | **corretta** | sbagliata | sì | Il L26131 quadra: 7.620 prodotti contro 4.260+980+2.380+0, differenza 0, distinto dal L26130 che non quadra per 1.000 pezzi. |
| Q133 | corretta | corretta | sì | 54,2% ricalcolato da 480 e 220 minuti e coerenza confermata con le 3 h 40 min del MOD-PR-04. |
| Q137 | corretta | corretta | sì | 42.430,00 euro sulle 13 NC critiche e segnala che sei voci sono senza importo, quindi il totale e' per difetto. |
| Q138 | **corretta** | parziale | sì | 24 min 30 s contati sulle righe con gli orari del log, e riporta sia i 27 min del riepilogo sia i 29 min della NC-2026-088. |
| Q148 | corretta | corretta | sì | Sei verifiche con esito e data, piu' il riordino cronologico e la discordanza fra data di invio e accettazione del laboratorio. |
| Q152 | corretta | corretta | sì | Sequenza completa: deviazione CCP2 del primo pomeriggio, fermo delle 15:05 per interlock PKM450, guasto sonda delle 16:10 e riavvio delle 18:45. |
| Q153 | corretta | corretta | sì | Copre segnalazione dell'08/05, decisione di proseguire, guasto del 10/05 con guarnizione non originale e sostituzione del 15/05 con i 2 cm2 mancanti. |
| Q187 | corretta | corretta | sì | OEE 36,5 ricalcolato dai tre fattori e 220 minuti ricondotti al fermo di 3 h 40 min della PKM-450. |
| Q199 | **corretta** | parziale | sì | Collega la dimensione oltre i 7 mm e i bordi netti al rischio di lesione e alla PRO-QA-14, distinguendo la Classe 2 dalla gravita' critica della NC. |
| Q207 | corretta | corretta | sì | Risponde NO confrontando i cinque adempimenti prescritti coi fatti, citando la NC-2026-090 sul riprocesso non effettuato. |
| Q237 | corretta | corretta | sì | Risponde NO fondando il verdetto sul datalogger (68,9 minimo) contro il '74,5 conforme' del cartaceo MOD-QA-12; la prevalenza e' applicata nella conclusione ma non enunciata come regola. |
| Q238 | **corretta** | parziale | sì | Distingue i due canali invece di sceglierne uno: 68,9 al cuore e 68,6 di TT_02 dal footer; il minimo di avvio a freddo indicato (18,3) diverge dal 21,5 della risposta attesa. |
| Q239 | parziale | parziale | sì | Da' 24 min e mezzo con i 27 min del riepilogo e i 29 min della NC, ma non segnala anomalia sonda, campioni non validi e checksum fallito, che il criterio indica come bonus decisivo. |

*In grassetto i cinque esiti migliorati rispetto alla baseline A.*

---

## Commento del coordinatore alle due voci discusse al gate

*Aggiunto in sede di chiusura, 17/08/2026. **Il testo del giudice qui sopra non è stato
modificato.***

### Q019 — «documento del canone» è un'interpretazione da correggere

Nella sessione del giudice la fonte `docs/doc-ccp2-limite-critico.md`, citata dal rispondente
accanto al manuale HACCP, è stata descritta come **documento del canone**.

**Non lo è.** È una **nota del vault**, scritta durante la canonizzazione della fetta pilota.
Il canone (`01_metodo\canone_aurora.md`) era **fisicamente fuori dal perimetro montato** del
rispondente, che girava con radice sul vault e `--add-dir` solo su `04_misurazioni\`: non è
stato aperto e non era apribile. L'equivoco nasce dal fatto che il giudice vedeva i soli nomi
dei file citati, e un percorso `docs/….md` in un elenco di fonti può essere letto come un
documento di progetto.

Verificato sul file delle risposte: **Q019 è l'unica delle 30 risposte che cita una nota del
vault** — il rapporto del rispondente ne dichiara due, ma il conteggio ne trova una sola.

Ne discende una decisione registrata nel decision log e **da prendere in pre-registrazione,
prima della Sessione 6**: come conta `fonti_corrette` quando la risposta cita una nota invece
del grezzo. Proposta da discutere: **la fonte che conta resta il grezzo, la nota è
navigazione e non provenienza.**

### Q237 — riserva del giudice, riesame a occhio: esito confermato

Il giudice assegna **corretta** con una riserva esplicita: «la prevalenza è applicata nella
conclusione ma non enunciata come regola».

Riesame eseguito al gate: la risposta stabilisce la non conformità del turno con i dati
giusti — 50 letture sotto il limite, minimo 68,9, flag di allarme su 49 — contro il «74,5
conforme» del registro cartaceo. Il criterio chiedeva di stabilire la non conformità, e la
risposta la stabilisce. **Esito `corretta` confermato**: non enunciare la regola di prevalenza
in forma generale è una mancanza di forma, non di sostanza.

La riserva ha però prodotto una regola di vault, applicata a tutte le note in cui ricorre:
**se una nota stabilisce una regola decisionale, il `summary` la enuncia** — perché è il
`summary` che il retrieval mostra per primo, e una regola che vive solo nel corpo non arriva
a chi legge la risposta.
---

## Testo discorsivo della sessione del giudice — trascrizione dall'incollaggio in chat

*Aggiunto in sede di chiusura dal coordinatore (17/08/2026). Fonte: il messaggio di
chiusura della sessione del giudice, incollato dal titolare nella chat di coordinamento.
Le lacune segnate con […] sono perdite di copia del terminale, non omissioni del giudice.
Le tabelle dei conteggi, identiche a quelle ricontate sopra da `conta_fumo.py`, non sono
duplicate. La voce su Q019 va letta insieme alla correzione d'interpretazione nel commento
del coordinatore qui sopra.*

> **File scritto.** `04_misurazioni\fumo_s2_2026-08-16\fumo_valutazione.jsonl` — il file
> non esisteva, è stato creato. 30 righe totali, tutte con misura `"S2fumo"`.
> [tabella degli esiti: 28 corrette · 2 parziali · 0 sbagliate · 0 allucinate]
>
> Le due parziali sono Q076 (dà 68,9 e 68,6 ma non i 27 min di permanenza sotto soglia
> richiesti dal criterio) e Q239 (dà 24 min e mezzo, i 27 min del footer e i 29 min della
> NC, ma non segnala anomalia sonda, campioni non validi e checksum fallito, che il
> criterio indica come bonus decisivo).
>
> **Confronto con la baseline A.** Tutti e 30 gli id sono presenti nella misura A di
> `baseline_2026-08-14_grezzo\valutazione.jsonl`: nessuna esclusione dal confronto.
> [tabella del conteggio per esito sugli stessi 30 id — identica ai conteggi sopra]
>
> **Id migliorati (5).**
> — Q074, parziale → corretta: «In A mancava il materiale dichia[…]nza marca né datasheet;
>   la fumo lo riporta insieme al "detectabile: no credo".»
> — Q132, sbagliata → corretta: «In A il mass balance .xlsx non era leggibile e concludeva
>   che i numeri non quadravano; la fumo legge il foglio "A valle", somma
>   4.260+980+2.380+0 […] 0, distinguendo il L26131 dal L26130.»
> — Q138, parziale → corretta: «In A mancavano i 27 min dichiara[…] la fumo li cita
>   accanto ai 24 min 30 s contati sulle righe e ai 29 min della NC-2026-088.»
> — Q199, parziale → corretta: «In A mancava la dimensione oltre i 7 mm, che è il criterio
>   della valutazione del rischio; la fumo la collega esplicitamente al rischio di
>   les[…]»
> — Q238, parziale → corretta: «In A mancava il confronto con i […] TT_02; la fumo
>   distingue i due canali invece di sceglierne uno.»
>
> **Id peggiorati.** «Nessuno. Nessun esito della fumo è inferiore a quello dell[…] I due
> parziali della fumo (Q076, Q239) erano parziali anche in A: invariati, non peggiorati.»
>
> **Fonti corrette.** «30/30 contro 27/30. Le tre che in A erano sbagliate — Q001, Q132,
> Q199 — nella fumo citano la fonte attesa.»
>
> **Note di lettura, senza giudizio di valore.**
> — «Trenta domande su duecentottantadue. Su un campione di q[…] fra due o tre esiti non
>   ha significato statistico: uno scarto di 5 esiti su 30 non è distinguibile dal rumore
>   di campionamento, e questi numeri non autorizzano una stima della differenza
>   sull'intero set. Servono a dire che il design della fetta non ha rott[…]ntificare un
>   guadagno.»
> — «La fetta è selezionata sul lotto L26130, cioè sul nucleo che la canonizzazione ha
>   lavorato: non è un campione casuale delle 282, e non è rappresentativa delle aree non
>   canonizzate.»
> — «Un fatto da segnalare a chi coordina, non un esito: in Q019 il rispondente cita fra
>   le fonti `docs/doc-ccp2-limite-critico.md`, cioè un documento del canone e non un
>   documento dell'archivio. Ho contato la[…]accanto compare il manuale_HACCP che è la
>   fonte attesa, ma […] non ho potuto verificare quel file — è fuori dal perimetro del
>   giudice. Se in Sessione 6 il canone diventerà una fonte citabile a pieno titolo, va
>   deciso prima come si conta nella metrica fonti_corrette, a[…] baseline smette di
>   essere omogeneo.»
> — «Q237 è corretta ma con una riserva registrata in motivazione: la risposta fa
>   prevalere il datalogger nella conclusione ("non conforme") e ci[…]entrambi i valori
>   68,9 e 74,5, però dichiara il conflitto e, […] non da risolvere» invece di enunciare
>   che il dato strumentale prevale e che la registrazione cartacea non è veritiera.
>   Sull'id più importante del set, vale la pena guardarla a occhio prima di
>   industrializzare.»
