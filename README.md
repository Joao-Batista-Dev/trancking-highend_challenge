# Sistema de Loja de Veiculos

Teste Técnico - Vaga de Desenvolvedor Júnior - Tracking HighEnd

## Requisitos

Certifique-se de que você tenha os seguintes requisitos instalados em seu sistema:

- Docker
- Python
- Django (instalado automaticamente ao seguir as instruções abaixo)
- Outras dependências listadas no arquivo `requirements.txt`


## Instalação das Dependências

Com o ambiente virtual ativado, instale as dependências do projeto usando o comando:
```bash
pip install -r requirements.txt
```

## Rodar o projeto

Git clone:
```bash
https://github.com/Joao-Batista-Dev/trancking-highend_challenge
```

Entre no diretório do projeto
```bash
cd countries_challenge
```

Exercute o docker:
```bash
docker-compose up --build
```

Criando um usuário admin:
```bash
docker-compose exec countries_app python manage.py runserver 0.0.0.0:8000
```

### Todos os Endpoints

### **GET** `countries/top10`
#### Request Schema
```json
{
    "nome": "China",
    "populacao": 1402112000,
    "continente": "Asia"
}
```

### **GET** `countries/?name=brasil`
#### Response Schema
```json
"name": {
    "common": "Brazil",
    "official": "Federative Republic of Brazil",
    "nativeName": {
        "por": {
            "official": "República Federativa do Brasil",
            "common": "Brasil"
        }
    }
}
```

### **POST** `countries/assess/`
#### Response Schema
```json
{
  "countrie": "argentina",
  "liked": true
}

```


Após isso, o sistema estará pronto para ser acessado em:
[http://localhost:8000](http://localhost:8000)
