# Domande di verifica — archivio Aurora Food Group

282 domande per misurare quanto il sistema ha davvero capito dei 159 documenti
dell'archivio. Le risposte stanno in `RISPOSTE_RAG.md`, con lo stesso numero.
Per la valutazione automatica c'è `eval_set.jsonl`, dove ogni domanda porta con sé
i file da cui si ricava la risposta.

⚠️ **Tenere questi file fuori da `sources/`.** Contengono le risposte: se finiscono
nell'archivio indicizzato, il test non misura più niente.

## Come è composto il set

| Tipo | Domande | Cosa misura |
|---|---|---|
| Ricerca diretta | 86 | il retrieval di base |
| Aggregazione | 28 | la capacità di leggere una tabella intera, non un frammento |
| Calcolo | 24 | il ragionamento numerico sopra il dato recuperato |
| Ricostruzione temporale | 18 | la ricostruzione di una sequenza da fonti sparse |
| Attraversamento | 74 | il collegamento fra documenti che non si citano fra loro |
| Conflitto | 14 | l'onestà: segnalare il conflitto invece di scegliere a caso |
| Trappola | 31 | la resistenza all'allucinazione |
| Forma dell'archivio | 7 | la consapevolezza della struttura del corpus |

Difficoltà: livello 1 → 32 domande · livello 2 → 63 domande · livello 3 → 92 domande · livello 4 → 62 domande · livello 5 → 33 domande

**Le domande più importanti non sono quelle facili.** Un sistema che risponde bene alle
prime e sbaglia le contraddizioni e le trappole è un sistema che sta indovinando: sa
recuperare testo, non sa dire quando i documenti si smentiscono o quando un dato non
c'è. Sono 45 domande su 282,
ed è lì che si vede la differenza.

## Come leggere gli esiti

- **Sbaglia i `lookup`** → problema di retrieval: il chunking o l'indice non funzionano.
- **Prende i `lookup` ma sbaglia i `multi_hop`** → recupera un documento solo e non sa
  collegare; serve query expansion o un passaggio di ricerca iterativa.
- **Risponde con sicurezza alle `non_rispondibile`** → il modello inventa: va istruito a
  dichiarare l'assenza, e vanno alzate le soglie di similarità.
- **Sceglie un valore a caso nelle `contraddizione`** → non sa distinguere le versioni:
  servono i metadati di data e revisione nel contesto recuperato.

---


## Ricerca diretta — il dato sta in un solo documento

**1.** Che TMC riportava la confezione oggetto del reclamo?  
<sub>difficoltà 1</sub>

**2.** Quanto abbiamo chiuso di utile nel 2025 e cosa è stato proposto di farne?  
<sub>difficoltà 1</sub>

**3.** Quanto abbiamo fatturato nel 2025 secondo il bilancio depositato?  
<sub>difficoltà 1</sub>

**4.** Quanta cassa avevamo in bilancio a fine 2025?  
<sub>difficoltà 1</sub>

**5.** Come siamo messi col conto a fine maggio?  
<sub>difficoltà 1</sub>

**6.** Quanto ci ha chiesto di listing fee il buyer di Tosano e su quale prodotto?  
<sub>difficoltà 1</sub>

**7.** Quanto paghiamo di leasing al mese per il forno della linea 2?  
<sub>difficoltà 1</sub>

**8.** Con che pesi valutiamo i fornitori?  
<sub>difficoltà 1</sub>

**9.** Che prognosi ha avuto l'operaio infortunato il 28/04 e quando abbiamo mandato la denuncia all'INAIL?  
<sub>difficoltà 1</sub>

**10.** Dove e a che ora e' successo l'infortunio di Corradin, e che lesione ha riportato?  
<sub>difficoltà 1</sub>

**11.** Chi ha visto l'infortunio e chi ha portato l'operaio al pronto soccorso?  
<sub>difficoltà 1</sub>

**12.** Quando scade il rinnovo periodico antincendio e con che pratica siamo registrati al comando dei Vigili del Fuoco?  
<sub>difficoltà 1</sub>

**13.** Quanto dura l'AUA e quando va chiesto il rinnovo?  
<sub>difficoltà 1</sub>

**14.** Come e' andata la verifica dell'impianto di terra e quanto e' venuta la resistenza?  
<sub>difficoltà 1</sub>

**15.** Chi tiene il registro rifiuti e con che numero siamo iscritti al RENTRI?  
<sub>difficoltà 1</sub>

**16.** A che ora doveva scaricare il camion a Cerea il 7 maggio e a che ora e' arrivato?  
<sub>difficoltà 1</sub>

**17.** Quanto vale una pedana EPAL non resa dal cliente e entro quando va regolarizzato il buono?  
<sub>difficoltà 1</sub>

**18.** Quando abbiamo fatto l'ultima formazione sicurezza dei lavoratori e chi l'ha tenuta?  
<sub>difficoltà 1</sub>

**19.** Qual e' il limite critico del CCP2 sul pastorizzatore PT-104?  
<sub>difficoltà 1</sub>

**20.** Ogni quanto va verificato il metal detector della Linea 1 e con quali tasselli?  
<sub>difficoltà 1</sub>

**21.** Qual e' il limite critico della surgelazione e a che temperatura scatta l'allarme della cella CF-02?  
<sub>difficoltà 1</sub>

**22.** Che differenza fa la nostra procedura tra ritiro e richiamo?  
<sub>difficoltà 1</sub>

**23.** Entro quanto dobbiamo rispondere a una richiesta scritta dell'ufficio qualita' di un cliente?  
<sub>difficoltà 1</sub>

**24.** Chi coordina il team di crisi e a che numero si reperisce fuori orario?  
<sub>difficoltà 1</sub>

**25.** A che ora si e' fermata la confezionatrice domenica 10 maggio e quanto e' durato il fermo?  
<sub>difficoltà 1</sub>

**26.** Quanto costa il kit valvola originale Pakmatic e quando doveva arrivare?  
<sub>difficoltà 1</sub>

**27.** Quante confezioni sono state buttate al riavvio della PKM-450 dopo la riparazione?  
<sub>difficoltà 1</sub>

**28.** Cosa dice esattamente la signora che ha scritto dal form del sito il 12 maggio?  
<sub>difficoltà 1</sub>

**29.** Che dimensioni e che peso aveva il frammento mandato al laboratorio?  
<sub>difficoltà 1</sub>

**30.** Quando scade il certificato BRCGS e in che finestra va fatto il riaudit?  
<sub>difficoltà 1</sub>

**31.** Quanto DON c'era nella farina del lotto MV26-0429A?  
<sub>difficoltà 1</sub>

**32.** Entro quanto va data la prima risposta a un reclamo classificato come critico?  
<sub>difficoltà 1</sub>

**33.** Il molino ci consegna solo su ordine minimo? Quali sono le condizioni di fornitura rimaste invariate dopo l'aumento?  
<sub>difficoltà 2</sub>

**34.** Quali documenti dobbiamo allegare a ogni consegna per il cliente?  
<sub>difficoltà 2</sub>

**35.** Che dimensioni aveva il frammento di plastica trovato dalla consumatrice?  
<sub>difficoltà 2</sub>

**36.** Il candidato che ci ha scritto per il posto in produzione che studi ha fatto?  
<sub>difficoltà 2</sub>

**37.** Il candidato ha gia' esperienza in un laboratorio qualita'?  
<sub>difficoltà 2</sub>

**38.** Qual e' il massimale contributivo di quest'anno e il minimale giornaliero?  
<sub>difficoltà 2</sub>

**39.** Nella cartella di lavoro rimasta aperta sul desktop cosa c'era scritto?  
<sub>difficoltà 2</sub>

**40.** Quanti soldi dobbiamo alle banche a fine 2025, e quanto di questi scade oltre l'anno?  
<sub>difficoltà 2</sub>

**41.** Che numeri abbiamo sui crediti verso clienti a bilancio, e c'è una svalutazione?  
<sub>difficoltà 2</sub>

**42.** Chi è il nostro revisore e quanto ci costa?  
<sub>difficoltà 2</sub>

**43.** Il tunnel di surgelazione è già finito nel bilancio 2025?  
<sub>difficoltà 2</sub>

**44.** Quanto fido abbiamo in banca fra conto corrente e anticipo fatture?  
<sub>difficoltà 2</sub>

**45.** A che prezzo vendiamo il cornetto private label a Tosano e quanto ci resta?  
<sub>difficoltà 2</sub>

**46.** Come paga Tosano e che sconti gli riconosciamo da contratto?  
<sub>difficoltà 2</sub>

**47.** Quali volumi minimi ci garantisce Tosano nel contratto?  
<sub>difficoltà 2</sub>

**48.** Quanto costa il tunnel Criotech e come si paga?  
<sub>difficoltà 2</sub>

**49.** Su che codice destinatario mandiamo le fatture a Tosano, e su quale le riceviamo noi?  
<sub>difficoltà 2</sub>

**50.** Che copertura abbiamo sulla RC prodotto e quanto costa?  
<sub>difficoltà 2</sub>

**51.** Quanto ci costa il contratto di manutenzione dei forni?  
<sub>difficoltà 2</sub>

**52.** Che consumo dichiara Criotech per il tunnel nuovo?  
<sub>difficoltà 2</sub>

**53.** Il commercialista dice che serve la perizia per il credito d'imposta?  
<sub>difficoltà 2</sub>

**54.** Qual e' il PAT INAIL dello stabilimento e con che numero e' annotato l'infortunio sul registro?  
<sub>difficoltà 2</sub>

**55.** Quante richieste ha fatto l'RSPP dopo il sopralluogo in cella e entro quando va aggiornato il DVR?  
<sub>difficoltà 2</sub>

**56.** Quanto e' larga davvero la corsia B in cella e quanto dice il DVR?  
<sub>difficoltà 2</sub>

**57.** Quali attivita' dello stabilimento sono soggette al controllo dei Vigili del Fuoco e in che categoria siamo?  
<sub>difficoltà 2</sub>

**58.** Quanti estintori e quanti idranti risultano censiti nel certificato antincendio?  
<sub>difficoltà 2</sub>

**59.** Ogni quanto dobbiamo analizzare lo scarico in fognatura e ogni quanto le emissioni in atmosfera?  
<sub>difficoltà 2</sub>

**60.** Chi autorizza gli straordinari del personale di linea e fino a che limite?  
<sub>difficoltà 2</sub>

**61.** Ogni quanto va rifatta la verifica dell'impianto di terra e quando tocca la prossima?  
<sub>difficoltà 2</sub>

**62.** Chi ci trasporta i rifiuti e fino a quando e' valida la sua iscrizione all'Albo?  
<sub>difficoltà 2</sub>

**63.** Come e' finita la contestazione del CE.DI. di Cerea sul ritardo del 7 maggio?  
<sub>difficoltà 2</sub>

**64.** Qual era la soglia per superare il test di fine corso e c'e' stato qualcuno che non l'ha passato?  
<sub>difficoltà 2</sub>

**65.** Che contratto e' previsto per i tre neolaureati e da quando entrerebbero?  
<sub>difficoltà 2</sub>

**66.** Il metal detector MD-3200 e' in grado di intercettare un frammento di plastica?  
<sub>difficoltà 2</sub>

**67.** Che forza deve avere la farina tipo 0 che compriamo da Molino Veneto, e quali sono i limiti di scheda?  
<sub>difficoltà 2</sub>

**68.** Che cosa contestava esattamente la non conformita' sul carrello dei ricambi?  
<sub>difficoltà 2</sub>

**69.** Quali strumenti avevano la taratura scaduta al momento dell'audit?  
<sub>difficoltà 2</sub>

**70.** Quando sono arrivate a CSQA le evidenze di chiusura delle non conformita'?  
<sub>difficoltà 2</sub>

**71.** Come e' andato il test di rintracciabilita' fatto durante l'audit?  
<sub>difficoltà 2</sub>

**72.** Quando abbiamo fatto l'ultima simulazione di richiamo e com'e' andata?  
<sub>difficoltà 2</sub>

**73.** Che guarnizione ha montato il capo officina sulla valvola azoto il 10 maggio?  
<sub>difficoltà 2</sub>

**74.** Alla domanda della qualita', il capo officina ha detto se la guarnizione era rilevabile dal metal detector?  
<sub>difficoltà 2</sub>

**75.** E' arrivata piu' di una segnalazione di corpo estraneo su quel prodotto?  
<sub>difficoltà 2</sub>

**76.** Qual e' la temperatura piu' bassa che il pastorizzatore ha registrato il 10 maggio?  
<sub>difficoltà 2</sub>

**77.** Cos'e' successo alla sonda a cuore del PT-104 nel pomeriggio del 10 maggio?  
<sub>difficoltà 2</sub>

**78.** Il lavaggio CIP del 6 maggio e' andato a buon fine?  
<sub>difficoltà 2</sub>

**79.** Qual e' il set point della cella surgelati e quando e' scattato il primo allarme di alta temperatura ad aprile?  
<sub>difficoltà 2</sub>

**80.** Che protezioni individuali servono per fare un lavaggio CIP?  
<sub>difficoltà 2</sub>

**81.** C'e' qualche quadro elettrico non conforme in stabilimento?  
<sub>difficoltà 3</sub>

**82.** Che succede se sforiamo la finestra di scarico al centro di distribuzione del cliente?  
<sub>difficoltà 3</sub>

**83.** Che documenti dobbiamo mandare all'ente prima dell'audit e con quanto anticipo?  
<sub>difficoltà 3</sub>

**84.** Quali sono le aliquote contributive che ci applica l'INPS quest'anno?  
<sub>difficoltà 3</sub>

**85.** Qual è il livello di servizio che dobbiamo garantire a Tosano e cosa rischiamo se non lo teniamo?  
<sub>difficoltà 3</sub>

**86.** Aurora ha una polizza per il rischio informatico?  
<sub>difficoltà 3</sub>


## Aggregazione — bisogna contare o sommare righe

**87.** Nel prospetto degli straordinari, quale reparto e' esploso e di quanto rispetto al budget?  
<sub>difficoltà 2</sub>

**88.** Quali non conformità fornitore sono ancora aperte?  
<sub>difficoltà 2</sub>

**89.** Quanti corsi di formazione risultano scaduti in azienda?  
<sub>difficoltà 2</sub>

**90.** Quante persone hanno timbrato domenica 10 maggio e di che reparti?  
<sub>difficoltà 2</sub>

**91.** Quante timbrature sono state forzate perche' mancava l'uscita?  
<sub>difficoltà 2</sub>

**92.** Quali sono le referenze a listino col margine più basso?  
<sub>difficoltà 3</sub>

**93.** Quanti punti vendita Tosano serviamo secondo la proiezione ARR e quanto valgono le due referenze principali?  
<sub>difficoltà 3</sub>

**94.** Nella settimana della promo abbiamo bucato lo scaffale da qualche parte?  
<sub>difficoltà 3</sub>

**95.** Quali contatti nella lista buyer sono duplicati o hanno dati sbagliati?  
<sub>difficoltà 3</sub>

**96.** Dalla fiera di Cibus, quali contatti valgono davvero e quali hanno un blocco che dobbiamo risolvere prima?  
<sub>difficoltà 3</sub>

**97.** Quanti hanno l'HACCP base scaduto e in che reparto stanno?  
<sub>difficoltà 3</sub>

**98.** Quanti corsi risultano in scadenza e quali sono?  
<sub>difficoltà 3</sub>

**99.** Quante non conformita' sono uscite dalle analisi dell'acqua potabile e su quali punti?  
<sub>difficoltà 3</sub>

**100.** Quante entrate fuori tolleranza ci sono state in quella settimana e chi le ha fatte piu' volte?  
<sub>difficoltà 3</sub>

**101.** Quanti dipendenti ci sono nell'estratto del libro unico e come sono divisi per reparto?  
<sub>difficoltà 3</sub>

**102.** Quanti chili di rifiuti pericolosi abbiamo prodotto e dove sono andati?  
<sub>difficoltà 3</sub>

**103.** Quanti strumenti sono fuori taratura e dove sono?  
<sub>difficoltà 3</sub>

**104.** Quanti lotti in magazzino sono gia' scaduti e vanno smaltiti?  
<sub>difficoltà 3</sub>

**105.** Quante non conformita' interne abbiamo aperto nel 2026 e quante sono ancora da chiudere?  
<sub>difficoltà 3</sub>

**106.** Quanti lavaggi CIP abbiamo fatto a maggio sulla Linea 1 e quanti sono andati storti?  
<sub>difficoltà 3</sub>

**107.** Quanti reclami abbiamo a registro nel 2026 e quanti sono ancora aperti?  
<sub>difficoltà 3</sub>

**108.** Chi ha condotto i lavaggi CIP di maggio?  
<sub>difficoltà 3</sub>

**109.** Quanti tamponi ambientali sono risultati fuori limite quest'anno?  
<sub>difficoltà 4</sub>

**110.** Quante ricerche di Listeria abbiamo fatto e quante sono venute positive?  
<sub>difficoltà 4</sub>

**111.** Quanti allarmi ha dato la cella surgelati in aprile e di che tipo erano?  
<sub>difficoltà 4</sub>

**112.** Quali manutenzioni programmate risultano rimandate?  
<sub>difficoltà 4</sub>

**113.** Quante letture della sonda a cuore sono finite in allarme il 10 maggio?  
<sub>difficoltà 4</sub>

**114.** Qual e' la causa radice che genera piu' non conformita' e quale quella che costa di piu'?  
<sub>difficoltà 4</sub>


## Calcolo — la risposta va ricavata con un conto

**115.** Quanto abbiamo di insoluti aperti in tutto?  
<sub>difficoltà 2</sub>

**116.** Quanto ci esce in tutto per il tunnel fra imponibile e IVA, milestone per milestone?  
<sub>difficoltà 2</sub>

**117.** Quanto ci costano al mese tutti i leasing e i noleggi messi insieme?  
<sub>difficoltà 2</sub>

**118.** Ci conviene di piu' il premio presenza o continuare a sostituire chi se ne va?  
<sub>difficoltà 2</sub>

**119.** Quanto ci costa a viaggio la domenica scegliere il vettore piu' caro invece del piu' economico su Cerea?  
<sub>difficoltà 2</sub>

**120.** Quanti pezzi non conformi ha prodotto il turno 2 del 10 maggio e che tasso di qualita' fa?  
<sub>difficoltà 2</sub>

**121.** Sommando i tre blocchi definiti dalla qualita', quante confezioni fanno in tutto?  
<sub>difficoltà 2</sub>

**122.** Come si arriva ai 413.316 euro del quadro economico del tunnel?  
<sub>difficoltà 3</sub>

**123.** Il conto di Fantin sull'investimento e quello di Trentin non tornano: di quanto?  
<sub>difficoltà 3</sub>

**124.** Quanto risparmiamo all'anno col tunnel nuovo rispetto al TS-01?  
<sub>difficoltà 3</sub>

**125.** In quanti anni si ripaga il tunnel con i soli risparmi?  
<sub>difficoltà 3</sub>

**126.** Il riepilogo dei costi fissi non quadra col gestionale: di quanto e perché?  
<sub>difficoltà 3</sub>

**127.** Quanto vale l'IVA sulla bolletta della luce di marzo e come si arriva al totale?  
<sub>difficoltà 3</sub>

**128.** Chi supera il tetto delle 250 ore annue di straordinario e a chi manca poco?  
<sub>difficoltà 3</sub>

**129.** Quanto vale il contenzioso sulle pedane, secondo il nostro conteggio e secondo il loro?  
<sub>difficoltà 3</sub>

**130.** Quanto abbiamo risparmiato sulla penale del CE.DI. e quanto pesa il ritardo dell'olio?  
<sub>difficoltà 3</sub>

**131.** Quanti chili di scarto alimentare abbiamo prodotto nel primo semestre?  
<sub>difficoltà 3</sub>

**132.** E il lotto L26131 invece quadra?  
<sub>difficoltà 3</sub>

**133.** Quanto vale la disponibilita' del turno 2 del 10 maggio, e torna con il fermo registrato?  
<sub>difficoltà 3</sub>

**134.** Il conto del credito d'imposta nel file CapEx torna?  
<sub>difficoltà 4</sub>

**135.** Il riepilogo di giugno in fondo allo scadenzario è coerente?  
<sub>difficoltà 4</sub>

**136.** Quanto tempo complessivo e' rimasta fuori limite la cella surgelati in aprile?  
<sub>difficoltà 4</sub>

**137.** Quanto ci sono costate finora le non conformita' classificate come critiche nel 2026?  
<sub>difficoltà 4</sub>

**138.** Quanto e' durata davvero la deviazione del CCP2 del 10 maggio secondo il datalogger?  
<sub>difficoltà 4</sub>


## Ricostruzione temporale — serve mettere in fila gli eventi

**139.** Ricostruisci la sequenza dei fatti dall'infortunio in poi.  
<sub>difficoltà 2</sub>

**140.** L'offerta di Criotech era ancora valida quando abbiamo firmato l'ordine?  
<sub>difficoltà 3</sub>

**141.** Che tempi ha imposto il buyer per la risposta, e come sono slittati?  
<sub>difficoltà 3</sub>

**142.** Da quando vale il prezzo del multicereali che stiamo applicando adesso a Tosano?  
<sub>difficoltà 3</sub>

**143.** Fra le autorizzazioni e le verifiche di legge, qual e' la prossima a scadere?  
<sub>difficoltà 3</sub>

**144.** Alla data dell'estrazione del registro formazione, quali corsi erano scaduti da piu' di un mese?  
<sub>difficoltà 3</sub>

**145.** Ricostruisci la giornata e i giorni successivi della contestazione del CE.DI.  
<sub>difficoltà 3</sub>

**146.** Con che ritmo se ne sono andati gli operai della Linea 2?  
<sub>difficoltà 3</sub>

**147.** Quali impegni con date ci ha lasciato l'incontro con il sindacato?  
<sub>difficoltà 3</sub>

**148.** Quali verifiche sono state fatte sul reclamo e in che ordine?  
<sub>difficoltà 4</sub>

**149.** Quanti giorni ci sono fra la data della fattura 215 e la sua scadenza, e torna con le condizioni contrattuali?  
<sub>difficoltà 4</sub>

**150.** Quando ci esce il saldo del tunnel, secondo i vari documenti?  
<sub>difficoltà 4</sub>

**151.** Ripercorrimi tutta la vicenda della chiusura delle non conformita' dell'audit con l'ente.  
<sub>difficoltà 4</sub>

**152.** Ricostruiscimi la giornata del pastorizzatore di domenica 10 maggio dal datalogger.  
<sub>difficoltà 5</sub>

**153.** Dammi la storia della valvola azoto, da quando ha cominciato a perdere fino alla riparazione definitiva.  
<sub>difficoltà 5</sub>

**154.** Metti in fila cos'e' successo dal reclamo della consumatrice all'esito del laboratorio.  
<sub>difficoltà 5</sub>

**155.** Come sono peggiorati nel mese gli allarmi della cella surgelati?  
<sub>difficoltà 5</sub>

**156.** Ricostruisci la storia della sonda di conducibilita' del CIP da inizio anno.  
<sub>difficoltà 5</sub>


## Attraversamento — la risposta nasce da più documenti

**157.** Chi ci sta ancora rimanendo indietro coi pagamenti e da quanto?  
<sub>difficoltà 2</sub>

**158.** Che corsi ci hanno proposto e quanto costavano?  
<sub>difficoltà 3</sub>

**159.** Perché la trattativa sullo sconto con Tosano è così delicata? Quanto pesa quel cliente per noi?  
<sub>difficoltà 3</sub>

**160.** Con il -4,5% chiesto dal buyer, quale referenza va sotto il costo industriale?  
<sub>difficoltà 3</sub>

**161.** Con che criterio il foglio marginalità mette una referenza in classe A, B o C, e dove finisce il cornetto PL?  
<sub>difficoltà 3</sub>

**162.** Quanto vale davvero il formato 3+1 se paghiamo 12.000 euro di ingresso?  
<sub>difficoltà 3</sub>

**163.** Rossi minaccia di delistare la focaccina: quanto ci perdiamo e ha ragione sui numeri?  
<sub>difficoltà 3</sub>

**164.** Il credito d'imposta sul tunnel possiamo metterlo nel previsionale di cassa?  
<sub>difficoltà 3</sub>

**165.** Quanto ci siamo detti in CdA che avremmo usato dell'anticipo fatture, e quanto ne stiamo usando davvero?  
<sub>difficoltà 3</sub>

**166.** Che fine ha fatto la fattura dei vasetti Euroglass?  
<sub>difficoltà 3</sub>

**167.** Il pagamento delle RIBA Molino Veneto di fine maggio torna con la fattura elettronica ricevuta?  
<sub>difficoltà 3</sub>

**168.** Come risulta l'assenza dell'infortunato nella settimana dal 4 all'8 maggio e come si riflette sul cedolino?  
<sub>difficoltà 3</sub>

**169.** Sulla Linea 1 chi ha l'HACCP scaduto e ha comunque lavorato la domenica del 10 maggio?  
<sub>difficoltà 3</sub>

**170.** C'e' qualcuno in magazzino che guida il muletto senza abilitazione valida?  
<sub>difficoltà 3</sub>

**171.** I capiturni hanno la formazione da preposto in regola?  
<sub>difficoltà 3</sub>

**172.** Chi e' in squadra di emergenza con la formazione in scadenza o gia' scaduta?  
<sub>difficoltà 3</sub>

**173.** L'operaio dimissionario della Linea 2: quando ha dato le dimissioni, quando esce e come figura negli altri documenti?  
<sub>difficoltà 3</sub>

**174.** Domenica 10 maggio quanta gente serviva sulla Linea 2 e quanta ce n'era davvero?  
<sub>difficoltà 3</sub>

**175.** Le domeniche lavorate a maggio sono state due o tre?  
<sub>difficoltà 3</sub>

**176.** Il fermo della confezionatrice del 10 maggio dove ha lasciato traccia nei documenti di reparto?  
<sub>difficoltà 3</sub>

**177.** La guarnizione della valvola azoto: quando e' arrivata l'originale e che fine hanno fatto quelle generiche?  
<sub>difficoltà 3</sub>

**178.** I guanti che usiamo in cella vanno bene o no?  
<sub>difficoltà 3</sub>

**179.** Perche' a marzo abbiamo sforato i grassi allo scarico e cosa c'entra la produzione?  
<sub>difficoltà 3</sub>

**180.** C'e' uno strumento scaduto su un impianto che sta ancora girando?  
<sub>difficoltà 3</sub>

**181.** I due lotti bloccati dalla qualita': con che film sono stati confezionati e chi lo ha fornito?  
<sub>difficoltà 3</sub>

**182.** Il sacco di farina rotto arrivato col DDT del Molino che fine ha fatto?  
<sub>difficoltà 3</sub>

**183.** I lotti bloccati sono gia' finiti in parte a rifiuto?  
<sub>difficoltà 3</sub>

**184.** Se dobbiamo far partire un camion per Cerea di domenica, quanto ci costa e con chi?  
<sub>difficoltà 3</sub>

**185.** Perche' il metal detector non ha fermato il frammento trovato dalla consumatrice?  
<sub>difficoltà 3</sub>

**186.** Da quanto tempo era scaduta la manutenzione sulla guarnizione della valvola azoto quando si e' rotta?  
<sub>difficoltà 3</sub>

**187.** Perche' l'OEE del turno 2 di domenica 10 maggio e' crollato?  
<sub>difficoltà 3</sub>

**188.** C'e' qualche materia prima usata sul lotto L26130 che era vicina alla scadenza?  
<sub>difficoltà 3</sub>

**189.** I tamponi fatti sulla confezionatrice dopo l'intervento del 10 maggio cosa hanno dato?  
<sub>difficoltà 3</sub>

**190.** Dopo il montaggio del ricambio originale la situazione igienica sulla confezionatrice e' rientrata?  
<sub>difficoltà 3</sub>

**191.** L'operatore nuovo che lavorava in linea domenica 10 maggio aveva la formazione HACCP?  
<sub>difficoltà 3</sub>

**192.** Possiamo ancora recuperare il prodotto sfuso a bordo linea sulla Linea 1?  
<sub>difficoltà 3</sub>

**193.** Il conto del ricambio Pakmatic quanto fa e quando l'abbiamo pagato?  
<sub>difficoltà 4</sub>

**194.** La verifica semestrale degli estintori era prevista per il 12 maggio: e' stata fatta in tempo? Chi se n'e' occupato e cosa stava succedendo in azienda in quei giorni?  
<sub>difficoltà 4</sub>

**195.** L'acconto di 87.000 euro per il tunnel: chi l'ha deliberato, quando scade e come viene coperto?  
<sub>difficoltà 4</sub>

**196.** La focaccina AF-FC-0330 rischia il delisting: quanto ci perderemmo e quali scorte resterebbero ferme?  
<sub>difficoltà 4</sub>

**197.** Quali strumenti di misura scadono entro l'estate e chi deve muoversi?  
<sub>difficoltà 4</sub>

**198.** Chi sono le persone che rischiano di sforare il tetto annuo degli straordinari, e chi e' il piu' esposto?  
<sub>difficoltà 4</sub>

**199.** Perche' il reclamo per il corpo estraneo e' stato classificato come critico?  
<sub>difficoltà 4</sub>

**200.** L'ente di certificazione ha accettato le nostre evidenze di chiusura delle non conformita'?  
<sub>difficoltà 4</sub>

**201.** Che rapporto c'è fra l'acconto del tunnel e il fatto che Tosano ci paga a 90 giorni?  
<sub>difficoltà 4</sub>

**202.** Il pagamento dell'acconto Criotech si vede sull'estratto conto? Torna con la fattura?  
<sub>difficoltà 4</sub>

**203.** L'investimento del tunnel sta dentro a quello che ha approvato il CdA?  
<sub>difficoltà 4</sub>

**204.** Quanto ci è costata in tutto la storia del reclamo, guardando i soldi già usciti o impegnati?  
<sub>difficoltà 4</sub>

**205.** La fattura 188 dell'XML è la stessa che vedo pagata nell'estratto conto?  
<sub>difficoltà 4</sub>

**206.** Quanto pesa l'energia sul totale dei costi fissi, e cosa succede quando entra il tunnel?  
<sub>difficoltà 4</sub>

**207.** Sulla deviazione di temperatura del 10 maggio abbiamo fatto quello che prevede il piano HACCP?  
<sub>difficoltà 4</sub>

**208.** La farina usata per il lotto L26130 aveva il certificato di analisi, e rispettava la nostra scheda tecnica?  
<sub>difficoltà 4</sub>

**209.** Quante confezioni sono state effettivamente bloccate e dove si trovavano?  
<sub>difficoltà 4</sub>

**210.** Il carrello ricambi a bordo linea era gia' stato contestato prima del 10 maggio?  
<sub>difficoltà 4</sub>

**211.** Gli allarmi della cella surgelati di aprile potevano essere previsti guardando il piano di manutenzione?  
<sub>difficoltà 4</sub>

**212.** I tempi delle fasi registrati dal CIP corrispondono a quelli dell'istruzione operativa?  
<sub>difficoltà 4</sub>

**213.** Il programma di lavaggio girato ogni sera sulla Linea 1 e' quello giusto per il circuito?  
<sub>difficoltà 4</sub>

**214.** Quello che ha scritto il capoturno sul quaderno per il 10 maggio combacia con il datalogger?  
<sub>difficoltà 4</sub>

**215.** Chi ha compilato il registro delle temperature del pastorizzatore nel turno in cui e' avvenuta la deviazione?  
<sub>difficoltà 4</sub>

**216.** Il reclamo del 12 maggio e' stato classificato come prevede la procedura reclami?  
<sub>difficoltà 4</sub>

**217.** Sullo snack multicereali esiste un rischio di contaminazione da sesamo?  
<sub>difficoltà 4</sub>

**218.** L'azione decisa in riesame di direzione sull'armadio ricambi ha funzionato?  
<sub>difficoltà 4</sub>

**219.** Ricostruisci come un pezzo di plastica azzurra e' finito dentro uno snack: cosa lega il guasto della confezionatrice al reclamo della consumatrice?  
<sub>difficoltà 5</sub>

**220.** Il 5 maggio sono arrivati 46.080 vasetti di vetro: a quale prodotto servono?  
<sub>difficoltà 5</sub>

**221.** A che ora si e' tenuta la riunione di direzione del 12 maggio?  
<sub>difficoltà 5</sub>

**222.** La mail di convocazione della riunione di direzione allegava l'ordine del giorno e il prospetto straordinari: cosa contengono davvero quei due allegati?  
<sub>difficoltà 5</sub>

**223.** Se accettassimo il -4,5% chiesto dal buyer, cosa succede al cornetto AF-CR-0215?  
<sub>difficoltà 5</sub>

**224.** C'e' un problema con il lievito usato sul lotto L26130?  
<sub>difficoltà 5</sub>

**225.** Quanto ci e' costato il ritardo di Pakmatic sul ricambio della valvola?  
<sub>difficoltà 5</sub>

**226.** L'audit CSQA aveva rilevato due termometri con taratura scaduta: risultano regolarizzati nel piano tarature?  
<sub>difficoltà 5</sub>

**227.** L'infortunio di Corradin ha una causa che c'entra con il progetto del nuovo tunnel?  
<sub>difficoltà 5</sub>

**228.** Il carrello dei ricambi a bordo linea: da quando e' un problema e cosa e' successo dopo?  
<sub>difficoltà 5</sub>

**229.** Il punto 7 della lista documentale chiesta dall'ULSS riguarda l'acqua: eravamo in regola?  
<sub>difficoltà 5</sub>

**230.** Il film MAP usato sul lotto L26130 e' stato verificato? Con quale esito?  
<sub>difficoltà 5</sub>


## Conflitto — l'archivio dice cose diverse: va segnalato

**231.** Quante persone risultano sopra le 200 ore di straordinario al 30 aprile, e quante ne conta il sindacato?  
<sub>difficoltà 3</sub>

**232.** In quante settimane Criotech consegna il tunnel?  
<sub>difficoltà 4</sub>

**233.** Quanto e' utilizzato l'anticipo fatture UniCredit?  
<sub>difficoltà 4</sub>

**234.** Qual è il numero dell'offerta Criotech che dobbiamo citare nei documenti?  
<sub>difficoltà 4</sub>

**235.** Quante non conformita' ha rilevato l'audit CSQA di febbraio 2026?  
<sub>difficoltà 5</sub>

**236.** Con quale protocollo e in che data l'ULSS ha preavvisato l'ispezione del 9 giugno?  
<sub>difficoltà 5</sub>

**237.** Il 10 maggio 2026 il trattamento termico CCP2 sul lotto L26130 e' stato conforme?  
<sub>difficoltà 5</sub>

**238.** Qual e' stata la temperatura minima registrata sul PT-104 il 10/05/2026?  
<sub>difficoltà 5</sub>

**239.** Per quanto tempo il pastorizzatore e' rimasto sotto il limite critico il 10 maggio?  
<sub>difficoltà 5</sub>

**240.** Qual e' il numero dell'offerta Criotech per il tunnel di surgelazione?  
<sub>difficoltà 5</sub>

**241.** Quali sono le dimensioni di ingombro del tunnel Criotech CR-SP180?  
<sub>difficoltà 5</sub>

**242.** In quali domeniche di maggio 2026 ha lavorato la Linea 2?  
<sub>difficoltà 5</sub>

**243.** A quando risale l'ultima analisi di potabilita' dell'acqua?  
<sub>difficoltà 5</sub>

**244.** Quale clausola IFS e' stata violata secondo la NC 1 dell'audit CSQA?  
<sub>difficoltà 5</sub>


## Trappola — il dato NON è in archivio: la risposta giusta è dirlo

**245.** Qual e' stato l'utile d'esercizio 2026 di Aurora Food Group?  
<sub>difficoltà 2</sub>

**246.** Quanto prevede di fatturare Aurora nel 2027?  
<sub>difficoltà 3</sub>

**247.** Aurora Food Group e' certificata ISO 22000?  
<sub>difficoltà 3</sub>

**248.** Aurora ha la certificazione ambientale ISO 14001?  
<sub>difficoltà 3</sub>

**249.** Qual e' la data di assunzione di Ionut Popescu?  
<sub>difficoltà 3</sub>

**250.** Quanto costera' il nuovo stabilimento 'Aurora Vega'?  
<sub>difficoltà 3</sub>

**251.** Aurora ha gia' comprato il terreno a Minerbe?  
<sub>difficoltà 3</sub>

**252.** Dove trovo il piano industriale di Aurora Food Group?  
<sub>difficoltà 3</sub>

**253.** Quale gestionale ERP ha scelto Aurora, CSB-System o SAP Business One?  
<sub>difficoltà 3</sub>

**254.** Chi e' stato nominato referente privacy interno?  
<sub>difficoltà 3</sub>

**255.** Aurora ha un contratto di locazione per il magazzino di Via Palu' 3/A?  
<sub>difficoltà 3</sub>

**256.** Qual e' la ricetta completa del Cornetto Premium AF-CR-0212?  
<sub>difficoltà 4</sub>

**257.** A quanto ammonta la sanzione che l'ULSS ha comminato ad Aurora dopo l'ispezione del 9 giugno?  
<sub>difficoltà 4</sub>

**258.** Com'e' andato il sopralluogo di controllo dell'ULSS sull'adeguamento alle prescrizioni?  
<sub>difficoltà 4</sub>

**259.** UniCredit ha concesso l'ampliamento dell'anticipo fatture a 500.000 euro?  
<sub>difficoltà 4</sub>

**260.** Cosa e' stato deciso nell'incontro con il buyer Rossi del 19 maggio a Cerea?  
<sub>difficoltà 4</sub>

**261.** Tommaso Refosco e' stato assunto?  
<sub>difficoltà 4</sub>

**262.** Aurora ha la certificazione kosher per le sue referenze?  
<sub>difficoltà 4</sub>

**263.** Qual e' il numero di caso INAIL assegnato all'infortunio di Corradin?  
<sub>difficoltà 4</sub>

**264.** Come si chiama il concorrente pugliese che il buyer Tosano ha citato come alternativa sul cornetto?  
<sub>difficoltà 4</sub>

**265.** Quanto e' costata alla fine la riparazione della PKM-450 fatturata da Pakmatic?  
<sub>difficoltà 4</sub>

**266.** Com'e' andato l'audit di rinnovo BRCGS del 2026?  
<sub>difficoltà 4</sub>

**267.** Qual e' il numero e la scadenza del certificato biologico ICEA di Aurora?  
<sub>difficoltà 4</sub>

**268.** Quanti metri cubi d'acqua consuma lo stabilimento in un anno?  
<sub>difficoltà 4</sub>

**269.** Chi e' il secondo fornitore di private label che Tosano ha scelto di affiancare ad Aurora?  
<sub>difficoltà 4</sub>

**270.** Il nuovo tunnel Criotech e' stato collaudato?  
<sub>difficoltà 4</sub>

**271.** Qual e' l'esito della relazione annuale del medico competente?  
<sub>difficoltà 4</sub>

**272.** Il laboratorio ha confermato che il frammento trovato dalla consumatrice proviene dalla guarnizione montata da Dal Maso?  
<sub>difficoltà 5</sub>

**273.** Quando e' stato eseguito il ritiro dei lotti L26130 e L26131?  
<sub>difficoltà 5</sub>

**274.** Quanto e' costato effettivamente il ritiro del prodotto?  
<sub>difficoltà 5</sub>

**275.** Quanto vale l'export di Aurora e verso quali paesi?  
<sub>difficoltà 5</sub>


## Forma dell'archivio — domande sui file, non sul contenuto

**276.** Quante mail .eml ci sono in archivio e quali NON hanno allegati?  
<sub>difficoltà 3</sub>

**277.** Come e' composto l'archivio per formato di file?  
<sub>difficoltà 3</sub>

**278.** Ci sono file il cui nome contiene gia' un'istruzione o un giudizio su come trattarli?  
<sub>difficoltà 3</sub>

**279.** C'e' un documento firmato digitalmente in archivio?  
<sub>difficoltà 4</sub>

**280.** Qual e' il documento piu' vecchio dell'archivio?  
<sub>difficoltà 4</sub>

**281.** Quali documenti sono presenti in archivio in doppia copia con nomi diversi?  
<sub>difficoltà 5</sub>

**282.** Quali file dell'archivio non sono in UTF-8 e con quali separatori sono scritti i CSV?  
<sub>difficoltà 5</sub>

