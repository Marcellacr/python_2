#programa para desenhar um quadrado com um caracter, no qual o usuario da o numero de linhas e colunas

def desenharQuadrado (caracter, numLinhas, numColunas):

    print(caracter * numColunas)

    for i in range(numLinhas - 2):
        print(caracter + " " * (numColunas -2) + caracter)

    # for i in range(numColunas):
    #     print(caracter * numColunas)

    print(caracter * numColunas)


caracter = input("Introduza um caracter: ")
numLinhas = int(input("Introduza o número de linhas: "))
numColunas = int(input("Introduza o número de colunas: "))

desenharQuadrado(caracter, numLinhas, numColunas)
