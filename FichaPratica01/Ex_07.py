#um programa que peça 3 preços, apresente valor
# a pagar com desconto de 10% sobre o valor total

print("Introduza o valor do produto 1: ")
produto1 = float(input())

print("Introduza o valor do produto 2: ")
produto2 = float(input())

print("Introduza o valor do produto 3: ")
produto3 = float(input())

totalProdutos = produto1 + produto2 + produto3

totalCompras = totalProdutos * 0.1
print("O valor total da compra é: ", totalCompras)