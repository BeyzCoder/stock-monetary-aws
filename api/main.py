from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from mangum import Mangum

from api.routes import statements, quotes

app = FastAPI()

app.include_router(statements.router, prefix="/statements")
app.include_router(quotes.router, prefix="/quotes")

@app.get("/")
async def root() -> JSONResponse:
    resp = {"Status" : "Server Up Running!"}
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp)

handler = Mangum(app=app) 