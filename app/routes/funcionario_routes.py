from flask import Blueprint
from app.controllers import funcionario_controller

funcionario_bp = Blueprint("funcionarios", __name__)

@funcionario_bp.route("/funcionarios", methods=["POST"])
def add_funcionario():
    """
    Cria um novo funcionário
    ---
    tags:
      - Funcionários
    parameters:
      - in: body
        name: corpo
        schema:
          type: object
          properties:
            nome:
              type: string
              example: João Silva
            idade:
              type: integer
              example: 30
            cargo:
              type: string
              example: Analista
    responses:
      201:
        description: Funcionário criado com sucesso
    """
    return funcionario_controller.add_funcionario()

@funcionario_bp.route("/funcionarios", methods=["GET"])
def get_funcionarios():
    """
    Lista todos os funcionários
    ---
    tags:
      - Funcionários
    responses:
      200:
        description: Lista de funcionários
    """
    return funcionario_controller.get_funcionarios()

@funcionario_bp.route("/funcionarios/<int:funcionario_id>", methods=["GET"])
def get_funcionario(funcionario_id):
    """
    Retorna um funcionário específico pelo ID
    ---
    tags:
      - Funcionários
    parameters:
      - in: path
        name: funcionario_id
        type: integer
        required: true
    responses:
      200:
        description: Funcionário encontrado
    """
    return funcionario_controller.get_funcionario(funcionario_id)

@funcionario_bp.route("/funcionarios/<int:funcionario_id>", methods=["PUT"])
def update_funcionario(funcionario_id):
    """
    Atualiza um funcionário
    ---
    tags:
      - Funcionários
    parameters:
      - in: path
        name: funcionario_id
        type: integer
        required: true
      - in: body
        name: corpo
        schema:
          type: object
          properties:
            nome:
              type: string
            idade:
              type: integer
            cargo:
              type: string
    responses:
      200:
        description: Funcionário atualizado com sucesso
    """
    return funcionario_controller.update_funcionario(funcionario_id)

@funcionario_bp.route("/funcionarios/<int:funcionario_id>", methods=["DELETE"])
def delete_funcionario(funcionario_id):
    """
    Deleta um funcionário pelo ID
    ---
    tags:
      - Funcionários
    parameters:
      - in: path
        name: funcionario_id
        type: integer
        required: true
    responses:
      200:
        description: Funcionario deletado com sucesso
    """
    return funcionario_controller.delete_funcionario(funcionario_id)
