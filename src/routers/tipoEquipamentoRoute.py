from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.config.dbContext import get_dbContext
from src.services.tipoEquipamentoService import TipoEquipamentoService
from src.repositories.tipoEquipamentoRepository import TipoEquipamentoRepository
from src.schemas.tipoEquipamentoSchema import TipoEquipamentoCreate, TipoEquipamentoResponse
from src.utils.auth import admin_role, general_role


router = APIRouter()


def get_tipo_equipamento_service(db: Session = Depends(get_dbContext)):
    repository = TipoEquipamentoRepository(db)
    return TipoEquipamentoService(repository)


@router.get("/", response_model=List[TipoEquipamentoResponse])
def get_tiposEquipamento(service: TipoEquipamentoService = Depends(get_tipo_equipamento_service),
                         user: dict = Depends(general_role)):
    return service.get_all_tipos()


@router.post("/", response_model=TipoEquipamentoResponse)
def create_tipoEquipamento(tipo_data: TipoEquipamentoCreate,
                           user: dict = Depends(admin_role),
                           service: TipoEquipamentoService = Depends(get_tipo_equipamento_service)):
    try:
        return service.create_tipo(tipo_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
