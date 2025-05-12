from flask import request, jsonify
from config import db
from turma.turma_model import Turma
from professor.professor_model import Professor

def listar_turmas():
    turmas = Turma.query.all()
    return ([t.to_dict() for t in turmas]), 200

def buscar_turma(turma_id):
    turma = Turma.query.get(turma_id)
    if turma:
        return turma.to_dict(), 200
    return {"erro": "Turma não encontrada"}, 404

def criar_turma(dados):
    campos = ['nome', 'materia', 'descricao', 'ativo', 'professor_id']
    for campo in campos:
        if campo not in dados:
            return {"erro": f"Campo obrigatório '{campo}' não enviado"}, 400

    professor = Professor.query.get(dados['professor_id'])
    if not professor:
        return {"erro": "Professor não encontrado"}, 404

    try:
        nova_turma = Turma(
            nome=dados['nome'],
            materia=dados['materia'],
            descricao=dados['descricao'],
            ativo=dados['ativo'],
            professor_id=dados['professor_id']
        )

        db.session.add(nova_turma)
        db.session.commit()

        return nova_turma.to_dict(), 201

    except Exception as e:
        db.session.rollback()
        return {"erro": str(e)}, 500

def atualizar_turma(turma_id, dados):
    turma = Turma.query.get(turma_id)
    if not turma:
        return {"erro": "Turma não encontrada"}, 404

    turma.nome = dados.get('nome', turma.nome)
    turma.materia = dados.get('materia', turma.materia)
    turma.descricao = dados.get('descricao', turma.descricao)
    turma.ativo = dados.get('ativo', turma.ativo)
    turma.professor_id = dados.get('professor_id', turma.professor_id)

    try:
        db.session.commit()
        return turma.to_dict(), 200
    except Exception as e:
        return {"erro": f"Erro ao atualizar turma: {str(e)}"}, 500

def remover_turma(turma_id):
    turma = Turma.query.get(turma_id)
    if not turma:
        return {"erro": "Turma não encontrada"}, 404

    try:
        db.session.delete(turma)
        db.session.commit()
        return {"mensagem": "Turma removida com sucesso"}, 200
    except Exception as e:
        db.session.rollback()
        return {"erro": str(e)}, 500
