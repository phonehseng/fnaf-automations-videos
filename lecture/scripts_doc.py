"""Write ../docs/SCRIPTS.md from productions.json: every video's narration,
scene by scene.

usage: python scripts_doc.py
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
prods = json.loads((HERE / "productions.json").read_text(encoding="utf-8"))
out = ["# Video scripts", "",
       "Generated from `lecture/productions.json` by `lecture/scripts_doc.py` - the narration as recorded "
       "(Piper TTS, `en_GB-alan-medium`) and shown on screen as subtitles. Each numbered line is one "
       "animated scene (`DRAW.<name>` in `lecture/night_shift_lecture.html`).", ""]
for pid, p in prods.items():
    out += [f"## {p['label']}  (`{pid}`, {p['layout']})", ""]
    for i, sc in enumerate(p["scenes"], 1):
        mode = f" ({sc['mode']})" if sc.get("mode") else ""
        head = f" - {sc['headline']}" if sc.get("headline") else ""
        out += [f"**{i}. {sc['draw']}{mode}**{head}", ""] + [f"> {c}" for c in sc["cues"]] + [""]
(HERE.parent / "docs" / "SCRIPTS.md").write_text("\n".join(out), encoding="utf-8")
print("wrote docs/SCRIPTS.md")
