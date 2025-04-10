from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.config.base import Base


class TipoEquipamentoModel(Base):
    __tablename__ = "tiposequipamento"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)

    equipamentos = relationship("EquipamentoModel", back_populates="tipo_rel")