from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.dbContext import get_dbContext
from src.repositories.usuarioRepository import UsuarioRepository
from src.services.usuarioService import UsuarioService
from src.schemas.usuarioSchema import UsuarioResponse
from src.utils.auth import get_current_user

router = APIRouter()


def get_usuario_service(db: Session = Depends(get_dbContext)):
    repository = UsuarioRepository(db)
    return UsuarioService(repository)


@router.get("/", response_model=list[UsuarioResponse])
def get_usuarios(service: UsuarioService = Depends(get_usuario_service), user: dict = Depends(get_current_user)):
    return service.get_all_usuarios()
