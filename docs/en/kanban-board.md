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

## Initial Cards

| Name | Description | Owner | Priority | Estimate | Status |
|---|---|---|---|---|---|
| Kanban process description | This document (`kanban-board.md`) | author | High | S | In Progress |
| Vision and scope document | `vision-and-scope.md` — problem, stakeholders, scope | author | High | S | To Do (draft already started) |
| Non-functional requirements specification | Formal NFR document (usability, security, portability, etc.) | author | High | M | Backlog |
| User story backlog (functional requirements) | Epics + stories + acceptance criteria covering the 19 requirements in the assignment | author | High | L | Backlog |
| Architecture notebook | Architecture description (elements, relationships, impact of Flask/SQLAlchemy/Jinja2) | author | High | M | Backlog |
| User interface design (storyboards + wireframes) | One storyboard per key usage scenario; simple wireframes per screen | author | Medium | M | Backlog |
| Physical database design | Diagram + description of tables/columns/keys/relationships | author | High | M | Backlog |
| Flask project setup | Folder structure, dependencies, initial SQLite database, basic authentication | author | High | M | Backlog |
| Projects CRUD | Implementation of the Project entity | author | High | M | Backlog |
| Product Backlog CRUD | Implementation (1 per project) | author | High | M | Backlog |
| Sprint Backlogs CRUD | Implementation (N per project) | author | High | M | Backlog |
| User Stories CRUD + moving between backlogs | Includes As/I want/So that format | author | High | L | Backlog |
| Epics CRUD + linking to stories | | author | Medium | M | Backlog |
| Acceptance Criteria CRUD | Given/When/Then format | author | High | M | Backlog |
| Story points, MoSCoW and RICE | Fields + automatic RICE score calculation | author | High | M | Backlog |
| Functional prototype + demo video | Recording covering one success scenario per service | author | High | M | Backlog |
| Deployment infrastructure description | Required hardware/software/services | author | Medium | S | Backlog |
| Package the delivery (ZIP + unpack test) | Name `ESW-<student ID>.ZIP`, check integrity and no viruses | author | High | S | Backlog |

> This board evolves throughout the work — new cards are added to the Backlog as subtasks emerge (e.g., each user story of the system itself can become an implementation card when its turn comes).

## Recommended Next Step

With the board created, the next card to pull into "In Progress" is the **Vision and scope document** (already drafted in `vision-and-scope.md`) and, in parallel or shortly after, the **user story backlog** — the largest artifact and the foundation for everything else (architecture, UI, and database all derive from it).
