# Non-Functional Requirements Specification (System-Wide Requirements)

*(Assignment artifact 3: "non-functional requirements specification via a dedicated artifact". Canonical version for grading: [`docs/pt-BR/non-functional-requirements.md`](../pt-BR/non-functional-requirements.md). Covers additional functional requirements not captured in user stories, quality attributes, interfaces, compliance, constraints, licensing, and documentation.)*

## 1. Functional Requirements Not Covered by User Stories

Most functional requirements live in [`user-stories.md`](user-stories.md). The items below are functional but cross-cutting (they don't belong to a single story):

- **Automatic creation of dependent data**: creating a project automatically creates its Product Backlog (see US-05); deleting a project cascades to delete all dependent data (see US-08); deleting a Sprint Backlog returns its stories to the Product Backlog instead of deleting them (see US-14).
- **Closed-domain value validation**: story points, MoSCoW, and RICE only accept the values defined in the assignment (section 2, items 15–18) — validated both in the UI and on the server (never trust the HTML `<select>` alone).
- **Administrator account seeding**: on the application's first run, an account with the `admin` role is created/promoted from environment variables (`ADMIN_EMAIL`, `ADMIN_PASSWORD`), with no equivalent public endpoint.

## 2. Quality Attributes

| Attribute | Requirement |
|---|---|
| **Usability** | All CRUD screens follow the same navigation pattern (list → view details → edit/delete with confirmation); validation error messages appear next to the offending field; breadcrumb navigation (Project → Backlog → Story). |
| **Performance** | Each listing page (projects, backlogs, stories) must load in under 1s with up to 100 stories per backlog in a local development environment — a scale compatible with SQLite and individual/academic use, with no need for large-scale production optimizations. |
| **Reliability** | No deletion (project, backlog, story, epic, criterion) happens without explicit user confirmation; every cascading delete is intentional and documented (see section 1). |
| **Maintainability** | Code organized by layer (routes/views, models, forms) following Flask's standard convention; no business logic embedded in Jinja2 templates. |
| **Portability** | Runs in any environment with Python 3.10+ installed; the database is a single SQLite file, with no external database service dependency. |
| **Auditability** | Every business data mutation (create/edit/delete on any entity) and every authentication event (login, logout, failed login) generates an audit record (see Epic 9, `user-stories.md`). |
| **Testability** | Validation rules (story points/MoSCoW/RICE values, the RICE formula, RBAC) isolated in pure functions/service modules, testable without spinning up a full HTTP server. |

## 3. Security Requirements

- **Authentication**: session managed by `Flask-Login`; no data route accessible without a valid session (US-03).
- **Passwords**: hashed with Argon2 (`argon2-cffi`); never stored or logged in plain text; never included in error responses (US-37).
- **Authorization (RBAC)**: `user` and `admin` roles; role checks performed on the server (decorator/middleware), never by hiding UI elements alone (US-33, US-34).
- **CSRF**: every POST/PUT/DELETE form protected by a CSRF token (`Flask-WTF`) (US-37).
- **Session cookies**: `HttpOnly`, `Secure` (required in production over HTTPS), `SameSite=Lax` or stricter (US-37).
- **HTTP security headers**: `Content-Security-Policy`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY` (or the equivalent `frame-ancestors`), via `Flask-Talisman`.
- **Encryption at rest**: fields marked sensitive encrypted with Fernet (authenticated AES-128) before being written to SQLite; the encryption key kept out of version control, injected via environment variable (US-38).
- **Isolation between users**: a user never accesses another user's project data, except the Administrator in monitoring-only mode (US-03, US-34).
- **Authentication attempt logging**: every failed login is audited with the attempted email and timestamp, never with the attempted password (US-35).

## 4. User Interface Requirements

- Graphic user interface (GUI) via browser — satisfies assignment requirement (1).
- Layout responsive enough for desktop use (no mobile support requirement — see `vision-and-scope.md`, Out of Scope).
- Forms display validation errors clearly, next to the field, without reloading to a blank page.
- Destructive actions (deleting a project/backlog/story/epic/criterion) always require explicit confirmation before executing.
- Administrator dashboard visually distinct from regular project screens, to make it clear the user is outside the context of a specific project.

## 5. Interface Requirements with External Devices

Not applicable — the system doesn't integrate with external devices (sensors, specific hardware, printers, etc.). The only "device" is the user's browser, already covered in section 4.

## 6. Interface Requirements with Other Software Systems

Not applicable in the MVP — the system is self-contained, with no external API integration (see `vision-and-scope.md`, Out of Scope: "Integration with external tools"). There are no webhooks, import/export to other systems, or external SSO in this version.

## 7. Compliance (Standards, Norms, Metrics)

- **OWASP Top 10** (2021) used as a reference checklist for the security decisions in section 3 (injection, broken authentication, sensitive data exposure, broken access control, security misconfiguration).
- **OWASP ASVS** (level 1) used as an informal reference for the implemented authentication/session controls.
- **PEP 8** as the Python code style standard.
- **Semantic Versioning** doesn't apply to this academic assignment (no multiple public package releases), but the Git commit history follows descriptive messages per logical change.
- No specific legal standard (e.g., GDPR/LGPD) is treated in depth, since this is an academic prototype with no real third-party data — but the data-minimization and password-protection principles in section 3 already follow the spirit of personal data protection.

## 8. Design Constraints

- Must be runnable locally with `flask run`, with no mandatory cloud infrastructure for the demo (see `infrastructure.md`).
- Single database (SQLite) — a deliberate decision that limits heavy concurrent writes, acceptable given individual/academic use (see `tech-stack.md`).
- No frontend SPA/build step — all pages are server-rendered with Jinja2, to keep the architecture simple to describe in the architecture notebook.
- The academic assignment's deadline limits scope to what's described in `vision-and-scope.md` (see Out of Scope).

## 9. Licensing Aspects

- Repository and code published under the **MIT** license (a `LICENSE` file to be added to the repository) — permissive, suitable for an academic project used as a public GitHub portfolio piece.
- All libraries listed in `tech-stack.md` (Flask, SQLAlchemy, Flask-Login, Flask-WTF, Flask-Talisman, argon2-cffi, cryptography, python-dotenv) are open source under permissive licenses (BSD/MIT/Apache-2.0), compatible with using and redistributing the project.

## 10. Documentation Requirements

- Planning documentation delivered in pt-BR (`docs/pt-BR/`) for the course, mirrored in English (`docs/en/`) for the public GitHub repository — see `README.md`.
- Every artifact required by the assignment (section 3 of `docs/spec/ESW-TRABALHO-PRATICO.md`) corresponds to a versioned, traceable file in Git, with change history.
- The repository README keeps an up-to-date delivery checklist as artifacts are completed.
- Code comments reserved for non-obvious decisions (why, not what) — no lengthy docstrings or comments redundant with the code itself.
