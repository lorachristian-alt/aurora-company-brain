# -*- coding: utf-8 -*-
"""elenco_fonti_prescrittive — lo strumento di E29, la riconciliazione VERTICALE.

metodo_03 §5.1-bis. La riconciliazione ORIZZONTALE confronta i documenti che REGISTRANO
la stessa grandezza, e si trova da se': i numeri stonano. La VERTICALE cerca il documento
che PRESCRIVE come quella grandezza vada misurata, e **non si trova da sola** - perche' chi
scrive la nota sta guardando il registro, e il documento che prescrive e' da un'altra parte
dell'archivio. Nel lotto 1C undici note discutevano CCP, tarature e frequenze senza il
manuale HACCP, e in QUATTRO casi il manuale conteneva esattamente cio' che la nota
dichiarava mancante.

IL CRITERIO, e va scritto perche' la lista non e' ovvia:
  Un grezzo e' una FONTE PRESCRITTIVA se dice **come una cosa DEVE essere** - un limite, una
  frequenza, un metodo, una responsabilita', una specifica, un obbligo, una tariffa in
  vigore - invece di **registrare cio' che e' successo**.
  Prescrivono: manuali, istruzioni operative, procedure, capitolati, schede tecniche,
  politiche, piani, contratti e accordi firmati, autorizzazioni, listini e tariffe in
  vigore, circolari normative.
  Registrano: log, registri, rapporti di prova, verbali, bolle, fatture, mail, quaderni,
  cruscotti, analisi, preventivi non accettati.
  ⚠️ Alcuni documenti fanno **tutte e due le cose** - un piano di manutenzione prescrive la
  periodicita' E registra le esecuzioni. Sono marcati `misto`, e per R1 valgono come
  prescrittivi: cio' che conta e' che contengano una prescrizione da citare.
  ⚠️ Un CERTIFICATO o un'attestazione **non e' una fonte prescrittiva**: attesta uno stato,
  non lo prescrive. Il requisito che quel certificato dimostra vive nella norma, che in
  questo corpus non c'e'.

⚠️ LA GUARDIA PIU' IMPORTANTE DI R1, ed e' il motivo per cui la colonna «citabile» esiste:
  una fonte prescrittiva il cui grezzo appartiene a un lotto NON ancora canonizzato
  **non si cita e non si usa**. Citarla la farebbe risultare «gia' coperta» e manderebbe in
  rosso la disgiunzione della matrice (`verifica_matrice_lotti.py`, controllo 4);
  scriverne il contenuto senza citarla e' **contesto importato**, cioe' il difetto che ha
  richiesto quattro giri di giudizio nel lotto 1B. Si apre una riga nella tabella di
  tracciamento con l'obbligo esplicito per il lotto che la porta.
  Precedente identico: T18, dove la terza gamba stava in un file del lotto 10 ed e' stata
  TRACCIATA invece che usata.

Che cosa e' scritto a mano qui dentro e che cosa no:
  - **a mano**: quali grezzi prescrivono e che cosa prescrivono. E' un giudizio, e sta qui
    perche' abbia un padrone solo e si possa discutere;
  - **da script**: il lotto di appartenenza (dagli elenchi in `qa\\lotti\\` e dalla fetta
    pilota), se il grezzo e' GIA' CANONIZZATO (incrociando i `fonti` di tutte le note del
    vault) e quindi se e' CITABILE. Questi tre non si scrivono a mano, mai.

Uso:
    python elenco_fonti_prescrittive.py            # scrive fonti_prescrittive_corpus_v1.md
    python elenco_fonti_prescrittive.py --stdout   # solo a schermo, non scrive
Esce 0 se l'elenco e' integro, 1 se un grezzo non esiste o non sta in nessun lotto.
"""
import argparse, io, os, sys
from datetime import date

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(QUI, "qa"))
import qa_comune as Q

DIR_LOTTI = os.path.join(QUI, "qa", "lotti")
PILOTA = os.path.join(QUI, "qa", "fetta_l26130.txt")
USCITA = os.path.join(QUI, "fonti_prescrittive_corpus_v1.md")

# ---------------------------------------------------------------------------
# La curatela: (grezzo, classe, che cosa prescrive).
# `classe`: prescrittiva | misto  -- «misto» prescrive E registra.
# ---------------------------------------------------------------------------
FONTI = [
    ("manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt", "prescrittiva",
     "I punti critici di controllo, i loro **limiti critici**, le **frequenze di verifica**, "
     "le **azioni correttive** e **chi ne risponde**. E' la fonte prescrittiva madre del corpus: "
     "ogni nota che nomina un CCP, una taratura o una frequenza di verifica ricade su questa"),
    ("Scheda_tecnica_prodotto_AF-SN-0450_rev4.pdf", "prescrittiva",
     "Le **specifiche del prodotto finito**: parametri chimico-fisici, tetto dell'ossigeno "
     "residuo in confezione, TMC, dati di imballo. E' cio' che il prodotto DEVE essere, "
     "contro cio' che le prove misurano"),
    ("manuale_uso_manutenzione_PKM450_estratto.pdf", "prescrittiva",
     "Uso e manutenzione della confezionatrice di Linea 1: ricambi prescritti, codifica degli "
     "allarmi, interventi periodici. E' la fonte del costruttore, e prevale su un piano interno "
     "quando dicono cose diverse"),
    ("checklist_metal_detector_manuale_operaio.txt", "prescrittiva",
     "**Come e quando** si verifica il metal detector: cadenza dei controlli, tasselli di prova "
     "da usare, che cosa si registra. E' l'istruzione operativa del CCP3"),
    ("scheda_manutenzione_ordinaria_forni_industrial.csv", "misto",
     "**Prescrive la periodicita'** degli interventi su impianti e strumenti, e **registra** le "
     "esecuzioni. E' uno dei due registri paralleli della metrologia trovati nel lotto 1C"),
    ("piano_produzione_settimanale_sett19_21.xlsx", "misto",
     "**Prescrive** che cosa si produce, su quale linea e in quale turno, e **registra** il "
     "programma effettivamente emesso. E' il termine contro cui si legge una produzione fuori piano"),
    ("contratto_manutenzione_impianto_frigo_TS01.docx", "prescrittiva",
     "Obblighi di manutenzione sugli impianti del freddo: perimetro degli impianti coperti, "
     "periodicita', adempimenti F-gas, responsabilita' del manutentore. ⚠️ E' una **bozza mai "
     "firmata**, ed e' un fatto gia' canonizzato: prescrive cio' che le parti avevano concordato "
     "di scrivere, non un obbligo perfezionato"),
    ("elenco_attrezzature_taratura_strumenti_2026.csv", "misto",
     "**Prescrive** la periodicita' di taratura e convalida del parco strumenti, e **registra** "
     "lo stato di ciascuno. E' l'altro dei due registri paralleli della metrologia"),
    ("IO-05_istruzione_operativa_lavaggio_CIP.docx", "prescrittiva",
     "L'istruzione operativa del lavaggio CIP: fasi, parametri, registrazioni obbligatorie"),
    ("scheda_sicurezza_detergente_acido_lavaggio_CIP.txt", "prescrittiva",
     "Condizioni d'uso e di sicurezza del detergente acido del CIP"),
    ("scheda_allergeni_matrice_cross_contamination.docx", "prescrittiva",
     "La matrice della contaminazione incrociata da allergeni: che cosa non puo' seguire che cosa, "
     "e con quale bonifica"),
    ("capitolato_tecnico_fornitura_imballaggi_plastici.txt", "prescrittiva",
     "Le specifiche tecniche che il film di imballaggio deve rispettare. E' il termine prescrittivo "
     "della divergenza sulla barriera al vapore gia' registrata nella matrice"),
    ("DoC_MOCA_Flexipack_film_PP_EVOH_2026.pdf", "prescrittiva",
     "La dichiarazione di conformita' del materiale a contatto: **condizioni d'impiego** entro cui "
     "il film e' dichiarato idoneo"),
    ("piano_autocontrollo_acqua_potabile_analisi.csv", "misto",
     "**Prescrive** il piano di autocontrollo dell'acqua potabile - punti, parametri, frequenze - e "
     "**registra** gli esiti"),
    ("PRO-QA-08_gestione_reclami_cliente_rev2.docx", "prescrittiva",
     "La procedura di gestione dei reclami: tempi di risposta, responsabilita', registrazioni"),
    ("procedura_ritiro_prodotto_CRISI_GDO.txt", "prescrittiva",
     "La procedura di ritiro e richiamo del prodotto: chi decide, in quanto tempo, con quali "
     "comunicazioni"),
    ("politica_qualita_e_sicurezza_alimentare_2026.docx", "prescrittiva",
     "La politica per la qualita' e la sicurezza alimentare: impegni della direzione e "
     "responsabilita' assegnate"),
    ("contratto_fornitura_MolinoVeneto_2026_firmato.pdf", "prescrittiva",
     "Il contratto **firmato** di fornitura della farina: formula di indicizzazione, prezzi, "
     "modalita' di consegna. Prevale sul listino, ed e' una contraddizione con vincitore gia' "
     "registrata nel canone"),
    ("scheda_tecnica_farina_tipo_0_MolinoVeneto.txt", "prescrittiva",
     "Le specifiche della farina tipo 0: parametri, TMC, modo di conservazione"),
    ("Listino_MolinoVeneto_giu2026.pdf", "prescrittiva",
     "Il listino del fornitore in vigore da giugno 2026"),
    ("tariffe_vettori_terzi_trasporto_fresco_2026.csv", "prescrittiva",
     "Le tariffe di trasporto in vigore per i vettori terzi del fresco"),
    ("accordo_quadro_private_label_Tosano_2026_firmato.txt", "prescrittiva",
     "L'accordo quadro **firmato** con il cliente per la private label: condizioni, dati di "
     "imballo, impegni di servizio"),
    ("listino_prezzi_canale_GDO_fresco_v3.csv", "prescrittiva",
     "Il listino GDO in vigore (rev. 3). ⚠️ La rev. 2 dello stesso listino e' **superata dal "
     "01/03/2026** e non e' una fonte prescrittiva in vigore: e' la fotografia di una prescrizione "
     "passata"),
    ("job_description_responsabile_produzione.docx", "prescrittiva",
     "Le responsabilita' assegnate al responsabile di produzione. E' la fonte prescrittiva delle "
     "note che dicono **chi risponde di cosa** in reparto"),
    ("piano_turni_apprendisti_tecnologi_food.txt", "prescrittiva",
     "Il piano dei turni degli apprendisti tecnologi: chi c'e', quando"),
    ("reperibilita_gennaio_febbraio_2026.csv", "prescrittiva",
     "Il calendario di reperibilita': chi risponde fuori orario"),
    ("Circolare_INPS_aliquote_contributive_2026.txt", "prescrittiva",
     "Le aliquote contributive in vigore. E' l'unica fonte prescrittiva **esterna e normativa** "
     "del corpus"),
    ("DVR_estratto_valutazione_rischi_2026.pdf", "prescrittiva",
     "Le misure di prevenzione e protezione prescritte, e chi ne risponde"),
    ("AUA_autorizzazione_unica_ambientale_scarichi.pdf", "prescrittiva",
     "I **limiti di scarico** autorizzati e le frequenze di autocontrollo che l'autorizzazione impone"),
    ("CPI_certificato_prevenzione_incendi_VVF.pdf", "prescrittiva",
     "Le condizioni di esercizio antincendio a cui il certificato subordina l'attivita'"),
    ("assicurazione_polizza_RCT_RCO_quietanza_2026.pdf", "prescrittiva",
     "Coperture, massimali ed esclusioni della RCT/RCO: e' cio' che DEVE valere in caso di sinistro"),
    ("polizza_RC_prodotto_rinnovo_2026_OCR.txt", "prescrittiva",
     "Coperture, massimali ed esclusioni della RC prodotto"),
    ("mail_fornitore_ingrediente_nuovo_paprika_specifiche.txt", "prescrittiva",
     "Le specifiche dell'ingrediente nuovo dichiarate dal fornitore"),
    ("ricetta_base_esperimento_snack_salato_v12.txt", "prescrittiva",
     "La formulazione: quantita' e ordine, cioe' come il prodotto DEVE essere fatto"),
    # ⚠️ LOTTO 3C, 22/08/2026. Le due fonti che il pacchetto certificazione porta dentro, e
    # sono la prima applicazione della regola affinata qui sopra: **un certificato non
    # prescrive i requisiti che attesta, ma prescrive le proprie condizioni di validita'**.
    ("Certificato_BRCGS_Food_Issue9_Aurora_2026.pdf", "misto",
     "**Attesta** il grade AA e lo scope certificato — e per quella meta' NON e' prescrittivo, "
     "perche' i requisiti dello standard nel corpus non ci sono. ⚠️ **Ma le sei CONDIZIONI DI "
     "VALIDITA' E USO DEL MARCHIO prescrivono**, e vincolano: il logo BRCGS si usa solo nella "
     "comunicazione business-to-business ed **e' vietato sul prodotto e sul suo imballo "
     "primario**; ogni modifica significativa di processo, layout, scope o assetto societario "
     "va comunicata **entro 3 giorni lavorativi**, e altrettanto gli eventi gravi — richiami, "
     "ritiri, allerte, provvedimenti dell'Autorita'; il certificato non e' trasferibile e resta "
     "di proprieta' dell'ente"),
    ("Conferma_incarico_audit_rinnovo_2026.pdf", "prescrittiva",
     "Gli obblighi dell'incarico di audit di rinnovo: la **documentazione preliminare da "
     "trasmettere almeno 20 giorni prima** della data concordata e il suo elenco puntuale, la "
     "restituzione controfirmata **entro il 20/04/2026**, il corrispettivo e i termini di "
     "pagamento. ⚠️ E prescrive in avanti anche una conseguenza: **un ulteriore ritardo nella "
     "chiusura delle NC apre una non conformita' sul processo di gestione delle azioni "
     "correttive**"),
    ("noleggio_distributori_automatici_contratto.txt", "prescrittiva",
     "Obblighi del contratto di noleggio. Fonte prescrittiva **minore**, senza aggancio a punti "
     "critici o responsabilita' di processo"),
    ("manutenzione_fotocopiatrice_contratto_copie.csv", "prescrittiva",
     "Obblighi del contratto copie. Fonte prescrittiva **minore**, come sopra"),
]


def elenchi_dei_lotti():
    """nome del grezzo -> lotto, letto dagli elenchi. Il lotto non si scrive a mano."""
    dove = {}
    sorgenti = [("pilota (fetta L26130)", PILOTA)]
    for n in sorted(os.listdir(DIR_LOTTI)):
        if n.endswith(".txt") and not n.endswith("_note.txt"):
            sorgenti.append((n[:-4], os.path.join(DIR_LOTTI, n)))
    for etichetta, percorso in sorgenti:
        with io.open(percorso, encoding="utf-8") as f:
            for r in f:
                r = r.strip()
                if r and not r.startswith("#"):
                    dove[r] = etichetta
    return dove


def grezzi_citati():
    """I grezzi che almeno una nota del vault cita in `fonti`. Da script, mai a memoria."""
    citati = set()
    for n in Q.tutte_le_note():
        citati |= {str(f) for f in n.fonti}
    return citati


def main():
    ap = argparse.ArgumentParser(description="L'elenco delle fonti prescrittive del corpus (E29).")
    ap.add_argument("--stdout", action="store_true", help="stampa e basta, non scrive il file")
    args = ap.parse_args()

    dove = elenchi_dei_lotti()
    citati = grezzi_citati()
    nel_manifest = Q.manifest_nomi()
    errori = []

    righe, citabili, tracciate = [], [], []
    for nome, classe, cosa in FONTI:
        if nome not in nel_manifest:
            errori.append("%s: non esiste nel manifest del corpus v1" % nome)
        lotto = dove.get(nome)
        if lotto is None:
            errori.append("%s: non compare in nessun elenco di lotto" % nome)
            lotto = "(nessun lotto)"
        gia = nome in citati
        righe.append((nome, classe, cosa, lotto, gia))
        (citabili if gia else tracciate).append(nome)

    fuori = []
    fuori.append("# Le fonti prescrittive del corpus v1 — lo strumento di E29\n")
    fuori.append("> **Cos'è** · L'elenco dei grezzi che **prescrivono** invece di registrare, con")
    fuori.append("> che cosa prescrive ciascuno, il lotto a cui appartiene e se è **già canonizzato**.")
    fuori.append("> Serve alla riconciliazione **verticale** (`metodo_03` §5.1-bis, E29): chi tocca un")
    fuori.append("> punto critico, una taratura, una frequenza di verifica o una responsabilità di")
    fuori.append("> processo apre e cita la fonte che lo **prescrive**, o dichiara perché non serve.")
    fuori.append("> **Dove vive** · `06_operativo\\`, **fuori dal vault**: è metodo, non contenuto.")
    fuori.append("> **Chi lo genera** · `06_operativo\\elenco_fonti_prescrittive.py`. Le colonne")
    fuori.append("> «lotto» e «già canonizzato» le produce lo script; che cosa prescrive è curatela,")
    fuori.append("> e vive nel sorgente perché abbia un padrone solo.")
    fuori.append("> **Generato il** · %s\n" % date.today().isoformat())
    fuori.append("---\n")
    fuori.append("## Il criterio, per non doverlo indovinare\n")
    fuori.append("Un grezzo è una **fonte prescrittiva** se dice **come una cosa DEVE essere** — un")
    fuori.append("limite, una frequenza, un metodo, una responsabilità, una specifica, un obbligo, una")
    fuori.append("tariffa in vigore — invece di **registrare ciò che è successo**.\n")
    fuori.append("| | |")
    fuori.append("|---|---|")
    fuori.append("| **Prescrivono** | manuali, istruzioni operative, procedure, capitolati, schede tecniche, politiche, piani, contratti e accordi firmati, autorizzazioni, listini e tariffe in vigore, circolari normative |")
    fuori.append("| **Registrano** | log, registri, rapporti di prova, verbali, bolle, fatture, mail, quaderni, cruscotti, analisi, preventivi non accettati |")
    fuori.append("| **`misto`** | prescrive **e** registra: un piano di manutenzione detta la periodicità e annota le esecuzioni. Per la riconciliazione verticale vale come prescrittivo — ciò che conta è che contenga una prescrizione da citare |")
    fuori.append("")
    fuori.append("⚠️ **Un certificato non è una fonte prescrittiva PER I REQUISITI CHE ATTESTA**: quelli")
    fuori.append("vivono nella norma, che in questo corpus non c'è. ⚠️ **Ma le CONDIZIONI DI VALIDITÀ")
    fuori.append("stampate sul certificato prescrivono, e vincolano l'azienda**: dove si può usare il")
    fuori.append("marchio e dove no, entro quanti giorni si comunica una modifica di processo, che cosa")
    fuori.append("fa decadere il titolo. **Affinata il 22/08/2026, aprendo il lotto 3C**: la formulazione")
    fuori.append("precedente — «un certificato non è una fonte prescrittiva», senza distinzioni — avrebbe")
    fuori.append("tenuto fuori dall'elenco un documento che impone **sei obblighi numerati** con un")
    fuori.append("termine di tre giorni lavorativi. ⚠️ **La regola vecchia era vera sulla METÀ del")
    fuori.append("documento che aveva guardato.**\n")
    fuori.append("Per lo stesso motivo un listino **superato** non è in vigore: è la fotografia di una")
    fuori.append("prescrizione passata.\n")
    fuori.append("---\n")
    fuori.append("## ⚠️ La guardia: citabile solo se il suo lotto è già canonizzato\n")
    fuori.append("Una fonte prescrittiva il cui grezzo appartiene a un lotto **non ancora canonizzato**")
    fuori.append("**non si cita e non si usa**. Citarla la farebbe risultare «già coperta» e manderebbe")
    fuori.append("in rosso la disgiunzione della matrice; **scriverne il contenuto senza citarla è")
    fuori.append("contesto importato**, cioè il difetto che ha richiesto quattro giri di giudizio nel")
    fuori.append("lotto 1B. Si apre invece una riga nella **tabella di tracciamento**, con l'obbligo")
    fuori.append("esplicito per il lotto che la porterà. Precedente identico: **T18**.\n")
    fuori.append("| | Quante |")
    fuori.append("|---|---|")
    fuori.append("| **CITABILI oggi** (grezzo già canonizzato) | **%d** |" % len(citabili))
    fuori.append("| **DA TRACCIARE** (grezzo in un lotto futuro) | **%d** |" % len(tracciate))
    fuori.append("| **totale fonti prescrittive** | **%d** |" % len(righe))
    fuori.append("")
    fuori.append("---\n")
    fuori.append("## L'elenco\n")
    fuori.append("| Grezzo | Classe | Che cosa prescrive | Lotto | Già canonizzato | Citabile in R1 |")
    fuori.append("|---|---|---|---|---|---|")
    for nome, classe, cosa, lotto, gia in sorted(righe, key=lambda r: (not r[4], r[3], r[0])):
        fuori.append("| `%s` | %s | %s | %s | %s | %s |"
                     % (nome, classe, cosa, lotto,
                        "**sì**" if gia else "no",
                        "**sì**" if gia else "**NO** — si traccia"))
    fuori.append("")

    testo = "\n".join(fuori)
    if args.stdout:
        print(testo)
    else:
        with io.open(USCITA, "w", encoding="utf-8", newline="\n") as f:
            f.write(testo)
        print("scritto: %s" % USCITA)

    print("\nFonti prescrittive: %d · citabili in R1: %d · da tracciare: %d"
          % (len(righe), len(citabili), len(tracciate)))
    print("Citabili: %s" % ", ".join(sorted(citabili)))
    if errori:
        print("\nERRORI: %d" % len(errori))
        for e in errori:
            print("  - " + e)
        return 1
    print("\nElenco integro: ogni grezzo esiste nel manifest e sta in esattamente un lotto.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
