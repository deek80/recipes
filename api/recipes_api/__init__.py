from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from recipes_api import models, schemas
from recipes_api.config import app_config
from recipes_api.database import connection

app = FastAPI()
db = Depends(connection)


@app.get("/", response_model=schemas.Recipe)
def recipe(db=db):
    query = select(models.Recipe, models.Instruction).join(models.Instruction)
    print("Q:", query)
    result = db.execute(query).all()
    for (r, i) in result:
        print("result:", r.__dict__, i.__dict__)
    return result


if app_config.environment == "test":
    from recipes_api.test import init_db, seed_db

    @app.get("/seed", response_model=schemas.Recipe)
    def seed(db=db):
        init_db(db)
        seed_db(db)