from flask import Blueprint, request
from .turma_controller import (
    listar_turmas, buscar_turma,
    criar_turma, remover_turma, atualizar_turma
)
from app_data import professores  # usa professores globais

turma_bp = Blueprint('turmas', __name__)

@turma_bp.route('/', methods=['GET'])
def route_listar_turmas():
    return listar_turmas()

@turma_bp.route('/<int:turma_id>', methods=['GET'])
def route_buscar_turma(turma_id):
    return buscar_turma(turma_id)

@turma_bp.route('/', methods=['POST'])
def route_criar_turma():
    dados = request.get_json()
    return criar_turma(dados, professores)

@turma_bp.route('/<int:turma_id>', methods=['DELETE'])
def route_remover_turma(turma_id):
    return remover_turma(turma_id)

@turma_bp.route('/<int:turma_id>', methods=['PUT'])
def route_atualizar_turma(turma_id):
    dados = request.get_json()
    return atualizar_turma(turma_id, dados)
