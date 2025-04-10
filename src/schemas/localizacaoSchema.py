from pydantic import BaseModel
from typing import Optional


class LocalizacaoBase(BaseModel):
    nome: str


class LocalizacaoCreate(LocalizacaoBase):
    pass


class LocalizacaoResponse(LocalizacaoBase):
    id: int
    estoque_id: int
    
    class Config:
        orm_mode = True
