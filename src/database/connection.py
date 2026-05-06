from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_PATH = "sqlite:///src/database.db"

engine = create_engine(DB_PATH, connect_args={"check_same_thread": False}, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():

    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()