def calculadora():
    while True:
        # Solicita ao usuário os valores e a operação desejada
        try:
            valor1 = int(input("Digite o primeiro valor: "))
            valor2 = int(input("Digite o segundo valor: "))
            operacao = input("Digite a operação desejada (+, -, *, /): ")
        
            # Verifica e executa a operação
            if operacao == '+':
                resultado = valor1 + valor2
            elif operacao == '-':
                resultado = valor1 - valor2
            elif operacao == '*':
                resultado = valor1 * valor2
            elif operacao == '/':
                if valor2 != 0:
                    resultado = valor1 / valor2
                else:
                    print("Erro: Divisão por zero não é permitida.")
                    continue
            else:
                print("Operação inválida. Por favor, escolha entre +, -, * ou /.")
                continue

            # Exibe o resultado
            print(f"O resultado de {valor1} {operacao} {valor2} é: {resultado}")

        except ValueError:
            print("Erro: Por favor, insira valores numéricos válidos.")
            continue

        # Pergunta se o usuário deseja continuar
        repetir = input("Deseja continuar? (introduza s/n): ").strip().lower()
        if repetir != 's':
            print("Encerrando o programa.")
            break

# Executa a calculadora
calculadora()
