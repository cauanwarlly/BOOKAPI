import pytest
from app import create_app, db
from app.models.funcionario_model import Funcionario

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()   # limpa tudo
            db.create_all() # recria as tabelas limpas
        yield client


def test_post_funcionario(client):
    response = client.post("/funcionarios", json={
        "nome": "Carlos Silva",
        "idade": 29,
        "cargo": "Analista de Sistemas"
    })
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["message"] == "Funcionário criado com sucesso!"




def test_get_funcionarios(client):
    client.post("/funcionarios", json={
        "nome": "Ana Costa",
        "idade": 32,
        "cargo": "Designer"
    })
    response = client.get("/funcionarios")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert data[0]["nome"] == "Ana Costa"

def test_get_single_funcionario(client):
    client.post("/funcionarios", json={
        "nome": "Lucas",
        "idade": 40,
        "cargo": "Engenheiro"
    })
    response = client.get("/funcionarios/1")
    assert response.status_code == 200
    assert response.get_json()["cargo"] == "Engenheiro"

def test_update_funcionario(client):
    client.post("/funcionarios", json={
        "nome": "João",
        "idade": 45,
        "cargo": "Gerente"
    })
    response = client.put("/funcionarios/1", json={"cargo": "Diretor"})
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["message"] == "Funcionario atualizado com sucesso!"

    get_response = client.get("/funcionarios/1")
    assert get_response.get_json()["cargo"] == "Diretor"

def test_delete_funcionario(client):
    client.post("/funcionarios", json={
        "nome": "Maria",
        "idade": 28,
        "cargo": "Secretária"
    })
    response = client.delete("/funcionarios/1")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["message"] == "Funcionario deletado com sucesso!"

    not_found = client.get("/funcionarios/1")
    assert not_found.status_code == 404
