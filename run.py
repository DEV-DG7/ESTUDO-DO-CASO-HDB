import logging
import os
from app import create_app

# Configuração de logging
logging.basicConfig(level=logging.INFO)

# Inicializando o app através da função create_app
app = create_app()

def start_app():
    """Função para iniciar a aplicação Flask."""
    try:
        # Simula uma exceção geral com base em uma variável de ambiente para fins de teste
        if os.getenv('FORCE_GENERAL_EXCEPTION') == 'True':
            raise Exception("Exceção forçada para fins de teste.")

        # Verificando variáveis de ambiente para garantir cobertura de erro
        debug_mode = os.getenv('FLASK_DEBUG', 'False') == 'True'
        host = os.getenv('FLASK_RUN_HOST', '127.0.0.1')

        # Lidando com erro de valor ao converter porta para inteiro
        try:
            port = int(os.getenv('FLASK_RUN_PORT', 5000))
        except ValueError as ve:
            logging.error("Erro ao converter porta para inteiro")
            raise ValueError("Erro de inicialização: Porta inválida") from ve

        if not host or host.isspace():
            logging.error("Host inválido fornecido")
            raise ValueError("Erro de inicialização: Host inválido")

        app.run(debug=debug_mode, host=host, port=port)
        logging.info("Aplicação iniciada com sucesso.")
    except ValueError as ve:
        logging.error(f"Erro de valor ao iniciar a aplicação: {ve}")
        raise
    except Exception as e:
        logging.error(f"Erro inesperado ao iniciar a aplicação: {e}")
        raise Exception("Erro de inicialização") from e

# Verificação de ambiente para rodar a aplicação
if __name__ == "__main__":
    start_app()
