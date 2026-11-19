from app import app


def test_index():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.get_json() == {"status": "online"}


def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_tasks():
    response = app.test_client().get("/tasks")
    assert response.status_code == 200
    assert len(response.get_json()) == 3
