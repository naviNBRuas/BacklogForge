# Demo Video Script

*(Supports Instructions 23–24 of the assignment: the video must demonstrate the prototype working correctly, with one success scenario for each service provided. Canonical version: [`docs/pt-BR/video-script.md`](../pt-BR/video-script.md). This checklist ensures no service is left out of the recording.)*

> Suggestion: record in a single continuous session, following the order below — it matches the system's natural usage flow (Epics 1 to 9 of the user story backlog).

## Scenario Checklist (one per service)

- [ ] **1. Authentication** — sign up (US-01), try accessing `/projects/` while logged out and get redirected (US-03), log in (US-02), log out (US-04).
- [ ] **2. Projects** — create a project (US-05), see it listed (US-06), edit name/description (US-07).
- [ ] **3. Product Backlog** — open the automatically-created Product Backlog (US-09), edit its notes (US-10).
- [ ] **4. Sprint Backlogs** — create a sprint (US-11), open the project's sprint list (US-12), edit the sprint (US-13).
- [ ] **5. User Stories** — create a story in the Product Backlog using the As/I want/So that format (US-15), view its details (US-16), edit it (US-17), move it into the sprint created above (US-19).
- [ ] **6. Epics** — create an epic (US-20), open the epic list (US-21), link the story from step 5 to the epic (US-23).
- [ ] **7. Acceptance Criteria** — add a Given/When/Then criterion to the story (US-24), view the criteria list (US-25), edit the criterion (US-26).
- [ ] **8. Estimation and Prioritization** — assign story points, MoSCoW, and RICE criteria to the story (US-28 to US-30), show the automatically calculated RICE score (US-31), sort the Product Backlog by RICE and by MoSCoW (US-32).
- [ ] **9. RBAC, Security, and Auditing** — log in as the seeded Administrator account, open `/admin` (US-33, US-34), show the audit log containing the actions recorded in the previous steps (US-35, US-36); try accessing `/admin` with the regular account and show the 403 error (reinforces RBAC).
- [ ] **Deletions** (optional but recommended): delete a criterion, a story, an epic, a sprint (showing stories returning to the Product Backlog), and finally the whole project (showing the cascade delete).

## Recording Notes

- Run locally with `flask --app run.py run` (see `README.md`, "Running Locally" section) — no production deployment is needed for the video.
- Show the browser's address bar on every screen transition, to make clear these are real pages served by Flask, not mockups.
- When demonstrating RBAC (step 9), make it explicit that two different accounts are involved (regular user vs. administrator) — e.g., by showing the logged-in email in the top-right corner before and after switching accounts.
