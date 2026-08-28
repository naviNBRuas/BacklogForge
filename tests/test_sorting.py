from app.backlogs.routes import sort_stories


class FakeStory:
    def __init__(self, rice_score, moscow):
        self.rice_score = rice_score
        self.moscow = moscow


def test_sort_by_rice_descending():
    stories = [FakeStory(10, "M"), FakeStory(100, "S"), FakeStory(None, "C")]
    result = sort_stories(stories, "rice")
    assert [s.rice_score for s in result] == [100, 10, None]


def test_sort_by_moscow_order():
    stories = [FakeStory(0, "W"), FakeStory(0, "M"), FakeStory(0, "C"), FakeStory(0, "S")]
    result = sort_stories(stories, "moscow")
    assert [s.moscow for s in result] == ["M", "S", "C", "W"]


def test_no_sort_keeps_original_order():
    stories = [FakeStory(1, "M"), FakeStory(2, "S")]
    assert sort_stories(stories, None) is stories


def test_product_backlog_sort_endpoint(app, client):
    from tests.conftest import signup_and_login

    signup_and_login(client)
    resp = client.post("/projects/new", data={"name": "Proj", "description": ""})
    project_id = int(resp.headers["Location"].rstrip("/").split("/")[-1])

    for reach, name in [(10, "low"), (1000, "high")]:
        resp = client.post(
            f"/projects/{project_id}/product/stories/new",
            data={"role_text": "user", "action_text": name, "benefit_text": "x"},
        )
        story_id = int(resp.headers["Location"].rstrip("/").split("/")[-1])
        client.post(
            f"/projects/{project_id}/stories/{story_id}/estimate",
            data={
                "story_points": "", "moscow": "", "epic_id": "0",
                "rice_reach": str(reach), "rice_impact": "3", "rice_confidence": "1.0", "rice_effort": "1",
            },
        )

    resp = client.get(f"/projects/{project_id}/backlogs/product?sort=rice")
    assert resp.status_code == 200
    body = resp.get_data(as_text=True)
    assert body.index("high") < body.index("low")
