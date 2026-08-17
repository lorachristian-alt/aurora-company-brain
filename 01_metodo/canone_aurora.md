# CANONE AURORA FOOD GROUP — chiave di lettura e sanity check

> **Cos'è** · L'unica fonte di verità della simulazione: valori canonici, persone col loro
> registro linguistico, filo rosso, contraddizioni volute (tre gruppi) e ciò che NON
> esiste in archivio.
> **Quando si usa** · In ogni sessione di generazione, canonizzazione o revisione: è
> l'arbitro di ogni dato.
> **Cosa non toccare** · I valori esistenti. Si può solo AGGIUNGERE, in sezioni datate;
> le contraddizioni registrate non si «correggono» mai: sono l'oggetto del test.
> **Mai dentro il vault né in alcun indice.** (File rinominato: ex `CANONE_AURORA.md`.)

⚠️ **Questo file NON va messo dentro `sources/`.** È l'unico documento pulito e completo
dell'intera simulazione: dentro l'archivio falserebbe qualunque test, perché conterrebbe già
tutte le risposte in forma ordinata. Serve a te per verificare se il sistema ha capito, non al
sistema per capire.

**Aurora Food Group S.r.l. non esiste.** Persone, fornitori, lotti, eventi e documenti sono
inventati. I nomi di aziende ed enti reali che compaiono nell'archivio (una catena della GDO,
un ente di certificazione, una banca, un'azienda sanitaria) sono usati come sfondo di una
vicenda interamente fittizia: nessun comportamento descritto è mai avvenuto.

---

## 1. ANAGRAFICA — i valori canonici

Tutti i codici sotto **superano i rispettivi algoritmi di controllo** (Luhn per la P.IVA,
modulo-10 GS1 per EAN/ITF, CIN italiano + MOD-97 per l'IBAN). Sono verificabili con qualunque
validatore online: è voluto.

| Dato | Valore canonico |
|---|---|
| Ragione sociale | **Aurora Food Group S.r.l.** |
| Sede e stabilimento | Via dell'Industria 27, **37044 Cologna Veneta (VR)** |
| P.IVA / C.F. | **03984710230** |
| REA / capitale | VR-389241 · 500.000,00 € i.v. |
| PEC · SDI | aurorafoodgroup@pec.it · **M5UXCR1** |
| Telefono | **0442 854122** (prefisso corretto per Cologna Veneta) |
| IBAN UniCredit | **IT33W0200859870000104882913** |
| Registrazione sanitaria | n. 037/2019/SIAN — ULSS 9 Scaligera |
| Dipendenti · fatturato 2025 | 50 · 11.480.312 € (bilancio depositato; le slide commerciali arrotondano a 11.480.000 — vedi § 4) |
| Certificazioni | BRCGS Food Issue 9 grade **AA** (cert. BRC/IT/24/00871) · IFS Food v8 **Higher Level 97,32%** · ente **CSQA** |

### Prodotti — codici e barcode canonici

| Codice | Descrizione | EAN-13 | ITF-14 cartone |
|---|---|---|---|
| AF-SN-0450 | Snack salato rustico multicereali 100 g ATM | 8034123450123 | 18034123450120 |
| AF-SN-0455 | Snack salato rustico 100 g promo 3+1 | 8034123454558 | 18034123454555 |
| AF-CR-0212 | Cornetto Premium burro 6×50 g surgelato | 8034123452127 | 18034123452124 |
| AF-CR-0215 | Cornetto Premium PL 8×45 g surgelato | 8034123452158 | 18034123452155 |
| AF-CR-0220 | Sfogliatina bio ai cereali | 8034123452202 | 18034123452209 |
| AF-FC-0330 | Focaccina olio EVO 2×90 g ATM | 8034123453308 | 18034123453305 |
| AF-SN-0401 · AF-CR-0210 | articoli **obsoleti**, mai cancellati dall'anagrafica | 8034123440117 · 8034123452103 | — |

### Formato del lotto
`L26<giorno giuliano a 3 cifre>-<linea>-<turno>` — es. **L26130-L1-T2** = 10/05/2026, Linea 1, turno 2.
Corrispondenze: 124 = 04/05 · 128 = 08/05 · **130 = 10/05 (domenica)** · 131 = 11/05 · 132 = 12/05.
La croissanteria porta lotti **-L2-**; il piano di produzione assegna però AF-CR-0212 alla
Linea 3, che è la fase di surgelazione. Il passaggio nel tunnel non cambia il codice di
lotto, ma i due documenti vanno letti insieme.

### CCP — identici in tutto l'archivio
- **CCP1** setacciatura farina 800 µm + magnete 10.000 Gauss
- **CCP2** trattamento termico PT-104: **T al cuore ≥ 72,0 °C per ≥ 2 min** (set point 74-76 °C)
- **CCP3** metal detector MD-3200: **Fe 2,0 / NFe 2,5 / AISI 316 3,0 mm**, verifica **ogni 60 min** su MOD-QA-07 rev.5
- **CCP4** surgelazione: T al cuore ≤ −18 °C entro 240 min

---

## 2. LE PERSONE

| Nome | Ruolo | Firma riconoscibile |
|---|---|---|
| **Giancarlo Bertoldi** | Fondatore e AD, 63 anni | maiuscole, niente punteggiatura, scrive a tarda notte |
| **Silvia Bertoldi** | Direzione commerciale (figlia) | «non scrivere mai la parola difetto» |
| **ing. Marco Fantin** | Direttore di stabilimento | telegrafico, decide e chiude |
| **dott.ssa Elena Marchetti** | Responsabile Qualità, team leader HACCP | burocratese, cita le norme, insiste |
| **Sara Pozzato** | Assistente qualità / laboratorio | compila i registri |
| **Denis Zanella** | Responsabile produzione | |
| **Ionut Popescu** | Capoturno Linea 1 | italiano imperfetto, quaderno a mano |
| **Adel Ben Salah** · **Roberto Guerra** | Capoturni Linea 2 e 3 | |
| **Ivano Dal Maso** | Capo officina | veneto stretto, peggiora sotto pressione |
| **Mirco Bissoli** | Manutentore, turno notte | |
| **Nicola Faggionato** | Responsabile magazzino e spedizioni | |
| **rag. Luisa Trentin** | Amministrazione | note tra parentesi dentro i fogli Excel |
| **Federica Sartori** | HR e segreteria (part-time) | |
| **dott. Alberto Zanchetta** | R&D, tecnologo | |
| **Giulia Meneghello** | Tirocinante R&D (tesi UNIPD) | |
| **Paolo Zampieri** | Agente di vendita GDO | appunti sul blocco |
| **Emanuele Corradin** | Operaio Linea 3 | infortunato il 28/04/2026 |
| **Paolo Bertacco** | Operaio Linea 2, **RLS** | |
| esterni | **p.i. Sergio Bonato** (RSPP) · **dott.ssa Chiara Vicentini** (HACCP) · **dott. Andrea Bellotto** (commercialista) · **dott. Guido Salvalaio** (medico competente) | |
| cliente | **dott.ssa Anna Perbellini** (QA) · **Mario Rossi** (buyer) · **Luca Vantini** (CE.DI.) | |
| consumatrice | **Milena Grigolon**, Bussolengo — autrice del reclamo | |

---

## 3. IL FILO ROSSO — la storia che l'archivio lascia ricostruire

Nessun documento la racconta per intero. Questa è la sequenza vera, da usare come metro.

1. **17-18/02/2026 — audit CSQA.** Grade AA con **2 NC minori** (più 5 osservazioni):
   NC 1 = registrazioni CCP senza verifica in seconda firma (BRCGS cl. 2.10.2 / IFS 2.3.9.2);
   NC 2 = ricambi e attrezzi di manutenzione tenuti in area produttiva (cl. 4.7.5).
   Le evidenze di chiusura vengono trasmesse **in ritardo, il 02/04/2026**.
2. **Aprile-maggio** — promo «Sottocosto Primavera» del cliente principale: Linea 2 lavora
   **tre domeniche di fila**, sei operai in **proiezione** di superamento del limite annuo (l'azienda ne conta cinque sopra le 200 ore al 30/04, il sindacato sei: i conteggi non coincidono) → contestazione RSU.
3. **08/05** — Dal Maso segnala che la **valvola di iniezione azoto della PKM-450 perde**.
   Il ricambio originale Pakmatic arriva solo il 15/05. Si va avanti lo stesso.
4. **10/05 (domenica), Linea 1, lotto L26130**:
   - **14:20:07-14:44:37** secondo il datalogger il PT-104 scende sotto i 72 °C (minimo
     **68,9 °C al cuore**); la non conformità interna e la nota della responsabile qualità
     scrivono invece 14:18-14:47 — vedi § 4, vince il datalogger: deviazione CCP2
     registrata dal datalogger. Sul registro cartaceo l'operaio scrive «74,5 conforme» → **la NC 1
     dell'audit si materializza**.
   - **15:05** si rompe la valvola azoto: **fermo di 3h40**, OEE del turno crollato a 36,5.
   - **18:45** Dal Maso ripara con una **guarnizione azzurra non originale** presa dal carrello
     ricambi tenuto a bordo linea → **la NC 2 dell'audit si materializza**.
   - Il metal detector non rileva la plastica: non è metallica.
5. **12/05** — reclamo dal form del sito: **Milena Grigolon** trova un frammento di **plastica dura
   azzurra (~9×4 mm)** in uno snack AF-SN-0450 lotto L26130. Pratica **REC-2026-011**.
6. **14/05** — la QA del cliente chiede una relazione scritta **entro 48 ore** (scadenza sabato 16).
   Si valuta il ritiro cautelativo. **Perimetro del blocco: ~8.400 confezioni** — solo il prodotto
   confezionato dopo il riavvio delle 18:45, non i lotti interi — di cui ~5.100 già a scaffale.
   Costo stimato del ritiro: 31.500 €.
7. **15/05** — la guarnizione viene sostituita con l'originale: **mancano ~2 cm² di materiale**.
   Restano da valutare i lotti prodotti dal 12 al 15/05 (L26132-L26134): **non ancora fatto**.
8. **In parallelo, la cassa**: il cliente paga a **90 giorni**, mentre scade l'**acconto del 30%
   (87.000 € su 290.000)** per il tunnel di surgelazione. Il previsionale va sotto l'affidamento.
9. **05/05** — il buyer chiede **−4,5% sul listino** più **12.000 € di listing fee**: su AF-CR-0215
   il margine industriale andrebbe **sotto zero**.
10. **09/06** — ispezione dell'autorità sanitaria (verbale 2026/SIAN/00214): tre rilievi, due prescrizioni con scadenza e una **diffida** sul carrello ricambi tenuto a bordo della confezionatrice — la NC 2 dell'audit torna per la terza volta. Nessuna sanzione comminata.
11. Sullo sfondo: 4 dimissioni in 5 mesi sulla Linea 2, un infortunio lieve (Corradin, 28/04,
    12 giorni), il progetto del nuovo stabilimento «Aurora Vega» e i preventivi per l'ERP.

---

## 4. LE CONTRADDIZIONI VOLUTE

Queste **non sono errori**: sono trappole deliberate. Un sistema che risponde con un solo valore
senza segnalare il conflitto sta indovinando, non ragionando.

| Contraddizione | Dove | Risposta corretta |
|---|---|---|
| **Due listini** con prezzi diversi | `listino_prezzi_canale_GDO_fresco_v3.csv` (valido) e `listino prezzi GDO v2 VECCHIO non usare.csv` (superato dal 01/03/2026) | vale la **rev. 3**; il v2 è storico |
| **Due previsionali di cassa** | `previsionale_cassa_giugno_agosto2026.xlsx` e `previsionale cassa giugno-agosto DEF (2).xlsx` | vale quello **senza «(2)»**: la copia lo dichiara nel foglio Ipotesi |
| **Fatturato dichiarato in due modi** | slide commerciali vs bilancio | il dato buono è quello del **bilancio depositato** |
| **Pezzi/cartone di AF-SN-0450** | scheda tecnica (10) vs listino e accordo quadro (12) | conflitto reale mai risolto in azienda |
| **Lo stesso documento in due file** | quattro coppie: `certificato_analisi_lotto_farina_MV26_0429A.pdf` ≡ `SKM_C224e26051412340.pdf`; `DoC_MOCA_Flexipack_film_PP_EVOH_2026.pdf` ≡ `doc 2 (1).pdf`; `Rapporto_di_Prova_AnalyticaVeneta_2026_04187.pdf` ≡ `Scansione_20260518_0003.pdf`; `DDT_Euroglass_Boccacci_Vetro_N99201.txt` ≈ `img20260428_09241055.txt` | sono **duplicati**, non documenti diversi |
| **Il mass balance non quadra** | `tracciabilita_lotti_massbalance_L26130.xlsx` | lo scostamento è **dichiarato e non spiegato**: è il punto della storia |
| **Registro cartaceo vs datalogger** | MOD-QA-12 dice «74,5 conforme», il log dice 68,9 °C | **vince il datalogger**; la discrepanza è il cuore del caso |

---

## 5. COSA NON ESISTE NELL'ARCHIVIO

Serve per le domande-trappola: a queste la risposta corretta è **«non presente in archivio»**.

- Nessuna certificazione **ISO 22000 o ISO 9001 di Aurora** (quelle in archivio sono dei
  fornitori), nessun **biologico di stabilimento**
  (solo BRCGS, IFS e una certificazione bio limitata a una referenza).
- Nessun **bilancio 2026** (l'ultimo depositato è il 2025) e nessun **obiettivo di fatturato**
  2027: esiste però una proiezione dei ricavi ricorrenti sui contratti in essere.
- Nessun **contratto di lavoro individuale**, nessun cedolino nominativo completo
  (solo un estratto del libro unico).
- Nessun **export ufficiale** verso l'estero: i contatti esteri sono solo lead di fiera.
- Nessuna **sanzione comminata** (esiste però una diffida con prescrizioni) e nessun
  contenzioso **giudiziale**: quello sulle pedane è commerciale, e la denuncia INAIL di
  infortunio esiste.
- Nessun **preventivo, computo o business plan** su Aurora Vega: esistono la localizzazione
  a Minerbe (VR), una valutazione «meramente esplorativa» a verbale del CdA e un accenno
  nella job description.
- Nessun **organigramma aggiornato dopo marzo 2026**, nessun piano industriale formale.
- Nessuna **ricetta completa** del cornetto premium (solo lo snack in sviluppo).

---

## 6. COM'È FATTO L'ARCHIVIO

159 documenti, 6.2 MB, 11 formati: `.txt` 50 · `.csv` 30 · `.pdf` 27 · `.xlsx` 15 · `.eml` 12 · `.docx` 11 · `.jpg` 4 · `.pptx` 4 · `.log` 3 · `.xml` 2 · `.p7m` 1
In cartella c'è anche `_QUESTO_ARCHIVIO_E_SIMULATO.txt`, un'avvertenza che non fa parte del corpus.
`.docx` 11 · `.jpg` 4 · `.pptx` 4 · `.log` 3 · `.xml` 2 · `.p7m` 1.

Caratteristiche volute, che una pipeline deve saper reggere:
- **encoding misto** — 6 file di testo sono in `cp1252` con terminatori CRLF;
- **OCR degradato** su 5 documenti scansionati (`0`↔`O`, accenti rotti, righe storte);
- **date in tre formati** nello stesso file (`10/05/26`, `2026-05-10`, `10-mag-26`);
- **separatori CSV incoerenti** (`;` e `,`), decimali con la virgola, header ripetuti a metà file;
- **allegati veri dentro le mail** `.eml` (il PDF citato è davvero allegato, in base64);
- **metadati coerenti con l'emittente**: la visura dice InfoCamere, il CPI dice Vigili del Fuoco;
- **rumore di fondo**: ~22 file (menù della trattoria convenzionata, cancelleria, condominio, palestra) che non
  c'entrano nulla con la storia e servono a impedire che il retrieval «indovini per contesto».


## Contraddizioni verificate e volute (secondo gruppo)

Queste divergenze sono reali nell'archivio e vanno trovate, non corrette. Sono state
riscontrate una per una sui documenti: chi risponde citando una sola delle due fonti
sbaglia, anche quando la fonte che cita esiste davvero.

| Cosa diverge | Dove | Valore da preferire |
|---|---|---|
| Aumento del listino farine | `Listino_MolinoVeneto_giu2026.pdf` applica +9,8% sulla W300 e percentuali diverse per referenza; `contratto_fornitura_MolinoVeneto_2026_firmato.pdf` art. 3.2 impone una formula unica che dà +8,8% | Il contratto. Lo scarto sulla sola W300 vale 4.200-5.100 EUR/anno |
| Prezzo base della semola | Contratto art. 3.1: 655,00 EUR/t; listino, colonna «in vigore»: 66,10 EUR/q.le | Il contratto (655,00) |
| Barriera al vapore del film | DoC Flexipack dichiara WVTR ≤ 4,5 g/m²·24h; il capitolato `CTF-IMB-02 rev. 4` sottoscritto da entrambe richiede ≤ 4,0 | Il capitolato. Il film in uso non soddisfa la specifica firmata |
| Esito dei lavaggi CIP | `log_lavaggio_CIP_linea1_maggio.log` chiude PASS 18 cicli su 28 con risciacquo finale sopra il limite di IO-05 (536 µS/cm), e due cicli con la sonda in `FAULT` | IO-05. Il criterio di accettazione non è implementato nel pannello |
| Portata del CIP | Log: 8,4-10,0 m³/h su 170 letture; IO-05 prescrive 15 m³/h | IO-05. Le condizioni della validazione di pulizia non sono mai raggiunte |
| Allarmi della cella surgelati | Sei allarmi in escalation da -16,1 a -11,4 °C fra il 10 e il 26/04, cinque con `ACK=NO`; nessuna NC aperta nel registro | Il log. L'anomalia CF-02 segnalata il 12/05 era leggibile un mese prima |
| Integrità del log cella | I record di apertura allarme contengono già `DUR=` della durata totale: il file è stato scritto a posteriori, e dopo il riavvio del 21/04 l'orologio è `RTC=NOSYNC` | Nessuno. Il log non è utilizzabile come evidenza in audit |
| DDT Molino Veneto n. 48392 | `SKM_C224e26050408520.jpg` dà 12 colli da 1.000 kg, targa BF 442 XY, «merce ok»; `DDT_MOLINO_VENETO_..._OCR_SPORCO.txt` dà 480 sacchi da 25 kg, targa EV 512 KT, un sacco lacerato e un lotto segregato | Nessuno dei due da solo. Il lotto segregato MV26-0430/A è in carico alla Qualità e va cercato |
| Misura del frammento | `MOD-QA-31` verbalizza ~9 × 4 mm «da fotografia»; sulla foto, col riferimento metrico, il frammento misura ≈ 7,3 × 5,0 mm | La foto. La classificazione non cambia, il dato verbalizzato sì |
| Codice dell'allarme PKM-450 | La foto del pannello mostra `E-214 GAS`; il rapporto di fermo macchina scrive `AL-217` | Da riconciliare sul manuale: l'archivio non lo risolve |
| Budget 2026 | Le slide dicono 13,2 mln; `budget_2026_vs_consuntivo_per_linea.xlsx` totalizza 4.151.378 EUR e l'analisi di marginalità converge su ≈ 4,8 mln | Nessuno. Il perimetro del file budget non è dichiarato |
| Costo ingredienti dello snack nuovo | Il business case per AF-SN-0470 mette 0,26 EUR/pz; la marginalità costa AF-SN-0450, stessa linea e ricetta più povera, a 0,5478 | La distinta base. Col dato vero il margine passa dal 35% al 7,6% |
| Domeniche di produzione della promo | La conferma d'ordine dice 26/04, 03/05 e 10/05; il verbale RSU e i consumi dei forni dicono 03, 10 e 17/05 | La conferma d'ordine per la promo (le consegne del mercoledì tornano); i consumi restano un dato fisico da spiegare |
| Firma della fattura elettronica | `IT03984710230_00215.xml.p7m` incapsula l'XML in una `SignedData` ben formata, ma senza certificato X.509 né `signedAttrs` | È un contenitore, non una prova di firma: nessun verificatore CAdES lo accetta |
| Revisione del manuale HACCP | Intestazione «REVISIONE 4 del 15/01/2024», piè di pagina «rev.5», matrice interna fino a «Rev. 5 - 08/04/2026» | La matrice delle revisioni (rev. 5) |

### Un caso che sembra un errore e non lo e': i consumi energetici

`consumi_energetici_forni_kwh_maggio26.csv` non supera una verifica aritmetica ingenua:
in 59 righe su 186 la somma delle tre fasce non fa il totale, e in 137 il costo non e'
esattamente totale x tariffa. **Non e' un difetto.** Il contatore misura valori con
decimali: le colonne F1, F2, F3 e il totale sono arrotondamenti all'intero, mentre il
costo e' calcolato sul consumo reale. Dividendo il costo per la tariffa si ottiene il
consumo vero, e su **165 righe su 165** la somma delle fasce cade entro 1,5 kWh da quel
valore, come deve essere sommando tre arrotondamenti.

Chi analizza questo file deve accorgersene: rispondere "il file contiene 137 errori di
calcolo" e' sbagliato quanto non verificarlo affatto.


## Contraddizioni verificate e volute (terzo gruppo)

Emerse dalla revisione integrale dei 160 file. Come le precedenti: **sono nell'archivio
apposta**, e chi risponde citando una sola fonte sbaglia.

| Cosa diverge | Dove | Valore da preferire |
|---|---|---|
| Data di pagamento dell'acconto Criotech (87.000 EUR) | CapEx, scadenzario e previsionale dicono 15/05; gli ordini d'acquisto 25-26/05; l'estratto conto UniCredit registra il bonifico il **20/05** | L'estratto conto: il saldo progressivo quadra al centesimo, e il 15/05 il conto non aveva copertura |
| Pezzi del lotto L26130-L1-T2 | Mass balance: 8.940 pezzi · foglio OEE, stesso turno: 5.580 prodotti / 5.250 conformi | Nessuno dei due da solo. Il mass balance regge la quadratura BRCGS, l'OEE regge D×P×Q: la divergenza va dichiarata |
| Straordinari gennaio-aprile | Il `Prospetto_straordinari` si dichiara derivato dal libro unico ma non coincide: 3.446 ore contro 3.544, e cinque persone sopra le 200 ore contro sei | Il libro unico. Il prospetto e' l'estratto che il sindacato ha in mano |
| Costo industriale per referenza | Il listino GDO e la distinta base danno valori diversi su quattro referenze su sei (AF-CR-0212: 1,92 contro 1,62; AF-FC-0330: 0,94 contro 0,485) | La distinta base, che e' analitica; ma i margini gia' presentati in trattativa nascono dal listino |
| Prezzo di vendita a Tosano dello stesso articolo | Listino rev.3 0,89 · listino rev.2 0,8615 · anagrafica di gestionale 0,86 · proiezione ARR 0,79 | Il listino rev.3. Il gestionale e' fermo alla rev.2 superata dal 01/03/2026 |
| Impianto assicurativo | La polizza in archivio e' Novaria (RC prodotti 5 mln, scadenza 30/06/2026); il report OpEx parla di Generali e AIG, e apre un sinistro su una polizza che non esiste in archivio | La polizza. Il report OpEx e' appunti dichiaratamente provvisori |
| Sviluppo dello snack AF-SN-0470 | Il file ricetta data la v12 al 16/04 con paprika Italspezie; il quaderno di laboratorio la prova l'11/05 con paprika La Dehesa, e la mail del 07/05 dice «parte la settimana prossima» | Il quaderno e la mail: sono contemporanei ai fatti |
| Velocita' nominale delle linee | Piano di produzione: 1.250 / 780 / 640 pz/h · foglio OEE: 1.800 e 1.200 pz/h | Da riconciliare: cambia ogni saturazione e ogni performance |
| Costo dell'energia elettrica | 0,182 EUR/kWh nei consumi mensili · 0,205 nel CapEx, dichiarato «media contratto gen-apr» | Il payback del tunnel dipende da quale sia vero |
| Domeniche lavorate a maggio | Il libro unico ne conta **due** (10 e 17) e paga 16 ore festive; consumi, budget e verbale RSU ne contano **tre** (3, 10, 17); la conferma d'ordine dice 26/04, 03/05, 10/05 | Tre versioni, con una conseguenza retributiva: 8 ore festive per persona non liquidate |
| Costo della non qualita' gen-mag | 24.420 EUR nel cruscotto · 29.600 nel budget · 39.500 nel foglio «NC per causa» · 135.793 sommando il registro NC | Il registro e' l'unico analitico, ma include stime; il cruscotto conta solo le NC chiuse |
| Classifica dei fornitori | Molino Veneto e Analytica Veneta hanno lo stesso punteggio (88,2): la formula `MATCH(...;0)` prende sempre il primo, cosi' Molino compare due volte e Analytica sparisce | Un pari merito gestito male da una formula: e' il tipo di errore che nessuno nota |
| Revisore legale | La visura dice Peruffo Maria Grazia, n. 148223, nomina 28/04/2025; il bilancio dice Maurizio Peruzzi, n. 118442, nomina 14/05/2024 | Nomi quasi omografi ma persone diverse: prevale l'iscrizione al Registro Imprese |
| Organico e turni della Linea 2 | Il piano di produzione presuppone 21 persone su tre turni; libro unico e timbrature ne registrano 10 su due turni; il verbale RSU dice «10 a fronte delle 12 previste» | Il libro unico. Il terzo turno di Linea 2 esiste solo nel piano |
| Operatori del pastorizzatore | Il log cita RANZATO_F e CESTARO_L, che non hanno badge nel file timbrature ne' matricola nel libro unico (ma compaiono nell'ordine DPI) | L'export delle timbrature e' parziale senza dichiararlo |


## Aggiunte del 16/08/2026 — contraddizioni emerse in Sessione 1

Registrate applicando la procedura di **categoria B** di `metodo_03_canonizzazione.md`
§9.5: divergenza reale del corpus, non elencata nei tre gruppi precedenti, trovata
mentre si scriveva il manuale di canonizzazione. **I grezzi non sono stati toccati.**
Come le altre: sono nell'archivio, vanno trovate e dichiarate, non corrette.

| Cosa diverge | Dove | Valore da preferire |
|---|---|---|
| **Data della riunione di direzione** | `Convocazione_riunione_direzione_12_05.eml` (inviata ven 08/05/2026 16:20) convoca per **martedi 12/05/2026 ore 9:30**, con un ordine del giorno di sei punti in cui il reclamo non compare; il file `trascrizione_riunione_direzione_12_05_2026.txt` porta 12_05 nel nome ma dichiara in prima riga «riunione direzione **13 05 2026**», cita il file audio `REC_20260513_1732.m4a` (13/05, ore 17:32) e si apre sul reclamo arrivato «ieri sera alle 18 e 23» | **Il contenuto della trascrizione: 13/05.** Tre segnali interni concordi (prima riga, nome del file audio, «ieri sera»). La convocazione documenta la riunione **convocata**, non quella **tenuta**, e il nome del file segue la convocazione. ⚠️ L'archivio **non dice** se la riunione del 12/05 sia stata rinviata o se se ne siano tenute due: quella parte resta una questione aperta |
| **Data di apertura del reclamo REC-2026-011** | `MOD-QA-31_reclamo_REC-2026-011.pdf` dichiara «Data apertura **12/05/2026**»; la mail di Marchetti del **13/05 08:41** annuncia «Ho aperto il reclamo n. REC-2026-011» e la trascrizione del 13/05 dice «alle 9 e 22 ho aperto la pratica» | **Da riconciliare.** La scheda data l'apertura al giorno del reclamo, la responsabile qualita' la colloca il mattino dopo. Coerente con la prassi di compilare i moduli con la data dell'evento anziche' della registrazione, ma l'archivio non lo dichiara |


## Aggiunte del 16/08/2026 — contraddizioni emerse in Sessione 2 (fetta pilota L26130)

Registrate applicando la procedura di **categoria B** di `metodo_03_canonizzazione.md`
§9.5: divergenze reali del corpus, non elencate nei gruppi precedenti, trovate dal
revisore indipendente mentre si canonizzava la fetta pilota del caso L26130. **I grezzi
non sono stati toccati.** Come le altre: sono nell'archivio, vanno trovate e dichiarate,
non corrette. Ciascuna ha gia' la sua nota-questione nel vault.

| Cosa diverge | Dove | Valore da preferire |
|---|---|---|
| **Termine minimo di conservazione del lotto di farina MV26-0429/A** | `certificato_analisi_lotto_farina_MV26_0429A.pdf` §1 → **29/12/2026**, dichiarato come «8 mesi in sacco/silo» dalla macinazione del 29/04; `tracciabilita_lotti_massbalance_L26130.xlsx` foglio «A monte» riga 6 → **04/11/2026**; `inventario_magazzino_scadenze_FEFO_maggio.csv` riga 5 → **30/10/2026** | **Nessuno.** Solo il certificato del fornitore dichiara il criterio con cui la data e' ottenuta; i due documenti interni non lo dichiarano e divergono anche fra loro di cinque giorni. E' la data su cui si decide l'ordine di prelievo in logica FEFO |
| **Modo di consegna dello stesso lotto di farina** | Il certificato del molino dichiara consegna **sfusa in autocisterna**, DDT n. **1187/26 del 05/05/2026**, **28.400 kg**; mass balance e inventario registrano **DDT 48392 del 04/05/2026** e **sacchi da 25 kg** a scaffale | **Nessuno.** Sfuso e insaccato non possono coesistere per la stessa merce, e i DDT citati sono due. Le due letture possibili — partita unica spedita in due forme, oppure errore di trascrizione nella ricostruzione compilata in emergenza — non sono decidibili sull'archivio |
| **Materiale della guarnizione montata sulla PKM-450 il 10/05** | Trascrizione 13/05 [00:02:24] e [00:12:39] → **silicone**; risposta scritta di Dal Maso del 13/05 13:47 allegata al MOD-PR-04 → **«gomma»**, senza datasheet ne' marca; `Rapporto_di_Prova_AnalyticaVeneta_2026_04187.pdf` §4.2-4.3 → **polimero fluorurato** (PTFE e/o FKM), con assenza di bande poliolefiniche | **Nessuno, e le fonti non parlano dello stesso oggetto**: le prime due descrivono la guarnizione montata, la terza il frammento del reclamo. Silicone e fluoropolimero sono materiali diversi: se la guarnizione fosse in silicone il frammento non potrebbe venire da essa. Nella stessa mail Dal Maso afferma che la guarnizione provvisoria e' ancora montata e tiene, e che i pezzi della guarnizione **vecchia** disintegrata erano l'originale Pakmatic — kit che monta guarnizioni dichiarate in PTFE |
| **Codice del kit valvola azoto originale** | `report_fermo_macchina_confezionatrice_MAP.txt` → «kit valvola orig. Pakmatic cod. **PK45-VN2-08**», ripetuto nella RDA approvata; `R_ricambio_valvola_iniezione_azoto_PKM450_URGENTE.eml` (Pakmatic, 08/05 16:55) → gruppo **PKV-088-N2**, kit **PKV-088-KIT** | **Da riconciliare.** Le due fonti concordano su tutto il resto e divergono solo sulla sigla: la spiegazione piu' semplice e' codice interno contro codice di catalogo, ma nessun documento mette i due codici uno accanto all'altro |
| **Ora di arrivo della segnalazione dal form del sito** | La trascrizione del 13/05 [00:00:37] colloca l'arrivo «ieri sera alle **18 e 23**», cioe' il 12/05 alle 18:23; ma dentro `RE_RE_URGENTE_reclamo_corpo_estraneo_lotto_L26130.eml` la catena porta un messaggio sullo stesso oggetto inviato **martedi 12 maggio alle 17:55**, ventotto minuti prima | **Da riconciliare**, insieme alla divergenza gia' registrata sulla data di apertura: la corrispondenza interna sul reclamo comincia prima dell'ora in cui il reclamo sarebbe arrivato |
| **Misura del frammento: la terza lettura** | Alla coppia gia' registrata (`MOD-QA-31` ~9 x 4 mm «da fotografia» contro la foto col riferimento metrico, dove il frammento e' piu' corto e piu' largo) si aggiunge il **rapporto di prova**, §4.1: **9,2 x 4,1 x 1,8 mm**, massa 0,081 g, misura strumentale al microscopio su campione fisico | **Resta valido l'arbitrato gia' registrato sulla coppia scheda/foto** (vince la foto: una stima non puo' contraddire il documento da cui dichiara di essere tratta). Fra **foto e laboratorio**, invece, **nessuno**: il rapporto fra i due lati si inverte e l'archivio non spiega lo scarto — orientamento del frammento, ortogonalita' dello scatto e convenzione di misura del laboratorio non sono affermati da nessun documento |
