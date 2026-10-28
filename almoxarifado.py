class Almoxarifado:
    def __init__(self, unidade):
        self.unidade = unidade
        self.produtos = []


    # Adiciona um produto à lista
    def adicionar(self, produto):
        self.produtos.append(produto)


    # Conta os produtos que estão em falta
    def contar_em_falta(self):
        total = 0
        for p in self.produtos:
            if p.situacao() == "Em falta":
                total = total + 1
        return total


    # Busca um produto pelo código
    def buscar(self, codigo):
        for p in self.produtos:
            if p.codigo == codigo:
                return p
        return None


    # Registra a entrada de um produto
    def entrada(self, codigo, qtd):
        p = self.buscar(codigo)


        if p is None:
            return False


        p.entrada(qtd)
        return True


    # Registra a saída de um produto
    def saida(self, codigo, qtd):
        p = self.buscar(codigo)


        if p is None:
            return False


        return p.saida(qtd)


    # Lista os dados de todos os produtos
    def listar(self):
        lista = []


        for p in self.produtos:
            lista.append(p.listar_produtos())


        return lista


    # Monta a lista de produtos que precisam de reposição
    def solicitacao_compra(self):
        lista = []


        for p in self.produtos:
            if p.situacao() != "OK":
                lista.append({
                    "codigo": p.codigo,
                    "nome": p.nome,
                    "situacao": p.situacao()
                })


        return lista


    # Calcula o valor total do estoque
    def valor_estoque(self):
        total = 0


        for p in self.produtos:
            total = total + (p.quantidade * p.preco)


        return total


    # Devolve os dados do almoxarifado em um dicionário
    def para_dicionario(self):
        return {
            "unidade": self.unidade,
            "total_produtos": len(self.produtos),
            "produtos": self.listar()
        }