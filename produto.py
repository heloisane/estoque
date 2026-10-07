class Produto :
    def _int__(self, codigo, nome, preco, quantidade, tipo ):
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
            