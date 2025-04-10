from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.config.base import Base


class EquipamentoModel(Base):
    __tablename__ = "equipamentos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    status = Column(String(50), nullable=False)
    criado_em = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    atualizado_em = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)

    estoque_id = Column(Integer, ForeignKey("estoques.id", name="fk_equipamento_estoque"), nullable=False)
    tipo_id = Column(Integer, ForeignKey("tiposequipamento.id", name="fk_equipamento_tipo"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id", name="fk_equipamento_categoria"), nullable=False)

    estoque_rel = relationship("EstoqueModel", back_populates="equipamentos")
    tipo_rel = relationship("TipoEquipamentoModel", back_populates="equipamentos")
    categoria_rel = relationship("CategoriaModel", back_populates="equipamentos")