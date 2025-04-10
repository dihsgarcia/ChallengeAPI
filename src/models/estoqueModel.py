from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.config.base import Base
from src.enums.statusEnum import StatusEnum


class EstoqueModel(Base):
    __tablename__ = "estoques"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    status = Column(String(50), nullable=False,
                    default=StatusEnum.ATIVADO.value)
    criado_em = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    atualizado_em = Column(TIMESTAMP, server_default=func.now(),
                           onupdate=func.now(), nullable=False)

    localizacoes = relationship(
        "LocalizacaoModel", back_populates="estoque_rel", lazy="joined")
