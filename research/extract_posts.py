"""Extract Medium posts to Hugo markdown files.

Parses the Medium RSS feed for full-content posts plus directly-fetched
HTML for older posts. Converts HTML to lightweight markdown and writes
each post to content/posts/<slug>.md with proper Hugo frontmatter.
"""

import html
import os
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path("/Users/nedwin/projects/neddwyer-com")
POSTS_DIR = ROOT / "content" / "posts"
POSTS_DIR.mkdir(parents=True, exist_ok=True)


def html_to_md(s: str) -> str:
    """Crude but functional HTML → markdown for Medium's post markup."""
    # Strip out images that are Medium tracking pixels / favicons
    s = re.sub(r"<figure>\s*<img[^>]+src=\"([^\"]+)\"[^>]*/?>(?:\s*<figcaption>([^<]+)</figcaption>)?\s*</figure>",
               lambda m: f"\n\n![{m.group(2) or ''}]({m.group(1)})\n\n", s, flags=re.DOTALL)
    s = re.sub(r"<img[^>]+src=\"([^\"]+)\"[^>]*/?>", r"\n\n![](\1)\n\n", s)

    # Headings
    s = re.sub(r"<h1[^>]*>(.*?)</h1>", r"\n\n# \1\n\n", s, flags=re.DOTALL)
    s = re.sub(r"<h2[^>]*>(.*?)</h2>", r"\n\n## \1\n\n", s, flags=re.DOTALL)
    s = re.sub(r"<h3[^>]*>(.*?)</h3>", r"\n\n### \1\n\n", s, flags=re.DOTALL)
    s = re.sub(r"<h4[^>]*>(.*?)</h4>", r"\n\n#### \1\n\n", s, flags=re.DOTALL)

    # Inline emphasis
    s = re.sub(r"<strong[^>]*>(.*?)</strong>", r"**\1**", s, flags=re.DOTALL)
    s = re.sub(r"<b[^>]*>(.*?)</b>", r"**\1**", s, flags=re.DOTALL)
    s = re.sub(r"<em[^>]*>(.*?)</em>", r"*\1*", s, flags=re.DOTALL)
    s = re.sub(r"<i[^>]*>(.*?)</i>", r"*\1*", s, flags=re.DOTALL)
    s = re.sub(r"<code[^>]*>(.*?)</code>", r"`\1`", s, flags=re.DOTALL)

    # Links
    s = re.sub(r"<a[^>]+href=\"([^\"]+)\"[^>]*>(.*?)</a>",
               r"[\2](\1)", s, flags=re.DOTALL)

    # Blockquotes
    s = re.sub(r"<blockquote[^>]*>(.*?)</blockquote>",
               lambda m: "\n\n" + "\n".join("> " + ln for ln in m.group(1).strip().split("\n")) + "\n\n",
               s, flags=re.DOTALL)

    # Paragraphs
    s = re.sub(r"<p[^>]*>(.*?)</p>", r"\n\n\1\n\n", s, flags=re.DOTALL)

    # Line breaks
    s = re.sub(r"<br\s*/?>", "\n", s)

    # Lists
    s = re.sub(r"<li[^>]*>(.*?)</li>", r"- \1\n", s, flags=re.DOTALL)
    s = re.sub(r"</?[uo]l[^>]*>", "\n", s)

    # Strip remaining tags
    s = re.sub(r"<[^>]+>", "", s)

    # Decode entities
    s = html.unescape(s)

    # Collapse whitespace
    s = re.sub(r"\n{3,}", "\n\n", s)
    s = re.sub(r"[ \t]+\n", "\n", s)
    s = re.sub(r"\n[ \t]+", "\n", s)

    return s.strip()


def slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s).strip("-")
    return s


def write_post(title: str, slug: str, date: str, summary: str, body: str,
               medium_url: str, tags: list = None):
    tags = tags or []
    tags_toml = "[" + ", ".join(f'"{t}"' for t in tags) + "]"
    fm = f"""+++
title = "{title}"
slug = "{slug}"
date = {date}
description = "{summary}"
tags = {tags_toml}
canonical_url = "{medium_url}"
+++

{body}
"""
    out = POSTS_DIR / f"{slug}.md"
    out.write_text(fm)
    print(f"Wrote {out.relative_to(ROOT)} ({len(body)} chars)")


# === Parse RSS feed ===
print("Parsing RSS feed...")
rss_path = ROOT / "research" / "medium-feed.xml"
tree = ET.parse(rss_path)
root = tree.getroot()

ns = {"content": "http://purl.org/rss/1.0/modules/content/",
      "dc": "http://purl.org/dc/elements/1.1/"}

signature_slugs = {
    "seed-stage-investor-update-template",
    "my-grand-theory-of-customer-validation",
    "19-things-ive-done",
    "the-kanye-west-work-ethic-rap-camp",
    "set-and-forget-the-product-we-forgot-about",
    "my-love-affair-with-large-competitive-fragmented-markets",
    "your-expense-policy-is-hurting-your-team",
    "emerging-infrastructure-and-the-entrepreneurial-opportunity",
}

# Map Medium slug → preferred local slug
slug_overrides = {
    "my-grand-theory-of-customer-validation": "grand-theory-of-customer-validation",
}

rss_count = 0
for item in root.iter("item"):
    title = item.findtext("title", "").strip()
    link = item.findtext("link", "").strip()
    pubdate = item.findtext("pubDate", "").strip()
    content_html = item.findtext("content:encoded", "", namespaces=ns)

    # Pull out Medium slug from URL
    m = re.search(r"/([a-z0-9-]+)-([a-f0-9]+)(?:\?|$)", link)
    if not m:
        continue
    medium_slug = m.group(1)

    # Use preferred slug if overridden, else use Medium slug
    local_slug = slug_overrides.get(medium_slug, medium_slug)

    # Parse date to ISO
    dt = parsedate_to_datetime(pubdate)
    date_iso = dt.strftime("%Y-%m-%dT%H:%M:%S%z")
    # Hugo expects ISO 8601 with colon in offset
    date_iso = date_iso[:-2] + ":" + date_iso[-2:]

    # Convert HTML body to markdown
    body = html_to_md(content_html)

    # Summary = first ~200 chars of body, no markdown
    summary_src = re.sub(r"[#*`\[\]\(\)_>]", "", body)
    summary_src = re.sub(r"\s+", " ", summary_src).strip()
    summary = summary_src[:200].rstrip() + ("..." if len(summary_src) > 200 else "")
    summary = summary.replace('"', "'")

    # Strip canonical Medium URL (no source param)
    canonical = re.sub(r"\?source=.*$", "", link)

    write_post(title, local_slug, date_iso, summary, body, canonical)
    rss_count += 1

print(f"Wrote {rss_count} posts from RSS feed.\n")


# === Parse older HTML pages for Seek Rejection & Psychological Runway ===
print("Parsing older signature posts...")

def extract_medium_article(html_path: Path) -> tuple:
    """Return (title, body_markdown) extracted from a Medium article HTML."""
    raw = html_path.read_text(encoding="utf-8", errors="replace")
    # Title is in <title> tag (strip Medium suffix)
    title_m = re.search(r"<title[^>]*>([^<]+)</title>", raw)
    title = title_m.group(1) if title_m else "Untitled"
    title = re.sub(r"\s*\|\s*by Ned Dwyer.*$", "", title)
    title = re.sub(r"\s*-\s*Medium\s*$", "", title)
    title = html.unescape(title).strip()

    # Body — find the <article>...</article> region
    art_m = re.search(r"<article[^>]*>(.*?)</article>", raw, flags=re.DOTALL)
    if not art_m:
        # Fallback: look for the main story section
        art_m = re.search(r"<section[^>]+name=\"[^\"]+\"[^>]*>(.*?)</section>", raw, flags=re.DOTALL)
    body_html = art_m.group(1) if art_m else raw

    # Strip out the title element that may be duplicated
    body_html = re.sub(r"<h1[^>]*>.*?</h1>", "", body_html, count=1, flags=re.DOTALL)

    body_md = html_to_md(body_html)
    return title, body_md


older = [
    ("seek-rejection.html", "Seek rejection", "seek-rejection",
     "2011-08-01T00:00:00+00:00",
     "https://nedwin.medium.com/seek-rejection-cec46377b8e2"),
    ("psych-runway.html", "Managing your psychological runway", "managing-your-psychological-runway",
     "2015-06-30T00:00:00+00:00",
     "https://nedwin.medium.com/managing-your-psychological-runway-dc232d80ae98"),
]

for fname, title, slug, date_iso, canonical in older:
    p = ROOT / "research" / fname
    if not p.exists() or p.stat().st_size < 1000:
        print(f"  ! {fname} missing or too small, skipping")
        continue
    _, body = extract_medium_article(p)
    if len(body) < 500:
        print(f"  ! {fname} body extraction looks empty ({len(body)} chars)")
    summary_src = re.sub(r"[#*`\[\]\(\)_>]", "", body)
    summary = re.sub(r"\s+", " ", summary_src).strip()[:200]
    summary = summary.replace('"', "'")
    write_post(title, slug, date_iso, summary, body, canonical)

print("\nDone.")
print(f"Posts written to: {POSTS_DIR}")
