#!/usr/bin/env python3
"""Turn a lychee JSON report into a Markdown summary.

Sorts results into three groups:
  broken        - the link is dead: 404/410, missing local file or anchor,
                  domain no longer resolves. These need fixing.
  unverifiable  - the checker could not tell: 401/403/429/5xx, timeouts,
                  TLS or other network errors. Usually a site blocking bots;
                  check by hand in a browser.
  redirected    - the link works but now lands on a different page, which
                  often means a product was renamed or moved. Worth a look.
                  (Needs lychee's --verbose output, which records redirects.)

Each entry names the use case (the inventory row) it was cited in.

Usage:
  link_report.py REPORT.json [--title TEXT] [--output FILE] [--fail-on-broken]
                 [--docs-dir DIR]

With --fail-on-broken the script exits 1 when anything is broken, so it can
gate a pull request. Unverifiable and redirected links never cause a failure.
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from urllib.parse import urlsplit

BROKEN_CODES = {404, 410}
BROKEN_TEXT = re.compile(
    r"file not found|dns resolution failed|failed to lookup address|"
    r"no such host|name or service not known",
    re.IGNORECASE,
)
MISSING_ANCHOR = re.compile(r"cannot find fragment", re.IGNORECASE)
ROW_NAME = re.compile(r"^\|\s*\*\*(.+?)\*\*\s*\|")  # | **Use case name** | ...


def classify(url, status):
    text = f"{status.get('text', '')} {status.get('details', '')}"
    if status.get("code") in BROKEN_CODES or BROKEN_TEXT.search(text):
        return "broken"
    if MISSING_ANCHOR.search(text):
        # Anchors in our own Markdown are reliable to check. Anchors on
        # external pages are often added by JavaScript, so don't trust those.
        return "broken" if url.startswith("file://") else "unverifiable"
    return "unverifiable"


def short_reason(status):
    if status.get("code"):
        return f"HTTP {status['code']}"
    text = status.get("text", "error")
    return text.split(" (")[0].split(". ")[0][:80]


def _comparable(url):
    """Normalise away redirects that don't mean anything moved."""
    parts = urlsplit(url)
    host = parts.netloc.lower().removeprefix("www.")
    path = parts.path.rstrip("/") or "/"
    return host, path, parts.query


def meaningful_redirect(origin, final):
    """True when a redirect lands on a different page, not just https/www/slash."""
    return _comparable(origin) != _comparable(final)


class Docs:
    """Reads Markdown files on demand to locate links and name their rows."""

    def __init__(self, root):
        self.root = root
        self._lines = {}

    def lines(self, path):
        if path not in self._lines:
            try:
                with open(path, encoding="utf-8") as fh:
                    self._lines[path] = fh.read().splitlines()
            except OSError:
                self._lines[path] = []
        return self._lines[path]

    def use_case(self, location):
        """'file.md:129' -> 'Lead research & enrichment' if that line is an inventory row."""
        path, _, line = location.rpartition(":")
        if not line.isdigit():
            return ""
        lines = self.lines(path)
        number = int(line)
        if 0 < number <= len(lines):
            match = ROW_NAME.match(lines[number - 1])
            if match:
                return match.group(1)
        return ""

    def find(self, url, docs_dir):
        """file:line locations of url in Markdown files under docs_dir."""
        hits = []
        for dirpath, _, files in os.walk(docs_dir):
            for name in sorted(files):
                if name.endswith(".md"):
                    path = os.path.relpath(os.path.join(dirpath, name))
                    for number, text in enumerate(self.lines(path), start=1):
                        if url in text:
                            hits.append(f"{path}:{number}")
        return hits

    def display(self, url):
        """Show local file links relative to the repo, web links as-is."""
        if url.startswith("file://"):
            path = url[len("file://"):]
            if self.root and path.startswith(self.root):
                path = path[len(self.root):].lstrip("/")
            return f"`{path}`"
        return url


def _where(entry, source):
    line = (entry.get("span") or {}).get("line")
    return f"{source}:{line}" if line else source


def collect(report, docs, docs_dir=None):
    """Return {group: {url: {"reason": str, "where": [file:line, ...]}}}."""
    found = {}  # url -> {"group", "reason", "where"}
    for map_name in ("error_map", "timeout_map"):
        for source, entries in (report.get(map_name) or {}).items():
            for entry in entries:
                url = entry["url"]
                status = entry.get("status") or {}
                item = found.setdefault(url, {"group": None, "reason": None, "where": []})
                # lychee reports repeats of an earlier failure as "Error (cached)";
                # those only add a location, the first real result sets the reason.
                if "cached" not in status.get("text", "").lower() and item["group"] is None:
                    item["group"] = (
                        "unverifiable" if map_name == "timeout_map" else classify(url, status)
                    )
                    item["reason"] = short_reason(status)
                item["where"].append(_where(entry, source))

    # Links that worked, but only after redirecting somewhere else.
    for source, entries in (report.get("success_map") or {}).items():
        for entry in entries:
            hops = (entry.get("redirects") or {}).get("redirects") or []
            if not hops or entry["url"].startswith("file://"):
                continue
            final = hops[-1].get("url", "")
            if not meaningful_redirect(entry["url"], final):
                continue
            item = found.setdefault(
                entry["url"], {"group": "redirected", "reason": final, "where": []}
            )
            item["where"].append(_where(entry, source))

    groups = {"broken": {}, "unverifiable": {}, "redirected": {}}
    for url, item in found.items():
        if docs_dir and not url.startswith("file://"):
            # When the checked input was a scratch file (e.g. the lines a PR
            # added), point at where the link really lives in the docs.
            item["where"] = docs.find(url, docs_dir) or item["where"]
        groups[item["group"] or "unverifiable"][url] = {
            "reason": item["reason"] or "Error",
            "where": item["where"],
        }
    return groups


def _location_key(loc):
    path, _, line = loc.rpartition(":")
    return (path, int(line)) if line.isdigit() else (loc, 0)


def table(items, docs, reason_header="Problem"):
    rows = [f"| Use case | Link | {reason_header} | Where |", "|---|---|---|---|"]
    entries = []
    for url, info in items.items():
        where = sorted(set(info["where"]), key=_location_key)
        names = sorted({n for n in (docs.use_case(w) for w in where) if n})
        entries.append(("<br>".join(names) or "—", url, info["reason"], where))
    for names, url, reason, where in sorted(entries, key=lambda e: (e[0], e[1])):
        rows.append(f"| {names} | {docs.display(url)} | {reason} | {'<br>'.join(where)} |")
    return "\n".join(rows)


def _checked(report):
    """Links actually checked (excludes skipped ones, e.g. web links in --offline mode)."""
    return sum(report.get(k, 0) or 0 for k in ("successful", "errors", "timeouts"))


def _plural(n, word):
    return f"{n} {word}{'' if n == 1 else 's'}"


def render(report, groups, title, docs):
    broken = groups["broken"]
    unverifiable = groups["unverifiable"]
    redirected = groups["redirected"]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    run = ""
    if os.environ.get("GITHUB_RUN_ID"):
        run_url = (
            f"{os.environ.get('GITHUB_SERVER_URL', 'https://github.com')}/"
            f"{os.environ.get('GITHUB_REPOSITORY')}/actions/runs/{os.environ['GITHUB_RUN_ID']}"
        )
        run = f" · [workflow run]({run_url})"

    out = [
        f"## {title}",
        "",
        f"**{len(broken)} broken · {len(unverifiable)} could not be verified · "
        f"{len(redirected)} redirected · {_checked(report)} links checked**",
        "",
        f"_Checked {now}{run}_",
        "",
        "### Broken: please fix",
        "",
    ]
    if broken:
        out += [
            "These links are dead (page or anchor not found, or the domain is gone). "
            "Find where the page moved, or cite a Wayback Machine snapshot "
            "(https://web.archive.org/) and keep the original \"retrieved\" date.",
            "",
            table(broken, docs),
        ]
    else:
        out.append("None. :tada:")

    out += ["", "### Could not verify automatically", ""]
    if unverifiable:
        out += [
            "Usually a site blocking automated requests or rate limiting, not a dead page. "
            "Open these in a browser if you are editing nearby rows; no action is needed otherwise.",
            "",
            f"<details><summary>Show {_plural(len(unverifiable), 'link')}</summary>",
            "",
            table(unverifiable, docs),
            "",
            "</details>",
        ]
    else:
        out.append("None.")

    out += ["", "### Redirected", ""]
    if redirected:
        out += [
            "These still work but land on a different page, which can mean the product was "
            "renamed or the page was folded into another one. Check the new page still "
            "supports the row, then update the citation to the new URL.",
            "",
            f"<details><summary>Show {_plural(len(redirected), 'link')}</summary>",
            "",
            table(redirected, docs, reason_header="Now goes to"),
            "",
            "</details>",
        ]
    else:
        out.append("None.")

    out += [
        "",
        "---",
        "_Generated by `.github/workflows/use-cases-link-check.yml`. "
        "To skip a URL that can never be checked automatically, add a pattern to `.lycheeignore`._",
        "",
    ]
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("report", help="lychee report written with --format json")
    parser.add_argument("--title", default="Link check")
    parser.add_argument("--output", help="write Markdown here (default: stdout)")
    parser.add_argument("--fail-on-broken", action="store_true")
    parser.add_argument(
        "--docs-dir",
        help="look up where each external link appears in Markdown under this folder",
    )
    args = parser.parse_args()

    with open(args.report, encoding="utf-8") as fh:
        report = json.load(fh)

    docs = Docs(os.environ.get("GITHUB_WORKSPACE") or os.getcwd())
    groups = collect(report, docs, args.docs_dir)
    markdown = render(report, groups, args.title, docs)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(markdown)
    else:
        sys.stdout.write(markdown)

    print(
        " ".join(f"{name}={len(items)}" for name, items in groups.items()),
        file=sys.stderr,
    )
    if args.fail_on_broken and groups["broken"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
