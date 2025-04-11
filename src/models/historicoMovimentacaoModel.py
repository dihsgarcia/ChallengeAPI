from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.config.base import Base


class HistoricoMovimentacaoModel(Base):
    __tablename__ = "historicomovimentacao"

    id = Column(Integer, primary_key=True, index=True)
    equipamento_id = Column(Integer, ForeignKey("equipamentos.id", name="fk_historico_equipamento"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", name="fk_historico_usuario"), nullable=False)
    tipo_movimentacao = Column(String(50), nullable=False)
    data_hora = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    localizacao_id = Column(Integer, ForeignKey("localizacoes.id", name="fk_historico_localizacao"), nullable=False)

    equipamento_rel = relationship("EquipamentoModel", back_populates="historico_movimentacoes")
    usuario_rel = relationship("UsuarioModel", back_populates="historico_movimentacoes")
    localizacao_rel = relationship("LocalizacaoModel", back_populates="historico_movimentacoes")