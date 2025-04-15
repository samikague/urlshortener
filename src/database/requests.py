from typing import Tuple
import PyRandomString
from loguru import logger
from sqlalchemy import Select, Delete, Update
from src.database.database import async_session
from src.database.models import ShortUrl

class main_methods:
    async def create_shorturl(self, original_url: str) -> Tuple[bool, dict]:
        async with async_session() as session:
            prs = PyRandomString.RandomString()
            short_code = prs.get_string()
            control_token = prs.get_string(max_length=32)
            new_short_url = ShortUrl(
                                    control_token=control_token,
                                    original_url=original_url,
                                    short_code=short_code
                                     )
            try:
                session.add(new_short_url)
                await session.commit()
                return True, {
                    "SUrl": short_code,
                    "CToken": control_token
                }
            except Exception as e:
                logger.error(e)
                return False, {
                    "error": e
                    }
    
    async def get_original_url(self, Short_Url: str) -> Tuple[bool, str]:
        async with async_session() as sess:
            try:
                original_url = await sess.scalar(Select(ShortUrl.original_url).where(ShortUrl.short_code == Short_Url))
                return True, str(original_url)
            except Exception as e:
                logger.error(e)
                return False, str(e)
            
            

class actions_methods():
    async def delete_short_url(self, Short_Url: str, Control_Token: str):
        async with async_session() as session:
            ControlToken = await session.scalar(Select(ShortUrl.control_token).where(ShortUrl.short_code == Short_Url))
            if Control_Token == ControlToken:
                try:
                    await session.execute(Delete(ShortUrl).where(ShortUrl.short_code == Short_Url))
                    await session.commit()
                    return True, {"message": f"URL with Short-Code {Short_Url} deleted"}
                except Exception as e:
                    logger.error(e)
                    return False, {"error": str(e)}
            else:
                return False, {"message": "Permission denied"}
            
    async def regenerate_short_url(self, Short_Url: str, Control_Token: str):
        async with async_session() as session:
            ControlToken = await session.scalar(Select(ShortUrl.control_token).where(ShortUrl.short_code == Short_Url))
            prs = PyRandomString.RandomString()
            short_code = prs.get_string()
            if Control_Token == ControlToken:
                try:
                    await session.execute(Update(ShortUrl).where(ShortUrl.short_code == Short_Url).values(short_code=short_code))
                    await session.commit()
                    return True, {
                        "New_Short_Url": short_code
                        }
                except Exception as e:
                    logger.error(e)
                    return False, {"error": str(e)}
            else:
                return False, {"error": "Permission denied"}
        