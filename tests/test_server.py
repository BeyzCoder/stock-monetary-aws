from fastapi.testclient import TestClient  
from api.main import app

client = TestClient(app)

def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"Status" : "Server Up Running!"}

# def test_routes():
#     resp = client.get("/statements/")
#     assert resp.status_code == 200
#     assert resp.json() == {"Status" : "Statement Route Working!"}

#     resp = client.get("/quotes/")
#     assert resp.status_code == 200
#     assert resp.json() == {"Status" : "Quotes Route Working!"}
