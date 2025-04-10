from sqlalchemy.orm import Session
from src.models.equipamentoModel import EquipamentoModel


class EquipamentoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(EquipamentoModel).all()

    def get_by_id(self, equipamento_id: int):
        return self.db.query(EquipamentoModel).filter(EquipamentoModel.id == equipamento_id).first()

    def create(self, equipamento: EquipamentoModel):
        self.db.add(equipamento)
        self.db.commit()
        self.db.refresh(equipamento)
        return equipamento

    def update(self, equipamento: EquipamentoModel):
        self.db.commit()
        self.db.refresh(equipamento)
        return equipamento