
# produtos/repositorio.py

from produtos.almoxarifado import Almoxarifado
from produtos.produto import Produto

# Criando o almoxarifado
_almoxarifado = Almoxarifado("Lages")

# Cadastrando os produtos
_almoxarifado.adicionar(
    Produto("P001", "Luva de vaqueta", 18.50, 12, "EPI")
)

_almoxarifado.adicionar(
    Produto("P002", "Óculos de proteção", 12.25, 3, "EPI")
)

_almoxarifado.adicionar(
    Produto("P003", "Broca 8 mm", 9.75, 0, "Ferramenta")
)

_almoxarifado.adicionar(
    Produto("P004", "Paquímetro 150 mm", 85.00, 8, "Instrumento")
)


# Devolve o almoxarifado
def almoxarifado():
    return _almoxarifado


# Busca um produto pelo código
def buscar(codigo):
    return _almoxarifado.buscar(codigo)
