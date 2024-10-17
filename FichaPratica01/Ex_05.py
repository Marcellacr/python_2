#média aritmética de um conjunto de 3 valores

print("Introduza o valor 1: ")
valor1 = float(input())

print("Introduza o valor 2: ")
valor2 = float(input())

print("Introduza o valor 3: ")
valor3 = float(input())

media = (valor1 + valor2 + valor3) / 3
print("A média aritimética é: ", media)

media_ponderada = valor1 * 0.20 + valor2 * 0.20 + valor3 * 0.50
print("A média ponderada é: ", media_ponderada)
