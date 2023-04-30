from fastapi import FastAPI
from core.config import settings
from apis.pages.route_homepage import general_pages_router
from fastapi.staticfiles import StaticFiles

from db.session import engine   
from db.base import Base 

# including router
def include_router(app):
	app.include_router(general_pages_router)

# configuring static files
def configure_static(app):
    app.mount("/static", StaticFiles(directory="staticfiles"), name="static")

def create_tables():   
	print("create_tables") 
	Base.metadata.create_all(bind=engine)

def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	configure_static(app)
	create_tables()
	return app 




app = start_application()