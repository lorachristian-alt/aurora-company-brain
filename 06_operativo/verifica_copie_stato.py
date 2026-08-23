# -*- coding: utf-8 -*-
"""verifica_copie_stato — le copie che restano negli strumenti concordano col loro padrone.

⚠️ NASCE AL GATE DEL LOTTO 3B (23/08/2026), DAL CENSIMENTO DELLE COPIE DI STATO, ed e' la
risposta strutturale alla vigilanza aperta il giorno prima: *«quante altre copie di stato ci
sono dentro la suite?»* — §4.47, e §6 del passaggio di consegne.

Il censimento ha diviso le copie in DUE SPECIE, e solo la seconda arriva fin qui:

  1. **STATO DERIVABILE** — un elenco, un conteggio, un percorso il cui padrone e' un file
     che cambia da solo. Queste NON si controllano: si CANCELLANO, e lo strumento legge dal
     padrone. Il censimento ne ha convertite tre (`ricalibra_budget.py` ×2, il conteggio dei
     lotti chiusi in `verifica_matrice_lotti.py`), dopo le due riparate il 22-23/08
     (`verifica_dominio.py`, `qa_link_integrity.py`).

  2. **VOCABOLARI CHIUSI DEL MANUALE** — le aree, i prefissi, i `type`, le cartelle. Un
     validatore DEVE averli in memoria per validare, e farglieli leggere a runtime da un
     manuale in prosa significherebbe **mandare rossa tutta la suite** il giorno in cui
     qualcuno riformatta un titolo. ⚠️ **Ma una copia non controllata mente in silenzio**, ed
     e' precisamente cio' che §4.47 dice che succede sempre. Quindi la copia resta dove serve
     e QUESTO SCRIPT LA CONFRONTA COL PADRONE.

⚠️ **La differenza fra le due specie non e' comoda, e' sostanziale**: la prima e' uno stato
che il progetto PRODUCE mentre lavora e che nessuno decide; la seconda e' una DECISIONE
scritta in un manuale, che cambia solo quando qualcuno la cambia — e allora questo script
diventa rosso nello stesso turno.

I PADRONI, uno per vocabolario:
  - le **aree** ............ `metodo_03` §2.2, il blocco recintato dei dieci valori;
  - i **prefissi** ......... `metodo_03` §4.1, la tabella dei prefissi di dominio;
  - i **`type`** ........... `metodo_03` §2.4, l'intestazione della tabella dei campi;
  - le **cartelle** ........ `tassonomia_vault.md`, la tabella delle 11 cartelle.

Uso:
    python verifica_copie_stato.py
Esce 0 se ogni copia concorda col suo padrone, 1 altrimenti.
"""
import io
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
sys.path.insert(0, os.path.join(QUI, "qa"))
import qa_comune as Q   # noqa: E402

METODO = os.path.join(RADICE, "01_metodo", "metodo_03_canonizzazione.md")
TASSONOMIA = os.path.join(RADICE, "01_metodo", "tassonomia_vault.md")


def leggi(percorso):
    with io.open(percorso, encoding="utf-8") as f:
        return f.read()


def sezione(testo, titolo, livello=3):
    """Il corpo di una sezione, dal suo titolo al titolo successivo di pari livello o piu' alto."""
    marca = "#" * livello + " " + titolo
    i = testo.find(marca)
    if i < 0:
        return ""
    resto = testo[i + len(marca):]
    m = re.search(r"^#{1,%d}\s" % livello, resto, re.M)
    return resto[:m.start()] if m else resto


# ---------------------------------------------------------------- i quattro padroni

def aree_dal_manuale(manuale):
    """§2.2: il blocco recintato che elenca i valori, separati da `·` e a capo."""
    corpo = sezione(manuale, "2.2 Il vocabolario chiuso delle aree")
    m = re.search(r"```\s*\n(.*?)\n```", corpo, re.S)
    if not m:
        return set()
    return {v.strip() for v in re.split(r"[·\n]", m.group(1)) if v.strip()}


def prefissi_dal_manuale(manuale):
    """§4.1: la prima colonna della tabella dei prefissi, che porta i nomi fra apici inversi.

    La riga `bozza- · sessione- · diario-` ne porta tre in una cella sola, e l'`_index-` e'
    scritto come `_index-<cartella>`: si tiene il gambo fino al trattino finale."""
    corpo = sezione(manuale, "4.1 I nomi dei file")
    fuori = set()
    for riga in corpo.split("\n"):
        if not riga.startswith("|") or riga.startswith("|---") or "| Prefisso |" in riga:
            continue
        prima = riga.strip().strip("|").split("|")[0]
        for t in re.findall(r"`([^`]+)`", prima):
            t = t.strip()
            t = re.sub(r"<[^>]+>$", "", t)
            if t.endswith("-"):
                fuori.add(t)
    return fuori


def type_dal_manuale(manuale):
    """§2.4: l'intestazione della tabella dei campi obbligatori porta gli otto `type`."""
    corpo = sezione(manuale, "2.4 Quali campi sono obbligatori, per `type`")
    for riga in corpo.split("\n"):
        if riga.startswith("| Campo |"):
            celle = [c.strip() for c in riga.strip().strip("|").split("|")][1:]
            return {c.strip("`") for c in celle if c}
    return set()


def cartelle_dalla_tassonomia(tassonomia):
    """La tabella delle 11 cartelle: prima colonna, nome fra apici inversi."""
    fuori = set()
    for riga in tassonomia.split("\n"):
        if not riga.startswith("| `"):
            continue
        m = re.match(r"^\|\s*`([a-z_]+)`\s*\|", riga)
        if m:
            fuori.add(m.group(1))
    return fuori


# ---------------------------------------------------------------- le copie censite
#
# Ogni voce: (che cosa, la copia nello strumento, dove vive la copia, il padrone letto).
def censimento():
    manuale, tassonomia = leggi(METODO), leggi(TASSONOMIA)
    return [
        ("il vocabolario chiuso delle aree", set(Q.AREE),
         "qa_comune.AREE", aree_dal_manuale(manuale), "metodo_03 §2.2"),
        ("i prefissi dei nomi di file", set(Q.PREFISSI),
         "qa_comune.PREFISSI", prefissi_dal_manuale(manuale), "metodo_03 §4.1"),
        ("il vocabolario chiuso di `type`", set(Q.TYPE_AMMESSI),
         "qa_comune.TYPE_AMMESSI", type_dal_manuale(manuale), "metodo_03 §2.4"),
        ("le cartelle del vault", set(Q.CARTELLE),
         "qa_comune.CARTELLE", cartelle_dalla_tassonomia(tassonomia), "tassonomia_vault.md"),
    ]


def main():
    guasti = []
    print("=" * 84)
    print("LE COPIE CHE RESTANO NEGLI STRUMENTI, CONFRONTATE COL LORO PADRONE")
    print("=" * 84)
    print("| Che cosa | Copia | Padrone | Voci | Esito |")
    print("|---|---|---|---|---|")
    for cosa, copia, dove, padrone, chi in censimento():
        if not padrone:
            guasti.append("%s: il padrone (%s) non e' stato letto - la lettura si e' rotta, "
                          "e un confronto contro l'insieme vuoto assolverebbe sempre" % (dove, chi))
            esito = "PADRONE ILLEGGIBILE"
        elif copia == padrone:
            esito = "concordi"
        else:
            solo_copia = sorted(copia - padrone)
            solo_padrone = sorted(padrone - copia)
            guasti.append("%s diverge da %s: solo nella copia %s | solo nel padrone %s"
                          % (dove, chi, solo_copia or "-", solo_padrone or "-"))
            esito = "**DIVERGONO**"
        print("| %s | `%s` | %s | %d | %s |" % (cosa, dove, chi, len(padrone), esito))

    print("")
    print("Copie di stato DERIVABILE ancora in giro: nessuna nota al censimento del 23/08/2026.")
    print("Le due copie deliberate, che restano e non sono difetti:")
    print("  - `verifica_copia_sources.py`  l'assert su 160 voci del manifest e' un ALLARME,")
    print("    non una fonte: serve proprio a scattare se il manifest cambia;")
    print("  - `elenco_fonti_prescrittive.FONTI` e `candidate_r1.DOMINI` sono CURATELA")
    print("    dichiarata (E56), cioe' un giudizio scritto, non uno stato ricavabile.")

    if guasti:
        print("\nERRORI: %d" % len(guasti))
        for g in guasti:
            print("  - " + g)
        print("\nUna copia che diverge dal padrone mente in silenzio: si allinea la COPIA.")
        return 1
    print("\nOgni copia concorda col suo padrone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
