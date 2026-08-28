from app.extensions import db
from app.models import AuditLog, Project, User
from tests.conftest import signup_and_login


def test_signup_hashes_password(app, client):
    signup_and_login(client)
    with app.app_context():
        user = User.query.filter_by(email="user@example.com").first()
        assert user is not None
        assert user.password_hash != "password123"


def test_login_failure_is_audited(app, client):
    client.post("/auth/login", data={"email": "nope@example.com", "password": "wrong"})
    with app.app_context():
        assert AuditLog.query.filter_by(action="login_failed").count() == 1


def test_unauthenticated_user_redirected_to_login(client):
    response = client.get("/projects/")
    assert response.status_code == 302
    assert "/auth/login" in response.headers["Location"]


def test_create_project_creates_product_backlog(app, client):
    signup_and_login(client)
    client.post("/projects/new", data={"name": "Sales System", "description": "desc"})
    with app.app_context():
        project = Project.query.filter_by(name="Sales System").first()
        assert project is not None
        assert project.product_backlog is not None


def test_user_cannot_access_other_users_project(app, client):
    signup_and_login(client, email="a@example.com")
    resp = client.post("/projects/new", data={"name": "A's Project", "description": ""})
    project_id = int(resp.headers["Location"].rstrip("/").split("/")[-1])
    client.get("/auth/logout")

    signup_and_login(client, email="b@example.com")
    resp = client.get(f"/projects/{project_id}")
    assert resp.status_code == 403


def test_full_story_lifecycle(app, client):
    signup_and_login(client)
    resp = client.post("/projects/new", data={"name": "Proj", "description": ""})
    project_id = int(resp.headers["Location"].rstrip("/").split("/")[-1])

    resp = client.post(
        f"/projects/{project_id}/product/stories/new",
        data={"role_text": "customer", "action_text": "buy things", "benefit_text": "save time"},
    )
    story_id = int(resp.headers["Location"].rstrip("/").split("/")[-1])

    client.post(
        f"/projects/{project_id}/stories/{story_id}/criteria/new",
        data={"given_text": "I am logged in", "when_text": "I checkout", "then_text": "I get a receipt"},
    )

    client.post(
        f"/projects/{project_id}/stories/{story_id}/estimate",
        data={
            "story_points": "5", "moscow": "M", "epic_id": "0",
            "rice_reach": "100", "rice_impact": "3", "rice_confidence": "1.0", "rice_effort": "5",
        },
    )

    client.post(f"/projects/{project_id}/backlogs/sprints/new", data={"name": "Sprint 1"})

    with app.app_context():
        from app.models import UserStory, SprintBacklog

        story = UserStory.query.get(story_id)
        assert story.story_points == 5
        assert story.moscow == "M"
        assert story.rice_score == 60.0
        assert len(story.acceptance_criteria) == 1

        sprint = SprintBacklog.query.filter_by(name="Sprint 1").first()

    client.post(
        f"/projects/{project_id}/stories/{story_id}/move",
        data={"sprint_backlog_id": str(sprint.id)},
    )
    with app.app_context():
        story = UserStory.query.get(story_id)
        assert story.sprint_backlog_id == sprint.id
        assert story.product_backlog_id is None

    client.post(f"/projects/{project_id}/backlogs/sprints/{sprint.id}/delete")
    with app.app_context():
        story = UserStory.query.get(story_id)
        assert story.sprint_backlog_id is None
        assert story.product_backlog_id is not None


def test_non_admin_cannot_access_admin_dashboard(client):
    signup_and_login(client)
    resp = client.get("/admin/")
    assert resp.status_code == 403


def test_admin_can_access_dashboard(app, client):
    with app.app_context():
        from argon2 import PasswordHasher

        admin = User(email="admin@example.com", password_hash=PasswordHasher().hash("adminpass1"), role="admin")
        db.session.add(admin)
        db.session.commit()

    client.post("/auth/login", data={"email": "admin@example.com", "password": "adminpass1"})
    resp = client.get("/admin/")
    assert resp.status_code == 200
