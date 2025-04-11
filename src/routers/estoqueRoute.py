from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.config.dbContext import get_dbContext
from src.repositories.estoqueRepository import EstoqueRepository
from src.services.estoqueService import EstoqueService
from src.schemas.estoqueSchema import EstoqueCreate, EstoqueResponse
from src.schemas.localizacaoSchema import LocalizacaoResponse
from src.enums.statusEnum import StatusEnum
from src.utils.auth import admin_role, general_role

router = APIRouter()


def get_estoque_service(db: Session = Depends(get_dbContext)):
    repository = EstoqueRepository(db)
    return EstoqueService(repository)


@router.get("/", response_model=list[EstoqueResponse], tags=["Estoques"])
def get_estoques(service: EstoqueService = Depends(get_estoque_service),
                 user: dict = Depends(general_role)):
    return service.get_all_estoques()


@router.get("/{estoque_id}", response_model=EstoqueResponse, tags=["Estoques"])
def get_estoque(estoque_id: int,
                service: EstoqueService = Depends(get_estoque_service),
                user: dict = Depends(general_role)):
    estoque = service.get_estoque_by_id(estoque_id)
    if not estoque:
        raise HTTPException(status_code=404, detail="Estoque não encontrado")
    return estoque


@router.get("/{estoque_id}/localizacoes", response_model=List[LocalizacaoResponse], tags=["Estoques"])
def get_localizacoes_by_estoque_id(estoque_id: int,
                                   service: EstoqueService = Depends(
                                       get_estoque_service),
                                   user: dict = Depends(general_role)):
    try:
        return service.get_localizacoes_by_estoque_id(estoque_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=EstoqueResponse, tags=["Estoques"])
def create_estoque(
        estoque_data: EstoqueCreate,
        service: EstoqueService = Depends(get_estoque_service),
        user: dict = Depends(admin_role)):
    try:
        return service.create_estoque(estoque_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.patch("/", response_model=EstoqueResponse, tags=["Estoques"])
def alterar_status(estoque_id: int,
                   status: StatusEnum,
                   service: EstoqueService = Depends(get_estoque_service),
                   user: dict = Depends(admin_role)):
    try:
        return service.alterar_status(estoque_id, status)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
