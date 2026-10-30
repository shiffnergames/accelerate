"""Build accelerate-offline.html: one file with three.js and the fonts baked in, so it runs with no internet.

Run from the repo folder:   python3 tools/make_offline.py
Then upload accelerate-offline.html to Google Drive, download it on the Chromebook, and open it.

index.html loads two things from the internet: the three.js library and the Bungee/Nunito fonts.
This script downloads both and pastes them straight into a copy of the page.
"""
import base64, pathlib, re, sys, urllib.request

repo = pathlib.Path(__file__).resolve().parent.parent
src_path = repo / "index.html"
out_path = repo / "accelerate-offline.html"

THREE_URL = "https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"
FONTS_URL = "https://fonts.googleapis.com/css2?family=Bungee&family=Nunito:wght@600;800&display=swap"
# Google Fonts only hands out the small modern (woff2) files to a browser-looking request
CHROME_UA = "Mozilla/5.0 (X11; CrOS x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"


def fetch(url, ua=None):
    req = urllib.request.Request(url, headers={"User-Agent": ua} if ua else {})
    with urllib.request.urlopen(req) as r:
        return r.read()


src = src_path.read_text()

# 1. Fonts: keep only the latin @font-face blocks, download each font file and inline it as base64
css = fetch(FONTS_URL, CHROME_UA).decode()
faces = []
for subset, body in re.findall(r"/\* (\w[\w-]*) \*/\s*@font-face \{(.*?)\}", css, re.S):
    if subset != "latin":
        continue
    url = re.search(r"url\((https://[^)]+)\)", body).group(1)
    b64 = base64.b64encode(fetch(url)).decode()
    faces.append("@font-face {" + body.replace(url, f"data:font/woff2;base64,{b64}") + "}")
if not faces:
    sys.exit("no latin font blocks found in the Google Fonts CSS")
link_re = r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^"]*">'
if not re.search(link_re, src):
    sys.exit("fonts <link> tag not found in index.html")
src = re.sub(link_re, lambda m: "<style>\n" + "\n".join(faces) + "\n</style>", src, count=1)

# 2. three.js: paste the library in place of the CDN <script> tag
three = fetch(THREE_URL).decode()
if "</script" in three:
    sys.exit("three.js contains </script>, cannot inline it")
tag_re = r'<script src="https://cdnjs\.cloudflare\.com/ajax/libs/three\.js/r128/three\.min\.js"></script>'
if not re.search(tag_re, src):
    sys.exit("three.js <script> tag not found in index.html")
src = re.sub(tag_re, lambda m: "<script>\n" + three + "\n</script>", src, count=1)

# 3. Make sure nothing else still points at the internet (the GitHub Pages link in the text is fine)
leftovers = [u for u in re.findall(r"https://[^\s\"')]+", src) if "shiffnergames.github.io" not in u]
if leftovers:
    sys.exit("still loading from the internet: " + ", ".join(leftovers))

out_path.write_text(src)
print(f"wrote {out_path.name} ({out_path.stat().st_size // 1024} KB), {len(faces)} fonts inlined")
