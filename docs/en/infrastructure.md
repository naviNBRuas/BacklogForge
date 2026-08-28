# Deployment Infrastructure Description

*(Assignment artifact 9: "deployment infrastructure description, covering hardware, software, and services". Canonical version for grading: [`docs/pt-BR/infrastructure.md`](../pt-BR/infrastructure.md).)*

## 1. Hardware

| Scenario | Requirement |
|---|---|
| Local run (demo/evaluation) | Any machine able to run Python 3.10+: 1 vCPU, 512 MB RAM, and ~100 MB free disk are already enough (lightweight app, embedded SQLite). |
| Hosted deployment (optional, production) | A minimal instance from a free/low-cost provider (e.g., 512 MB–1 GB RAM) is enough given individual/academic usage volume (see `non-functional-requirements.md` §8). |

## 2. Software

| Layer | Required software |
|---|---|
| Runtime | Python 3.10 or newer |
| Package manager | `pip` (+ `venv` for environment isolation) |
| Framework and libraries | Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF, Flask-Talisman, argon2-cffi, cryptography, python-dotenv (full list and versions in `requirements.txt`, to be created together with the code) |
| Database | SQLite (built into Python — no separate database server installation) |
| Application server (production) | `gunicorn` (or an equivalent WSGI server) behind a reverse proxy, if deployed publicly — for a local demo, `flask run` is enough |
| Web server/proxy (production) | Optional: Nginx (or the hosting provider's own proxy) for TLS/HTTPS and extra headers |
| Operating system | Any OS with Python 3 support (Linux, macOS, Windows) — no specific OS dependency |
| Version control | Git + GitHub (this project's public repository) |

## 3. Services

| Service | Purpose | Needed for... |
|---|---|---|
| Remote Git repository (GitHub) | Versioning and change history (assignment instruction 2) | Always |
| HTTPS/TLS (certificate) | Required by the security NFRs (`Secure` cookies, HSTS via Flask-Talisman) whenever the app is exposed outside `localhost` | Only for hosted deployment, not the local demo |
| Application hosting (optional) | E.g., Render, Railway, or PythonAnywhere — a free/hobby tier is enough for the expected volume | Only if choosing to demo via a public URL instead of a video/local run |
| SQLite file storage | The hosting service's own persistent disk (or local disk, for the demo) | Always — there's no separate managed database service in the MVP |

## 4. Environment Variables and Secrets

No secret is committed to the repository (see `.gitignore`). The following variables are required at runtime:

| Variable | Purpose |
|---|---|
| `SECRET_KEY` | Flask's session-signing key. |
| `DATABASE_URL` | Path to the SQLite file (defaults to a local path if omitted). |
| `ENCRYPTION_KEY` | Fernet key for the `EncryptedString` mechanism (see `architecture-notebook.md` §5). |
| `ADMIN_EMAIL` / `ADMIN_PASSWORD` | Used only on first run, to create/promote the initial administrator account (see `vision-and-scope.md` § RBAC). |

In local development, these variables are loaded from a `.env` file (via `python-dotenv`), which is never committed.

## 5. Deployment Steps (Summary)

1. Provision the environment (local or hosted) with Python 3.10+.
2. Clone the repository and install dependencies (`pip install -r requirements.txt`).
3. Set the environment variables from section 4.
4. Run the initial migrations/schema creation (`flask db upgrade` or equivalent, to be defined together with the code).
5. Start the application: `flask run` (local demo) or `gunicorn app:app` behind an HTTPS proxy (hosted).
6. Verify the initial administrator account was created successfully and that the `/admin` dashboard is accessible only to it.
