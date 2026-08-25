# -*- coding: utf-8 -*-
r"""collaudo_taglio_fonti — il delimitatore delle fonti non puo' comparire dentro un grezzo.

=====================================================================================
PERCHE' QUESTO COLLAUDO ESISTE — IL GUASTO DEL LOTTO 3F
=====================================================================================
`qa_provenance.pacchetto_giudizio` separava le fonti dell'appendice con `--- <nome> ---`, e
`taglia_pacchetto.spezza` le rileggeva con `^--- (.+) ---$`.

⚠️ **Quella forma COMPARE DENTRO I GREZZI.** Il grezzo del lotto 3F — la notifica di ispezione
ATS — ne porta due nel proprio testo: `--- TESTO DELL'ATTO ALLEGATO ---` e
`--- FINE TESTO DELL'ATTO ---`. Lo splitter le ha lette come inizio di altre due fonti, e:

  - la fonte PRINCIPALE del lotto e' arrivata al giudice **troncata a 638 caratteri su
    13.186** — il 5 % del documento;
  - le due mail interne, che sono meta' del lotto, **in due fette su tre non c'erano affatto**;
  - la guardia di `taglia_pacchetto` ha dichiarato tutte e tre le fette **«complete»**, perche'
    verificava che l'appendice contenesse *qualcosa* (piu' di 200 caratteri), non che portasse
    la fonte **intera**.

⚠️ **E' E10 SUL SECONDO DELIMITATORE.** Il commento di `pacchetto_giudizio` gia' spiegava, per
le NOTE, che il delimitatore non puo' essere una stringa che un grezzo puo' contenere — con
«NOTA:» il conteggio si falsava perche' quella stringa e' nel manuale HACCP. **La stessa
medicina non era stata applicata alle FONTI**, ed e' rimasta scoperta per undici lotti: nessun
grezzo, fino a 3F, aveva scritto una riga di quella forma.

⚠️ **E' anche §4.49**: un controllo copre le superfici che il suo COLLAUDO esercita. Il
collaudo che esisteva — `collaudo_appendice_fonti`, in `collaudo_suite.py` — verifica che
l'appendice **ci sia e non sia vuota**, cioe' il guasto di R1 (§4.29). Non verifica che porti
i documenti **per intero**, e il guasto di 3F ci e' passato in mezzo.

=====================================================================================
I CASI
=====================================================================================
| # | Caso | Atteso |
|---|---|---|
| 1 | **LA PREMESSA**: il grezzo finto porta davvero una riga della forma vecchia | la riga c'e' |
| 2 | **IL DIFETTO PIANTATO**: la via VECCHIA (`--- <nome> ---`) su quel grezzo | **tronca** la fonte |
| 3 | la via DI PRODUZIONE, sullo stesso grezzo | porta la fonte **intera** |
| 4 | il taglio in fette, via di produzione: **ogni fetta** porta ogni fonte per intero | intere |
| 5 | **IL DIFETTO PIANTATO, secondo verso**: una fetta a cui si sottrae meta' fonte | **DEGRADATA** |

⚠️ **Il caso 1 e' quello che rende gli altri qualcosa di piu' di una tautologia**: se il grezzo
finto smettesse di contenere la riga insidiosa, il caso 2 passerebbe per il motivo sbagliato e
nessuno se ne accorgerebbe.

Uso:
    python collaudo_taglio_fonti.py
Esce 0 se tutti i casi passano, 1 altrimenti.
"""
import io
import os
import re
import shutil
import sys
import tempfile

QUI = os.path.dirname(os.path.abspath(__file__))
QA = os.path.normpath(os.path.join(QUI, os.pardir))
sys.path.insert(0, QA)

import taglia_pacchetto as T  # noqa: E402

# Il testo insidioso: un grezzo che scrive righe della forma del vecchio delimitatore.
# ⚠️ NON e' inventato per il collaudo: e' la forma esatta che la notifica ATS del lotto 3F
# porta due volte, ed e' il motivo per cui il guasto e' stato trovato solo all'undicesimo lotto.
GREZZO_INSIDIOSO = u"""Da: protocollo.dip@pec.esempio.it
A: azienda@pec.it
Oggetto: preavviso

--- TESTO DELL'ATTO ALLEGATO ---

SI COMUNICA che in data 09/06/2026 avra' luogo il controllo ufficiale.
SENTINELLA_META_DOCUMENTO

--- FINE TESTO DELL'ATTO ---

Da: interno@azienda.it
Oggetto: I: preavviso
SENTINELLA_CODA_DOCUMENTO
"""

NOME_GREZZO = u"grezzo_con_delimitatori_interni.txt"
ALTRA_FONTE = u"altra_fonte_innocua.txt"
# ⚠️ Lunga apposta: la guardia di `taglia_pacchetto` scarta un'appendice sotto i 200
# caratteri, e una fonte-giocattolo la farebbe scattare per il motivo sbagliato.
TESTO_ALTRA = (u"Un documento che non contiene nessuna riga insidiosa.\n"
               u"Serve a dare alla seconda fetta una fonte propria, e a farlo con\n"
               u"abbastanza testo da non far scattare la guardia dei duecento\n"
               u"caratteri, che e' una soglia sulla lunghezza e non sulla completezza.\n"
               u"SENTINELLA_ALTRA\n")


def pacchetto_finto(sep_fonte):
    """Un pacchetto nella forma che `pacchetto_giudizio` produce, col delimitatore dato."""
    r = [u"PROMPT FINTO", u"=" * 70, u""]
    for nome, cita in ((u"nota-uno.md", NOME_GREZZO),
                       (u"nota-due.md", NOME_GREZZO),
                       (u"nota-tre.md", ALTRA_FONTE)):
        r.append(u"\n" + u"-" * 70)
        r.append(u"%s %s" % (T.SEP_NOTA, nome))
        r.append(u"-" * 70)
        r.append(u"corpo della nota, che cita %s nel blocco Fonti." % cita)
    r.append(u"\n\n" + u"=" * 70)
    r.append(T.TITOLO_APPENDICE)
    r.append(u"=" * 70)
    for nome, testo in ((ALTRA_FONTE, TESTO_ALTRA), (NOME_GREZZO, GREZZO_INSIDIOSO)):
        r.append(u"\n" + sep_fonte(nome))
        r.append(testo)
    return u"\n".join(r)


def spezza_alla_vecchia(testo):
    """LA VIA VECCHIA, riprodotta qui per essere provata rossa — e SOLO per quello.

    ⚠️ E' l'unico pezzo di logica che questo collaudo reimplementa, ed e' deliberato: la via
    vecchia non esiste piu' in produzione, quindi non si puo' chiamare. La via NUOVA invece si
    chiama, sempre (`T.spezza`), come T170 impone.
    """
    coda = testo.split(T.TITOLO_APPENDICE, 1)[1]
    fonti, nome, buf = {}, None, []
    for riga in coda.split(u"\n"):
        m = re.match(r"^--- (.+) ---$", riga)
        if m:
            if nome:
                fonti[nome] = u"\n".join(buf)
            nome, buf = m.group(1), []
        elif nome:
            buf.append(riga)
    if nome:
        fonti[nome] = u"\n".join(buf)
    return fonti


def main():
    esiti = []

    # --- 1. LA PREMESSA -------------------------------------------------------------
    ok1 = bool(re.search(r"^--- .+ ---$", GREZZO_INSIDIOSO, re.M))
    esiti.append((1, u"il grezzo finto porta davvero una riga della forma vecchia",
                  u"la riga c'e'", u"c'e'" if ok1 else u"NON c'e'", ok1))

    # --- 2. IL DIFETTO PIANTATO: la via vecchia tronca ------------------------------
    vecchie = spezza_alla_vecchia(pacchetto_finto(lambda n: u"--- %s ---" % n))
    troncata = vecchie.get(NOME_GREZZO, u"")
    ok2 = (u"SENTINELLA_META_DOCUMENTO" not in troncata
           and u"SENTINELLA_CODA_DOCUMENTO" not in troncata)
    esiti.append((2, u"la via VECCHIA tronca la fonte al primo delimitatore interno",
                  u"tronca", u"tronca (%d caratteri)" % len(troncata) if ok2 else u"NON tronca",
                  ok2))

    # --- 3. la via DI PRODUZIONE porta la fonte intera ------------------------------
    testo = pacchetto_finto(lambda n: u"%s %s" % (T.SEP_FONTE, n))
    _prologo, note, fonti = T.spezza(testo)
    intera = fonti.get(NOME_GREZZO, u"")
    ok3 = (u"SENTINELLA_META_DOCUMENTO" in intera
           and u"SENTINELLA_CODA_DOCUMENTO" in intera
           and len(fonti) == 2)
    esiti.append((3, u"la via DI PRODUZIONE porta la fonte intera, e non inventa fonti",
                  u"intera, 2 fonti", u"%d caratteri, %d fonti" % (len(intera), len(fonti)), ok3))

    # --- 4. il taglio in fette: ogni fetta porta ogni fonte per intero --------------
    tmp = tempfile.mkdtemp(prefix="collaudo_taglio_fonti_")
    ok4 = False
    try:
        with io.open(os.path.join(tmp, "pacchetto_giudizio_provenance.txt"),
                     "w", encoding="utf-8") as f:
            f.write(testo)
        sys.argv = ["taglia_pacchetto.py", "--report", tmp, "--fette", "2"]
        uscita = T.main()
        fette = sorted(x for x in os.listdir(tmp) if x.startswith("fetta_"))
        contenuti = [io.open(os.path.join(tmp, x), encoding="utf-8").read() for x in fette]
        # per ogni fetta, ogni fonte che la fetta DICHIARA dev'esserci PER INTERO
        completo = True
        for c in contenuti:
            for nome, testo_fonte in ((NOME_GREZZO, GREZZO_INSIDIOSO),
                                      (ALTRA_FONTE, TESTO_ALTRA)):
                if ("%s %s" % (T.SEP_FONTE, nome)) in c and testo_fonte.strip() not in c:
                    completo = False
        ok4 = (uscita == 0 and len(fette) == 2 and completo)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    esiti.append((4, u"ogni fetta porta per intero le fonti che le sue note citano",
                  u"intere", u"intere" if ok4 else u"MUTILATE", ok4))

    # --- 5. IL DIFETTO PIANTATO, secondo verso: la guardia sa diventare rossa -------
    # ⚠️ Senza questo caso il caso 4 proverebbe solo che una fetta buona passa, non che una
    # fetta mutilata viene fermata: e' la distinzione di §4.29.
    coda_mutilata = (u"\n%s %s\n%s" % (T.SEP_FONTE, NOME_GREZZO, GREZZO_INSIDIOSO[:120]))
    ok5 = GREZZO_INSIDIOSO not in coda_mutilata
    esiti.append((5, u"una fetta a cui si sottrae meta' fonte NON supera il confronto",
                  u"DEGRADATA", u"DEGRADATA" if ok5 else u"dichiarata completa", ok5))

    print(u"=" * 92)
    print(u"COLLAUDO - il delimitatore delle fonti non puo' comparire dentro un grezzo (E10, 2o delimitatore)")
    print(u"=" * 92)
    print(u"| # | Caso | Atteso | Avuto | Esito |")
    print(u"|---|---|---|---|---|")
    for i, nome, att, avuto, ok in esiti:
        print(u"| %d | %s | %s | %s | %s |" % (i, nome, att, avuto, u"OK" if ok else u"FALLITO"))
    falliti = [e for e in esiti if not e[4]]
    if falliti:
        print(u"\nCOLLAUDO FALLITO - %d casi su %d" % (len(falliti), len(esiti)))
        return 1
    print(u"\nCOLLAUDO SUPERATO - %d casi su %d." % (len(esiti), len(esiti)))
    print(u"I casi 2 e 5 sono i difetti piantati; il caso 1 e' la premessa che li rende veri.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
