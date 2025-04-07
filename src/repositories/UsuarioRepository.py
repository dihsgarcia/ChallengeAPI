from sqlalchemy.orm import Session
from src.models.UsuarioModel import UsuarioModel


class UsuarioRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(UsuarioModel).all()

    def get_by_id(self, usuario_id: int):
        return self.db.query(UsuarioModel).filter(UsuarioModel.id == usuario_id).first()

    def get_by_email(self, email: str):
        return self.db.query(UsuarioModel).filter(UsuarioModel.email == email).first()

    def create(self, usuario: UsuarioModel):
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def delete(self, usuario_id: int):
        usuario = self.get_by_id(usuario_id)
        if usuario:
            self.db.delete(usuario)
            self.db.commit()
