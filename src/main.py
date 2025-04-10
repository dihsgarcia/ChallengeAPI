from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from src.routers import authRoute, estoqueRoute, equipamentoRoute, tipoEquipamentoRoute, categoriaRoute
from src.config.dbContext import Base, engine
from src.models.usuarioModel import UsuarioModel
from src.models.tipoUsuarioModel import TipoUsuarioModel

app = FastAPI(
    title="Challenge API",
    description="API para gerenciamento de estoques, usuários e equipamentos.",
    version="1.0.0"
)


app.include_router(authRoute.router, prefix="/auth", tags=["Auth"])
app.include_router(estoqueRoute.router, prefix="/estoques", tags=["Estoques"])
app.include_router(equipamentoRoute.router, prefix="/equipamentos", tags=["Equipamentos"])
app.include_router(tipoEquipamentoRoute.router, prefix="/tiposEquipamento", tags=["TiposEquipamento"])
app.include_router(categoriaRoute.router, prefix="/categorias", tags=["Categorias"])

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"statusCode": exc.status_code, "message": exc.detail},
    )


@app.get("/")
def read_root():
    return {"message": "Bem-vindo à Challenge API!"}
