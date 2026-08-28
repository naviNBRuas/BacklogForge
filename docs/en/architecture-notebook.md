# Architecture Notebook

*(Assignment artifact 5: "software architecture description". Canonical version for grading: [`docs/pt-BR/architecture-notebook.md`](../pt-BR/architecture-notebook.md).)*

## 1. Architecture Goals

- Keep the architecture **simple and explicit**: every decision must be justifiable and describable in this document, avoiding framework "magic" that would make it hard to explain (see `tech-stack.md`, Flask vs. Django rationale).
- Ensure **RBAC and auditing are cross-cutting**, applied consistently across every data route, not implemented ad hoc per screen.
- Support the assignment's domain vocabulary (Project → Product Backlog / Sprint Backlog → User Story → Acceptance Criterion, with Epic as a cross-cutting grouping) as a **first-class data model**, not generic fields of a task-tracker system.
- Be runnable and demoable locally by a single person, with no infrastructure beyond Python + SQLite.

## 2. Assumptions

- Data volume compatible with individual/academic use (dozens of projects, hundreds of stories) — no assumption of production-scale multi-tenancy.
- The evaluator (professor) will run the prototype locally or watch the demo video — no high-availability assumption.
- Only one Flask process running at a time during the demo (no need for distributed locking over SQLite).

## 3. Dependencies

- **Web framework**: Flask (routing, Jinja2 templates, request context).
- **ORM/Database**: Flask-SQLAlchemy over SQLite — the data model (section 6) depends directly on SQLAlchemy's object-relational mapping.
- **Authentication/Session**: Flask-Login — Section 5 (RBAC) depends on `current_user` and the session lifecycle this library manages.
- **Form security**: Flask-WTF (CSRF, validation) — every write view depends on a corresponding `FlaskForm`.
- **Secure headers/cookies**: Flask-Talisman — applied once, at application startup (`create_app`), affecting every response.
- **Password hashing**: argon2-cffi.
- **Encryption at rest**: cryptography (Fernet).
- See `tech-stack.md` for the full list and the rationale behind each choice.

## 4. Requirements Influencing the Architecture

- The **security NFRs** (`non-functional-requirements.md`, section 3) force a centralized authorization layer (not scattered across templates) and a cross-cutting audit mechanism.
- **Assignment requirement (5)** ("only one Product Backlog can exist per project") is modeled as a uniqueness constraint in the database (a unique `project_id` foreign key on the `product_backlogs` table), not merely validated in the application.
- **Requirement (8)** ("move stories between backlogs") implies a User Story belongs to **one** backlog at a time, but the backlog type (Product or Sprint) can vary — modeled with a simple polymorphic association (see section 6).

## 5. Architectural Decisions, Constraints, and Justifications

| Decision | Justification | Accepted constraint |
|---|---|---|
| Layered monolithic architecture (routes → services → models), no microservices | Academic scope and timeline; a single developer | Doesn't scale horizontally — acceptable, out of scope (see NFR §8) |
| RBAC implemented as a decorator (`@require_role("admin")`) applied on routes, not scattered manual checks | Centralizes the authorization rule in a single, independently testable spot | Every new route must remember to apply the decorator — mitigated with a review checklist on the Kanban board itself (the "Review" column) |
| Audit log as its own table (`audit_logs`), written by a central service (`audit.log(user, action, entity)`) called explicitly from write operations | Avoids relying on database triggers (less portable) and keeps the "what to audit" decision in Python code, easy to describe here | The audit call can be forgotten in a new write operation — mitigated by concentrating all write operations in service methods (section 6), not directly in routes |
| Encryption at rest via a SQLAlchemy `TypeDecorator` (custom `EncryptedString` field) | Makes encryption transparent to the rest of the code — readers/writers of the field don't need to know it's encrypted | Equality search/indexing on the encrypted field is inefficient — acceptable since sensitive fields aren't used in filters/searches |
| A single Product Backlog per project, created automatically on project creation (not exposed as a manual creation) | Reflects assignment requirement (5) directly in the flow, with no unnecessary extra screen | None — no relevant trade-off |

## 6. Architecture Mechanisms

- **Routes (views) layer**: receives the HTTP request, validates input via `Flask-WTF`, delegates to the service layer, renders the Jinja2 template or redirects.
- **Service layer**: pure/orchestrating functions (e.g., `project_service.create_project(user, data)`) that apply business rules (cascading Product Backlog creation, closed-value validation for story points/MoSCoW/RICE, RICE score calculation) and call the audit service.
- **Model (SQLAlchemy) layer**: domain entities (section 7) and the `EncryptedString` `TypeDecorator` for sensitive fields.
- **Authorization mechanism**: `@login_required` decorator (Flask-Login) + a custom `@require_role(role)` decorator that checks `current_user.role`; a `@require_project_owner` decorator that checks whether `current_user` owns the accessed project (prevents a user from accessing another user's resource via URL manipulation).
- **Audit mechanism**: `audit_service.log(actor, action, entity_type, entity_id)` called at the end of every successful write operation in business services; queried only by the `/admin/audit-logs` route, protected by `@require_role("admin")`.
- **RICE calculation mechanism**: a pure function `calculate_rice(reach, impact, confidence, effort)` returning `(reach * impact * confidence) / effort`, used both for display and for sorting the backlog (requirement 19).

## 7. Architecture Abstractions

Domain entities (elements) and their relationships (mapped 1:1 to the physical database design tables, see `database-design.md`):

- `User` (1) — (N) `Project` (owner)
- `Project` (1) — (1) `ProductBacklog`
- `Project` (1) — (N) `SprintBacklog`
- `Project` (1) — (N) `Epic`
- `UserStory` belongs to exactly one backlog (`ProductBacklog` **or** `SprintBacklog`, never both) and optionally to an `Epic`
- `UserStory` (1) — (N) `AcceptanceCriterion`
- `AuditLog` references a `User` (actor) and, generically (type + id), the affected entity

The central abstraction is the **User Story as an aggregate**: story points, MoSCoW, and RICE criteria are its own attributes (not separate entities), while Acceptance Criteria are a child entity with a dependent lifecycle (cascade-deleted with the story).

## 8. Architecture by Perspective

- **Logical perspective** (modules): `auth/`, `projects/`, `backlogs/`, `stories/`, `epics/`, `admin/` — each with `routes.py`, `services.py`, `forms.py`; `models.py` and `extensions.py` (SQLAlchemy/Login/Talisman instances) shared at the package root.
- **Process perspective**: a single synchronous HTTP request handled at a time by Flask's development server (`flask run`); no async/background job processing in the MVP.
- **Data perspective**: see `database-design.md` — a single SQLite file, no replication.
- **Deployment perspective**: see `infrastructure.md` — a single Flask process, served locally or by a simple service (Render/PythonAnywhere) behind HTTPS.
- **Security perspective**: see `non-functional-requirements.md` §3 — authentication, RBAC, CSRF, secure cookies, HTTP headers, encryption at rest, and auditing cut across all other perspectives.

## 9. Impact of the Tools Used on the Architecture

- **Flask** (vs. Django): having no built-in ORM/auth/admin forces the explicit layered architecture described in section 6 — a deliberate decision to make the architecture easier to describe and defend in this document (see `tech-stack.md`).
- **Flask-SQLAlchemy**: sets the data access pattern (Active Record-like via `db.Model`), shaping the service layer to manipulate ORM objects instead of raw SQL.
- **Flask-Login**: imposes the `UserMixin` + `LoginManager.user_loader` pattern, which shapes how the user's `role` is loaded on every request (via `current_user.role`).
- **Flask-WTF**: requires every write route to have a corresponding `Form` class, which naturally forces centralized per-form validation instead of scattered manual checks in views.
- **Flask-Talisman**: applied once in the application factory (`create_app`), globally affects headers/cookies of every response with no changes required in individual views.
- **Jinja2** (server-rendered, no SPA): removes the need for a separate JSON API and frontend build tooling, keeping the architecture to a single presentation layer.
