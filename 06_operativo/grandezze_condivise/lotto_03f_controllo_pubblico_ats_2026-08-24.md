# Grandezze condivise — lotto `lotto_03f_controllo_pubblico_ats`

> **Artefatto d'apertura di E2** (E60), generato da `06_operativo\grandezze_condivise.py`
> il **24/08/2026 alle 21:41**. ⚠️ **Dice DOVE guardare, non che cosa concludere**: se due
> documenti portano la stessa grandezza, vanno letti insieme — l'esito del confronto lo
> scrive il rapporto, uno per uno.

**1 grezzi nel lotto**: `notifica_ATS_ispezione_programmata_igiene.txt`

## A. Dentro il lotto — le grandezze che compaiono in più di un grezzo

**Nessuna.** ⚠️ Non è un esito neutro: un lotto i cui grezzi non condividono nessuna
grandezza è un lotto **senza riconciliazione orizzontale interna**, e il rapporto lo
dichiara invece di tacerlo.

**0 grandezze condivise fra i grezzi del lotto.**

## B. Fra il lotto e il vault — le grandezze che una nota già scritta porta già

⚠️ **È la metà che nessuno guardava**, e in 3B ha prodotto **sette divergenze su otto**.

| Genere | Grandezza | Nei grezzi | Le note del vault che la portano già |
|---|---|---|---|
| codice | `IO-05` | `notifica_ATS_ispezione_programmata_igiene.txt` | `fatto-abilitazione-obbligatoria-cip`, `fatto-abort-cip-per-soda-bassa`, `fatto-cicli-cip-chiusi-con-sonda-guasta`, `fatto-cicli-cip-maggio`, `fatto-cip-fuori-criterio`, `fatto-criterio-conducibilita-cip-superato`, `fatto-impianto-haccp-verificato-in-audit`, `fatto-nc-26-018-ruote-carrelli-febbraio` … e altre 28 |
| codice | `MD-3200` | `notifica_ATS_ispezione_programmata_igiene.txt` | `area-manutenzione`, `area-qualita`, `fatto-allarme-acustico-md-3200-basso`, `fatto-carica-in-salita-linea-1-aprile`, `fatto-ccp-stato-al-riesame-2026`, `fatto-ccp3-non-in-causa-sul-frammento`, `fatto-convalida-md-1800-scaduta`, `fatto-due-registri-paralleli-della-metrologia` … e altre 27 |
| codice | `MOD-QA-07` | `notifica_ATS_ispezione_programmata_igiene.txt` | `area-qualita`, `fatto-allarme-acustico-md-3200-basso`, `fatto-ccp3-non-in-causa-sul-frammento`, `fatto-chiusura-nc-documentale-e-il-richiamo`, `fatto-formazione-2025-sotto-obiettivo`, `fatto-giro-di-vite-seconde-firme-ccp3`, `fatto-impianto-haccp-verificato-in-audit`, `fatto-nc1-seconde-firme-undici-moduli-su-venti` … e altre 19 |
| codice | `MOD-QA-12` | `notifica_ATS_ispezione_programmata_igiene.txt` | `area-qualita`, `fatto-allarme-acustico-md-3200-basso`, `fatto-chiusura-nc-documentale-e-il-richiamo`, `fatto-datalogger-dl-001-in-taratura`, `fatto-deviazione-ccp2-l26130`, `fatto-evidenze-audit-oltre-termine`, `fatto-impianto-haccp-verificato-in-audit`, `fatto-nc1-seconde-firme-undici-moduli-su-venti` … e altre 18 |
| codice | `MOD-HR-11` | `notifica_ATS_ispezione_programmata_igiene.txt` | `area-risorse-umane`, `fatto-abilitazione-obbligatoria-cip`, `fatto-chiusura-nc-documentale-e-il-richiamo`, `fatto-firma-registro-formazione-all-ingresso`, `fatto-formazione-2025-sotto-obiettivo`, `fatto-formazione-allergeni-registrata-biennale`, `fatto-mani-addetto-farcitura-non-conforme`, `fatto-operatore-senza-formazione-haccp-l26130` … e altre 9 |
| data | `09/06/2026` | `notifica_ATS_ispezione_programmata_igiene.txt` | `fatto-cloro-residuo-ghiaccio-in-calo`, `fatto-due-sessioni-formative-programmate-per-il-09-06`, `fatto-impianto-haccp-verificato-in-audit`, `fatto-ispezione-ats-carrello-ricambi`, `fatto-registro-formazione-intestazione-ripetuta`, `questione-carrello-ricambi-dichiarato-rimosso`, `questione-posizione-md-3200-in-linea`, `questione-taratura-termoregistratore-cf-02` |
| data | `25/05/2026` | `notifica_ATS_ispezione_programmata_igiene.txt` | `fatto-date-in-quattro-grafie-registro-tamponi`, `fatto-lettura-mancante-registro-tamponi`, `fatto-listeria-scarico-pt-104-aprile`, `fatto-nc-26-055-nastro-forno-maggio`, `fatto-nc-26-056-ganasce-pkm-450-maggio`, `questione-frequenza-tamponi-prescritta-e-reale`, `kpi-tamponi-superfici-2026` |
| numero | `37044` | `notifica_ATS_ispezione_programmata_igiene.txt` | `self-certificazioni`, `doc-pro-qa-08`, `doc-pro-qa-14`, `entita-veneta-energia` |
| numero | `1.000,00` | `notifica_ATS_ispezione_programmata_igiene.txt` | `doc-indicatori-reclami`, `questione-reclami-per-confezioni-o-per-pezzi` |
| numero | `0442` | `notifica_ATS_ispezione_programmata_igiene.txt` | `entita-elena-marchetti` |
| numero | `193` | `notifica_ATS_ispezione_programmata_igiene.txt` | `fatto-test-rintracciabilita-audit-2h50` |
| ora | `8:30` | `notifica_ATS_ispezione_programmata_igiene.txt` | `entita-chemifood-italia` |

**12 grandezze del lotto sono già nel vault**, su 25 estratte.

## C. Le entità che il vault già conosce, nominate dai grezzi del lotto

⚠️ **Sono le porte del grafo**: una scheda entità già scritta è il posto in cui la
divergenza fra il lotto e il vault diventa visibile — ed è dove va aggiornata.

| Entità nominata | Scheda nel vault | In quali grezzi |
|---|---|---|
| Analytica Veneta | `entita-analytica-veneta` | `notifica_ATS_ispezione_programmata_igiene.txt` |
| Elena Marchetti | `entita-elena-marchetti` | `notifica_ATS_ispezione_programmata_igiene.txt` |
| Federica | `entita-federica-sartori` | `notifica_ATS_ispezione_programmata_igiene.txt` |
| Ivano | `entita-ivano-dal-maso` | `notifica_ATS_ispezione_programmata_igiene.txt` |
| MD-3200 | `macchina-md-3200` | `notifica_ATS_ispezione_programmata_igiene.txt` |
| Vicentini | `entita-chiara-vicentini` | `notifica_ATS_ispezione_programmata_igiene.txt` |
| analytica | `entita-analytica-veneta` | `notifica_ATS_ispezione_programmata_igiene.txt` |
| dott.ssa Elena Marchetti | `entita-elena-marchetti` | `notifica_ATS_ispezione_programmata_igiene.txt` |
| e.marchetti@aurorafoodgroup.it | `entita-elena-marchetti` | `notifica_ATS_ispezione_programmata_igiene.txt` |
| f.sartori | `entita-federica-sartori` | `notifica_ATS_ispezione_programmata_igiene.txt` |
| team leader HACCP | `entita-elena-marchetti` | `notifica_ATS_ispezione_programmata_igiene.txt` |

**11 entità del vault sono nominate dai grezzi del lotto.**
