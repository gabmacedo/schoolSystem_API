from flask import jsonify, request
from config import db
from aluno.aluno_model import Aluno
from datetime import datetime

def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify([aluno.to_dict() for aluno in alunos]), 200

def buscar_aluno(aluno_id):
    aluno = Aluno.query.get(aluno_id)
    if aluno:
        return jsonify(aluno.to_dict()), 200
    else:
        return jsonify({"erro": "Aluno não encontrado"}), 404

def criar_aluno():
    dados = request.get_json()

    campos_obrigatorios = ['nome', 'data_nascimento', 'nota_primeiro_semestre', 'nota_segundo_semestre', 'turma_id']
    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({"erro": f"Campo obrigatório '{campo}' não enviado"}), 400
        
    try:
        novo_aluno = Aluno(
            nome=dados['nome'],
            data_nascimento=datetime.strptime(dados['data_nascimento'], '%Y-%m-%d').date(),
            nota_primeiro_semestre=dados['nota_primeiro_semestre'],
            nota_segundo_semestre=dados['nota_segundo_semestre'],
            turma_id=dados['turma_id']
        )
        db.session.add(novo_aluno)
        db.session.commit()
        return jsonify(novo_aluno.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500
    

def atualizar_aluno(aluno_id):
    aluno = Aluno.query.get(aluno_id)
    if not aluno:
        return jsonify({"erro": "Aluno não encontrado"}), 404

    dados = request.get_json()

    try:
        if 'nome' in dados:
            aluno.nome = dados['nome']
        if 'data_nascimento' in dados:
            aluno.data_nascimento = datetime.strptime(dados['data_nascimento'], '%Y-%m-%d').date()
        if 'nota_primeiro_semestre' in dados:
            aluno.nota_primeiro_semestre = dados['nota_primeiro_semestre']
        if 'nota_segundo_semestre' in dados:
            aluno.nota_segundo_semestre = dados['nota_segundo_semestre']
        if 'turma_id' in dados:
            aluno.turma_id = dados['turma_id']

        db.session.commit()
        return jsonify(aluno.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500

def remover_aluno(aluno_id):
    aluno = Aluno.query.get(aluno_id)
    if not aluno:
        return jsonify({"erro": "Aluno não encontrado"}), 404

    try:
        db.session.delete(aluno)
        db.session.commit()
        return jsonify({"mensagem": "Aluno removido com sucesso"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500