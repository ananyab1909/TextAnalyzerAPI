import pytest
from flask import Flask
from app.routes import bp

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app.test_client()

def test_analyze_valid(client):
    res = client.post('/analyze', json={"text": "This is a good example"})
    assert res.status_code == 200
    data = res.get_json()
    assert data["word_count"] == 5
    assert data["sentiment"] == "positive"

def test_analyze_empty_text(client):
    res = client.post('/analyze', json={})
    assert res.status_code == 400
