import requests


def test_ping():
    response = requests.get('http://localhost:8000/ping')
    assert response.status_code == 200, 'Status code is not 200'
    assert response.json() == {"message": "pong"}, 'Mismatch in /ping answer'
