from fastapi import FastAPI, Depends
from sqlalchemy import select
from recipes_api import models, schemas
from recipes_api.config import config

app = FastAPI()
db = Depends(config.db.connection)


@app.get("/", response_model=schemas.Recipe)
def recipe(db=db):
    query = select(models.Recipe, models.Instruction).join(models.Instruction)
    print("Q:", query)
    result = db.execute(query).all()
    for (r, i) in result:
        print("result:", r.__dict__, i.__dict__)
    return result


if config.environment == "test":
    from recipes_api.fake import init_db, seed_db

    @app.get("/seed", response_model=schemas.Recipe)
    def seed(db=db):
        init_db(db)
        seed_db(db)