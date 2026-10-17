# TaskTracker Acadêmico

Projeto do Bootcamp II para organizar atividades acadêmicas pelo terminal.

## Funcionalidades

- Cadastrar título, descrição, disciplina, prioridade e data limite.
- Recusar títulos vazios ou compostos apenas por espaços.
- Aceitar exclusivamente Alta, Média, Media e Baixa como prioridades.
- Iniciar cada tarefa com status Pendente.
- Listar todos os dados das tarefas e informar quando a lista está vazia.
- Concluir tarefas cadastradas, conforme o planejamento da Fase 1.

## Tecnologias

Python 3, Git e GitHub. Não há bibliotecas externas para instalar.

## Instalação e execução

1. Instale o Python 3 e o Git.
2. Baixe o repositório e abra um terminal na pasta tasktracker-projeto.
3. Execute:

```console
python src/main.py
```

No Windows, também pode ser usado `py src/main.py`.

## Menu

1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação
4. Concluir tarefa

A opção 4 e o campo disciplina preservam o planejamento acadêmico original.
A data tem formato livre, conforme permitido no enunciado. Os dados ficam
em memória durante a execução e são descartados ao encerrar o programa.

## Estrutura

```text
tasktracker-projeto/
├── README.md
├── .gitignore
├── requirements.txt
├── docs/
│   ├── planejamento_logico.pdf
│   └── slides_planejamento_fase1.pdf
└── src/
    └── main.py
```

O planejamento lógico foi reconstruído a partir dos slides fornecidos da
Fase 1, pois o documento original do Google Docs não estava disponível.
Os slides originais estão preservados em docs/slides_planejamento_fase1.pdf.
Caso o documento original seja recuperado, substitua docs/planejamento_logico.pdf
por ele para atender exatamente à rastreabilidade solicitada pelo professor.

## Verificação manual

1. Liste tarefas antes de cadastrar: deve aparecer uma mensagem de lista vazia.
2. Cadastre com título vazio e depois apenas espaços: deve pedir novamente.
3. Informe prioridade Urgente: deve rejeitar e pedir novamente.
4. Informe Media: deve aceitar e exibir Média.
5. Liste duas tarefas: todos os campos devem aparecer com status Pendente.
6. Conclua uma tarefa e liste novamente: o status deve ser Concluída.
7. Digite uma opção inválida no menu: deve avisar e voltar ao menu.
8. Escolha 3: deve encerrar a aplicação.

## Autor

Gabriel Braga Ledo Luduvico - Ciência de Dados e Machine Learning, Turma A.

## Próxima etapa

Preparar o empacotamento e a execução com Docker na Fase 3.
