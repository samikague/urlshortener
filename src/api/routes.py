from fastapi import APIRouter



router = APIRouter()

@router.get("/health")
async def health_check() -> dict:
    return {"status": "ok"}

@router.post("/create", status_code=200)
async def create_short_url() -> dict:
    return {"message": "There is nothing here at the moment"}

@router.get("/{short_url}", status_code=301)
async def redirect_to_short_url() -> dict:
    return {"message": "There is nowhere to redirect at the moment"}

@router.post("/{short_url}/delete")
async def delete_short_url() -> dict:
    return {"message": "Here will be the function for deleting short url by authorize_id"}

@router.post("/{short_url}/regen")
async def regenerate_short_url() -> dict:
    return {"message": "Here will be function for regenerate short url by authorize_id"}
