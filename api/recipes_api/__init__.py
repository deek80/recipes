from fastapi import FastAPI
from sqlalchemy import select
from recipes_api.dependencies import db
from recipes_api.database import init_db, seed_db, Recipe
from recipes_api.schemas import RecipeSchema

app = FastAPI()


@app.get("/", response_model=RecipeSchema)
def get(db=db):
    return db.execute(select(Recipe)).scalar_one()


@app.get("/seed")
def seed(db=db):
    init_db(db)
    seed_db(db)
    return {"status": "success"}