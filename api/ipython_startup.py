from sqlalchemy import select
from recipes_api.database import connection
from recipes_api.models import *
from recipes_api.test import init_db, seed_db

db = next(connection())
init_db(db)
seed_db(db)
