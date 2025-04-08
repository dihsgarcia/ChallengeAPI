from pydantic import BaseModel

class TipoUsuarioBase(BaseModel):
    descricao: str

class TipoUsuarioCreate(TipoUsuarioBase):
    pass

class TipoUsuarioResponse(TipoUsuarioBase):
    id: int

    class Config:
        orm_mode = True