
# api/erros.py

from fastapi import HTTPException


def proibido(mensagem="Acesso proibido."):
    return HTTPException(status_code=403, detail=mensagem)


def nao_encontrado(mensagem="Não encontrado."):
    return HTTPException(status_code=404, detail=mensagem)


def recusado(mensagem="Operação recusada."):
    return HTTPException(status_code=422, detail=mensagem)
