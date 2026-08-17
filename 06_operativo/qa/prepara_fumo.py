# -*- coding: utf-8 -*-
"""prepara_fumo — estrae gli id delle domande che ricadono dentro la fetta pilota.

Sessione 2, mini-misura di fumo. Legge `03_valutazione\\eval_set.jsonl` e scrive
in `06_operativo\\qa\\fumo_ids.txt` **soltanto gli id** delle domande le cui fonti
attese stanno TUTTE dentro la fetta.

⚠️ Perche' esiste questo script, e non lo fa una persona a mano: chi canonizza non
apre mai `03_valutazione\\` (metodo_03 §10.38). Lo script e' l'eccezione strumentale
che permette di selezionare un sottoinsieme di domande senza che nessuno veda le
domande, le risposte attese o i criteri. Per questo:

  * stampa e scrive SOLO gli id, mai altro campo;
  * in diagnostica mostra al piu' i NOMI delle chiavi del file, mai i loro valori;
  * non copia, non riassume e non tiene in memoria nient'altro.

Uso:
    python prepara_fumo.py
    python prepara_fumo.py --fetta fetta_l26130.txt --out fumo_ids.txt
"""
import argparse, io, json, os, sys

QUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(QUI))          # radice del repository
EVAL = os.path.join(REPO, "03_valutazione", "eval_set.jsonl")

# i nomi sotto cui il campo delle fonti attese puo' comparire
CHIAVI_FONTI = ("fonti", "fonti_corrette", "fonti_attese", "sources", "file", "files")
CHIAVI_ID = ("id", "ID", "id_domanda", "qid")


def leggi_fetta(percorso):
    fetta = set()
    for r in io.open(percorso, encoding="utf-8"):
        r = r.strip()
        if r and not r.startswith("#"):
            fetta.add(r)
    return fetta


def main():
    ap = argparse.ArgumentParser(description="Id delle domande interamente coperte dalla fetta.")
    ap.add_argument("--fetta", default=os.path.join(QUI, "fetta_l26130.txt"))
    ap.add_argument("--eval", default=EVAL)
    ap.add_argument("--out", default=os.path.join(QUI, "fumo_ids.txt"))
    ap.add_argument("--copia-domande", metavar="CARTELLA", default=None,
                    help="copia id+testo delle domande selezionate da domande_solo.jsonl "
                         "nella cartella della misura, senza mostrarne il contenuto")
    args = ap.parse_args()

    fetta = leggi_fetta(args.fetta)
    if not fetta:
        print("La fetta e' vuota: controlla %s" % args.fetta); sys.exit(1)

    if not os.path.isfile(args.eval):
        print("Non trovo %s" % args.eval); sys.exit(1)

    dentro, totale, senza_fonti = [], 0, 0
    chiave_fonti = chiave_id = None

    for riga in io.open(args.eval, encoding="utf-8"):
        riga = riga.strip()
        if not riga:
            continue
        voce = json.loads(riga)
        totale += 1

        if chiave_id is None:
            chiave_id = next((k for k in CHIAVI_ID if k in voce), None)
            chiave_fonti = next((k for k in CHIAVI_FONTI if k in voce), None)
            if chiave_id is None or chiave_fonti is None:
                # diagnostica che non rivela contenuti: solo i NOMI dei campi
                print("Non riconosco lo schema del file. Chiavi presenti: %s"
                      % ", ".join(sorted(voce.keys())))
                print("Aggiungi il nome giusto a CHIAVI_ID / CHIAVI_FONTI e rilancia.")
                sys.exit(1)

        fonti = voce.get(chiave_fonti)
        if isinstance(fonti, str):
            fonti = [f.strip() for f in fonti.replace(";", ",").split(",") if f.strip()]
        if not fonti:
            senza_fonti += 1          # domande non rispondibili: non entrano nella fumo
            continue
        if all(f in fetta for f in fonti):
            dentro.append(str(voce[chiave_id]))

    with io.open(args.out, "w", encoding="utf-8") as f:
        f.write("# id delle domande le cui fonti attese stanno tutte dentro la fetta pilota\n")
        f.write("# generato da prepara_fumo.py — SOLO id, nessun altro campo\n")
        for i in dentro:
            f.write(i + "\n")

    print("voci lette: %d | senza fonti dichiarate (escluse): %d | dentro la fetta: %d"
          % (totale, senza_fonti, len(dentro)))
    print("scritto: %s" % args.out)

    # --- consegna delle domande al rispondente -------------------------------------
    # Il rispondente gira con `03_valutazione\` FUORI dal perimetro fisico (principio 6
    # della scaletta): le domande devono essergli portate dentro. Questa copia prende da
    # `domande_solo.jsonl` — che contiene le domande e NON le risposte attese — le sole
    # voci selezionate, e le scrive nella cartella della misura. Nessun contenuto passa
    # per il terminale di chi coordina: si stampa solo il conteggio.
    if args.copia_domande:
        sorgente = os.path.join(REPO, "03_valutazione", "domande_solo.jsonl")
        if not os.path.isfile(sorgente):
            print("Non trovo %s: le domande vanno incollate a mano." % sorgente); sys.exit(1)
        voluti, scritte = set(dentro), 0
        os.makedirs(args.copia_domande, exist_ok=True)
        destinazione = os.path.join(args.copia_domande, "domande_fumo.jsonl")
        with io.open(destinazione, "w", encoding="utf-8") as out:
            for riga in io.open(sorgente, encoding="utf-8"):
                riga = riga.strip()
                if not riga:
                    continue
                voce = json.loads(riga)
                k = next((x for x in CHIAVI_ID if x in voce), None)
                if k is not None and str(voce[k]) in voluti:
                    out.write(json.dumps(voce, ensure_ascii=False) + "\n")
                    scritte += 1
        print("domande copiate per il rispondente: %d -> %s" % (scritte, destinazione))
        if scritte != len(dentro):
            print("⚠️ attese %d, copiate %d: verifica prima di misurare." % (len(dentro), scritte))
    if not dentro:
        print("\nNessuna domanda ricade interamente nella fetta: la misura di fumo non ha oggetto.")


if __name__ == "__main__":
    main()
