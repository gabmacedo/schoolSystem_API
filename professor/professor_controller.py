from flask import jsonify, request
from config import db
from professor.professor_model import Professor

def listar_professores():
    professores = Professor.query.all()
    return [p.to_dict() for p in professores], 200

def buscar_professor(professor_id):
    professor = Professor.query.get(professor_id)
    if professor:
        return professor.to_dict(), 200
    return {"erro": "Professor não encontrado"}, 404

def criar_professor(dados):
    campos = ['nome', 'materia', 'observacoes', 'idade']
    for campo in campos:
        if campo not in dados:
            return {"erro": f"Campo obrigatório '{campo}' não enviado"}, 400

    try:
        novo_professor = Professor(
            nome=dados['nome'],
            materia=dados['materia'],
            observacoes=dados.get('observacoes', ''),
            idade=dados['idade']
        )

        db.session.add(novo_professor)
        db.session.commit()

        return novo_professor.to_dict(), 201
    
    except Exception as e:
        db.session.rollback()
        return {"erro": str(e)}, 500

def atualizar_professor(professor_id):
    professor = Professor.query.get(professor_id)
    if not professor:
        return {"erro": "Professor não encontrado"}, 404

    dados = request.get_json()

    professor.nome = dados.get('nome', professor.nome)
    professor.materia = dados.get('materia', professor.materia)
    professor.observacoes = dados.get('observacoes', professor.observacoes)
    professor.idade = dados.get('idade', professor.idade)

    try:
        db.session.commit()
        return professor.to_dict(), 200
    except Exception as e:
        return {"erro": f"Erro ao atualizar professor: {str(e)}"}, 500

def remover_professor(professor_id):
    professor = Professor.query.get(professor_id)
    if not professor:
        return {"erro": "Professor não encontrado"}, 404

    try:
        db.session.delete(professor)
        db.session.commit()
        return {"mensagem": "Professor removido com sucesso"}, 200
    except Exception as e:
        db.session.rollback()
        return {"erro": str(e)}, 500
