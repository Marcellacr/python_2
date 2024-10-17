comissoes=[]
total = 0
#utilizador deve inserir 10 números

for i in range(0,12):
    num = float(input(f"Insira na lista de comissões [{i}]: "))
    comissoes.append(num)

#calcular total

for i in range(0,12):
    total += comissoes[i]
print("Total", total)


#modo resumido
#comissaoTotal = sum(comissoes)




