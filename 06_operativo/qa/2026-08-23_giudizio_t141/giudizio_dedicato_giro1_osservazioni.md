# Giudizio DEDICATO alle due note di T141 — primo giro

> **E58, primo impiego.** Le due note erano nate dai ritrovamenti del terzo giro del lotto 3C e
> avevano passato QA e controllo delle citazioni **senza mai vedere lo strato di giudizio**.
> Subagente a contesto pulito, senza canone, pacchetto generato dopo la QA (E33).
> **Misura del 23/08/2026.**

**Esito: 2 note su 2 `afferma_oltre`.** Il verdetto in `giudizio_dedicato_giro1.jsonl`.

## Lacune di copertura segnalate

- `fatto-due-nc-interne-sul-proprio-ritardo` → `verbale_riesame_direzione_SGQ_2026.txt` (nel
  pacchetto come fonte dell'altra nota): §3.3 porta il termine dei 28 giorni e l'annotazione a
  margine «evidenze poi trasmesse a CSQA in data 02/04/2026, oltre il termine — v. NC-2026-049 e
  NC-2026-061», di cui la nota parlava per via indiretta.
- `fatto-due-nc-interne-sul-proprio-ritardo` → `Rilievo_Audit_BRC_IFS_CSQA_febbraio2026.txt`: la
  sezione 6 misura lo stesso ritardo **dal lato dell'ente**, con la «NOTA CSQA (Franceschini N.,
  03/04/2026)» che la nota commentava senza averla fra le fonti.
- `questione-vendor-rating-2025-c-e-o-non-c-e` → `non_conformita_interne_registro_2026.csv`:
  registra gli eventi che il verbale usa come motivazione delle classi — `NC-2026-023` del
  10/02/2026 su Flexipack, `NC-2026-032` del 20/02/2026 su Euroglass, `NC-2026-011` del
  21/01/2026 su Latteria Bassanese.

⚠️ **Le tre segnalazioni sono RESPINTE come motivo di riscrittura, e accolte come conferma della
correzione fatta.** Il giudice non conosce il grafo (§9.5 passo 5): i fatti che indica hanno già
la loro nota padrona — `fatto-evidenze-audit-oltre-termine` e `fatto-grade-aa-messo-in-guardia` —
e la correzione applicata **rimanda a quelle invece di aggiungere le fonti**, che è ciò che E40
prescrive. Aggiungerle avrebbe creato due doppie padrone.

## Osservazioni minori, e che cosa se n'è fatto

| Osservazione | Esito |
|---|---|
| `NC-2026-049` risulta **CHIUSA il 02/04/2026** nel registro, e la tabella della nota portava «—»; la citazione della riga 51 si fermava prima dei campi azione correttiva, responsabile, data e stato | **accolta** — tabella corretta, citazione estesa a tutta la riga |
| «Aurora conta SEDICI giorni di ritardo, **e lo mette a verbale**» — il sedici sta nel registro `MOD-QA-18 rev.3`, non in un verbale | **accolta** — «lo scrive nel proprio registro» |
| «Responsabile di entrambe: Marchetti E., **cioè la persona il cui ritardo le non conformità registrano**» — il campo dichiara chi risponde, non chi ha causato, e la causa radice chiama in causa anche i capiturno | **accolta** — la distinzione è ora scritta |
| «un esito che l'ente **non ha mai scritto in quei termini**» — negativo universale su ciò che l'ente ha scritto, non verificabile dal CSV | **accolta** — ristretto a ciò che il registro riporta |
| «il rilievo è infondato, **e nessuno lo ha contestato**» — affermazione dal silenzio, e il rapporto va nel verso opposto | **accolta** — sostituita col dato: «Azione correttiva proposta… Stato: APERTA» |
| «Una valutazione dell'anno 2025 non poteva contenerlo» è categorica ma dichiarata come indizio non decisivo nel capoverso successivo | **respinta** — inferenza dichiarata, che il prompt esenta |

## ⚠️ Un difetto trovato per strada, e corretto

`fatto-evidenze-audit-oltre-termine` portava `non_conformita_interne_registro_2026.csv`
**due volte** nell'elenco `fonti`. Correzione soppressiva, nessuna affermazione toccata; la nota
è entrata nel perimetro di QA di questo giudizio (E32).
