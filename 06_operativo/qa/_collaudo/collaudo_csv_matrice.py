# -*- coding: utf-8 -*-
"""collaudo_csv_matrice — una riga col separatore dentro un campo non deve nascere.

⚠️ **PERIMETRO CHIUSO.** Non tocca `matrice_corpus_v1.csv`: costruisce righe finte e
verifica il solo predicato che decide se una riga puo' essere scritta.

PERCHE' ESISTE.
Il 21/08/2026 `genera_matrice_file_fatto.py` e' andato in errore **a meta' scrittura** e
ha lasciato il CSV a 184 righe delle 293 che aveva. La causa non era nello script che
scriveva: erano **tre righe gia' nel file** con un punto e virgola non protetto dentro il
campo `fatto` — «presa in carico a NO; l'episodio si ripete il 30/05» — che il lettore
spezzava in sette campi invece di sei.

⚠️ **E si vedevano.** Nel censimento comparivano come **tre lotti fantasma** chiamati col
nome di una nota, perche' lo slittamento dei campi spostava la nota nella colonna del
lotto. Sono rimaste li' per un lotto intero senza che nessuno le guardasse.

IL DIFETTO CHE QUESTO COLLAUDO PIANTA, e il verso conta:
una riga malformata dev'essere **RIFIUTATA IN SCRITTURA**, non scoperta in lettura. Un
controllo in lettura arriva sempre dopo il danno; un controllo in scrittura lo impedisce,
e lascia sul disco il file vecchio e integro invece di uno nuovo e mezzo.

Uso:
    python collaudo_csv_matrice.py
Esce 0 se tutti i casi passano, 1 altrimenti.
"""
import io, os, sys, tempfile

QUI = os.path.dirname(os.path.abspath(__file__))
OPERATIVO = os.path.dirname(os.path.dirname(QUI))
sys.path.insert(0, OPERATIVO)
sys.path.insert(0, os.path.join(OPERATIVO, "qa"))
import genera_matrice_file_fatto as G


def riga(fatto, lotto="1B"):
    return {"file": "log_esempio.log", "fatto": fatto, "cartella_prevista": "areas",
            "nota_padrona_prevista": "fatto-esempio", "lotto": lotto, "stato": "fatta"}


CASI = [
    # (etichetta, riga, deve_essere_rifiutata)
    ("la riga pulita passa",
     riga("Porta della cella aperta 38 minuti il 15/04 con allarme a cinque minuti"), False),
    ("il separatore dentro il campo `fatto` — il caso vero del 21/08",
     riga("presa in carico a NO; l'episodio si ripete il 30/05 e diventa NC-2026-114"), True),
    ("il separatore dentro un altro campo",
     riga("un fatto qualunque", lotto="1B;2A"), True),
    ("un ritorno a capo dentro il campo",
     riga("un fatto\nspezzato in due righe"), True),
    ("una virgoletta nuda dentro il campo",
     riga('un fatto con "virgolette" dritte'), True),
]


def main():
    print("=" * 74)
    print("CONTROLLO IN SCRITTURA — una riga malformata non deve nascere")
    print("=" * 74)
    esiti = []
    for etichetta, r, atteso in CASI:
        guasti = G.controlla_riga(r, "riga di collaudo")
        rifiutata = bool(guasti)
        ok = (rifiutata == atteso)
        esiti.append(ok)
        print("%-56s %-10s %s"
              % (etichetta, "rifiutata" if rifiutata else "accettata",
                 "ok" if ok else "*** FALLITO"))

    # e la misura di chiusura sa contare i campi di un file scritto a mano
    print()
    print("=" * 74)
    print("MISURA DI CHIUSURA — righe e campi per riga")
    print("=" * 74)
    tmp = tempfile.mkdtemp(prefix="collaudo_csv_")
    try:
        p = os.path.join(tmp, "finto.csv")
        with io.open(p, "w", encoding="utf-8", newline="") as f:
            f.write(";".join(G.COLONNE) + "\n")
            f.write("a;b;areas;c;1B;fatta\n")
            f.write("a;b;con;un;campo;in;piu\n")
        n, campi = G.conta_campi(p)
        ok = (n == 2 and campi == [6, 7])
        esiti.append(ok)
        print("due righe, di cui una con sette campi: contate %d righe, campi %s  %s"
              % (n, campi, "ok" if ok else "*** FALLITO"))
    finally:
        import shutil
        shutil.rmtree(tmp, ignore_errors=True)

    print()
    if all(esiti):
        print("COLLAUDO SUPERATO — %d casi su %d." % (len(esiti), len(esiti)))
        print("La riga malformata viene fermata PRIMA che il file venga aperto in scrittura.")
        return 0
    print("COLLAUDO FALLITO: la guardia in scrittura non ferma cio' che deve.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
