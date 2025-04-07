from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.DbContext import get_dbContext
from src.repositories.UsuarioRepository import UsuarioRepository
from src.services.UsuarioService import UsuarioService
from src.schemas.UsuarioSchema import UsuarioCreate
from pydantic import BaseModel

router = APIRouter()


class LoginRequest(BaseModel):
    email: str
    senha: str


def get_usuario_service(db: Session = Depends(get_dbContext)):
    repository = UsuarioRepository(db)
    return UsuarioService(repository)


@router.post("/register")
def register(usuario: UsuarioCreate, service: UsuarioService = Depends(get_usuario_service)):
    try:
        return service.register_usuario(usuario)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/login")
def login(request: LoginRequest, service: UsuarioService = Depends(get_usuario_service)):
    try:
        return service.login_usuario(request.email, request.senha)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
