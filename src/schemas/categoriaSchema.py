from pydantic import BaseModel


class CategoriaBase(BaseModel):
    nome: str


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaResponse(CategoriaBase):
    id: int

    class Config:
        orm_mode = True