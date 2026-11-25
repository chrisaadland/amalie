"""Lager dist/amalie.zip: hele Amalie som én skill for Claude-appen (claude.ai og desktop)."""
import pathlib, shutil, zipfile
rot = pathlib.Path(__file__).parent
skills = rot / "plugins" / "amalie" / "skills"
ut = rot / "dist" / "amalie"
shutil.rmtree(ut, ignore_errors=True)
for navn in ["skriveregler", "gjennomgang", "rediger", "forklar"]:
    shutil.copytree(skills / navn, ut / navn)
shutil.copy(skills / "amalie" / "SKILL.md", ut / "SKILL.md")
bytt = {f"`amalie:{n}`": f"`{n}/SKILL.md`" for n in ["skriveregler", "gjennomgang", "rediger", "forklar"]}
bytt.update({f"amalie:{n}": f"{n}/SKILL.md" for n in ["skriveregler", "gjennomgang", "rediger", "forklar"]})
bytt["Last skillen før du gjør noe annet."] = "Les filen før du gjør noe annet."
for f in ut.rglob("*.md"):
    s = f.read_text()
    for a, b in bytt.items():
        s = s.replace(a, b)
    f.write_text(s)
zipsti = rot / "dist" / "amalie.zip"
with zipfile.ZipFile(zipsti, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(ut.rglob("*")):
        if f.is_file():
            z.write(f, f.relative_to(ut.parent))
print(zipsti.relative_to(rot))
