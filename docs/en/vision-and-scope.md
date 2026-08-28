# Vision and Scope

*(Assignment artifact 2: "vision and scope document". Canonical version for grading: [`docs/pt-BR/vision-and-scope.md`](../pt-BR/vision-and-scope.md).)*

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
| Administrator (global system role) | Monitors all users, projects, and audit logs; doesn't take part in any specific project's work |
| Professor/evaluator (ESW course) | Evaluates the system as the course's practical assignment |

## Environment of Future Users

- Access via web browser, desktop (no mobile app requirement).
- Individual or small-team use — each account sees the projects it participates in (in the MVP: each user only sees their own projects, except the Administrator, who has global visibility — see "Role-Based Access Control" below and "Out of Scope").

## Needs Addressed

- Structure a project's requirements using user-story vocabulary without relying on ad hoc spreadsheets.
- Move stories between backlogs (product ↔ sprints) as planning progresses.
- Prioritize using two complementary methods: **MoSCoW** (qualitative) and **RICE** (quantitative).
- Keep account and project data protected (strong password hashing, sensitive data encrypted at rest, secure sessions) and keep relevant system actions auditable (a log of who did what, and when).
- Give an Administrator role visibility over the whole system (users, projects, logs), without mixing that responsibility with PO/Developer work inside a project.

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
12. Role-based access control (RBAC): an **Administrator** role with a monitoring dashboard (users, projects, audit logs).
13. Audit log of the system's relevant actions (who did what, when).

## Role-Based Access Control (RBAC)

Unlike the initial draft, the MVP now has real role-based access control (not just a label):

- **User** (default role for any account): full read/write access to their own projects and everything inside them (PO and Developer are, in practice, the same user performing different functions within a solo project — the system doesn't require a second account per role).
- **Administrator**: a global role, assigned to a specific account (not per-project). Doesn't access other users' project content to edit it, but has a monitoring dashboard with: a list of all users and projects in the system, and the full audit log. This role exists for system administration/observability, not to take part in the agile work itself.
- The first administrator account is set via seed/configuration (e.g., an environment variable) on first run — there's no public "become admin" endpoint.

## Non-Functional Requirements (summary — detailed in `docs/en/non-functional-requirements.md`)

- **Usability**: CRUDs must follow a consistent navigation pattern across entities.
- **Portability**: runs in any environment with Python 3 installed (embedded SQLite).
- **Security**: passwords never stored in plain text (strong hashing, e.g. `bcrypt`/`argon2`); sensitive data encrypted at rest; CSRF protection on forms; secure session cookies (`HttpOnly`, `Secure`, `SameSite`); security HTTP headers; role-based access control (RBAC) enforced on every sensitive route, not just the login screen.
- **Auditability**: structured logging of security events and data changes (create/edit/delete on any entity, login/logout, authentication failures), with timestamp and responsible user, queryable by the Administrator.

## Out of Scope (MVP)

- Real-time multi-user collaboration on the same project (e.g., multiple POs editing simultaneously with live updates).
- PO/Developer roles as distinct permissions *within* the same project (they remain narrative labels on user stories — the actual technical permission is: project owner vs. Administrator).
- Notifications/email.
- Integration with external tools (Jira, GitHub Issues).
- Native mobile app.

## Elements of the Proposed Solution

Monolithic web application (Flask + SQLite), session-based authentication with role-based access control (User/Administrator), strong password hashing and sensitive data encrypted at rest, persistent audit log, server-rendered CRUD for each domain entity, and a view for calculating/displaying the RICE score per story. See `docs/en/tech-stack.md` for the specific security/logging libraries.
