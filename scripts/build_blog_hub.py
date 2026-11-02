"""Builds blog/index.html: one page listing every post from Trading Científico's Substacks.

Run: python scripts/build_blog_hub.py  (stdlib only). A daily GitHub Action re-runs it.
"""
import html
import json
import pathlib
import urllib.request
from datetime import datetime

SOURCES = [
    ("https://tradingcientifico.substack.com", "Tests de reels y estrategias virales"),
    ("https://neytrading.substack.com", "Series: episodic pivot y momentum"),
]
OUT = pathlib.Path(__file__).resolve().parents[1] / "blog" / "index.html"


def fetch_posts(base, label, limit=50):
    url = f"{base}/api/v1/archive?sort=new&limit={limit}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    return [{
        "date": p["post_date"][:10],
        "title": p["title"],
        "subtitle": p.get("subtitle") or "",
        "url": p["canonical_url"],
        "source": label,
    } for p in data]


def render(posts):
    rows = []
    for p in posts:
        d = datetime.strptime(p["date"], "%Y-%m-%d").strftime("%d/%m/%Y")
        rows.append(
            f'<li><a href="{html.escape(p["url"])}">{html.escape(p["title"])}</a>'
            f'<span class="meta">{d} · {html.escape(p["source"])}</span>'
            + (f'<p>{html.escape(p["subtitle"])}</p>' if p["subtitle"] else "")
            + "</li>")
    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Trading Científico · Todos los tests</title>
<meta name="description" content="Cada estrategia de trading viral, probada con datos reales: reglas, costos y años fuera de muestra.">
<style>
body{{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;max-width:720px;margin:0 auto;padding:24px 16px;color:#111;background:#fff}}
h1{{font-size:1.6rem;margin:0 0 4px}} .lead{{color:#555;margin:0 0 20px}}
input{{width:100%;padding:12px;font-size:1rem;border:2px solid #eb6834;border-radius:8px;box-sizing:border-box;margin-bottom:16px}}
ul{{list-style:none;padding:0;margin:0}} li{{padding:14px 0;border-bottom:1px solid #eee}}
li a{{font-weight:600;color:#3b6ea5;text-decoration:none;font-size:1.05rem}} li a:hover{{text-decoration:underline}}
.meta{{display:block;color:#888;font-size:.8rem;margin-top:4px}} li p{{margin:6px 0 0;color:#444;font-size:.92rem}}
footer{{margin-top:28px;color:#888;font-size:.8rem}}
</style></head><body>
<h1>Trading Científico</h1>
<p class="lead">Las estrategias de trading virales, probadas con datos reales. Busca el título que viste en el video.</p>
<input id="q" type="search" placeholder="Buscar: puts, senadores, momentum…" aria-label="Buscar post">
<ul id="list">{''.join(rows)}</ul>
<footer>Actualizado {datetime.utcnow().strftime('%d/%m/%Y')} · <a href="https://www.tradingcientifico.com">tradingcientifico.com</a></footer>
<script>
const q=document.getElementById('q'),items=[...document.querySelectorAll('#list li')];
q.addEventListener('input',()=>{{const t=q.value.toLowerCase();items.forEach(li=>li.style.display=li.textContent.toLowerCase().includes(t)?'':'none');}});
</script></body></html>"""


def main():
    posts = []
    for base, label in SOURCES:
        posts += fetch_posts(base, label)
    posts.sort(key=lambda p: p["date"], reverse=True)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(posts), encoding="utf-8")
    print(f"{len(posts)} posts -> {OUT}")


if __name__ == "__main__":
    main()
