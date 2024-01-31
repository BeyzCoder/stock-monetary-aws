from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
async def quotes() -> JSONResponse:
    resp = {"Status" : "Quotes Route Working!"}
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp)

@router.get("/history-price/dates/{symbol}")
async def history_price(symbol: str) -> JSONResponse:
    resp = {"history_price" : symbol}
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp)

@router.get("/dividend/dates/{symbol}")
async def dividend(symbol: str) -> JSONResponse:
    resp = {"dividend" : symbol}
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp)

@router.get("/stock-split/dates/{symbol}")
async def stock_split(symbol: str) -> JSONResponse:
    resp = {"stock_split" : symbol}
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp)
