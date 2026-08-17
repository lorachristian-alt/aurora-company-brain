# -*- coding: utf-8 -*-
"""collaudo_suite — la suite QA trova tutto cio' che deve, e niente di cio' che non deve.

Costruisce un vault finto con DUE note: una corretta, costruita su valori
riscontrati nei grezzi veri, e una con cinque difetti piantati apposta. Poi lancia
la suite e verifica che ciascun difetto sia stato trovato e che la nota corretta
NON abbia prodotto errori.

Un controllo che non e' stato collaudato non e' un controllo: e' una speranza.

⚠️ Questa cartella NON entra mai nel vault: e' banco di prova, non archivio.

Uso:  python collaudo_suite.py
Esce 0 se il collaudo passa, 1 altrimenti.
"""
import io, os, re, shutil, subprocess, sys

QUI = os.path.dirname(os.path.abspath(__file__))
QA = os.path.dirname(QUI)
sys.path.insert(0, QA)
VAULT = os.path.join(QUI, "vault_finto")
REPORT = os.path.join(QUI, "report")

# --- i due grezzi veri su cui poggia il collaudo -----------------------------
LOG = "log_temperature_pastorizzatore_linea1_10_05_26.log"
OEE = "calcolo_sfrido_efficienza_OEE_linea_bakery.csv"

INDEX_AREAS = """\
---
title: "areas — collaudo"
summary: "Vault finto per il collaudo della suite QA: due note, una corretta e una con difetti piantati apposta."
type: index
tags: [areas, indice]
data_nota: 2026-08-16
---

# areas

Banco di prova della suite. Non e' un archivio.

## Hub
- [[area-qualita]] — l'hub d'area che regge le due note del collaudo.
"""

HUB = """\
---
title: "Qualita — hub di collaudo"
summary: "Hub d'area del vault finto, che elenca le due note su cui si collauda la suite QA."
type: hub
area: qualita
tags: [areas, qualita, collaudo]
fonti:
  - %s
stato: risolto
data_nota: 2026-08-16
related: "[[_index-areas]]"
---

# Qualita — hub di collaudo

Hub minimo, che serve solo a dare una radice alle due note del collaudo.

## Le note di questo tema
- [[fatto-collaudo-buono]] — la deviazione del 10/05, con valori riscontrati.
- [[fatto-collaudo-rotto]] — la stessa deviazione, con cinque difetti piantati.

## Fonti
- [[%s]] — riga 14:21:07
""" % (LOG, LOG)

BUONA = """\
---
title: "Deviazione di temperatura del 10/05/2026 — nota di collaudo corretta"
summary: "Il 10/05/2026 il datalogger del PT-104 registra 68,9 gradi al cuore alle 14:21:07 con flag di allarme, sul turno che il foglio OEE chiude a 36,5."
type: atomica
area: qualita
tags: [areas, qualita, collaudo, ccp2]
fonti:
  - %s
  - %s
stato: risolto
aliases: []
data_fatto: 2026-05-10
data_nota: 2026-08-16
related: "[[area-qualita]]"
---

# Deviazione di temperatura del 10/05/2026 — nota di collaudo corretta

Il datalogger del pastorizzatore registra una temperatura al cuore di **68,9 °C**
alle 14:21:07 del 10/05/2026, con flag di allarme sul tracciato.

Lo stesso turno, sul foglio di efficienza, dichiara **5.580** pezzi prodotti e
**5.250** conformi su 14.400 teorici, con un OEE di **36,5** e **220** minuti di
fermo.

## Perche' conta

E' la nota di controllo del collaudo: ogni valore qui sopra e' stato riscontrato
nei due file citati, quindi la suite non deve emettere nessun ERRORE su di essa.
Si aggancia a [[area-qualita]] e alla sua gemella difettosa
[[fatto-collaudo-rotto]].

## Fonti
- [[%s]] — riga 14:21:07
- [[%s]] — riga 145, colonna `Pz_prodotti`
""" % (LOG, OEE, LOG, OEE)

# cinque difetti piantati, uno per riga di specifica:
#  1. fonte inventata          -> qa_frontmatter (non nel manifest)
#  2. numero senza riscontro   -> qa_provenance
#  3. wikilink rotto           -> qa_link_integrity
#  4. area fuori vocabolario   -> qa_frontmatter
#  5. stato sbagliato          -> qa_frontmatter (chiuso fuori da projects\)
ROTTA = """\
---
title: "Deviazione di temperatura del 10/05/2026 — nota di collaudo difettosa"
summary: "La stessa deviazione della nota gemella, riscritta con cinque difetti piantati apposta per verificare che la suite li trovi tutti."
type: atomica
area: qualita-alimentare
tags: [areas, qualita, collaudo]
fonti:
  - %s
  - verbale_inesistente_2026.pdf
stato: chiuso
aliases: []
data_fatto: 2026-05-10
data_nota: 2026-08-16
related: "[[area-qualita]]"
---

# Deviazione di temperatura del 10/05/2026 — nota di collaudo difettosa

Il turno del 10/05/2026 ha prodotto **99999** pezzi, valore che non compare in
nessuna delle fonti citate.

Il rimando qui sotto punta a una nota che non esiste: [[nota-che-non-esiste-mai]].

## Fonti
- [[%s]] — riga 14:21:07
- [[verbale_inesistente_2026.pdf]] — pag. 1, §2
""" % (LOG, LOG)

# --- cosa il collaudo PRETENDE di trovare -------------------------------------
ATTESI = [
    ("fonte inventata",        "qa_frontmatter",     r"verbale_inesistente_2026\.pdf.*manifest|manifest.*verbale_inesistente"),
    ("area fuori vocabolario", "qa_frontmatter",     r"qualita-alimentare.*vocabolario"),
    ("stato sbagliato",        "qa_frontmatter",     r"stato vuole risolto\|aperto"),
    ("wikilink rotto",         "qa_link_integrity",  r"wikilink rotto.*nota-che-non-esiste-mai"),
    ("numero senza riscontro", "qa_provenance",      r"99999|99\.999"),
]


def scrivi(p, t):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with io.open(p, "w", encoding="utf-8") as f:
        f.write(t)


def prepara():
    if os.path.isdir(VAULT):
        shutil.rmtree(VAULT)
    scrivi(os.path.join(VAULT, "areas", "_index-areas.md"), INDEX_AREAS)
    scrivi(os.path.join(VAULT, "areas", "area-qualita.md"), HUB)
    scrivi(os.path.join(VAULT, "areas", "fatto-collaudo-buono.md"), BUONA)
    scrivi(os.path.join(VAULT, "areas", "fatto-collaudo-rotto.md"), ROTTA)
    subprocess.run([sys.executable, os.path.join(QA, "genera_llms.py"), "--vault", VAULT],
                   cwd=QA, capture_output=True, text=True)


def esegui():
    if os.path.isdir(REPORT):
        shutil.rmtree(REPORT)
    os.makedirs(REPORT)
    out = {}
    for s in ("qa_frontmatter.py", "qa_link_integrity.py", "qa_provenance.py", "qa_copertura.py"):
        r = subprocess.run(
            [sys.executable, os.path.join(QA, s), "--perimetro", "lotto", LOG, OEE,
             "--vault", VAULT, "--report", REPORT],
            cwd=QA, capture_output=True, text=True, encoding="utf-8", errors="replace")
        out[s.replace(".py", "")] = (r.stdout or "") + (r.stderr or "")
    return out


def main():
    prepara()
    out = esegui()

    print("=" * 74)
    print("COLLAUDO DELLA SUITE QA — cosa doveva trovare")
    print("=" * 74)
    mancati = []
    for etichetta, script, rx in ATTESI:
        testo = out.get(script, "")
        ok = re.search(rx, testo, re.I | re.S) is not None
        print("%-26s %-20s %s" % (etichetta, script, "TROVATO" if ok else "*** NON TROVATO ***"))
        if not ok:
            mancati.append(etichetta)

    print("\n" + "=" * 74)
    print("COLLAUDO — cosa NON doveva segnalare (la nota corretta)")
    print("=" * 74)
    falsi = []
    for script, testo in out.items():
        for riga in testo.splitlines():
            if riga.startswith("ERRORE") and "fatto-collaudo-buono" in riga:
                falsi.append(riga.strip())
    if falsi:
        for r in falsi:
            print("*** FALSO POSITIVO ***  " + r)
    else:
        print("nessun ERRORE sulla nota corretta: la suite non spara sui vivi.")

    avvisi_buona = [r.strip() for t in out.values() for r in t.splitlines()
                    if r.startswith("AVVISO") and "fatto-collaudo-buono" in r]
    if avvisi_buona:
        print("\n(avvisi sulla nota corretta, ammessi e non bloccanti:)")
        for r in avvisi_buona:
            print("   " + r)

    print("\n" + "=" * 74)
    if mancati or falsi:
        print("COLLAUDO FALLITO — difetti non trovati: %s | falsi positivi: %d"
              % (", ".join(mancati) or "nessuno", len(falsi)))
        return 1
    print("COLLAUDO SUPERATO — 5 difetti su 5 trovati, 0 falsi positivi sulla nota corretta.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
