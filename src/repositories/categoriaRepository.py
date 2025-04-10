from sqlalchemy.orm import Session
from src.models.categoriaModel import CategoriaModel


class CategoriaRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(CategoriaModel).all()

    def create(self, categoria: CategoriaModel):
        self.db.add(categoria)
        self.db.commit()
        self.db.refresh(categoria)
        return categoria