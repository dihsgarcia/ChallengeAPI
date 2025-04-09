from pydantic import BaseModel
from datetime import datetime
from src.enums.statusEnum import StatusEnum

class EstoqueBase(BaseModel):
    nome: str
    status: StatusEnum = StatusEnum.ATIVADO


class EstoqueCreate(EstoqueBase):
    pass


class EstoqueResponse(EstoqueBase):
    id: int
    criado_em: datetime
    atualizado_em: datetime

    class Config:
        orm_mode = True