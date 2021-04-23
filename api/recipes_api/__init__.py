from fastapi import FastAPI, Depends
from sqlalchemy import select
from recipes_api import models, schemas
from recipes_api.config import config

app = FastAPI()
db = Depends(config.db_session)


@app.get("/", response_model=schemas.Recipe)
def recipe(db=db):
    result = db.execute(select(models.Recipe)).scalar()
    print("result:", result.__dict__)
    return result


@app.get("/config")
def get_config():
    return config.dict()


if config.environment == "test":
    from recipes_api.fake import init_db, seed_db

    @app.get("/seed", response_model=schemas.Recipe)
    def seed(db=db):
        init_db(db)
        seed_db(db)