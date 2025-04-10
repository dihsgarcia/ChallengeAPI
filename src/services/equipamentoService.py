from sqlalchemy.exc import SQLAlchemyError
from src.repositories.equipamentoRepository import EquipamentoRepository
from src.models.equipamentoModel import EquipamentoModel
from src.schemas.equipamentoSchema import EquipamentoCreate, EquipamentoUpdate
from src.enums.statusEnum import StatusEnum


class EquipamentoService:
    def __init__(self, repository: EquipamentoRepository):
        self.repository = repository

    def get_all_equipamentos(self):
        return self.repository.get_all()

    def get_equipamento(self, equipamento_id: int):
        return self.repository.get_by_id(equipamento_id)

    def create_equipamento(self, equipamento_data: EquipamentoCreate):
        try:
            novo_equipamento = EquipamentoModel(
                nome=equipamento_data.nome,
                status=equipamento_data.status,
                estoque_id=equipamento_data.estoque_id,
                tipo_id=equipamento_data.tipo_id,
                categoria_id=equipamento_data.categoria_id
            )
            return self.repository.create(novo_equipamento)
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao criar equipamento: {str(e)}")

    def update_equipamento(self, equipamento_id: int, equipamento_data: EquipamentoUpdate):
        equipamento = self.repository.get_by_id(equipamento_id)
        if not equipamento:
            raise Exception("Equipamento não encontrado")

        for key, value in equipamento_data.dict(exclude_unset=True).items():
            setattr(equipamento, key, value)

        return self.repository.update(equipamento)

    def alterar_status(self, equipamento_id: int, status: StatusEnum):
        estoque = self.repository.get_by_id(equipamento_id)
        if not estoque:
            raise Exception("Equipamento não encontrado")
        estoque.status = status.value
        self.repository.update(estoque)
        return estoque
    
    def get_equipamentos_by_filter(self, estoque_id=None, localizacao_id=None, tipo_id=None, categoria_id=None):
        return self.repository.get_by_filter(
            estoque_id=estoque_id,
            localizacao_id=localizacao_id,
            tipo_id=tipo_id,
            categoria_id=categoria_id
        )