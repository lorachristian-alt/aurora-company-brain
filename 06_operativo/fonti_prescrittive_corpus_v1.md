# Le fonti prescrittive del corpus v1 — lo strumento di E29

> **Cos'è** · L'elenco dei grezzi che **prescrivono** invece di registrare, con
> che cosa prescrive ciascuno, il lotto a cui appartiene e se è **già canonizzato**.
> Serve alla riconciliazione **verticale** (`metodo_03` §5.1-bis, E29): chi tocca un
> punto critico, una taratura, una frequenza di verifica o una responsabilità di
> processo apre e cita la fonte che lo **prescrive**, o dichiara perché non serve.
> **Dove vive** · `06_operativo\`, **fuori dal vault**: è metodo, non contenuto.
> **Chi lo genera** · `06_operativo\elenco_fonti_prescrittive.py`. Le colonne
> «lotto» e «già canonizzato» le produce lo script; che cosa prescrive è curatela,
> e vive nel sorgente perché abbia un padrone solo.
> **Generato il** · 2026-08-19

---

## Il criterio, per non doverlo indovinare

Un grezzo è una **fonte prescrittiva** se dice **come una cosa DEVE essere** — un
limite, una frequenza, un metodo, una responsabilità, una specifica, un obbligo, una
tariffa in vigore — invece di **registrare ciò che è successo**.

| | |
|---|---|
| **Prescrivono** | manuali, istruzioni operative, procedure, capitolati, schede tecniche, politiche, piani, contratti e accordi firmati, autorizzazioni, listini e tariffe in vigore, circolari normative |
| **Registrano** | log, registri, rapporti di prova, verbali, bolle, fatture, mail, quaderni, cruscotti, analisi, preventivi non accettati |
| **`misto`** | prescrive **e** registra: un piano di manutenzione detta la periodicità e annota le esecuzioni. Per la riconciliazione verticale vale come prescrittivo — ciò che conta è che contenga una prescrizione da citare |

⚠️ **Un certificato non è una fonte prescrittiva**: attesta uno stato, non lo
prescrive. Il requisito che dimostra vive nella norma, che in questo corpus non c'è.
Per lo stesso motivo un listino **superato** non è in vigore: è la fotografia di una
prescrizione passata.

---

## ⚠️ La guardia: citabile solo se il suo lotto è già canonizzato

Una fonte prescrittiva il cui grezzo appartiene a un lotto **non ancora canonizzato**
**non si cita e non si usa**. Citarla la farebbe risultare «già coperta» e manderebbe
in rosso la disgiunzione della matrice; **scriverne il contenuto senza citarla è
contesto importato**, cioè il difetto che ha richiesto quattro giri di giudizio nel
lotto 1B. Si apre invece una riga nella **tabella di tracciamento**, con l'obbligo
esplicito per il lotto che la porterà. Precedente identico: **T18**.

| | Quante |
|---|---|
| **CITABILI oggi** (grezzo già canonizzato) | **10** |
| **DA TRACCIARE** (grezzo in un lotto futuro) | **26** |
| **totale fonti prescrittive** | **36** |

---

## L'elenco

| Grezzo | Classe | Che cosa prescrive | Lotto | Già canonizzato | Citabile in R1 |
|---|---|---|---|---|---|
| `Scheda_tecnica_prodotto_AF-SN-0450_rev4.pdf` | prescrittiva | Le **specifiche del prodotto finito**: parametri chimico-fisici, tetto dell'ossigeno residuo in confezione, TMC, dati di imballo. E' cio' che il prodotto DEVE essere, contro cio' che le prove misurano | lotto_01a_linea1_turno_ccp | **sì** | **sì** |
| `checklist_metal_detector_manuale_operaio.txt` | prescrittiva | **Come e quando** si verifica il metal detector: cadenza dei controlli, tasselli di prova da usare, che cosa si registra. E' l'istruzione operativa del CCP3 | lotto_01a_linea1_turno_ccp | **sì** | **sì** |
| `manuale_uso_manutenzione_PKM450_estratto.pdf` | prescrittiva | Uso e manutenzione della confezionatrice di Linea 1: ricambi prescritti, codifica degli allarmi, interventi periodici. E' la fonte del costruttore, e prevale su un piano interno quando dicono cose diverse | lotto_01a_linea1_turno_ccp | **sì** | **sì** |
| `piano_produzione_settimanale_sett19_21.xlsx` | misto | **Prescrive** che cosa si produce, su quale linea e in quale turno, e **registra** il programma effettivamente emesso. E' il termine contro cui si legge una produzione fuori piano | lotto_01a_linea1_turno_ccp | **sì** | **sì** |
| `scheda_manutenzione_ordinaria_forni_industrial.csv` | misto | **Prescrive la periodicita'** degli interventi su impianti e strumenti, e **registra** le esecuzioni. E' uno dei due registri paralleli della metrologia trovati nel lotto 1C | lotto_01a_linea1_turno_ccp | **sì** | **sì** |
| `contratto_manutenzione_impianto_frigo_TS01.docx` | prescrittiva | Obblighi di manutenzione sugli impianti del freddo: perimetro degli impianti coperti, periodicita', adempimenti F-gas, responsabilita' del manutentore. ⚠️ E' una **bozza mai firmata**, ed e' un fatto gia' canonizzato: prescrive cio' che le parti avevano concordato di scrivere, non un obbligo perfezionato | lotto_01b_freddo_energia | **sì** | **sì** |
| `elenco_attrezzature_taratura_strumenti_2026.csv` | misto | **Prescrive** la periodicita' di taratura e convalida del parco strumenti, e **registra** lo stato di ciascuno. E' l'altro dei due registri paralleli della metrologia | lotto_01c_metrologia_gas | **sì** | **sì** |
| `IO-05_istruzione_operativa_lavaggio_CIP.docx` | prescrittiva | L'istruzione operativa del lavaggio CIP: fasi, parametri, registrazioni obbligatorie | lotto_02a_cip | **sì** | **sì** |
| `scheda_sicurezza_detergente_acido_lavaggio_CIP.txt` | prescrittiva | Condizioni d'uso e di sicurezza del detergente acido del CIP | lotto_02a_cip | **sì** | **sì** |
| `manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt` | prescrittiva | I punti critici di controllo, i loro **limiti critici**, le **frequenze di verifica**, le **azioni correttive** e **chi ne risponde**. E' la fonte prescrittiva madre del corpus: ogni nota che nomina un CCP, una taratura o una frequenza di verifica ricade su questa | pilota (fetta L26130) | **sì** | **sì** |
| `piano_autocontrollo_acqua_potabile_analisi.csv` | misto | **Prescrive** il piano di autocontrollo dell'acqua potabile - punti, parametri, frequenze - e **registra** gli esiti | lotto_02b_autocontrollo_igiene | no | **NO** — si traccia |
| `scheda_allergeni_matrice_cross_contamination.docx` | prescrittiva | La matrice della contaminazione incrociata da allergeni: che cosa non puo' seguire che cosa, e con quale bonifica | lotto_02b_autocontrollo_igiene | no | **NO** — si traccia |
| `DoC_MOCA_Flexipack_film_PP_EVOH_2026.pdf` | prescrittiva | La dichiarazione di conformita' del materiale a contatto: **condizioni d'impiego** entro cui il film e' dichiarato idoneo | lotto_02c_moca | no | **NO** — si traccia |
| `capitolato_tecnico_fornitura_imballaggi_plastici.txt` | prescrittiva | Le specifiche tecniche che il film di imballaggio deve rispettare. E' il termine prescrittivo della divergenza sulla barriera al vapore gia' registrata nella matrice | lotto_02c_moca | no | **NO** — si traccia |
| `PRO-QA-08_gestione_reclami_cliente_rev2.docx` | prescrittiva | La procedura di gestione dei reclami: tempi di risposta, responsabilita', registrazioni | lotto_03_sistema_qualita | no | **NO** — si traccia |
| `politica_qualita_e_sicurezza_alimentare_2026.docx` | prescrittiva | La politica per la qualita' e la sicurezza alimentare: impegni della direzione e responsabilita' assegnate | lotto_03_sistema_qualita | no | **NO** — si traccia |
| `procedura_ritiro_prodotto_CRISI_GDO.txt` | prescrittiva | La procedura di ritiro e richiamo del prodotto: chi decide, in quanto tempo, con quali comunicazioni | lotto_03_sistema_qualita | no | **NO** — si traccia |
| `Listino_MolinoVeneto_giu2026.pdf` | prescrittiva | Il listino del fornitore in vigore da giugno 2026 | lotto_04_filiera_logistica | no | **NO** — si traccia |
| `contratto_fornitura_MolinoVeneto_2026_firmato.pdf` | prescrittiva | Il contratto **firmato** di fornitura della farina: formula di indicizzazione, prezzi, modalita' di consegna. Prevale sul listino, ed e' una contraddizione con vincitore gia' registrata nel canone | lotto_04_filiera_logistica | no | **NO** — si traccia |
| `scheda_tecnica_farina_tipo_0_MolinoVeneto.txt` | prescrittiva | Le specifiche della farina tipo 0: parametri, TMC, modo di conservazione | lotto_04_filiera_logistica | no | **NO** — si traccia |
| `tariffe_vettori_terzi_trasporto_fresco_2026.csv` | prescrittiva | Le tariffe di trasporto in vigore per i vettori terzi del fresco | lotto_04_filiera_logistica | no | **NO** — si traccia |
| `accordo_quadro_private_label_Tosano_2026_firmato.txt` | prescrittiva | L'accordo quadro **firmato** con il cliente per la private label: condizioni, dati di imballo, impegni di servizio | lotto_05_commerciale | no | **NO** — si traccia |
| `listino_prezzi_canale_GDO_fresco_v3.csv` | prescrittiva | Il listino GDO in vigore (rev. 3). ⚠️ La rev. 2 dello stesso listino e' **superata dal 01/03/2026** e non e' una fonte prescrittiva in vigore: e' la fotografia di una prescrizione passata | lotto_05_commerciale | no | **NO** — si traccia |
| `Circolare_INPS_aliquote_contributive_2026.txt` | prescrittiva | Le aliquote contributive in vigore. E' l'unica fonte prescrittiva **esterna e normativa** del corpus | lotto_07_persone | no | **NO** — si traccia |
| `job_description_responsabile_produzione.docx` | prescrittiva | Le responsabilita' assegnate al responsabile di produzione. E' la fonte prescrittiva delle note che dicono **chi risponde di cosa** in reparto | lotto_07_persone | no | **NO** — si traccia |
| `piano_turni_apprendisti_tecnologi_food.txt` | prescrittiva | Il piano dei turni degli apprendisti tecnologi: chi c'e', quando | lotto_07_persone | no | **NO** — si traccia |
| `reperibilita_gennaio_febbraio_2026.csv` | prescrittiva | Il calendario di reperibilita': chi risponde fuori orario | lotto_07_persone | no | **NO** — si traccia |
| `AUA_autorizzazione_unica_ambientale_scarichi.pdf` | prescrittiva | I **limiti di scarico** autorizzati e le frequenze di autocontrollo che l'autorizzazione impone | lotto_08_sicurezza_ambiente | no | **NO** — si traccia |
| `CPI_certificato_prevenzione_incendi_VVF.pdf` | prescrittiva | Le condizioni di esercizio antincendio a cui il certificato subordina l'attivita' | lotto_08_sicurezza_ambiente | no | **NO** — si traccia |
| `DVR_estratto_valutazione_rischi_2026.pdf` | prescrittiva | Le misure di prevenzione e protezione prescritte, e chi ne risponde | lotto_08_sicurezza_ambiente | no | **NO** — si traccia |
| `assicurazione_polizza_RCT_RCO_quietanza_2026.pdf` | prescrittiva | Coperture, massimali ed esclusioni della RCT/RCO: e' cio' che DEVE valere in caso di sinistro | lotto_08_sicurezza_ambiente | no | **NO** — si traccia |
| `polizza_RC_prodotto_rinnovo_2026_OCR.txt` | prescrittiva | Coperture, massimali ed esclusioni della RC prodotto | lotto_08_sicurezza_ambiente | no | **NO** — si traccia |
| `mail_fornitore_ingrediente_nuovo_paprika_specifiche.txt` | prescrittiva | Le specifiche dell'ingrediente nuovo dichiarate dal fornitore | lotto_09_rd_investimenti | no | **NO** — si traccia |
| `ricetta_base_esperimento_snack_salato_v12.txt` | prescrittiva | La formulazione: quantita' e ordine, cioe' come il prodotto DEVE essere fatto | lotto_09_rd_investimenti | no | **NO** — si traccia |
| `manutenzione_fotocopiatrice_contratto_copie.csv` | prescrittiva | Obblighi del contratto copie. Fonte prescrittiva **minore**, come sopra | lotto_10_rumore_archivio | no | **NO** — si traccia |
| `noleggio_distributori_automatici_contratto.txt` | prescrittiva | Obblighi del contratto di noleggio. Fonte prescrittiva **minore**, senza aggancio a punti critici o responsabilita' di processo | lotto_10_rumore_archivio | no | **NO** — si traccia |
