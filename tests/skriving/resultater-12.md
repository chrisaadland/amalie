# Resultater fra den store skrivetesten, 2026-11-23

> **TEST.** Virksomhetene og tallene i bestillingene er oppdiktet.

Tolv bestillinger ([bestillinger-12.md](bestillinger-12.md)) i offentlig, privat og ideell sektor. Amalie 0.12 og 1.0 skrev alle tolv. Fire blinde dommere, hver med sitt fagfelt, ga alle 24 tekstene en karakter fra 1 til 10. Tekstene ligger i [ut12-0.12/](ut12-0.12/) og [ut12-1.0/](ut12-1.0/).

## Resultat: 0.12 skriver bedre enn 1.0

| Dommer | Sum 0.12 | Sum 1.0 | Foretrakk 0.12 | Foretrakk 1.0 |
|---|---|---|---|---|
| Klarspråk, Språkrådet | 94,5 | 85,5 | 10 | 2 |
| Innholdsdesign, NAV og Skatteetaten | 97,5 | 83 | 11 | 1 |
| Innholdsdesign, GOV.UK | 91 | 85 | 8 | 4 |
| Stemme og tone, Mailchimp og Monzo | 92 | 76 | 11 | 1 |

Når karakterene fra alle fire legges sammen per bestilling, vinner 0.12 i 10 av 12. 1.0 vinner én (P2), og én er uavgjort (I1).

Tekstene fra 1.0 har 1991 ord til sammen, og tekstene fra 0.12 har 3039. Dommerne trakk 1.0 for å ha strøket det leseren trengte, for å sette en markør der leseren ventet et svar, og for å være tørr.

Den lille testen med seks bestillinger og én dommer ([resultater.md](resultater.md)) viste det motsatte. Den testen var for liten.

## Hva alle fire dommerne var enige om

1. **Passiv i feilmeldinger er feil.** «Mobilnummer må fylles ut» skal være «Skriv inn mobilnummeret ditt». En bydeform legger heller ikke skylden på brukeren.
2. **Kravet om bindeord gir tvungne «fordi»- og «så»-setninger.** Eksempel: «Da kan du sykle i tre måneder før du bestemmer deg, fordi du kan si opp abonnementet etter det.» Bindeord skal stå der sammenhengen finnes. Ellers er det bedre å dele setningen.
3. **Det samme står to eller tre ganger.** Det skjer i begge versjonene, selv om regelen finnes.
4. **«Hvert poeng ett sted» og «ville leseren savnet den?» er for strenge.** Sikkerhetsinformasjon som «ring 113» og hovedhandlingen skal stå både øverst og der leseren handler. Setninger som takker eller viser forståelse, gjør en jobb, og blir strøket når regelen brukes mekanisk.
5. **«Vis det med en person i en situasjon» gir oppdiktede scener**, for eksempel en treåring i barnesetet klokka halv åtte. Det strider mot regelen om å skrive sant.

## Det dommerne savnet i reglene

| Dommer | Savnet |
|---|---|
| Språkrådet | Ordstilling (verb og preposisjon nær hverandre, ingen løse ledd til slutt). Hvem «du» er når leseren handler for en annen. Ordriktighet. Dårlige nyheter: beklag én gang, uten å anta noe. |
| NAV og Skatteetaten | Feilmeldinger som sier hva brukeren gjør. Faste deler i vedtak (saksnummer, dato, klagefrist som dato). Vis forståelse uten å gjette. Tilpass teksten til kanalen. Skriv det du vet, og sett markøren bare på det som mangler. |
| GOV.UK | Én påstand per setning, også under 25 ord. Handlingen i de første ordene. Knappetekst. Publiseringsdato på varsler. |
| Mailchimp og Monzo | Si hvordan leseren har det når mye står på spill. Én tydelig oppfordring tidlig og til slutt. Stemmen varierer med kanalen. Lov med fragmenter og rytme i sosiale medier. Svar på «hva får jeg ut av det?». |

## Det vi lærte om testing

- Seks tester med én dommer ga feil konklusjon. Tolv tester med fire dommere snudde den.
- Kortere er ikke det samme som bedre. Dommerne ville ha fullstendige svar på det leseren lurer på.

## Runde 2: etter rettelsene

Reglene ble rettet etter det dommerne var enige om. 1.0 skrev de tolv tekstene på nytt ([ut12-1.0-rettet/](ut12-1.0-rettet/)). Fire nye dommere med de samme rollene sammenlignet dem blindt med de samme tekstene fra 0.12.

| Dommer | Sum 0.12 | Sum 1.0 rettet | Foretrakk 0.12 | Foretrakk 1.0 |
|---|---|---|---|---|
| Språkrådet | 97 | 81 | 10 | 1 |
| NAV og Skatteetaten | 98 | 83,5 | 10 | 2 |
| GOV.UK | 94 | 89 | 8 | 4 |
| Mailchimp og Monzo | 90 | 73 | 10 | 2 |

Samlet vinner 0.12 i 9 av 12, 1.0 i én (O3, grensesnitt), og to er uavgjort. Rettelsene hjalp ikke. Tekstene fra 1.0 var fortsatt omtrent en tredjedel kortere (1931 ord mot 3039).

Det dommerne pekte på denne gangen:
- «Én påstand per setning» i G3 gir telegramstil (tre av fire dommere).
- «Vis én gang at du forstår» i G1 blir en fast frase: «Vi forstår at du hadde håpet på et annet svar.»
- Tekster som skal få noen til å gi, kjøpe eller melde seg, mangler et bilde og en grunn til å handle.
- Frister bør stå som datoer, og teksten bør si hva som skjer etterpå.

Konklusjon: Det som gjør 0.12 bedre, ligger i hele regelsettet og arbeidsflyten til 0.12, ikke i enkeltregler som kan rettes én for én.

## Runde 3: 1.0 bygget på reglene fra 0.12

Reglene fra 0.12 ble hentet tilbake. Endringene: kundene er tatt ut, eksemplene er nøytrale, feilmeldingene er aktive, og selvgjennomgangen følger tekstens lengde. Tekstene ligger i [ut12-1.0-fra-0.12/](ut12-1.0-fra-0.12/).

| Dommer | Sum 0.12 | Sum 1.0 fra 0.12 | Foretrakk 0.12 | Foretrakk 1.0 | Foretrakk tekst A |
|---|---|---|---|---|---|
| Språkrådet | 91,5 | 87,5 | 7 | 5 | 12 av 12 |
| NAV og Skatteetaten | 94 | 81 | 9 | 3 | 10 av 12 |
| GOV.UK | 92 | 87 | 7 | 5 | 12 av 12 |
| Mailchimp og Monzo | 85 | 70 | 9 | 2 | 9 av 12 |

0.12 får fortsatt høyest karakter, men avstanden er mindre enn i runde 1 og 2.

**Resultatet er usikkert av to grunner:**
1. Dommerne foretrakk tekst A i 9–12 av 12 bestillinger. Hvilken versjon som var A, ble trukket tilfeldig. Rekkefølgen styrte dommerne. I runde 1 skjedde ikke dette.
2. Reglene i 1.0 er nesten de samme som i 0.12, men tekstene ble likevel 30 % kortere (2142 ord mot 3039). Vi har bare én kjøring av 0.12. Den kan ha vært en heldig kjøring.

**Det som trengs for å vite sikkert:** en test der 0.12 skriver de tolv tekstene på nytt og sammenlignes med sin egen første kjøring. Er forskjellen like stor der, måler testen tilfeldig variasjon og ikke versjonen. Dommerne bør også se hvert par i begge rekkefølger.
