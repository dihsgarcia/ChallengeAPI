from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from src.routers import authRoute, usuarioRoute
from src.config.dbContext import Base, engine
from src.models.usuarioModel import UsuarioModel
from src.models.tipoUsuarioModel import TipoUsuarioModel

app = FastAPI(
    title="Challenge API",
    description="API para gerenciamento de estoques, usuários e equipamentos.",
    version="1.0.0"
)


app.include_router(authRoute.router, prefix="/auth", tags=["Auth"])
app.include_router(usuarioRoute.router, prefix="/usuarios", tags=["User"])


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"statusCode": exc.status_code, "message": exc.detail},
    )


@app.get("/")
def read_root():
    return {"message": "Bem-vindo à Challenge API!"}
