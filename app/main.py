from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
import middleware
import database
from routers import test_endpoints
import uvicorn

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.db.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.db.disconnect()

app.add_middleware(BaseHTTPMiddleware, dispatch=middleware.db_logging)
app.include_router(test_endpoints.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)