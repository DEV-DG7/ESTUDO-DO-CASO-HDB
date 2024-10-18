import unittest
from app import app
from run import start_app
import os

class TestExample(unittest.TestCase):
    def setUp(self):
        """Configura o cliente de teste para a aplicação."""
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        """Teste da rota home."""
        response = self.app.get('/')
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')

    def test_addition(self):
        """Teste da rota de adição."""
        response = self.app.get('/add/1/2')
        self.assertEqual(response.data.decode('utf-8'), '3')

    def test_addition_invalid(self):
        """Teste de rota de adição inválida."""
        response = self.app.get('/add/a/b')
        self.assertEqual(response.status_code, 404)

    def test_login_success(self):
        """Teste do login bem-sucedido."""
        response = self.app.post('/login', data={'username': 'admin'})
        self.assertEqual(response.status_code, 302)

    def test_login_failure(self):
        """Teste do login com usuário inválido."""
        response = self.app.post('/login', data={'username': 'invalid_user'}, follow_redirects=True)
        self.assertIn('Falha no login. Usuário incorreto!', response.data.decode('utf-8'))

    def test_login_empty_username(self):
        """Teste do login com username vazio."""
        response = self.app.post('/login', data={'username': ''}, follow_redirects=True)
        self.assertIn('Username é obrigatório!', response.data.decode('utf-8'))

    def test_tasks(self):
        """Teste da rota de tarefas."""
        with self.app:
            self.app.post('/login', data={'username': 'admin'})
            response = self.app.get('/tasks')
            self.assertEqual(response.data.decode('utf-8'), 'Aqui estão suas tarefas')

    def test_logout(self):
        """Teste do logout."""
        with self.app:
            self.app.post('/login', data={'username': 'admin'})
            response = self.app.get('/logout')
            self.assertEqual(response.status_code, 302)

    def test_api_test(self):
        """Teste da rota da API."""
        response = self.app.get('/api/test')
        self.assertEqual(response.data.decode('utf-8'), 'API está funcionando!')

    # Testes para o arquivo run.py para garantir 100% de cobertura
    def test_start_app_invalid_port(self):
        """Teste do start_app com uma porta inválida."""
        with self.assertRaises(ValueError):
            os.environ['FLASK_RUN_PORT'] = 'invalid_port'  # Simula erro de porta inválida
            start_app()

    def test_start_app_invalid_host(self):
        """Teste do start_app com um host inválido."""
        with self.assertRaises(ValueError):
            os.environ['FLASK_RUN_HOST'] = ''  # Simula erro de host inválido
            start_app()

    def test_start_app_valid_config(self):
        """Teste do start_app com uma configuração válida."""
        os.environ['FLASK_RUN_PORT'] = '5000'
        os.environ['FLASK_RUN_HOST'] = '127.0.0.1'
        os.environ['FLASK_DEBUG'] = 'False'

        try:
            start_app()  # Não deve gerar nenhuma exceção
        except Exception as e:
            self.fail(f"start_app levantou uma exceção inesperada: {e}")

    def test_start_app_default_port(self):
        """Teste do start_app com a porta padrão."""
        if 'FLASK_RUN_PORT' in os.environ:
            del os.environ['FLASK_RUN_PORT']
        os.environ['FLASK_RUN_HOST'] = '127.0.0.1'

        try:
            start_app()  # Deve rodar na porta padrão (5000)
        except Exception as e:
            self.fail(f"start_app levantou uma exceção inesperada: {e}")

    def test_start_app_general_exception(self):
        """Teste que simula uma exceção geral ao iniciar a aplicação."""
        os.environ['FORCE_GENERAL_EXCEPTION'] = 'True'  # Força uma exceção geral
        with self.assertRaises(Exception):
            start_app()
        os.environ.pop('FORCE_GENERAL_EXCEPTION')  # Limpa a variável de ambiente após o teste

if __name__ == '__main__':
    unittest.main()
