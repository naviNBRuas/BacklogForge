from tests.conftest import signup_and_login


def test_key_pages_render(client):
    assert client.get("/auth/signup").status_code == 200
    assert client.get("/auth/login").status_code == 200

    signup_and_login(client)
    assert client.get("/projects/").status_code == 200
    assert client.get("/projects/new").status_code == 200

    resp = client.post("/projects/new", data={"name": "Proj", "description": ""})
    project_id = int(resp.headers["Location"].rstrip("/").split("/")[-1])

    assert client.get(f"/projects/{project_id}").status_code == 200
    assert client.get(f"/projects/{project_id}/backlogs/product").status_code == 200
    assert client.get(f"/projects/{project_id}/epics/").status_code == 200
    assert client.get(f"/projects/{project_id}/epics/new").status_code == 200
    assert client.get(f"/projects/{project_id}/backlogs/sprints/new").status_code == 200
    assert client.get(f"/projects/{project_id}/product/stories/new").status_code == 200

    resp = client.post(
        f"/projects/{project_id}/product/stories/new",
        data={"role_text": "customer", "action_text": "x", "benefit_text": "y"},
    )
    story_id = int(resp.headers["Location"].rstrip("/").split("/")[-1])
    assert client.get(f"/projects/{project_id}/stories/{story_id}").status_code == 200
    assert client.get(f"/projects/{project_id}/stories/{story_id}/criteria/new").status_code == 200
