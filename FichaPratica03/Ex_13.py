from unicodedata import numeric

vezes = int(input("Quantos números deseja inserir: "))
crescente = True
count = 1
anterior = int(input("Insira um numero: "))
while (count < vezes):
    num = int(input("Insira um número: "))
    count += 1

if (atual >= anterior): #quebra de sequencia crescente
    crescente = False

if (crescente):
    print("Crescente")
else:
print("Não crescente")

