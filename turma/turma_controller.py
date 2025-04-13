from .turma_model import get_turmas, get_turma_id, post_turma, delete_turma, put_turma

def listar_turmas():
    return get_turmas()

def buscar_turma(turma_id):
    turma = get_turma_id(turma_id)
    if turma:
        return turma, 200
    return {"erro": "Turma não encontrada"}, 404

def criar_turma(dados, professores):
    if not all(k in dados for k in ("nome", "turno", "professor_id")):
        return {"erro": "Dados incompletos"}, 400

    if not any(p["id"] == dados["professor_id"] for p in professores):
        return {"erro": "Professor não encontrado"}, 404

    return post_turma(dados), 201

def remover_turma(turma_id):
    if delete_turma(turma_id):
        return {"mensagem": "Turma removida com sucesso"}, 200
    return {"erro": "Turma não encontrada"}, 404

def atualizar_turma(turma_id, dados):
    turma_atualizada = put_turma(turma_id, dados)
    if turma_atualizada:
        return turma_atualizada, 200
    return {"erro": "Turma não encontrada"}, 404
