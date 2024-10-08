# Use a imagem python:3.8-slim
FROM python:3.8-slim

# Definir o diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema necessárias para compilar pacotes
RUN apt-get update && apt-get install -y \
    gcc \
    libdbus-1-dev \
    libdbus-glib-1-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar o arquivo de requisitos
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código
COPY . .

# Comando para rodar a aplicação
CMD ["python", "run.py"]  # Atualizado para o arquivo correto de execução
