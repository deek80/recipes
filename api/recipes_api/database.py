from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from recipes_api.config import app_config


_make_session = sessionmaker(
    autocommit=False, autoflush=False, bind=create_engine(**app_config.db_config)
)


def connection():
    with _make_session(future=True) as session:
        yield session