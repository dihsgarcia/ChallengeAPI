from sqlalchemy.exc import SQLAlchemyError
from src.repositories.tipoEquipamentoRepository import TipoEquipamentoRepository
from src.models.tipoEquipamentoModel import TipoEquipamentoModel
from src.schemas.tipoEquipamentoSchema import TipoEquipamentoCreate


class TipoEquipamentoService:
    def __init__(self, repository: TipoEquipamentoRepository):
        self.repository = repository

    def get_all_tipos(self):
        return self.repository.get_all()

    def create_tipo(self, tipo_data: TipoEquipamentoCreate):
        try:
            novo_tipo = TipoEquipamentoModel(nome=tipo_data.nome)
            return self.repository.create(novo_tipo)
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao criar tipo de equipamento: {str(e)}")