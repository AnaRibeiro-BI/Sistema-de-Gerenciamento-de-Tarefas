# Sistema de Gerenciamento de Tarefas
# objetivo: Criar um program que permita ao usuário gerenciar uma lista de tarefas.
# Requisitos: # entrada de dados # listas e dicionários # condicionais # conjuntos # operadores lógicos e relacionados
# Descrição da atividade: o sistema deve permitir ao usuário adicionar, listar, marcar como concluída, remover tarefas e exibir categorias.


from datetime import date # permite criar datas no formato YYYY-MM-DD para salvar quando cada tarefa foi criada.
import json # possibilita gravar/ler as tarefas em arquivo no formato JSON (estrutura legível e fácil de reabrir).
import os # usado para verificar se o arquivo de tarefas já existe no sistema operacional.

ARQUIVO_TAREFAS = "tarefas_GOF.json" # Define o nome do arquivo onde as tarefas serão salvas.

# Função para carregar tarefas do arquivo. Objetivo: ler o arquivo JSON, caso exista, e retornar uma lista de dicionários representando as tarefas.
# Se o arquivo não existir, retorna uma lista vazia.
# os.path.exists evita erro ao tentar abrir um arquivo inexistente.

def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS): # evita erro ao tentar abrir um arquivo inexistente.
        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Função para salvar tarefas no arquivo Objetivo: gravar a lista tarefas no arquivo em formato JSON.
# indent=2 deixa o arquivo legível (formatação com espaçamento).
def salvar_tarefas():
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)  
# ensure_ascii=False preserva acentos e indent=2 deixa o arquivo legível (formatação com espaçamento).
# Essas funções garantem persistência de dados – sem elas, tudo seria perdido ao fechar o programa.

tarefas = carregar_tarefas() # Carrega as tarefas ao iniciar o programa.

PRIORIDADES = {"alta": 1, "média": 2, "media": 2, "baixa": 3}  # Dicionário para mapear prioridades a valores numéricos (útil para ordenação).

while True: # Loop principal do programa, exibindo o menu e processando as opções do usuário.
    
    # É o controlador do fluxo. Cada elif abaixo é uma operação que manipula a lista tarefas.
    
    print("\n--- MENU PRINCIPAL ---")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Remover tarefa")
    print("5 - Mostrar categorias únicas")
    print("6 - Editar tarefa")
    print("7 - Filtrar tarefas")
    print("8 - Status da Tarefa")
    print("9 - Sair")

    opcao = input("Escolha uma opção: ")    # Lê a opção do usuário.


    if opcao == "1":
        # Adicionar nova tarefa (com opção de voltar)
        print("Digite 'voltar' a qualquer momento para cancelar e retornar ao menu.")
        descricao = input("Descrição da tarefa: ")
        if descricao.strip().lower() == "voltar":
            print("Cadastro de tarefa cancelado.")
            continue
        categoria = input("Categoria: ")
        if categoria.strip().lower() == "voltar":
            print("Cadastro de tarefa cancelado.")
            continue

        # Solicitar prioridade
        while True:
            prioridade = input("Prioridade (alta, média, baixa): ").strip().lower()
            if prioridade == "voltar":
                print("Cadastro de tarefa cancelado.")
                break
            if prioridade in ["alta", "média", "media", "baixa"]:
                if prioridade == "media":
                    prioridade = "média"
                break
            else:
                print("Prioridade inválida. Digite: alta, média ou baixa.")
        else:
            continue

        if prioridade == "voltar":
            continue

        # Solicitar usuário
        usuarios_permitidos = ["Lioniso", "Ana", "Camila", "Rossana", "Angela", "Renata"]
        while True:
            usuario = input(f"Usuário ({', '.join(usuarios_permitidos)}): ").strip()
            if usuario.lower() == "voltar":
                print("Cadastro de tarefa cancelado.")
                break
            if usuario in usuarios_permitidos:
                break
            else:
                print("Usuário inválido. Escolha um dos usuários permitidos.")
        else:
            continue

        if usuario.lower() == "voltar":
            continue

        # Criar dicionário representando a tarefa, incluindo data de criação, prioridade e usuário
        nova_tarefa = {
            "descricao": descricao,
            "categoria": categoria,
            "concluida": False,
            "data_criacao": date.today().isoformat(),
            "prioridade": prioridade,
            "usuario": usuario
        }

        # Adicionar à lista de tarefas
        tarefas.append(nova_tarefa)
        salvar_tarefas()
        print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        # Listar todas as tarefas
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\n--- LISTA DE TAREFAS ---")
            for i, tarefa in enumerate(tarefas):
                status = "✔" if tarefa["concluida"] else "✗" # Marca visual para indicar se a tarefa está concluída ou não.
                print(f"{i+1}. [{status}] {tarefa['descricao']} ({tarefa['categoria']})")  # Exibe a tarefa com seu status e categoria.

    elif opcao == "3":
        # Marcar tarefa como concluída
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\n--- TAREFAS ---")
            for i, tarefa in enumerate(tarefas): # Percorre a lista de tarefas com enumerate para exibir índice + informações básicas.
                if not tarefa["concluida"]:
                    status = "✗"
                    print(f"{i+1}. [{status}] {tarefa['descricao']} ({tarefa['categoria']})")

            try: # Tenta converter a entrada do usuário para inteiro.
                indice = int(input("Número da tarefa a marcar como concluída: ")) - 1
                if 0 <= indice < len(tarefas): # Verifica se o índice é válido.
                    if not tarefas[indice]["concluida"]:
                        tarefas[indice]["concluida"] = True
                        salvar_tarefas()
                        print("Tarefa marcada como concluída!")
                    else:
                        print("Esta tarefa já está concluída.")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")

    elif opcao == "4":
        # Exibe/Conta todas as tarefas com len e Remove a escolhida com pop e salva.
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
                    salvar_tarefas()
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
# Usa um conjunto (set) para eliminar duplicatas.
# Por que set? Conjuntos não permitem elementos repetidos, ideal para extrair valores únicos.
            for tarefa in tarefas:
                categorias.add(tarefa["categoria"])

            print("\n--- CATEGORIAS ---")
            for i, categoria in enumerate(categorias):
                print(f"{i+1}. {categoria}")


    elif opcao == "6":
        # Editar tarefa
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\n--- TAREFAS ---")
            for i, tarefa in enumerate(tarefas):
                status = "✔" if tarefa["concluida"] else "✗"
                print(f"{i+1}. [{status}] {tarefa['descricao']} ({tarefa['categoria']})")
            try:
                indice = int(input("Número da tarefa a editar: ")) - 1
                if 0 <= indice < len(tarefas):
                    tarefa = tarefas[indice]
                    print("O que deseja editar?")
                    print("1 - Descrição")
                    print("2 - Categoria")
                    print("3 - Prioridade")
                    print("4 - Usuário")
                    campo = input("Escolha uma opção: ")
                    if campo == "1":
                        nova = input("Nova descrição: ")
                        tarefa["descricao"] = nova
                    elif campo == "2":
                        nova = input("Nova categoria: ")
                        tarefa["categoria"] = nova
                    elif campo == "3":
                        while True:
                            nova = input("Nova prioridade (alta, média, baixa): ").strip().lower()
                            if nova in ["alta", "média", "media", "baixa"]:
                                if nova == "media":
                                    nova = "média"
                                tarefa["prioridade"] = nova
                                break
                            else:
                                print("Prioridade inválida. Digite: alta, média ou baixa.")
                    elif campo == "4":
                        usuarios_permitidos = ["Lioniso", "Ana Luyza", "Camila", "Rossana", "Angela", "Renata"]
                        while True:
                            nova = input(f"Novo usuário ({', '.join(usuarios_permitidos)}): ").strip()
                            if nova in usuarios_permitidos:
                                tarefa["usuario"] = nova
                                break
                            else:
                                print("Usuário inválido. Escolha um dos usuários permitidos.")
                    else:
                        print("Opção inválida.")
                    salvar_tarefas()
                    print("Tarefa editada com sucesso!")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")

    elif opcao == "7":
        # Filtrar tarefas - Usa list comprehension para criar uma nova lista com as tarefas que satisfazem o critério.
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("Filtrar por:")
            print("1 - Categoria")
            print("2 - Prioridade")
            print("3 - Usuário")
            filtro = input("Escolha uma opção: ")
            if filtro == "1":
                categoria = input("Categoria para filtrar: ").strip()
                filtradas = [t for t in tarefas if t["categoria"].lower() == categoria.lower()]
            elif filtro == "2":
                prioridade = input("Prioridade para filtrar (alta, média, baixa): ").strip().lower()
                if prioridade == "media": prioridade = "média"
                filtradas = [t for t in tarefas if t["prioridade"] == prioridade]
            elif filtro == "3":
                usuarios_permitidos = ["Lioniso", "Ana", "Camila", "Rossana", "Angela", "Renata"]
                usuario = input(f"Usuário para filtrar ({', '.join(usuarios_permitidos)}): ").strip()
                filtradas = [t for t in tarefas if t["usuario"] == usuario]
            else:
                print("Opção inválida.")
                filtradas = []
            if filtradas:
                print("\n--- TAREFAS FILTRADAS ---")
                for i, tarefa in enumerate(filtradas):
                    status = "✔" if tarefa["concluida"] else "✗"
                    print(f"{i+1}. [{status}] {tarefa['descricao']} ({tarefa['categoria']}) | Prioridade: {tarefa['prioridade']} | Usuário: {tarefa['usuario']} | Data: {tarefa['data_criacao']}")
            else:
                print("Nenhuma tarefa encontrada com esse filtro.")

    elif opcao == "8":
        # Status da Tarefa - Conta e exibe o número de tarefas concluídas e pendentes.
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            concluidas = sum(1 for t in tarefas if t["concluida"])
            pendentes = len(tarefas) - concluidas
            print("\n--- STATUS DAS TAREFAS ---")
            print(f"Tarefas concluídas: {concluidas}")
            print(f"Tarefas pendentes: {pendentes}")
            
    elif opcao == "9":
        print("Saindo do sistema...")
        break # Encerra o laço while True, finalizando o programa.

    else:
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 6.")