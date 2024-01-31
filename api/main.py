from fastapi import FastAPI
from fastapi.responses import JSONResponse
from mangum import Mangum

app = FastAPI()

@app.get("/")
async def root() -> JSONResponse:
    return {"Status" : "Server Running!"}

handler = Mangum(app=app)