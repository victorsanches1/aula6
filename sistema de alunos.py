def main():
    notas = {}          
    lista_nomes = []     

    while True:
        print("\n=== SISTEMA DE ALUNOS ===")
        print("1 - Adicionar aluno")
        print("2 - Listar alunos")
        print("3 - Buscar nota")
        print("0 - Sair")

        try:
            opcao = int(input("Opção: "))
        except ValueError:
            print("Opção inválida. Digite um número.")
            continue

        if opcao == 1:
            adicionar_aluno(notas, lista_nomes)
        elif opcao == 2:
            listar_alunos(notas, lista_nomes)
        elif opcao == 3:
            buscar_nota(notas)
        elif opcao == 0:
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

def adicionar_aluno(notas, lista_nomes):
    nome = input("Nome do aluno: ").strip()
    try:
        nota = float(input("Nota final: "))
    except ValueError:
        print("Nota inválida. Use ponto como separador decimal (ex: 7.5)")
        return

    if nome in notas:
        print("Aluno já cadastrado. Atualizando nota.")
    else:
        lista_nomes.append(nome)

    notas[nome] = nota
    print("Aluno cadastrado com sucesso!")

def listar_alunos(notas, lista_nomes):
    if not lista_nomes:
        print("Nenhum aluno cadastrado.")
        return

    print("\nLista de alunos:")
    for nome in lista_nomes:
        print(f"- {nome} | Nota: {notas[nome]}")

def buscar_nota(notas):
    nome = input("Nome do aluno: ").strip()
    if nome in notas:
        print(f"Nota de {nome}: {notas[nome]}")
    else:
        print("Aluno não encontrado.")

if __name__ == "__main__":
    main()
