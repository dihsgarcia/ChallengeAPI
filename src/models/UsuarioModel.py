from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.config.base import Base


class UsuarioModel(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    tipo_usuario = Column(Integer, ForeignKey("tiposusuario.id", name="fk_tipo_usuario"), nullable=False)

    tipo_usuario_rel = relationship(
        "TipoUsuarioModel",
        back_populates="usuarios",
        primaryjoin="UsuarioModel.tipo_usuario == TipoUsuarioModel.id",
        lazy="joined"
    )
