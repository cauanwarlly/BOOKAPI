from flask import request, jsonify
from app.models.funcionario_model import Funcionario
from app import db

def add_funcionario():
    data = request.get_json()
    funcionario = Funcionario(**data)
    db.session.add(funcionario)
    db.session.commit()
    return jsonify({"message": "Funcionário criado com sucesso!"}), 201

def get_funcionarios():
    funcionarios = Funcionario.query.all()
    return jsonify([f.to_dict() for f in funcionarios])

def get_funcionario(funcionario_id):
    funcionario = Funcionario.query.get_or_404(funcionario_id)
    return jsonify(funcionario.to_dict())

def update_funcionario(funcionario_id):
    funcionario = Funcionario.query.get_or_404(funcionario_id)
    data = request.get_json()
    funcionario.nome = data.get("nome", funcionario.nome)
    funcionario.idade = data.get("idade", funcionario.idade)
    funcionario.cargo = data.get("cargo", funcionario.cargo)
    db.session.commit()
    return jsonify({"message": "Funcionario atualizado com sucesso!"})

def delete_funcionario(funcionario_id):
    funcionario = Funcionario.query.get_or_404(funcionario_id)
    db.session.delete(funcionario)
    db.session.commit()
    return jsonify({"message": "Funcionario deletado com sucesso!"})