import os
from app import app  # Certifique-se de que a instância do Flask está no arquivo app.py

if __name__ == "__main__":
    # Verificar se está em ambiente de desenvolvimento
    if os.environ.get("FLASK_ENV") == "development":
        app.run(debug=True, host='127.0.0.1', port=5000)
    else:
        app.run(debug=False, host='127.0.0.1', port=5000)
