from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
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
    
    def get_by_filter(self, estoque_id=None, localizacao_id=None, tipo_id=None, categoria_id=None):
        query = self.db.query(EquipamentoModel).options(
            joinedload(EquipamentoModel.estoque_rel),
            joinedload(EquipamentoModel.tipo_rel),
            joinedload(EquipamentoModel.categoria_rel)
        )

        if estoque_id:
            query = query.filter(EquipamentoModel.estoque_id == estoque_id)
        if localizacao_id:
            query = query.filter(EquipamentoModel.historico_movimentacoes.any(localizacao_id=localizacao_id))
        if tipo_id:
            query = query.filter(EquipamentoModel.tipo_id == tipo_id)
        if categoria_id:
            query = query.filter(EquipamentoModel.categoria_id == categoria_id)

        return query.all()