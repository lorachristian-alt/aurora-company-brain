# -*- coding: utf-8 -*-
r"""censimento_superlativi — quante note del vault portano un superlativo SULL'ARCHIVIO (E57).

=====================================================================================
PERCHE' QUESTO SCRIPT ESISTE
=====================================================================================
E57 dice che il discrimine di un superlativo o di un'esclusiva e' il SOGGETTO: con
soggetto-documento si verifica sulla fonte e regge, con soggetto-ARCHIVIO non e'
verificabile da nessuna nota, perche' **nessuna nota ha l'archivio fra le proprie fonti**.

⚠️ **La classe non e' nata nel lotto 3C: ci e' stata solo trovata.** Uno dei quattro casi del
terzo giro era `fatto-obblighi-registro-f-gas`, del lotto **1B**. Il gate ha quindi chiesto un
numero, non una riparazione: **quante note del vault portano oggi questa forma**, perche' senza
il numero nessuno sa se le occorrenze siano quattro o quaranta, e la decisione su quando
ripararle sarebbe a sentimento — lo stesso ragionamento con cui `censimento_formule.py` ha dato
il suo numero a T89.

⚠️ **QUESTO SCRIPT NON RIPARA NIENTE, e non deve.** Le occorrenze si riparano **nel lotto che
le tocca** o nella rete finale di fine corsa: aprire un giro sul vault per una classe di
scrittura e' il calcolo lineare del lotto 1C in un'altra forma. Qui si produce **il numero e
l'elenco**, che vanno nella riga **T142** della tabella di tracciamento.

=====================================================================================
CHE COSA CONTA, E CON QUALE DEFINIZIONE
=====================================================================================
Una nota entra nel censimento se **nella stessa frase** compaiono due cose:

1. un QUANTIFICATORE della famiglia di E47 — «l'unico», «il solo», «il primo», «il piu' ...»,
   «nessun altro», «l'unica traccia», «esclusiva», e le negazioni equivalenti;
2. un TERMINE DI PERIMETRO che nomina l'archivio invece di un documento — «archivio», «vault»,
   «corpus», «tutto il resto», «tutte le note», «nessun altro documento», «da nessuna parte».

⚠️ **La frase e' l'unita', ma la FINESTRA e' stretta: sessanta caratteri intorno al termine di
perimetro.** Con la frase intera la classificazione dipendeva dall'ORDINE delle parole, ed e' un
difetto che il primo giro ha davvero prodotto: nel summary di
`kpi-temperatura-uscita-tunnel-ts-01-aprile` un «nessuna lettura sopra -18,0» che dell'archivio
non parla catturava la classe, e «e' l'unica registrazione continua di quel valore
nell'archivio» — che e' esattamente la classe di E57 — finiva contata come assenza. **Il
quantificatore che conta e' quello che governa il termine di perimetro**, cioe' quello che gli
sta vicino. Sessanta caratteri e' la stessa misura di E23.

⚠️ **Il blocco `## Fonti` resta fuori** dal testo esaminato: e' apparato di citazione, e una
citazione testuale che contenga un superlativo e' della FONTE, non della nota. Restano dentro
`title` e `summary`, che E30 impone di leggere come note a se'.

=====================================================================================
LE DUE CLASSI, E PERCHE' NON SI SOMMANO
=====================================================================================
⚠️ **Il primo censimento dava 42 note e 47 occorrenze, e quel numero mescolava DUE REGIMI
DIVERSI.** Pubblicarlo cosi' avrebbe ripetuto in piccolo l'errore del 38,7 % del lotto 3C: un
numero vero, con un nome che promette piu' di quanto misura. Le occorrenze si dividono in due, e
**le due meta' non si sommano mai**:

| Classe | La forma | Chi la governa |
|---|---|---|
| **`superlativo`** | affermativo: «e' l'unico X dell'archivio», «e' la prima evidenza in archivio» | **E57** — nessuna nota ha l'archivio fra le fonti, e **nessuna procedura la verifica**: si restringe al perimetro citato, o va in tabella di tracciamento |
| **`assenza`** | esistenziale NEGATIVO: «nessun documento dell'archivio riporta X» | **E3 ed E43** — l'assenza si dichiara solo dopo la ricerca su tutto `sources\`, e la ricerca lascia il suo artefatto datato. **E' verificabile**, e la sua verifica ha gia' una procedura |

⚠️ **La differenza non e' grammaticale, e' di VERIFICABILITA'.** Un'assenza si prova cercando, e
chi cerca lascia l'artefatto; un primato si proverebbe solo leggendo tutto l'archivio e
confrontandolo, che e' cio' che nessuna nota fa. **Solo la prima classe e' la classe di E57**, ed
e' quella che T142 conta.

=====================================================================================
CHE COSA QUESTO SCRIPT NON PUO' FARE
=====================================================================================
⚠️ **E' un CENSIMENTO, non un verdetto**, e la differenza va detta perche' il numero non venga
letto per quello che non e'. Lo script riconosce una FORMA; il soggetto lo decide chi legge.
Restano fuori portata, in entrambi i versi:

- **falsi positivi**: «il registro non compare in nessun altro documento **di questo lotto**»
  porta entrambe le famiglie, ma il perimetro e' dichiarato — regge, e `RE_RESTRIZIONE` lo toglie
  quando la restrizione e' testuale;
- **falso positivo di OMONIMIA**: nel corpus «archivio» nomina anche **l'archivio CARTACEO di
  Aurora**, che e' un oggetto fisico dell'azienda e non il vault. Il caso esiste ed e'
  `fatto-digitalizzazione-archivio-rinviata` — «l'unica azione non attuata del riesame 2025» non
  parla del vault per niente. ⚠️ **Oggi lo esclude la FINESTRA**, perche' nel testo attuale il
  quantificatore sta oltre i sessanta caratteri, e per questo il contatore delle omonimie
  stampa zero: `RE_ARCHIVIO_FISICO` e' la guardia che serve **se quel testo cambia**;
- **falsi negativi**: «e' la sola traccia che ne resti» non nomina l'archivio ma lo sottintende,
  e nessuna regex lo vede.

**Il numero e' quindi un LIMITE INFERIORE della classe, e va dichiarato cosi'.**

Uso:
    python censimento_superlativi.py               # il numero e l'elenco delle note
    python censimento_superlativi.py --frasi       # anche la frase, per ciascuna occorrenza
    python censimento_superlativi.py --vault <dir>
"""
import argparse
import io
import os
import re
import sys
from datetime import datetime

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(QUI, "qa"))
import qa_comune as Q  # noqa: E402


# --- le due famiglie di espressioni ------------------------------------------------
#
# 1. Il QUANTIFICATORE. E' la famiglia di E47, scritta come la porta il manuale: unicita',
#    primato, massimo, e le negazioni che dicono la stessa cosa al rovescio.
RE_QUANTIFICATORE = re.compile(
    r"\b(?:"
    r"l['’]unic[oa]|un['’]unic[oa]|unic[oa]\b|"
    r"il\s+sol[oa]\b|la\s+sol[ao]\b|l['’]sol[oa]\b|\bsoltanto\b|"
    r"nessun['’]?\s*altr[oa]\b|nessun\s+documento\b|nessuna\s+nota\b|"
    r"nessun\s+altro\b|nessuna\s+altra\b|"
    r"il\s+primo\b|la\s+prima\b|il\s+solo\s+caso\b|"
    r"il\s+più\s+\w+|la\s+più\s+\w+|"
    r"esclusiv[ao]\b|in\s+esclusiva\b|"
    r"non\s+compare\s+altrove\b|non\s+esiste\s+altrove\b"
    r")",
    re.I)

# 2. Il TERMINE DI PERIMETRO che nomina l'ARCHIVIO invece di un documento. E' questa meta'
#    che rende l'affermazione non verificabile: parla di cio' che sta ALTROVE.
RE_PERIMETRO = re.compile(
    r"\b(?:"
    r"archivio|vault|corpus|"
    r"tutto\s+il\s+resto|tutti\s+gli\s+altri\s+documenti|tutte\s+le\s+note|"
    r"nessun\s+altro\s+documento|nessun\s+altro\s+file|"
    r"da\s+nessuna\s+parte|in\s+nessun\s+altro\s+punto|"
    r"l['’]intero\s+archivio|dell['’]archivio|nell['’]archivio|in\s+archivio"
    r")\b",
    re.I)

# Un termine di perimetro seguito da una RESTRIZIONE esplicita non e' un'affermazione
# sull'archivio: «in nessun altro documento DI QUESTO LOTTO» ha il suo perimetro dichiarato.
# Non e' un filtro sul verdetto — che resta di chi legge — ma toglie dall'elenco i casi in cui
# la restrizione e' testuale e visibile.
RE_RESTRIZIONE = re.compile(
    r"\b(?:di\s+questo\s+lotto|di\s+questa\s+nota|fra\s+le\s+fonti|"
    r"di\s+questo\s+registro|di\s+questo\s+file|di\s+questo\s+documento|"
    r"del\s+pacchetto|citat[oi]\s+qui)\b", re.I)

# «Archivio» nel corpus e' anche l'ARCHIVIO CARTACEO di Aurora: un oggetto fisico
# dell'azienda, che col vault non c'entra. E' un'OMONIMIA, non un'occorrenza, e va tolta dal
# conteggio dichiarando quante se ne tolgono.
RE_ARCHIVIO_FISICO = re.compile(
    r"archivi(?:o|azione)\s+(?:cartace|fisic|informatic|digital)|"
    r"digitalizzazione\s+dell['’]archivio", re.I)

# L'esistenziale NEGATIVO: «nessun documento dell'archivio riporta X». E' un'ASSENZA
# DICHIARATA, e la governano E3 ed E43 — ricerca su tutto `sources\` piu' artefatto datato.
# NON e' la classe di E57, che e' l'affermazione POSITIVA di un primato.
RE_ESISTENZIALE_NEGATIVO = re.compile(
    r"\b(?:nessun[a'’]?\s*(?:altr[oa]\s+)?(?:documento|nota|file|riga|fonte|traccia|"
    r"riscontro|punto|parte|lettura|valore)|non\s+compare|non\s+esiste|non\s+risulta|"
    r"non\s+ha\s+nessun|non\s+lo\s+dice|non\s+la\s+porta|non\s+lo\s+riporta)", re.I)

# La finestra, in caratteri, dentro cui un quantificatore si considera riferito al termine di
# perimetro. Sessanta e' la stessa misura che E23 usa per il marcatore di un valore derivato:
# la distanza entro cui due parole della stessa frase si governano davvero.
FINESTRA = 60

# Il frontmatter, ridotto ai due campi che E30 impone di leggere come note a se'.
RE_TITLE = re.compile(r'^title:\s*"?(.*?)"?\s*$', re.M)
RE_SUMMARY = re.compile(r'^summary:\s*"?(.*?)"?\s*$', re.M)

# Il taglio in frasi: punto fermo, punto e virgola, due punti, capoverso, cella di tabella.
RE_FRASE = re.compile(r"(?:[.;:!?]\s+|\n+|\s\|\s)")


def frasi_della_nota(nota):
    """Le frasi da esaminare: title, summary e il corpo SENZA il blocco «## Fonti».

    ⚠️ Il blocco delle fonti resta fuori: e' apparato di citazione, e un superlativo dentro
    una citazione testuale appartiene alla FONTE, non a chi scrive la nota.
    """
    pezzi = []
    m = RE_TITLE.search(nota.grezzo)
    if m:
        pezzi.append(("title", m.group(1)))
    m = RE_SUMMARY.search(nota.grezzo)
    if m:
        pezzi.append(("summary", m.group(1)))
    for riga in RE_FRASE.split(nota.corpo_senza_fonti):
        r = riga.strip()
        if r:
            pezzi.append(("corpo", r))
    return pezzi


def occorrenze(nota):
    """Le frasi in cui un quantificatore e un termine di perimetro stanno INSIEME.

    Restituisce due liste, che NON si sommano: le occorrenze di classe `superlativo`
    (E57) e quelle di classe `assenza` (E3/E43). Piu' il conteggio delle omonimie
    scartate, perche' un filtro che toglie in silenzio e' uno script che tace.
    """
    superlativi, assenze, omonimie = [], [], 0
    for dove, frase in frasi_della_nota(nota):
        if RE_RESTRIZIONE.search(frase):
            continue
        for p in RE_PERIMETRO.finditer(frase):
            # ⚠️ LA FINESTRA E' STRETTA, E NON E' UN DETTAGLIO DI IMPLEMENTAZIONE. Con la
            # frase intera la classificazione dipendeva dall'ORDINE delle parole: nel summary
            # di `kpi-temperatura-uscita-tunnel-ts-01-aprile` un «nessuna lettura sopra
            # -18,0» che non parla dell'archivio catturava la classe, e «e' l'unica
            # registrazione continua di quel valore nell'archivio» — che e' esattamente la
            # classe di E57 — finiva contata come assenza. Il quantificatore che conta e'
            # quello che governa IL TERMINE DI PERIMETRO, cioe' quello che gli sta vicino.
            a, b = max(0, p.start() - FINESTRA), min(len(frase), p.end() + FINESTRA)
            intorno = frase[a:b]
            q = RE_QUANTIFICATORE.search(intorno)
            if not q:
                continue
            if RE_ARCHIVIO_FISICO.search(intorno):
                omonimie += 1
                continue
            voce = (dove, q.group(0), p.group(0), " ".join(frase.split()))
            if RE_ESISTENZIALE_NEGATIVO.search(intorno):
                assenze.append(voce)
            else:
                superlativi.append(voce)
            break        # una frase conta una volta sola: e' un'affermazione, non due
    return superlativi, assenze, omonimie


def main():
    ap = argparse.ArgumentParser(
        description="Censimento delle note che portano un superlativo sull'ARCHIVIO (E57).")
    ap.add_argument("--frasi", action="store_true",
                    help="stampa anche la frase di ogni occorrenza")
    ap.add_argument("--vault", default=Q.VAULT)
    args = ap.parse_args()

    note = Q.tutte_le_note(args.vault)
    # Fuori dal censimento, e per tre ragioni diverse:
    #  - gli `_index` sono apparato di navigazione, non affermano fatti;
    #  - le note-strumento di `code\` sono esenti dallo strato di giudizio (E20): parlano
    #    degli strumenti del progetto, e un «l'unico script che...» non e' questa classe;
    #  - `workspace\` sono le note di diario, che la QA gia' esclude dai conteggi di qualita':
    #    raccontano la sessione, non l'azienda.
    esaminate = [n for n in note
                 if n.type != "index" and n.cartella not in ("code", "workspace", "sources")]

    sup_note, ass_note, omonimie = [], [], 0
    n_sup = n_ass = 0
    for n in esaminate:
        s, a, o = occorrenze(n)
        omonimie += o
        if s:
            sup_note.append((n, s))
            n_sup += len(s)
        if a:
            ass_note.append((n, a))
            n_ass += len(a)

    ora = datetime.now().strftime("%H:%M:%S del %d/%m/%Y")
    print("censimento_superlativi (E57) - misura delle %s" % ora)
    print("vault: %s" % args.vault)
    print("note nel vault: %d - esaminate: %d (esclusi `_index`, `code\\`, `workspace\\`, `sources\\`)"
          % (len(note), len(esaminate)))
    print("")
    print("=" * 70)
    print("CLASSE `superlativo` - LA CLASSE DI E57, quella che T142 conta")
    print("  affermazione POSITIVA di un primato sull'archivio: nessuna procedura la verifica")
    print("=" * 70)
    print("  note: %d   occorrenze: %d" % (len(sup_note), n_sup))
    print("")
    if sup_note:
        print("| # | Nota | Cartella | Occ. | Dove |")
        print("|---|---|---|---|---|")
        for i, (n, occ) in enumerate(sorted(sup_note, key=lambda x: x[0].slug), 1):
            dove = ", ".join(sorted(set(d for d, _, _, _ in occ)))
            print("| %d | `%s` | `%s\\` | %d | %s |" % (i, n.slug, n.cartella, len(occ), dove))
    else:
        print("(nessuna)")

    print("")
    print("=" * 70)
    print("CLASSE `assenza` - NON E' la classe di E57: la governano E3 ed E43")
    print("  esistenziale NEGATIVO: e' verificabile, e la sua verifica ha gia' una procedura")
    print("=" * 70)
    print("  note: %d   occorrenze: %d" % (len(ass_note), n_ass))
    print("")
    if ass_note:
        print("| # | Nota | Cartella | Occ. |")
        print("|---|---|---|---|")
        for i, (n, occ) in enumerate(sorted(ass_note, key=lambda x: x[0].slug), 1):
            print("| %d | `%s` | `%s\\` | %d |" % (i, n.slug, n.cartella, len(occ)))
    else:
        print("(nessuna)")

    print("")
    print("Omonimie scartate (l'archivio CARTACEO di Aurora, non il vault): %d" % omonimie)

    if args.frasi:
        print("")
        print("=" * 70)
        print("LE FRASI, una per occorrenza")
        print("=" * 70)
        for etichetta, gruppo in (("superlativo", sup_note), ("assenza", ass_note)):
            print("\n### classe `%s`" % etichetta)
            for n, occ in sorted(gruppo, key=lambda x: x[0].slug):
                print("\n--- %s" % n.slug)
                for dove, q, p, frase in occ:
                    print("  [%s] quantificatore «%s» + perimetro «%s»" % (dove, q, p))
                    print("      %s" % (frase[:300] + ("..." if len(frase) > 300 else "")))

    print("")
    print("⚠️ Le due classi NON si sommano: `assenza` ha gia' il suo regime (E3/E43), solo")
    print("   `superlativo` e' scoperta ed e' la classe che E57 chiude.")
    print("⚠️ Questo e' un CENSIMENTO, non un verdetto: lo script riconosce una FORMA, il")
    print("   soggetto lo decide chi legge. Il numero e' un LIMITE INFERIORE della classe.")
    print("⚠️ Le occorrenze si riparano nel lotto che le tocca o nella rete finale, non qui.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
