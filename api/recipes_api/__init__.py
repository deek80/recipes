from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from recipes_api.database import session, seed_database

app = FastAPI()


@app.get("/recipes/{slug}")
def get_recipe(slug: str, db: Session = Depends(session)):
    print(slug, db)
    return {"AAA": 123}


@app.get("/seed")
def seed():
    seed_database()
    return {"status": "success"}