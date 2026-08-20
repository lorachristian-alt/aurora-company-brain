# -*- coding: utf-8 -*-
"""cerca_assenza — la ricerca che attesta un'assenza, e lascia il suo artefatto (E43).

Dichiarare che «nessun grezzo dice X» e' affermare un fatto, e va verificato come un fatto:
con una ricerca su TUTTO `sources\\`, non sui documenti dove ci si aspettava di trovarlo (E3).

=====================================================================================
PERCHE' QUESTO SCRIPT ESISTE
=====================================================================================
⚠️ **E3 e' stato pagato QUATTRO volte in cinque lotti**: `PRP-09` nel pilota, l'ossigeno
residuo in 1A, e due note nel lotto 2A dove la formula di attestazione — «assenza verificata
su tutto sources\\, manifest v1.1» — era stata scritta **senza che la ricerca fosse stata
fatta**. In un caso il documento dato per assente era gia' fra le fonti della nota stessa.

E' §4.20 al rovescio: quando una soglia scatta sempre il difetto e' nella grandezza che
misura; **quando una regola viene violata sempre, il difetto non e' nella diligenza di chi la
applica, e' nel fatto che nessuno puo' verificarla.** Una regola pagata quattro volte non ha
bisogno di essere ripetuta: ha bisogno di un controllo.

⚠️ **Che cosa questo strumento puo' e non puo' fare, detto con precisione.** Non puo'
verificare il CONTENUTO di un'assenza: nessuno script stabilisce che «nessun grezzo dice X»
sia vero, perche' X puo' essere scritto in dieci modi. Puo' pero' rendere verificabile la
PROCEDURA — che la ricerca sia stata eseguita, con quali termini, su quale perimetro e con
quale esito — perche' quella lascia un file. `qa_frontmatter.py` verifica poi che ogni nota
che porta la formula di E3 rimandi a un artefatto **che esiste**.

⚠️ **La ricerca guarda il TESTO ESTRATTO, non il nome del file.** Usa lo stesso estrattore
congelato della suite (`text_of`, metodo_01 §5-bis), cosi' cerca dentro i `.docx` e i `.pdf`
come dentro i `.txt` — ed e' proprio dentro un `.docx` che stava, in 2A, il documento dato
per assente. ⚠️ Sui `.jpg` l'estrattore e' cieco e restituisce stringa vuota: l'artefatto lo
DICHIARA, invece di far credere che la ricerca li abbia coperti.

Uso:
    python cerca_assenza.py --termini "MOD-HR-11" "registro formazione" --nome mod-hr-11
Scrive `06_operativo\\ricerche_assenza\\<nome>_<data>.md` e stampa il rimando da incollare
nella nota. Esce 0 se l'assenza e' confermata, 1 se invece qualcosa e' stato TROVATO — perche'
in quel caso l'assenza non si scrive.
"""
import argparse, io, os, sys
from datetime import datetime

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(QUI, "qa"))
import qa_comune as Q

DIR = os.path.join(QUI, "ricerche_assenza")


def main():
    ap = argparse.ArgumentParser(description="Cerca un termine su tutto sources\\ e lascia l'artefatto.")
    ap.add_argument("--termini", nargs="+", required=True,
                    help="i termini da cercare; basta che UNO compaia perche' l'assenza cada")
    ap.add_argument("--nome", required=True, help="slug dell'artefatto, senza estensione")
    ap.add_argument("--nota", default="", help="la nota che dichiarera' l'assenza, se gia' nota")
    args = ap.parse_args()

    manifest = sorted(Q.manifest_nomi())
    quando = datetime.now()
    trovati, ciechi, letti = [], [], 0

    for nome in manifest:
        try:
            testo = Q.testo_fonte(nome)
        except Exception as ex:
            ciechi.append((nome, "estrazione non riuscita: %s" % str(ex)[:50]))
            continue
        if not testo.strip():
            ciechi.append((nome, "nessun testo estraibile (immagine o file muto)"))
            continue
        letti += 1
        basso = Q.senza_accenti(testo).lower()
        for t in args.termini:
            if Q.senza_accenti(t).lower() in basso:
                trovati.append((nome, t))

    r = ["# Ricerca di assenza — `%s`" % args.nome, "",
         "> **Che cos'è** · L'artefatto che E43 impone a chi dichiara un'assenza: la prova che",
         "> la ricerca su tutto `sources\\` è stata **eseguita**, con i termini e il perimetro",
         "> che ha avuto. ⚠️ Non prova che l'assenza sia vera — nessuno script può — prova che",
         "> il gesto è stato fatto.", "",
         "| | |", "|---|---|",
         "| Eseguita il | **%s** |" % quando.strftime("%d/%m/%Y alle %H:%M:%S"),
         "| Termini cercati | %s |" % " · ".join("`%s`" % t for t in args.termini),
         "| Perimetro | i **%d** file del manifest `manifest_corpus_v1.1.json`, in `sources\\` |" % len(manifest),
         "| File con testo estraibile | **%d** |" % letti,
         "| File senza testo estraibile | **%d** — elencati sotto |" % len(ciechi),
         "| Confronto | senza accenti, senza distinzione di maiuscole |",
         "| Esito | **%s** |" % ("ASSENZA CONFERMATA" if not trovati
                                 else "TROVATO in %d file: l'assenza NON si scrive" % len(trovati)),
         ""]
    if args.nota:
        r += ["Dichiarata nella nota `%s`." % args.nota, ""]
    if trovati:
        r += ["## Dove è stato trovato", ""]
        r += ["- `%s` — termine `%s`" % (f, t) for f, t in trovati] + [""]
    r += ["## I file su cui la ricerca è cieca, e va detto", "",
          "L'estrattore congelato non ha un ramo per le immagini e restituisce stringa vuota:",
          "su questi file la ricerca **non ha guardato**, e chi legge l'artefatto deve saperlo.",
          ""]
    r += ["- `%s` — %s" % (f, m) for f, m in ciechi] or ["*(nessuno)*"]
    r += ["", "---", "",
          "Prodotto da `06_operativo\\cerca_assenza.py`. Non si scrive a mano: si rilancia."]

    os.makedirs(DIR, exist_ok=True)
    out = "%s_%s.md" % (args.nome, quando.strftime("%Y-%m-%d"))
    io.open(os.path.join(DIR, out), "w", encoding="utf-8", newline="\n").write("\n".join(r) + "\n")

    print("artefatto: 06_operativo\\ricerche_assenza\\%s" % out)
    print("file letti: %d · ciechi: %d · trovati: %d" % (letti, len(ciechi), len(trovati)))
    if trovati:
        print("\n⚠️ TROVATO — l'assenza NON si dichiara:")
        for f, t in trovati[:10]:
            print("   %s  (termine: %s)" % (f, t))
        return 1
    print("\nRimando da incollare nella nota:")
    print("   ricerca depositata in `06_operativo\\ricerche_assenza\\%s`" % out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
