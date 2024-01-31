from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
async def statement() -> JSONResponse:
    resp = {"Status" : "Statement Route Working!"}
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp)

@router.get("/income/{symbol}")
async def income(symbol: str) -> JSONResponse:
    resp = {"income_statement" : symbol}
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp)

@router.get("/balance/{symbol}")
async def balance(symbol: str) -> JSONResponse:
    resp = {"balance_statement" : symbol}
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp)

@router.get("/cash/{symbol}")
async def cash(symbol: str) -> JSONResponse:
    resp = {"cash_statement" : symbol}
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp)
