from fastapi import APIRouter
from pydantic import BaseModel
from api.deps import UsuarioAtual
from solicitacoes import servico

router = APIRouter(prefix="/solicitacoes", tags=["Solicitações"])


class NovoPedido(BaseModel):
    codigo: str
    produtos: list


@router.get("")
def listar(quem: UsuarioAtual):
    return servico.listar(quem)


@router.post("")
def abrir(dados: NovoPedido, quem: UsuarioAtual):
    return servico.abrir(quem, dados.codigo, dados.produtos)


@router.post("/{codigo}/aprovar")
def aprovar(codigo: str, quem: UsuarioAtual):
    return servico.aprovar(quem, codigo)


@router.post("/{codigo}/cancelar")
def cancelar(codigo: str, quem: UsuarioAtual):
    return servico.cancelar(quem, codigo)