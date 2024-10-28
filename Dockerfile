# Use a imagem Python 3.12
FROM python:3.12

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie todos os seus arquivos Python para o contêiner
COPY . /app

# Instale as dependências da aplicação, se houver um requirements.txt
# RUN pip install -r requirements.txt

# Comando para rodar a aplicação
CMD ["python", "main.py"]