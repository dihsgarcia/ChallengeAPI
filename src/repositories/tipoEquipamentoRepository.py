from sqlalchemy.orm import Session
from src.models.tipoEquipamentoModel import TipoEquipamentoModel


class TipoEquipamentoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(TipoEquipamentoModel).all()

    def create(self, tipo_equipamento: TipoEquipamentoModel):
        self.db.add(tipo_equipamento)
        self.db.commit()
        self.db.refresh(tipo_equipamento)
        return tipo_equipamento