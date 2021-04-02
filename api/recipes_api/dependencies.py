from fastapi import Depends
from recipes_api.database import Session


def _get_session():
    with Session(future=True) as session:
        yield session


db = Depends(_get_session)