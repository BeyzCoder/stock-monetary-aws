from fastapi.testclient import TestClient  
from api.main import app

client = TestClient(app)

def test_income():
    symbol = "O"
    resp = client.get("/statements/income/O")
    assert resp.status_code == 200
    assert resp.json() == {"income_statement" : symbol}

def test_balance():
    symbol = "AAPL"
    resp = client.get("/statements/balance/AAPL")
    assert resp.status_code == 200
    assert resp.json() == {"balance_statement" : symbol}

def test_cash():
    symbol = "AMZN"
    resp = client.get("/statements/cash/AMZN")
    assert resp.status_code == 200
    assert resp.json() == {"cash_statement" : symbol}

