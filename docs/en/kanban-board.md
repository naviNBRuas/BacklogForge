# Kanban Board — Managing the BacklogForge Project

*(Artifact 1 of the assignment: "description of the management process, including information about the board and cards used". Canonical version for grading: [`docs/pt-BR/kanban-board.md`](../pt-BR/kanban-board.md).)*

## Why Kanban Here

Solo project, with a known and finite set of artifacts to deliver (see `README.md`) plus building the prototype. Kanban was chosen (it's required by the assignment) because it: visualizes all pending/in-progress work on a single board, limits work in progress (important for a single person — avoids opening too many fronts at once), and lets "documentation artifact" and "code task" live in the same flow.

## Board Columns and Purpose of Each

| # | Column | Purpose |
|---|---|---|
| 1 | **Backlog** | All identified work not yet prioritized to start. Entry point for new ideas/tasks as they come up. |
| 2 | **To Do** | Work already prioritized and ready to be pulled — prerequisites resolved, scope clear enough to start. |
| 3 | **In Progress** | Work being executed right now. **WIP limit = 1** (solo project — avoids context switching). |
| 4 | **Review** | Work technically done, awaiting self-review against the assignment's criteria before being considered complete (e.g., re-reading the artifact against the PDF's evaluation checklist). |
| 5 | **Done** | Work reviewed and finalized — ready to be part of the final delivery (ZIP). |

> Flow: `Backlog → To Do → In Progress → Review → Done`. Cards only move backward (e.g., Review → To Do) if self-review finds a problem.

## Card Format

Each card records: **Name**, **Description**, **Owner** (always the author, solo project), **Priority** (High/Medium/Low), **Estimate** (S/M/L — small/medium/large, given the academic scope), **Dates** (created / completed).

> **This board is live**: its state (the "Status" column) reflects real progress as of the last update, and the "Movement History" section below logs every column transition with a date — this isn't just a static description of the process, it's the tool actually used to manage this project.

## Cards

| Name | Description | Owner | Priority | Estimate | Status | Created | Completed |
|---|---|---|---|---|---|---|---|
| Kanban process description | This document (`kanban-board.md`) | Navinchandry Bittencourt Ruas | High | S | Done | 2026-08-27 | 2026-08-28 |
| Vision and scope document | `vision-and-scope.md` — problem, stakeholders, scope | Navinchandry Bittencourt Ruas | High | S | Done | 2026-08-27 | 2026-08-28 |
| User story backlog (functional requirements) | Epics + stories + acceptance criteria covering the 19 requirements in the assignment | Navinchandry Bittencourt Ruas | High | L | Done | 2026-08-28 | 2026-08-28 |
| Non-functional requirements specification | Formal NFR document (usability, security, portability, standards, etc.) | Navinchandry Bittencourt Ruas | High | M | Done | 2026-08-27 | 2026-08-28 |
| Architecture notebook | Architecture description (goals, assumptions, dependencies, decisions, mechanisms, abstractions, impact of Flask/SQLAlchemy/Jinja2) | Navinchandry Bittencourt Ruas | High | M | Done | 2026-08-27 | 2026-08-28 |
| Physical database design | Diagram + description of tables/columns/keys/relationships | Navinchandry Bittencourt Ruas | High | M | Done | 2026-08-27 | 2026-08-28 |
| User interface design (storyboards + wireframes) | One storyboard per key usage scenario; simple wireframes per screen | Navinchandry Bittencourt Ruas | Medium | M | Done | 2026-08-27 | 2026-08-28 |
| Flask project setup | Folder structure, dependencies, initial SQLite database, basic authentication | Navinchandry Bittencourt Ruas | High | M | Done | 2026-08-27 | 2026-08-28 |
| Implementation — Epic 1: Authentication (US-01 to US-04) | Account, login, access restriction, logout | Navinchandry Bittencourt Ruas | High | M | Done | 2026-08-28 | 2026-08-28 |
| Implementation — Epic 2: Projects (US-05 to US-08) | Projects CRUD | Navinchandry Bittencourt Ruas | High | M | Done | 2026-08-28 | 2026-08-28 |
| Implementation — Epic 3: Product Backlog (US-09, US-10) | Product Backlog CRUD (1 per project) | Navinchandry Bittencourt Ruas | High | S | Done | 2026-08-28 | 2026-08-28 |
| Implementation — Epic 4: Sprint Backlogs (US-11 to US-14) | Sprint Backlogs CRUD (N per project) | Navinchandry Bittencourt Ruas | High | M | Done | 2026-08-28 | 2026-08-28 |
| Implementation — Epic 5: User Stories (US-15 to US-19) | CRUD + moving between backlogs | Navinchandry Bittencourt Ruas | High | L | Done | 2026-08-28 | 2026-08-28 |
| Implementation — Epic 6: Epics (US-20 to US-23) | Epics CRUD + linking to stories | Navinchandry Bittencourt Ruas | Medium | M | Done | 2026-08-28 | 2026-08-28 |
| Implementation — Epic 7: Acceptance Criteria (US-24 to US-27) | CRUD, Given/When/Then format | Navinchandry Bittencourt Ruas | High | M | Done | 2026-08-28 | 2026-08-28 |
| Implementation — Epic 8: Estimation and Prioritization (US-28 to US-32) | Story points, MoSCoW, RICE + calculation and sorting | Navinchandry Bittencourt Ruas | High | M | Done | 2026-08-28 | 2026-08-28 |
| Implementation — Epic 9: RBAC, Security, and Auditing (US-33 to US-38) | User/Administrator roles, encryption at rest, technical logging and audit log, admin dashboard | Navinchandry Bittencourt Ruas | High | L | Done | 2026-08-28 | 2026-08-28 |
| Functional prototype + demo video | Recording covering one success scenario per service | Navinchandry Bittencourt Ruas | High | M | In Progress | 2026-08-27 | — |
| Deployment infrastructure description | Required hardware/software/services | Navinchandry Bittencourt Ruas | Medium | S | Done | 2026-08-27 | 2026-08-28 |
| Authorship document | `authorship.md` — which artifacts each member built (Instruction 6, required even for solo work) | Navinchandry Bittencourt Ruas | High | S | Done | 2026-08-28 | 2026-08-28 |
| LICENSE | MIT license file promised in `non-functional-requirements.md` §9 but never created | Navinchandry Bittencourt Ruas | Low | S | Done | 2026-08-28 | 2026-08-28 |
| Demo video script | `video-script.md` — scenario checklist ensuring 1 success case per service (Instruction 24) | Navinchandry Bittencourt Ruas | High | S | Done | 2026-08-28 | 2026-08-28 |
| PDF export pipeline | `scripts/build_pdfs.py` (pandoc + xelatex) — Instruction 7 requires PDF delivery | Navinchandry Bittencourt Ruas | High | M | Done | 2026-08-28 | 2026-08-28 |
| Package the delivery (ZIP + unpack test) | Name `ESW-241034353.ZIP`, check integrity and no viruses | Navinchandry Bittencourt Ruas | High | S | Backlog | 2026-08-27 | — |

> Current WIP (In Progress column): **1/1** — within the limit. New cards are added to the Backlog as subtasks emerge (e.g., the 8 implementation cards above were born from breaking the user story backlog into epics, when that card was completed).

## Movement History

| Date | Card | From → To | Note |
|---|---|---|---|
| 2026-08-27 | Kanban process description | Backlog → In Progress | Initial board draft. |
| 2026-08-27 | Vision and scope document | Backlog → To Do | Draft started in parallel. |
| 2026-08-28 | Kanban process description | In Progress → Review → Done | Column/card structure validated against the grading criteria (assignment item 01). |
| 2026-08-28 | Vision and scope document | To Do → In Progress → Review → Done | Draft framing removed; content already covered the grading criterion's points (item 02). |
| 2026-08-28 | User story backlog | Backlog → In Progress → Review → Done | 32 stories across 8 epics written covering the 19 requirements; traceability table checked row by row. |
| 2026-08-28 | Non-functional requirements specification | Backlog → To Do → In Progress | Pulled next, since it's the only remaining "requirements" artifact and is a conceptual prerequisite of the architecture. |
| 2026-08-28 | Implementation — Epics 1 to 8 | (created directly in Backlog) | Implementation cards derived from breaking the user story backlog into epics. |
| 2026-08-28 | Scope: RBAC/security/logging | Out of Scope → In Scope | Author's decision to make roles (User/Administrator) a real access control mechanism, with encryption at rest and logging/auditing — updated in `vision-and-scope.md`, `tech-stack.md`; produced the "Implementation — Epic 9" card and 6 new stories (US-33 to US-38) in the user story backlog. |
| 2026-08-28 | Non-functional requirements specification | In Progress → Review → Done | Document covers quality attributes, security (RBAC, encryption, session), interfaces, compliance (OWASP), constraints, licensing, and documentation — checked against grading criterion 03. |
| 2026-08-28 | Architecture notebook | To Do → In Progress | Pulled next: the security/RBAC decisions from the NFR doc (previous item) are a direct prerequisite for the architecture mechanisms to be described here. |
| 2026-08-28 | Architecture notebook | In Progress → Review → Done | Document covers goals, assumptions, dependencies, decisions/constraints, mechanisms, abstractions, perspectives, and tool impact — checked against grading criterion 05. |
| 2026-08-28 | Physical database design | Backlog → To Do → In Progress | Pulled next: the entities and relationships already defined in the notebook's section 7 are the direct basis for the physical schema. |
| 2026-08-28 | Physical database design | In Progress → Review → Done | ER diagram (mermaid) + 7 tables described (name, columns, keys, relationships, purpose) — checked against grading criterion 07. |
| 2026-08-28 | User interface design (storyboards + wireframes) | Backlog → In Progress | Pulled next. |
| 2026-08-28 | User interface design (storyboards + wireframes) | In Progress → Review → Done | 4 storyboards (signup/login, story+criteria, sprint planning, admin dashboard) with ASCII wireframes — checked against grading criterion 06. |
| 2026-08-28 | Deployment infrastructure description | Backlog → In Progress | Pulled next — the last remaining "requirements/design" artifact before the prototype. |
| 2026-08-28 | Deployment infrastructure description | In Progress → Review → Done | Hardware, software, services, environment variables, and deployment steps described — checked against grading criterion 09. All 7 documentation artifacts (criteria 01–07 and 09) are done; only the prototype (criterion 08) remains. |
| 2026-08-28 | Flask project setup | Backlog → In Progress | Pulled next: the first implementation card, a prerequisite for all of Epics 1–9. |
| 2026-08-28 | Flask project setup | In Progress → Review → Done | App factory, extensions (SQLAlchemy/Login/WTF/Talisman), config, full schema (`app/models.py`), RBAC decorators, and audit service created and tested (`tests/`). |
| 2026-08-28 | Implementation — Epics 1 to 9 | Backlog → In Progress → Review → Done | All 38 stories implemented as Flask routes + Jinja2 templates; a 12-test automated suite (`pytest`) covers signup/login, isolation between users, full CRUD, RICE calculation, moving/deleting a sprint, admin RBAC, and encryption — all passing. Real server tested with `flask run` and `curl`. |
| 2026-08-28 | Functional prototype + demo video | Backlog → In Progress | Prototype code is ready and tested; only the demo video recording remains (a manual step for the author, outside automation's scope). |
| 2026-08-28 | Full audit against the assignment | — | A full re-read of `docs/spec/ESW-TRABALHO-PRATICO.md` (requirements, instructions, and grading criteria) found 5 gaps: (1) authorship document missing (Instruction 6); (2) textual artifacts only in Markdown, no PDF (Instruction 7); (3) `LICENSE` promised but never created; (4) no script ensuring "1 success scenario per service" coverage in the video (Instruction 24); (5) US-32 (sort backlog) marked Done under Epic 8 without actually being implemented. |
| 2026-08-28 | Authorship document, LICENSE, video script, PDF pipeline | Backlog → In Progress → Review → Done | The 4 documentation/process gaps from the audit were resolved in the same session. |
| 2026-08-28 | Implementation — Epic 8 (US-32) | Review (reopened) → Done | Code gap from the audit fixed: `?sort=rice\|moscow` implemented on the Product Backlog and Sprint Backlog, with 4 new tests. |

## Recommended Next Step

All documentation/design artifacts and the full prototype code (Epics 1–9, 38 stories) are done and tested. Only the **demo video** and, finally, **packaging the delivery** (a ZIP named `ESW-241034353.ZIP`) remain.
