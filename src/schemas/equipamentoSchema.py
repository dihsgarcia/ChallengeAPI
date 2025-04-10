from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from src.schemas.categoriaSchema import CategoriaResponse
from src.schemas.tipoEquipamentoSchema import TipoEquipamentoResponse
from src.schemas.estoqueSchema import EstoqueResponse
from src.enums.statusEnum import StatusEnum

class EquipamentoBase(BaseModel):
    nome: str
    status: StatusEnum = StatusEnum.ATIVADO
    estoque_id: int
    tipo_id: int
    categoria_id: int


class EquipamentoCreate(EquipamentoBase):
    pass


class EquipamentoUpdate(BaseModel):
    nome: Optional[str]
    status: Optional[str]
    estoque_id: Optional[int]
    tipo_id: Optional[int]
    categoria_id: Optional[int]


class EquipamentoResponse(EquipamentoBase):
    id: int
    criado_em: datetime
    atualizado_em: datetime
    estoque_rel: EstoqueResponse
    tipo_rel: TipoEquipamentoResponse
    categoria_rel: CategoriaResponse

    class Config:
        orm_mode = True