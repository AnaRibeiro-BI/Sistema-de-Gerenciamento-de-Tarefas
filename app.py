from flask import Flask, render_template, request, redirect, url_for
import json, os
from datetime import date

app = Flask(__name__)
ARQUIVO = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    tarefas = carregar_tarefas()
    concluidas = sum(1 for t in tarefas if t.get("concluida"))
    pendentes = len(tarefas) - concluidas
    return render_template('index.html', tarefas=tarefas, concluidas=concluidas, pendentes=pendentes)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        descricao = request.form['descricao']
        categoria = request.form['categoria']
        prioridade = request.form['prioridade']
        usuario = request.form['usuario']

        nova_tarefa = {
            "descricao": descricao,
            "categoria": categoria,
            "prioridade": prioridade,
            "usuario": usuario,
            "concluida": False,
            "data_criacao": date.today().isoformat()
        }

        tarefas = carregar_tarefas()
        tarefas.append(nova_tarefa)
        salvar_tarefas(tarefas)
        return redirect(url_for('index'))
    return render_template('cadastro.html')

@app.route('/concluir/<int:indice>')
def concluir(indice):
    tarefas = carregar_tarefas()
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)
    return redirect(url_for('index'))

@app.route('/remover/<int:indice>')
def remover(indice):
    tarefas = carregar_tarefas()
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        salvar_tarefas(tarefas)
    return redirect(url_for('index'))

@app.route('/editar/<int:indice>', methods=['GET', 'POST'])
def editar(indice):
    tarefas = carregar_tarefas()
    if indice >= len(tarefas):
        return redirect(url_for('index'))
    if request.method == 'POST':
        tarefas[indice]["descricao"] = request.form['descricao']
        tarefas[indice]["categoria"] = request.form['categoria']
        tarefas[indice]["prioridade"] = request.form['prioridade']
        tarefas[indice]["usuario"] = request.form['usuario']
        salvar_tarefas(tarefas)
        return redirect(url_for('index'))
    return render_template('editar.html', tarefa=tarefas[indice], indice=indice)

if __name__ == '__main__':
    app.run(debug=True)