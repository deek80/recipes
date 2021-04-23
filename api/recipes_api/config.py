from functools import cached_property
from pydantic import BaseSettings
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


class AppConfig(BaseSettings):
    environment: str = "test"
    db_url: str = "postgresql://dev:dev@db/dev"
    db_echo: bool = True

    @cached_property
    def _make_db_session(self):
        return sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=create_engine(url=self.db_url, echo=self.db_echo),
        )

    def db_session(self):
        with self._make_db_session(future=True) as session:
            yield session

    class Config:
        env_prefix = "fastapi_"


config = AppConfig()