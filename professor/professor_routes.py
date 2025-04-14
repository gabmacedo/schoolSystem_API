from flask import Blueprint, request, jsonify
from professor.professor_controller import listar_professores, buscar_professor, criar_professor, remover_professor, atualizar_professor

professor_bp = Blueprint('professor_bp', __name__)

@professor_bp.route('/', methods=['GET'])
def get_professores():
    return jsonify(listar_professores())

@professor_bp.route('/<int:professor_id>', methods=['GET'])
def get_professor(professor_id):
    professor = buscar_professor(professor_id)
    if professor:
        return jsonify(professor)
    return jsonify({"erro": "Professor não encontrado"}), 404

@professor_bp.route('/', methods=['POST'])
def post_professor():
    dados = request.get_json()
    resposta, status = criar_professor(dados)
    return jsonify(resposta), status

@professor_bp.route('/<int:professor_id>', methods=['DELETE'])
def delete_professor(professor_id):
    resposta, status = remover_professor(professor_id)
    return jsonify(resposta), status

@professor_bp.route('/<int:professor_id>', methods=['PUT'])
def put_professor(professor_id):
    dados = request.get_json()
    resposta, status = atualizar_professor(professor_id, dados)
    return jsonify(resposta), status
