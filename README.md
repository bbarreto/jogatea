# Prancha de Comunicação

Para rodar o projeto, faça o clone do repositório e utilize os seguintes comandos.

```
# Para compilar a imagem Docker com o projeto
docker build . --tag prancha:latest

# Iniciar o servidor localmente expondo a porta 8000
docker run -d -p 8000:8000 prancha:latest

```