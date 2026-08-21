# -*- coding: utf-8 -*-
"""censimento_formule — quante formule dei fogli di calcolo l'estrattore congelato non vede.

=====================================================================================
PERCHE' QUESTO SCRIPT ESISTE
=====================================================================================
La nota `fatto-medie-non-calcolate-file-reflue` cita due formule `AVERAGE`, e lo strato di
giudizio le ha contestate **perche' nel testo estratto non ci sono**. Hanno ragione tutti e
due: le formule stanno nel file, l'estrattore congelato restituisce **i valori, non le
formule**.

⚠️ **Non e' un difetto di una nota: e' un punto cieco della catena di provenienza**, perche'
la QA e lo strato di giudizio girano entrambi su quel testo. Un fatto che vive in una formula
e' invisibile a tutti e due (riga **T89** della tabella di tracciamento).

⚠️ **Questo script NON ripara niente e non tocca l'estrattore**, che e' congelato
(metodo_01 §5-bis) e che e' il modulo di misura: cambiarlo invaliderebbe il confronto fra le
baseline. Serve a **dare a T89 un numero**, perche' oggi nessuno sa se il buco riguardi un
file o trenta — e senza numero la decisione al gate sarebbe a sentimento.

=====================================================================================
CHE COSA CONTA, E CON QUALE DEFINIZIONE
=====================================================================================
Per ogni `.xlsx` del manifest apre il file **come archivio** e legge i fogli in XML:

- **cella con formula**: porta un elemento `<f>`;
- **formula INVISIBILE all'estrattore**: la cella ha `<f>` e **non ha un valore in cache**
  (`<v>` assente o vuoto). L'estrattore restituisce la cache, quindi di quella cella non
  restituisce nulla — ne' il risultato ne' la formula;
- **formula visibile a meta'**: ha `<f>` e un `<v>` con un valore. L'estrattore restituisce il
  **risultato** ma non la formula: chi legge il testo estratto vede il numero e **non sa che e'
  calcolato**, ne' su quali celle.

⚠️ **La seconda categoria e' quella che conta per la soglia**, ma la terza non e' innocua: e'
il caso in cui un numero derivato sembra un dato di misura.

Uso:
    python censimento_formule.py            # tabella per il rapporto
    python censimento_formule.py --dettaglio  # anche cella per cella
"""
import argparse, io, os, re, sys, zipfile
from datetime import datetime

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(QUI, "qa"))
import qa_comune as Q

RE_FOGLIO = re.compile(r'name="([^"]+)"\s+sheetId="(\d+)"')
RE_CELLA = re.compile(r'<c r="([A-Z]+\d+)"[^>]*>(.*?)</c>', re.S)
RE_FORMULA = re.compile(r"<f[^>]*>(.*?)</f>", re.S)
RE_VALORE = re.compile(r"<v>(.*?)</v>", re.S)


def fogli(z):
    try:
        d = z.read("xl/workbook.xml").decode("utf-8", "replace")
    except KeyError:
        return []
    return RE_FOGLIO.findall(d)


def censisci(percorso):
    """(celle con formula, invisibili, visibili a meta', dettaglio)."""
    con_f = invis = meta = 0
    det = []
    try:
        z = zipfile.ZipFile(percorso)
    except Exception as ex:
        return None, None, None, [("(apertura fallita)", str(ex)[:60])]
    nomi = fogli(z)
    for i, (nome, _) in enumerate(nomi, 1):
        chiave = "xl/worksheets/sheet%d.xml" % i
        if chiave not in z.namelist():
            continue
        x = z.read(chiave).decode("utf-8", "replace")
        for rif, corpo in RE_CELLA.findall(x):
            mf = RE_FORMULA.search(corpo)
            if not mf:
                continue
            con_f += 1
            mv = RE_VALORE.search(corpo)
            if mv is None or not mv.group(1).strip():
                invis += 1
                det.append(("%s!%s" % (nome, rif), "INVISIBILE — formula %s, nessun valore in cache" % mf.group(1)[:40]))
            else:
                meta += 1
                det.append(("%s!%s" % (nome, rif), "a meta' — formula %s, valore %s" % (mf.group(1)[:30], mv.group(1)[:20])))
    return con_f, invis, meta, det


def main():
    ap = argparse.ArgumentParser(description="Conta le formule che l'estrattore congelato non restituisce.")
    ap.add_argument("--dettaglio", action="store_true")
    args = ap.parse_args()
    quando = datetime.now()

    manifest = sorted(n for n in Q.manifest_nomi() if n.lower().endswith((".xlsx", ".xlsm")))
    citati = set()
    for n in Q.tutte_le_note(Q.VAULT):
        citati |= {str(f) for f in n.fonti}

    righe, tot_f = [], [0, 0, 0]
    for nome in manifest:
        p = os.path.join(Q.VAULT, "sources", nome)
        con_f, invis, meta, det = censisci(p)
        if con_f is None:
            righe.append((nome, "-", "-", "-", nome in citati, det))
            continue
        tot_f[0] += con_f; tot_f[1] += invis; tot_f[2] += meta
        righe.append((nome, con_f, invis, meta, nome in citati, det))

    print("<!-- CENSIMENTO DELLE FORMULE — generato da `06_operativo\\censimento_formule.py`")
    print("     il %s. Si incolla VERBATIM. -->" % quando.strftime("%Y-%m-%d alle %H:%M:%S"))
    print()
    print("| Foglio di calcolo | Celle con formula | Di cui **invisibili** | Visibili a metà | Già canonizzato |")
    print("|---|---|---|---|---|")
    for nome, con_f, invis, meta, gia, _ in righe:
        print("| `%s` | %s | %s | %s | %s |"
              % (nome, con_f, "**%s**" % invis if isinstance(invis, int) and invis else invis,
                 meta, "sì" if gia else "**no**"))
    print("| **totale** | **%d** | **%d** | **%d** | |" % tuple(tot_f))
    print()

    da_fare = [r for r in righe if not r[4] and isinstance(r[2], int) and r[2] > 0]
    print("Fogli di calcolo nel manifest ............... %d" % len(manifest))
    print("Con almeno una formula ...................... %d" % sum(1 for r in righe if isinstance(r[1], int) and r[1] > 0))
    print("Con almeno una formula INVISIBILE ........... %d" % sum(1 for r in righe if isinstance(r[2], int) and r[2] > 0))
    print("  di cui NON ancora canonizzati ............. %d   <-- il numero della soglia" % len(da_fare))
    if da_fare:
        for r in da_fare:
            print("     %s" % r[0])
    print()
    print("SOGLIA scritta al gate del 21/08/2026: se piu' di TRE grezzi non ancora canonizzati")
    print("portano formule invisibili, l'estensione di cantiere della QA si fa prima di quei lotti.")
    print("ESITO: %s" % ("SOPRA SOGLIA — l'estensione si fa" if len(da_fare) > 3
                         else "SOTTO SOGLIA — basta il percorso di lettura dichiarato"))

    if args.dettaglio:
        print("\n--- dettaglio, cella per cella ---")
        for nome, _, _, _, _, det in righe:
            if det:
                print("\n%s" % nome)
                for rif, che in det:
                    print("   %-24s %s" % (rif, che))
    return 0


if __name__ == "__main__":
    sys.exit(main())
