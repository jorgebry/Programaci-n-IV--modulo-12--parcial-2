from app import app

def test_get_vacunas():
    client = app.test_client()
    response = client.get("/vacunas")
    assert response.status_code == 200
    assert "datos" in response.get_json()
