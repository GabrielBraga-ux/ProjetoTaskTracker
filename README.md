# TaskTracker Acadêmico

Projeto do Bootcamp II para organizar atividades acadêmicas pelo terminal.

Repositório público do projeto:
[Segunda-Etapa-TaskTracker](https://github.com/GabrielBraga-ux/Segunda-Etapa-TaskTracker).
As atualizações da etapa final devem continuar neste mesmo repositório.

## Funcionalidades

- Cadastrar título, descrição, disciplina, prioridade e data limite.
- Recusar títulos vazios ou compostos apenas por espaços.
- Aceitar exclusivamente Alta, Média, Media e Baixa como prioridades.
- Iniciar cada tarefa com status Pendente.
- Listar todos os dados das tarefas e informar quando a lista está vazia.
- Concluir tarefas cadastradas, conforme o planejamento da Fase 1.

## Tecnologias

Python 3, Git, GitHub, Docker e Docker Compose. Não há bibliotecas externas Python para instalar.

## Etapa final: execução com Docker no PowerShell

Instale o [Docker Desktop para Windows](https://docs.docker.com/desktop/setup/install/windows-install/),
abra o aplicativo e aguarde o mecanismo Docker iniciar. Utilize containers Linux.
Com Docker, o Python roda dentro da imagem e não precisa estar instalado separadamente no computador.

Abra o PowerShell na pasta do projeto:

```powershell
cd "C:\Users\Jean Pierre\Documents\ChatGPT\Meu Site 2\tasktracker-projeto"
```

Confira a instalação e o mecanismo:

```powershell
docker --version
docker compose version
docker info
```

### Construir a imagem

```powershell
docker build -t tasktracker:final .
```

O ponto final indica a pasta atual. Na primeira execução, o Docker precisa de internet
para obter a imagem base `python:3.11-slim`.

### Executar o container isolado

```powershell
docker run --rm -it tasktracker:final
```

`-i` mantém a entrada aberta e `-t` cria um terminal. `--rm` remove o container ao sair.
Use a opção 3 no menu para encerrar.

### Executar com Docker Compose (recomendado)

```powershell
docker compose run --rm --build tasktracker-app
```

O Compose constrói a imagem e usa a configuração do serviço `tasktracker-app`.
`stdin_open: true` mantém a entrada aberta e `tty: true` disponibiliza o terminal
interativo necessário para `input()`. Não é necessário publicar portas para esta aplicação CLI.

### O que cada instrução faz

- `FROM python:3.11-slim`: define a imagem base com Python.
- `WORKDIR /app`: define a pasta de trabalho no container.
- `PYTHONUNBUFFERED=1`: mostra as saídas imediatamente.
- `COPY src/ /app/src/`: copia o código para a imagem.
- `CMD`: inicia `python src/main.py` ao executar o container.
- `.dockerignore`: evita enviar arquivos desnecessários ao contexto da construção.

### Problemas comuns

- `docker` não reconhecido: instale o Docker Desktop e reabra o PowerShell.
- Erro de conexão com o mecanismo: abra o Docker Desktop e espere iniciar.
- Pedido de WSL/virtualização: siga as instruções apresentadas pelo Docker Desktop.
- Sem interação: use `docker run --rm -it` ou o comando Compose acima.
- Código antigo: reconstrua a imagem após alterar os arquivos.

Referências: [Docker Compose run](https://docs.docker.com/reference/cli/docker/compose/run/)
e [configuração de serviços](https://docs.docker.com/reference/compose-file/services/).

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
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── docs/
│   ├── planejamento_logico.pdf
│   └── slides_planejamento_fase1.pdf
├── tests/
│   └── test_tasktracker.py
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

## Situação da validação

Testes automatizados das regras podem ser executados sem instalar bibliotecas:

```powershell
python -m unittest discover -s tests -v
```

Eles verificam título, prioridade, cadastro, listagem, conclusão e menu.

Os sete testes automatizados do Python passaram. O estudante demonstrou a construção da imagem e a abertura do menu com docker run em captura de tela. A validação completa em container
depende de executar os comandos acima em um computador com Docker disponível.
Não considere a etapa Docker concluída antes de construir a imagem e testar o menu dentro do container.

## Entrega final

Atualize o repositório público existente, mantendo o histórico das fases anteriores.
Grave um vídeo de cinco minutos com rosto e áudio próprios, formato horizontal 16:9,
publicado no YouTube como Público ou Não Listado. Demonstre GitHub, Dockerfile,
Compose, construção da imagem, execução interativa, validação de erro e listagem.
O PDF para o AVA deve conter seu nome e os links ativos do GitHub e desse novo vídeo.

