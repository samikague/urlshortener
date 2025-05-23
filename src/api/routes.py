from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from src.database.requests import main_methods, actions_methods
from src.api.classes import ShortUrl_class, Authorize_Class
from src.api.misc import Response


router = APIRouter()

@router.get("/health", status_code=200, responses=Response.Health_Response)
async def health_check() -> dict:
    return {"status": "ok"}

@router.post("/create", status_code=200, responses=Response.Create_Response)
async def create_short_url(data: ShortUrl_class, req: Request) -> dict:
    methods = main_methods()
    isSuccess, OutcomingData = await methods.create_shorturl(original_url=data.original_url)
    if isSuccess:
        return {
            "Short_Url": f"{req.base_url}api/{OutcomingData["SUrl"]}",
            "Control_Token": OutcomingData["CToken"]
                }
    else:
        return {"message": {OutcomingData["error"]}}
    

@router.get("/{short_url}", status_code=301)
async def redirect_to_short_url(short_url):
    methods = main_methods()
    isSuccess, OutcomingData = await methods.get_original_url(short_url)
    if isSuccess and OutcomingData != "None":
        return RedirectResponse(OutcomingData)
    else:
        return {"message": OutcomingData}

    

@router.delete("/{short_url}", responses=Response.Delete_Response)
async def delete_short_url(data: Authorize_Class, short_url: str) -> dict:
    methods = actions_methods()
    isSuccess, OutcomingData = await methods.delete_short_url(Short_Url=short_url, Control_Token=data.control_token)
    if isSuccess:
        return {"message": OutcomingData["message"]}
    else:
        return {"message": OutcomingData["error"]}

@router.put("/{short_url}", responses=Response.Regenerate_Response)
async def regenerate_short_url(data: Authorize_Class, short_url: str) -> dict:
    methods = actions_methods()
    isSuccess, OutcomingData = await methods.regenerate_short_url(Short_Url=short_url, Control_Token=data.control_token)
    if isSuccess:
        return {"message": OutcomingData["message"]}
    else:
        return {"message": OutcomingData["error"]}
