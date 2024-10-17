def mostrar_menu():
    print("\nSelecione uma opção:")
    print("1. Criar")
    print("2. Atualizar")
    print("3. Eliminar")
    print("4. Sair")

def menu():
    while True:
        mostrar_menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            print("Você escolheu a opção: Criar")
        elif opcao == "2":
            print("Você escolheu a opção: Atualizar")
        elif opcao == "3":
            print("Você escolheu a opção: Eliminar")
        elif opcao == "4":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

# Executa o menu
menu()
