from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.base import Base

from src.models.estoqueModel import EstoqueModel
from src.models.localizacaoModel import LocalizacaoModel


DATABASE_URL = "postgresql://postgres:admin@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def get_dbContext():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
