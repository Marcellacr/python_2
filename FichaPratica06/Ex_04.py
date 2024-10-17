#ler lista tamanho 10, e menor elemento
numeros=[]


for i in range(0,10):
    num = int(input(f"Insira os números [{i}]: "))
    numeros.append(num)

print(numeros)

menor = min(numeros)

print(menor)