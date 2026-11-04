class Produto :
    def __init__(self, codigo = None, nome = None, preco = 0.0, quantidade = 0, tipo = None):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.tipo = tipo

    def listar_produtos(self):
       return{
           "codigo": self.codigo,
           "nome": self.nome,
           "preco": self.preco,
           "quantidade": self.quantidade,
           "tipo": self.tipo,
           "situação": self.situacao(),
        }
    
    def situacao(self):
        if self.quantidade == 0:
            return "em falta"
        elif self.quantidade <= 1:
            return "repor estoque"
        else:
            return "ok"

    def entrada (self, qtd):
        self.quantidade = (self.quantidade + qtd)

    def saida (self , qtd):
        if qtd <= self.quantidade:
            self.quantidade = (self.quantidade - qtd)
            return True
        return False    
         
