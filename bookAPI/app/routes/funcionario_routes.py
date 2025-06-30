from flask import Blueprint
from app.controllers import funcionario_controller

funcionario_bp = Blueprint("funcionarios", __name__)





funcionario_bp.post("/funcionarios")(funcionario_controller.add_funcionario)
funcionario_bp.get("/funcionarios")(funcionario_controller.get_funcionarios)
funcionario_bp.get("/funcionarios/<int:funcionario_id>")(funcionario_controller.get_funcionario)
funcionario_bp.put("/funcionarios/<int:funcionario_id>")(funcionario_controller.update_funcionario)
funcionario_bp.delete("/funcionarios/<int:funcionario_id>")(funcionario_controller.delete_funcionario)
