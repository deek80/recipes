from pydantic import BaseModel, BaseSettings


class Config(BaseSettings):
    environment: str = "test"
    db_url: str = "sqlite:///:memory:"
    db_echo: bool = True

    @property
    def db_config(self):
        return {
            "url": self.db_url,
            "echo": self.db_echo,
            "connect_args": (
                {"check_same_thread": False} if self.db_url.startswith("sqlite") else {}
            ),
        }

    class Config:
        env_prefix = "fastapi_"


app_config = Config()