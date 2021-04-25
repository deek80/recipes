from fastapi import APIRouter, Depends
from sqlalchemy.sql.expression import select
from recipes_api import models, schemas
from recipes_api.setup import config

db = Depends(config.db_session)

recipes = APIRouter(prefix="/recipes")


@recipes.get("/", response_model=schemas.Recipe)
def root(db=db):
    # just testing for now -- return the first Recipe
    result = db.execute(select(models.Recipe)).scalar()
    return result


# already asking to break this into two files!
test = APIRouter(prefix="/test")


@test.get("/config")
def get_config():
    return config


@test.get("/seed", response_model=schemas.Recipe)
def seed(db=db):
    from recipes_api.fake import init_db, seed_db

    init_db(db)
    seed_db(db)