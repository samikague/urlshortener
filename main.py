from fastapi import FastAPI
import uvicorn
from loguru import logger
import PyRandomString

from src.database.database import init_db
from src.api.routes import router as api_router
from fastapi.responses import RedirectResponse

app = FastAPI()


app.include_router(api_router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.get("/")
async def root():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    try:
        uvicorn.run("main:app", host="0.0.0.0", port=8000)
    except Exception as e:
        logger.error(e)