import os
import logging
import sys
from flask import Flask, redirect, url_for, request, flash, render_template
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin

# Inicializa a aplicação Flask
app = Flask(__name__)

# Configuração da chave secreta
app.secret_key = os.environ.get('SECRET_KEY', 'minha-chave-secreta')

# Configuração do gerenciador de login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Configuração de logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# Definição da classe de usuário
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Função de callback para carregar usuário
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')

        if not username:
            logging.warning('Tentativa de login sem fornecer username')
            flash('Username é obrigatório!', 'warning')
            return redirect(url_for('login'))  # Redireciona em vez de renderizar

        if username == 'admin':
            user = User(id=1)
            login_user(user)
            logging.info(f'Login bem-sucedido para o usuário: {username}')
            return redirect(url_for('tasks'))
        else:
            logging.warning(f'Falha de login para o usuário: {username}')
            flash('Falha no login. Usuário incorreto!', 'danger')
            return redirect(url_for('login'))  # Redireciona em vez de renderizar

    return render_template('login.html')  # Renderiza a página de login inicialmente

# Rota protegida para as tarefas
@app.route('/tasks')
@login_required
def tasks():
    return 'Aqui estão suas tarefas'

# Rota de logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    logging.info('Usuário deslogado')
    return redirect(url_for('login'))

# Rota da API de teste
@app.route('/api/test')
def test_api():
    return 'API está funcionando!', 200

# Nova rota adicionada para a página inicial
@app.route('/')
def home():
    return "Hello, World!"

# Rota de adição
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return str(num1 + num2)

# Função para criar a aplicação Flask
def create_app():
    return app

# Execução da aplicação
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)  # Cobrir esta linha
