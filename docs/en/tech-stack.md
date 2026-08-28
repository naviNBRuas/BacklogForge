# Technical Stack Decision

> Canonical version for grading: [`docs/pt-BR/tech-stack.md`](../pt-BR/tech-stack.md).

## Choice

- **Backend**: Python 3 + **Flask** (micro-framework — little configuration, straight to the point for a solo project).
- **Frontend**: **server-rendered** with **Jinja2** (Flask's own templates) + simple CSS. No SPA (React/Vue) — avoids build tooling, bundlers, and client-side state complexity that bring no benefit at this assignment's scope.
- **Database**: **SQLite** — single file, zero server configuration, sufficient for a demo prototype, and directly serves as the basis for the required "physical database design" artifact.
- **Authentication**: simple Flask session (`flask-login` or manual equivalent) + password hashing (`werkzeug.security`).
- **Version control**: Git (required by the assignment — "platform that allows version control").

## Why This Combination (given the constraint: individual, web, "simplest path")

| Alternative considered | Why not |
|---|---|
| React/Next.js + separate REST API + Postgres | Two layers (frontend/backend) to maintain solo; build tooling; overkill for one person and a demo prototype |
| Node.js + Express + EJS + SQLite | Also valid, but Flask has less boilerplate for simple CRUD, and Jinja2 is more direct than EJS for someone already thinking in Python |
| Django | Full framework (admin, ORM, auth built-in) — could speed things up, but has more "magic"/conventions to learn; Flask keeps the architecture more explicit for the required "architecture notebook" |

**Trade-off accepted**: Flask requires manually assembling pieces that Django gives for free (auth, admin), but that's desirable here — the assignment asks to **describe architectural decisions**, which is more natural when the choices are explicit.

## Assignment Requirements the Stack Directly Addresses

- **(1) TUI or GUI interface** → GUI via browser (Flask/Jinja2 pages).
- **Physical database design** → SQLite schema, with tables for `users`, `projects`, `product_backlogs`, `sprint_backlogs`, `epics`, `user_stories`, `acceptance_criteria`.
- **Prototype + system test video** → locally runnable Flask app with `flask run`, easy to screen-record.
- **Deployment infrastructure** → simple hosting possible (e.g., Render, Railway, PythonAnywhere, or local execution for the demo) — to be detailed in the infrastructure artifact.

## Planned Libraries (to be confirmed during implementation)

- `Flask`
- `Flask-SQLAlchemy` (lightweight ORM over SQLite — makes it easier to describe the physical database design and avoids scattering raw SQL through the code)
- `Flask-Login` (session/authentication)
- `Flask-WTF` (forms + validation + CSRF protection)
- `Werkzeug` (password hashing — already ships with Flask)
