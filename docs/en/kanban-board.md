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
| Kanban process description | This document (`kanban-board.md`) | author | High | S | Done | 2026-08-27 | 2026-08-28 |
| Vision and scope document | `vision-and-scope.md` — problem, stakeholders, scope | author | High | S | Done | 2026-08-27 | 2026-08-28 |
| User story backlog (functional requirements) | Epics + stories + acceptance criteria covering the 19 requirements in the assignment | author | High | L | Done | 2026-08-28 | 2026-08-28 |
| Non-functional requirements specification | Formal NFR document (usability, security, portability, standards, etc.) | author | High | M | Done | 2026-08-27 | 2026-08-28 |
| Architecture notebook | Architecture description (goals, assumptions, dependencies, decisions, mechanisms, abstractions, impact of Flask/SQLAlchemy/Jinja2) | author | High | M | Done | 2026-08-27 | 2026-08-28 |
| Physical database design | Diagram + description of tables/columns/keys/relationships | author | High | M | Done | 2026-08-27 | 2026-08-28 |
| User interface design (storyboards + wireframes) | One storyboard per key usage scenario; simple wireframes per screen | author | Medium | M | In Progress | 2026-08-27 | — |
| Flask project setup | Folder structure, dependencies, initial SQLite database, basic authentication | author | High | M | Backlog | 2026-08-27 | — |
| Implementation — Epic 1: Authentication (US-01 to US-04) | Account, login, access restriction, logout | author | High | M | Backlog | 2026-08-28 | — |
| Implementation — Epic 2: Projects (US-05 to US-08) | Projects CRUD | author | High | M | Backlog | 2026-08-28 | — |
| Implementation — Epic 3: Product Backlog (US-09, US-10) | Product Backlog CRUD (1 per project) | author | High | S | Backlog | 2026-08-28 | — |
| Implementation — Epic 4: Sprint Backlogs (US-11 to US-14) | Sprint Backlogs CRUD (N per project) | author | High | M | Backlog | 2026-08-28 | — |
| Implementation — Epic 5: User Stories (US-15 to US-19) | CRUD + moving between backlogs | author | High | L | Backlog | 2026-08-28 | — |
| Implementation — Epic 6: Epics (US-20 to US-23) | Epics CRUD + linking to stories | author | Medium | M | Backlog | 2026-08-28 | — |
| Implementation — Epic 7: Acceptance Criteria (US-24 to US-27) | CRUD, Given/When/Then format | author | High | M | Backlog | 2026-08-28 | — |
| Implementation — Epic 8: Estimation and Prioritization (US-28 to US-32) | Story points, MoSCoW, RICE + calculation and sorting | author | High | M | Backlog | 2026-08-28 | — |
| Implementation — Epic 9: RBAC, Security, and Auditing (US-33 to US-38) | User/Administrator roles, encryption at rest, technical logging and audit log, admin dashboard | author | High | L | Backlog | 2026-08-28 | — |
| Functional prototype + demo video | Recording covering one success scenario per service | author | High | M | Backlog | 2026-08-27 | — |
| Deployment infrastructure description | Required hardware/software/services | author | Medium | S | Backlog | 2026-08-27 | — |
| Package the delivery (ZIP + unpack test) | Name `ESW-<student ID>.ZIP`, check integrity and no viruses | author | High | S | Backlog | 2026-08-27 | — |

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

## Recommended Next Step

With the physical database design done, the card in progress is the **User interface design (storyboards + wireframes)** — the CRUDs for each already-modeled entity become the screens to sketch.
