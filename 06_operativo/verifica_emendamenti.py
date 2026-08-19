# -*- coding: utf-8 -*-
"""verifica_emendamenti — il registro degli emendamenti concorda con metodo_03.

`registro_emendamenti.md` e' un INDICE, non una copia: non porta il testo delle
regole, ma dice per ogni emendamento in quale sezione di metodo_03 vive e se nel
manuale compare il marcatore `(Enn)`. Un indice che sbaglia il puntatore e' peggio
di nessun indice, e questi puntatori si scrivono a mano una volta e poi invecchiano.

Controlla:
  1. la numerazione del registro e' continua da E1 e senza buchi ne' doppioni;
  2. ogni sezione dichiarata nella colonna «Vive in» esiste in metodo_03;
  3. la colonna «Marc.» dice il vero: se e' `si`, la sigla `(Enn)` compare nel
     manuale; se e' `no`, non compare;
  4. ogni marcatore presente nel manuale ha la sua riga nel registro (nessun
     emendamento applicato e mai registrato);
  5. per i marcatori presenti, la sezione dichiarata e' fra quelle in cui il
     marcatore compare davvero.

Uso:
    python verifica_emendamenti.py
Esce 0 se il registro concorda con il manuale, 1 altrimenti.
"""
import io, os, re, sys

QUI = os.path.dirname(os.path.abspath(__file__))
METODO = os.path.join(QUI, os.pardir, "01_metodo", "metodo_03_canonizzazione.md")
REGISTRO = os.path.join(QUI, "registro_emendamenti.md")


def leggi(percorso):
    with io.open(percorso, encoding="utf-8") as f:
        return f.read()


def sezioni_del_manuale(testo):
    """Numeri di sezione presenti come titolo: '## 9.' -> 9, '### 9.5' -> 9.5.

    Il registro cita anche sotto-riferimenti che non sono titoli (`§10, divieto
    9-bis`, `§9.5, passo 8`): di quelli si verifica la sezione portante, cioe' la
    parte numerica prima della virgola.
    """
    viste = set()
    for riga in testo.split("\n"):
        m = re.match(r'^#{2,4}\s+(\d+(?:\.\d+)?)', riga)
        if m:
            viste.add(m.group(1))
            viste.add(m.group(1).split(".")[0])
    return viste


def marcatori_del_manuale(testo):
    """Sigla -> insieme delle sezioni in cui compare, leggendo il testo dall'alto."""
    dove = {}
    sezione = "(testa)"
    for riga in testo.split("\n"):
        m = re.match(r'^#{2,4}\s+(\d+(?:\.\d+)?)', riga)
        if m:
            sezione = m.group(1)
        for n in re.findall(r'\bE(\d{1,2})\b', riga):
            dove.setdefault(int(n), set()).add(sezione)
    return dove


def righe_del_registro(testo):
    """Le righe della tabella: numero, sezioni dichiarate, flag del marcatore."""
    fuori = []
    for riga in testo.split("\n"):
        m = re.match(r'^\|\s*\*\*E(\d{1,2})\*\*\s*\|', riga)
        if not m:
            continue
        celle = [c.strip() for c in riga.strip().strip("|").split("|")]
        numero = int(m.group(1))
        vive_in, marcatore = celle[5], celle[6].lower()
        sezioni = re.findall(r'§(\d+(?:\.\d+)?)', vive_in)
        fuori.append((numero, sezioni, marcatore, vive_in))
    return fuori


def main():
    manuale, registro = leggi(METODO), leggi(REGISTRO)
    sezioni = sezioni_del_manuale(manuale)
    marcatori = marcatori_del_manuale(manuale)
    righe = righe_del_registro(registro)
    errori = []

    if not righe:
        errori.append("il registro non contiene nessuna riga di emendamento")

    numeri = [r[0] for r in righe]
    attesi = list(range(1, len(numeri) + 1))
    if sorted(numeri) != attesi:
        errori.append("numerazione non continua: attesi E1..E%d, trovati %s"
                      % (len(numeri), ", ".join("E%d" % n for n in sorted(numeri))))

    for numero, sez, marcatore, vive_in in righe:
        if not sez:
            errori.append("E%d: nessuna sezione riconosciuta in «%s»" % (numero, vive_in))
        for s in sez:
            if s not in sezioni:
                errori.append("E%d: la sezione §%s non esiste in metodo_03" % (numero, s))
        presente = numero in marcatori
        if marcatore.startswith("s") and not presente:
            errori.append("E%d: il registro dichiara il marcatore, il manuale non lo porta" % numero)
        if marcatore.startswith("n") and presente:
            errori.append("E%d: il registro dichiara «no», ma il manuale porta la sigla (in %s)"
                          % (numero, ", ".join("§" + x for x in sorted(marcatori[numero]))))
        if presente and marcatore.startswith("s"):
            if not (set(sez) & marcatori[numero]):
                errori.append("E%d: dichiarato in %s, il marcatore compare in %s"
                              % (numero, ", ".join("§" + x for x in sez),
                                 ", ".join("§" + x for x in sorted(marcatori[numero]))))

    for numero in sorted(marcatori):
        if numero not in numeri:
            errori.append("E%d compare in metodo_03 ma non ha riga nel registro" % numero)

    print("Emendamenti nel registro: %d" % len(righe))
    print("Marcatori inline in metodo_03: %d (%s)"
          % (len(marcatori), ", ".join("E%d" % n for n in sorted(marcatori))))
    senza = sorted(n for n, _, m, _ in righe if m.startswith("n"))
    print("Applicati senza marcatore: %d (%s)"
          % (len(senza), ", ".join("E%d" % n for n in senza) or "nessuno"))

    if errori:
        print("\nERRORI: %d" % len(errori))
        for e in errori:
            print("  - " + e)
        return 1
    print("\nRegistro e manuale concordano.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
