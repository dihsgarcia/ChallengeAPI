from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.base import Base

from src.models.tipoUsuarioModel import TipoUsuarioModel
from src.models.usuarioModel import UsuarioModel
from src.models.estoqueModel import EstoqueModel
from src.models.localizacaoModel import LocalizacaoModel
from src.models.tipoEquipamentoModel import TipoEquipamentoModel
from src.models.categoriaModel import CategoriaModel
from src.models.equipamentoModel import EquipamentoModel
from src.models.historicoMovimentacaoModel import HistoricoMovimentacaoModel

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def get_dbContext():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
