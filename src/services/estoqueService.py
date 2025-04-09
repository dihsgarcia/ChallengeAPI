from sqlalchemy.exc import SQLAlchemyError
from src.repositories.estoqueRepository import EstoqueRepository
from src.schemas.estoqueSchema import EstoqueCreate
from src.models.estoqueModel import EstoqueModel
from src.enums.statusEnum import StatusEnum


class EstoqueService:
    def __init__(self, repository: EstoqueRepository):
        self.repository = repository

    def get_all_estoques(self):
        return self.repository.get_all()

    def get_estoque_by_id(self, estoque_id: int):
        return self.repository.get_by_id(estoque_id)

    def create_estoque(self, estoque_data: EstoqueCreate):
        try:
            status_lower = estoque_data.status.lower()

            if status_lower not in StatusEnum.__members__.values():
                raise ValueError(
                    "Os Status possiveis são: ativado ou desativado.")

            novo_estoque = EstoqueModel(
                nome=estoque_data.nome,
                status=estoque_data.status
            )
            return self.repository.create(novo_estoque)
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao criar estoque: {str(e)}")

    def alterar_status(self, estoque_id: int, status: StatusEnum):
        estoque = self.repository.get_by_id(estoque_id)
        if not estoque:
            raise Exception("Estoque não encontrado")
        estoque.status = status.value
        self.repository.update(estoque)
        return estoque
