"""Download every Medium-hosted image referenced in post bodies, save under
static/images/posts/<post-slug>/<filename>, and rewrite markdown to point
at the local copies. Idempotent — re-runs are safe.
"""

import re
import urllib.request
from pathlib import Path

ROOT = Path("/Users/nedwin/projects/neddwyer-com")
POSTS = ROOT / "content" / "posts"
IMAGES_BASE = ROOT / "static" / "images" / "posts"

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Match cdn-images-1.medium.com OR miro.medium.com (Medium's two CDNs)
IMAGE_URL_RE = re.compile(
    r"https://(?:cdn-images-1|miro)\.medium\.com/(?:max/\d+/)?([^)\s\"']+)"
)


def sanitize_filename(raw):
    """Convert Medium's '1*hashprefix.jpeg' filename to a clean local name."""
    # Strip the leading 'N*' resolution prefix if present
    name = re.sub(r"^\d+\*", "", raw)
    # If the name has no extension, default to .png (Medium does this for some)
    if "." not in name:
        name = name + ".png"
    return name


def download(url, dest):
    """Download URL to dest. Skip if already present (idempotent)."""
    if dest.exists() and dest.stat().st_size > 0:
        return "cached"
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()
    dest.write_bytes(data)
    return f"downloaded ({len(data):,} bytes)"


total_images = 0
total_downloaded = 0

for post_path in sorted(POSTS.glob("*.md")):
    slug = post_path.stem
    text = post_path.read_text(encoding="utf-8")

    # Find all unique Medium image URLs in this post
    urls = list(dict.fromkeys(IMAGE_URL_RE.findall(text)))
    # The regex group is the path after /max/N/ or root — but we want full URLs too
    # Re-find with a broader pattern to get the full URLs
    full_urls = list(dict.fromkeys(
        re.findall(r"https://(?:cdn-images-1|miro)\.medium\.com/[^)\s\"']+", text)
    ))

    if not full_urls:
        continue

    print(f"\n=== {slug} ({len(full_urls)} image(s)) ===")

    post_dir = IMAGES_BASE / slug
    new_text = text

    for full_url in full_urls:
        # Extract the filename portion (last path segment)
        raw_name = full_url.rstrip("/").rsplit("/", 1)[-1]
        # Strip query strings
        raw_name = raw_name.split("?")[0]
        local_name = sanitize_filename(raw_name)
        dest = post_dir / local_name
        try:
            result = download(full_url, dest)
            print(f"  {result}: {local_name}")
            total_images += 1
            if result != "cached":
                total_downloaded += 1
        except Exception as e:
            print(f"  ! FAILED: {full_url}\n      {type(e).__name__}: {e}")
            continue

        # Rewrite the markdown
        local_url = f"/images/posts/{slug}/{local_name}"
        new_text = new_text.replace(full_url, local_url)

    if new_text != text:
        post_path.write_text(new_text, encoding="utf-8")
        print(f"  ✓ rewrote markdown")


print(f"\n{'='*40}")
print(f"Total images: {total_images}")
print(f"Newly downloaded: {total_downloaded}")
print(f"Already cached: {total_images - total_downloaded}")
print(f"\nFinal output dir: {IMAGES_BASE}")
