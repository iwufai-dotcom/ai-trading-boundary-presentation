#!/usr/bin/env python3
"""Publish a standalone HTML file into the GitHub Pages directory layout."""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from datetime import date, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "site-manifest.json"
HTML_ARCHIVE = ROOT / "html"
UPLOAD_LOG = ROOT / "upload-log.md"


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "untitled-page"


def extract_title(source: Path) -> str:
    text = source.read_text(encoding="utf-8", errors="ignore")
    match = re.search(r"<title[^>]*>(.*?)</title>", text, re.IGNORECASE | re.DOTALL)
    if not match:
        return source.stem
    return re.sub(r"\s+", " ", match.group(1)).strip()


def parse_mapping(value: str, separator: str) -> tuple[str, str]:
    if separator not in value:
        raise argparse.ArgumentTypeError(f"Expected mapping in the form left{separator}right")
    left, right = value.split(separator, 1)
    left = left.strip()
    right = right.strip()
    if not left or not right:
        raise argparse.ArgumentTypeError(f"Expected non-empty mapping in the form left{separator}right")
    return left, right


def parse_resource_mapping(value: str) -> tuple[Path, Path]:
    source, relative_target = parse_mapping(value, ":")
    target = Path(relative_target)
    if target.is_absolute() or ".." in target.parts:
        raise argparse.ArgumentTypeError("Resource target must be a safe relative path")
    return Path(source).expanduser(), target


def parse_replacement(value: str) -> tuple[str, str]:
    return parse_mapping(value, "=")


def load_manifest() -> dict:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {"updated_at": "", "items": []}


def save_manifest(manifest: dict) -> None:
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def render_index(manifest: dict) -> None:
    items = [item for item in manifest.get("items", []) if item.get("status") == "active"]
    cards = []
    for item in sorted(items, key=lambda entry: entry.get("updated_at", ""), reverse=True):
        title = html.escape(item["title"])
        path = html.escape(item["path"])
        updated = html.escape(item.get("updated_at", ""))
        cards.append(f"""      <article class="item">
        <div>
          <a class="title" href="{path}">{title}</a>
          <div class="meta">{path} · updated {updated}</div>
        </div>
        <a class="open" href="{path}">打开页面</a>
      </article>""")

    body = "\n".join(cards) or "      <p>暂无已发布页面。</p>"
    (ROOT / "index.html").write_text(f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AI Trading Boundary HTML 发布索引</title>
  <style>
    :root {{
      --bg: #f4f4f1;
      --panel: #ffffff;
      --ink: #202326;
      --text: #5a6066;
      --muted: #8d949b;
      --line: #d8d9d6;
      --accent: #b84a3a;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", Arial, sans-serif;
      line-height: 1.6;
    }}
    main {{
      width: min(960px, calc(100vw - 40px));
      margin: 56px auto;
    }}
    header {{
      border-bottom: 1px solid var(--line);
      padding-bottom: 20px;
      margin-bottom: 24px;
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: 32px;
      font-weight: 650;
      letter-spacing: 0;
    }}
    p {{
      margin: 0;
      color: var(--text);
      font-size: 15px;
    }}
    .list {{
      display: grid;
      gap: 12px;
    }}
    .item {{
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 16px;
      align-items: center;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 18px 20px;
    }}
    .title {{
      display: block;
      color: var(--ink);
      font-size: 18px;
      font-weight: 600;
      text-decoration: none;
    }}
    .title:hover {{ color: var(--accent); }}
    .meta {{
      margin-top: 4px;
      color: var(--muted);
      font-size: 13px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    }}
    .open {{
      color: var(--accent);
      text-decoration: none;
      font-size: 14px;
      font-weight: 600;
      white-space: nowrap;
    }}
    @media (max-width: 640px) {{
      main {{ margin: 32px auto; }}
      .item {{ grid-template-columns: 1fr; }}
      h1 {{ font-size: 26px; }}
    }}
  </style>
</head>
<body>
  <main>
    <header>
      <h1>AI Trading Boundary HTML 发布索引</h1>
      <p>「AI 与人在交易中的效率与边界」项目的公开 HTML 页面；每个页面都有固定路径，历史版本由 Git 保存。</p>
    </header>
    <section class="list" aria-label="Published pages">
{body}
    </section>
  </main>
</body>
</html>
""", encoding="utf-8")


def archive_source_html(source: Path, slug: str) -> str:
    HTML_ARCHIVE.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    archive_name = f"{timestamp}_{slug}.html"
    archive_path = HTML_ARCHIVE / archive_name
    shutil.copyfile(source, archive_path)
    return archive_path.relative_to(ROOT).as_posix()


def copy_resource(source: Path, target_dir: Path, relative_target: Path) -> str:
    source = source.expanduser().resolve()
    if not source.exists():
        raise SystemExit(f"Resource does not exist: {source}")

    target = target_dir / relative_target
    target.parent.mkdir(parents=True, exist_ok=True)
    if source.is_dir():
        shutil.copytree(source, target, dirs_exist_ok=True)
    else:
        shutil.copy2(source, target)
    return relative_target.as_posix()


def read_public_html(source: Path, replacements: list[tuple[str, str]]) -> str:
    text = source.read_text(encoding="utf-8", errors="ignore")
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def append_upload_log(
    title: str,
    slug: str,
    source: Path,
    archive_path: str,
    resource_paths: list[str],
    replacements: list[tuple[str, str]],
) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    public_path = f"pages/{slug}/"
    if not UPLOAD_LOG.exists():
        UPLOAD_LOG.write_text("# HTML 上传记录\n\n", encoding="utf-8")
    with UPLOAD_LOG.open("a", encoding="utf-8") as log:
        log.write(f"## {timestamp} - {title}\n\n")
        log.write(f"- slug: `{slug}`\n")
        log.write(f"- source_name: `{source.name}`\n")
        log.write(f"- archived_html: `{archive_path}`\n")
        log.write(f"- public_path: `{public_path}`\n")
        if resource_paths:
            log.write(f"- resources: `{', '.join(resource_paths)}`\n")
        if replacements:
            rendered = ", ".join(f"`{old}` -> `{new}`" for old, new in replacements)
            log.write(f"- path_replacements: {rendered}\n")
        log.write("- risk_check: pending manual review before push\n\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Publish an HTML file to pages/<slug>/index.html")
    parser.add_argument("source", type=Path)
    parser.add_argument("--slug", help="Stable URL slug. Reusing it updates the existing page.")
    parser.add_argument("--title", help="Display title in the root index.")
    parser.add_argument(
        "--resource",
        action="append",
        default=[],
        type=parse_resource_mapping,
        help="Copy a file or directory into the public page, formatted as /source/path:relative/target/path",
    )
    parser.add_argument(
        "--replace",
        action="append",
        default=[],
        type=parse_replacement,
        help="Replace text only in the public page HTML, formatted as old=new",
    )
    args = parser.parse_args()

    source = args.source.expanduser().resolve()
    if not source.exists():
        raise SystemExit(f"Source file does not exist: {source}")
    if source.suffix.lower() not in {".html", ".htm"}:
        raise SystemExit("Source file must be .html or .htm")

    title = args.title or extract_title(source)
    slug = slugify(args.slug or source.stem)
    archive_path = archive_source_html(source, slug)
    target_dir = ROOT / "pages" / slug
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "index.html").write_text(read_public_html(source, args.replace), encoding="utf-8")
    resource_paths = [copy_resource(src, target_dir, rel) for src, rel in args.resource]

    today = date.today().isoformat()
    manifest = load_manifest()
    manifest["updated_at"] = today
    items = manifest.setdefault("items", [])
    next_item = {
        "slug": slug,
        "title": title,
        "path": f"pages/{slug}/",
        "source_archive": archive_path,
        "status": "active",
        "updated_at": today,
    }
    for index, item in enumerate(items):
        if item.get("slug") == slug:
            items[index] = {**item, **next_item}
            break
    else:
        items.append(next_item)

    save_manifest(manifest)
    render_index(manifest)
    append_upload_log(title, slug, source, archive_path, resource_paths, args.replace)
    print(f"Published {source} -> pages/{slug}/index.html")
    print(f"Archived source HTML -> {archive_path}")
    for resource_path in resource_paths:
        print(f"Copied resource -> pages/{slug}/{resource_path}")


if __name__ == "__main__":
    main()
