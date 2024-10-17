listaContactos = []

opcao = 0

while (opcao != 4):
    print("\n******* Lista de Contactos ********")
    print("1. Adicionar Novo Contacto")
    print("2. Consultar Lista de Contacto")
    print("3. Pesquisar um Contacto")
    print("4. Sair")
    opcao = int(input("Opção desejada: "))
    
    match (opcao):
        case 1:
            print("\n Adicionar novo Contacto")

            nome = input("Nome: ")
            telemovel = input("Telemóvel: ")
            morada = input("Morada: ")
    
            novoContacto = {
                "nome": nome,
                "telemovel": telemovel,
                "morada": morada
            }
            
            listaContactos.append(novoContacto)
            
        case 2:
            print("\n Consultar Lista de Contactos")
            print(listaContactos)
            
        case 3:
            print("\n Pesquisar um Contacto")
        
        case 4:
            print("\n Sair")

        case _:
            print("\n Opção não reconhecida")
