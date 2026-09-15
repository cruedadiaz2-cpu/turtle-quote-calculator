"""Build index.html from src/page.html.

Single source of truth: src/page.html. The logos live beside it as real files and
get inlined as data URIs so the built page is one self-contained file - handy for
dropping onto turtlecleaningusa.com later without carrying an assets folder.

Run from anywhere:  python src/build.py
"""
import base64
import pathlib

SRC_DIR = pathlib.Path(__file__).parent
REPO = SRC_DIR.parent

PAGE = SRC_DIR / "page.html"
OUT = REPO / "index.html"

LOGOS = ["turtle-mark-color.png", "turtle-mark-white.png"]

html = PAGE.read_text(encoding="utf-8")

for name in LOGOS:
    b64 = base64.b64encode((REPO / name).read_bytes()).decode("ascii")
    before = html
    html = html.replace(f'src="{name}"', f'src="data:image/png;base64,{b64}"')
    if html == before:
        raise SystemExit(f"logo reference not found in source: {name}")

# page.html carries no document skeleton, so add one.
marker = "</style>\n"
if marker not in html:
    raise SystemExit("could not find the end of the inline <style> block")
head, _, rest = html.partition(marker)

OUT.write_text(
    '<!doctype html>\n<html lang="en">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    + head
    + "  body{ margin:0; }\n</style>\n</head>\n<body>\n"
    + rest
    + "\n</body>\n</html>\n",
    encoding="utf-8",
)

print(f"built {OUT.name}: {OUT.stat().st_size:,} bytes")
