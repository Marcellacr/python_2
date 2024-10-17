lista = []

for i in range(1,11):
    num = int(input(f"Insira o número [{i}]: "))
    lista.append(num)
print(lista)

#valor a ser pesquisado

num_pesquisar = int(input("Qual numero deseja pesquisar: "))
if num_pesquisar in lista:
    print(f"O {num_pesquisar} EXISTE no Array.")
else:
    print(f"O {num_pesquisar} NÃO existe no Array.")