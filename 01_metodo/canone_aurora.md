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


## Aggiunte del 18/08/2026 — contraddizioni emerse in Sessione 4, lotto 1A (Linea 1: turno, CCP, confezionatrice)

Registrate applicando la procedura di **categoria B** di `metodo_03_canonizzazione.md` §9.5:
divergenze reali del corpus, non elencate nei gruppi precedenti, trovate dal revisore
indipendente sui sette grezzi del lotto 1A. **I grezzi non sono stati toccati.** Ciascuna ha
gia' la sua nota nel vault.

⚠️ **Tre di queste righe aggiungono gambe a divergenze gia' registrate**, e due di esse
**tolgono credibilita' a una spiegazione che il canone aveva accolto**. Vale il precedente
fissato il 16/08 con «Misura del frammento: la terza lettura»: il canone si accresce, la
riga vecchia resta dov'e', e la nuova dice cosa e' cambiato.

| Cosa diverge | Dove | Valore da preferire |
|---|---|---|
| **Limite dell'ossigeno residuo in confezione: 1,0 % contro 2,0 %** | `Scheda_tecnica_prodotto_AF-SN-0450_rev4.pdf` pag. 2 §3 → obiettivo < 0,7 %, **massimo 1,0 %**; `non_conformita_interne_registro_2026.csv` → **target 2,0 %** in due voci, `NC-2026-038` del 02/03 («2,8% oltre target 2,0%») e `NC-2026-082` del 04/05 («2,4% su target 2,0%»); `appunti_capoturno_quaderno_linea1_OCR.txt` pag. 43, ven 8/5 → «(lim 2%)» | **Nessuno.** Non e' un operatore che sbaglia soglia: il 2,0 % e' la soglia su cui l'azienda **apre e chiude non conformita' vere**, con costo a consuntivo, e `NC-2026-082` porta la sigla dello stesso capoturno che quattro giorni dopo scrive «lim 2%». Documento contrattuale e pratica interna reggono due sistemi paralleli, e nessuna fonte dichiara quale prevalga. ⚠️ La scheda **non dichiara nemmeno a quale momento** della vita del prodotto valga il tetto |
| **Attivita' dell'acqua e umidita' dello stesso prodotto, in due ordini di grandezza** | Scheda tecnica pag. 2 §3 → **aw 0,93** (0,92-0,95), **umidita' 32 g/100 g** (max 34), pH 5,8; `Rapporto_di_Prova_AnalyticaVeneta_2026_04187.pdf` pag. 3 §3, sul lotto L26130 → **aw 0,936** ± 0,006 e **umidita' 31,6 g/100 g** ± 0,8, entrambe dichiarate **CONFORMI** con metodo normato; `test_shelf_life_accelerata_confezione_MAP_snack.csv` riga 3 e seguenti → **aw 0,31**, **umidita' 5,6 %**, pH 5,71, e su tutte le letture l'aw non supera mai 0,39 | **La scheda tecnica, confermata dal laboratorio accreditato.** ⚠️ **L'anomalia sta nel file delle prove di shelf life**, non nella scheda: due misure ufficiali concordano fra loro e la terza no. Il pH coincide su tutte e tre — 5,8 · 5,74 · 5,71 — quindi parlano dello stesso prodotto. Il file non dichiara metodo diverso ne' porzione diversa del campione, e nessuna nota di analisi segnala lo scarto. Pesa perche' **quel file e' la base della proposta di portare il TMC a sei mesi** |
| **Materiale della guarnizione ORIGINALE della valvola azoto: PTFE, FKM o EPDM** | `R_ricambio_valvola_iniezione_azoto_PKM450_URGENTE.eml` → «guarnizioni **PTFE** alimentari»; `manuale_uso_manutenzione_PKM450_estratto.pdf` pag. 2 §3.5 e pag. 5 §7 → «guarnizione a labbro… (**FKM** nera)»; `scheda_manutenzione_ordinaria_forni_industrial.csv` riga 26 → cod. `PKM-4471-**EPDM** (orig. Pakmatic)` | **Nessuno.** ⚠️ **Questa riga tocca una premessa gia' registrata il 16/08**: il canone accoglieva l'affermazione dell'officina secondo cui il kit originale monta guarnizioni in PTFE. Quella premessa ha ora due fonti contro, e l'**EPDM non e' un fluoropolimero**: se l'originale fosse in EPDM non potrebbe produrre lo spettro misurato dal laboratorio sul frammento, e l'argomento difensivo cade. Si registra la divergenza, non una nuova conclusione |
| **Codice del ricambio della valvola azoto: da due sigle a quattro** | Alle due gia' registrate si aggiungono: `manuale_uso_manutenzione_PKM450_estratto.pdf` → valvola completa **`PK-45.0770`** e guarnizione a labbro **`PK-45.0771`** (l'unica fonte che distingue i due articoli); `scheda_manutenzione_ordinaria_forni_industrial.csv` riga 26 → **`PKM-4471-EPDM`** | **Da riconciliare, e la spiegazione registrata non regge piu'.** Il canone attribuiva la divergenza a «codice interno contro codice di catalogo»: con quattro sigle, **due delle quali vengono dal costruttore stesso** e non coincidono fra loro, quella spiegazione esce dal novero delle plausibili. Nessun documento mette due di quei codici uno accanto all'altro |
| **Codice dell'allarme PKM-450: la terza codifica, e l'assenza da supposta a verificata** | Alla coppia `E-214 GAS` / `AL-217` il `manuale_uso_manutenzione_PKM450_estratto.pdf` pag. 5 §8 aggiunge **`A031` «allarme pressione gas»**, causa «pressione ingresso sotto 1,8 bar» | **Resta: nessuno.** `A031` descrive esattamente il guasto del 10/05 e non coincide con nessuno dei due. ⚠️ Fatto nuovo e utile: il colophon del manuale dichiara che **l'elenco allarmi completo sta nel manuale integrale di 184 pagine, che in archivio non c'e'**. La ricerca su tutti e 160 i file del manifest v1.1 con l'estrattore congelato da' due sole occorrenze, nessuna delle quali e' una tabella |
| **Il tassello AISI 316 non rilevato al primo colpo: 05/05 o 07/05?** | `checklist_metal_detector_manuale_operaio.txt`, 05/05 turno 2 ore 17:00 → «inox nn passato al 1° colpo?? rifatto -> ok», con «tassello AISI messo storto»; `appunti_capoturno_quaderno_linea1_OCR.txt` pag. 42, gio 7/5 → stesso episodio con la stessa spiegazione, ma alle 18 del 07/05; lo stesso modulo il 07/05 alle 18:00 → esito **regolare**, nessuna annotazione | **Nessuno.** O il capoturno ha annotato con due giorni di ritardo sulla giornata sbagliata, o gli episodi sono stati **due** e il secondo non e' mai arrivato sul modulo di un CCP. La seconda lettura e' la grave |
| **La Linea 1 ha prodotto una domenica che il piano non le assegnava** | `piano_produzione_settimanale_sett19_21.xlsx` foglio «Sett 19» righe 42-43 → per dom 10/05 **due sole righe, entrambe Linea 2**; riga 48, a penna → «il 10/05 turno 2 linea 1 SALTATO dalle 15 - confezionatrice ferma»; `checklist_metal_detector_manuale_operaio.txt` FOGLIO 8 → **tre turni** di Linea 1 quel giorno | **Nessuno.** E' una divergenza fra pianificato ed eseguito che sta dentro lo stesso file, e allarga il perimetro delle domeniche lavorate a maggio — gia' contraddizione registrata, ma sul solo versante della Linea 2. L'archivio non dice **chi** abbia aggiunto la Linea 1 |
| **Ora di arrivo dell'officina al fermo del 10/05: 15:25 o 15:50** | `report_fermo_macchina_confezionatrice_MAP.txt` §2 → constatazione del capo officina alle **15:25**; `appunti_capoturno_quaderno_linea1_OCR.txt` pag. 44 → «ariva ore **15.5O circa**» | **Nessuno.** Le due fonti hanno posizioni opposte rispetto all'evento: il rapporto e' compilato dal manutentore che dichiara il proprio tempo di risposta, il quaderno da chi aspettava con la linea ferma. Non cambia la durata del fermo, cambia il **tempo di risposta della manutenzione** di domenica |
| **Le verifiche CCP3 del 10/05 esistono in tre versioni documentali** | `MOD-QA-07_10-05-26_L1_T2_scansione.jpg` → 8 righe orarie, **5 eseguite**, 15:00 «macchina ferma», **16:00 e 17:00 barrate e vuote**, seconda firma su una sola riga, verifica di fine turno in bianco; `checklist_metal_detector_manuale_operaio.txt` FOGLIO 8 retro → **8 righe eseguite e conformi**, comprese quelle barrate, con operatore diverso; `appunti_capoturno_quaderno_linea1_OCR.txt` pag. 44 → «saltata verifica ore 15 e 16 x fermo!!!» | **Nessuno.** ⚠️ **E' la divergenza piu' grave del lotto.** Il canone registrava la NC 1 dell'audit e il caso registro cartaceo contro datalogger sul CCP2; questa e' diversa: **due compilazioni cartacee dello stesso turno che non coincidono**, su fogli destinati alla cartella evidenze per la risposta al cliente entro 48 ore. La trascrizione si mette in dubbio da sola annotando che tre righe «sembrano scritte tutte in una volta a fine serata» |
| **TMC proposto a sei mesi contro i 45 giorni della scheda tecnica in vigore** | Scheda tecnica pag. 3 → **shelf life 45 giorni**; `test_shelf_life_accelerata_confezione_MAP_snack.csv` riga 173, nota R&D del 02/07 → «proposta: **TMC 6 mesi** a T ambiente, da confermare con 90 gg reali» | **Vale la scheda tecnica.** Non e' una contraddizione fra documenti: e' una **proposta contro una specifica in vigore**. Si registra perche' e' il tipo di divergenza su cui un sistema interrogato risponde «sei mesi» citando una fonte vera, e perche' una modifica di quella portata tocca etichetta e accordo col cliente |
| **Il riepilogo della scheda di manutenzione non quadra con le righe che riepiloga** | `scheda_manutenzione_ordinaria_forni_industrial.csv` riga 59 → «RIEPILOGO PARZIALE: interventi SCADUTI n. 7 / RIMANDATI n. 8 (agg. 09/05/26 L.T.)»; le righe del file danno **11 scaduti e 7 rimandati**, e restringendo al solo tratto che precede il riepilogo **6 e 7** | **Il file, non il riepilogo.** ⚠️ E' un'incoerenza **intra-file**, quindi va scritta come nota che la dichiara e non come questione aperta. E' lo stesso modo di sbagliare gia' registrato sul pie' di pagina del datalogger: il totale scritto a mano che nessuno riconta |

### Due prove di solidita' del canone, dallo stesso lotto

Non sono contraddizioni: sono verifiche che il canone regge, e vale la pena registrarle.

- **La regola di composizione del codice di lotto** dichiarata dal manuale HACCP e' confermata
  in modo indipendente dalla `Scheda_tecnica_prodotto_AF-SN-0450_rev4.pdf`, pag. 3, che scrive
  «formato L26<giorno giuliano>-<linea>-<turno>».
- **La prevalenza del datalogger sul registro cartaceo** ha ora una base metrologica scritta:
  la `scheda_manutenzione_ordinaria_forni_industrial.csv`, righe 20-21, attesta che le sonde
  del PT-104 e la sonda a cuore erano in taratura valida al 10/05, con la seconda esplicitamente
  legata al modulo `MOD-QA-12`.


## Aggiunte del 19/08/2026 — contraddizioni emerse in Sessione 4, lotto 1B (freddo ed energia)

Registrate applicando la procedura di **categoria B** di `metodo_03_canonizzazione.md` §9.5:
divergenze reali del corpus, non elencate nei gruppi precedenti, trovate dal revisore
indipendente sui quattro grezzi del lotto 1B — log allarmi della cella surgelati, contratto
di manutenzione frigo (bozza non firmata), contatori di reparto e fattura dell'energia.
**I grezzi non sono stati toccati.** Ciascuna ha gia' la sua nota nel vault.

⚠️ **Tre di queste righe hanno la stessa forma, ed e' una forma nuova per questo canone:
un'AZIONE CORRETTIVA registrata che il dato disponibile non conferma.** Non sono divergenze
fra due misure: sono divergenze fra cio' che un registro dichiara di aver fatto e cio' che una
registrazione automatica mostra. Vale la pena isolarle come famiglia, perche' e' il tipo di
divergenza che un sistema interrogato non trova mai citando una fonte sola.

| Cosa diverge | Dove | Valore da preferire |
|---|---|---|
| **La non conformita' del 10/04 attribuisce al tunnel sbrinamenti che il log registra sulla cella** | `non_conformita_interne_registro_2026.csv` riga `NC-2026-067` del 10/04/2026 → «TS-01 allarme sbrinamento ricorrente, 3 eventi in settimana, capacita ridotta», gravita' alta, causa «obsolescenza impianto», costo stimato 2.600 EUR; `log_allarmi_cella_frigo_surgelati_aprile.log` → per il tunnel **nessun evento**, solo 429 letture e un riavvio, mentre i 192 sbrinamenti del mese sono tutti della cella `CF-02` e proprio in quei giorni raddoppiano | **Nessuno.** O il log non copre gli eventi del tunnel, pur registrandone le temperature ogni cinque minuti, o la non conformita' e' intestata all'impianto sbagliato. ⚠️ Se fosse il secondo caso, causa e azione — «manutenzione tampone, pianificazione installazione nuovo tunnel» — sono state decise sul pezzo sbagliato, e il pezzo giusto e' quello che a maggio consuma il 49,7 % in piu' |
| **L'azione correttiva di gennaio sposta gli sbrinamenti in fascia notturna; ad aprile sono sulle ventiquattro ore** | `non_conformita_interne_registro_2026.csv` riga `NC-2026-017` del 30/01/2026, gravita' alta, **CHIUSA** il 03/02 → causa «sbrinamento evaporatore programmato in orario di carico», azione «spostato ciclo sbrinamento su fascia notturna»; il log di aprile → sbrinamenti alle 04, 10, 16 e 22 fino all'11/04, poi otto al giorno, poi dodici | **Nessuno.** Il log non copre febbraio e marzo, quindi non si sa se l'azione sia stata applicata e disfatta o mai applicata. ⚠️ Tocca l'**efficacia di un'azione correttiva chiusa**, che e' cio' che BRCGS e IFS chiedono di verificare: chiusa in quattro giorni, su una non conformita' di gravita' alta |
| **L'azione correttiva del 30/05 «riduce» a cinque minuti un allarme che il 15/04 era gia' a cinque** | `non_conformita_interne_registro_2026.csv` riga `NC-2026-114` del 30/05/2026 → «riparazione fermo porta, allarme porta aperta ridotto a 5 min»; log del 15/04 → `ALARM DOOR_TIMEOUT LIM=00:05:00` | **Nessuno.** O l'azione descrive come nuovo un parametro esistente — e allora non cambia niente — o la soglia era stata allargata e riportata indietro senza che nessun documento lo registri, mentre la stessa centralina registra per iscritto gli altri cambi di parametro |
| **Due incrementi diversi per lo stesso mese, dentro la stessa fattura** | `bolletta_VenetaEnergia_maggio2026.pdf` pag. 4, riepilogo per la contabilita' → «ctr budget energia mag: +9,4% su apr»; pag. 2, grafico dei dodici mesi → `apr26 169.302` e `mag26 178.480`, cioe' **+5,4 %** | **Nessuno, e il perimetro non e' dichiarato.** Il +9,4 % potrebbe essere in euro anziche' in kWh — il contratto e' indicizzato al PUN — ma la fattura non lo dice e le fatture di aprile non sono in archivio. E' il numero che va al direttore di stabilimento |
| **Il terzo quasi-omografo Peruffo** | **Attilio Peruffo**, legale rappresentante di Frigotecnica Berica S.r.l. (`contratto_manutenzione_impianto_frigo_TS01.docx`), accanto alla coppia gia' registrata **Peruffo Maria Grazia** (visura) / **Peruzzi Maurizio** (bilancio) | **Sono tre persone diverse.** Non e' una divergenza fra valori: e' una trappola di entity resolution che il corpus contiene ora in tre esemplari. Registrato in `alias_entita.md` classe B |
| **Chi ha sbrinato la cella il 24/04: l'officina interna o un tecnico esterno** | `scheda_manutenzione_ordinaria_forni_industrial.csv` riga 103 → sbrinamento programmato mensile di `CF-02` eseguito il `24/04/26` da «interno (Bissoli)», stato `OK`; `log_allarmi_cella_frigo_surgelati_aprile.log` → lo stesso giorno uno sbrinamento **manuale** comandato in sessione di assistenza da un operatore **esterno** (`OP=EXT`, `ID=FRIGOTEC-11`) | **Nessuno.** O sono due attivita' diverse nella stessa giornata — il ciclo programmato e uno straordinario — o i due documenti attribuiscono lo stesso intervento a due esecutori diversi. Nessuna delle due fonti lo dichiara, e il rapporto di lavoro di quella giornata non e' in archivio |
| **Due date per la stessa procura, nello stesso rigo** | `contratto_manutenzione_impianto_frigo_TS01.docx`, intestazione delle parti → «giusta procura del **15/09/2024 03/11/2025**», due date affiancate senza congiunzione | **Nessuno.** E' un'incoerenza **intra-file**, prodotta dalle «revisioni NON accettate» che il documento dichiara in testa: stesso meccanismo dei due canoni dell'art. 9.1. Per il precedente del 18/08 si scrive come nota che la dichiara, non come questione aperta. Riguarda il potere di firma del direttore di stabilimento |

### Una correzione ai numeri di questo canone, non alle sue conclusioni — 19/08/2026

⚠️ **La sezione «Un caso che sembra un errore e non lo e': i consumi energetici» dichiara tre
numeri che non reggono al riconteggio**, e il divieto 36 di `metodo_03` vale esplicitamente anche
per i numeri scritti nei documenti di metodo. Il canone si accresce e non si riscrive: la sezione
del 15/08 resta dov'e', e questa riga dice cosa e' cambiato.

| Grandezza | Nel canone | Ricontata sul grezzo, due volte in modo indipendente |
|---|---|---|
| righe in cui la somma delle fasce non fa il totale | 59 | **68** su 186 |
| righe in cui il costo non e' totale x tariffa | 137 | **174** su 186 |
| righe entro 1,5 kWh dal consumo reale | «165 su 165» | **186 su 186** |

**La conclusione qualitativa del canone resta intatta e confermata:** non sono errori di
calcolo, sono arrotondamenti all'intero con il costo calcolato sul consumo reale. Cambia solo
il conteggio. **Come nasce il numero vecchio:** le righe con data nel formato `gg/mm/aa` sono
esattamente **165**, e le altre **21** sono in `aaaa-mm-gg` — l'analisi che ha prodotto «165 su
165» leggeva un solo formato dei due che convivono in quella colonna.

⚠️ Nella stessa famiglia, una precisazione alla riga «Integrita' del log cella» del secondo
gruppo: dopo il riavvio del 21/04 e' la centralina del **tunnel** a ripartire con `RTC=NOSYNC`,
mentre quella della **cella** riparta con `RTC=SYNC`. La conclusione — il log non e'
utilizzabile come evidenza in audit — regge sugli altri due difetti (la durata gia' presente nel
record di apertura e il file troncato), ma l'orologio non sincronizzato **non toglie data agli
allarmi di temperatura della cella**.
## Aggiunte del 19/08/2026 — contraddizioni emerse in Sessione 4, lotto 1C (metrologia e gas tecnici)

Registrate applicando la procedura di **categoria B** di `metodo_03_canonizzazione.md` §9.5:
divergenze reali del corpus, non elencate nei gruppi precedenti, trovate sui due grezzi del
lotto 1C — l'elenco delle attrezzature con lo stato di taratura e la bolla di ingresso dei gas
alimentari. **I grezzi non sono stati toccati.** Ciascuna ha gia' la sua nota nel vault.

⚠️ **La famiglia nuova di questo lotto ha un nome: DUE REGISTRI PARALLELI DELLA STESSA
GRANDEZZA, nessuno dei due dichiarato prevalente.** Non e' la stessa cosa delle divergenze fra
due misure ne' delle azioni correttive non confermate dal dato (famiglia del lotto 1B): qui due
sistemi di registrazione **censiscono gli stessi oggetti** — gli strumenti che misurano i punti
critici — e non concordano su date, periodicita' ed esecutore. Riguarda cio' che un auditor
verifica per primo quando vuole sapere se una registrazione vale.

| Cosa diverge | Dove | Valore da preferire |
|---|---|---|
| **Metrologia del `PT-104`: due censimenti, due periodicita', due esecutori** | `scheda_manutenzione_ordinaria_forni_industrial.csv` righe 20-21 → «Sonde TT_01/TT_02/TT_03» tarate ogni **6 mesi** il `09/02/26` e «Sonda a cuore T_CUORE» ogni **3 mesi** il `2026-03-16`, esecutore **Analytica Veneta (F0090)**, note «rif. CCP2» e «rif. CCP2 - MOD-QA-12»; `elenco_attrezzature_taratura_strumenti_2026.csv` righe 17-20 → i **quattro canali** `DL-001`…`DL-004` del datalogger (canale 1 «cuore prodotto», canali 2 e 3 «camera»), tarati **28/11/2025** con scadenza a **12 mesi**, esecutore **CalService Italia LAT 087**, incertezza ±0,15 °C | **Nessuno.** ⚠️ Tocca la **base metrologica dell'arbitrato datalogger contro registro cartaceo**, che il canone dava per acquisita con la sola scheda di manutenzione (add. 18/08, «due prove di solidita'»). La prova regge — al 10/05 entrambi i registri danno tarature in corso di validita' — ma **i due documenti non descrivono la stessa cosa**, e nessuna fonte dichiara se le voci del piano e le matricole dell'elenco siano lo stesso strumento |
| **Convalida dell'`MD-3200`: annuale o semestrale** | Piano di manutenzione riga 34 → «Convalida annuale Loma + certificato», `06-feb-26` → `06/02/27`, 850,00 €, `OdL-26-0090`; elenco attrezzature riga 39 → `04/03/2026` → `04/09/2026`, «verifica funzionale + certificazione tasselli», certificato `LM-26-1174` | **Nessuno.** Cambia il mese dell'intervento e la durata della copertura: dodici mesi contro sei |
| **`MD-1800`: SCADUTO in un registro, Conforme nell'altro** | Piano di manutenzione riga 37 → convalida `03-apr-25` → `03/04/26`, stato **`SCADUTO`**, «sollecitato da QA (Marchetti) 2 volte», nessun ordine di lavoro; elenco attrezzature riga 43 → `19/02/2026` → `19/08/2026`, esito **`Conforme`**, stato `IN USO`, certificato `LM-26-0983` | **Nessuno, ed e' la piu' grave del lotto.** Non sono due date diverse per lo stesso intervento: sono **due stati opposti dello stesso punto critico di controllo**, uno dei quali dice che la copertura manca da oltre un anno ed e' stata sollecitata senza esito |
| **Il kit dei tasselli del CCP3 passa da tre sigle a quattro** | `checklist_metal_detector_manuale_operaio.txt` → kit **`TL-114`**; piano di manutenzione riga 35 → **`TST-CERT-KIT`**; elenco attrezzature righe 40-42 → **tre matricole** `TT-001`/`TT-002`/`TT-003` con tre certificati `LM-26-1174-A/B/C`, piu' `TT-005` di scorta; `inventario_magazzino_scadenze_FEFO_maggio.csv` riga 104 → **`KIT-MD-05`**, 3 kit a giacenza | **Nessuno.** Quattro sistemi di codifica per la stessa funzione, e i conteggi non aiutano: il magazzino ha 3 kit, l'elenco tre matricole in linea piu' una di scorta, le altre due fonti parlano di un kit al singolare |
| **Posizione dell'`MD-3200` in linea** | `Scheda_tecnica_prodotto_AF-SN-0450_rev4.pdf` pag. 2 §5 → **fra il raffreddamento in spirale e il confezionamento**; elenco attrezzature riga 39, colonna `Ubicazione` → **«Linea 1 - post confezionamento»** | **Nessuno.** Cambia l'oggetto del controllo: dopo il confezionamento ricadrebbe nel campo del metal detector anche cio' che entra **durante** il confezionamento — che e' esattamente il caso del frammento di maggio |
| **La taratura attestata all'autorita' sanitaria non e' nel registro degli strumenti** | `Verbale_ispezione_ATS_09_06_2026.pdf` pag. 3 §1.6 → «termoregistratore CF-02: funzionante, ultima verifica taratura **12/02/2026**»; elenco attrezzature → sulla `CF-02` nessuno dei tre strumenti porta quella data (`TI-002` 09/01/2026, `DL-006` 14/01/2026, `TR-010` 11/11/2025) | **Nessuno.** ⚠️ **Specie nuova:** uno dei due termini e' un'**attestazione resa all'autorita' sanitaria** e verbalizzata in triplice copia, l'altro e' il registro interno che dovrebbe sostenerla |
| **La ritaratura del flussimetro azoto del 04/05 non compare nel registro degli strumenti** | `non_conformita_interne_registro_2026.csv` riga `NC-2026-082` del 04/05/2026 → causa «deriva flussimetro azoto», azione «ritaratura, annotazione su registro macchina», **CHIUSA** lo stesso giorno; elenco attrezzature riga 93 → `CV-003` «Dosatore azoto PKM-450 - flussimetro», ultima taratura **16/12/2025** | **Nessuno.** E' la famiglia gia' isolata in 1B — **un'azione correttiva registrata che il dato disponibile non conferma** — applicata questa volta a uno strumento: se la ritaratura c'e' stata, il registro metrologico non la riporta |
| **Tre codici e due numeri di bolla per la stessa consegna di azoto** | `bolla_ingresso_azoto_alimentare_Nordgas_OCR.txt` → lotto bulk `LOT-N-260502` su DDT `26/04512`; `tracciabilita_lotti_massbalance_L26130.xlsx` foglio «A monte» riga 14 → lotto `NG-26-0506` su DDT `BN-4471`; `inventario_magazzino_scadenze_FEFO_maggio.csv` riga 80 → `NG26-0644` | **Nessuno.** Il gas e' un additivo alimentare a contatto col prodotto: con tre codici scollegati la rintracciabilita' della partita passa per la data, non per il lotto |
| **Quantita' e livello del serbatoio di azoto del 06/05** | Bolla → `2.350` m³ gas equivalenti pari a `2.940` kg, livello da `22 %` a **`87 %`** a fine scarico; inventario riga 80 → **2.310** m³ e nota di riga «bolla Nordgas 06/05 - **livello 68%**» | **Nessuno.** Sulle quantita' lo scarto e' di 40 m³ e puo' essere consumo, dato che l'inventario e' dichiarato al 31/05; sul livello l'inventario **attribuisce alla bolla un valore che la bolla non contiene** |

### Due riconciliazioni, non due divergenze — 19/08/2026

Come per la coppia registrata il 18/08, vale la pena scriverle: sono casi in cui l'archivio,
letto per intero, **toglie** una contraddizione apparente invece di aggiungerne una.

- **L'azoto arriva per due strade, e questo concilia bolla e quaderno.** Il quaderno del
  capoturno del 6/5 annota «bomb0la n0rdgas cambiata alle 16», mentre la bolla dello stesso
  giorno consegna azoto **sfuso** in serbatoio e bombole di sola CO2. L'inventario riga 101
  registra **18 bombole di azoto «scorta rampa»** con nota «rampa emergenza PKM-450»: le
  bombole esistono in giacenza e non devono essere arrivate quel giorno per poter essere
  cambiate quel giorno. ⚠️ Che *quella* bombola venisse dalla rampa resta una lettura, non un
  fatto dichiarato da una fonte.
- **La non conformita' `NC-2026-084` coincide punto per punto col suo documento di origine.**
  La bolla annota «(v. n0stra NC interna O84)» e il registro delle non conformita' porta la
  `NC-2026-084` del 06/05/2026 con stessa data, stesso fornitore (`F0061`), stesso motivo
  (certificato in copia sbiadita), stessa azione (originale richiesto via PEC, ricevuto
  08/05), stesso responsabile e chiusura al 08/05. **E' il primo caso del corpus in cui una
  riga del registro NC trova il proprio documento e i due non divergono.**

### Un'assenza verificata, dal lotto 1C

- Il **certificato di analisi `CA-26/0912` del 05/05/2026**, richiamato dalla bolla come
  allegato e dichiarato consegnato «in copia cartacea», **non e' in archivio**: la ricerca su
  tutti i 160 file del manifest v1.1 con l'estrattore congelato non ne trova traccia. Le
  analisi dei due gas alimentari esistono quindi **solo come trascrizione dentro la bolla**,
  e il laboratorio che le firma e' **interno al fornitore**.
