from Pessoa import Pessoa
from Cidade import Cidade
from Categoria import Categoria
from Produto import Produto
from Pedido import Pedido



cid01 = Cidade()
cid02 = Cidade("Porto Alegre")

cli01 = Pessoa("João")
cli02 = Pessoa("Maria", 1.82)
cli03 = Pessoa("Joana", cid = cid01)

cat01 = Categoria()
cat02 = Categoria("Alimentos")

prod01 = Produto("Coca-Cola")
prod02 = Produto("Fanta", 8.65)
prod03 = Produto("Arroz", 5.95, cat02)
prod04 = Produto("Pepsi", cat = cat01)
# prod05 = Produto("Trakinas", cat02)

ped01 = Pedido("Rua A")
ped02 = Pedido("Rua B", cli02)



ped01.addProduto(prod01)
#print(ped01.addProduto(prod02))
ped01.addProduto(prod04)
#ped01.imprimir()
#print(ped01)

from Perecivel import Perecivel
prodPer01 = Perecivel("Alface", 3.99, cat01, 10)

print(prodPer01)