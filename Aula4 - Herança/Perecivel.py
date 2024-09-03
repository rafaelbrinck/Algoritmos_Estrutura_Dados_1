from Categoria import Categoria
from Produto import Produto

class Perecivel(Produto):
    def __init__(self, nome, preco=1.99, cat=Categoria("Perecíveis"), temperatura=8):
        super().__init__(nome, preco, cat)
        self.temperatura = temperatura
        
    def __str__(self):
        return super().__str__() + "\nTemperatura: " + str(self.temperatura)