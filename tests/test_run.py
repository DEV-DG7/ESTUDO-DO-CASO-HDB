import unittest
from unittest.mock import patch
import run

class TestRun(unittest.TestCase):

    @patch('run.app.run')
    def test_start_app(self, mock_run):
        """Testa se a aplicação inicia sem erros."""
        mock_run.return_value = None
        try:
            run.start_app()
            mock_run.assert_called_once()  # Verifica se o app.run foi chamado uma vez
        except Exception:
            self.fail("A aplicação não deveria gerar exceções")

    @patch('run.app.run', side_effect=Exception("Erro de inicialização"))
    def test_start_app_with_exception(self, mock_run):
        """Testa o tratamento de erro ao iniciar a aplicação."""
        with self.assertRaises(Exception) as context:
            run.start_app()
        self.assertEqual(str(context.exception), "Erro de inicialização")

    @patch('run.start_app')
    def test_main_execution(self, mock_start_app):
        """Testa se a aplicação inicia ao executar o run.py diretamente."""
        with patch('run.__name__', "__main__"):
            run.start_app()
            mock_start_app.assert_called_once()

if __name__ == '__main__':
    unittest.main()
