#verificar maior valor PAR inserido, caso nao tenha deverá informar
numeros = []
crescente = True


for i in range(0,10):
    num = int(input(f"Insira os números [{i}]: "))
    numeros.append(num)

maiorPar= -1 #aqui tem que inicializar com qualquer numero impar

for i in range(0,10):
    if (numeros[i] % 2 == 0):

        if(maiorPar % 2 != 0):
            maiorPar = numeros[i]

        if(maiorPar%2==0 and numeros[i] > maiorPar):
            maiorPar = numeros[i]

if(maiorPar%2==0):
    print("Maior PAR: ", maiorPar)
else:
    print("não há PARES")


