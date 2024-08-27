from Produto import Produto
from Pessoa import Pessoa

class Pedido:
    def __init__(self, end, pessoa = Pessoa(nome = "Cliente não informado")):
        self.id = None
        self.endereco = end
        self.cliente = pessoa
        self.__produtos = []
    
    def addProduto(self, prod):  
        if prod is not None:
            self.__produtos.append(prod)
        total = 0.0
        for produto in self.__produtos:
            total += produto.preco
        return total
    
    def __str__(self):
        txt = "Produtos: \n"
        for produto in self.__produtos:
            txt += "------------------------"
            txt += "\nNome: "+ produto.nome
            txt += "\nPreço: "+ str(produto.preco)
            txt += "\nCategoria: "+ produto.categoria.nome
        return txt
    
    def imprimir(self):
        print(self)