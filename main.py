pacientes = {}

def criar_paciente():
    id = input("Informe o ID do paciente: ")
    if id.isdigit():
      id = int(id)
      if id in pacientes:
          print("Paciente já existe.")
      else:
        nome = input("Informe o nome do paciente: ")
        idade = input("Informe a idade do paciente: ")
        pacientes[id] = {"nome": nome, "idade": idade}
        print(f"Paciente {nome} criado com sucesso!")
    else:
      print('\n >> ID inválido. Por favor, informe um numero inteiro! <<')

def ler_paciente():
    id = input("Informe o ID do paciente que deseja consultar: ")
    if id in pacientes:
        print(f"ID: {id}, Nome: {pacientes[id]['nome']}, Idade: {pacientes[id]['idade']}")
    else:
        print("Paciente não encontrado.")


def atualizar_paciente():
    id = input("Informe o ID do paciente que deseja atualizar: ")
    if id in pacientes:
        nome = input("Informe o novo nome (ou pressione Enter para manter o atual): ")
        idade = input("Informe a nova idade (ou pressione Enter para manter a atual): ")

        if nome:
            pacientes[id]["nome"] = nome
        if idade:
            pacientes[id]["idade"] = idade

        print(f"Paciente {id} atualizado com sucesso!")
    else:
        print("Paciente não encontrado.")


def deletar_paciente():
    id = input("Informe o ID do paciente que deseja deletar: ")
    if id in pacientes:
        del pacientes[id]
        print(f"Paciente {id} deletado com sucesso!")
    else:
        print("Paciente não encontrado.")

def listar_pacientes():
    if pacientes:
        print("Lista de pacientes cadastrados")
        for id, info in pacientes.items():
                print(f"ID: {id}, Nome: {info['nome']}, Idade: {info['idade']}")
    else:
        print("Nenhum paciente cadastrado.")

def menu():
    while True:
        print("\n--- Sistema de Gerenciamento de Pacientes ---")
        print("1. Adicionar paciente")
        print("2. Consultar paciente")
        print("3. Atualizar paciente")
        print("4. Deletar paciente")
        print("5. Listar todos os pacientes")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_paciente()
        elif opcao == '2':
            ler_paciente()
        elif opcao == '3':
            atualizar_paciente()
        elif opcao == '4':
            deletar_paciente()
        elif opcao == '5':
            listar_pacientes()
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()