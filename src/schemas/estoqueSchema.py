from pydantic import BaseModel, field_validator
from datetime import datetime
from src.enums.statusEnum import StatusEnum


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
    pass


class EstoqueResponse(EstoqueBase):
    id: int
    criado_em: datetime
    atualizado_em: datetime

    class Config:
        orm_mode = True
