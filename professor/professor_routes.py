from flask import Blueprint
from professor.professor_controller import listar_professores, buscar_professor, criar_professor, atualizar_professor, remover_professor


professor_bp = Blueprint('professor_bp', __name__)

@professor_bp.route('/', methods=['GET'])
def get_professores():
    return listar_professores()

@professor_bp.route('/<int:professor_id>', methods=['GET'])
def get_professor(professor_id):
    return buscar_professor(professor_id)

@professor_bp.route('/', methods=['POST'])
def post_professor():
    return criar_professor()

@professor_bp.route('/<int:professor_id>', methods=['PUT'])
def put_professor(professor_id):
    return atualizar_professor(professor_id)

@professor_bp.route('/<int:professor_id>', methods=['DELETE'])
def delete_professor(professor_id):
    return remover_professor(professor_id)
