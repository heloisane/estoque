from produto import Produto

p1 = Produto()
p1.nome = "banana"
p1.quantidade = 12
preco = 9.50
p1.codigo = 1234
tipo = "fruta"

p2 = Produto()
p2.nome = "maçã"
p2.quantidade = 24
p2.preco = 10.50
p2.codigo = 1235
tipo = "fruta"

p3 = Produto()
p3.nome = "laranja"
p3.quantidade = 36
p3.preco = 12.50
p3.codigo = 1236
tipo = "fruta"

print(p1.listar_produtos)
print(p2.listar_produtos)
print(p3.listar_produtos)


