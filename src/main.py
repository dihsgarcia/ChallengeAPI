from fastapi import FastAPI
from src.routers import AuthRoute, UsuarioRoute

app = FastAPI(
    title="Challenge API",
    description="API para gerenciamento de estoques, usuários e equipamentos.",
    version="1.0.0"
)

app.include_router(AuthRoute.router, prefix="/auth", tags=["Autenticação"])
app.include_router(UsuarioRoute.router, prefix="/usuarios", tags=["Usuários"])


@app.get("/")
def read_root():
    return {"message": "Bem-vindo à Challenge API!"}
