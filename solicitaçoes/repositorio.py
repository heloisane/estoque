from solicitacoes.pedido import Pedido

_pedidos = []

def listar():
    return [p.para_dicionario() for p in _pedidos]

def buscar(codigo):
    for pedido in _pedidos:
        if pedido.codigo == codigo:
            return pedido
    return None

def adicionar(pedido):
    _pedidos.append(pedido)

def remover(codigo):
    pedido = buscar(codigo)
    if pedido is None:
        return False
    _pedidos.remove(pedido)
    return True