from pydantic import BaseModel
from typing import Optional


class LocalizacaoBase(BaseModel):
    nome: str
    estoque_id: int


class LocalizacaoCreate(LocalizacaoBase):
    pass


class LocalizacaoResponse(LocalizacaoBase):
    id: int

    class Config:
        orm_mode = True
