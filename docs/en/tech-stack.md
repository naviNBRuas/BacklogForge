# Technical Stack Decision

> Canonical version for grading: [`docs/pt-BR/tech-stack.md`](../pt-BR/tech-stack.md).

## Choice

- **Backend**: Python 3 + **Flask** (micro-framework — little configuration, straight to the point for a solo project).
- **Frontend**: **server-rendered** with **Jinja2** (Flask's own templates) + simple CSS. No SPA (React/Vue) — avoids build tooling, bundlers, and client-side state complexity that bring no benefit at this assignment's scope.
- **Database**: **SQLite** — single file, zero server configuration, sufficient for a demo prototype, and directly serves as the basis for the required "physical database design" artifact.
- **Authentication and authorization**: Flask session via `Flask-Login`, with role-based access control (RBAC — User/Administrator) and strong password hashing (`argon2` via `argon2-cffi`, with `werkzeug.security` as a fallback).
- **Encryption at rest**: `cryptography` (Fernet, authenticated AES-128) for sensitive database fields; encryption key from an environment variable (`python-dotenv` in development), never committed.
- **Web application security**: `Flask-WTF` (CSRF on all forms), `Flask-Talisman` (HTTP security headers, `Secure`/`HttpOnly`/`SameSite` cookies, HTTPS enforced in production).
- **Logging and auditing**: standard library `logging` module with `RotatingFileHandler` for application logs; a dedicated `audit_logs` table (via SQLAlchemy) for the business audit log (who did what, when), queryable by the Administrator.
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
- `Flask-Login` (session/authentication + loading the user and their role on every request)
- `Flask-WTF` (forms + validation + CSRF protection)
- `Flask-Talisman` (HTTP security headers and secure cookies)
- `Werkzeug` (security utilities — already ships with Flask)
- `argon2-cffi` (Argon2 password hashing, OWASP's current recommendation)
- `cryptography` (symmetric encryption of sensitive fields at rest)
- `python-dotenv` (load secrets — `SECRET_KEY`, encryption key — from environment variables in development)

## Security, RBAC, and Logging (detailed in `docs/en/non-functional-requirements.md`)

- **RBAC**: two roles in the MVP — `user` (default, owns their own projects) and `admin` (global role, monitoring view). Enforced via a decorator (`@login_required` + role check) on every sensitive route, not left to the UI alone.
- **Encryption at rest**: fields considered sensitive (to be decided case by case — there's no ultra-sensitive data in the domain beyond credentials, but the pattern is ready to use, e.g. a project's private notes) encrypted with Fernet before being written to SQLite.
- **Logging**: two kinds — (1) technical application logging (errors, requests) via `logging`/`RotatingFileHandler`, for debugging; (2) business audit log (login, logout, authentication failure, create/edit/delete on any entity), persisted in its own table and exposed on a dashboard visible only to the Administrator.
