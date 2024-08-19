# Método que tem retorno e não recebe parametro
def getPI():
    return 3.14


# Método que não tem retorno e não recebe parâmetro
def imprimirPI():
    print( 3.14 )


# Método que tem retorno e recebe parâmetro
def calcularAreaCirculo(raio):
    area = getPI() * ( raio * raio )
    return area


# Método que não tem retorno e recebe parâmetro
def imprimirAreaCirculo(raio):
    print(calcularAreaCirculo(raio))