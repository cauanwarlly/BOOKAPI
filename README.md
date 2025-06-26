# BooksAPI

Uma API RESTful desenvolvida em Flask para gerenciamento de livros e registrar funcionários , com documentação Swagger integrada e testes automatizados.

## 🚀 Funcionalidades

- CRUD completo de livros
- Documentação automática com Swagger
- Testes automatizados com pytest
- Cobertura de testes monitorada
- Banco de dados SQLite com SQLAlchemy

## 📋 Pré-requisitos

- Python 3.x
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório:
```bash
git https://github.com/cauanwarlly/BOOKAPI.git
cd BOOKAPI
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🚀 Executando o Projeto

1. Inicie o servidor:
```bash
python run.py
```

2. Acesse a documentação Swagger:
```
http://localhost:5000/apidocs
```

## 📚 Endpoints da API

### Livros

- `POST /books` - Adiciona um novo livro
- `GET /books` - Lista todos os livros
- `GET /books/<id>` - Obtém um livro específico
- `PUT /books/<id>` - Atualiza um livro
- `DELETE /books/<id>` - Remove um livro

### Funcionario

- `POST /Funcionario` - Adiciona um novo Funcionario
- `GET /Funcionario` - Lista todos os Funcionario
- `GET /Funcionario/<id>` - Obtém um Funcionario específico
- `PUT /Funcionario/<id>` - Atualiza um Funcionario
- `DELETE /Funcionario/<id>` - Remove um Funcionario

## 🧪 Testes

Execute os testes com cobertura:
```bash
pytest --cov=app tests/
```

Cobertura atual:

--------------------------------------------------------------------
- `app\__init__.py`: 100%
- `app\config.py`: 100%
- `app\controllers\book_controller.py`: 100%
- `app\controllers\funcionario_controller.py`: 100%
- `app\models\book_model.py`: 100%
- `app\models\funcionario_model.py`: 100%
- `app\routes\book_routes.py`: 100%
- `app\routes\funcionario_routes.py`: 100%
-  **TOTAL** : 100%
---------------------------------------------------------------------

## 🛠️ Tecnologias Utilizadas

- Flask
- SQLAlchemy
- Flasgger (Swagger)
- pytest
- pytest-flask
- pytest-cov

## 📝 Estrutura do Projeto

```
bookAPI/
│
├── app/                        # Aplicação principal
│   │
│   ├── __init__.py             # Inicializa a aplicação Flask
│   ├── models/                 # Modelos do banco de dados (Book, Funcionario)
│   │   ├── book_model.py
│   │   └── funcionario_model.py
│   ├── controllers/            # Lógica de negócios (CRUDs)
│   │   ├── book_controller.py
│   │   └── funcionario_controller.py
│   ├── routes/                 # Rotas e Blueprints
│   │   ├── book_routes.py
│   │   ├── author_routes.py
│   │   └── funcionario_routes.py
│   └── config.py               # Configurações da aplicação
│
├── instance/                   # Configuração específica (por ex., banco SQLite local)
│
├── main.py                     # Ponto de entrada da aplicação 
├── run.py                      # Alternativa de execução 
├── requirements.txt            # Dependências (Flask, SQLAlchemy, etc.)
├── tests/                      # Testes com Pytest
│   │
│   ├── conftest.py             # Configuração dos testes
│   ├── test_books.py
│   └── test_funcionarios.py
``` 
