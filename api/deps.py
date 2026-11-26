
# api/deps.py

from typing import Annotated
from fastapi import Header, Depends, HTTPException

from usuarios import repositorio as repo


def usuario_atual(authorization: str = Header(None)):

    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Token não informado."
        )

    token = authorization.replace("Bearer ", "")

    usuario = repo.controle_acesso().usuario_logado(token)

    if usuario is None:
        raise HTTPException(
            status_code=401,
            detail="Token inválido."
        )

    return usuario


UsuarioAtual = Annotated[
    object,
    Depends(usuario_atual)
]
