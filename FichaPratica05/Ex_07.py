from FichaPratica05.Ex_06 import numeroPositivo, primo, parImpar

numero = int(input("Insira um número: "))
opcao = 10


while (opcao != 7):
    print("\n\n**** Programa de Anaçise de um Número: ", numero, "******")
    print("1. Par ou Impar")
    print("2. Positivo ou Negativo")
    print("3. Primo ou Não Primo")
    print("4. Triangular ou Não Triangular")
    print("5. Par ou Impar")
    print("6. Trocar de Número")
    print("7. Sair")
    print("****************************")

    opcao = int(input("Insira a opação: "))

    match (opcao):
        case 1:
            if(parImpar(numero)):
                print("Par")
            else:
                print("Impar")
            break
        case 2:
            if(numeroPositivo(numero)):
                print("Positivo")
            else:
                print("Negativo")
            break

        case 3:
            if(primo(numero)):
                print("Primo")
            else:
                print("Não Primo")
            break

        case 4:
