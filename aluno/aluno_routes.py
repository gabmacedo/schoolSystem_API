from flask import Blueprint, request, jsonify
from aluno_controller import listar_alunos, buscar_aluno, criar_aluno, remover_aluno, atualizar_aluno

aluno_bp = Blueprint('aluno_bp', __name__)

@aluno_bp.route('/', methods=['GET'])
def get_alunos():
    return jsonify(listar_alunos())

@aluno_bp.route('/<int:aluno_id>', methods=['GET'])
def get_aluno(aluno_id):
    aluno = buscar_aluno(aluno_id)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

@aluno_bp.route('/criar', methods=['POST'])
def post_aluno():
    dados = request.get_json()
    resposta, status = criar_aluno(dados)
    return jsonify(resposta), status

@aluno_bp.route('/<int:aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    resposta, status = remover_aluno(aluno_id)
    return jsonify(resposta), status

@aluno_bp.route('/<int:aluno_id>', methods=['PUT'])
def put_aluno(aluno_id):
    dados = request.get_json()
    resposta, status = atualizar_aluno(aluno_id, dados)
    return jsonify(resposta), status