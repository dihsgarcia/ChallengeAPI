from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.config.dbContext import Base


class TipoUsuarioModel(Base):
    __tablename__ = "tiposusuario"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(100), nullable=False)

    usuarios = relationship(
        "UsuarioModel",
        back_populates="tipo_usuario_rel",
        lazy="joined"
    )
