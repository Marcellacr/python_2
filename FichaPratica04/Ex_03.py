valor = int(input('Digite um número de 0 a 100: '))

chute = int(input("Qual o seu palpite? "))

count = 1
if(chute == valor):
    print("Você acertou!")

while(chute > valor):
    print("Seu palpite foi superior ao valor")
    count+= 1
while(chute < valor):
    print("Seu palpite foi inferior ao valor")
    count += 1

print(count)