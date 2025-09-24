# Sistema de Gerenciamento de Tarefas
# objetivo: Criar um programa que permita ao usuário gerenciar uma lista de tarefas.
# Requisitos:
# entrada de dados
# lsitas e dicionários
# condicionais
# conjuntos
# operadores lógicos e relacionados
# Descrição da atividade: o sistema deve permitir ao usuário adicionar, listar, marcar como concluída, remover tarefas e exibir categorias.

tarefas = []

while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Remover tarefa")
    print("5 - Mostrar categorias únicas")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Adicionar nova tarefa
        descricao = input("Descrição da tarefa: ")
        categoria = input("Categoria: ")

        # Criar dicionário representando a tarefa
        nova_tarefa = {
            "descricao": descricao,
            "categoria": categoria,
            "concluida": False
        }

        # Adicionar à lista de tarefas
        tarefas.append(nova_tarefa)
        print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        # Listar todas as tarefas
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\n--- LISTA DE TAREFAS ---")
            for i, tarefa in enumerate(tarefas):
                status = "✔" if tarefa["concluida"] else "✗"
                print(f"{i+1}. [{status}] {tarefa['descricao']} ({tarefa['categoria']})")

    elif opcao == "3":
        # Marcar tarefa como concluída
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\n--- TAREFAS ---")
            for i, tarefa in enumerate(tarefas):
                if not tarefa["concluida"]:
                    status = "✗"
                    print(f"{i+1}. [{status}] {tarefa['descricao']} ({tarefa['categoria']})")

            try:
                indice = int(input("Número da tarefa a marcar como concluída: ")) - 1
                if 0 <= indice < len(tarefas):
                    if not tarefas[indice]["concluida"]:
                        tarefas[indice]["concluida"] = True
                        print("Tarefa marcada como concluída!")
                    else:
                        print("Esta tarefa já está concluída.")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")

    elif opcao == "4":
        # Remover tarefa
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\n--- TAREFAS ---")
            for i, tarefa in enumerate(tarefas):
                status = "✔" if tarefa["concluida"] else "✗"
                print(f"{i+1}. [{status}] {tarefa['descricao']} ({tarefa['categoria']})")

            try:
                indice = int(input("Número da tarefa a remover: ")) - 1
                if 0 <= indice < len(tarefas):
                    tarefa_removida = tarefas.pop(indice)
                    print(f"Tarefa '{tarefa_removida['descricao']}' removida com sucesso!")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")

    elif opcao == "5":
        # Mostrar categorias únicas usando conjunto
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            categorias = set()
            for tarefa in tarefas:
                categorias.add(tarefa["categoria"])

            print("\n--- CATEGORIAS ---")
            for i, categoria in enumerate(categorias):
                print(f"{i+1}. {categoria}")

    elif opcao == "6":
        # Sair do programa
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 6.")
