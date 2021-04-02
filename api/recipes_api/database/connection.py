from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "sqlite:///:memory:"
engine = create_engine(db_url, connect_args={"check_same_thread": False})
make_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def session():
    db = make_session()
    try:
        yield db
    finally:
        db.close()
