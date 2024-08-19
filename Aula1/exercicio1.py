import os
import time

ListaProdutos = ["Chocolate", "Vodka", "Miojo", "Verde"]
ListaPreco = [5.9 , 27.8, 2.5, 100]
ListaQuantidade = [20,10,30,25]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar():
    produto = input("Produto: ")
    preco = input('Preco: ')
    quantidade = int(input('Quantidade: '))
    ListaProdutos.append(produto.capitalize())
    ListaPreco.append(preco)
    ListaQuantidade.append(quantidade)
    print('\nProduto adicionado com sucesso!')
    time.sleep(2)
    

def imprimirProdutos(produto):
    for i, ind in enumerate(ListaProdutos):
        if i == produto:
            nome = ind
            for i, ind in enumerate(ListaPreco):
                if i == produto:
                    preco = ind
                    for i, ind in enumerate(ListaQuantidade):
                        if i == produto:
                            quantidade = ind
    print(f'Produto: {nome}  |  Preço: R${preco} |  Quantidade: {quantidade}')
    time.sleep(3)

def removerProdutos(produto):
    clear()
    ListaProdutos.pop(produto)
    print("Produto removido com sucesso!")
    time.sleep(2)
    clear()
    for i, ind in enumerate(ListaProdutos):
        print(f'Id: {i}  -  Produto: {ind}')
    time.sleep(2)

while True:
    clear()
    print("-"*40)
    print("1 - Adicionar Produtos")
    print("2 - Mostrar Produtos")
    print("3 - Remover Produtos")
    print("9 - Sair")
    print("-"*40)
    op = int(input("O que deseja: "))
    if op == 1:
        clear()
        adicionar()
    elif op == 2:
        clear()
        for i, ind in enumerate(ListaProdutos):
            print(f'Id: {i}  -  Produto: {ind}')
        produto = int(input("\n Qual posicao do produto que deseja mostrar: "))
        imprimirProdutos(produto)
    elif op == 3:
        clear()
        for i, ind in enumerate(ListaProdutos):
            print(f'Id: {i}  -  Produto: {ind}')
        produto = int(input("\n Qual posicao do produto que deseja remover: "))
        removerProdutos(produto)
    elif op == 9:
        break
    else:
        clear()
        print('Escolha uma opção correta!')
