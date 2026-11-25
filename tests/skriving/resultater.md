# Resultater fra skrivetestene, 2026-11-23

> **TEST.** Virksomhetene og tallene i bestillingene er oppdiktet.

Seks bestillinger ([bestillinger.md](bestillinger.md)) ble skrevet av Amalie 0.12 og 1.0. En blind dommer, en egen agent som ikke visste hvilken versjon som skrev hva, ga hver tekst 1–5 poeng på fem punkter: leseren, om teksten høres naturlig ut, én mening, sant og lengde. Tekstene ligger i [ut-0.12/](ut-0.12/) og [ut-1.0/](ut-1.0/).

## Hvilken tekst dommeren foretrakk

| Bestilling | Runde 1 (1.0 før rettelser) | Runde 2 (1.0) |
|---|---|---|
| S1 Infoside, parkering | 0.12 | 0.12 |
| S2 Skjema, kontonummer | 0.12 | 1.0 |
| S3 E-post, senteret stenger | 1.0 | 1.0 |
| S4 Nyhet, bibliotek | 1.0 | 1.0 |
| S5 Notat til leder | 1.0 | 1.0 |
| S6 Metabeskrivelser | 1.0 | 0.12 (likt i poeng) |
| **1.0 foretrukket** | **4 av 6** | **4 av 6** |

## Poeng

| | 0.12 | 1.0 |
|---|---|---|
| Runde 1, dommer 1 | 128 | 129 |
| Runde 2, dommer 2 | 123 | 128 |

Tekstene fra 0.12 var de samme i begge rundene, men dommerne ga dem 128 og 123 poeng. Forskjellen mellom to dommere er altså større enn forskjellen mellom versjonene. Seks tester med én dommer kan ikke vise at 1.0 skriver bedre enn 0.12. De viser at 1.0 skriver minst like godt, med en mer generell og kortere kjerne.

## Mønstre dommerne fant i begge versjonene

1. **Små tillegg utenfor premissarket.** Skribenten legger til det som virker rimelig, for eksempel hvor kunden finner kontonummeret. G7 er gjort tydeligere etter runde 2.
2. **Det leseren lurer mest på, kommer sent.** Svaret om boten kommer etter stegene for å søke.
3. **Korte uttrykk som kan leses på to måter, og ting som står to ganger.**

Etter runde 1 ble G1, G5, G9, E11 og selvgjennomgangen styrket med eksempler fra andre områder enn testene.

## Gjennomgangstestene

17 av 17 besto med 1.0 ([cases.tsv](../cases.tsv)). Testene er lette, fordi hver tekst har ett tydelig brudd. De viser at reglene fanger bruddene, men ikke om gjennomgangen holder seg unna tvilsomme funn i lange tekster.

## Det testsettet trenger før neste versjon

- Minst 12 skrivebestillinger, også lange tekster.
- To dommere med ulike roller, for eksempel en språkrådgiver og en leser fra målgruppen. Snittet av de to avgjør.
- Tre lange tekster i gjennomgangstestene, med flere brudd og flere gode setninger.
- Eksempler i reglene hentes aldri fra testene.
