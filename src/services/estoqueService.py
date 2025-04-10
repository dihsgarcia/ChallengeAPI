from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload
from typing import List
from src.repositories.estoqueRepository import EstoqueRepository
from src.schemas.estoqueSchema import EstoqueCreate
from src.schemas.localizacaoSchema import LocalizacaoResponse
from src.models.estoqueModel import EstoqueModel
from src.models.localizacaoModel import LocalizacaoModel
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
            self.repository.create(novo_estoque)

            for localizacao_data in estoque_data.localizacoes:
                nova_localizacao = LocalizacaoModel(
                    nome=localizacao_data.nome,
                    estoque_id=novo_estoque.id
                )
                self.repository.db.add(nova_localizacao)

            self.repository.db.commit()
   
            return novo_estoque

        except SQLAlchemyError as e:
            self.repository.db.rollback()
            raise Exception(f"Erro ao criar estoque: {str(e)}")

    def alterar_status(self, estoque_id: int, status: StatusEnum):
        estoque = self.repository.get_by_id(estoque_id)
        if not estoque:
            raise Exception("Estoque não encontrado")
        estoque.status = status.value
        self.repository.update(estoque)
        return estoque
    
    def get_localizacoes_by_estoque_id(self, estoque_id: int) -> List[LocalizacaoResponse]:
        estoque = self.repository.get_by_id(estoque_id)
        if not estoque:
            raise Exception("Estoque não encontrado")

        return estoque.localizacoes
