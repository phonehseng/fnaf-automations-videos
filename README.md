# FNAF Automations - videos

The explainer videos about [FNAF Automations](https://github.com/phonehseng/Fnaf-automations),
a Python + OpenCV bot that plays Five Nights at Freddy's by watching the screen.
This repository is the content: scripts, the animation engine and the
production tools. The bot itself lives in its own repository.

| | |
|---|---|
| `lecture/` | the animation page (`night_shift_lecture.html`, every scene of every video), the productions and their narration (`productions.json`), and the tools that record, render, mix and assemble the videos - see `lecture/README.md` |
| `docs/SCRIPTS.md` | every video's narration, scene by scene (generated from `productions.json`) |
| `docs/VOICEOVER_SCRIPT.md` | the script of the first explainer (2026-10-22) |
| `tools/capture_freddy.py` | films Freddy walking his route on the cameras, for the shorts |

## Productions

* **The Night Shift Lecture** - long form, 16:9, ~10 minutes; narrated and without narrator
* **The Night Shift Lecture** - vertical, ~7 minutes
* **Shorts** (9:16, narrated): What if a bot played FNAF on 20/20/20/20? - Why watching Foxy
  freezes him - My first FNAF bot never looked - How a bot sees FNAF - Freddy's AI explained -
  Human vs robot night guard

## What is not in here

Footage, audio, renders and the narration voice are large and can be rebuilt:
`lecture/export_footage.py` and `lecture/prepare_stills.py` cut the clips and stills from
the OBS recordings and the bot's extracted game pictures (expected next to this repository,
in `../Fnaf-automations`), `lecture/narrate.py` needs the Piper voice `en_GB-alan-medium` in
`lecture/voices/`.

All music and sound effects are synthesized by `lecture/sound.py`; the game footage and
pictures are from Five Nights at Freddy's (Scott Cawthon), shown for commentary.
