"""Runs every case in cases.tsv through Amalie's review mode and saves the output in ut/."""
import csv, subprocess, pathlib
from concurrent.futures import ThreadPoolExecutor
here = pathlib.Path(__file__).parent
(here / "ut").mkdir(exist_ok=True)
rows = list(csv.DictReader(open(here / "cases.tsv"), delimiter="\t"))
def run(r):
    p = subprocess.run(["claude", "-p", f"Amalie, se over denne teksten (kunde: ukjent): «{r['tekst']}»",
                        "--allowedTools", "Skill,Read"], stdin=subprocess.DEVNULL, capture_output=True, text=True, cwd=str(pathlib.Path.home()))
    (here / "ut" / f"{r['id']}.txt").write_text(p.stdout + ("\nSTDERR:\n" + p.stderr[-500:] if p.returncode else ""))
with ThreadPoolExecutor(3) as ex: list(ex.map(run, rows))
