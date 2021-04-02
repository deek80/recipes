from .connection import engine
from .models import Model


def seed_database():
    Model.metadata.create_all(bind=engine)
