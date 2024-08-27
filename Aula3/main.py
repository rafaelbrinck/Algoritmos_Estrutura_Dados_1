from Pessoa import Pessoa
from Cidade import Cidade
from Categoria import Categoria
from Produto import Produto



cid01 = Cidade()
cid02 = Cidade("Porto Alegre")

cli01 = Pessoa("João")
cli02 = Pessoa("Maria", 1.82)
cli03 = Pessoa("Joana", cid = cid01)



