from sqlalchemy.exc import SQLAlchemyError
from src.repositories.categoriaRepository import CategoriaRepository
from src.models.categoriaModel import CategoriaModel
from src.schemas.categoriaSchema import CategoriaCreate


class CategoriaService:
    def __init__(self, repository: CategoriaRepository):
        self.repository = repository

    def get_all_categorias(self):
        return self.repository.get_all()

    def create_categoria(self, categoria_data: CategoriaCreate):
        try:
            nova_categoria = CategoriaModel(nome=categoria_data.nome)
            return self.repository.create(nova_categoria)
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao criar categoria: {str(e)}")