# User Story Backlog

*(Assignment artifact 4: "functional requirements specification via user stories". Canonical version for grading: [`docs/pt-BR/user-stories.md`](../pt-BR/user-stories.md).)*

> Covers the 19 numbered requirements in [`docs/spec/ESW-TRABALHO-PRATICO.md`](../spec/ESW-TRABALHO-PRATICO.md) (section 2). Each story follows the `As a [role] I want [action] so that [benefit]` format; each acceptance criterion follows `Given/When/Then`. Roles used: **User** (any authenticated person), **Product Owner (PO)**, and **Developer** (roles within a project — see `vision-and-scope.md`).
>
> Each story carries Story Points (series 0,1,2,3,5,8,13,21,34,55), MoSCoW (M/S/C/W), and RICE (R×I×C/E). These three fields prioritize *building this backlog* (they're attributes of managing this own work, not of the system being built) — the system in turn must let end users assign these same fields to the stories they register (requirements 14–19).

## Epic 1 — Authentication and User Account

*Covers requirements (2), (3).*

### US-01 — Create an account
As a **user**, I want to create an account with email and password, so that I can access the system.

- **Acceptance criterion 1**: Given I'm on the signup screen, when I provide a valid email, password, and password confirmation, then my account is created and the password is stored hashed (never in plain text).
- **Acceptance criterion 2**: Given I provide an email that's already registered, when I submit the signup form, then I get an error message and no duplicate account is created.

**Story Points**: 3 · **MoSCoW**: M (Must) · **RICE**: R=100, I=3, C=100%, E=3 → **100**

### US-02 — Log in
As a **user**, I want to log in with email and password, so that I can access the system's services.

- **Acceptance criterion 1**: Given I have an account, when I provide the correct email and password, then I'm authenticated and redirected to my project list.
- **Acceptance criterion 2**: Given I provide incorrect credentials, when I submit the login form, then I get an error message and remain unauthenticated.

**Story Points**: 2 · **MoSCoW**: M · **RICE**: R=100, I=3, C=100%, E=2 → **150**

### US-03 — Restrict access to authenticated users
As a **user**, I want data routes to require login, so that my projects stay protected from unauthorized access.

- **Acceptance criterion 1**: Given I'm not authenticated, when I try to access any project/backlog/story route, then I'm redirected to the login screen.
- **Acceptance criterion 2**: Given I'm authenticated, when I access a project URL that isn't mine, then I get an access-denied error (403/404), not another user's data.

**Story Points**: 3 · **MoSCoW**: M · **RICE**: R=100, I=2, C=100%, E=3 → **67**

### US-04 — Log out
As a **user**, I want to end my session, so that no one else can stay logged in as me.

- **Acceptance criterion 1**: Given I'm authenticated, when I click "Log out", then my session ends and I'm redirected to the login screen.

**Story Points**: 1 · **MoSCoW**: S (Should) · **RICE**: R=100, I=1, C=100%, E=1 → **100**

## Epic 2 — Projects

*Covers requirement (4).*

### US-05 — Create a project
As a **user**, I want to create a project with a name and description, so that I can start organizing its backlog.

- **Acceptance criterion**: Given I'm authenticated, when I fill in a name (required) and description and submit the form, then the project is created, associated with me, and an empty Product Backlog is created automatically for it.

**Story Points**: 3 · **MoSCoW**: M · **RICE**: R=100, I=3, C=100%, E=3 → **100**

### US-06 — List and view projects
As a **user**, I want to see the list of my projects and open the details of one, so that I can track its progress.

- **Acceptance criterion**: Given I have one or more projects, when I access the home screen, then I see all my projects listed; opening one shows its data, its Product Backlog, and its Sprint Backlogs.

**Story Points**: 2 · **MoSCoW**: M · **RICE**: R=100, I=2, C=100%, E=2 → **100**

### US-07 — Edit a project
As a **user**, I want to update a project's name/description, so that its information stays correct.

- **Acceptance criterion**: Given I own the project, when I change name/description and save, then the new data is persisted and reflected in the listing.

**Story Points**: 2 · **MoSCoW**: S · **RICE**: R=100, I=1, C=100%, E=2 → **50**

### US-08 — Delete a project
As a **user**, I want to delete a project I no longer use, so that my list stays organized.

- **Acceptance criterion 1**: Given I own the project, when I confirm deletion, then the project and all its dependent data (backlogs, stories, epics, criteria) are removed.
- **Acceptance criterion 2**: Given I request deletion, when the system asks for confirmation, then deletion only happens after explicit confirmation.

**Story Points**: 3 · **MoSCoW**: S · **RICE**: R=60, I=1, C=80%, E=3 → **16**

## Epic 3 — Product Backlog

*Covers requirement (5).*

### US-09 — View the project's Product Backlog
As a **PO**, I want to view my project's Product Backlog, so that I can see all stories not yet moved into a sprint.

- **Acceptance criterion**: Given the project exists, when I access its "Product Backlog" tab, then I see all stories associated with it, ordered by priority (RICE or MoSCoW).

**Story Points**: 2 · **MoSCoW**: M · **RICE**: R=100, I=2, C=100%, E=2 → **100**

### US-10 — Edit Product Backlog data
As a **PO**, I want to edit Product Backlog information (e.g., description/notes), so that I can document its purpose.

- **Acceptance criterion**: Given the Product Backlog exists (created together with the project), when I edit its description and save, then the change is persisted.

**Story Points**: 1 · **MoSCoW**: C (Could) · **RICE**: R=100, I=0.5, C=80%, E=1 → **40**

> There's no standalone "create/delete Product Backlog" story: requirement (5) states there is **exactly one** Product Backlog per project, created together with it (US-05) and removed together with it (US-08) — creating/deleting it separately doesn't make business sense.

## Epic 4 — Sprint Backlogs

*Covers requirement (6).*

### US-11 — Create a Sprint Backlog
As a **PO**, I want to create a new Sprint Backlog inside a project, so that I can plan a sprint's work.

- **Acceptance criterion**: Given I'm on the project page, when I provide the sprint's name/period and confirm, then a new empty Sprint Backlog is created and listed among the project's sprints.

**Story Points**: 3 · **MoSCoW**: M · **RICE**: R=100, I=3, C=100%, E=3 → **100**

### US-12 — List and view Sprint Backlogs
As a **user**, I want to see all Sprint Backlogs of a project and open each one, so that I can track sprint planning.

- **Acceptance criterion**: Given the project has one or more sprints, when I access its sprints tab, then all of them are listed; opening one shows the stories it contains.

**Story Points**: 2 · **MoSCoW**: M · **RICE**: R=100, I=2, C=100%, E=2 → **100**

### US-13 — Edit a Sprint Backlog
As a **PO**, I want to edit a Sprint Backlog's name/period, so that I can correct the plan.

- **Acceptance criterion**: Given the sprint exists, when I change its data and save, then the changes are persisted.

**Story Points**: 2 · **MoSCoW**: S · **RICE**: R=90, I=1, C=80%, E=2 → **36**

### US-14 — Delete a Sprint Backlog
As a **PO**, I want to delete a Sprint Backlog, so that I can remove a cancelled sprint or one created by mistake.

- **Acceptance criterion**: Given the sprint exists, when I confirm deletion, then the sprint is removed and its stories automatically return to the Product Backlog (they are not deleted).

**Story Points**: 3 · **MoSCoW**: S · **RICE**: R=70, I=1, C=80%, E=3 → **19**

## Epic 5 — User Stories

*Covers requirements (7), (8), (9).*

### US-15 — Create a user story
As a **PO**, I want to create a user story in the `As/I want/So that` format, so that I can register a functional requirement of the system being planned.

- **Acceptance criterion 1**: Given I'm in a project's Product Backlog, when I fill in role, action, and benefit and save, then the story is created and automatically associated with the project's Product Backlog.
- **Acceptance criterion 2**: Given I leave any of the three fields empty, when I try to save, then I get a validation error and the story is not created.

**Story Points**: 5 · **MoSCoW**: M · **RICE**: R=100, I=3, C=100%, E=5 → **60**

### US-16 — List and view stories
As a **user**, I want to see the list of a backlog's stories and open the details of each one, so that I can track its content, estimate, and criteria.

- **Acceptance criterion**: Given the backlog has stories, when I access it, then all are listed with role/action/benefit summarized; opening one shows its acceptance criteria, story points, MoSCoW, and RICE.

**Story Points**: 3 · **MoSCoW**: M · **RICE**: R=100, I=2, C=100%, E=3 → **67**

### US-17 — Edit a user story
As a **PO**, I want to edit a story's role/action/benefit, so that I can correct or refine its text.

- **Acceptance criterion**: Given the story exists, when I change its text and save, then the new version is persisted.

**Story Points**: 2 · **MoSCoW**: S · **RICE**: R=90, I=1, C=90%, E=2 → **41**

### US-18 — Delete a user story
As a **PO**, I want to delete an obsolete user story, so that I can keep the backlog clean.

- **Acceptance criterion**: Given the story exists, when I confirm deletion, then it and its associated acceptance criteria are removed.

**Story Points**: 2 · **MoSCoW**: S · **RICE**: R=70, I=1, C=80%, E=2 → **28**

### US-19 — Move a story between backlogs
As a **PO**, I want to move a story from the Product Backlog to a Sprint Backlog (and vice versa), so that I can plan what will be done in each sprint.

- **Acceptance criterion 1**: Given a story is in the Product Backlog, when I select a destination Sprint Backlog and confirm, then the story now belongs to that sprint and disappears from the Product Backlog listing.
- **Acceptance criterion 2**: Given a story is in a Sprint Backlog, when I choose "return to Product Backlog", then it returns there.

**Story Points**: 5 · **MoSCoW**: M · **RICE**: R=100, I=3, C=90%, E=5 → **54**

## Epic 6 — Epics

*Covers requirements (10), (11).*

### US-20 — Create an epic
As a **PO**, I want to create an epic with a name and description, so that I can group stories related to a larger theme.

- **Acceptance criterion**: Given I'm in the project, when I provide the epic's name/description and save, then the epic is created and listed in the project.

**Story Points**: 2 · **MoSCoW**: S · **RICE**: R=80, I=1, C=80%, E=2 → **32**

### US-21 — List and view epics
As a **user**, I want to see a project's epics and the stories linked to each one, so that I can understand the progress of a larger theme.

- **Acceptance criterion**: Given epics with linked stories exist, when I open an epic, then I see its description and the list of associated stories.

**Story Points**: 2 · **MoSCoW**: S · **RICE**: R=80, I=1, C=80%, E=2 → **32**

### US-22 — Edit and delete an epic
As a **PO**, I want to edit or delete an epic, so that I can correct its content or remove it if it no longer makes sense.

- **Acceptance criterion 1**: Given the epic exists, when I change its data and save, then the change is persisted.
- **Acceptance criterion 2**: Given I delete an epic, when I confirm, then the epic is removed and stories linked to it remain in the system, just unlinked.

**Story Points**: 2 · **MoSCoW**: C · **RICE**: R=60, I=0.5, C=80%, E=2 → **12**

### US-23 — Link a story to an epic
As a **PO**, I want to link a user story to an epic, so that I can relate it to a larger product goal.

- **Acceptance criterion 1**: Given at least one epic exists in the project, when I open a story and select an epic, then the story now shows that link.
- **Acceptance criterion 2**: Given a story is linked to an epic, when I remove the link, then the story still exists, just without an associated epic.

**Story Points**: 3 · **MoSCoW**: S · **RICE**: R=80, I=1, C=80%, E=3 → **21**

## Epic 7 — Acceptance Criteria

*Covers requirements (12), (13).*

### US-24 — Create an acceptance criterion
As a **PO**, I want to add acceptance criteria to a story in the `Given/When/Then` format, so that it's clear when the story can be considered done.

- **Acceptance criterion 1**: Given I'm on a story's page, when I fill in context, action, and expected result and save, then a new criterion is created and listed under that story.
- **Acceptance criterion 2**: Given I leave any of the three fields empty, when I try to save, then I get a validation error.

**Story Points**: 3 · **MoSCoW**: M · **RICE**: R=100, I=2, C=100%, E=3 → **67**

### US-25 — List a story's criteria
As a **user**, I want to see all of a story's acceptance criteria, so that I fully understand what needs to be validated.

- **Acceptance criterion**: Given the story has one or more criteria, when I open its details, then all criteria appear listed in the order they were created.

**Story Points**: 1 · **MoSCoW**: M · **RICE**: R=100, I=2, C=100%, E=1 → **200**

### US-26 — Edit an acceptance criterion
As a **PO**, I want to edit an existing acceptance criterion, so that I can correct or refine its description.

- **Acceptance criterion**: Given the criterion exists, when I change its text and save, then the new version is persisted.

**Story Points**: 2 · **MoSCoW**: S · **RICE**: R=90, I=1, C=90%, E=2 → **41**

### US-27 — Delete an acceptance criterion
As a **PO**, I want to delete an obsolete acceptance criterion, so that the story keeps only relevant criteria.

- **Acceptance criterion**: Given the criterion exists, when I confirm deletion, then it's removed from the story.

**Story Points**: 1 · **MoSCoW**: S · **RICE**: R=70, I=1, C=90%, E=1 → **63**

## Epic 8 — Estimation and Prioritization (Story Points, MoSCoW, RICE)

*Covers requirements (14), (15), (16), (17), (18), (19).*

### US-28 — Assign story points to a story
As a **PO**, I want to assign story points to a user story, so that I can estimate its relative effort.

- **Acceptance criterion 1**: Given I'm editing a story, when I select a story points value, then only 0, 1, 2, 3, 5, 8, 13, 21, 34, or 55 are available to choose from.
- **Acceptance criterion 2**: Given I try to submit a value outside that series (e.g., via a manual request), when the system validates it, then the assignment is rejected with a validation error.

**Story Points**: 2 · **MoSCoW**: M · **RICE**: R=100, I=2, C=100%, E=2 → **100**

### US-29 — Assign a MoSCoW label to a story
As a **PO**, I want to assign a MoSCoW label (M, S, C, or W) to a story, so that I can communicate its qualitative priority to the team.

- **Acceptance criterion**: Given I'm editing a story, when I select one of the four options (Must, Should, Could, Won't) and save, then the label is shown alongside the story in listings.

**Story Points**: 2 · **MoSCoW**: M · **RICE**: R=100, I=2, C=100%, E=2 → **100**

### US-30 — Assign RICE criteria to a story
As a **PO**, I want to assign Reach, Impact, Confidence, and Effort to a story, so that I can calculate its quantitative priority.

- **Acceptance criterion 1**: Given I'm editing a story, when I provide Reach (number of users), Impact (3, 2, 1, 0.5, or 0.25), Confidence (100%, 80%, or 50%), and Effort (0,1,2,3,5,8,13,21,34,55), then the values are saved.
- **Acceptance criterion 2**: Given I provide an Impact, Confidence, or Effort value outside the valid options, when I try to save, then I get a validation error.

**Story Points**: 3 · **MoSCoW**: M · **RICE**: R=100, I=3, C=100%, E=3 → **100**

### US-31 — Calculate and display the RICE score
As a **PO**, I want the system to automatically calculate a story's RICE score, so that I don't have to compute `(R×I×C)/E` manually.

- **Acceptance criterion 1**: Given a story has Reach, Impact, Confidence, and Effort filled in, when I view the story (or the backlog listing), then the calculated RICE score is shown.
- **Acceptance criterion 2**: Given Effort is greater than zero and the other fields have valid values, when the calculation runs, then the result is exactly `(Reach × Impact × Confidence) / Effort`.

**Story Points**: 3 · **MoSCoW**: M · **RICE**: R=100, I=3, C=100%, E=3 → **100**

### US-32 — Sort the backlog by priority
As a **PO**, I want to sort a backlog's stories by RICE score (or by MoSCoW label), so that I can quickly decide what to tackle first.

- **Acceptance criterion**: Given the backlog has stories with a calculated RICE score, when I choose "sort by RICE", then stories appear from highest to lowest score.

**Story Points**: 3 · **MoSCoW**: C · **RICE**: R=90, I=1, C=80%, E=3 → **24**

## Epic 9 — RBAC, Security, and Auditing

*Extends the original scope (see `vision-and-scope.md` § Role-Based Access Control); doesn't derive from a numbered assignment requirement, but from an additional requirement the author decided to add.*

### US-33 — Assign the Administrator role
As an **Administrator**, I want a distinct `admin` role separate from the default `user` role, so that only designated accounts get access to system monitoring.

- **Acceptance criterion 1**: Given an account has the `user` role, when it tries to access an Administrator-only route, then it gets an access-denied error (403).
- **Acceptance criterion 2**: Given the application runs for the first time, when the initial administrator account is set via environment variable/seed, then that account gets the `admin` role.

**Story Points**: 3 · **MoSCoW**: M · **RICE**: R=1, I=2, C=100%, E=3 → **1**

### US-34 — Admin dashboard: users and projects
As an **Administrator**, I want to see the list of all users and all projects in the system, so that I can monitor overall application usage.

- **Acceptance criterion**: Given I'm authenticated as an Administrator, when I access the admin dashboard, then I see the full list of users (email, creation date) and projects (name, owner, creation date), without being able to edit other users' project content.

**Story Points**: 3 · **MoSCoW**: M · **RICE**: R=1, I=2, C=90%, E=3 → **1**

### US-35 — Audit log of actions
As an **Administrator**, I want every entity creation, edit, and deletion (and login/logout/failed login) to generate an audit record, so that I can investigate what happened in the system.

- **Acceptance criterion 1**: Given an entity (project, backlog, story, epic, criterion) is created, edited, or deleted, when the operation completes, then a record is stored with: responsible user, action, affected entity, and timestamp.
- **Acceptance criterion 2**: Given a login attempt fails, when that happens, then an audit record is stored with the attempted email and timestamp (without storing the password).

**Story Points**: 5 · **MoSCoW**: M · **RICE**: R=1, I=3, C=90%, E=5 → **1**

### US-36 — View the audit log
As an **Administrator**, I want to view and filter the audit log (by user, action type, period), so that I can investigate incidents or misuse.

- **Acceptance criterion**: Given audit records exist, when I access the logs screen as Administrator and apply a filter, then I see only records matching the filter, ordered from most recent to oldest.

**Story Points**: 3 · **MoSCoW**: S · **RICE**: R=1, I=1, C=80%, E=3 → **0.3**

### US-37 — Secure session and password
As a **user**, I want my password stored with strong hashing and my session protected by secure cookies, so that my account isn't easily compromised.

- **Acceptance criterion 1**: Given I create or change my password, when it's persisted, then it's stored as an Argon2 hash (never in plain text, never reversible).
- **Acceptance criterion 2**: Given I'm authenticated, when I inspect the session cookie, then it has the `HttpOnly`, `Secure` (in production), and `SameSite=Lax` (or stricter) attributes.
- **Acceptance criterion 3**: Given I submit a form without a valid CSRF token, when the server processes the request, then it's rejected.

**Story Points**: 5 · **MoSCoW**: M · **RICE**: R=100, I=3, C=100%, E=5 → **60**

### US-38 — Encrypt sensitive data at rest
As a **user**, I want fields marked as sensitive (e.g., private project notes, if any) to be encrypted in the database, so that a leak of the SQLite file doesn't expose that data in plain text.

- **Acceptance criterion 1**: Given a field is marked sensitive in the data model, when it's written to the database, then its value is encrypted (Fernet/AES) and doesn't appear in plain text under direct inspection of the `.sqlite3` file.
- **Acceptance criterion 2**: Given the field is read back by the application, when shown to an authorized user, then it appears normally decrypted.

**Story Points**: 5 · **MoSCoW**: S · **RICE**: R=60, I=1, C=70%, E=5 → **8**

## Summary by MoSCoW Priority

| MoSCoW | Stories |
|---|---|
| **Must (M)** | US-01, US-02, US-03, US-05, US-06, US-09, US-11, US-12, US-15, US-16, US-19, US-24, US-25, US-28, US-29, US-30, US-31, US-33, US-34, US-35, US-37 |
| **Should (S)** | US-04, US-07, US-08, US-13, US-14, US-17, US-18, US-20, US-21, US-23, US-26, US-27, US-36, US-38 |
| **Could (C)** | US-10, US-22, US-32 |
| **Won't (this release)** | — (none identified beyond the MVP scope described in `vision-and-scope.md`) |

## Traceability to the Assignment's Requirements

| Requirement (assignment, section 2) | Stories |
|---|---|
| (1) TUI/GUI interface | Addressed by the stack (see `tech-stack.md`), not a standalone story — it's an NFR. |
| (2), (3) Account and authentication | US-01, US-02, US-03, US-04 |
| (4) Projects CRUD | US-05 to US-08 |
| (5) Product Backlog CRUD | US-09, US-10 |
| (6) Sprint Backlogs CRUD | US-11 to US-14 |
| (7) User Stories CRUD | US-15 to US-18 |
| (8) Move stories between backlogs | US-19 |
| (9) Standard story format | US-15 (acceptance criterion 1) |
| (10) Epics CRUD | US-20 to US-22 |
| (11) Link story to epic | US-23 |
| (12) Acceptance Criteria CRUD | US-24 to US-27 |
| (13) Standard acceptance criterion format | US-24 (acceptance criterion 1) |
| (14), (15) Story points | US-28 |
| (16) MoSCoW label | US-29 |
| (17), (18) RICE criteria | US-30 |
| (19) RICE score calculation | US-31 |
| Additional requirement: RBAC, security, and auditing (author's decision, not numbered in the assignment) | US-33 to US-38 |
