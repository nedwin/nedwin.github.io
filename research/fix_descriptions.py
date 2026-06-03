"""Update description= frontmatter for the 9 posts with cruft.

Strip-and-trim approach: each new description is text Ned actually wrote
on Medium, with the image/cruft removed.
"""

import re
from pathlib import Path

ROOT = Path("/Users/nedwin/projects/neddwyer-com")
POSTS = ROOT / "content" / "posts"

updates = {
    "19-things-ive-done": "Since I was a little kid I've always looked for ways to make a buck.",
    "emerging-infrastructure-and-the-entrepreneurial-opportunity":
        "Less than 10 years ago one of the first steps in launching your web or mobile app was buying and setting up your own dedicated hardware in a back room or remote server farm.",
    "my-love-affair-with-large-competitive-fragmented-markets":
        "It's easy to think all the good startup problems in B2B SAAS have already been solved.",
    "seed-stage-investor-update-template":
        "Every month I write an update to our investors and advisors. I've been doing this since before Great Question was a company, before we wrote any lines of code.",
    "the-kanye-west-work-ethic-rap-camp":
        "In late 2009 Kanye West set himself up in a mansion in Hawaii to record one of the greatest albums of all times: My Beautiful Dark Twisted Fantasy.",
    "there-is-no-show-business-commission":
        "In the latest season of Comedians in Cars Getting Coffee, Alec Baldwin talks about the Show Business Commission.",
    "welcome-spritz-the-worlds-most-refreshing-corporate-card":
        "Today I'm excited to launch Spritz: the world's most refreshing corporate card. Every company in the world has expenses but no one likes doing them.",
    "what-the-quickbooks-accounting-community-can-learn-from-godaddy-pro":
        "With QuickBooks recent testing of an integrated bookkeeping service many accountants & bookkeepers have raised valid concerns about whether the platform they promote is about to compete with them.",
    "your-expense-policy-is-hurting-your-team":
        "For most companies their expense policy is an afterthought. It starts off informally.",
}


def update_post(slug, new_desc):
    p = POSTS / f"{slug}.md"
    if not p.exists():
        print(f"!! missing: {slug}")
        return
    text = p.read_text(encoding="utf-8")

    # Escape any double-quotes inside the new description
    safe_desc = new_desc.replace('"', '\\"')

    # Replace the description line (matches across multi-line descriptions too)
    new_text, count = re.subn(
        r'^description = "[^"]*"',
        f'description = "{safe_desc}"',
        text,
        count=1,
        flags=re.MULTILINE,
    )

    if count == 0:
        print(f"!! no description match in: {slug}")
        return

    p.write_text(new_text, encoding="utf-8")
    print(f"✓ {slug}  ({len(new_desc)} chars)")


for slug, desc in updates.items():
    update_post(slug, desc)

print("\nDone.")
