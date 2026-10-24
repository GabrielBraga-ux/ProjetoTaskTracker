"""Verificações das regras do programa, sem bibliotecas externas."""

import importlib.util
import io
from pathlib import Path
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location(
    "tasktracker", Path(__file__).resolve().parents[1] / "src" / "main.py"
)
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


class TaskTrackerTests(unittest.TestCase):
    def test_titulo_recusa_vazio_e_espacos(self):
        with patch("builtins.input", side_effect=["", "   ", "  Trabalho  "]), \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertEqual(app.ler_titulo(), "Trabalho")
            self.assertEqual(output.getvalue().count("Erro:"), 2)

    def test_prioridade_valida_e_normaliza(self):
        for entrada, esperada in [("Alta", "Alta"), ("Média", "Média"),
                                  ("Media", "Média"), ("Baixa", "Baixa")]:
            with self.subTest(entrada=entrada), patch("builtins.input", return_value=entrada):
                self.assertEqual(app.ler_prioridade(), esperada)

    def test_prioridade_recusa_outros_valores(self):
        with patch("builtins.input", side_effect=["Urgente", "", "alta", "Alta"]), \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertEqual(app.ler_prioridade(), "Alta")
            self.assertEqual(output.getvalue().count("Erro:"), 3)

    def test_cadastro_e_listagem_com_todos_os_campos(self):
        tarefas = []
        valores = ["Trabalho", "Exercícios", "Estatística", "Media", "30/10/2026"]
        with patch("builtins.input", side_effect=valores), \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            app.cadastrar_tarefa(tarefas)
            app.visualizar_tarefas(tarefas)
        self.assertEqual(len(tarefas), 1)
        self.assertEqual(tarefas[0]["status"], "Pendente")
        for texto in ["Trabalho", "Exercícios", "Estatística", "Média",
                      "30/10/2026", "Pendente", "sucesso"]:
            self.assertIn(texto, output.getvalue())

    def test_listagem_vazia(self):
        with patch("sys.stdout", new_callable=io.StringIO) as output:
            app.visualizar_tarefas([])
        self.assertIn("Não existem tarefas", output.getvalue())

    def test_conclusao_valida_numero_e_altera_status(self):
        tarefas = [{"titulo": "Trabalho", "descricao": "Exercícios",
                    "disciplina": "Bootcamp", "prioridade": "Alta",
                    "data_limite": "30/10/2026", "status": "Pendente"}]
        with patch("builtins.input", side_effect=["abc", "999", "1"]), \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            app.concluir_tarefa(tarefas)
        self.assertEqual(tarefas[0]["status"], "Concluída")
        self.assertIn("número inteiro", output.getvalue())
        self.assertIn("não encontrada", output.getvalue())

    def test_menu_recusa_opcao_invalida_e_sai(self):
        with patch("builtins.input", side_effect=["9", "3"]), \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            app.main()
        self.assertIn("Opção inválida", output.getvalue())
        self.assertIn("Aplicação encerrada", output.getvalue())


if __name__ == "__main__":
    unittest.main()
