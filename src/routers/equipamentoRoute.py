from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from src.config.dbContext import get_dbContext
from src.services.equipamentoService import EquipamentoService
from src.repositories.equipamentoRepository import EquipamentoRepository
from src.schemas.equipamentoSchema import EquipamentoCreate, EquipamentoUpdate, EquipamentoResponse
from src.enums.statusEnum import StatusEnum
from src.utils.auth import admin_role, general_role

router = APIRouter()


def get_equipamento_service(db: Session = Depends(get_dbContext)):
    repository = EquipamentoRepository(db)
    return EquipamentoService(repository)


@router.get("/", response_model=List[EquipamentoResponse], tags=["Equipamentos"])
def get_equipamentos(service: EquipamentoService = Depends(get_equipamento_service),
                     user: dict = Depends(general_role)):
    return service.get_all_equipamentos()


@router.get("/{equipamento_id}", response_model=EquipamentoResponse, tags=["Equipamentos"])
def get_equipamento(equipamento_id: int,
                    service: EquipamentoService = Depends(
                        get_equipamento_service),
                    user: dict = Depends(general_role)):
    equipamento = service.get_equipamento(equipamento_id)
    if not equipamento:
        raise HTTPException(
            status_code=404, detail="Equipamento não encontrado")
    return equipamento


@router.get("/search/", response_model=List[EquipamentoResponse], tags=["Equipamentos"])
def get_equipamentos_by_filter(
    estoque_id: Optional[int] = Query(None),
    localizacao_id: Optional[int] = Query(None),
    tipo_id: Optional[int] = Query(None),
    categoria_id: Optional[int] = Query(None),
    user: dict = Depends(general_role),
    service: EquipamentoService = Depends(get_equipamento_service)
):
    try:
        return service.get_equipamentos_by_filter(
            estoque_id=estoque_id,
            localizacao_id=localizacao_id,
            tipo_id=tipo_id,
            categoria_id=categoria_id
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/", response_model=EquipamentoResponse, tags=["Equipamentos"])
def create_equipamento(equipamento_data: EquipamentoCreate,
                       user: dict = Depends(admin_role),
                       service: EquipamentoService = Depends(get_equipamento_service)):
    try:
        return service.create_equipamento(equipamento_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{equipamento_id}", response_model=EquipamentoResponse, tags=["Equipamentos"])
def update_equipamento(equipamento_id: int,
                       equipamento_data: EquipamentoUpdate,
                       user: dict = Depends(admin_role),
                       service: EquipamentoService = Depends(get_equipamento_service)):
    try:
        return service.update_equipamento(equipamento_id, equipamento_data)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.patch("/", response_model=EquipamentoResponse, tags=["Equipamentos"])
def alterar_status(equipamento_id: int,
                   status: StatusEnum,
                   ser: dict = Depends(admin_role),
                   service: EquipamentoService = Depends(get_equipamento_service)):
    try:
        return service.alterar_status(equipamento_id, status)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
