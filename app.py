from flask import Flask, redirect, url_for, request, flash, render_template
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin
import logging
import sys

# Configuração do Flask e Flask-Login
app = Flask(__name__)
app.secret_key = 'minha-chave-secreta'  # Certifique-se de definir uma chave secreta real

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Configuração de logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# Usuário fictício para fins de exemplo
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Carregando usuário
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        
        # Verificação do username
        if not username:
            logging.warning('Tentativa de login sem fornecer username')
            flash('Username é obrigatório!', 'warning')
            return redirect(url_for('login'))

        if username == 'admin':  # Simulando login de sucesso
            user = User(id=1)  # Simulação de ID do usuário
            login_user(user)
            logging.info(f'Login bem-sucedido para o usuário: {username}')
            return redirect(url_for('tasks'))
        else:
            logging.warning(f'Falha de login para o usuário: {username}')
            flash('Falha no login. Usuário incorreto!', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')  # Retorna um template simples para o login

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

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
