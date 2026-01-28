#!/usr/bin/env python3
import json
import re
from pathlib import Path
from datetime import datetime, timezone

POSTS_DIR = Path("_posts")
OUTPUT = Path("_data/wordcount.json")

FRONT_MATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)
CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]*`")
HTML_TAG_RE = re.compile(r"<[^>]+>")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
MD_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\([^)]+\)")
MULTISPACE_RE = re.compile(r"\s+")

def strip_front_matter(text: str) -> str:
    return re.sub(FRONT_MATTER_RE, "", text, count=1)

def normalize_markdown(text: str) -> str:
    # remove fenced code blocks (toggle if you want code included)
    text = re.sub(CODE_FENCE_RE, " ", text)
    text = re.sub(INLINE_CODE_RE, " ", text)
    # images: keep alt text
    text = re.sub(MD_IMAGE_RE, r"\1", text)
    # links: keep link text
    text = re.sub(MD_LINK_RE, r"\1", text)
    # strip basic markdown chars + any raw HTML
    text = text.replace("#", " ").replace("*", " ").replace("_", " ")
    text = re.sub(HTML_TAG_RE, " ", text)
    return text

def count_words(text: str) -> int:
    text = re.sub(MULTISPACE_RE, " ", text).strip()
    if not text:
        return 0
    return len(re.findall(r"[A-Za-z0-9']+", text))

def post_id_from_path(path: Path) -> str:
    """
    Jekyll post.id looks like: /YYYY/MM/DD/slug
    for a filename: YYYY-MM-DD-slug.md
    """
    name = path.stem  # YYYY-MM-DD-slug
    m = re.match(r"^(?P<y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})-(?P<slug>.+)$", name)
    if not m:
        # fallback: use stem as slug if naming is nonstandard
        return f"/unknown/unknown/unknown/{name}"
    y, mo, d, slug = m.group("y"), m.group("m"), m.group("d"), m.group("slug")
    return f"/{y}/{mo}/{d}/{slug}"

def main():
    if not POSTS_DIR.exists():
        raise SystemExit(f"_posts directory not found: {POSTS_DIR.resolve()}")

    posts_data = {}
    total_words = 0
    total_posts = 0

    for path in sorted(POSTS_DIR.rglob("*")):
        if path.suffix.lower() not in {".md", ".markdown", ".html"}:
            continue

        raw = path.read_text(encoding="utf-8", errors="ignore")
        text = strip_front_matter(raw)
        text = normalize_markdown(text)
        w = count_words(text)

        post_id = post_id_from_path(path)
        posts_data[post_id] = {
            "words": w,
            "path": str(path).replace("\\", "/"),
        }

        total_words += w
        total_posts += 1

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "total_words": total_words,
        "total_posts": total_posts,
        "posts": posts_data,
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT} ({total_posts} posts, {total_words} words)")

if __name__ == "__main__":
    main()
