# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos de requisitos
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código
COPY . .

# Instale o OWASP Dependency-Check
RUN apt-get update && apt-get install -y owasp-dependency-check

# Comando para rodar os testes e análises
CMD ["sh", "-c", "python -m unittest discover && bandit -r . && dependency-check --scan ./ --format HTML --out report.html"]
