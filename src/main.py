"""TaskTracker Acadêmico: organização de tarefas pelo terminal."""


def ler_titulo():
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("Erro: o título não pode ficar vazio.")


def ler_prioridade():
    prioridades = {"Alta": "Alta", "Média": "Média", "Media": "Média", "Baixa": "Baixa"}
    while True:
        prioridade = input("Prioridade (Alta/Média/Media/Baixa): ").strip()
        if prioridade in prioridades:
            return prioridades[prioridade]
        print("Erro: informe Alta, Média (ou Media) ou Baixa.")


def cadastrar_tarefa(tarefas):
    print("\n--- Cadastrar tarefa ---")
    tarefa = {
        "titulo": ler_titulo(),
        "descricao": input("Descrição: ").strip(),
        "disciplina": input("Disciplina: ").strip(),
        "prioridade": ler_prioridade(),
        "data_limite": input("Data limite (ex.: 20/10/2026): ").strip(),
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")


def visualizar_tarefas(tarefas):
    if not tarefas:
        print("\nNão existem tarefas cadastradas no momento.")
        return
    print("\n--- Tarefas cadastradas ---")
    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Disciplina: {tarefa['disciplina']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status: {tarefa['status']}")


def concluir_tarefa(tarefas):
    if not tarefas:
        print("\nNão existem tarefas cadastradas no momento.")
        return
    visualizar_tarefas(tarefas)
    while True:
        escolha = input("\nNúmero da tarefa para concluir (0 para cancelar): ").strip()
        if escolha == "0":
            return
        try:
            numero = int(escolha)
        except ValueError:
            print("Erro: digite um número inteiro.")
            continue
        if not 1 <= numero <= len(tarefas):
            print("Erro: tarefa não encontrada.")
            continue
        tarefa = tarefas[numero - 1]
        if tarefa["status"] == "Concluída":
            print("Essa tarefa já está concluída.")
            return
        tarefa["status"] = "Concluída"
        print("Tarefa concluída com sucesso!")
        return


def main():
    tarefas = []
    while True:
        print("\n=== TaskTracker Acadêmico ===")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")
        print("4. Concluir tarefa")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("Aplicação encerrada. Até logo!")
            break
        elif opcao == "4":
            concluir_tarefa(tarefas)
        else:
            print("Opção inválida. Escolha 1, 2, 3 ou 4.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nAplicação encerrada.")
