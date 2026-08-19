# -*- coding: utf-8 -*-
"""qa_all — il lanciatore della suite.

metodo_03 §7.5. Esegue i quattro controlli nell'ordine
`frontmatter -> link -> provenance -> copertura` e scrive un report unico con il
contatore per esito, l'elenco degli ERRORI, quello degli AVVISI e la riga di
riepilogo che va nello stato di sessione.

**Nessun numero si dichiara senza che questo script l'abbia contato** (regola d'oro 5).

Uso:
    python qa_all.py --perimetro lotto @lotti/<lotto>.txt --lotto <nome>
    python qa_all.py --perimetro vault
    python qa_all.py --perimetro lotto @lotti/<lotto>.txt --note-toccate <elenco>
    python qa_all.py --perimetro lotto @lotti/<manutenzione>.txt   (E35: 0 grezzi, N note)

⚠️ Le vie qui sopra sono le VIE DI PRODUZIONE, e sono collaudate una per una in
`_collaudo/collaudo_suite.py`, che le elenca nel proprio docstring. Chi ne aggiunge una
pianta anche il difetto che la esercita: quello che sta FRA il lanciatore e i figli -
l'inoltro degli argomenti, i default, l'ordine di chiamata - non vive dentro nessuna
unita', e nessun test di unita' lo vede per costruzione.

Esce 0 (verde) · 1 (almeno un ERRORE) · 2 (solo AVVISI).
"""
import argparse, os, re, subprocess, sys
from datetime import date

import qa_comune as Q

ORDINE = ["qa_frontmatter.py", "qa_link_integrity.py", "qa_provenance.py", "qa_copertura.py"]
QUI = os.path.dirname(os.path.abspath(__file__))


def main():
    ap = argparse.ArgumentParser(description="Esegue tutta la suite QA delle note.")
    Q.aggiungi_argomenti(ap)
    ap.add_argument("--lotto", default=None,
                    help="nome del lotto, per la cartella e per l'intestazione del report. "
                         "Se non si passa e il perimetro e' `@lotti/<nome>.txt`, vale <nome> (FIX 4)")
    ap.add_argument("--pacchetto-giudizio", action="store_true",
                    help="prepara anche il pacchetto per lo strato di giudizio della provenance")
    args, _ = ap.parse_known_args()
    modo, _file_lotto = Q.leggi_perimetro(args)

    # FIX 4 - l'etichetta del lotto non si inventa e non resta al default per distrazione.
    # Il report del lotto 1C portava «lotto l26130» perche' --lotto non era stato passato:
    # il documento che prova la QA di un lotto portava il nome di un altro lotto, e al gate
    # finale quei report sono la prova. --lotto esplicito vince sempre; qui si riempie solo
    # il vuoto, e con un'informazione corretta.
    if args.lotto is None:
        args.lotto = Q.nome_lotto_da_perimetro(args.perimetro) or "l26130"

    d = args.report or os.path.join(Q.QA_DIR, "%s_%s" % (date.today().isoformat(),
                                                         "vault" if modo == "vault" else args.lotto))
    os.makedirs(d, exist_ok=True)

    base = ["--perimetro"] + args.perimetro + ["--report", d, "--vault", args.vault]
    # FIX 1 - il flag si INOLTRA. Senza questa riga E32 reggeva solo per caso: ogni figlio,
    # dentro leggi_perimetro, si ricalcolava da se' la convenzione `lotti/<lotto>_note.txt`
    # quando il perimetro arriva come `@elenco.txt`. Chi passa l'elenco ESPLICITAMENTE - nome
    # diverso, percorso diverso, che e' il caso del lotto di manutenzione - se lo vedeva
    # ignorare IN SILENZIO, con la QA verde e le note modificate fuori perimetro.
    if getattr(args, "note_toccate", None):
        base += ["--note-toccate", args.note_toccate]
    esiti = {}
    for script in ORDINE:
        cmd = [sys.executable, os.path.join(QUI, script)] + base
        if script == "qa_provenance.py" and args.pacchetto_giudizio:
            cmd.append("--pacchetto-giudizio")
        print("\n=== %s ===" % script)
        r = subprocess.run(cmd, cwd=QUI, capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        sys.stdout.write(r.stdout or "")
        if r.stderr and r.returncode not in (0, 1, 2):
            sys.stdout.write(r.stderr)
        esiti[script] = r.returncode

    # ---- si ricontano gli esiti dai report scritti, non dalla memoria -----------
    tot_err = tot_avv = 0
    pezzi = []
    for script in ORDINE:
        p = os.path.join(d, script.replace(".py", ".md"))
        if not os.path.isfile(p):
            pezzi.append("## %s\n\n*(nessun report prodotto: lo script e' uscito male)*\n" % script)
            continue
        testo = open(p, encoding="utf-8").read()
        e = int(re.search(r"- ERRORI: \*\*(\d+)\*\*", testo).group(1))
        a = int(re.search(r"- AVVISI: \*\*(\d+)\*\*", testo).group(1))
        tot_err += e; tot_avv += a
        pezzi.append(testo)

    # ---- inventario delle note, ricontato qui e non a memoria (regola d'oro 5) ------
    note = Q.tutte_le_note(args.vault)
    per_cartella, per_type = {}, {}
    for n in note:
        per_cartella[n.cartella] = per_cartella.get(n.cartella, 0) + 1
        per_type[n.type or "(senza type)"] = per_type.get(n.type or "(senza type)", 0) + 1
    conteggio_qualita = sum(v for k, v in per_cartella.items() if k not in Q.ESCLUSE_QUALITA)

    inventario = ["## Inventario delle note\n",
                  "| Cartella | Note |", "|---|---|"]
    for c in Q.CARTELLE:
        if c in per_cartella:
            inventario.append("| `%s\\` | %d |" % (c, per_cartella[c]))
    inventario += ["| **totale** | **%d** |" % len(note), "",
                   "*Escluse `workspace\\` e `sources\\` dai conteggi di qualità: "
                   "**%d** note.*\n" % conteggio_qualita,
                   "| `type` | Note |", "|---|---|"]
    for t in sorted(per_type):
        inventario.append("| `%s` | %d |" % (t, per_type[t]))
    inventario.append("")

    codice = 1 if tot_err else (2 if tot_avv else 0)
    stato = "VERDE" if codice == 0 else ("ROSSO" if codice == 1 else "GIALLO")

    # E35 - il perimetro di manutenzione si DICHIARA in chiaro, nel report e nel riepilogo.
    # Un lotto che non canonizza nessun grezzo e' un fatto che chi legge il report deve
    # vedere senza doverlo dedurre da un elenco vuoto.
    manut = getattr(args, "manutenzione", 0)
    if modo == "vault":
        riga_perimetro = "- Perimetro: **vault**"
        etichetta_perimetro = "vault"
    elif manut:
        riga_perimetro = ("- Perimetro: **lotto** (lotto `%s`) — **perimetro di manutenzione: "
                          "0 grezzi, %d note** (E35)" % (args.lotto, manut))
        etichetta_perimetro = "manutenzione (0 grezzi, %d note)" % manut
    else:
        riga_perimetro = "- Perimetro: **lotto** (lotto `%s`)" % args.lotto
        etichetta_perimetro = "lotto"
    riepilogo = ("suite QA · perimetro %s · **%d ERRORI, %d AVVISI** · esito **%s**"
                 % (etichetta_perimetro, tot_err, tot_avv, stato))

    testata = [
        "# Suite QA delle note — report unico",
        "",
        "- Data: %s" % date.today().isoformat(),
        riga_perimetro,
        "- Vault: `%s`" % args.vault,
        "",
        "| Controllo | Codice di uscita |",
        "|---|---|",
    ] + ["| `%s` | %d |" % (s, esiti[s]) for s in ORDINE] + [
        "",
        "## Riga di riepilogo per lo stato di sessione",
        "",
        "> " + riepilogo,
        "",
        "---",
        "",
    ] + inventario + ["---", ""]

    p = Q.scrivi_report(d, "qa_all.md", "\n".join(testata) + "\n\n".join(pezzi))
    print("\n" + "=" * 70)
    for r in inventario:
        if r.startswith("|") or r.startswith("*"):
            print(r)
    print(riepilogo)
    print("report unico: %s" % p)
    sys.exit(codice)


if __name__ == "__main__":
    main()
