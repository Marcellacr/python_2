#imprimir uma tabuada

def imprimirTabuada(num):

    for i in range(1,11):
        resultadoTabuada = num * i
        print(f"{num} x {i} = {resultadoTabuada}")


num = int(input("Digite um número positivo: "))

imprimirTabuada(num)

