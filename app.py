import os
from flask import Flask, redirect, url_for, request, flash, render_template
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin
import logging
import sys

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY', 'minha-chave-secreta')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('DEV-DG7')

        if not username:
            logging.warning('Tentativa de login sem fornecer username')
            flash('Username é obrigatório!', 'warning')
            return redirect(url_for('login'))

        if username == 'admin':
            user = User(id=1)
            login_user(user)
            logging.info(f'Login bem-sucedido para o usuário: {username}')
            return redirect(url_for('tasks'))
        else:
            logging.warning(f'Falha de login para o usuário: {username}')
            flash('Falha no login. Usuário incorreto!', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/tasks')
@login_required
def tasks():
    return 'Aqui estão suas tarefas'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    logging.info('Usuário deslogado')
    return redirect(url_for('login'))

@app.route('/api/test')
def test_api():
    return 'API está funcionando!', 200

def create_app():
    """Função que cria e retorna a aplicação Flask"""
    return app

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
