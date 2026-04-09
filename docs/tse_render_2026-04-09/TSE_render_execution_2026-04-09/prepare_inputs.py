from __future__ import annotations

import re
from pathlib import Path


ROOT = Path("/Users/zhangbin/Desktop/TSE_render_handoff_2026-04-09")
OUT = Path("/Users/zhangbin/Desktop/TSE_render_execution_2026-04-09/generated")


def parse_main(md_path: Path) -> tuple[str, str, str]:
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError("Main manuscript title line not found")
    title = lines[0][2:].strip()

    try:
        abstract_start = lines.index("## Abstract") + 1
        intro_start = lines.index("## 1. Introduction")
    except ValueError as exc:
        raise ValueError("Expected abstract/introduction headings not found") from exc

    abstract = "\n".join(lines[abstract_start:intro_start]).strip()
    body = "\n".join(lines[intro_start:]).strip()
    return title, abstract, body


def parse_metadata(txt_path: Path) -> dict[str, str]:
    text = txt_path.read_text(encoding="utf-8")
    data: dict[str, str] = {}
    for line in text.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return data


def count_words(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'-]*", text))


def main() -> None:
    title, abstract, body = parse_main(
        ROOT / "manuscript/tse_flagship/tse_flagship_main.md"
    )
    appendix_text = (
        ROOT / "manuscript/tse_flagship/tse_flagship_appendix.md"
    ).read_text(encoding="utf-8")
    appendix_lines = appendix_text.splitlines()
    appendix_title = appendix_lines[0][2:].strip() if appendix_lines and appendix_lines[0].startswith("# ") else "Appendix: Bounded Artifact Review Notes"
    appendix_body = "\n".join(appendix_lines[1:]).strip()
    meta = parse_metadata(ROOT / "submission/tse_submission_metadata_current.txt")

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "main_body.md").write_text(body + "\n", encoding="utf-8")
    (OUT / "appendix_body.md").write_text(appendix_body + "\n", encoding="utf-8")
    (OUT / "main_title.txt").write_text(title + "\n", encoding="utf-8")
    (OUT / "main_abstract.txt").write_text(abstract + "\n", encoding="utf-8")
    (OUT / "author.txt").write_text(meta.get("Author", "Bin Zhang") + "\n", encoding="utf-8")
    (OUT / "affiliation.txt").write_text(
        meta.get("Affiliation", "Independent Researcher") + "\n", encoding="utf-8"
    )
    (OUT / "abstract_word_count.txt").write_text(
        str(count_words(abstract)) + "\n", encoding="utf-8"
    )
    (OUT / "main_metadata.yaml").write_text(
        "\n".join(
            [
                "---",
                f'title: "{title}"',
                f'author: "{meta.get("Author", "Bin Zhang")}"',
                'date: ""',
                'documentclass: "IEEEtran"',
                "classoption:",
                '  - "journal"',
                "abstract: |",
                *[f"  {line}" for line in abstract.splitlines()],
                "...",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (OUT / "appendix_metadata.yaml").write_text(
        "\n".join(
            [
                "---",
                f'title: "{appendix_title}"',
                f'author: "{meta.get("Author", "Bin Zhang")}"',
                'date: ""',
                'documentclass: "IEEEtran"',
                "classoption:",
                '  - "journal"',
                "...",
                "",
            ]
        ),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
