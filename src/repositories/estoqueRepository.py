from sqlalchemy.orm import Session
from src.models.estoqueModel import EstoqueModel


class EstoqueRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(EstoqueModel).all()

    def get_by_id(self, estoque_id: int):
        return self.db.query(EstoqueModel).filter(EstoqueModel.id == estoque_id).first()

    def create(self, estoque: EstoqueModel):
        self.db.add(estoque)
        self.db.commit()
        self.db.refresh(estoque)
        return estoque
    
    def update(self, estoque: EstoqueModel):
        self.db.commit()
        self.db.refresh(estoque)
        return estoque

    def delete(self, estoque_id: int):
        estoque = self.get_by_id(estoque_id)
        if estoque:
            self.db.delete(estoque)
            self.db.commit()