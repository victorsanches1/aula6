MAX = 100
funcionarios = []

def adicionar_funcionario():
    if len(funcionarios) >= MAX:
        print("Limite de funcionários atingido!")
        return

    nome = input("Nome: ").strip()
    cargo = input("Cargo: ").strip()
    
    try:
        salario = float(input("Salário: "))
    except ValueError:
        print("Valor de salário inválido!")
        return

    funcionario = {
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    }
    funcionarios.append(funcionario)
    print("Funcionário cadastrado!\n")

def listar_funcionarios():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.\n")
        return

    print("\nLista de Funcionários:")
    for i, f in enumerate(funcionarios, start=1):
        print(f"{i}) {f['nome']} - {f['cargo']} - R$ {f['salario']:.2f}")
    print()

def buscar_funcionario():
    nome_busca = input("Nome do funcionário: ").strip()

    for f in funcionarios:
        if f['nome'].lower() == nome_busca.lower():
            print(f"Cargo: {f['cargo']} | Salário: R$ {f['salario']:.2f}\n")
            return

    print("Funcionário não encontrado.\n")

def menu():
    while True:
        print("=== SISTEMA DE FUNCIONÁRIOS ===")
        print("1 - Adicionar funcionário")
        print("2 - Listar funcionários")
        print("3 - Buscar funcionário")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_funcionario()
        elif opcao == '2':
            listar_funcionarios()
        elif opcao == '3':
            buscar_funcionario()
        elif opcao == '0':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!\n")

menu()
