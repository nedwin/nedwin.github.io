"""Re-extract Seek Rejection and Psychological Runway from Wayback Machine HTML.

These two posts get blocked by Cloudflare on direct Medium fetch, but the
Wayback Machine has clean copies that include the original Medium markup.
"""

import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from extract_posts import html_to_md, write_post  # reuse

ROOT = Path("/Users/nedwin/projects/neddwyer-com")


def extract_article_body(html_text: str) -> str:
    """Pull the <article> body and clean Wayback Machine wrappers."""
    # Strip out Wayback Machine toolbar injection
    html_text = re.sub(r"<!--\s*BEGIN WAYBACK TOOLBAR INSERT\s*-->.*?<!--\s*END WAYBACK TOOLBAR INSERT\s*-->",
                       "", html_text, flags=re.DOTALL)
    # Find article
    m = re.search(r"<article[^>]*>(.*?)</article>", html_text, flags=re.DOTALL)
    if not m:
        return ""
    body = m.group(1)
    # Remove "Ned Dwyer" byline paragraph at top
    body = re.sub(r"<p[^>]*>\s*Ned Dwyer\s*</p>", "", body, count=1)
    # Remove any duplicate h1 (the title)
    body = re.sub(r"<h1[^>]*>.*?</h1>", "", body, count=1, flags=re.DOTALL)
    # Remove "follow" buttons, "clap" widgets, share blocks
    body = re.sub(r"<button[^>]*>.*?</button>", "", body, flags=re.DOTALL)
    body = re.sub(r"<aside[^>]*>.*?</aside>", "", body, flags=re.DOTALL)
    return body


posts = [
    {
        "title": "Seek rejection",
        "slug": "seek-rejection",
        "date": "2011-08-01T00:00:00+00:00",
        "html_file": "seek-rejection-wayback.html",
        "canonical": "https://nedwin.medium.com/seek-rejection-cec46377b8e2",
    },
    {
        "title": "Managing your psychological runway",
        "slug": "managing-your-psychological-runway",
        "date": "2015-06-30T00:00:00+00:00",
        "html_file": "psych-runway-wayback.html",
        "canonical": "https://nedwin.medium.com/managing-your-psychological-runway-dc232d80ae98",
    },
]

for p in posts:
    src = ROOT / "research" / p["html_file"]
    raw = src.read_text(encoding="utf-8", errors="replace")
    article = extract_article_body(raw)
    body_md = html_to_md(article)

    # Strip "By Ned Dwyer" lines and date stamps that aren't part of the post
    body_md = re.sub(r"^Ned Dwyer.*?\n", "", body_md, count=1, flags=re.MULTILINE)
    # Trim Wayback URL prefixes from any links
    body_md = re.sub(r"https?://web\.archive\.org/web/[^/]+/", "", body_md)

    summary_src = re.sub(r"[#*`\[\]\(\)_>!]", "", body_md)
    summary = re.sub(r"\s+", " ", summary_src).strip()[:200]
    summary = summary.replace('"', "'")

    write_post(p["title"], p["slug"], p["date"], summary, body_md, p["canonical"])

print("\nWayback re-extraction complete.")
