1️⃣ Estrutura geral

Lista de tarefas (tarefas):
Cada tarefa é um dicionário com vários campos:
{
    "descricao": "...",
    "categoria": "...",
    "responsavel": "...",
    "concluida": False,
    "prioridade": "Alta/Média/Baixa",
    "prioridade_nivel": 1/2/3,   # usado para ordenar
    "criada_em": date.today(),   # data automática
    "prazo": date ou None        # opcional
}

O programa fica rodando dentro de um loop while True mostrando o menu principal e chamando funções conforme a escolha do usuário.

2️⃣ Funções de entrada
Essas funções garantem que os dados não venham vazios ou com formato errado.
Função	O que faz
input_non_empty()	Repete a pergunta até o usuário digitar algo não vazio.
input_priority()	Aceita 1/2/3 ou Alta/Média/Baixa, e retorna a prioridade + um número interno para facilitar a ordenação.
input_date_optional()	Aceita uma data no formato YYYY-MM-DD ou ENTER para deixar em branco.

Por quê? → Isso evita erros de digitação e garante que o programa não quebre.

3️⃣ Criar tarefa
criar_tarefa()
Pede descrição, categoria, responsável, prioridade e prazo.
Coloca a data atual em criada_em.
Cria um dicionário e adiciona na lista tarefas.

4️⃣ Listar tarefas com filtros e ordenação
listar_tarefas()
Primeiro pergunta qual filtro aplicar:
Todas
Pendentes
Concluídas
Por categoria
Por responsável
Por prioridade
Depois pergunta se quer ordenar:
Sem ordenação
Por prioridade (Alta → Baixa)
Por prazo (mais próximo primeiro)
Por data de criação (mais antiga primeiro)
Mostra cada tarefa com todos os campos formatados.

5️⃣ Buscar por palavra-chave
buscar_por_palavra()
Digite um trecho da descrição.
O programa mostra só as tarefas que contêm essa palavra (sem diferenciar maiúsculas/minúsculas).

6️⃣ Marcar como concluída
marcar_concluida()
Mostra todas as tarefas numeradas.
O usuário digita o número da tarefa que quer marcar.
A tarefa recebe "concluida": True.

7️⃣ Remover tarefa
remover_tarefa()
Mostra todas as tarefas.
O usuário escolhe uma para remover.
Pede confirmação antes de excluir.

8️⃣ Categorias únicas
mostrar_categorias_unicas()
Usa um set para pegar apenas categorias distintas e exibe.

9️⃣ Menu principal
No final, o programa mostra:
1 - Adicionar tarefa
2 - Listar tarefas (com filtros/ordenação)
3 - Buscar por palavra-chave
4 - Marcar tarefa como concluída
5 - Remover tarefa
6 - Mostrar categorias únicas
7 - Sair

Ele fica repetindo até o usuário digitar 7.

🔑 Ideias-chave aprendidas
Validação de entradas impede que o programa quebre.
Filtros e ordenação dão mais controle ao usuário.
Datas e prioridades mostram como lidar com tipos mais ricos (datetime.date).
Funções deixam o código organizado e reaproveitável.