from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "sqlite:///:memory:", connect_args={"check_same_thread": False}, echo=True
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)