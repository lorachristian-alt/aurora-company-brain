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
- **testo BARRATO nei documenti** *(riga aggiunta il 23/08/2026, al gate del lotto 3B — T157)*: passaggi cancellati con la barratura, che nel testo estratto sono **indistinguibili da quelli vigenti**.

### Il barrato — accrescimento del 23/08/2026, gate del lotto 3B (T157)

⚠️ **Chi legge questo canone deve aspettarsi il barrato, perché è un tratto del corpus e non
un incidente di qualche file.** La riga entra qui perché lo strumento che lo vede esiste da
`E48` — l'**estrazione di cantiere**, che lo restituisce marcato `[BARRATO: …]` — mentre
l'**estrattore di misura non lo vede e resta identico**: chi confronta il prima e il dopo di una
misura sta leggendo un archivio in cui il barrato è testo normale.

**Il conto, misurato sul corpus il 23/08/2026 con `estrazione_cantiere.testo_cantiere` (E49: il
numero è contato sulla fonte, non riportato):**

| | |
|---|---|
| grezzi che portano almeno un passaggio barrato | **11** |
| passaggi barrati in tutto | **40** |
| di quegli 11, già canonizzati | **6** |
| formati | `.docx` per dieci, `.pptx` per uno |

⚠️ **Il numero corregge il «tre» del prompt di questo gate**, che era composto a mano: è la
stessa specie che questo gate sta legiferando — un conteggio del coordinatore invece di una
lettura dalla fonte (§4.47).

**Perché il barrato cambia il senso di un documento, e non lo sfuma:**

- **la politica per la qualità 2026** elenca nove impegni, e il nono — «perseguire la crescita
  del fatturato quale obiettivo primario dell'organizzazione» — è **barrato**. Nel testo
  estratto è indistinguibile dagli altri otto: chi legge il grezzo conta nove impegni dove
  l'azienda ne ha lasciati otto, e il nono è **una proposta ritirata**;
- **`PRO-QA-08`** porta **tre** barrati sostanziali — l'applicazione ai reclami dei fornitori, la
  comunicazione al titolare per le classi 1 e 2, il laboratorio interno;
- **la lettera di risposta a Tosano** ne porta **nove**, il numero più alto del corpus, e la sua
  natura di **bozza** è proprio ciò che il barrato racconta.

**La regola che ne discende, e che vale per ogni nota:** un riscontro che vive **solo** in testo
barrato **non sostiene un'affermazione al presente** — è contenuto **revocato**, e la nota che
lo usa lo dichiara. Un fatto letto dalla struttura del file porta `verifica: strutturale`.


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


## Aggiunte del 19/08/2026 — divergenze emerse nel lotto R1 (riconciliazione verticale)

⚠️ **Queste tre non vengono da grezzi nuovi: vengono dall'aver messo le note già scritte
davanti al documento che le prescrive.** È il primo gruppo del canone che nasce da una
riconciliazione **verticale** invece che orizzontale, e le prime due riguardano il **manuale
HACCP**, cioè il documento prescrittivo di vertice dell'archivio.

| Divergenza | Le versioni | Chi vince |
|---|---|---|
| **Il manuale HACCP dichiara rimosso il carrello ricambi, e tre documenti successivi lo smentiscono** | `manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt` §9.1 nota (5), nella revisione **08/04/2026**: «il carrello ricambi di linea **è stato rimosso**; ogni intervento in produzione richiede il modulo MOD-PR-04 con conta attrezzi in ingresso e in uscita» · `non_conformita_interne_registro_2026.csv` `NC-2026-029`, azione «rimozione carrello da area produttiva, armadio chiuso in officina», **chiusa il 02/04/2026** · `report_fermo_macchina_confezionatrice_MAP.txt` del **10/05**: guarnizione «presa dal carrello ricambi **che tengo a bordo linea 1**» · `non_conformita_interne_registro_2026.csv` `NC-2026-089` del 10/05, causa radice «**carrello ricambi ancora in area produttiva nonostante chiusura NC audit**» · `Verbale_ispezione_ATS_09_06_2026.pdf`, **diffida** sul carrello a bordo della confezionatrice | **Nessuno.** ⚠️ **Specie nuova, e la più grave del gruppo**: è la famiglia isolata in 1B — *un'azione correttiva registrata che il dato disponibile non conferma* — applicata al **manuale di autocontrollo**. La revisione in vigore incorpora come fatto compiuto una rimozione che un mese dopo l'azienda stessa registra come non avvenuta, e il manuale è il documento che si esibisce all'ente di certificazione e all'autorità |
| **La validazione del CCP2 potrebbe essere scaduta, e il manuale lo chiede a sé stesso** | `manuale_HACCP_...` §11.3: «CCP2 mediante studio di penetrazione termica su prodotto farcito peggiore caso, rapporto Studio Alimentaria **SA-VAL-21/09 del 2021**, rivalidazione prevista 2024 - **NOTA: rivalidazione eseguita? vedi verbale team 03/2024**» · §8.1 riga CCP2, voce Verifica: «challenge test/validazione trattamento **ogni 3 anni** o a modifica di prodotto/processo» | **Nessuno.** Al 10/05/2026 la validazione del punto critico che ha deviato ha **cinque anni**, e il documento che la prescrive **non sa dire se sia stata rifatta**: la nota interrogativa è rimasta dentro la revisione 5 dell'08/04/2026. Il `verbale team 03/2024` che dovrebbe scioglierla **non è in archivio** — assenza verificata sui 160 file del manifest v1.1. È un'incoerenza **intra-file** su un documento prescrittivo, stessa specie del piè di pagina del datalogger, ma su una premessa di validità del CCP2 |
| **L'attività dell'acqua di AF-SN-0450: il manuale dà due matrici, e questo cambia l'arbitrato del 18/08** | `manuale_HACCP_...` §5.1, Famiglia A: «**aw 0,30-0,40 (prodotto); farcitura in massa aw 0,90-0,94**, pH 5,4-5,9» · `Scheda_tecnica_prodotto_AF-SN-0450_rev4.pdf` → aw **0,93** · `Rapporto_di_Prova_AnalyticaVeneta_2026_04187.pdf` → aw **0,936** · `test_shelf_life_accelerata_confezione_MAP_snack.csv` → aw **0,31** | ⚠️ **Nessuno, e la riga del 18/08 va letta con questa accanto.** L'arbitrato del lotto 1A concludeva «la scheda tecnica, confermata dal laboratorio accreditato; l'anomalia sta nel file delle prove di shelf life». Il manuale mostra che **i due valori misurano matrici diverse**: 0,31 è compatibile con l'aw *del prodotto* (0,30-0,40), 0,93 con quella *della farcitura in massa* (0,90-0,94). Ne segue che il file delle prove **non è più l'anomalo**, e che nasce una divergenza nuova: **manuale contro scheda tecnica sull'aw del prodotto**, 0,30-0,40 contro 0,93. ⚠️ La riga del 18/08 **resta dov'è**: il canone si accresce, e questa dice che cosa è cambiato |

### Perché questo gruppo vale più di quanto sembri

Le prime due divergenze si trovano **solo** leggendo il manuale HACCP **come documento a sé**,
invece che come fonte da citare per un limite. La terza si trova solo mettendo il manuale
accanto a una divergenza che il canone aveva già arbitrato. ⚠️ **Nessuna delle tre sarebbe
emersa dalla riconciliazione orizzontale**, che confronta i documenti che registrano: il
manuale non registra niente, prescrive — e per due volte su tre **prescrive male, o dichiara
compiuto ciò che non lo è**.

## Aggiunte del 19/08/2026 — divergenze emerse nel lotto 2A (il lavaggio CIP)

Il lotto porta dentro il vault il log del CIP di maggio **e le due fonti che lo prescrivono**:
`IO-05` e la scheda di sicurezza del detergente acido. Le due righe che questo canone già
teneva sul CIP — l'esito dei lavaggi e la portata — sono state riscontrate riga per riga e
**restano valide**. Quelle qui sotto sono divergenze **nuove**, e hanno una caratteristica
comune che le distingue da tutte le altre registrate finora.

⚠️ **Non sono registri che si contraddicono: sono DUE DOCUMENTI PRESCRITTIVI IN VIGORE che
non concordano fra loro.** Fino a qui il canone raccoglieva divergenze fra documenti che
*registrano* — due letture dello stesso DDT, due conteggi dello stesso turno — o al più fra
un registro e la fonte che lo governa (T64). Qui la contraddizione è **fra due prescrizioni**,
e nessuna delle due è il registro dell'altra: chi lavora ha davanti due istruzioni valide che
gli dicono cose diverse.

| Divergenza | Le versioni | Chi vince |
|---|---|---|
| **Quale sia il detergente acido del CIP** | `IO-05_istruzione_operativa_lavaggio_CIP.docx` §3, §5 e §12: **`CHEMIFOOD AN-15`, «Acido nitrico 15%»**, dosato all'1,0-1,5 % · `scheda_sicurezza_detergente_acido_lavaggio_CIP.txt` §1.1 e §3.2: **`ACIDFOOD CIP 25`, cod. `CF-AC-025`**, acido nitrico **20-25 %** più acido fosforico 5-1O %. Stesso fornitore, Chemifood Italia; **nessuna delle due sigle compare nell'altro documento** | **Nessuno.** ⚠️ **Pesa oltre sé stessa**: se sono due prodotti diversi, l'archivio **non contiene la scheda di sicurezza del prodotto realmente in uso**, e ogni confronto fra le due fonti — concentrazioni, temperature, DPI — perde il presupposto. Se sono lo stesso prodotto, l'istruzione ne dichiara una concentrazione di principio attivo che la scheda smentisce |
| **Con quali DPI si maneggia l'acido** | `IO-05` §2: guanti in **neoprene**, e — dopo la cancellazione della FFP2 da parte dell'RSPP — **semimaschera con filtro `B-P2`**; grembiule antiacido · scheda di sicurezza §8.2: guanti in **gomma butilica o fluoroelastomero** `EN 374` **classe 6**, **facciale con filtro tipo `E`**, tuta antiacido **tipo 3** `EN l4605` | **Nessuno.** Entrambi i documenti sono in vigore e ciascuno è autorevole nel proprio dominio: l'istruzione è **verificata dall'RSPP**, la scheda è del **fabbricante della sostanza**. Nessuno dei due cita l'altro sui dispositivi. ⚠️ La cancellazione della FFP2 prova che in Aurora la protezione respiratoria **è stata riesaminata almeno una volta**; se quel riesame abbia tenuto conto della scheda, che chiede il tipo `E`, nessun documento lo dice |
| **Ogni quanto si verifica il lavaocchi di sala CIP** | Scheda di sicurezza §8.2: **verifica settimanale** di docce di emergenza e lavaocchi · `IO-05` §3, annotazione attribuita a `Dal Maso I.` e incorporata nella revisione in vigore: «lavaocchi controllato da me **ogni primo lunedì del mese**» | **Nessuno.** ⚠️ **Specie propria**: non è una regola contro una regola, è **una regola contro una dichiarazione di prassi**. L'annotazione non contesta la frequenza del fabbricante — **non la nomina** — e un documento verificato dall'RSPP incorpora così, senza segnalarla, una cadenza quattro volte più lunga di quella richiesta |
| **La sequenza delle fasi eseguita non è quella che il programma dichiarato prevede** | `IO-05` §6: al programma `P2` competono le fasi **1-2-3-4-5**, e la sanificazione è la **fase 6**, che appartiene a `P4` e `P5` ed è elencata **in coda** · `log_lavaggio_CIP_linea1_maggio.log`: tutti e 30 i cicli dichiarano `PRG=IO-05_P2_LINEA1`, il `P1` non compare mai, e i 28 cicli completi eseguono **sei** fasi con `SANIF_PAA` **fra il lavaggio acido e il risciacquo finale** | **`IO-05`**, e il log resta com'è — ⚠️ **riaperto e confermato il 21/08/2026: v. B3 in fondo a questo file.** Il tracciato risulta più severo **di entrambi** i prescrittivi, non solo di `IO-05`. Lo scarto è **doppio**: nella composizione — una fase in più di quelle che il `P2` prevede — e nell'**ordine**, perché la sanificazione cade prima del risciacquo finale invece che dopo. ⚠️ Il tracciato risulta così **più severo** del nome che porta, non meno: è un'etichetta che non corrisponde al contenuto, sull'unico campo che direbbe quale programma doveva girare quella notte |
| **Il prolungamento automatico che l'istruzione descrive non ha riscontro** | `IO-05` §7 punto 2: «se non arriva a 75 °C **il pannello allunga il tempo da solo**, NON forzare l'avanzamento» · il log: la fase alcalina dura `1200 s` **in tutti e 28 i cicli**, comprese le notti in cui 57 letture su 116 stanno sotto i 75 °C | **Nessuno, e non si sceglie.** È la famiglia isolata nel lotto 1B — *un'azione correttiva o automatismo dichiarato che il dato non conferma* — applicata a un **automatismo di impianto**. Se il pannello non lo esegua, o lo esegua senza registrarlo, il tracciato non lo dice: nessun campo distingue una durata impostata da una prolungata |
| **Il pannello non misura la grandezza che l'istruzione chiede di registrare** | `IO-05` §7 punto 1: si registra la «**concentrazione** soda letta dalla sonda di conducibilità (deve stare tra 1,5 e 2,0 **%**)» · il log: le unità di misura presenti sono `mS/cm`, `C`, `m3/h` e `%` **del livello tanica** — **mai una concentrazione di prodotto** · `non_conformita_interne_registro_2026.csv` `NC-2026-113` del 29/05, IN CORSO: «fase sanificazione PAA registrata **senza concentrazione misurata**», causa «kit titolazione esaurito» | **Nessuno: è una lacuna di misura, non una divergenza di valori.** La concentrazione si determina **a mano, per titolazione**, e il pannello dà una conducibilità: sono due grandezze diverse, legate da una curva che nessun documento dell'archivio riporta. La NC del 29/05 è la prova che la misura manuale esiste, e che quando il kit finisce la registrazione resta vuota |

### Una riga che il canone aveva già, e che questo lotto rende verificabile solo a metà

⚠️ La riga «**Esito dei lavaggi CIP**» di questo canone dichiara **18 cicli su 28** chiusi
`PASS` con risciacquo finale sopra il limite, e fissa quel limite a **536 µS/cm**. Il
conteggio è stato riprodotto ed è esatto — 18 su 28 con l'ultima lettura del risciacquo
finale sopra 0,536 mS/cm.

⚠️ **Ma quel limite non è ricavabile dai tre grezzi del lotto.** `IO-05` prescrive uno
**scarto** — «≤ 50 µS/cm **sopra il valore dell'acqua di rete**» — e il log non registra mai
l'acqua di rete. I 536 presuppongono di conoscerla; il termine di paragone sta in un grezzo
che appartiene al **lotto 2B** e che quindi **non si cita e non si usa** (divieto 9-bis).

Perciò la nota del vault dichiara il criterio **non verificabile sulle proprie fonti** e si
ferma lì, e la riga **T72** della tabella di tracciamento porta l'obbligo esplicito per il
lotto 2B: quando quel dato entra, il criterio va applicato ai 28 cicli e questa riga del
canone acquista la sua gamba numerica dentro il vault. ⚠️ **È la prima volta che il canone
conosce un numero che i grezzi già canonizzati non permettono di scrivere**, e la distanza
fra i due si chiude con una riga di tracciamento, non con una deroga.

---

## Divergenze nuove — revisione del lotto 2B, 21/08/2026

> **Come è nata questa sezione** · Revisione indipendente del lotto 2B (autocontrollo
> analitico: tamponi di superficie, acqua potabile, acque reflue), passo 3 di `metodo_03`
> §9.5, eseguita da un revisore a contesto pulito con questo canone alla mano.
> ⚠️ **Tutte e cinque nascono dai grezzi**, e ognuna porta il documento e la riga in cui si
> legge: nessuna è stata dedotta da questo canone. Il canone si accresce, non si riscrive.

### B1 · Un auditor CSQA in stabilimento sette giorni prima delle date certificate

`registro_tamponi_superfici_listeria_salmonella.csv`, rapporto `AV-26/0158`, `Data_prelievo`
**`2026-02-10`**, riga «uscita PT-104 / Listeria monocytogenes», colonna `Note`: «**prelievo in
presenza auditor CSQA prova a campione**».

`Rilievo_Audit_BRC_IFS_CSQA_febbraio2026.txt`, intestazione: «Date audit / Audit dates:
**17/02/2026 - 18/02/2026**».

⚠️ **Nessuno dei due documenti prevale e l'archivio non scioglie.** O c'è stata una presenza
CSQA una settimana prima delle date certificate — che nessun documento registra — o la
campagna di febbraio è datata male, **ed è l'unica del file in grafia `aaaa-mm-gg`**, o
l'annotazione è stata scritta a posteriori sulla riga sbagliata.

### B2 · Un tampone di superficie fuori limite che `MOD-QA-19` non contiene

`non_conformita_interne_registro_2026.csv`, riga `NC-2026-005`, data **`2026-01-13`**:
«Tampone superficie **impastatrice IMP-300** oltre limite CBT, ripetuto dopo sanificazione»,
causa «sanificazione weekend incompleta», azione «rilavaggio secondo IO-05, **tampone di
verifica MOD-QA-19**».

Il registro dei tamponi ha una campagna **proprio quel giorno** (`AV-26/0142`, 13/01/26) e
**non contiene il punto `IMP-300`** — che non compare fra i 21 punti dell'anno — né alcun
tampone di verifica successivo su quel punto.

⚠️ **Pesa più della gemella del 24/02**: qui l'evento cade **nello stesso giorno di una
campagna registrata**, il che indebolisce la spiegazione «prelievo straordinario fuori piano».

### B3 · `NC-2026-034` dichiara due azioni che il registro dei tamponi non conferma

Stessa riga di B2-bis, `non_conformita_interne_registro_2026.csv`, `NC-2026-034` del
**24/02/2026**, gravità **critica**, chiusa il 28/02: azione «sanificazione straordinaria,
**ritampone a 48 h negativo**, **aumento frequenza MOD-QA-19**».

Il `MOD-QA-19` **non porta nessun prelievo il 26/02** — le sole date di febbraio sono 10/02 e
14/02 — e **non mostra alcun infittimento** né a marzo né ad aprile: la campagna di marzo è di
dimensione ordinaria, e l'unico passaggio a frequenza quindicinale che il registro documenta è
di **maggio**, motivato dal registro stesso con la positività di **aprile**.

⚠️ **È la famiglia già isolata in 1B — un'azione correttiva registrata che il dato disponibile
non conferma — applicata al piano di monitoraggio ambientale**, su una non conformità di
gravità critica chiusa in quattro giorni.

### B4 · Tre serie di numerazione delle non conformità, con collisioni fra soggetti diversi

⚠️ **È una trappola di entity resolution: quasi-omografi che designano eventi diversi.**

| Sigla | Documento | Evento |
|---|---|---|
| `NC-26-018` | registro tamponi, 14/02 | ruote carrelli farcitura fuori limite |
| `NC-2026-018` | `MOD-QA-18` | fermo forno `FT-01`, pressostato gas in avaria |
| `NC-26-041` | registro tamponi, 13/04 | Listeria nello scarico sotto `PT-104` |
| `NC-2026-041` | `MOD-QA-18`, 05/03 | ordine straordinario Tosano, cambio formato |
| `NC-26-055` | registro tamponi, 11/05 | nastro forno `FT-01` a 52 UFC/cm² |
| `NC-2026-055` | `MOD-QA-18`, 25/03 | prototipo `AF-SN-0470` v12, sesamo in saletta pilota |
| `NC-26-056` | registro tamponi, 11/05 | ganasce `PKM-450` a 1,2×10³ |
| `NC-2026-056` | `MOD-QA-18`, 26/03 | quarta dimissione in 5 mesi su Linea 2 |
| `NC-ACQ-26-01` · `-02` | registro acqua | ghiaccio; ferro agli spogliatoi |

⚠️ **E nessuna delle non conformità dei due registri analitici compare in `MOD-QA-18`**, che è
il registro che dichiara di essere il registro delle non conformità interne (riga 1 di titolo).
La differenza fra le due grafie è di **due cifre nell'anno**, e nient'altro.

### B5 · Lavoro domenicale a marzo

`analisi_acque_reflue_autocontrollo_2026.xlsx`, foglio «Scarico finale», riga 24: la causa del
superamento del 19/03 è «trascinamento grassi da lavaggio teglie Linea 2 (**campagna domenicale
ordini Tosano**, volumi lavaggio raddoppiati)».

⚠️ Il perimetro delle domeniche lavorate che questo canone censisce **non comprende marzo**. La
nota del vault fa la cosa giusta e **si rifiuta di fondere le due campagne**, ma la riga qui
mancava.

---

## Divergenze nuove — revisione del lotto 2B-bis, 21/08/2026

> **Come è nata questa sezione** · Revisione indipendente del lotto 2B-bis (gli allergeni: la
> scheda con la matrice di cross contamination e la formazione annuale che la insegna),
> passo 3 di `metodo_03` §9.5, eseguita da un revisore a contesto pulito con questo canone
> alla mano (E45).
> ⚠️ **Tutte e otto nascono dai grezzi.** ⚠️ **Una sola non è scrivibile in nessuna nota** —
> B6 poggia su un grezzo che nessun lotto ha ancora canonizzato, e il divieto 9-bis vale anche
> quando la divergenza è vera: il canone la registra, il vault aspetta il suo lotto. **Le altre
> sette sono entrate nel vault il giorno stesso.**

### B1 · Il documento di vertice e quello che lo attua non concordano su quali proteine si cercano, né ogni quanto

`manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt` §9.2, rev. 5 dell'08/04/2026: «lavaggio
validato tra referenze incompatibili con test proteina specifica (**latte, uovo, soia**) a cura
QC (Pozzato S., **1 validazione/trimestre per linea**)».

`scheda_allergeni_matrice_cross_contamination.docx` §6.2: test rapidi su **latte, uovo,
sesamo** — **la soia non c'è**; §6.1: la validazione è «eseguita 2024, riverificata 2025, da
ripetere dopo l'installazione del tunnel `CR-SP180`», cioè **una tantum**, non trimestrale per
linea.

⚠️ **Il sesamo — l'allergene nuovo — non è nel piano di test del documento di vertice**, che
pure lo dichiara «in fase di introduzione con la referenza in sviluppo `AF-SN-0470`»; e la
scheda che dovrebbe attuarlo toglie invece la soia. Sono **due prescrittivi in vigore, uno
annesso all'altro** (All. 12), e **nessuno dei due cita l'altro sul punto**.

⚠️ **È la divergenza più pesante del gruppo, ed è anche quella che il lotto poteva cogliere da
solo**: il manuale è già nel vault e questo stesso lotto lo cita come fonte.

### B2 · La scheda allergeni prescrive di aprire una non conformità sul modulo dei reclami

Scheda §6.4: «Due non conformita' consecutive: fermo linea e **apertura NC su `MOD-QA-31`** con
riesame della procedura di lavaggio».

`MOD-QA-31` è la scheda **reclami** — `procedura_ritiro_prodotto_CRISI_GDO.txt` riga 197,
«`MOD-QA-31` Gestione reclami e segnalazioni», e il file `MOD-QA-31_reclamo_REC-2026-011.pdf`.
Le non conformità interne stanno su **`MOD-QA-18`**.

⚠️ **Lo stesso inciampo è già auto-segnalato altrove nel corpus**:
`piano_autocontrollo_acqua_potabile_analisi.csv` riga 90, «chiusura `NC-ACQ-26-01` su
`MOD-QA-31`? **no, registro NC qualità (refuso, verificare modulo giusto con Marchetti)**».

⚠️ **È la famiglia di B4 del gruppo precedente — le serie parallele di numerazione delle non
conformità — estesa dai numeri ai moduli.** Non è un refuso isolato: **in Aurora la sigla del
modulo su cui si apre una NC è instabile**, e lo è in tre documenti indipendenti.

### B3 · Come sia composto «il lavaggio completo CIP»

`IO-05_istruzione_operativa_lavaggio_CIP.docx` §5 elenca **sei voci** — prerisciacquo,
lavaggio alcalino, risciacquo intermedio, lavaggio acido, risciacquo finale, **sanificazione
«solo se richiesta dal programma»** — sotto la frase «**il ciclo completo ha 5 fasi**». ⚠️ **Il
conto torna solo se la sanificazione non è contata**, cioè se il ciclo completo è quello senza.

Scheda §5.3: il lavaggio di tipo **`L3`** — «completo CIP secondo `IO-05`» — è «soda caustica,
risciacquo, acido, risciacquo, **sanificante PAA**».

⚠️ **Gli scarti sono due e vanno in direzioni opposte.** La scheda **omette il prerisciacquo**,
che in `IO-05` è la fase 1, e **include la sanificazione**, che `IO-05` tiene condizionata.
**Non è «`IO-05` più una fase»: è `IO-05` meno la prima e più l'ultima.**

⚠️ **Questa riga è stata scritta una prima volta come indebolimento di un arbitrato del lotto
2A, e la seconda lettura l'ha corretta.** Il gruppo del lotto 2A arbitra «**`IO-05`**, e il log
resta com'è», concludendo che il tracciato è **più severo del nome che porta**; sembrava che il
PRPo1 togliesse a quella conclusione il fondamento, perché prescrive la fase che il log esegue
in più.

⚠️ **Non lo toglie, e la ragione sta nella riga che il primo passaggio non aveva letto**:
§5.3 prescrive quel sanificante **solo dentro il lavaggio `L3`, e l'`L3` solo in quattro
circostanze** — «Obbligatorio: dopo sesamo; prima del bio; dopo referenze con crema nocciola; a
fine settimana produttiva». ⚠️ **E il log non dichiara mai il tipo di lavaggio**: §5.4 lo
affida al registro del capoturno, non al pannello. **Che i 28 cicli di maggio fossero `L3` non
lo dice nessuna fonte**, e il `SANIF_PAA` compare in 28 cicli su 30 — molto più spesso delle
occasioni che l'`L3` prevede.

⚠️ **Quindi l'arbitrato del lotto 2A regge, e ne esce più preciso**: il tracciato è più severo
**di entrambi i documenti**, non solo di `IO-05`. ⚠️ **La divergenza sulla composizione resta
vera e vive per conto proprio**: riguarda che cosa sia il lavaggio completo, non che cosa
faccia il pannello di notte.

### B4 · La nota alla matrice motiva un perimetro che la tabella non elenca

Scheda §3, note alla matrice: «"**PC soia**" su **Linea 1 e Linea 2** deriva dalla lecitina di
soia presente in alcuni semilavorati e dal flusso promiscuo di linea».

Nella tabella **nessuna referenza di Linea 2 porta `PC` sulla soia**: `AF-CR-0212` e
`AF-CR-0215` hanno **`C`**, `AF-CR-0220` ha **`A`**.

⚠️ **Questa riga era stata scritta come incoerenza intra-file, e non lo è.** Lo stesso documento
dichiara che su Linea 2 girano **referenze che la tabella non contiene**: §3, «crema nocciola
usato su referenze fuori scheda (mercato Ho.Re.Ca.) lavorate su Linea 2», e §4.3, sequenza tipo
di Linea 2, voce «referenze con crema nocciola (fuori scheda)». **Il perimetro della motivazione
esiste: è fatto di referenze che la matrice, per costruzione, non elenca.**

⚠️ **Resta il fatto sull'archivio, ed è più utile di quello che avevo scritto**: la matrice
motiva una classificazione su una linea le cui referenze rilevanti **non hanno una riga**, e chi
legge la sola tabella non può ricostruire il perimetro.

### B5 · L'aula dà arachidi e solfiti come possibili; la matrice li dà assenti

`formazione_allergeni_operatori_2026.pptx`, slide 4, tabella «Dove lo trovi da noi»: «5 Arachidi
| **non presente ma ATTENZIONE ai fornitori**»; «12 Anidride solforosa e solfiti | **possibile
in alcune materie prime**».

La matrice li dà **`A`** su tutte e sette le referenze, e la legenda definisce `A` come «non in
ricetta **e non presente nel flusso della linea**, nessuna dicitura».

⚠️ **E l'elenco degli allergeni «non presenti nel sito» della scheda §3 è di sei voci** —
crostacei, pesce, sedano, senape, lupini, molluschi — **e arachidi e solfiti non ci sono**:
restano `A` senza che nessun documento li dichiari assenti dal sito.

### B6 · Il registro della formazione non conferma nessuna delle sessioni allergeni del 2026 · ⚠️ non scrivibile

`registro_presenze_corsi_HACCP_scaduti.csv`, estrazione del **18/05/2026**: le sole righe
«**Allergeni (PRPo1)**» sono **cinque**, tutte del **09/10/2025**, con scadenza **09/10/2027**
ed ente «interno (Marchetti)».

**Non c'è nessuna riga** per la sessione annuale del **19-20/03/2026**, né per la straordinaria
del **10/04/2026** che la scheda §9.2 dichiara erogata a tre nomi: **nessuno dei tre ha una riga
allergeni**.

⚠️ **E la validità registrata è biennale, mentre §9.1 prescrive il richiamo annuale.**

⚠️ **`Bissoli Mirco — Manutentore notte` non ha alcuna riga allergeni**, e ha l'HACCP base
**scaduto** dal 20/04/2026 con la nota «turno notte - organizzare recupero diurno pagato»: al
18/05 la sessione di recupero proposta per il 26/03 **non risulta fatta**. ⚠️ **Corrobora
`fatto-turno-notte-senza-formazione`, che chiude correttamente con «la risposta non è nel
materiale»** — e conferma che quella chiusura era la sola onesta.

⚠️ **Il grezzo è fuori dal perimetro di 2B-bis e non è ancora canonizzato: la divergenza sta
qui e non può entrare in nessuna nota** finché quel file non entra in un lotto (divieto 9-bis).

### B7 · L'aula dichiara registrati tamponi allergeni che `MOD-QA-19` non contiene

`formazione_allergeni_operatori_2026.pptx`, slide 8, nota del relatore: «i tamponi post-pulizia
di Sara includono anche **la ricerca allergeni (proteina del latte)** sui punti critici della
Linea 2, non solo la carica batterica».

`registro_tamponi_superfici_listeria_salmonella.csv` porta **sette parametri** — carica
batterica, *Listeria*, Enterobacteriaceae, *Salmonella*, *S. aureus*, muffe, lieviti — e
**nessuno è una proteina o un allergene**. I test proteina esistono davvero — `NC-2026-101` del 19/05 verbalizza
un «tampone proteina latte su sfogliatrice» — ma **non lasciano traccia in `MOD-QA-19`**, e la
scheda stessa li tiene su due binari distinti (§6.2 test rapidi ≠ §6.3 `MOD-QA-19`).

⚠️ **Forza media, e va detto**: la lettura innocente è che il relatore parli dei test rapidi.
Ma **chi interrogasse l'archivio su «dove sono registrati i tamponi allergeni» non troverebbe
nulla**, e questo è un fatto sull'archivio, non sul relatore.

### B8 · Un limite «non rilevato» come condizione di avvio di un prodotto che quell'allergene lo contiene

Scheda §6.2: «proteina **latte**: **prima di ogni partenza bio su Linea 2**…; limite: **non
rilevato**». Matrice, riga `AF-CR-0220`, la sfogliatina bio: **latte = `C`**, cioè
**ingrediente**.

⚠️ **Il vincolo di §4.3 sul bio è di certificazione biologica** — contaminazione da
convenzionale, vincolo ICEA — **non allergenica**: la scheda **sovrappone i due senza
distinguerli**, e ne esce un criterio di accettazione che il prodotto controllato non può
soddisfare.

### Che cosa dicono, prese insieme

⚠️ **Sei delle otto stanno fra la scheda allergeni e un documento che le sta sopra o accanto**
— il manuale HACCP, l'istruzione CIP, il registro delle NC, il registro dei tamponi, il
registro della formazione. **Una sola è intra-file** (B4), e una è di merito (B8).

⚠️ **Il PRPo1 è un documento che prescrive molto e si riconcilia poco.** È annesso al manuale
(All. 12) e non lo cita mai; nomina `IO-05` e ne cambia il contenuto; nomina `MOD-QA-31` e
intende `MOD-QA-18`; nomina `MOD-QA-19` per registrazioni che quel registro non porta. **Il
canone lo registra come tratto del documento**, non come una serie di sviste indipendenti.

---

## Divergenze nuove — revisione del lotto 3A, 22/08/2026

> **Come è nata questa sezione** · Revisione indipendente del lotto 3A (il riesame della
> direzione e il cruscotto KPI), passo 3 di `metodo_03` §9.5, eseguita da un revisore a
> contesto pulito col canone alla mano (E45).
> ⚠️ **È la sezione più ricca che il progetto abbia prodotto: quindici divergenze**, e la
> ragione è nella diagnosi del revisore — **il lotto ha letto i due grezzi come documenti,
> quasi mai uno contro l'altro e mai contro il vault che aveva intorno.**
> ⚠️ **Sette voci non sono scrivibili in nessuna nota** (divieto 9-bis) e stanno in fondo, in
> C7: poggiano sul rapporto d'audit, che nessun lotto ha ancora canonizzato.

### C1 · Il mock recall del 10/03: conforme per due fonti, non conforme per il riesame

`manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt`: «mock recall annuale (`PRO-QA-14`) con
obiettivo di ricostruzione **≥ 99% entro 4 h**».
`non_conformita_interne_registro_2026.csv`, `NC-2026-044`: le 3 h 50 sono «**entro il limite di
4 h della `PRO-QA-14`** ma vicino alla soglia», gravità **media**.
`verbale_riesame_direzione_SGQ_2026.txt` §5.3: «contro obiettivo **2 h** (**NON conforme**)».

⚠️ **Il verbale prende metà del criterio del manuale e cambia l'altra metà**: applica la soglia
del 99 % sul bilancio di massa e sostituisce il tempo. ⚠️ **E dalla non conformità discendono un
obiettivo 2026 a zero e il rinvio della decisione sul gestionale.** È la divergenza più pesante
del lotto, ed è scritta nel vault: `questione-mock-recall-due-ore-o-quattro`.

### C2 · I reclami di gennaio-febbraio 2026: cinque nel verbale, tre nel registro, e nessuno coincide

`verbale…` §4.2: «n. **5** (Ali' saldature film, consumatore numero verde, Famila etichetta bio,
piu' 2 minori)».
`cruscotto_KPI_qualita_2026.xlsx`, foglio «Reclami»: **tre** righe nel bimestre, e sono peso
sotto tolleranza *(Tosano)*, confezione non sigillata *(consumatore dal **form del sito**)*,
muffa a 5 gg dal TMC *(Alì)*.

⚠️ **Nessuna delle tre coincide con le tre descritte**: l'unico reclamo Alì è per muffa e non per
saldature, l'unico consumatore è arrivato dal form e non dal numero verde, e **«Famila» non
compare fra i reclami di nessun registro**.

### C3 · Lo stesso indicatore con due target a un ordine di grandezza di distanza

`verbale…` §10.1: «Reclami / mio pezzi · **< 0,85**». `cruscotto…` riga 6: «Reclami cliente per
milione di pz (ppm) · target **8**».

⚠️ **E il cruscotto dichiara di derivare i target da quel riesame.** ⚠️ *(Una gamba non è
scrivibile: `PRO-QA-08` porta «Obiettivo 2026: < 8,0» su un denominatore diverso — **confezioni**
invece di **pezzi** — ed è il grezzo del lotto 3D.)*

### C4 · Il cruscotto e la tabella obiettivi non si mappano

**Due target su dieci contraddicono il verbale**; **quattro obiettivi del riesame non hanno riga
nel cruscotto**, fra cui l'unico giudicato non raggiungibile; **cinque righe del cruscotto non
hanno un obiettivo nel riesame**. ⚠️ **Il documento che dovrebbe dire se gli obiettivi reggano
misura in larga parte altro.** Nel vault: `questione-cruscotto-e-obiettivi-non-si-mappano`.

### C5 · Il costo della non qualità al 28/02: 6.800 nel verbale, 2.400 nel cruscotto

`verbale…` §10.1: «**6.800** al 28/02». `cruscotto…` riga 12: gennaio 980 + febbraio 1.420 =
**2.400** *(somma)*. ⚠️ **Stesso indicatore, stessa data, 2,8 volte di scarto fra i due grezzi
dello stesso lotto.**

### C6 · Il costo gen-mag vale 24.420 in un foglio e 39.500 nell'altro, nello STESSO file

Foglio «KPI mensili», riga 12: **24.420 €** *(somma)*. Foglio «NC per causa», colonna dei costi:
**39.500 €** *(somma)*. ⚠️ **Il canone già portava i due valori senza dire che sono lo stesso
workbook.** Nel vault: `kpi-costo-non-qualita-due-totali`.

### C7 · Le deviazioni CCP: il cruscotto le colloca nel mese sbagliato

`verbale…` §5.4 e `non_conformita_interne_registro_2026.csv` datano l'unica deviazione al
**14/01/2026** (`NC-2026-006`); `cruscotto…` riga 9 dà **gennaio 0** e **febbraio 1**. ⚠️ Il
totale al 28/02 coincide, il mese no.

### C8 · L'analisi di Pareto conta 56 non conformità dove il registro ne ha 119

`cruscotto…`, «NC per causa»: 14+11+9+7+6+4+5 = **56** *(somma)*; la cella `TOTALE` è una formula
mai calcolata. `non_conformita_interne_registro_2026.csv`, stesso periodo: **119 righe**, di cui
73 chiuse. ⚠️ **56 non è né il totale né le chiuse, e il perimetro non è dichiarato.** Corollario:
«NC aperte a fine mese» dà **19** a maggio, il registro ne ha **43** non chiuse.

### C9 · La Listeria del 24/02: l'azione raddoppia la frequenza in zona 2, l'evento è in zona 3

Il verbale §6.3 e il registro delle NC collocano l'evento sulla **canalina di Linea 3**, e il
registro dei tamponi censisce quel punto in **zona 3**; l'azione verbalizzata raddoppia la
frequenza **in zona 2**. ⚠️ **Aggiunge una gamba a B3 del lotto 2B e la sposta più in alto**:
l'azione non è più solo annotata da chi compila, è **verbalizzata davanti alla direzione** — e
con il perimetro sbagliato.

### C10 · Il cruscotto dei tamponi non è ricavabile da `MOD-QA-19`

Nove punti contro ventuno; le guarnizioni della cella in **zona 2** qui e in **zona 1** nel
registro; una **«zona 4»** che il registro non ha; punti fra i più campionati assenti; e
percentuali che **nessun numero di prelievi del registro può produrre** — al massimo sette in un
mese. ⚠️ **Due registri paralleli della stessa grandezza, nessuno dichiarato prevalente**: è la
famiglia isolata nel lotto 1C. Nel vault: `questione-due-registri-dei-tamponi`.

### C11 · Le tarature in scadenza a marzo che il registro degli strumenti non ha

`verbale…` §6.1: «In scadenza marzo: **termometro campione di laboratorio** e **2 sonde
spillone**». `elenco_attrezzature_taratura_strumenti_2026.csv`: **nessun «termometro campione»**;
le due sonde spillone scadono nel **2027**; le sole scadenze di marzo 2026 sono due strumenti
**già `SCADUTO`**. ⚠️ **Un'attestazione resa alla direzione contro il registro che dovrebbe
sostenerla**, ed è la specie isolata in 1C.

### C12 · «Settimane 19-21» è una quarta versione delle domeniche della promo

`verbale…` §7.2 le colloca in «**aprile-maggio**»; `piano_produzione_settimanale_sett19_21.xlsx`
fa cominciare la settimana 19 il **04/05**. ⚠️ **Nelle settimane che il verbale nomina non cade
nessuna domenica di aprile**, e il 10/05 è già «la terza domenica consecutiva». Quarta versione
di un insieme che il canone porta già in tre.

### C13 · La clausola IFS della NC di audit

`verbale…` §3.2: «rif. BRCGS 9 cl. 2.10.2 / **IFS 2.3.9.2**». `non_conformita_interne_registro_2026.csv`,
`NC-2026-028`: «/ **IFS 5.1.2**». ⚠️ **Vince il verbale** — il rapporto d'audit scrive 2.3.9.2 —
ma la divergenza fra i due grezzi canonizzati resta, e il registro delle NC porta la clausola
sbagliata.

### C14 · La tabella delle azioni perde i co-responsabili che il corpo del verbale nomina

§5.2 «**Zanella e Faggionato** presenteranno» → `A4` solo Faggionato. §7.2 «incarica **HR e il
Responsabile Produzione**» → `A5` solo Sartori. §6.2 «mandato all'**ufficio acquisti**» → `A7`
Trentin, che il §1 colloca in Amministrazione. ⚠️ **Incoerenza intra-file, sull'unica tabella che
va in bacheca ai reparti come estratto.**

### C15 · Il consuntivo 2025 è chiuso con un evento del 2026, fuori dal periodo dichiarato

Il riesame «copre il periodo 01/01/2025 - 28/02/2026»; l'ultima riga del consuntivo 2025 —
«Mock recall entro 2 h · **v. 5.3** · NO» — rimanda a un evento del **10/03/2026**, **posteriore
di due giorni alla riunione**.

### C16 · ⚠️ NON SCRIVIBILI IN NESSUNA NOTA — `Rilievo_Audit_BRC_IFS_CSQA_febbraio2026.txt`

**Nessuna delle 322 note del vault cita questo file, e nessun lotto lo ha canonizzato.** Le sette
voci qui sotto sono vere e appartengono al canone; **il vault le aspetta** (divieto 9-bis). ⚠️ **È
la vena più ricca del perimetro di 3A, e sta dietro a un file che il progetto non ha ancora
aperto.**

1. **Il termine è il 18/03, non il 17/03**: «entro 28 gg dalla **riunione di chiusura**, ossia
   entro il **18/03/2026**». Il vault ha canonizzato il 17/03 e i «sedici giorni» fino al titolo
   di una nota; con il 18/03 sono **quindici**.
2. **«2 NC minori» è un rendiconto parziale**: il rapporto dà «0 NC maggiori, 2 NC minori **e 5
   osservazioni**», e le chiude come «NC nn. 1-7». Il verbale le osservazioni non le nomina.
3. **Due termometri dei CCP con taratura scaduta dal 30/11/2025** — matricole `TP-08` e `TP-11`,
   che **non esistono nel registro degli strumenti**, mentre il §6.1 dichiara il 92 % in validità.
4. **Il seguito del ritardo**: sollecito PEC del 20/03, nuovo termine perentorio 01/04, arrivo il
   02/04, e l'avviso che «in caso di reiterazione… comportera' la segnalazione ai fini del grading
   BRCGS (**riduzione a grade A**)». ⚠️ **Il vault sa del ritardo e non sa che il grade AA — che
   la direzione chiama «obiettivo primario» — è stato messo in guardia.**
5. **La rivalidazione del CCP2 ha una risposta**: la questione aperta dal lotto R1 chiedeva se
   fosse stata rifatta; l'ente dichiara che «non risulta ancora formalizzata» e che la validazione
   2021 «resta tecnicamente applicabile».
6. **Terza gamba sul limite di 4 h**: il test di rintracciabilità dell'audit è «2 h 50 min —
   **ESITO: CONFORME**», e il mock recall 2025 «esito conforme». Con un obiettivo di 2 h nessuno
   dei due lo sarebbe.
7. **Formazione allergeni: quattro operatori, non tre.** L'osservazione ne conta **quattro**
   assunti «tra ottobre 2025 e gennaio 2026»; `NC-2026-015` ne dichiara **tre**. ⚠️ E i quattro
   rimpiazzi sono un dato sul turnover che il §7.1 del verbale non porta.

---

## Divergenze nuove — revisione del lotto 3C, 22/08/2026

> **Come si legge questa sezione.** Otto divergenze qualificate `B` dal revisore col canone, su
> un lotto che porta il **certificato BRCGS**, il **rapporto d'audit CSQA del febbraio 2026**,
> la **conferma d'incarico del rinnovo** e la **catena di quattro mail** fra l'ente e la RSGQ.
> ⚠️ **Quattro sono entrate nel vault come note, quattro no**, e il perché è sempre lo stesso:
> il **divieto 9-bis** — una gamba sta in un lotto non ancora canonizzato, e allora la
> divergenza si registra qui e **non si scrive in nessuna nota**.

### D1 — L'inventario delle evidenze del 02/04 non torna, e la voce che manca è quella decisiva ✍️ **scritta**

**L'ente registra NOVE voci ricevute** (`Rilievo_Audit_BRC_IFS_CSQA_febbraio2026.txt` §6),
**la RSGQ ne elenca CINQUE** nel messaggio del 2 aprile, e copre **due dei sette rilievi**.
⚠️ **L'ente verbalizza di aver ricevuto la «foto rimozione carrello ricambi»; il mittente
allega la foto di un «armadio dedicato ordinato (in consegna)»** — e cinque giorni dopo l'ente
scrive che la rimozione non è dimostrata. **Le tre righe non stanno insieme in nessun ordine.**
Nota: `questione-evidenze-del-02-04-nove-o-cinque`.

### D2 — Il prossimo controllo dell'ente è di sorveglianza nel 2027 o di rinnovo nel 2026 ✍️ **scritta**

Due cluster coerenti al loro interno e incompatibili fra loro, **a quattro giorni di
distanza**: il rapporto §6 e il certificato dicono **audit di sorveglianza 02/2027** e riaudit
**06/02-06/03/2027**; la conferma d'incarico e la mail del 7 aprile dicono **audit di rinnovo
23-24 giugno 2026** con campionamento **aprile-giugno**. ⚠️ **Divergono su tre cose insieme**:
quando, che tipo di audit sia, e quando Aurora sarà misurata sull'applicazione della seconda
firma. Nota: `questione-quando-l-ente-torna-a-verificare`.

### D3 — La convalida annuale del metal detector ha tre date ✍️ **scritta**

`11/2025` secondo il rapporto d'audit — cioè **dichiarata all'auditor** — `06-feb-26` secondo
il piano di manutenzione, `04/03/2026` secondo il registro delle attrezzature. ⚠️ **E la
periodicità non torna nemmeno fra i due registri interni**: dodici mesi contro sei, sullo
stesso strumento, nello stesso anno; il manuale HACCP prescrive «verifica annuale». Nota:
`questione-convalida-md-3200-tre-date`.

### D4 — La clausola della NC 1 esiste in tre versioni, e il registro interno le incrocia ✍️ **scritta**

`BRCGS 2.10.2 / IFS 2.3.9.2` (rapporto, verbale di riesame, manuale) · `BRCGS 2.10.2 / IFS
5.1.2` (registro NC interne, `NC-2026-028`) · `BRCGS 3.11.3 / IFS 5.1.2` (mail del 7 aprile).
⚠️ **La combinazione mista è quella con cui Aurora ha archiviato la NC a sistema, e non
compare in nessun documento dell'ente.** Nota: `questione-clausola-della-nc1-in-due-versioni`.

⚠️ **Una quinta gamba esiste e non è citabile**: `PRO-QA-08_gestione_reclami_cliente_rev2.docx`
riga 113 ripete `BRCGS 9 cl. 2.10.2 / IFS 5.1.2`. **Il suo lotto — `3D`, reclami — non è
canonizzato**, e il divieto 9-bis vieta di citarla e di scriverne il contenuto. **Alla
canonizzazione di 3D quella riga va aggiunta alla nota.**

### D5 — La parcella dell'audit di febbraio esiste in quattro versioni incompatibili 🚫 **non scrivibile**

| Fonte | Che cosa dice |
|---|---|
| `Fatture_Elettroniche_SDI_Inbound_Q2.txt` | fattura **2201/26 del 28-02-2026**, «AUDIT COMBINATO BRCGS ISSUE 9 + IFS FOOD V8 - 2 GG UOMO X 2 AUDITOR» |
| `estratto_conto_unicredit_maggio26.csv` riga 59 | bonifico **13/05/26**, **5.490,00**, «FT 2201/26» |
| `report_costi_fissi_OpEx_manutenzioni.txt` righe 176 e 282 | «fattura CSQA n. **2026/1187** = **6.850 €** + iva», «PAGATA il **15/04**» |
| `previsionale_cassa_giugno_agosto2026.xlsx` | «CSQA Certificazioni Srl Saldo audit febbraio 30/06/2026 **6100** sì fattura ferma da marzo» |

⚠️ **Quattro numeri di fattura, importo e data che non si riconciliano.** 🚫 **Tre gambe su
quattro stanno nel lotto 6 (amministrazione), non canonizzato**: la divergenza si registra qui
e **non entra in nessuna nota**. Obbligo esplicito per il lotto che porta l'amministrazione.

### D6 — La durata dell'audit ha un terzo testimone, ed è quello che decide 🚫 **non scrivibile**

Il vault tiene aperta la divergenza fra «2 giorni uomo x 2 auditor (32 h on site)» del rapporto
e «2,0 giornate/uomo on site» del certificato
(`questione-categorie-e-durata-audit-divergenti`, T123). ⚠️ **La fattura decide**: la riga
fatturata è **«2 GG UOMO X 2 AUDITOR»**, cioè la versione del rapporto. 🚫 **Ma la fattura è
del lotto 6**: la nota resta aperta e **non si chiude con questa gamba**. Obbligo esplicito
per il lotto dell'amministrazione, che dovrà tornare su T123.

⚠️ **Corollario contabile, e vale come domanda per S7**: il rinnovo costa **4.850,00** per
**metà** delle giornate/uomo fatturate a febbraio. Nessun documento lo spiega.

### D7 — CSQA ha due partite IVA nel corpus, entrambe valide 🚫 **non scrivibile**

`02603680246` nel piè di pagina della mail del 7 aprile; **`IT02052850241`** nell'intestazione
della fattura elettronica. **Stessa ragione sociale, stesso indirizzo.** ⚠️ **Entrambe superano
il controllo di Luhn**, quindi per la regola di ammissione della tabella alias **non sono una
variante ma due identificativi distinti**: non si uniscono. 🚫 La seconda gamba è del lotto 6:
`entita-csqa-certificazioni` ne porta **una sola**, ed è quella del pacchetto certificazione.

### D8 — Due obblighi di comunicazione con un termine, e nessuna traccia dell'adempimento 🚫 **non scrivibile**

**Il certificato**, condizione 3: gli eventi gravi — richiami, ritiri, allerte, **provvedimenti
dell'Autorità competente** — «devono essere notificati **entro 3 giorni lavorativi**». Il
corpus ha `Verbale_ispezione_ATS_09_06_2026.pdf`, **con diffida**.

**L'accordo quadro Tosano**, art. 11.2: comunicare «entro **5 giorni lavorativi** ogni
sospensione, ritiro, **downgrade** o mancato rinnovo, nonche' l'esito di ogni audit di
certificazione con evidenza delle non conformita' rilevate»; art. 16.2: risoluzione di diritto.

⚠️ **Ricerca su tutto il corpus: ZERO documenti registrano l'una o l'altra comunicazione.**
⚠️ **È l'anello che manca a `fatto-grade-aa-messo-in-guardia`**, che chiama il declassamento il
fatto più pesante del pacchetto **senza sapere che un downgrade è un evento contrattuale con un
termine di cinque giorni**. 🚫 L'accordo Tosano è del lotto 5: obbligo esplicito per quel lotto.


---

## Divergenze nuove — revisione del lotto 3B, 23/08/2026

> **Come si legge questa sezione.** Tredici divergenze su un lotto che porta la **Politica per
> la qualità `DOC-QA-01` rev. 8** e lo **scadenzario della formazione** estratto il 18/05/2026.
> ⚠️ **Otto sono scrivibili, cinque no**: il divieto 9-bis, e stavolta i grezzi che mancano sono
> tre — il registro presenze del corso sicurezza, il fascicolo dell'infortunio e le timbrature.
> ⚠️ **E il lotto ha letto benissimo i due grezzi, quasi mai uno contro il vault**: sette delle
> otto scrivibili nascono dall'accostamento col **verbale di riesame**, canonizzato il giorno
> prima e già citato da decine di note.

### E1 — Reclami per milione: «confezioni» contro «pezzi», e stavolta la gamba è scrivibile

`politica_qualita_e_sicurezza_alimentare_2026.docx`, §GLI OBIETTIVI MISURABILI PER IL 2026:
«Reclami cliente e consumatore / **reclami per milione di confezioni** / **9,4** / **< 8,0**».
`verbale_riesame_direzione_SGQ_2026.txt` §4.1: «Reclami cliente/consumatore anno 2025: n. 41 totali, pari a **0,89 reclami**» e «per milione
di pezzi venduti (obiettivo: **< 1,0** - RAGGIUNTO).»; §10.1: «Reclami / mio pezzi **< 0,85**».

⚠️ **La riga C3 del lotto 3A dava la gamba «confezioni» per NON scrivibile**, perché stava in
`PRO-QA-08` (lotto 3D): **la politica la rende scrivibile oggi**, e aggiunge il **consuntivo**,
che il canone non aveva.

⚠️ **E la conversione di unità non chiude.** Dai due consuntivi: 41/0,89 = **46,07 milioni di
pezzi**, 41/9,4 = **4,36 milioni di confezioni**, rapporto **10,56** *(calcolati)*. Con quel
fattore il target della politica varrebbe **0,76** per milione di pezzi, non **0,85**.
**Nessuno**: due misure dello stesso indicatore su due denominatori, e nessun documento le
riconcilia.

### E2 — Due tabelle di obiettivi 2026 che non si mappano, e un riesame che riconferma «senza modifiche»

Politica: **nove obiettivi** *(contati)*. `verbale_riesame_direzione_SGQ_2026.txt` §10.1:
**nove** *(contati)*. **In comune due soli indicatori** — reclami e ore/addetto — **e su
entrambi i valori divergono**. Un terzo è quasi-omonimo e diverge: «Chiusura azioni correttive,
% chiuse entro scadenza **≥ 95%**» contro «Chiusura NC entro 30 gg **>= 90%**». **Sei righe
della politica non hanno un obiettivo nel verbale, e sei del verbale non hanno una riga nella
politica** *(contate)*.

⚠️ E il verbale §9.5 scrive: «Politica per la sicurezza alimentare: **riconfermata senza
modifiche**, ripubblicata in bacheca con data 12/03/2026».

**Nessuno.** È **C4 del lotto 3A** — il cruscotto che non si mappa col riesame — **con un terzo
documento**: l'azienda porta tre tabelle di obiettivi 2026, e nessuna delle tre cita le altre.

### E3 — Il 97,32 % come «Valore 2025» in un documento emesso il 12/01/2026

Politica, intestazione: «Documento **`DOC-QA-01` rev. 8** — emissione **12/01/2026**»; tabella:
«Mantenimento certificazioni / esito audit BRCGS e IFS / **AA / Higher Level 97,32%**».
`Rilievo_Audit_BRC_IFS_CSQA_febbraio2026.txt`: «Date audit: **17/02/2026 - 18/02/2026**», «IFS
Food v8: **HIGHER LEVEL - 97,32 %**».

**Nessuno, e l'archivio non scioglie.** O l'audit 2025 ha dato lo stesso punteggio **a due
decimali** — e nessun documento del corpus lo dice — oppure quella riga è stata scritta **dopo
il 18/02** in un documento che porta la data del 12/01 e la firma del 15/01. ⚠️ Stessa specie
di **C15 (3A)**: un consuntivo chiuso con un evento fuori dal periodo.

### E4 — «La riunione di riesame di gennaio» che nell'archivio si tiene a marzo

Politica, annotazione di intestazione: «Da far firmare al titolare **PRIMA della riunione di
riesame di gennaio**, non dopo come l'anno scorso».
`verbale_riesame_direzione_SGQ_2026.txt`: «**Data: 12/03/2026** - ore 9:00 / 13:20»; «riesame si e' tenuto in data **14/03/2025**
(verbale RD-2025-01).»; §12.2 «Prossimo riesame ordinario: **marzo 2027**».

**Nessuno.** Il riesame di direzione di Aurora è un evento **di marzo** in tutte e tre le
occorrenze datate del corpus; l'istruzione che governa l'ordine dei gesti ne presuppone uno di
gennaio. ⚠️ **La conseguenza è di merito**: la firma del 15/01 rispetta la prescrizione solo
rispetto a una riunione che quell'anno non risulta essersi tenuta.

### E5 — Il registro dei titoli non registra NULLA del 2026

`registro_presenze_corsi_HACCP_scaduti.csv`, estrazione del **18/05/2026**: righe con `Data
corso` nel 2026 = **zero su 96** *(contate)*; la data di corso più recente è **09/10/2025**.

Contro: `formazione_allergeni_operatori_2026.pptx` slide 1, «Data: **19/03/2026** — turni 1 e 2
in sala mensa, turno 3 il **20/03**» e «**Firma sul registro `MOD-HR-11`** ALL'INGRESSO, non
all'uscita»; `scheda_allergeni_matrice_cross_contamination.docx` §9.2, «Sessione straordinaria
post `NC-2026-055` **erogata il 10/04/2026**»; e **lo stesso registro**, riga 35, colonna
`Note`: «**agg. 4h fatto 03/2026**», su una riga la cui `Data corso` resta `10/12/2024`.

**Nessuno.** ⚠️ **Non è l'assenza di una sessione: è l'assenza dell'intero anno**, e il file
**si contraddice da solo** annotando nelle `Note` un aggiornamento che non ha una riga.
Completa **2B-bis B6**, che il divieto 9-bis teneva fermo e che il lotto 3B ha scaricato solo a
metà. 🚫 Una quarta gamba non è citabile: il corso sicurezza del 14-15/04/2026 — v. **E9**.

### E6 — La sessione di recupero HACCP ha tre date

`verbale_riesame_direzione_SGQ_2026.txt` §11: «**A9** Recupero attestati HACCP in scadenza ·
Sartori · **21/05/2026**».
`scheda_allergeni_matrice_cross_contamination.docx` §9.3: «Richiami HACCP in scadenza: v. azione
A9 del riesame di direzione (**sessione del 21/05/2026, 2 assenti da recuperare il 04/06**)».
`registro_presenze_corsi_HACCP_scaduti.csv` riga 104, estratta il 18/05 **dalla stessa persona
responsabile di A9**: «sessione recupero HACCP **prenotata: 09/06/2026** mattina, aula mensa,
docente Vicentini - max 20 posti».

**Nessuno.** Tre giorni prima della scadenza di `A9` il responsabile dell'azione prenota la
sessione **dopo** la scadenza; la scheda dà la sessione come tenuta il 21/05 con due assenti.
⚠️ **Possibile che la scheda abbia letto la scadenza dell'azione come data della sessione** — ma
i «2 assenti da recuperare il 04/06» sono un dettaglio che una scadenza non produce.

### E7 — «Attestati HACCP in scadenza nel quadrimestre: n. 5» contro i dieci del registro

`verbale_riesame_direzione_SGQ_2026.txt` §7.3, seduta del 12/03/2026: «Attestati HACCP in
scadenza nel quadrimestre: **n. 5** (registro MOD-HR-11).»
`registro_presenze_corsi_HACCP_scaduti.csv`: **dieci** righe `HACCP base` con scadenza
`20/04/2026` *(contate)*, e **nessun altro titolo HACCP in scadenza fra il 12/03 e il
12/07/2026** *(contato)*.

**Il registro.** ⚠️ È la specie isolata nel lotto 1C e ripresa in **C11** — **un'attestazione
resa alla direzione contro il registro che dovrebbe sostenerla** — e qui il verbale cita il
registro **per nome**. ⚠️ **Da quel cinque discende l'azione `A9`**, dimensionata sulla metà del
problema.

### E8 — Quante persone lavorano in Aurora, e la terza gamba che riapre il conto

Politica §LA CULTURA: «ognuna delle **50 persone** che lavorano in Aurora».
`verbale_riesame_direzione_SGQ_2026.txt` §7.1: «Organico al 28/02/2026: **50 unita'** (38
produzione, 12 uffici)».
`registro_presenze_corsi_HACCP_scaduti.csv`: **52 nomi distinti** *(contati)*; tolte la cessata
del 19/04 e la tirocinante che entra il 15/06 restano **50** *(calcolato)*.

🚫 **E la terza gamba riapre tutto**: `verbale_formazione_sicurezza_lavoratori_accordo_stato_regioni.txt`
porta **22 convocati**, di cui **17 nomi che il registro non contiene** *(contati)* — il corpus
ne nomina almeno **69** *(calcolato)*. **Il lotto 3B non poteva vederlo** (9-bis), e la
questione nel vault chiude su «tolti quei due restano cinquanta».
**Obbligo esplicito per il lotto che canonizza la formazione sicurezza.**

### E9 — Il `MOD-HR-11` esiste in archivio, ed è un ALTRO documento 🚫 **non scrivibile**

`verbale_formazione_sicurezza_lavoratori_accordo_stato_regioni.txt`, riga 1: «**`MOD-HR-11`
rev.2 - registro formazione**»; in calce: «**Registrazione su scadenzario formazione
`MOD-HR-11` a cura di F. Sartori**».

⚠️ **Due documenti diversi portano lo stesso codice di modulo**, e il secondo chiama
«scadenzario formazione `MOD-HR-11`» proprio il file del lotto 3B: **il legame che tutte le note
di 3B dichiarano «non affermato da nessuna fonte» È affermato** — e in contraddizione con
l'intestazione dello stesso documento che lo afferma.

⚠️ **E il corso non lascia traccia**: 16 ore il **14-15/04/2026**, 22 partecipanti, attestati
`SBP-FORM-2026-0341`→`0360` — e il registro estratto il **18/05** non porta **nessuna** riga con
quella data. 🚫 Il grezzo non è canonizzato: **obbligo esplicito per il suo lotto**, che dovrà
tornare su **E5**, **E8** e su `doc-scadenzario-formazione-2026`.

### E10 — L'addestramento chiesto per un reparto, registrato su una riga 🚫 **non scrivibile**

`nota_infortunio_INAIL_operaio_linea3.txt`, sopralluogo del 04/05/2026, punto d):
«l'addestramento documentato sulla movimentazione carrelli in cella non e' presente nel
fascicolo (**`MOD-HR-11` privo della voce specifica**)»; richiesta 5: «inserimento
dell'addestramento specifico a registro **per tutti gli addetti Linea 3 e magazzino**».
`registro_presenze_corsi_HACCP_scaduti.csv` riga 47: l'annotazione «addestramento carrelli cella
**DA REGISTRARE** (nota RSPP 05/05)» compare **su una riga sola**, quella dell'infortunato.

**Nessuno.** ⚠️ Terza fonte indipendente che tratta il `MOD-HR-11` come **il registro dei
titoli**, e una prescrizione del RSPP eseguita su una frazione del perimetro chiesto.

### E11 — Un divieto operativo dichiarato, e nessun atto che lo chiuda 🚫 **non scrivibile**

`registro_presenze_corsi_HACCP_scaduti.csv` riga 71: «Preda Radu;Magazziniere;Carrello elevatore
12h;10/04/2021;**10/04/2026**;SCADUTO;CFP Veneto Sicuro;**NON ABILITATO ALLA GUIDA fino a
rinnovo - avvisato Faggionato 05/05**».
`log_timbrature_fabbrica_maggio_settimana2.csv`: `0603;PREDA RADU` in turno `MAGAZZ. T2` il 04,
05, 06, 07, 08 e **domenica 10/05/2026**.

**Nessuno, forza media.** Le timbrature **non dicono che abbia guidato**, e nessun documento
registra il rinnovo: resta **un divieto scritto senza un atto che lo chiuda**. 🚫 Le timbrature
non sono canonizzate.

### E12 — Il testo barrato è contenuto revocato, e il §6 non lo elenca fra i tratti del corpus

Politica: il nono impegno — «perseguire la crescita del fatturato quale obiettivo primario
dell'organizzazione» — sta **nel flusso del testo** ed è **barrato**;
`scheda_allergeni_matrice_cross_contamination_rev6.docx` porta **quattro** frammenti barrati e
dichiara «modifiche non accettate presenti nel documento»;
`contratto_manutenzione_impianto_frigo_TS01.docx` le dichiara in testa.

⚠️ **Un'estrazione che non porta il barrato legge nove impegni invece di otto**, e restituisce
**con citazione vera** l'esatta frase che il consulente ha fatto togliere perché «in audit è un
rilievo servito su un piatto». **Va al §6**, accanto a OCR, encoding e date multiformato.

### E13 — Il quarto quasi-omografo Peruzzi

`Peruzzi Erika`, operaia Linea 2, `HACCP base` 05/05/2024→05/05/2027, «CESSATA 19/04 - riga da
eliminare» (`registro_presenze_corsi_HACCP_scaduti.csv` riga 101), accanto a **Peruffo Maria
Grazia** (visura), **Peruzzi Maurizio** (bilancio) e **Attilio Peruffo** (Frigotecnica). ⚠️ **La
famiglia sale a quattro nel vault**, e a sei nel corpus: 🚫 `PERUZZI Loris` e 🚫 `Peruzzi
Luciano` stanno in due grezzi non canonizzati. **Classe B della tabella alias: non si uniscono
mai.**


## Divergenze nuove — revisione del lotto 3D, 24/08/2026

> Il lotto dei **reclami**: `PRO-QA-08`, la catena della segnalazione del consumatore e la
> catena dell'allerta RASFF. **Sette divergenze**, di cui **cinque scrivibili subito** e due
> con obbligo esplicito per il lotto che porterà la procedura di ritiro.

### F1 — La procedura di ritiro ha DUE CODICI, e le due gambe sono già canonizzate ✍️ **scritta**

`PRO-QA-08` §3 rimanda per il ritiro a **`PRO-QA-11`** «Gestione ritiro e richiamo prodotto»;
il **manuale HACCP** §10.3 rimanda a **`PRO-QA-14` rev. 3** «Gestione ritiro e richiamo del
prodotto», e il §9 del manuale ripete «vedi `PRO-QA-14` per il ritiro». ⚠️ **Nessuno dei due
documenti nomina l'altra sigla**, e il più recente dei due — la procedura, 14/03/2026 — è
quello che usa la sigla che nessun altro documento del corpus conosce: **`PRO-QA-11` compare in
un file solo su 160**, ed è `PRO-QA-08` stessa. Nota:
`questione-due-codici-per-la-procedura-di-ritiro`.

### F2 — `PRO-QA-08` designa DUE procedure diverse ✍️ **scritta**

Il documento con quel codice è la procedura dei **reclami**; il manuale HACCP, nella riga del
prerequisito `PRP-09`, usa la stessa sigla per la procedura di **rintracciabilità**
(identificazione del lotto, mass balance, esercitazione annuale). ⚠️ **Due oggetti, un codice**,
e nessuna fonte che li distingua — mentre la **politica per la qualità** impegna l'azienda «alla
procedura `PRO-QA-08`» per i reclami. Nota:
`questione-pro-qa-08-reclami-o-rintracciabilita`. **Classe C della tabella alias.**

### F3 — Il «riesame trimestrale HACCP» non esiste in nessun'altra fonte ✍️ **scritta**

La responsabile qualità dichiara di registrare l'allerta RASFF «nel **riesame trimestrale
HACCP**». Il manuale dà: team **almeno semestrale** (§4.2), riesame del piano **annuale**
(§12.1); il verbale di riesame colloca il prossimo ordinario a **marzo 2027** (§12.2). ⚠️
**Nessun documento dell'archivio conosce una cadenza trimestrale.** ⚠️ E il §12.1 elenca fra i
trigger di riesame **straordinario** proprio l'«allerta RASFF **su ingredienti in uso**» —
cioè la ragione per cui, non essendo l'additivo in uso, il riesame straordinario **non era
dovuto**. Nota: `questione-riesame-trimestrale-haccp`.

### F4 — La richiesta dell'auditor sulle allerte non è nel rapporto d'audit ✍️ **scritta**

La mail del 19/03 motiva la registrazione con «l'auditor a febbraio ci ha chiesto **proprio di
dimostrare la sorveglianza sistematica sulle allerte RASFF**». Il rapporto dell'audit di
febbraio porta **due non conformità minori e cinque osservazioni**, e **nessuna riguarda le
allerte**: né «allerta» né «RASFF» compaiono nel documento. ⚠️ **Non è detto che sia falso** —
un auditor chiede più di quanto finisca in un rapporto — **ma un'evidenza tenuta a sistema per
rispondere a una richiesta risponde a qualcosa che l'archivio non contiene**. Nota:
`questione-richiesta-auditor-sulle-allerte`.

### F5 — I reclami si contano su due denominatori diversi, e ora la gamba prescrittiva c'è ✍️ **scritta**

`PRO-QA-08` §10 prescrive «reclami totali per milione di **confezioni vendute**», obiettivo
**< 8,0**; la politica per la qualità dice lo stesso; il verbale di riesame §4.1 conta per
milione di **pezzi venduti**, obiettivo **< 1,0** e target 2026 **< 0,85**. ⚠️ **La divergenza
era già a canone da C3 del lotto 3A e da E1 del lotto 3B, e la gamba che mancava era proprio
il prescrittivo**: adesso c'è, e la questione ha una padrona —
`questione-reclami-per-confezioni-o-per-pezzi`.

### F6 — Il grezzo della segnalazione non concorda con sé stesso su quanti turni ✍️ **scritta**

Mail del **13/05 09:22**: quel giorno l'`AF-SN-0450` è stato prodotto solo su Linea 1, e il
lotto è «con ogni probabilità **`L26130-L1-T2` o `-T3`**» — il turno 1 aveva confezionato con
la valvola originale. Mail del **14/05 19:12**: la referenza è stata prodotta «SOLO su Linea 1,
**turni 1 e 2**». ⚠️ **Il turno 3 c'è in una frase e non c'è nell'altra**, a un giorno di
distanza e dalla stessa persona — e la scheda del reclamo blocca **tre** lotti, turno 3
compreso. Si aggiunge alla divergenza già a canone sulla Linea 1 che produce una domenica non
assegnata dal piano. Scritta in `fatto-perimetro-stimato-del-ritiro`.

### F7 — Il suffisso del lotto: letto dalla foto o illeggibile, dalla stessa foto ✍️ **scritta**

La segnalante scrive che dopo il codice ci sono «una L e dei numeri dopo» ma **stampati male**.
La mail interna del **12/05 14:33** dichiara che **dalla foto si legge** `L26130-L1-T2`; quella
del **13/05 09:22** lo dà **non leggibile** e da verificare. ⚠️ **La fotografia è la stessa.**
Scritta in `fatto-segnalazione-dal-form-12-05`.

### F8 — La scheda del reclamo classifica citando un'ALTRA procedura 🚫 **non scrivibile per intero**

`MOD-QA-31` scrive «Classe 2 (**`PRO-QA-14` par. 4**)» in intestazione e ripete «ai sensi del
par. 4 della `PRO-QA-14`» nella valutazione del rischio. ⚠️ **La scheda non dichiara di
applicare la scala di `PRO-QA-08`**: attribuisce la classificazione al paragrafo della
procedura di **ritiro e crisi**. ⚠️ **Che cosa quel paragrafo contenga, il vault non lo può
dire**: il documento appartiene a un lotto non ancora canonizzato, e il divieto 9-bis vale per
intero. **Obbligo esplicito per il lotto che lo porta**: verificare se porti una scala di
classificazione dei reclami, se coincida con quella di `PRO-QA-08` §5, e quale delle due
governi. Nota parziale: `questione-classe-del-reclamo-rec-2026-011`. **T159.**

### F9 — Undici annotazioni di revisione dentro un prescrittivo approvato ✍️ **scritta**

`PRO-QA-08` rev. 2, approvata il 14/03/2026, porta **tre passaggi barrati** e **undici
annotazioni di revisione lasciate nel flusso del testo** *(contate con l'estrazione di
cantiere)*, di cui due datate **02/04** e **12/05** — cioè posteriori all'approvazione. ⚠️ **Il
campo «copia controllata n.» è in bianco**: quello che l'archivio conserva è **una copia di
lavoro**, e le modifiche non sono state accettate. ⚠️ **Dieci annotazioni su undici descrivono
una regola, una richiesta o una lacuna; una sola registra un EVENTO** — «È successo» — ed è
quella da cui nasce il divieto di rispondere a voce al consumatore. Note:
`fatto-pro-qa-08-copia-di-lavoro`, `fatto-nessuno-risponde-a-voce-al-consumatore`.

### F10 — Una prova di solidità del canone, dalla scadenza dichiarata dalla consumatrice

⚠️ **Non è una divergenza: è una conferma, e vale la pena registrarla.** La segnalante dichiara
la scadenza **24/06/2026** su un prodotto del lotto `L26130`, cioè del **10/05/2026**: sono
**45 giorni** *(contati)*, esattamente la shelf life della scheda tecnica in vigore. **Un dato
scritto da un consumatore, senza alcun accesso ai documenti dell'azienda, cade sul valore
prescritto.**
