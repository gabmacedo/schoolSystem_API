from flask import Blueprint
from aluno.aluno_controller import listar_alunos, buscar_aluno, criar_aluno, remover_aluno, atualizar_aluno

aluno_bp = Blueprint('aluno_bp', __name__)

# LISTAR TODOS ALUNOS
@aluno_bp.route('/', methods=['GET'])
def get_alunos():
    return listar_alunos()

# LISTAR ALUNO POR ID
@aluno_bp.route('/<int:aluno_id>', methods=['GET'])
def get_aluno(aluno_id):
    return buscar_aluno(aluno_id)

# CRIAR ALUNO
@aluno_bp.route('/', methods=['POST'])
def post_aluno():
    return criar_aluno()

# REMOVER ALUNO
@aluno_bp.route('/<int:aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    return remover_aluno(aluno_id)

# ATUALIZAR ALUNO
@aluno_bp.route('/<int:aluno_id>', methods=['PUT'])
def put_aluno(aluno_id):
    return atualizar_aluno(aluno_id)