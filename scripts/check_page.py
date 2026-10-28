#!/usr/bin/env python3
"""Check a GitBook training page against the house rules.

Usage: python check_page.py "path/to/1. Page Title.md" [more pages ...]

Exits with code 1 when any page has an error. Warnings never fail the run.
"""
import pathlib
import re
import sys

ALLOWED_HEX = {
    "#c8e6c9", "#2e7d32",  # green
    "#bbdefb", "#1565c0",  # blue
    "#fff9c4", "#f9a825",  # yellow
    "#e1bee7", "#6a1b9a",  # purple
    "#ffcdd2", "#c62828",  # red
    "#1a1a1a",             # text
}
ALLOWED_RGB = {
    (200, 230, 201), (187, 222, 251), (255, 249, 196),
    (225, 190, 231), (255, 205, 210),
}
SMALL_WORDS = {
    "a", "an", "and", "as", "at", "but", "by", "for", "in",
    "nor", "of", "on", "or", "the", "to", "vs", "with",
}
RESIDUE = [
    "i hope this helps", "let me know if", "great question", "certainly!",
    "of course!", "let's dive", "here's what you need to know",
]


def split_blocks(text):
    """Return (prose_lines, mermaid_blocks) with code fences removed from prose."""
    prose, mermaid = [], []
    in_fence, lang, buf = False, "", []
    for line in text.splitlines():
        m = re.match(r"^\s*(`{3,}|~{3,})\s*([\w-]*)", line)
        if m and not in_fence:
            in_fence, lang, buf = True, m.group(2).lower(), []
            continue
        if m and in_fence and not m.group(2):
            if lang == "mermaid":
                mermaid.append("\n".join(buf))
            in_fence = False
            continue
        if in_fence:
            buf.append(line)
        else:
            prose.append(line)
    return prose, mermaid


def check_name(name, errors, warnings):
    if not re.match(r"^\d+\. \S.*\.md$", name):
        errors.append("File name must look like '<number>. <Title Case Name>.md'.")
        return
    title = re.sub(r"^\d+\. ", "", name)[:-3]
    words = title.split(" ")
    for i, w in enumerate(words):
        bare = re.sub(r"[^A-Za-z]", "", w)
        if not bare:
            continue
        if i == 0 and not w[0].isupper():
            errors.append(f"File name word '{w}' should start with a capital letter.")
        elif i > 0 and bare.lower() in SMALL_WORDS:
            if w[0].isupper():
                warnings.append(f"File name: small word '{w}' is usually lowercase.")
        elif w[0].isalpha() and w[0].islower():
            errors.append(f"File name word '{w}' should be capitalized.")
    if len(title) > 50:
        warnings.append("File name is long and may truncate in the GitBook sidebar.")


def check_mermaid(blocks, errors, warnings):
    for n, block in enumerate(blocks, 1):
        label = f"Mermaid block {n}"
        for h in re.findall(r"#[0-9a-fA-F]{3,8}\b", block):
            if h.lower() not in ALLOWED_HEX:
                errors.append(f"{label}: color {h} is outside the palette.")
        for r in re.findall(r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", block):
            if tuple(int(x) for x in r) not in ALLOWED_RGB:
                errors.append(f"{label}: rgb{r} is outside the palette.")
        for named in re.findall(r"(?:fill|stroke|color)\s*:\s*([A-Za-z]+)", block):
            errors.append(f"{label}: named color '{named}' used, use palette hex values.")
        first = block.strip().split("\n", 1)[0].strip().lower()
        is_flow = first.startswith(("flowchart", "graph"))
        if is_flow and "classdef" not in block.lower():
            errors.append(f"{label}: flowchart has no classDef, so nodes fall back to default grey.")
        if is_flow:
            nodes = len(re.findall(r"\b[A-Za-z][\w]*\s*[\[\(\{]", block))
            if nodes > 14:
                warnings.append(f"{label}: about {nodes} nodes, consider splitting it.")


def check_page(path):
    errors, warnings = [], []
    p = pathlib.Path(path)
    text = p.read_text(encoding="utf-8")

    check_name(p.name, errors, warnings)

    if not re.match(r"^---\s*\n(?:.*\n)*?description:\s*\S", text):
        errors.append("Missing front matter with a description.")

    prose, mermaid = split_blocks(text)

    for i, line in enumerate(prose, 1):
        if re.match(r"^# \S", line):
            warnings.append("Top-level '# ' heading found. GitBook already shows the file name as the title.")
            break

    for line in prose:
        stripped = re.sub(r"`[^`]*`", "", line)
        if "—" in stripped or "–" in stripped or " -- " in stripped:
            errors.append(f"Dash used as a connector: {line.strip()[:70]}")
            break

    low = "\n".join(prose).lower()
    for phrase in RESIDUE:
        if phrase in low:
            warnings.append(f"Chatbot phrase found: '{phrase}'.")

    check_mermaid(mermaid, errors, warnings)
    if not mermaid:
        warnings.append("No Mermaid diagram found.")

    if not re.search(r"https://\S+", text):
        warnings.append("No https link found. Pages need an official docs link.")
    if not re.search(r"^##\s+Official docs", text, re.M | re.I):
        warnings.append("No '## Official docs' section.")
    if "{% hint" not in text:
        warnings.append("No GitBook hint block. Pages open with trainer notes.")
    elif "Trainer notes" not in text:
        warnings.append("No 'Trainer notes' hint at the top.")

    if re.search(r"^##\s+Lab", text, re.M | re.I):
        for needle, msg in [
            ("### Prerequisites", "Lab has no Prerequisites section."),
            ("Expected result", "Lab steps have no 'Expected result'."),
            ("### Verify", "Lab has no Verify section."),
            ("### Cleanup", "Lab has no Cleanup section."),
            ("### Troubleshooting", "Lab has no Troubleshooting section."),
        ]:
            if needle.lower() not in text.lower():
                warnings.append(msg)
        for word in ("obviously", "simply", "just "):
            if re.search(rf"\b{word}", text, re.I):
                warnings.append(f"Word '{word.strip()}' found. It tends to hide an assumption.")

    return errors, warnings


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    failed = False
    for path in argv[1:]:
        errors, warnings = check_page(path)
        print(f"\n{path}")
        for e in errors:
            print(f"  ERROR   {e}")
        for w in warnings:
            print(f"  warning {w}")
        if not errors and not warnings:
            print("  OK")
        failed = failed or bool(errors)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
