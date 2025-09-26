def listar_tarefas(): # Função para listar tarefas na interface

    import código  # Importa o módulo código.py
    import tkinter as tk # Biblioteca para GUI 
    from tkinter import messagebox, simpledialog # Importa componentes de diálogo e mensagens

def listar_tarefas(): # Função para listar tarefas na interface
    tarefas = código.carregar_tarefas() # Carrega tarefas do arquivo
    lista.delete(0, tk.END) # Limpa a lista atual
    for i, tarefa in enumerate(tarefas): # Itera sobre as tarefas
        status = "✔" if tarefa.get("concluida") else "✗"
        desc = f"[{status}] {tarefa['descricao']} | {tarefa['categoria']} | Prioridade: {tarefa['prioridade']} | Usuário: {tarefa['usuario']}"
        lista.insert(tk.END, desc) # Insere a descrição na lista

def adicionar_tarefa(): # Função para adicionar uma nova tarefa
    descricao = simpledialog.askstring("Adicionar Tarefa", "Descrição da tarefa:") # Pede descrição, categoria, prioridade e usuário
    if not descricao:
        return
    categoria = simpledialog.askstring("Adicionar Tarefa", "Categoria:") # Pede categoria
    if not categoria:
        return
    prioridade = simpledialog.askstring("Adicionar Tarefa", "Prioridade (alta, média, baixa):") # Pede prioridade
    if not prioridade or prioridade.lower() not in ["alta", "média", "media", "baixa"]:
        messagebox.showerror("Erro", "Prioridade inválida.")
        return
    if prioridade.lower() == "media":
        prioridade = "média"
    usuarios_permitidos = ["Lioniso", "Ana", "Camila", "Rossana", "Angela", "Renata"]
    usuario = simpledialog.askstring("Adicionar Tarefa", f"Usuário ({', '.join(usuarios_permitidos)}):")
    if not usuario or usuario not in usuarios_permitidos:
        messagebox.showerror("Erro", "Usuário inválido.")
        return
    nova_tarefa = {
        "descricao": descricao,
        "categoria": categoria,
        "concluida": False,
        "data_criacao": código.date.today().isoformat(),
        "prioridade": prioridade,
        "usuario": usuario
    }
    tarefas = código.carregar_tarefas()
    tarefas.append(nova_tarefa)
    código.tarefas = tarefas
    código.salvar_tarefas()
    listar_tarefas()
    messagebox.showinfo("Sucesso", "Tarefa adicionada!")

# Solicita dados ao usuário via diálogos
# Valida prioridade e usuário.
# Cria um dicionário de tarefa e salva no arquivo.
# Atualiza a lista visual.

def remover_tarefa():
    idx = lista.curselection()
    # ... verifica seleção
    if not idx:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover.")
        return
    idx = idx[0]
    tarefas = código.carregar_tarefas()
    tarefa_removida = tarefas.pop(idx)
    código.tarefas = tarefas
    código.salvar_tarefas()
    listar_tarefas()
    messagebox.showinfo("Removida", f"Tarefa '{tarefa_removida['descricao']}' removida.")
# Remove a tarefa selecionada na interface e Atualiza o arquivo e a lista visual.

def marcar_concluida():
    idx = lista.curselection()
    if not idx:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para marcar como concluída.")
        return
    idx = idx[0]
    tarefas = código.carregar_tarefas()
    if not tarefas[idx]["concluida"]:
        tarefas[idx]["concluida"] = True
        código.tarefas = tarefas
        código.salvar_tarefas()
        listar_tarefas()
        messagebox.showinfo("Concluída", "Tarefa marcada como concluída!")
    else:
        messagebox.showinfo("Info", "Esta tarefa já está concluída.")

def detalhes_tarefa(event=None):
    idx = lista.curselection()
    if not idx:
        return
    idx = idx[0]
    tarefas = código.carregar_tarefas()
    tarefa = tarefas[idx]
    info = (f"Descrição: {tarefa['descricao']}\nCategoria: {tarefa['categoria']}\n"
            f"Prioridade: {tarefa['prioridade']}\nUsuário: {tarefa['usuario']}\n"
            f"Data: {tarefa['data_criacao']}\nConcluída: {'Sim' if tarefa['concluida'] else 'Não'}")
    messagebox.showinfo("Detalhes da Tarefa", info) # Mostra todos os detalhes da tarefa selecionada em uma janela popup.

root = tk.Tk()
root.title("Gerenciador de Tarefas GOF Senac")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

lista = tk.Listbox(frame, width=80, height=10)
lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
lista.bind('<Double-1>', detalhes_tarefa)

scroll = tk.Scrollbar(frame, orient=tk.VERTICAL, command=lista.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
lista.config(yscrollcommand=scroll.set)

btns = tk.Frame(root)
btns.pack(pady=5)

tk.Button(btns, text="Listar Tarefas", command=listar_tarefas).pack(side=tk.LEFT, padx=2)
tk.Button(btns, text="Adicionar Tarefa", command=adicionar_tarefa).pack(side=tk.LEFT, padx=2)
tk.Button(btns, text="Remover Tarefa", command=remover_tarefa).pack(side=tk.LEFT, padx=2)
tk.Button(btns, text="Marcar como Concluída", command=marcar_concluida).pack(side=tk.LEFT, padx=2)

listar_tarefas()
root.mainloop()

# Cria a janela principal.
# Adiciona uma lista de tarefas com barra de rolagem.
# Adiciona botões para cada ação.
# Liga o duplo clique na lista para mostrar detalhes.
# Inicializa a lista de tarefas ao abrir.