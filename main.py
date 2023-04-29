from fastapi import FastAPI
from models.users import *
from tortoise.contrib.fastapi import register_tortoise
app = FastAPI()

@app.get("/")
async def index():
    return {"Good": "Feelings"}


register_tortoise(
    app,
    db_url='sqlite://database.sqlite3',
    modules= {'models':["models"]},
    generate_schemas=True,
    add_exception_handlers=True
)

