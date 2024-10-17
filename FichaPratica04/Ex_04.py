num = int(input("Indique um numero: "))

for i in range(2,num):
    if(num % i == 0):
        primo=False

if primo:
    print("Primo")
else:
    print("Não é primo")