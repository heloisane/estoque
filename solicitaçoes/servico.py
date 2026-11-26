from solicitacoes import repositorio as repo
from solicitacoes.pedido import Pedido
from api.erros import nao_encontrado, proibido


def listar(quem):
    if not quem.pode("ver_produtos"):
        raise proibido()
    return repo.listar()


def abrir(quem, codigo, produtos):
    if not quem.pode("abrir_pedido"):
        raise proibido()

    pedido = Pedido(codigo, quem.matricula, produtos)
    repo.adicionar(pedido)

    return pedido.para_dicionario()


def aprovar(quem, codigo):
    if not quem.pode("aprovar_pedido"):
        raise proibido()

    pedido = repo.buscar(codigo)

    if pedido is None:
        raise nao_encontrado("Pedido não encontrado.")

    pedido.aprovar()
    return pedido.para_dicionario()


def cancelar(quem, codigo):
    if not quem.pode("cancelar_pedido"):
        raise proibido()

    pedido = repo.buscar(codigo)

    if pedido is None:
        raise nao_encontrado("Pedido não encontrado.")

    pedido.cancelar()
    return pedido.para_dicionario()