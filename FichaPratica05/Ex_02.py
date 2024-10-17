# definir o menor numero

def numeroMaisPequeno(num1, num2, num3):
    menor = min(num1, num2, num3)
    return menor


#teste

resultado = numeroMaisPequeno(2, 55, 8)
print("O menor número é:", resultado)