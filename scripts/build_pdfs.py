#!/usr/bin/env python3
"""Converts the pt-BR delivery docs (docs/pt-BR/*.md) to PDF via pandoc + xelatex.

Mermaid code fences are swapped for the pre-rendered PNG in docs/assets/,
since pandoc/LaTeX can't render mermaid directly. Run scripts/render_diagrams.sh
first if a diagram source changes.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "docs" / "pt-BR"
OUT_DIR = ROOT / "dist" / "pdf"
HEADER = ROOT / "scripts" / "pandoc-header.tex"

MERMAID_IMAGE = {
    "database-design.md": "database-design-er.png",
}

DOCS = [
    "kanban-board.md",
    "vision-and-scope.md",
    "non-functional-requirements.md",
    "user-stories.md",
    "architecture-notebook.md",
    "ui-design.md",
    "database-design.md",
    "infrastructure.md",
    "autoria.md",
]

TITLES = {
    "kanban-board.md": "Quadro Kanban",
    "vision-and-scope.md": "Visão e Escopo",
    "non-functional-requirements.md": "Requisitos Não Funcionais",
    "user-stories.md": "Histórias de Usuário",
    "architecture-notebook.md": "Architecture Notebook",
    "ui-design.md": "Projeto de Interface",
    "database-design.md": "Projeto Físico de Banco de Dados",
    "infrastructure.md": "Infraestrutura de Implantação",
    "autoria.md": "Autoria",
}


def prepare_markdown(name: str) -> Path:
    text = (SRC_DIR / name).read_text()
    image = MERMAID_IMAGE.get(name)
    if image:
        image_path = (ROOT / "docs" / "assets" / image).resolve()
        text = re.sub(
            r"```mermaid\n.*?\n```",
            f"![Diagrama entidade-relacionamento]({image_path}){{ width=70% }}",
            text,
            flags=re.S,
        )
    tmp = OUT_DIR / f"_{name}"
    tmp.write_text(text)
    return tmp


def build(name: str) -> None:
    src = prepare_markdown(name)
    out = OUT_DIR / (Path(name).stem + ".pdf")
    subprocess.run(
        [
            "pandoc", str(src),
            "-o", str(out),
            "--pdf-engine=xelatex",
            "-V", "geometry:margin=2.5cm",
            "-V", f"title={TITLES[name]}",
            "-V", "colorlinks=true",
            "-V", "mainfont=DejaVu Sans",
            "-V", "monofont=DejaVu Sans Mono",
            "-H", str(HEADER),
        ],
        check=True,
        cwd=OUT_DIR,
    )
    src.unlink()
    print(f"built {out}")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    targets = sys.argv[1:] or DOCS
    for name in targets:
        build(name)


if __name__ == "__main__":
    main()
