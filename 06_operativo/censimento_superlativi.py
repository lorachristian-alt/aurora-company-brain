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


# --- le due famiglie di espressioni, e dove vivono ora -------------------------------
#
# ⚠️ LE ESPRESSIONI E IL RICONOSCITORE NON STANNO PIU' QUI: stanno in `qa\qa_comune.py`, che
# e' il comune della suite. Ci sono stati spostati al gate del lotto 3D (24/08/2026), quando
# il controllo di E43 ha acquistato lo stesso riconoscitore: da quel giorno i chiamanti sono
# due — questo censimento, che produce il NUMERO di T142, e `qa_frontmatter`, che ne fa il
# CONTROLLO — e una classe con due padroni e' una classe che diverge.
#
# ⚠️ Lo spostamento e' stato TAGLIA-E-INCOLLA, non una riscrittura, e la prova e' un
# censimento eseguito prima e dopo sullo stesso vault: stessi numeri, stesse note, stesse
# frasi. Qui restano i soli nomi locali, che sono alias e non copie.
occorrenze = Q.occorrenze_di_perimetro
frasi_della_nota = Q.frasi_di_perimetro
FINESTRA = Q.FINESTRA_PERIMETRO

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
