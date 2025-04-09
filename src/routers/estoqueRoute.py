from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.dbContext import get_dbContext
from src.repositories.estoqueRepository import EstoqueRepository
from src.services.estoqueService import EstoqueService
from src.schemas.estoqueSchema import EstoqueCreate, EstoqueResponse
from src.enums.statusEnum import StatusEnum

router = APIRouter()


def get_estoque_service(db: Session = Depends(get_dbContext)):
    repository = EstoqueRepository(db)
    return EstoqueService(repository)


@router.get("/", response_model=list[EstoqueResponse])
def get_estoques(service: EstoqueService = Depends(get_estoque_service)):
    return service.get_all_estoques()


@router.get("/{estoque_id}", response_model=EstoqueResponse)
def get_estoque(estoque_id: int, service: EstoqueService = Depends(get_estoque_service)):
    estoque = service.get_estoque_by_id(estoque_id)
    if not estoque:
        raise HTTPException(status_code=404, detail="Estoque não encontrado")
    return estoque


@router.post("/", response_model=EstoqueResponse)
def create_estoque(estoque: EstoqueCreate, service: EstoqueService = Depends(get_estoque_service)):
    return service.create_estoque(estoque)


@router.patch("/{estoque_id}/status", response_model=EstoqueResponse)
def alterar_status(estoque_id: int, status: StatusEnum, service: EstoqueService = Depends(get_estoque_service)):
    try:
        return service.alterar_status(estoque_id, status)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))