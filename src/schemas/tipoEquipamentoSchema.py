from pydantic import BaseModel


class TipoEquipamentoBase(BaseModel):
    nome: str


class TipoEquipamentoCreate(TipoEquipamentoBase):
    pass


class TipoEquipamentoResponse(TipoEquipamentoBase):
    id: int

    class Config:
        orm_mode = True
