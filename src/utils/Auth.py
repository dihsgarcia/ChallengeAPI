import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from src.enums.tipoUsuarioEnum import TipoUsuarioEnum
from src.config.settings import settings

# SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

SECRET_KEY = settings["SECRET_KEY"]
ALGORITHM = settings["ALGORITHM"]
ACCESS_TOKEN_EXPIRE_MINUTES = settings["ACCESS_TOKEN_EXPIRE_MINUTES"]


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")


def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=401, detail="Token inválido ou expirado")
    return payload


def admin_role(user: dict = Depends(get_current_user)):
    if user["tipoUsuario"] != TipoUsuarioEnum.ADMIN.value:
        raise HTTPException(
            status_code=403, detail="Acesso negado. Apenas um ADMIN podem realizar esta ação.")


def general_role(user: dict = Depends(get_current_user)):
    if user["tipoUsuario"] not in [TipoUsuarioEnum.ADMIN.value, TipoUsuarioEnum.OPERADOR.value]:
        raise HTTPException(
            status_code=403, detail="Acesso negado. Apenas ADMIN ou OPERADOR podem acessar esta rota.")
