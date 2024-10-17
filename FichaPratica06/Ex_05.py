#o programa para com um numero negativo

numeros = []
num = 1
soma = 0

while (num >= 0):
    num=int(input("Insira um numero (negativo para parar): "))
    if (num > 0):
        numeros.append(num)

for i in range(0, len(numeros)): # se usar: (for i in numeros:) é a mesma coisa
    soma += numeros[i]  # se usar (soma += i) é a mesma coisa dessa linha

media = soma/len(numeros)
print("Media: ", media)