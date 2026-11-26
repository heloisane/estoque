from fastapi import FastAPI
from produtos.rotas import router as produtos_router
from solicitacoes.rotas import router as solicitacoes_router

app = FastAPI(
    title="API Almoxarifado",
    description="Sistema de controle de estoque",
    version="1.0.0"
)

app.include_router(produtos_router)
app.include_router(solicitacoes_router)


@app.get("/saude")
def saude():
    return {"status": "ok"}
    