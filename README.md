# BacklogForge

Practical assignment for the Software Engineering course (CIC0105) — a web system for **agile requirements management** (projects, product backlogs, sprint backlogs, epics, user stories with acceptance criteria, story points, MoSCoW, and RICE).

- **Mode**: individual.
- **Platform**: web (browser-based GUI).
- **Stack**: Python + Flask + Jinja2 (server-rendered) + SQLite — see [`docs/en/tech-stack.md`](docs/en/tech-stack.md) for the rationale.
- **Own-work management methodology**: Kanban — see [`docs/en/kanban-board.md`](docs/en/kanban-board.md).

## Current Status

All planning/design artifacts are done, and the Flask prototype is implemented and tested (all 38 user stories, 9 epics — see [`docs/en/kanban-board.md`](docs/en/kanban-board.md)). Only the demo video and final ZIP packaging remain.

## Running Locally

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
cp env.sample .env   # then edit SECRET_KEY, ADMIN_EMAIL, ADMIN_PASSWORD, etc.
pytest               # 12 tests: auth, RBAC, CRUD, RICE, encryption
flask --app run.py run
```

The first run seeds an `admin` account from `ADMIN_EMAIL`/`ADMIN_PASSWORD` (see [`docs/en/infrastructure.md`](docs/en/infrastructure.md)).

## Documentation

The assignment must be delivered in Portuguese (pt-BR) to the professor. This repo keeps two versions of each deliverable doc:

- [`docs/pt-BR/`](docs/pt-BR) — **canonical** version, used for grading/delivery.
- [`docs/en/`](docs/en) — English translation, for repo readability.
- [`docs/spec/`](docs/spec) — the original assignment spec (`ESW-TRABALHO-PRATICO.pdf`/`.md`, pt-BR, converted from the professor's password-protected PDF).

| Document | pt-BR (delivery) | English |
|---|---|---|
| Kanban board | [`docs/pt-BR/kanban-board.md`](docs/pt-BR/kanban-board.md) | [`docs/en/kanban-board.md`](docs/en/kanban-board.md) |
| Vision and scope | [`docs/pt-BR/vision-and-scope.md`](docs/pt-BR/vision-and-scope.md) | [`docs/en/vision-and-scope.md`](docs/en/vision-and-scope.md) |
| Non-functional requirements | [`docs/pt-BR/non-functional-requirements.md`](docs/pt-BR/non-functional-requirements.md) | [`docs/en/non-functional-requirements.md`](docs/en/non-functional-requirements.md) |
| User story backlog | [`docs/pt-BR/user-stories.md`](docs/pt-BR/user-stories.md) | [`docs/en/user-stories.md`](docs/en/user-stories.md) |
| Architecture notebook | [`docs/pt-BR/architecture-notebook.md`](docs/pt-BR/architecture-notebook.md) | [`docs/en/architecture-notebook.md`](docs/en/architecture-notebook.md) |
| Database design | [`docs/pt-BR/database-design.md`](docs/pt-BR/database-design.md) | [`docs/en/database-design.md`](docs/en/database-design.md) |
| UI design (storyboards + wireframes) | [`docs/pt-BR/ui-design.md`](docs/pt-BR/ui-design.md) | [`docs/en/ui-design.md`](docs/en/ui-design.md) |
| Infrastructure description | [`docs/pt-BR/infrastructure.md`](docs/pt-BR/infrastructure.md) | [`docs/en/infrastructure.md`](docs/en/infrastructure.md) |
| Artifact authorship | [`docs/pt-BR/autoria.md`](docs/pt-BR/autoria.md) | [`docs/en/authorship.md`](docs/en/authorship.md) |
| Demo video script/checklist | [`docs/pt-BR/video-script.md`](docs/pt-BR/video-script.md) | [`docs/en/video-script.md`](docs/en/video-script.md) |
| Tech stack | [`docs/pt-BR/tech-stack.md`](docs/pt-BR/tech-stack.md) | [`docs/en/tech-stack.md`](docs/en/tech-stack.md) |

### Generating delivery PDFs

The assignment requires textual artifacts as PDF (Instruction 7). The pt-BR docs are the source of truth; PDFs are a build step, not committed to git:

```bash
sudo apt-get install -y pandoc texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-lang-portuguese
python3 scripts/build_pdfs.py   # writes dist/pdf/*.pdf
```

## Required Deliverables (delivery checklist)

1. [x] Management process description (Kanban board/cards).
2. [x] Vision and scope document.
3. [x] Non-functional requirements specification (system-wide requirements).
4. [x] Functional requirements specification via user stories.
5. [x] Software architecture description (architecture notebook).
6. [x] User interface design (storyboards + wireframes).
7. [x] Physical database design.
8. [ ] System prototype + demo video — prototype code done and tested; scenario checklist ready ([`docs/en/video-script.md`](docs/en/video-script.md)); recording pending.
9. [x] Deployment infrastructure description.

> This README will be updated as artifacts are produced (each one becomes a card on the Kanban board).
