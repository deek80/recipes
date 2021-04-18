from functools import cached_property
from pydantic import BaseModel, BaseSettings
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


class DbConfig(BaseModel):
    url: str = "sqlite:///:memory:"
    echo: bool = True

    def dict(self, **args):
        data = super().dict(**args)
        if self.url.startswith("sqlite"):
            data["connect_args"] = {"check_same_thread": False}
        return data

    @cached_property
    def _make_session(self):
        return sessionmaker(
            autocommit=False, autoflush=False, bind=create_engine(**self.dict())
        )

    def connection(self):
        with self._make_session(future=True) as session:
            yield session


class MainConfig(BaseSettings):
    environment: str = "test"
    db: DbConfig = DbConfig()

    class Config:
        env_prefix = "fastapi_"


config = MainConfig()