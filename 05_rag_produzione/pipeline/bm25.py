# -*- coding: utf-8 -*-
"""
bm25.py — il ramo sparso, scritto a mano e non preso da una libreria.

Perche' a mano. Servono tre cose che nessuna libreria pronta dava insieme:
il tokenizzatore custom che non spezza i codici (metodo_04 §2), il controllo completo
sulle formule per poterle spiegare a voce davanti a un cliente, e la possibilita' di
ESPORTARE i pesi come vettori sparsi Qdrant. Il trucco e' che il prodotto scalare fra il
vettore sparso del documento e quello della domanda RESTITUISCE ESATTAMENTE il punteggio
BM25, quindi la ricerca lessicale gira dentro Qdrant come la ricerca densa e la
configurazione C ha davvero un indice solo.

Formula (BM25 nella variante di Lucene, quella con l'IDF sempre positivo):

    score(q,d) = SOMMA_su_t  IDF(t) * ( tf(t,d) * (k1+1) )
                             / ( tf(t,d) + k1 * (1 - b + b * |d| / avgdl) )
    IDF(t) = ln( 1 + (N - df(t) + 0.5) / (df(t) + 0.5) )

Il peso del documento porta tutto (IDF e saturazione), il peso della domanda vale 1 per
termine distinto: cosi' il prodotto scalare e' il punteggio, senza approssimazioni.
"""

import json
import math
from pathlib import Path

from pipeline.comune import tokenizza


class IndiceBM25:
    """Vocabolario, df e lunghezze: tutto cio' che serve a pesare un documento.

    Il vocabolario e' ordinato alfabeticamente e l'id di un termine e' la sua posizione:
    ricostruito dallo stesso corpus da' gli stessi id, che e' la condizione perche'
    l'indice sia riproducibile.
    """

    def __init__(self, k1, b):
        self.k1 = float(k1)
        self.b = float(b)
        self.vocabolario = []          # lista ordinata di termini
        self.id_di = {}                # termine -> id
        self.df = []                   # df per id
        self.n_doc = 0
        self.avgdl = 0.0

    # ---------------------------------------------------------------- costruzione

    @classmethod
    def costruisci(cls, testi, k1, b):
        idx = cls(k1, b)
        conteggi = []
        df_per_termine = {}
        lunghezze = []
        for t in testi:
            token = tokenizza(t)
            lunghezze.append(len(token))
            c = {}
            for tk in token:
                c[tk] = c.get(tk, 0) + 1
            conteggi.append(c)
            for tk in c:
                df_per_termine[tk] = df_per_termine.get(tk, 0) + 1

        idx.vocabolario = sorted(df_per_termine)
        idx.id_di = {t: i for i, t in enumerate(idx.vocabolario)}
        idx.df = [df_per_termine[t] for t in idx.vocabolario]
        idx.n_doc = len(testi)
        idx.avgdl = (sum(lunghezze) / len(lunghezze)) if lunghezze else 0.0
        return idx, conteggi, lunghezze

    # ---------------------------------------------------------------- pesi

    def idf(self, tid):
        df = self.df[tid]
        return math.log(1.0 + (self.n_doc - df + 0.5) / (df + 0.5))

    def vettore_documento(self, conteggi, lunghezza):
        """Vettore sparso di un documento: indici ordinati, valori = peso BM25."""
        norm = self.k1 * (1.0 - self.b + self.b * (lunghezza / self.avgdl if self.avgdl else 0.0))
        coppie = []
        for termine, tf in conteggi.items():
            tid = self.id_di.get(termine)
            if tid is None:
                continue
            coppie.append((tid, self.idf(tid) * (tf * (self.k1 + 1.0)) / (tf + norm)))
        coppie.sort()
        return [i for i, _ in coppie], [round(v, 6) for _, v in coppie]

    def vettore_domanda(self, domanda):
        """Vettore sparso di una domanda: 1.0 per termine distinto presente nel
        vocabolario. I termini mai visti si scartano: non avrebbero nessun documento."""
        tid = sorted({self.id_di[t] for t in tokenizza(domanda) if t in self.id_di})
        return tid, [1.0] * len(tid)

    # ---------------------------------------------------------------- persistenza

    def salva(self, percorso):
        Path(percorso).write_text(json.dumps({
            "k1": self.k1, "b": self.b, "n_doc": self.n_doc, "avgdl": self.avgdl,
            "vocabolario": self.vocabolario, "df": self.df,
        }, ensure_ascii=False), encoding="utf-8")

    @classmethod
    def carica(cls, percorso):
        d = json.loads(Path(percorso).read_text(encoding="utf-8"))
        idx = cls(d["k1"], d["b"])
        idx.vocabolario = d["vocabolario"]
        idx.id_di = {t: i for i, t in enumerate(idx.vocabolario)}
        idx.df = d["df"]
        idx.n_doc = d["n_doc"]
        idx.avgdl = d["avgdl"]
        return idx
