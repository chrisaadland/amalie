# Endringslogg for Amalie

## 1.0.0 (under arbeid) – satt sammen etter regelvurderingen

Fire ekspertdommere leste to regelsett uten å vite hvilket som var hvilket: 1.0 bygget på 0.12, og første utgave av 1.0 med ti grunnregler. Alle fire valgte grunnreglene som grunnlag. Vurderingen står i `docs/regelvurdering-2026-11-23.md`. Reglene er satt sammen etter det de var enige om:

- **Grunnlaget** er de ti grunnreglene, oppslagene og selvgjennomgangen i åtte steg.
- **Mengden innhold:** en ny tabell øverst i grunnreglene sier hva skribenten gjør ved lite, middels og mye innhold. Ved lite innhold skal hun svare kort med det hun har og ikke fylle ut.
- **Slutning er lov, tillegg er ikke lov (G7).** En slutning som følger av faktaene, skrives som et vilkår: «Ja, hvis …». Instrukser og beskrivelser av hvordan noe foregår, er påstander, og de må stå i kilden.
- **Hver setning bygger på noe (G9):** et faktum eller et spørsmål leseren har. Byttetesten stryker setninger som kunne stått i en hvilken som helst annen tekst.
- **Konkret person og konkret løfte (G6).** Personer har en rolle, og et løfte om hjelp sier hva hjelpen er.
- **G1:** svar på alt leseren spør om, også tvilen, med faktaene du har. Legg ikke til noe for å gjøre teksten lengre. Vanskelige beskjeder sier hva beskjeden betyr i praksis, uten faste fraser.
- **G3:** én påstand per setning er utgangspunktet, men et vilkår eller en grunn kan stå i samme setning. Bindeord brukes når faktaene gir sammenhengen. «Så» brukes bare om en følge. Et langt subjekt skal ikke skille verbet fra objektet.
- **G2:** står det ingen handling i faktaene, finn ikke på en.
- **Helhetsreglene leses alltid**, også for korte tekster.
- **Tomme servicefraser** er lagt inn i B10: «vi hjelper deg videre», «ta kontakt for mer informasjon».
- **T9, beslutningsgrunnlag for en leder,** er tatt med fra 0.12.

**Etter kontroll med én dommer:**
- G6: roller og løfter hentes fra kilden. Gir ikke kilden noen rolle, strykes personen. Eksemplene som fant på en rolle og en frist, er rettet.
- G1: lista over tvil er en sjekk. Spørsmål faktaene ikke svarer på, står ikke i teksten, men nevnes for den som bestilte den.
- G7 og G9: stryking er hovedregelen. En markør brukes bare når leseren må ha faktumet for å handle.
- G9: en setning som viser forståelse, må bygge på noe leseren har fortalt eller på faktaene.
- Mengden innhold: «lite» er under 10 fakta.
- Kortere: E1, E5, E10 og E12 er slått sammen med grunnreglene. Helhetsreglene gjelder lange tekster og tekster som hører sammen. B4 viser til G3, og dobbeltreglene i B10 og B13 er strøket. Selvgjennomgangen har fem steg i stedet for åtte.

1.0 bygget på 0.12 ligger i `docs/1.0-fra-0.12/`.

## Forkastet utgave av 1.0.0


Amalie er bygget om fra en skriveassistent for ett byrå til en generell skriveagent for norske innholdsfolk. Endringene bygger på en gjennomgang av hele regelsettet, to skrivetester med lederen som leser og en sammenligning med retningslinjene til NAV, GOV.UK, Skatteetaten og Mailchimp. Planen og lærdommene står i `docs/plan-1.0.md` i det private repoet.

**Ti grunnregler.** Regelsettet har fått en kjerne på ti prinsipper som alltid gjelder (`grunnregler.md`). Resten er oppslag. Hver regel i oppslagene viser hvilken grunnregel den hører til.

- G1 Leseren går foran. Svar på spørsmålene leseren har, i den rekkefølgen leseren stiller dem. Data om leseren går foran reglene.
- G2 Det viktigste først. Overskriften sier budskapet.
- G3 Skriv slik en flink person ville sagt det. Bindeord, les høyt, maks 25 ord.
- G4 La noen gjøre noe. Aktivt, «du», hva leseren kan gjøre, og en person i en situasjon.
- G5 Én mening. Ingen pyntemetaforer, ingen bibetydning, og pekeord som peker på én ting.
- G6 Konkret. Tall, steder og forklarte fagord.
- G7 Sant og etterprøvbart. Avsenderen er kjent, påstandene har grunnlag, og det planlagte skrives som planlagt.
- G8 Likt hele veien. Ord, tall, tiltale og avsender.
- G9 Bare det leseren trenger.
- G10 For alle lesere.

**Hvor de gamle reglene står nå**

| Før | Nå |
|---|---|
| A1, prinsippet «leseren går foran» | G1 |
| A2 | G2 |
| A5, A6, A11 | G3 |
| A4, A7, A13 | G4 |
| A10, A12 | G5 |
| A3, A8 | G6 og G8 |
| A9 | D16 |
| B1–B17 | `feilkatalog.md`, samme ID-er. B16 har fått skriftspråksord. |
| C1–C13 | `skrivemaate.md`, med ny C14 om tall |
| D1–D15 | `alle-lesere.md` |
| E1–E12 | `helhet.md`. E11 sier også at et regnestykke viser antakelsen det hviler på. |
| T1–T8 | `teksttyper.md` |
| T9 | Tatt ut. Det som var riktig i den, er G1 og G7. |

**Kundene er tatt ut.** Amalie kjenner ingen kunder, og eksemplene er nøytrale. Hun bruker en kundes stil når brukeren peker på hvor den ligger. Kundens valg går foran grunnreglene bare på noen få punkter: tiltaleform, målform, egne navn og ord, klokkeslett og standardtone.

**To nye moduser.** `rediger` retter en tekst med lett hånd og lar skribenten beholde stemmen sin, på tre nivåer: korrektur, språkvask og strukturell redigering. `forklar` forklarer en regel slik at skribenten lærer den.

**Selvgjennomgang.** Skrivemodusen går gjennom sin egen tekst før levering: leserens første spørsmål, helhet, høytlesing, likt hele veien, leseren, påstandene, lengden og feilkatalogen. Grundigheten følger teksten: korte tekster får to steg, vanlige leveranser alle åtte, og en rask tekst bare høytlesing. Det sparer tid og tokens der hele gjennomgangen ikke trengs.

**Porten for nye regler.** Før en rettelse blir en ny regel, spør Amalie om en grunnregel allerede dekker den, og om den bare gjelder én kunde eller én tekst. En ny regel lages bare når feilen kan skje i mange slags tekster.

**Testsett for skriving.** `tests/skriving/` har seks bestillinger med premissark, testet med høytlesing, leseren, påstandene og en blind dommer som sammenligner to versjoner.

**Rettet etter den store testen.** Tolv bestillinger og fire ekspertdommere viste at første utgave av 1.0 skrev dårligere enn 0.12. Tekstene var en tredjedel kortere og for tørre. Endringene:
- G1: svar fullt ut. Ny veiledning for vanskelige beskjeder og for lesere som handler for en annen.
- G2: handlingen står i de første ordene, og hovedhandlingen tidlig og igjen til slutt.
- G3: én påstand per setning. Bindeord bare der sammenhengen finnes. Hold sammen det som hører sammen. Fragmenter er lov i sosiale medier og kampanjer.
- G4: feilmeldinger og instruksjoner er aktive («Skriv inn …»). Unntaket for passiv er tatt ut. Et eksempel med en person bygger bare på fakta du har.
- G7: skriv det du vet først, og sett markøren bare på det som mangler.
- G9: strykespørsmålet er tatt ut. Setninger som svarer, forklarer, viser forståelse eller takker, gjør en jobb. Sikkerhetsinformasjon og hovedhandlingen kan stå to steder.
- T1: feilmeldinger i bydeform. T3: si hva leseren får ut av det. T4: varsler har tidspunkt og åpner med handlingen. T5: faste deler i vedtak.
- tone.md: ny del om kanal.
- Selvgjennomgangen sjekker én påstand per setning, ekte bindeord, gjentakelser og markører.

**Testresultat.** I skrivetestene foretrakk en blind dommer 1.0 i 4 av 6 tekster, i to runder med hver sin dommer. Forskjellen mellom dommerne var større enn forskjellen mellom versjonene, så testene viser at 1.0 skriver minst like godt som 0.12. Detaljene står i `tests/skriving/resultater.md`. Gjennomgangstestene: 17 av 17.

**Markører.** Ny markør [AVKLAR INTERNT] for det avsenderen ikke har bestemt ennå.
