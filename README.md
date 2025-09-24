# Sistema-de-Gerenciamento-de-Tarefas
Um sistema de gerenciamento de tarefas em Python com interface de linha de comando (CLI) que permite criar, organizar e gerenciar tarefas com diversas funcionalidades avançadas.

📋 Funcionalidades
✅ Adicionar tarefas com descrição, categoria, responsável e prioridade
📅 Datas flexíveis - suporte a prazos opcionais e data de criação automática
🎯 Sistema de prioridades - Alta, Média e Baixa
🔍 Filtros avançados - por status, categoria, responsável ou prioridade
📊 Ordenação personalizável - por prioridade, prazo ou data de criação
🔎 Busca por palavra-chave na descrição das tarefas
📂 Visualização de categorias únicas
💾 Armazenamento em memória (durante a execução)

Menu Principal
O sistema oferece um menu interativo com as seguintes opções:
Adicionar tarefa - Criar nova tarefa com todos os detalhes
Listar tarefas - Visualizar com filtros e ordenação
Buscar por palavra-chave - Encontrar tarefas por termo específico
Marcar tarefa como concluída - Atualizar status das tarefas
Remover tarefa - Excluir tarefas com confirmação
Mostrar categorias únicas - Listar todas as categorias existentes
Sair - Encerrar o programa

📝 Estrutura das Tarefas
Cada tarefa contém os seguintes campos:
Descrição - Texto da tarefa (obrigatório)
Categoria - Classificação da tarefa (obrigatório)
Responsável - Pessoa designada (obrigatório)
Status - Concluída ou pendente
Prioridade - Alta, Média ou Baixa
Data de criação - Automática (data atual)
Prazo - Opcional (formato YYYY-MM-DD)

🎮 Comandos de Prioridade
Ao adicionar tarefas, você pode usar:
Alta: 1, alta, a
Média: 2, média, media, m
Baixa: 3, baixa, b

🔧 Filtros Disponíveis
Na listagem de tarefas, você pode filtrar por:
Todas as tarefas
Apenas pendentes
Apenas concluídas
Por categoria específica
Por responsável específico
Por nível de prioridade

📊 Opções de Ordenação
Sem ordenação
Por prioridade (Alta → Baixa)
Por prazo (mais próximo primeiro)
Por data de criação (mais antiga primeiro)

⚠️ Observações
Os dados são armazenados apenas durante a execução do programa
Use o formato YYYY-MM-DD para datas
Entradas vazias não são permitidas nos campos obrigatórios
O sistema é case-insensitive para buscas e filtros

🛠️ Tecnologias Utilizadas
Python 3
Módulo datetime para manipulação de datas
Estruturas de dados nativas do Python (listas, dicionários)
