from flask import Flask, redirect, url_for, session, request
from flask_login import LoginManager, login_required, login_user, logout_user
import logging
import sys

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

@app.route('/login', methods=['POST'])
def login():
    # Autenticação de exemplo
    username = request.form.get('username')
    if username == 'admin':  # Simulando login de sucesso
        login_user(user)
        logging.info(f'Login bem-sucedido para usuário: {username}')
        return redirect(url_for('tasks'))
    else:
        logging.warning(f'Falha de login para usuário: {username}')
        return 'Falha no login', 401

@app.route('/tasks')
@login_required
def tasks():
    return 'Aqui estão suas tarefas'
