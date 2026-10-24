# Imagem leve com o Python usado para executar a aplicação.
FROM python:3.11-slim

WORKDIR /app

# Exibe mensagens imediatamente e evita arquivos temporários de bytecode.
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONIOENCODING=utf-8

# O projeto não depende de bibliotecas externas.
COPY src/ /app/src/

CMD ["python", "src/main.py"]
