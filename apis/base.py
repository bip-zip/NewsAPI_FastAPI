from fastapi import APIRouter

from apis.version1 import route_general_pages
from apis.version1 import route_users
from apis.version1 import route_news



api_router = APIRouter()
api_router.include_router(route_general_pages.general_pages_router,prefix="",tags=["general_pages"])
api_router.include_router(route_users.router,prefix="/users",tags=["users"])
api_router.include_router(route_news.router,prefix="/news",tags=["news"])