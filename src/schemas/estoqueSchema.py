from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import List, Optional
from src.enums.statusEnum import StatusEnum
from src.schemas.localizacaoSchema import LocalizacaoCreate
from src.schemas.localizacaoSchema import LocalizacaoResponse


class EstoqueBase(BaseModel):
    nome: str
    status: StatusEnum = StatusEnum.ATIVADO

    @field_validator("status", mode="before")
    @classmethod
    def normalize_status(cls, value):
        if isinstance(value, str):
            return value.lower()
        return value


class EstoqueCreate(EstoqueBase):
    localizacoes: Optional[List[LocalizacaoCreate]] = []


class EstoqueResponse(EstoqueBase):
    id: int
    criado_em: datetime
    atualizado_em: datetime
    localizacoes: List[LocalizacaoResponse]

    class Config:
        orm_mode = True
