from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.DbContext import get_dbContext
from src.repositories.UsuarioRepository import UsuarioRepository
from src.services.UsuarioService import UsuarioService
from src.schemas.UsuarioSchema import UsuarioCreate, UsuarioResponse
from src.utils.Auth import get_current_user

router = APIRouter()

def get_usuario_service(db: Session = Depends(get_dbContext)):
    repository = UsuarioRepository(db)
    return UsuarioService(repository)


@router.get("/", response_model=list[UsuarioResponse])
def get_usuarios(db: Session = Depends(get_usuario_service), user: dict = Depends(get_current_user)):
    service = UsuarioService(db)
    return service.get_all_usuarios()


# @router.get("/", response_model=list[UsuarioResponse])
# def getUsuarios(db: Session = Depends(getUsuarioService)):
#     service = UsuarioService(db)
#     return service.getAllUsuarios()

# @router.get("/{usuario_id}", response_model=UsuarioResponse)
# def getUsuario(usuario_id: int, db: Session = Depends(getUsuarioService)):
#     service = UsuarioService(db)
#     try:
#         return service.getUsuarioById(usuario_id)
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))

# @router.post("/", response_model=UsuarioResponse)
# def createUsuario(usuario: UsuarioCreate, db: Session = Depends(getUsuarioService)):
#     service = UsuarioService(db)
#     return service.createUsuario(usuario)