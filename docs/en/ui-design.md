# User Interface Design (Storyboards + Wireframes)

*(Assignment artifact 6: "user interface design", represented by storyboards made of wireframes — simple screen sketches. Canonical version for grading: [`docs/pt-BR/ui-design.md`](../pt-BR/ui-design.md).)*

> Each storyboard covers a key usage scenario, as a sequence of screens (wireframes). The wireframes are low-fidelity sketches (ASCII), enough to communicate layout and flow, not the final visual design.

## Storyboard 1 — Sign Up, Log In, and First Project

*Scenario: a new user creates an account, logs in, and creates their first project (US-01, US-02, US-05).*

```
┌─ Screen 1: Sign Up ─────────────┐   ┌─ Screen 2: Log In ──────────────┐
│ BacklogForge                    │   │ BacklogForge                    │
│                                  │   │                                  │
│ Email:     [______________]     │──▶│ Email:     [______________]     │
│ Password:  [______________]     │   │ Password:  [______________]     │
│ Confirm:   [______________]     │   │                                  │
│                                  │   │            [ Log in ]           │
│            [ Create account ]   │   │  No account? Sign up            │
│  Already have an account? Log in│   │                                  │
└──────────────────────────────────┘   └──────────────┬───────────────────┘
                                                        ▼
┌─ Screen 3: My Projects (empty) ─────────────────────────────────────┐
│ BacklogForge          [me@email.com ▾]  [Log out]                    │
│                                                                        │
│  My Projects                                       [ + New Project ] │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  No projects yet. Create your first one!                     │   │
│  └──────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────┬──────────────────────────────────┘
                                   ▼ (clicks "+ New Project")
┌─ Screen 4: Create Project ────────────────────────────────────────────┐
│  Name:         [___________________________]                          │
│  Description:  [___________________________]                          │
│                [___________________________]                          │
│                                            [ Cancel ] [ Create ]      │
└───────────────────────────────────────────────┬──────────────────────┘
                                                  ▼
┌─ Screen 5: Project Page ──────────────────────────────────────────────┐
│ ← My Projects    Project: "Sales System"             [Edit][Delete]  │
│  [ Product Backlog ]  [ Sprints ]  [ Epics ]                          │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  Product Backlog (0 stories)                  [+ New Story]  │   │
│  └──────────────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────────────┘
```

## Storyboard 2 — Create a User Story with Criteria and Estimation

*Scenario: the PO creates a story in the Product Backlog, adds acceptance criteria, and assigns story points/MoSCoW/RICE (US-15, US-24, US-28 to US-31).*

```
┌─ Screen 1: Product Backlog ─────────┐   ┌─ Screen 2: New Story ──────────────┐
│ Product Backlog        [+ New Story]│──▶│ As a: [_______________________]   │
│  (empty or existing list)            │   │ I want: [_____________________]   │
│                                       │   │ So that: [____________________]   │
│                                       │   │              [Cancel] [Save]      │
└───────────────────────────────────────┘   └────────────────┬─────────────────┘
                                                                ▼
┌─ Screen 3: Story Details ─────────────────────────────────────────────────┐
│ ← Back    "As a customer I want... so that..."                           │
│                                                                            │
│  Story Points: [ 5 ▾]   MoSCoW: [ M ▾]   Epic: [ (none) ▾]              │
│                                                                            │
│  RICE:  Reach [___]  Impact [3 ▾]  Confidence [100% ▾]  Effort [5 ▾]     │
│  Calculated RICE score: 60                                    [ Save ]   │
│                                                                            │
│  Acceptance Criteria                                  [+ New Criterion]  │
│  ┌────────────────────────────────────────────────────────────────┐    │
│  │ (empty list)                                                     │    │
│  └────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────┬────────────────────────────┘
                                               ▼ (clicks "+ New Criterion")
┌─ Screen 4: New Acceptance Criterion ───────────────────────────────────┐
│  Given:  [_____________________________________]                      │
│  When:   [_____________________________________]                      │
│  Then:   [_____________________________________]                      │
│                                          [ Cancel ] [ Save ]            │
└─────────────────────────────────────────────────────────────────────────┘
```

## Storyboard 3 — Plan a Sprint (Move Stories Between Backlogs)

*Scenario: the PO creates a sprint and moves stories from the Product Backlog into it (US-11, US-19).*

```
┌─ Screen 1: Project "Sprints" tab ───────┐   ┌─ Screen 2: New Sprint ───────────┐
│  Sprints                  [+ New Sprint]│──▶│ Name:  [___________________]    │
│  (empty list)                           │   │ Start: [___] End: [___]         │
│                                          │   │              [Cancel][Create]   │
└──────────────────────────────────────────┘   └────────────────┬─────────────────┘
                                                                  ▼
┌─ Screen 3: Product Backlog (with stories) ────────────────────────────────┐
│  ☐ US-1 "As a customer..."          RICE 60   [Move to ▾: Sprint 1]      │
│  ☐ US-2 "As a PO..."                RICE 40   [Move to ▾: Sprint 1]      │
│                                              [ Move selected ]            │
└──────────────────────────────────────┬─────────────────────────────────┘
                                        ▼
┌─ Screen 4: Sprint 1 (with moved stories) ────────────────────────────────┐
│ ← Sprints    Sprint 1 (Sep 1 – Sep 14)                                   │
│  US-1 "As a customer..."   RICE 60   [Return to Product Backlog]        │
└────────────────────────────────────────────────────────────────────────┘
```

## Storyboard 4 — Administrator Dashboard (RBAC + Auditing)

*Scenario: an account with the `admin` role monitors users, projects, and the audit log (US-33 to US-36).*

```
┌─ Screen 1: Log In (admin account) ┐   ┌─ Screen 2: Administrator Dashboard ─────────┐
│ Email:    [admin@...]             │──▶│ [Admin Dashboard]    [me@email.com ▾][Log out]│
│ Password: [_________]             │   │  [ Users ]  [ Projects ]  [ Audit Log ]      │
│           [ Log in ]              │   │                                                │
└──────────────────────────────────────┘   └───────────────┬───────────────────────────┘
                                                             ▼
┌─ Screen 3: Audit Log ──────────────────────────────────────────────────────┐
│  Filter by: User [___▾]  Action [___▾]  Period [___] to [___] [Filter]    │
│  ┌────────────────────────────────────────────────────────────────────┐ │
│  │ 2026-08-28 14:02  ana@x.com   create   user_story #12               │ │
│  │ 2026-08-28 13:58  ana@x.com   login                                 │ │
│  │ 2026-08-28 13:50  bob@x.com   login_failed                          │ │
│  └────────────────────────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────────────────────────────┘
```

> Note: a regular `user` account that tries to access `/admin/*` directly via URL gets a 403 (Access Denied) error screen, not a silent redirect — visually reinforcing the RBAC described in `non-functional-requirements.md` §3.
