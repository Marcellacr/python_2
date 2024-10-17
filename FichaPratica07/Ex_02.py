# Dicionário traduções
tradutor = {
    "dog": "cachorro",
    "cat": "gato",
    "house": "casa",
    "car": "carro"
}

# Função principal
def traduzir_palavra():
    while True:
        # Solicita uma palavra em inglês
        palavra = input("Digite uma palavra em inglês: ").lower()

        # Verifica se o usuário deseja encerrar o programa
        if palavra in tradutor:
            print(f"A tradução de '{palavra}' é '{tradutor[palavra]}'.")
        
        else:
            print(f"Desculpe, a palavra '{palavra}' não está no dicionário.")

# Executa a função
traduzir_palavra()
    