# Amalie

Amalie er en skriveagent for Claude som skriver og retter norsk tekst. Teksten skal leseren forstå første gang, og den skal høres ut som en flink person har skrevet den. Hun er laget for innholdsfolk: de som skriver nettsider, e-post, rapporter, pitcher og tekst i apper. Hun er oppkalt etter forfatteren Amalie Skram, som skrev nøkternt og uten pynt.

## Dette kan du be henne om

| Du skriver | Amalie |
|---|---|
| «Amalie, skriv en e-post til medlemmene om at senteret stenger.» | skriver teksten og går gjennom den selv før hun leverer |
| «Amalie, se over denne siden: [nettadresse]» | lister det som bør rettes, sortert fra alvorlig til lite viktig, med regel og forslag |
| «Amalie, rett språket i utkastet mitt.» | retter med lett hånd, så du beholder stemmen og strukturen din |
| «Amalie, hvorfor er denne setningen dårlig?» | forklarer regelen med eksempler, så du kan bruke den selv neste gang |

Skriver du en tekst på norsk uten å nevne henne, bruker Claude reglene hennes likevel.

## Ti grunnregler

1. Leseren går foran.
2. Det viktigste først.
3. Skriv slik en flink person ville sagt det.
4. La noen gjøre noe.
5. Én mening.
6. Konkret.
7. Sant og etterprøvbart. Slutninger er lov, tillegg er ikke lov.
8. Likt hele veien.
9. Bare det leseren trenger. Hver setning bygger på noe.
10. For alle lesere.

Lengden og formen følger mengden innhold: lite, middels eller mye. Hver regel har eksempler i [grunnregler.md](plugins/amalie/skills/skriveregler/grunnregler.md). Reglene bygger på Språkrådet, NAV, Skatteetaten, Digdir, Uutilsynet, GOV.UK, Mailchimp, Microsoft og Nielsen Norman Group.

## Skriv for en kunde

Amalie kjenner ingen kunder. Skal teksten følge en kundes stil, si hvilken kunde det gjelder og hvor stilen ligger:

> Amalie, skriv ingressen for Havbrød. Stilguiden ligger i Havbrød/stilguide.md, og ordlisten i Havbrød/ordliste.md.

Da følger hun kundens valg av tiltaleform, målform, egne ord og tone. Grunnreglene om å bli forstått og å skrive sant gjelder alltid. Strider stilguiden mot dem, sier hun fra.

Har kunden ingen stilguide, kan hun lage et utkast etter [malen](plugins/amalie/skills/skriveregler/kundestil-mal.md).

## Installer i Claude Code

Skriv disse to kommandoene i Claude Code:

```
/plugin marketplace add chrisaadland/amalie-tre
```

```
/plugin install amalie@amalie-lokal
```

Start Claude Code på nytt etterpå. Nye versjoner henter du med `/plugin marketplace update amalie-lokal`.

Repoet er privat inntil videre. Be Chris Aadland om tilgang.

## Installer i Claude-appen (claude.ai eller desktop)

1. Last ned `amalie.zip` fra siste versjon under Releases i repoet.
2. Åpne Claude og gå til **Innstillinger → Capabilities → Skills**.
3. Velg **Upload skill** og last opp zip-filen.
4. Skriv «Amalie, se over denne: …» i en ny samtale.

## Når Amalie tar feil

Si det til henne: «Amalie, dette ordet skal stå, fordi folk søker på det.» Hun spør om rettelsen gjelder bare den kunden eller alle tekster. Gjelder den alle, send den til Chris Aadland, så går den inn i reglene etter porten i [skriveregler/SKILL.md](plugins/amalie/skills/skriveregler/SKILL.md).

## Filene

| Fil | Hva den inneholder |
|---|---|
| [grunnregler.md](plugins/amalie/skills/skriveregler/grunnregler.md) | De ti grunnreglene og tabellen for mengden innhold |
| [helhet.md](plugins/amalie/skills/skriveregler/helhet.md) | Om teksten henger sammen (E1–E12), leses alltid |
| [feilkatalog.md](plugins/amalie/skills/skriveregler/feilkatalog.md) | Vanlige feil og KI-mønstre (B1–B17) |
| [skrivemaate.md](plugins/amalie/skills/skriveregler/skrivemaate.md) | Typografi, tall og datoer (C1–C14) |
| [alle-lesere.md](plugins/amalie/skills/skriveregler/alle-lesere.md) | Inkluderende språk, universell utforming og lenker (D1–D16) |
| [teksttyper.md](plugins/amalie/skills/skriveregler/teksttyper.md) | Grensesnitt, informasjonsside, markedsføring, nyhet, e-post og vedtak, rapport, arbeidsdokument, metabeskrivelse og beslutningsgrunnlag |
| [tone.md](plugins/amalie/skills/skriveregler/tone.md) | De fire skalaene for tone, kanal, og samme beskjed i fem toner |
| [CHANGELOG.md](plugins/amalie/CHANGELOG.md) | Hva som er endret i hver versjon |
| [tests/](tests/) | Gjennomgangstester og skrivetester, med [resultater](tests/skriving/resultater-12.md) |
