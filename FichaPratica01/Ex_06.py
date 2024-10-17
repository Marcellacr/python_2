#programa que leia dois valores e armazene nas variais valor1 e valor2.
#Permute (troque) o valor das variaveis e apresente o resultado
print("Introduza o valor 1: ")
valor1 = int(input())

print("Introduza o valor 2: ")
valor2 = int(input())

#valor1, valor2 = valor2, valor1

valor1 ^= valor2
valor2 ^= valor1
valor1 ^= valor2

print("O valor 1 é: ", valor1)
print("O valor 2 é: ", valor2)