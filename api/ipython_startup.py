from sqlalchemy import select
from recipes_api.models import *
from recipes_api.setup import config
from recipes_api.fake import seed_db

db = next(config.db_session())
seed_db(db)
