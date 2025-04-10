from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.config.base import Base


class LocalizacaoModel(Base):
    __tablename__ = "localizacoes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    estoque_id = Column(Integer, ForeignKey(
        "estoques.id", name="fk_estoque"), nullable=False)

    estoque_rel = relationship("EstoqueModel", back_populates="localizacoes")
