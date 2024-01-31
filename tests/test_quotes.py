from fastapi.testclient import TestClient  
from api.main import app

client = TestClient(app)

def test_history_prices():
    symbol = "O"
    resp = client.get("/quotes/history-price/dates/O")
    assert resp.status_code == 200
    assert resp.json() == {"history_prices" : symbol}

def test_dividend():
    symbol = "AAPL"
    resp = client.get("/quotes/dividend/dates/AAPL")
    assert resp.status_code == 200
    assert resp.json() == {"dividend" : symbol}

def test_stock_split():
    symbol = "AMZN"
    resp = client.get("/quotes/stock-split/dates/AMZN")
    assert resp.status_code == 200
    assert resp.json() == {"stock_split" : symbol}

