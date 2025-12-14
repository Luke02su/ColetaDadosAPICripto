# Usa uma imagem base Python slim (menor e mais leve)
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o script Python para o diretório de trabalho
COPY script_api.py .

# Instala a dependência 'requests'
RUN pip install requests

# Comando padrão a ser executado quando o container inicia
CMD ["python", "script_api.py"]