from itertools import count

num = None
count = 0
somatorio = 0
while (num != 1):
    num = int(input("Insira um numero (-1 para parar): "))
    count += 1
    somatorio += num

    media = somatorio / count
    print("Média: ", media)
