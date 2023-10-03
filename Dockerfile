# Use a imagem base do Python
FROM python:3.8-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de requisitos para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install -r requirements.txt

# Copie os arquivos da aplicação para o contêiner
COPY app.py .
COPY model.pkl .

# Exponha a porta em que a API irá rodar
EXPOSE 5000

# Defina a variável de ambiente para evitar problemas de codificação com Python
ENV LANG C.UTF-8

# Execute a aplicação quando o contêiner for iniciado
CMD ["python", "app.py"]
