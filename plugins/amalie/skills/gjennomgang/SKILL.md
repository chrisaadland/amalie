---
name: gjennomgang
description: Amalies gjennomgangsmodus. Går gjennom en tekst som allerede finnes – en nettadresse, en skjermdump, en fil, kode eller innlimt tekst – og lister hvert brudd på Amalies grunnregler, sortert etter alvorlighet, med hvor det står, regelen skrevet ut og et forslag. Bruk når noen skriver «Amalie, se over denne», «gå gjennom teksten», «sjekk denne siden», «review», «hva er galt med denne teksten», eller limer inn en tekst, skjermdump eller URL og vil ha den vurdert. Vil brukeren ha teksten rettet direkte, bruk amalie:rediger.
---

# Gjennomgang

Gjennomgangen finner bruddene på grunnreglene i en tekst som allerede finnes. Den lister hva som er galt og foreslår en bedre versjon. Rettingene gjøres først når brukeren ber om det.

## 1. Hent teksten

| Det brukeren gir | Slik henter du teksten |
|---|---|
| Innlimt tekst | Bruk den som den er. |
| Nettadresse | Hent sideteksten med nettleseren eller WebFetch. Ta med titler, mellomtitler, knapper og lenketekster, ikke meny og bunntekst. |
| Skjermdump | Les bildet. Skriv av all synlig tekst, også knapper, feltnavn og feilmeldinger. |
| Fil (.md, .docx, .pdf) | Les filen. |
| Kode i et prosjekt | Finn tekstene brukeren ser: overskrifter, knapper, feilmeldinger, hjelpetekst. Noter fil og linje for hver. |

Noter hvor hver tekstbit står, for eksempel «Sidetittel», «Ingress», «Kort 2, beskrivelse» eller «Knapp under skjemaet».

Er teksten lengre enn omtrent 1 500 ord, spør hvilken del som er viktigst, eller gå gjennom de første 1 500 ordene setning for setning og si fra. Helhetsrunden gjelder alltid hele teksten. Gjelder gjennomgangen flere tekster som hører sammen, les alle før du vurderer helheten.

## 2. Finn teksttype og tone

Les [grunnregler.md](../skriveregler/grunnregler.md), [feilkatalog.md](../skriveregler/feilkatalog.md), [teksttyper.md](../skriveregler/teksttyper.md) og [tone.md](../skriveregler/tone.md). Les de andre oppslagene når teksten trenger dem.

- **Teksttype:** Bestem typen for hver del. En informasjonsside kan ha brødtekst (T2), knapper (T1) og en kampanjeboks (T3).
- **Tone:** Vurder hvilken tone teksten trenger, ut fra leseren og teksttypen.
- **Kundens stil:** Bare når brukeren peker på den (se «Kundens stil og tone» i `amalie:skriveregler`). Et funn som strider mot kundens regelnotat, meldes ikke.
- **Kommersiell avsender:** Selger avsenderen et produkt eller en tjeneste, og er leseren kunde? Sjekk da teksten mot [kommersiell.md](../skriveregler/kommersiell.md) også. Et faktum som mangler eller er gjort svakere enn i kilden (KA1), er et funn med høy alvorlighet.

## 3. Gå gjennom teksten

Gjør fem runder. Start med helheten, fordi en feil der kan gjøre setningsfunn unødvendige.

0. **Helhet** ([helhet.md](../skriveregler/helhet.md)). Les hele teksten uten å se på enkeltsetninger. Skriv for deg selv én linje per avsnitt med hva det sier. Sjekk om første setning svarer på overskriften, om overskriftene sier budskapet, om to steder sier ulike ting, om noe står flere ganger, og om teksten ender med et neste steg. Er det flere tekster, lag et faktaregister over tall, råd og begrunnelser som står mer enn ett sted.
1. **Setning for setning.** Sjekk hver setning, overskrift, knapp og lenketekst mot grunnreglene, feilkatalogen og reglene for teksttypen. Les hvert avsnitt høyt (G3): mangler bindeord, høres noe oversatt ut (B16), eller peker «det» og «dette» uklart (G5)? Før du foreslår å fjerne et ord, sjekk om søkedata eller kundens ordliste viser at leseren bruker det. Da går leseren foran regelen (G1).
2. **På tvers av like elementer.** Sammenlign kort, knapper, mellomtitler og listepunkter. Er de bygd likt? Brukes samme ord for samme ting (G8)?
3. **Mønstre.** Finn feil som går igjen, for eksempel samme subjekt i hver setning eller samme forsikringsord i alle kortene. Mønstrene i B13 pekes ut én gang for hele teksten.
4. **Leseren.** Les teksten som to eller tre konkrete lesere med hver sin grunn til å komme. Følg hver leser fra der de kommer inn til der de stopper. Fikk de svaret på spørsmålene sine, i den rekkefølgen de stiller dem? Vet de hvem som skriver? Fikk de tallet de trenger for å bestemme seg? Fant de veien videre? Denne runden finner det regelrundene ikke ser.

Sjekk også påstandene mot kildene du har (G7, B17), og bildenes alt-tekst (D9).

Ta bare med reelle brudd. Det er bedre med fem riktige funn enn tjue tvilsomme. Er teksten god, si det i første setning. Grensetilfeller er ikke funn. Nevn dem høyst i én linje under tabellene: «Kan vurderes: …». Finner du ingen reelle brudd, skriv «Ingen funn» og hopp over tabellene.

## 4. Sorter etter alvorlighet

| Alvorlighet | Hva det betyr | Typiske regler |
|---|---|---|
| **Høy** | Leseren kan misforstå, ta feil valg eller ikke klare oppgaven. Eller teksten påstår noe som ikke kan dokumenteres, gir to svar på samme spørsmål, bruker et ord kundens ordliste forbyr, eller stenger noen lesere ute. | G1, G2, G5, G7, KA1, B1, B5, B6, B11, B12, B17, C10, T1 (feilmeldinger og dialoger), D5, D9, D11, E3, E4, E9, E11 |
| **Middels** | Leseren forstår, men bruker lengre tid eller mister tillit. Telegramstil, oversatt språk, fagord uten forklaring, lange setninger, tomme fraser, feil tone, like elementer bygd ulikt, gjentakelser. | G3, G4, G6, G8, G9, G10, B2–B4, B7–B10, B13–B16, B18, resten av T1, T2–T8, D1–D4, D6–D8, D10, D12–D16, E2, E6–E8, Stil, Tone |
| **Lav** | Typografi og skrivemåte. | C1–C9, C11–C14 |

Regelen i tabellen er et utgangspunkt. Vurder hvor mye feilen betyr for leseren akkurat her. En feil i et notat bare kunden leser, er middels, med mindre den kan få kunden til å ta en feil beslutning. En feil i et arbeidsdokument (T7) vurderes som om den sto i teksten leseren ser.

## 5. Lever resultatet

Første linje: «Gjennomgang av [side eller fil]. Teksttyper: [typene]. Tone: [fire skalaer].» Følger du en kundes stil, legg til «Stil: [kunde]».

Så dommen i én eller to setninger: hvor mange funn, og det viktigste mønsteret.

Så én tabell per alvorlighet, i rekkefølgen høy, middels, lav. Hopp over en gruppe uten funn. Nummerer funnene fortløpende.

| # | Hvor | Teksten nå | Regel | Hva er galt | Forslag |
|---|---|---|---|---|---|
| 1 | Ingress | «Vi er her for å hjelpe deg.» | G6: Si hvem og hva, ikke bare at noe finnes. | Setningen sier ikke hvem som hjelper eller med hva. | «Spør [hvem som hjelper] om [hva].» |

- **Hvor:** stedet i teksten. Gjelder gjennomgangen kode, skriv fil og linje.
- **Teksten nå:** siter ordrett, bare den delen som er feil.
- **Regel:** ID og regelen skrevet ut i én kort setning, slik at leseren lærer regelen uten å slå opp.
- **Forslag:** følger teksttypen, tonen og kundens stil hvis brukeren har pekt på den.
- **Fakta:** Finn aldri på tall, datoer eller fakta i forslagene. Mangler et faktum, sett det i klammer: «[andel som har jobb etter studiene, kilde]».

Avslutt med de ett til tre mønstrene som går igjen, og hvilke funn som er raskest å rette. Spør så: «Skal jeg rette dem?»

## 6. Rett når brukeren sier ja

- **Tekst eller fil:** Lever hele teksten rettet, eller rett filen. Kjør selvgjennomgangen fra `amalie:skriveregler` på den rettede teksten.
- **Kode:** Endre tekstene i koden og ikke noe annet. Si hvilke filer som er endret.
- **Nettside uten tilgang til koden:** Lever rettet tekst som kan limes inn i publiseringsverktøyet.

Brukeren kan be om å rette bare én gruppe, for eksempel «rett de høye». Retter brukeren et funn eller sier at en regel tok feil, følg «Når noen retter Amalie» i `amalie:skriveregler`.
