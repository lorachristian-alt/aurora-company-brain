# -*- coding: utf-8 -*-
"""
collaudo.py — il collaudo di FUNZIONAMENTO della catena, non di qualita'.

Dieci domande scritte a mano leggendo `02_corpus\\`. **Nessuna viene dall'eval set**, che
questa sessione non ha mai visto e non vedra' mai. Servono a verificare che i pezzi
girino: che i due rami tornino candidati, che la fusione li unisca, che il reranker
riordini, che il generatore risponda e citi, e che ogni formato dell'archivio sia
raggiungibile — compreso il .jpg passato dall'OCR.

⚠️ REGOLA DI QUESTO FILE, e vale piu' del file stesso.
Se il collaudo rivela un DIFETTO — un crash, un formato non letto, la fusione che non
fonde — si corregge il codice e lo si annota. Se il collaudo fa venire voglia di
CAMBIARE UN PARAMETRO, la risposta e' no: la configurazione e' congelata e committata
prima di questo passo, e un parametro spostato guardando dei risultati e' esattamente
cio' che rende una misura non credibile. Si segnala al gate e si va avanti.

Il campo `atteso` non e' una risposta corretta: e' il file che una persona si aspetta di
veder tornare da quella ricerca. Un `atteso` mancato si scrive nel rapporto e basta.

Uso:
    python pipeline\\collaudo.py --solo-recupero     # non serve Ollama
    python pipeline\\collaudo.py --solo-generazione  # rilegge le tracce e genera
    python pipeline\\collaudo.py                     # catena intera, in un colpo

⚠️ Sui TEMPI, e non e' un dettaglio. `--solo-recupero` e `--solo-generazione` misurano
le stesse condizioni delle passate del runner: un solo protagonista in memoria. La
catena intera in un colpo tiene invece embedder, reranker e Ollama vivi insieme, e su 8
GB di RAM i suoi tempi dicono quanto pagina la macchina, non quanto costa la pipeline.
Per il verbale valgono i due tempi separati; quello intero serve solo a dimostrare che
la catena gira dall'inizio alla fine.
"""

import argparse
import json
import sys
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pipeline import comune                                        # noqa: E402
from pipeline.interroga import (Generatore, Recupero, costruisci_prompt,  # noqa: E402
                                estrai_campi)

DOMANDE = [
    {"n": 1, "che_prova": "ramo sparso su codice di lotto",
     "domanda": "Quanti chili di prodotto finito riporta il mass balance del lotto L26130?",
     "atteso": "tracciabilita_lotti_massbalance_L26130.xlsx"},
    {"n": 2, "che_prova": "ramo denso, nessun codice nella domanda",
     "domanda": "Che cosa ha stabilito il laboratorio esterno sul frammento rigido trovato dal cliente?",
     "atteso": "Rapporto_di_Prova_AnalyticaVeneta_2026_04187.pdf"},
    {"n": 3, "che_prova": "formato .log, dato numerico in serie",
     "domanda": "Quali temperature ha registrato il pastorizzatore della linea 1 il 10 maggio 2026?",
     "atteso": "log_temperature_pastorizzatore_linea1_10_05_26.log"},
    {"n": 4, "che_prova": "codice con trattino non spezzato dal tokenizzatore",
     "domanda": "Che cosa dice il certificato di analisi del lotto di farina MV26-0429A?",
     "atteso": "certificato_analisi_lotto_farina_MV26_0429A.pdf"},
    {"n": 5, "che_prova": "codice prodotto con due trattini",
     "domanda": "Quali sono le caratteristiche del prodotto AF-SN-0450 secondo la sua scheda tecnica?",
     "atteso": "Scheda_tecnica_prodotto_AF-SN-0450_rev4.pdf"},
    {"n": 6, "che_prova": "formato .eml e catena di risposte",
     "domanda": "Quando scade il certificato BRCGS e quando e' previsto l'audit di rinnovo?",
     "atteso": "R_R_R_scadenza_certificato_BRCGS_e_audit_di_rinnovo.eml"},
    {"n": 7, "che_prova": "formato .docx",
     "domanda": "Quali allergeni sono soggetti a rischio di cross contamination secondo la matrice aziendale?",
     "atteso": "scheda_allergeni_matrice_cross_contamination.docx"},
    {"n": 8, "che_prova": "formato .jpg passato dall'OCR",
     "domanda": "Che cosa riporta il modulo MOD-QA-07 compilato il 10-05-26 sulla linea 1 turno 2?",
     "atteso": "MOD-QA-07_10-05-26_L1_T2_scansione.jpg"},
    {"n": 9, "che_prova": "formato .xml di fattura elettronica, partita IVA nel nome",
     "domanda": "Qual e' la partita IVA di Aurora Food Group e in quali fatture elettroniche compare?",
     "atteso": None},
    {"n": 10, "che_prova": "formato .xlsx con piu' fogli, domanda di aggregazione",
     "domanda": "Quali referenze hanno la marginalita' piu' bassa nell'analisi 2026?",
     "atteso": "analisi_marginalita_per_referenza_2026.xlsx"},
]


def solo_generazione(cfg, uscita, impronta):
    """Rilegge le tracce del recupero e genera: in memoria c'e' solo Ollama, cioe' le
    stesse condizioni della passata 2 del runner. E' da qui che esce la stima onesta
    dei tempi della generazione."""
    gen = Generatore(cfg)
    ok, info = gen.disponibile()
    if not ok:
        sys.exit("Ollama: %s" % (info,))
    print("Ollama: %s disponibile" % cfg["generazione"]["modello"])

    esiti = []
    for d in DOMANDE:
        f = uscita / "tracce" / ("collaudo_%02d.json" % d["n"])
        if not f.exists():
            sys.exit("manca %s: lancia prima --solo-recupero" % f.name)
        tr = json.loads(f.read_text(encoding="utf-8"))
        pas = tr["passaggi_consegnati"]
        out = gen.genera(costruisci_prompt(d["domanda"], pas, cfg))
        risposta, fonti, conf, fuori = estrai_campi(out["testo"], pas)
        tr["generazione"] = dict(out, fonti_citate=fonti, fonti_fuori_contesto=fuori,
                                 confidenza=conf)
        tr["config_c"] = impronta
        f.write_text(json.dumps(tr, ensure_ascii=False, indent=1), encoding="utf-8")
        esiti.append({"n": d["n"], "che_prova": d["che_prova"],
                      "secondi_generazione": out["secondi"],
                      "token_prompt": out["token_prompt"],
                      "token_risposta": out["token_risposta"],
                      "fonti_citate": fonti, "fonti_fuori_contesto": fuori,
                      "confidenza": conf, "risposta_vuota": not bool(risposta),
                      "caratteri_risposta": len(risposta)})
        print("[%2d] %-46s  %6.1fs  %5s token prompt  %4s uscita  fonti %d%s"
              % (d["n"], d["che_prova"], out["secondi"], out["token_prompt"],
                 out["token_risposta"], len(fonti),
                 "  ⚠ FUORI CONTESTO" if fuori else ""))

    t = [e["secondi_generazione"] for e in esiti]
    tp = [e["token_prompt"] for e in esiti if e["token_prompt"]]
    rapporto = {
        "quando": datetime.now().isoformat(timespec="seconds"),
        "config_c": impronta,
        "fase": "solo generazione (condizioni della passata 2)",
        "domande": len(esiti),
        "secondi_medi": round(sum(t) / len(t), 2),
        "secondi_min": round(min(t), 2), "secondi_max": round(max(t), 2),
        "stima_282_ore": round(sum(t) / len(t) * 282 / 3600, 2),
        "token_prompt_max": max(tp) if tp else None,
        "num_ctx": cfg["generazione"]["num_ctx"],
        "risposte_vuote": sum(1 for e in esiti if e["risposta_vuota"]),
        "risposte_senza_fonti": sum(1 for e in esiti if not e["fonti_citate"]),
        "risposte_con_fonti_fuori_contesto": sum(1 for e in esiti
                                                 if e["fonti_fuori_contesto"]),
        "esiti": esiti,
    }
    (uscita / "rapporto_generazione.json").write_text(
        json.dumps(rapporto, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n--- sonda della generazione (solo Ollama in memoria) ---")
    print("medio %.1fs (min %.1f max %.1f)  ->  282 domande = %.2f h"
          % (rapporto["secondi_medi"], rapporto["secondi_min"],
             rapporto["secondi_max"], rapporto["stima_282_ore"]))
    print("token del prompt piu' lungo: %s su num_ctx %d"
          % (rapporto["token_prompt_max"], rapporto["num_ctx"]))
    print("risposte vuote %d · senza fonti %d · con fonti fuori contesto %d"
          % (rapporto["risposte_vuote"], rapporto["risposte_senza_fonti"],
             rapporto["risposte_con_fonti_fuori_contesto"]))
    print("scritto %s" % (uscita / "rapporto_generazione.json"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-recupero", action="store_true")
    ap.add_argument("--solo-generazione", action="store_true")
    ap.add_argument("--uscita", default=None)
    a = ap.parse_args()
    sys.stdout.reconfigure(line_buffering=True)

    cfg = comune.carica_config()
    from pipeline.impronta import impronta_config
    impronta = impronta_config(cfg)
    comune.fissa_thread(cfg)

    uscita = Path(a.uscita or (comune.BASE / "collaudo"))
    (uscita / "tracce").mkdir(parents=True, exist_ok=True)

    if a.solo_generazione:
        return solo_generazione(cfg, uscita, impronta)

    gen = None
    if not a.solo_recupero:
        gen = Generatore(cfg)
        ok, info = gen.disponibile()
        if not ok:
            sys.exit("Ollama: %s\n(usa --solo-recupero per collaudare la sola catena "
                     "di recupero)" % (info,))

    rec = Recupero(cfg)
    esiti = []
    try:
        for d in DOMANDE:
            t0 = time.time()
            tr = rec.recupera(d["domanda"])
            file_finali = [p["file"] for p in tr["passaggi_consegnati"]]
            file_rrf = []
            for x in tr["fusione_rrf"]:
                if x["file"] not in file_rrf:
                    file_rrf.append(x["file"])
            e = {
                "n": d["n"], "che_prova": d["che_prova"], "domanda": d["domanda"],
                "atteso": d["atteso"],
                "atteso_nei_passaggi": (d["atteso"] in file_finali) if d["atteso"] else None,
                "atteso_nella_rrf": (d["atteso"] in file_rrf) if d["atteso"] else None,
                "candidati_densi": len(tr["candidati_densi"]),
                "candidati_sparsi": len(tr["candidati_sparsi"]),
                "candidati_fusi": len(tr["fusione_rrf"]),
                "solo_denso": sum(1 for x in tr["fusione_rrf"] if x["rango_sparso"] is None),
                "solo_sparso": sum(1 for x in tr["fusione_rrf"] if x["rango_denso"] is None),
                "in_entrambi": sum(1 for x in tr["fusione_rrf"]
                                   if x["rango_denso"] is not None
                                   and x["rango_sparso"] is not None),
                "file_consegnati": file_finali,
                "origini": sorted({p["origine"] for p in tr["passaggi_consegnati"]}),
                "caratteri_contesto": tr["caratteri_contesto"],
                "tempi_recupero": tr["tempi"],
                "secondi_recupero": round(time.time() - t0, 2),
            }
            if gen is not None:
                out = gen.genera(costruisci_prompt(d["domanda"],
                                                   tr["passaggi_consegnati"], cfg))
                risposta, fonti, conf, fuori = estrai_campi(
                    out["testo"], tr["passaggi_consegnati"])
                tr["generazione"] = dict(out, fonti_citate=fonti,
                                         fonti_fuori_contesto=fuori, confidenza=conf)
                e.update(secondi_generazione=out["secondi"],
                         token_prompt=out["token_prompt"],
                         token_risposta=out["token_risposta"],
                         fonti_citate=fonti, fonti_fuori_contesto=fuori,
                         confidenza=conf, risposta_vuota=not bool(risposta))
            tr.update(collaudo=d["n"], config_c=impronta)
            (uscita / "tracce" / ("collaudo_%02d.json" % d["n"])).write_text(
                json.dumps(tr, ensure_ascii=False, indent=1), encoding="utf-8")
            esiti.append(e)
            print("[%2d] %-46s  rrf %2d (d %2d / s %2d / entrambi %2d)  atteso: %s  %5.1fs"
                  % (d["n"], d["che_prova"], e["candidati_fusi"], e["solo_denso"],
                     e["solo_sparso"], e["in_entrambi"],
                     "-" if d["atteso"] is None else
                     ("SI" if e["atteso_nei_passaggi"] else
                      ("rrf" if e["atteso_nella_rrf"] else "NO")),
                     e["secondi_recupero"] + e.get("secondi_generazione", 0)))
    finally:
        rec.chiudi()

    con_atteso = [e for e in esiti if e["atteso"]]
    rapporto = {
        "quando": datetime.now().isoformat(timespec="seconds"),
        "config_c": impronta,
        "domande": len(esiti),
        "atteso_nei_passaggi": sum(1 for e in con_atteso if e["atteso_nei_passaggi"]),
        "atteso_almeno_nella_rrf": sum(1 for e in con_atteso if e["atteso_nella_rrf"]),
        "con_atteso": len(con_atteso),
        "formati_toccati": sorted({f.rsplit(".", 1)[-1].lower()
                                   for e in esiti for f in e["file_consegnati"]}),
        "origini_toccate": sorted({o for e in esiti for o in e["origini"]}),
        "secondi_recupero_medi": round(sum(e["secondi_recupero"] for e in esiti)
                                       / len(esiti), 2),
        "esiti": esiti,
    }
    if not a.solo_recupero:
        rapporto["secondi_generazione_medi"] = round(
            sum(e["secondi_generazione"] for e in esiti) / len(esiti), 2)
    (uscita / "rapporto_collaudo.json").write_text(
        json.dumps(rapporto, ensure_ascii=False, indent=1), encoding="utf-8")

    print("\n--- collaudo ---")
    print("atteso fra i passaggi consegnati: %d/%d (nella sola RRF: %d/%d)"
          % (rapporto["atteso_nei_passaggi"], rapporto["con_atteso"],
             rapporto["atteso_almeno_nella_rrf"], rapporto["con_atteso"]))
    print("formati toccati: %s" % ", ".join(rapporto["formati_toccati"]))
    print("origini toccate: %s" % ", ".join(rapporto["origini_toccate"]))
    print("recupero medio: %.1fs" % rapporto["secondi_recupero_medi"])
    if not a.solo_recupero:
        print("generazione media: %.1fs" % rapporto["secondi_generazione_medi"])
    print("scritto %s" % (uscita / "rapporto_collaudo.json"))


if __name__ == "__main__":
    main()
