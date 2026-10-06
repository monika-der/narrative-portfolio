# Narrative Design Portfolio — Flask

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## Where to edit writing
- `templates/content/the_arrow.html` — full The Arrow text
- `templates/content/twine_project.html` — Twine presentation / embed area
- `templates/content/relics.html` — item descriptions
- `app.py` — project metadata and case-study copy
- `templates/index.html` — homepage / About / contact placeholder

The Arrow is intentionally styled as a readable text editor: editor chrome outside, serif prose inside, max reading width ~720px, warm off-white text, generous spacing.
