from pydantic import BaseModel
from datetime import datetime
from src.schemas.categoriaSchema import CategoriaResponse
from src.schemas.tipoEquipamentoSchema import TipoEquipamentoResponse
from src.schemas.estoqueSchema import EstoqueResponse


class EquipamentoBase(BaseModel):
    nome: str
    status: str
    estoque_id: int
    tipo_id: int
    categoria_id: int


class EquipamentoCreate(EquipamentoBase):
    pass


class EquipamentoResponse(EquipamentoBase):
    id: int
    criado_em: datetime
    atualizado_em: datetime
    estoque_rel: EstoqueResponse
    tipo_rel: TipoEquipamentoResponse
    categoria_rel: CategoriaResponse

    class Config:
        orm_mode = True