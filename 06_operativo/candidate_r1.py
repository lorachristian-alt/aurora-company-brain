# -*- coding: utf-8 -*-
"""candidate_r1 — il perimetro del lotto R1, generato da script e mai a memoria.

E35 lo impone: in un lotto di manutenzione **l'elenco delle note lo genera uno script**, e
il criterio con cui lo genera **si scrive nel rapporto**. Un perimetro composto a memoria si
restringe da se', e si restringe proprio sulle note che hanno piu' probabilita' di essere
sfuggite - che sono le stesse che sono sfuggite la prima volta.

IL CRITERIO, in due condizioni che devono valere INSIEME:

  1. la nota **nomina** almeno una delle cinque cose che una fonte prescrittiva governa:
     un punto critico, una taratura o convalida, una frequenza di verifica, un limite, o
     una responsabilita' di processo;
  2. e fra le sue `fonti` **non c'e' la fonte prescrittiva che governa quella famiglia**.
     Per quattro famiglie su cinque questo vuol dire «nessuna fonte prescrittiva», che e' il
     criterio dettato in apertura del lotto. Per la famiglia **punto critico** vuol dire
     specificamente **il manuale HACCP**, e il rafforzamento e' deliberato.

  ⚠️ PERCHE' LA QUINTA FAMIGLIA E' TRATTATA A PARTE, ed e' una correzione al criterio
  dettato, non un capriccio: col criterio generale, **26 note che nominano un punto critico
  senza citare il manuale HACCP uscivano dal perimetro** perche' citavano UN'ALTRA fonte
  prescrittiva - l'elenco delle attrezzature, la checklist del metal detector, il piano di
  manutenzione. Ma il limite critico di un CCP lo prescrive **il manuale**, non il registro
  degli strumenti: `fatto-strumenti-cf-02-e-ccp4` nomina il CCP4 e cita i due registri della
  metrologia, e nessuno dei due dice quale sia il limite critico di quel punto. Lasciarle
  fuori avrebbe fatto mancare a R1 **esattamente le note che lo hanno generato**. Il criterio
  vero e': una nota deve avere sotto mano la fonte che prescrive **cio' di cui parla**, non
  una fonte prescrittiva qualsiasi.

Se valgono entrambe, la nota discute una cosa prescritta senza avere sotto mano il
documento che la prescrive: e' esattamente la classe di difetto che il gate del lotto 1C ha
scoperto, dove in QUATTRO casi su undici la nota **dichiarava mancante** cio' che il manuale
HACCP contiene per esteso.

⚠️ **Il criterio e' deliberatamente LARGO sulla condizione 1.** Il costo di guardare una
nota che non ne aveva bisogno e' un minuto, e si chiude dichiarando che la fonte non serve -
che e' cio' che E29 prescrive di fare. Il costo di NON guardarne una che ne aveva bisogno e'
una nota che afferma il falso dentro la misura «dopo». ⚠️ Lo script **non giudica se la
verticale sia stata fatta BENE**: dice soltanto se la fonte che governa quella famiglia e'
fra le fonti. Il giudizio e' lavoro del lotto.

⚠️ **Il numero di partenza noto e' 30**, dal §11 del rapporto del lotto 1C: le note che
nominano un CCP senza citare il manuale HACCP. Lo script ne trova **40** per quella sola
famiglia, e **71** col criterio completo. **Vince lo script**, e la differenza si spiega nel
rapporto: la famiglia «punto critico» qui e' piu' larga di «nomina un CCP» - comprende anche
`limite critico`, `HACCP`, `prerequisito`, `PRP` - e le altre quattro famiglie non erano
state contate affatto al gate di 1C, dove si guardava il solo manuale.

Cosa resta fuori, e non e' una scelta di comodo: gli `_index` (apparato di navigazione), le
note-strumento del progetto (E20: documentano attrezzi, non fatti dell'azienda), le note di
diario e tutto cio' che sta in `workspace\\` e `sources\\` (metodo_03 §7.0).

=====================================================================================
LA MODALITA' RISTRETTA — E37, la riconciliazione verticale ARRETRATA
=====================================================================================
E37 (metodo_03 §9.5, passo 5-ter) chiede che questo script si rilanci **ristretto alle
fonti prescrittive che un lotto porta dentro il vault**, all'APERTURA di quel lotto: le
note che restituisce entrano nel suo `qa\\lotti\\<lotto>_note.txt` e quindi nel suo
perimetro di QA (E32).

⚠️ **Non basta cambiare l'insieme delle fonti: va cambiata anche la condizione 1**, o si
ricade nel difetto che E36 ha corretto. Una fonte prescrittiva governa un DOMINIO, e le
note da riaprire sono quelle che parlano di **quel** dominio senza avere sotto mano
**quella** fonte — non tutte le note che nominano un limite qualsiasi. Percio' un dominio
si dichiara in `DOMINI` con due cose insieme: le **fonti** che lo governano e le
**espressioni** che lo riconoscono. Un dominio senza espressioni proprie sarebbe il
criterio generico applicato a un elenco piu' corto, cioe' la forma sbagliata di E29.

⚠️ **Il default resta il lotto R1, invariato**: questa modalita' AGGIUNGE un aggancio, non
ne allenta nessuno (§4.9 del passaggio di consegne).

Uso:
    python candidate_r1.py                     # il perimetro del lotto R1 (default)
    python candidate_r1.py --stdout            # solo riepilogo, non scrive niente
    python candidate_r1.py --dominio cip --lotto lotto_02a_cip
                                               # E37: le note che il lotto 2A riapre
Esce 0 se l'elenco e' stato prodotto, 1 se e' vuoto (un perimetro vuoto e' un errore).
"""
import argparse, io, os, re, sys
from datetime import date

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(QUI, "qa"))
import qa_comune as Q
from elenco_fonti_prescrittive import FONTI

LOTTO = "r1_riconciliazione_verticale"
DIR_LOTTI = os.path.join(QUI, "qa", "lotti")
EL_GREZZI = os.path.join(DIR_LOTTI, LOTTO + ".txt")
EL_NOTE = os.path.join(DIR_LOTTI, LOTTO + "_note.txt")

PRESCRITTIVE = {nome for nome, _classe, _cosa in FONTI}
MANUALE_HACCP = "manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt"

# Quale fonte prescrittiva GOVERNA una famiglia. Dove la famiglia non compare qui, vale
# «una fonte prescrittiva qualsiasi», che e' il criterio dettato in apertura del lotto.
GOVERNA = {
    "punto critico": {MANUALE_HACCP},
}

# Le cinque famiglie della condizione 1. Ogni famiglia dichiara che cosa cerca, perche' il
# criterio va scritto nel rapporto e un'espressione regolare senza nome non e' un criterio.
FAMIGLIE = [
    ("punto critico", [
        r"\bCCP\s?-?\s?\d\b", r"\bCCP\b", r"punt[oi] critic", r"limit[ei] critic",
        r"\bHACCP\b", r"\bprerequisit", r"\bPRP\b",
    ]),
    ("taratura o convalida", [
        r"taratur", r"ritaratur", r"convalid", r"riferibilit", r"\bcertificat[oi] di taratura",
        r"\bmetrologi",
    ]),
    ("frequenza di verifica", [
        r"frequenz", r"periodicit", r"\bcadenz", r"ogni\s+\d+\s*(mesi|anni|ore|giorni)",
        r"semestral", r"trimestral", r"quadrimestral", r"annual[ei]\b", r"mensil",
        r"scadenz[ae]\b", r"\bscadut",
    ]),
    ("limite o soglia", [
        r"\blimit[ei]\b", r"\bsogli[ae]\b", r"\btett[oi]\b", r"\bmassim[oa]\b", r"\bminim[oa]\b",
        r"\bLIM\s*=", r"valore di allarme", r"\ballarm",
    ]),
    ("responsabilità di processo", [
        r"responsabil", r"chi risponde", r"\bincaricat", r"\bprepost", r"\bdeleg",
        r"a cura di\b", r"\besecutor", r"\bapprovaz",
    ]),
]
FAMIGLIE = [(nome, [re.compile(r, re.I) for r in rx]) for nome, rx in FAMIGLIE]

# --- E37: i DOMINI, per la modalita' ristretta -------------------------------------
# Un dominio dichiara INSIEME le fonti prescrittive che lo governano e le espressioni che
# lo riconoscono in una nota. Le due meta' non si separano: le fonti da sole darebbero il
# criterio generico su un elenco piu' corto, le espressioni da sole non direbbero quale
# fonte manca. Chi apre un lotto con fonti prescrittive nuove aggiunge qui il suo dominio,
# e il criterio finisce nel rapporto perche' e' scritto qui e non nella memoria di nessuno.
DOMINI = {
    # Lotto 2A. `IO-05` prescrive fasi, parametri, criteri di accettazione e registrazioni
    # del lavaggio CIP; la scheda di sicurezza prescrive le condizioni d'uso del detergente
    # acido — concentrazioni, temperature, DPI, incompatibilita'.
    "cip": {
        "fonti": {
            "IO-05_istruzione_operativa_lavaggio_CIP.docx",
            "scheda_sicurezza_detergente_acido_lavaggio_CIP.txt",
        },
        "espressioni": [
            r"\bCIP\b", r"\bCIP-?01\b", r"lavagg", r"sanific", r"detergent", r"risciacqu",
            r"conducibilit", r"\bsoda\b", r"caustic", r"acido nitric", r"\bPAA\b",
            r"peracetic", r"disinfez", r"pulizi", r"tampon[ei] superfic", r"\bigien",
        ],
        "cosa": "lavaggio CIP, sanificazione, conducibilita' e prodotti chimici di lavaggio",
    },
    # Lotto 2B. La scheda allergeni (PRPo1) prescrive matrice, sequenze di produzione,
    # tipi di lavaggio, validazione della pulizia, rework, etichettatura precauzionale e
    # segregazione a magazzino. E' la fonte che GOVERNA il rischio allergeni del sito.
    #
    # ⚠️ DUE FONTI, dal gate del 21/08/2026, e la seconda e' stata aggiunta per un numero.
    # Il lotto 2B-bis ha misurato un tasso di difetto di produzione del 9,1 %, e tutte e tre
    # le note scoperte erano del sotto-dominio della FORMAZIONE: parlano di allergeni ma
    # nascono dal materiale d'aula, non dalla scheda. Il criterio le contava scoperte perche'
    # il dominio dichiarava una fonte sola, e la misura sovrastimava.
    #
    # ⚠️ Il materiale di formazione E' governante su quel sotto-dominio: la scheda §9
    # prescrive la formazione ma non ne fissa il contenuto, e le regole che l'operatore
    # riceve — le cinque regole d'oro, i divieti, il test finale — stanno solo li'. Una nota
    # sulla formazione allergeni che cita il .pptx **non e' scoperta**: cita la fonte che
    # quel pezzo di dominio lo governa davvero.
    #
    # ⚠️ E QUESTO NON RISCRIVE LA SERIE. Il 9,1 % del lotto 2B-bis resta il numero misurato
    # con lo strumento di allora, e resta scritto cosi' (E46). Il prossimo lotto dichiara la
    # versione dello strumento che usa: due misure fatte con criteri diversi non stanno sulla
    # stessa curva.
    "allergeni": {
        "fonti": {
            "scheda_allergeni_matrice_cross_contamination.docx",
            "formazione_allergeni_operatori_2026.pptx",
        },
        "espressioni": [
            r"allergen", r"\bglutin", r"\bsesamo\b", r"frutta a guscio", r"\bsoia\b",
            r"contaminazione crociat", r"cross[- ]contamination", r"\brework\b",
            r"sequenza di produzione", r"puo' contenere", r"può contenere",
            r"etichettatura precauzional", r"\bPAL\b", r"\bPRPo1\b",
        ],
        "cosa": "allergeni, contaminazione crociata, sequenze di produzione, rework ed etichettatura precauzionale",
    },
    # Lotto 2B. Il piano di autocontrollo dell'acqua potabile prescrive punti di prelievo,
    # parametri, metodi e valori di parametro del D.Lgs. 18/2023: e' la fonte che governa
    # la qualita' dell'acqua usata in stabilimento, CIP e ghiaccio compresi.
    # Lotto 3C. ⚠️ **E' il primo dominio che nasce da una VERIFICA DA SCRIPT (E53) e non da
    # una dichiarazione**: `verifica_dominio.py --lotto lotto_03c_certificazione_audit` alle
    # 10:05:31 del 22/08/2026 ha trovato SETTE fonti prescrittive citate per sigla dentro i
    # grezzi del lotto, quattro delle quali citabili — `HACCP`, `IO-05`, `AF-SN-0450`, la
    # scheda del detergente. Un rapporto d'audit REGISTRA, ma cita clausole e criteri per
    # costruzione: il dominio c'era, ed era verificabile in apertura.
    #
    # ⚠️ LE DUE FONTI DEL DOMINIO PRESCRIVONO DAVVERO, e la prima ha costretto ad affinare una
    # regola dell'elenco. Il certificato **attesta** il grade — e per quella meta' non prescrive
    # nulla, perche' i requisiti dello standard nel corpus non ci sono — **ma le sue sei
    # CONDIZIONI DI VALIDITA' E USO DEL MARCHIO vincolano l'azienda**: dove il logo si puo'
    # usare, entro quanti giorni si comunica una modifica, che cosa fa decadere il titolo.
    # La conferma d'incarico prescrive gli obblighi verso l'ente per il rinnovo.
    #
    # ⚠️ Il dominio NON e' «gli audit»: e' **il rapporto con l'ente di certificazione** — che
    # cosa il titolo obbliga a fare, entro quando, e con quali conseguenze se si manca.
    "certificazione": {
        "fonti": {
            "Certificato_BRCGS_Food_Issue9_Aurora_2026.pdf",
            "Conferma_incarico_audit_rinnovo_2026.pdf",
        },
        # ⚠️ IL PRIMO TAGLIO DI QUESTE ESPRESSIONI ERA SBAGLIATO, e lo ha detto il numero:
        # 119 note riaperte su 288 valutate, cioe' **due note del vault su cinque**. Un debito
        # vero non ha quella forma. Dentro c'erano `certificat[oi]`, `non conformit`, `NC-\d`
        # e `scope`, che in un archivio di qualita' alimentare stanno **dappertutto** — e
        # «certificato» prende per primo il **certificato di TARATURA**, che appartiene a un
        # altro dominio e ha gia' la sua fonte.
        #
        # ⚠️ E' esattamente il difetto che E36 ha corretto, ricomparso dall'altra parte: **il
        # criterio generico applicato a un elenco piu' corto**. Un dominio si riconosce dalle
        # espressioni che nomina LUI e nessun altro. Qui: l'ente, gli schemi, il titolo e il
        # marchio — non la parola «certificato» e non la parola «non conformita'».
        "espressioni": [
            r"\bBRCGS?\b", r"\bIFS\b", r"\bCSQA\b", r"\bACCREDIA\b",
            r"\bBRC/IT/", r"\bIFS/IT/", r"\bIssue\s?9\b", r"\bIT BIO\b",
            r"\bgrade\s?A{1,2}\b", r"\bHigher Level\b",
            r"audit di (?:rinnovo|sorveglianza|certificazione)",
            r"organismo di certificaz", r"ente di certificaz", r"uso del marchio",
            r"certificazione (?:bio|biologica|di prodotto|di sistema)",
        ],
        "cosa": "il rapporto con l'ente di certificazione: titolo in vigore, scope, condizioni di validita' e uso del marchio, obblighi di comunicazione, chiusura delle non conformita' e programmazione degli audit",
    },
    # Lotto 3B. ⚠️ **E' IL PRIMO DOMINIO DICHIARATO SOTTO E56**: la coppia
    # espressioni-fonti si giustifica a vicenda, ed e' stata costruita chiedendosi, per ogni
    # espressione, QUALE fonte del dominio governi cio' che quell'espressione riconosce. Le
    # espressioni che non hanno passato quella prova sono elencate qui sotto col loro motivo,
    # perche' un dominio si legge anche da cio' che ha lasciato fuori.
    #
    # ⚠️ LE DUE FONTI GOVERNANO DAVVERO, e sono di due livelli diversi:
    #   - la SCHEDA ALLERGENI §9.1 prescrive l'obbligo e la sua periodicita' — «Tutto il
    #     personale di produzione, magazzino e manutenzione riceve formazione su allergeni al
    #     momento dell'assunzione e con richiamo annuale (registro MOD-HR-11)» — piu' i moduli
    #     per ruolo (§9.1) e la verifica di efficacia (§9.4);
    #   - il MANUALE HACCP prescrive il prerequisito che la contiene: «PRP-04 Igiene e
    #     formazione del personale (MOD-HR-11 registro formazione)», e al §9.2 «formazione
    #     specifica registrata su MOD-HR-11». E' la fonte che dice CHE la formazione e' un
    #     prerequisito del sistema, non solo una buona pratica.
    #
    # ⚠️ IL MATERIALE D'AULA e' la terza fonte, ed e' qui per la ragione che ha corretto il
    # 9,1 % di 2B-bis: la scheda prescrive CHE si formi, il .pptx e' cio' che l'operatore
    # riceve. Una nota sul contenuto della formazione che cita il materiale **non e' scoperta**.
    #
    # ⚠️ CHE COSA E' RIMASTO FUORI, e perche' — e' il verso «troppo largo» che 3C ha pagato:
    #   - la FORMAZIONE ANTINFORTUNISTICA (preposto, antincendio, primo soccorso, carrello
    #     elevatore, rischio alto 12h, RLS, dirigente): la governa il **DVR**, che e' fonte
    #     prescrittiva ma appartiene al lotto 8 e NON e' citabile. Le sue espressioni non
    #     entrano, o il tasso conterebbe scoperte note che una fonte non canonizzabile governa;
    #   - la VALIDITA' TRIENNALE dell'HACCP: il registro la attribuisce a una «procedura
    #     interna (3 anni)» che **nel corpus non c'e'**. Espressione senza fonte: fuori;
    #   - gli IMPEGNI E GLI OBIETTIVI DELLA POLITICA: nessuna fonte del corpus prescrive che
    #     cosa una politica per la qualita' debba contenere — lo fa il protocollo BRCGS, che il
    #     corpus non ha. Il certificato prescrive le condizioni di validita' e uso del marchio,
    #     **non il contenuto della politica**. Fuori: e' esattamente l'errore di 3C, dove le
    #     espressioni riconoscevano l'audit e le fonti governavano il titolo.
    "formazione": {
        "fonti": {
            "scheda_allergeni_matrice_cross_contamination.docx",
            "manuale_HACCP_Aurora_v4_2024_ESTRATTO_REALE.txt",
            "formazione_allergeni_operatori_2026.pptx",
        },
        # ⚠️ IL CONFINE DI PAROLA IN TESTA A `formazion` NON E' UN DETTAGLIO, ed e' costato
        # un giro: senza `\b` l'espressione pesca **`informazion`** — «un'informazione»,
        # «la stessa informazione» — e al primo taglio ha riaperto **cinque note** che di
        # formazione non parlano affatto (gli appunti in coda al file reflue, la carica in
        # salita, le quattro grafie del registro tamponi, la durezza in deroga, la SDS in
        # linea). E' il criterio generico di 3C in miniatura: **un dominio si riconosce dalle
        # espressioni che nomina LUI e nessun altro**.
        #
        # ⚠️ E' ANCHE IL SECONDO BUG DI CONFINE IN DUE GIORNI, nel verso opposto a quello di
        # `verifica_dominio.py`: la' un `\b` **in coda** alla sigla la faceva sparire in
        # silenzio, qui un `\b` **mancante in testa** faceva rumore. Uno strumento che
        # riconosce testo si sbaglia sui bordi, non sul centro.
        # ⚠️ SECONDO TAGLIO, e il primo era TROPPO LARGO: e' il verso di 3C, riprodotto dal
        # primo lotto che dichiara un dominio sotto E56. Col taglio di apertura il tasso di
        # difetto di produzione dava **63,6 % su 22 note**, il piu' alto della serie, e la prova
        # che il numero misurava la dichiarazione e non il metodo sta in una riga sola:
        # **`\bformazion` da sola pescava tutte e quattordici le scoperte.**
        #
        # ⚠️ LA PROVA E' PER ESPRESSIONE, non per numero, ed e' il test che E56 prescrive: per
        # ciascuna, quale fonte del dominio governa cio' che riconosce?
        #   - `\bformazion` riconosce **la parola**, e con essa la struttura del registro, chi lo
        #     estrae, la sua intestazione ripetuta e l'indicatore delle ore. **Nessuna fonte del
        #     dominio governa un file: governano l'OBBLIGO di formare e di registrare.** Fuori;
        #   - `HACCP (base|avanzato)` sono **nomi di corso del registro**, e la loro validita'
        #     viene dalla «procedura interna (3 anni)» che nel corpus non c'e'. Fuori;
        #   - `ore/addetto` e `ore per addetto` sono l'indicatore, e lo governa la tabella degli
        #     obiettivi della politica, che **non e' una fonte prescrittiva**. Fuori;
        #   - `scadenzario formazion` e' il nome del documento, non l'obbligo. Fuori.
        #
        # ⚠️ RESTANO le espressioni che nominano l'OBBLIGO e la sua registrazione, che e'
        # esattamente cio' che `PRP-04` e la scheda §9.1 prescrivono.
        "espressioni": [
            r"\bMOD-HR-11\b", r"\bPRP-04\b", r"richiamo annual",
            r"registro (?:della )?formazion", r"formazione (?:specifica|allergeni|obbligatoria|del personale)",
            r"sessione formativ", r"sessioni? di formazion", r"efficacia della formazion",
            r"\bneoassunt", r"nuovo assunto", r"nuovi assunti",
            r"\baddestrament", r"\baffiancament",
        ],
        "cosa": "la formazione del personale come PREREQUISITO del sistema HACCP: obbligo, periodicita', moduli per ruolo, registrazione su MOD-HR-11 e verifica di efficacia",
    },
    # Lotto 3D. ⚠️ **E' IL PRIMO DOMINIO DICHIARATO SOTTO E56 *E* COLLAUDATO SOTTO E59**, e
    # ha una particolarita' che va detta prima dei numeri: **la fonte del dominio la sta
    # portando questo lotto**, quindi al momento della dichiarazione **nessuna nota del vault
    # puo' citarla**. Il collaudo di E59 puo' percio' dire solo quanto un'espressione pesca
    # FUORI, non quanto pesca dentro: meta' della prova resta scoperta, e il rapporto lo
    # dichiara invece di darlo per fatto (§4.42).
    #
    # ⚠️ **LA FONTE E' UNA SOLA, ED E' UNA SCELTA, non una mancanza.** `PRO-QA-08` governa il
    # ciclo del reclamo dall'inizio alla fine: ricezione e protocollo (par. 6.1), classi e
    # tempi (par. 5 e 6.3), verifiche immediate sul lotto (6.2), indagine della causa radice
    # (7.1), campione reso (7.3), comunicazione al cliente e al consumatore (8), azioni
    # correttive (9), indicatori (10), archiviazione (11).
    #
    # ⚠️ **CIO' CHE E' STATO LASCIATO FUORI, e il motivo, perche' un dominio si legge anche da
    # quello — ed e' qui che 3C ha sbagliato**, mettendo le espressioni su una cosa e le fonti
    # su un'altra:
    #   - `ritiro` e `richiamo`: li governa **`PRO-QA-11`**, che e' del lotto 3E e non e'
    #     canonizzata. `PRO-QA-08` la **richiama**, non la contiene: par. 6.2.5 dice «convoca
    #     il team HACCP per la valutazione di attivazione della PRO-QA-11». Un'espressione sul
    #     ritiro pescherebbe note che un'altra fonte governa;
    #   - `azione correttiva`: la governa **`PRO-QA-05`**, che nel corpus non c'e'. `PRO-QA-08`
    #     par. 9 prescrive che l'azione si apra, non come si gestisce;
    #   - `non conformita'` e `NC-\d`: sono di tutto l'archivio, e la NC 1 dell'audit e'
    #     governata dal rapporto d'audit. E' la parola che al primo taglio di 3C riapriva due
    #     note del vault su cinque;
    #   - `campione` e `controcampione`: la campioteca la prescrive **anche** il manuale HACCP.
    #     Resta fuori `campione` da solo; entra `campione reso`, che e' la locuzione con cui
    #     `PRO-QA-08` par. 7.3 nomina l'oggetto che LUI governa;
    #   - `metal detector`, `CCP3`: `PRO-QA-08` par. 6.2.2 dice di **riesaminare** quelle
    #     registrazioni durante l'indagine; a prescriverle e' il manuale HACCP.
    "reclami": {
        "fonti": {
            "PRO-QA-08_gestione_reclami_cliente_rev2.docx",
        },
        "espressioni": [
            r"\breclam",                       # reclamo, reclami, reclamante: il nome dell'oggetto
            r"\bREC-20\d\d-\d{3}\b",           # il protocollo che par. 6.1.1 istituisce
            r"\bMOD-QA-31\b",                  # il modulo che par. 6.1.2 istituisce
            r"\bPRO-QA-08\b",
            r"corpo estrane",                  # l'esempio di classe 1 di par. 5, e il caso del lotto
            r"causa radice",                   # par. 7.1, il metodo obbligatorio per classi 1 e 2
            r"campione reso",                  # par. 7.3, l'oggetto che questa procedura governa
            r"blocco cautelativ",              # par. 6.2.3
            r"consumatore final",              # par. 8.2, la meta' di cui questa procedura e' padrona
        ],
        "cosa": "il ciclo del reclamo di cliente e consumatore: ricezione e protocollo, classificazione e tempi, verifiche immediate sul lotto, indagine della causa radice, campione reso, comunicazione, azioni correttive e indicatori",
    },
    "acqua": {
        "fonti": {
            "piano_autocontrollo_acqua_potabile_analisi.csv",
        },
        "espressioni": [
            r"acqua potabil", r"acqua di rete", r"potabilit", r"addolcitor",
            r"cloro residu", r"\bghiaccio\b", r"coliform", r"E\.\s?coli",
            r"enterococch", r"durezza total", r"\bD\.Lgs\.?\s*18/2023\b",
        ],
        "cosa": "acqua potabile, punti di prelievo, parametri di potabilita' e acqua di processo",
    },
}
for _d in DOMINI.values():
    _d["rx"] = [re.compile(r, re.I) for r in _d["espressioni"]]


def testo_della_nota(n):
    """title + summary + corpo senza il blocco Fonti: si cerca cio' che la nota AFFERMA,
    non i nomi dei file che cita - altrimenti «taratura» nel nome di un grezzo basterebbe."""
    fm = n.fm or {}
    return "\n".join([str(fm.get("title") or ""), str(fm.get("summary") or ""),
                      n.corpo_senza_fonti or ""])


def famiglie_toccate(testo):
    return [nome for nome, rx in FAMIGLIE if any(r.search(testo) for r in rx)]


def main():
    ap = argparse.ArgumentParser(description="Genera il perimetro di note di una riconciliazione verticale.")
    ap.add_argument("--stdout", action="store_true")
    ap.add_argument("--dominio", choices=sorted(DOMINI),
                    help="E37: restringe a un dominio prescrittivo (vedi DOMINI)")
    ap.add_argument("--lotto", help="slug del lotto: scrive qa\\lotti\\<slug>_note.txt")
    args = ap.parse_args()

    dom = DOMINI[args.dominio] if args.dominio else None
    lotto = args.lotto or LOTTO
    el_grezzi = os.path.join(DIR_LOTTI, lotto + ".txt")
    el_note = os.path.join(DIR_LOTTI, lotto + "_note.txt")

    note = Q.tutte_le_note()
    candidate, gia_coperte, fuori_classe = [], [], 0

    for n in note:
        if n.cartella in Q.ESCLUSE_QUALITA or n.type in ("index", "sessione", "daily") \
                or n.fm is None or Q.e_nota_strumento(n):
            fuori_classe += 1
            continue
        testo = testo_della_nota(n)
        fonti = {str(f) for f in n.fonti}
        if dom:
            # E37 + E36: la nota parla del DOMINIO, e non ha sotto mano la fonte che
            # quel dominio lo governa. Le due condizioni valgono insieme, come sempre.
            if not any(r.search(testo) for r in dom["rx"]):
                continue
            fam = [args.dominio]
            scoperte = fam if not (fonti & dom["fonti"]) else []
            coperta_da = sorted(fonti & dom["fonti"])
        else:
            fam = famiglie_toccate(testo)
            if not fam:
                continue
            # una famiglia e' SCOPERTA se la nota non cita nessuna delle fonti che la governano
            scoperte = [f for f in fam if not (fonti & GOVERNA.get(f, PRESCRITTIVE))]
            coperta_da = sorted(fonti & PRESCRITTIVE)
        if scoperte:
            candidate.append((n, scoperte))
        else:
            gia_coperte.append((n, fam, coperta_da))

    candidate.sort(key=lambda c: (c[0].cartella, c[0].slug))

    # ---- il riepilogo, che e' cio' che va nel rapporto -------------------------
    print("=" * 78)
    if dom:
        print("PERIMETRO RIAPERTO DAL LOTTO %s — riconciliazione verticale arretrata (E37)"
              % lotto)
        print("dominio «%s»: %s" % (args.dominio, dom["cosa"]))
        print("fonti che lo governano: %s" % ", ".join(sorted(dom["fonti"])))
    else:
        print("PERIMETRO DEL LOTTO R1 — riconciliazione verticale")
    print("generato da candidate_r1.py il %s" % date.today().isoformat())
    print("=" * 78)
    print("Note del vault ................................ %d" % len(note))
    print("  escluse per classe (_index, strumento, diario,")
    print("  workspace\\, sources\\) ....................... %d" % fuori_classe)
    print("  valutate ..................................... %d" % (len(note) - fuori_classe))
    print("")
    print("Nominano qualcosa che una fonte prescrittiva governa:")
    # ⚠️ L'etichetta cambia col MODO, perche' l'insieme cambia: in modalita' ristretta
    # (E37) «coperta» significa che la nota cita una fonte DEL DOMINIO, non una fonte
    # prescrittiva qualsiasi. Dirlo con la stessa parola nei due casi farebbe leggere il
    # numero come non e' - ed e' la specie che il censimento del gate 3B ha censito: una
    # dichiarazione che promette piu' di quanto misura (§4.49).
    if dom:
        print("  e CITANO gia' una fonte DEL DOMINIO ........... %d  (fuori perimetro)" % len(gia_coperte))
    else:
        print("  e CITANO gia' una fonte prescrittiva ......... %d  (fuori perimetro)" % len(gia_coperte))
    print("  e NON ne citano nessuna ...................... %d  <-- IL PERIMETRO" % len(candidate))
    print("")
    conta_fam = {}
    for _n, fam in candidate:
        for f in fam:
            conta_fam[f] = conta_fam.get(f, 0) + 1
    print("| Famiglia nominata | Note candidate |")
    print("|---|---|")
    nomi = [args.dominio] if dom else [nome for nome, _rx in FAMIGLIE]
    for nome in nomi:
        print("| %s | %d |" % (nome, conta_fam.get(nome, 0)))
    print("")
    per_cartella = {}
    for n, _f in candidate:
        per_cartella[n.cartella] = per_cartella.get(n.cartella, 0) + 1
    print("| Cartella | Note candidate |")
    print("|---|---|")
    for c in sorted(per_cartella):
        print("| `%s\\` | %d |" % (c, per_cartella[c]))
    print("")
    print("Le note gia' coperte, e da quale fonte prescrittiva:")
    for n, _fam, pres in sorted(gia_coperte, key=lambda g: g[0].slug):
        print("  %-58s %s" % (n.slug, ", ".join(pres)))

    if args.stdout:
        return 0 if candidate else 1

    if not candidate:
        print("\nERRORE: perimetro vuoto. Un elenco di note vuoto non e' un lotto di")
        print("manutenzione: e' un errore, e la guardia di E35 lo rifiuta.")
        return 1

    os.makedirs(DIR_LOTTI, exist_ok=True)

    coda_e32 = ("# --- da qui in giu': note toccate in corso di lotto (E32) ---\n"
                "# Preesistenti, che il lotto modifica senza citarne i grezzi.\n"
                "# --- da qui in giu': note NATE in questo lotto ---\n"
                "# Si dichiarano QUANDO SI CREANO, non si deducono a fine lotto: e'\n"
                "# la stessa disciplina di E32 applicata alle note nuove, e serve a\n"
                "# conta_perimetro_lotto.py, che i numeri del perimetro li legge da qui.\n")

    if dom:
        # E37, modalita' ristretta: il lotto canonizza grezzi SUOI, quindi l'elenco dei
        # grezzi e' del lotto e questo script non lo tocca. Si scrive solo l'elenco
        # delle note che la fonte prescrittiva nuova RIAPRE.
        with io.open(el_note, "w", encoding="utf-8", newline="\n") as f:
            f.write("# Note RIAPERTE dal lotto %s — riconciliazione verticale ARRETRATA (E37).\n"
                    % lotto)
            f.write("# GENERATO da 06_operativo\\candidate_r1.py --dominio %s il %s.\n"
                    % (args.dominio, date.today().isoformat()))
            f.write("# Criterio: la nota parla di %s,\n" % dom["cosa"])
            f.write("# e fra le sue fonti non c'e' nessuna delle fonti che governano quel\n")
            f.write("# dominio: %s.\n" % ", ".join(sorted(dom["fonti"])))
            f.write("# Non si edita a mano: si rilancia lo script.\n")
            for n, _fam in candidate:
                f.write("%s\n" % n.slug)
            f.write(coda_e32)
        print("\nscritto:\n  %s" % el_note)
        print("\nNote riaperte per riconciliazione verticale: %d." % len(candidate))
        return 0

    with io.open(el_grezzi, "w", encoding="utf-8", newline="\n") as f:
        f.write("# MANUTENZIONE\n")
        f.write("# Lotto R1 - riconciliazione verticale. Nessun grezzo nuovo si canonizza qui:\n")
        f.write("# si riparano note gia' scritte (E35, metodo_03 §9.4-bis). Il perimetro vero\n")
        f.write("# e' l'elenco delle note qui accanto, %s.\n" % os.path.basename(el_note))
    with io.open(el_note, "w", encoding="utf-8", newline="\n") as f:
        f.write("# Perimetro del lotto R1, GENERATO da 06_operativo\\candidate_r1.py il %s.\n"
                % date.today().isoformat())
        f.write("# Criterio: la nota nomina un punto critico, una taratura, una frequenza di\n")
        f.write("# verifica, un limite o una responsabilita' di processo, e fra le sue fonti\n")
        f.write("# non c'e' nessuna fonte prescrittiva (elenco di E29). Non si edita a mano:\n")
        f.write("# si rilancia lo script. Le note che il lotto TOCCA in piu' si aggiungono\n")
        f.write("# mentre le si tocca (E32), sotto la riga di separazione.\n")
        for n, fam in candidate:
            f.write("%s\n" % n.slug)
        f.write(coda_e32)
    print("\nscritti:\n  %s\n  %s" % (el_grezzi, el_note))
    print("\nPerimetro: 0 grezzi, %d note." % len(candidate))
    return 0


if __name__ == "__main__":
    sys.exit(main())
