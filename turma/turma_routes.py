from flask import Blueprint
from turma.turma_controller import listar_turmas, buscar_turma, criar_turma, atualizar_turma, remover_turma

turma_bp = Blueprint('turma_bp', __name__)

@turma_bp.route('/', methods=['GET'])
def get_turmas():
    return listar_turmas()

@turma_bp.route('/<int:turma_id>', methods=['GET'])
def get_turma(turma_id):
    return buscar_turma(turma_id)

@turma_bp.route('/', methods=['POST'])
def post_turma():
    return criar_turma()

@turma_bp.route('/<int:turma_id>', methods=['PUT'])
def put_turma(turma_id):
    return atualizar_turma(turma_id)

@turma_bp.route('/<int:turma_id>', methods=['DELETE'])
def delete_turma(turma_id):
    return remover_turma(turma_id)
