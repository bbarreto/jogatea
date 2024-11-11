# Prancha de Comunicação

# Modo desenvolvimento

Para rodar o projeto em modo de desenvolvimento, faça o clone do repositório.

## Configurações

Faça as alterações necessárias no arquivo `.env.dev`.

## Iniciando o modo desenvolvimento

Para iniciar o serviço, utilize o seguinte comando:

```
docker compose up
```

O servidor irá iniciar na porta 8000 e é acessível no navegador em http://127.0.0.1:8000/

## Autenticando a SDK do Google para geração de áudio

Este projeto usa a biblioteca do Google Cloud para conversão de texto em voz.

Você pode ativer sua conta em https://console.cloud.google.com/

Para iniciar a SDK e selecionar um projeto, execute:
```
docker compose exec web /root/google-cloud-sdk/bin/gcloud init
```

Para criar a chave de acesso padrão execute no terminal (com o servidor já iniciado):

```
docker compose exec web /root/google-cloud-sdk/bin/gcloud auth application-default login
```

Siga as instruções na tela para autenticar.

Este passo não é necessário caso esteja rodando o serviço em uma máquina virtual dentro do Google Cloud já que isso será responsabilidade de um IAM Role na plataforma.

## Para criar um usuário de administração

Execute o seguinte comando no terminal (com o servidor já iniciado):

```
docker compose exec web python manage.py createsuperuser
```

Após a criação do usuário, acesse: http://127.0.0.1:8000/admin para visualizar os registros do banco de dados.