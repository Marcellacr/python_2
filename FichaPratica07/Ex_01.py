# Dicionário de animais organizados por let
animais_letra = {
    "A": ["Andorinha", "Avestruz", "Alforreca"],
    "B": ["Baleia", "Búfalo", "Borboleta"],
    "C": ["Cachorro", "Camelo", "Cavalo"],
    "D": ["Dromedário", "Dinossauro", "Doninha"],
    # Adicione outras letras e listas de animais conforme necessário
}

# Função principal
def procurar_animais():
    while True:
        # Solicita uma letra ao usuário
        letra = input("Digite uma letra (ou 'S' para sair): ").upper()

        # Verifica se o usuário deseja sair
        if letra == 'S':
            print("Saindo... Até mais!")
            break

        # Verifica se a letra está no dicionário
        elif letra in animais_letra:
            print(f"Animais com a letra '{letra}': {', '.join(animais_letra[letra])}")
        
        else:
            print(f"Não há animais cadastrados com a letra '{letra}'.")

# Executa a função
procurar_animais()
