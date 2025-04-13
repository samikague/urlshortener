from typing import Any
from fastapi import FastAPI, APIRouter
from fastapi.responses import RedirectResponse
from .classes import ShortUrl


router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.post("/create", status_code=200)
async def create_short_url() -> dict:
    return {"message": "There is nothing here at the moment"}

@router.get("/url/{short_url}", status_code=301)
async def redirect_to_short_url() -> dict:
    return {"message": "There is nowhere to redirect at the moment"}
