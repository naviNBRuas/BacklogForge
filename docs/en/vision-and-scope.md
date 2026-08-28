# Vision and Scope — Draft

> Canonical version for grading: [`docs/pt-BR/vision-and-scope.md`](../pt-BR/vision-and-scope.md). Initial draft to guide the backlog. Should be reviewed/expanded to become the formal "vision and scope document" required for delivery.

## Problem

Teams that use user stories to manage requirements (agile teams, Scrum/Kanban) need a single place to record and prioritize: projects, backlogs (product and sprint), epics, and user stories — with acceptance criteria, estimation (story points), priority (MoSCoW), and value/effort-based prioritization (RICE). Today this is done in spreadsheets or generic tools (Trello, Notion) that don't natively model this specific vocabulary (epic → story → acceptance criterion, with scoring and MoSCoW/RICE already built in).

## Position in the Market

A **lean, specialized** tool, in the space between a spreadsheet (no structure) and a full Jira (heavy, expensive, complex). Equivalent in spirit to simple backlog tools for small teams/academic case studies.

## Stakeholders

| Stakeholder | Responsibility |
|---|---|
| User (authenticated) | Creates/manages their own projects, backlogs, and stories |
| Product Owner (role within a project) | Prioritizes the Product Backlog, defines MoSCoW/RICE |
| Developer (role within a project) | Views/updates stories assigned to sprints |
| Professor/evaluator (ESW course) | Evaluates the system as the course's practical assignment |

## Environment of Future Users

- Access via web browser, desktop (no mobile app requirement).
- Individual or small-team use — each account sees the projects it participates in (in the MVP: each user only sees their own projects, no collaborative multi-user support — see "Out of Scope").

## Needs Addressed

- Structure a project's requirements using user-story vocabulary without relying on ad hoc spreadsheets.
- Move stories between backlogs (product ↔ sprints) as planning progresses.
- Prioritize using two complementary methods: **MoSCoW** (qualitative) and **RICE** (quantitative).

## Features (summary — detailed as user stories)

1. User account + authentication.
2. Projects CRUD.
3. Product Backlog CRUD (1 per project).
4. Sprint Backlogs CRUD (N per project).
5. User Stories CRUD (`As a/I want/So that` format), associated with the Product Backlog on creation.
6. Move stories between backlogs.
7. Epics CRUD + story↔epic linking.
8. Acceptance Criteria CRUD per story (`Given/When/Then` format).
9. Assign story points (series 0, 1, 2, 3, 5, 8, 13, 21, 34, 55).
10. Assign MoSCoW label (M/S/C/W).
11. Assign RICE criteria (Reach, Impact, Confidence, Effort) and calculate the score `(R×I×C)/E`.

## Non-Functional Requirements (summary — detailed in the NFR artifact)

- Usability: CRUDs must follow a consistent navigation pattern across entities.
- Portability: runs in any environment with Python 3 installed (embedded SQLite).
- Basic security: passwords never stored in plain text; session required for all data routes.

## Out of Scope (MVP)

- Real-time multi-user collaboration on the same project (e.g., multiple POs editing simultaneously).
- Notifications/email.
- Integration with external tools (Jira, GitHub Issues).
- Native mobile app.

## Elements of the Proposed Solution

Monolithic web application (Flask + SQLite), session-based authentication, server-rendered CRUD for each domain entity, and a view for calculating/displaying the RICE score per story.
