"""Extract every link from every built page and check it returns 200.

Runs against the local Hugo public/ build (already produced by `hugo`).
Reports: broken internal links, broken external links, and a count.
"""

import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = Path("/Users/nedwin/projects/neddwyer-com/public")
BASE_URL = "https://neddwyer.com"

# Skip these (known not to support HEAD or commonly rate-limit)
SKIP_HOSTS = {"twitter.com", "x.com", "linkedin.com", "www.linkedin.com",
              "podcasts.apple.com", "informaconnect.com", "rosenfeldmedia.com"}

links_by_page = {}  # page_path → set of (link_text, url)
all_external = set()
all_internal = set()


def collect_links(html_path):
    """Pull every href= URL from an HTML file."""
    html = html_path.read_text(encoding="utf-8", errors="replace")
    # Limit to <body> if possible
    m = re.search(r"<body[^>]*>(.*)</body>", html, flags=re.DOTALL)
    body = m.group(1) if m else html
    hrefs = re.findall(r'href="([^"#?]+)(?:[#?][^"]*)?"', body)
    return hrefs


def categorize(url):
    """Return ('internal'|'external'|'skip', normalized_url)."""
    url = url.strip()
    if not url:
        return "skip", url
    if url.startswith(("mailto:", "tel:", "javascript:")):
        return "skip", url
    if url.startswith("/"):
        return "internal", url
    if url.startswith(("http://", "https://")):
        parsed = urllib.parse.urlparse(url)
        if parsed.netloc in SKIP_HOSTS:
            return "skip", url
        # Treat neddwyer.com as internal too
        if parsed.netloc in ("neddwyer.com", "www.neddwyer.com"):
            return "internal", parsed.path or "/"
        return "external", url
    return "skip", url


# 1. Walk every .html file under public/ and gather links
for html_file in ROOT.rglob("*.html"):
    rel = html_file.relative_to(ROOT)
    hrefs = collect_links(html_file)
    page_id = "/" + str(rel).replace("index.html", "").rstrip("/")
    links_by_page[page_id] = []
    for h in hrefs:
        kind, norm = categorize(h)
        if kind == "internal":
            all_internal.add(norm)
            links_by_page[page_id].append(("internal", norm))
        elif kind == "external":
            all_external.add(norm)
            links_by_page[page_id].append(("external", norm))

print(f"Pages crawled: {len(links_by_page)}")
print(f"Unique internal links: {len(all_internal)}")
print(f"Unique external links: {len(all_external)}")
print()


# 2. Check internal links exist on disk
print("=== INTERNAL LINK CHECK ===")
missing_internal = []
for url in sorted(all_internal):
    path = url.lstrip("/")
    # Try as a file, or as a directory with index.html
    p1 = ROOT / path
    p2 = ROOT / path / "index.html"
    p3 = ROOT / (path + ".html") if not path.endswith(".html") else None
    if p1.is_file() or p2.is_file() or (p3 and p3.is_file()):
        continue
    missing_internal.append(url)
if not missing_internal:
    print(f"  All {len(all_internal)} internal links resolve to a file ✓")
else:
    for m in missing_internal:
        print(f"  ✗ {m}")
print()


# 3. Check external links (HEAD; fall back to GET)
print("=== EXTERNAL LINK CHECK ===")


def check_one(url):
    """Try HEAD, then GET. Return (url, status_code | error_str)."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    try:
        req = urllib.request.Request(url, method="HEAD", headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            return url, resp.status
    except urllib.error.HTTPError as e:
        # 405 = method not allowed, try GET
        if e.code in (405, 403):
            try:
                req = urllib.request.Request(url, method="GET", headers=headers)
                with urllib.request.urlopen(req, timeout=10) as resp:
                    return url, resp.status
            except Exception as e2:
                return url, f"GET failed: {e2}"
        return url, f"HTTP {e.code}"
    except Exception as e:
        return url, f"ERR: {type(e).__name__}: {e}"


broken = []
ok_count = 0
with ThreadPoolExecutor(max_workers=10) as ex:
    futures = {ex.submit(check_one, u): u for u in sorted(all_external)}
    for fut in as_completed(futures):
        url, status = fut.result()
        if isinstance(status, int) and 200 <= status < 400:
            ok_count += 1
        else:
            broken.append((url, status))

print(f"  OK: {ok_count}/{len(all_external)}")
if broken:
    print(f"  Broken / error:")
    for url, status in sorted(broken):
        print(f"    ✗ [{status}] {url}")
else:
    print("  All external links return success codes ✓")
print()


# 4. Report which pages have broken links
if missing_internal or broken:
    print("=== AFFECTED PAGES ===")
    broken_urls = set(missing_internal) | {url for url, _ in broken}
    for page, links in sorted(links_by_page.items()):
        page_broken = [(k, u) for k, u in links if u in broken_urls]
        if page_broken:
            print(f"  {page}")
            for k, u in page_broken:
                print(f"    {k}: {u}")
