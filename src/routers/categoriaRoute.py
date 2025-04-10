from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.config.dbContext import get_dbContext
from src.services.categoriaService import CategoriaService
from src.repositories.categoriaRepository import CategoriaRepository
from src.schemas.categoriaSchema import CategoriaCreate, CategoriaResponse
from src.utils.auth import admin_role, general_role


router = APIRouter()


def get_categoria_service(db: Session = Depends(get_dbContext)):
    repository = CategoriaRepository(db)
    return CategoriaService(repository)


@router.get("/", response_model=List[CategoriaResponse])
def get_categorias(service: CategoriaService = Depends(get_categoria_service),
                   user: dict = Depends(general_role)):
    return service.get_all_categorias()


@router.post("/", response_model=CategoriaResponse)
def create_categoria(categoria_data: CategoriaCreate,
                     user: dict = Depends(admin_role),
                     service: CategoriaService = Depends(get_categoria_service)):
    try:
        return service.create_categoria(categoria_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
