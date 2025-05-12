from flask import jsonify, request
from config import db
from aluno.aluno_model import Aluno
from datetime import datetime
from turma.turma_model import Turma

def listar_alunos():
    alunos = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos], 200

def buscar_aluno(aluno_id):
    aluno = Aluno.query.get(aluno_id)
    if aluno:
        return aluno.to_dict(), 200
    else:
        return {"erro": "Aluno não encontrado"}, 404

def criar_aluno(dados):
    campos_obrigatorios = ['nome', 'data_nascimento', 'nota_primeiro_semestre', 'nota_segundo_semestre', 'turma_id']
    for campo in campos_obrigatorios:
        if campo not in dados:
            return {"erro": f"Campo obrigatório '{campo}' não enviado"}, 400

    turma = Turma.query.get(dados['turma_id'])
    if not turma:
        return {"erro": "Turma não encontrada"}, 404
        
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

        return novo_aluno.to_dict(), 201
    
    except Exception as e:
        db.session.rollback()
        return {"erro": str(e)}, 500
    

def atualizar_aluno(aluno_id):
    aluno = Aluno.query.get(aluno_id)
    if not aluno:
        return {"erro": "Aluno não encontrado"}, 404
    
    dados = request.get_json()

    aluno.nome = dados.get('nome', aluno.nome)
    aluno.data_nascimento = datetime.strptime(dados['data_nascimento'], '%Y-%m-%d').date()
    aluno.nota_primeiro_semestre = dados.get('nota_primeiro_semestre', aluno.nota_primeiro_semestre)
    aluno.nota_segundo_semestre = dados.get('nota_segundo_semestre', aluno.nota_segundo_semestre)
    aluno.turma_id = dados.get('turma_id', aluno.turma_id)

    try:
        db.session.commit()
        return aluno.to_dict(), 200
    except Exception as e:
        return {"erro": str(e)}, 500

def remover_aluno(aluno_id):
    aluno = Aluno.query.get(aluno_id)
    if not aluno:
        return {"erro": "Aluno não encontrado"}, 404

    try:
        db.session.delete(aluno)
        db.session.commit()
        return {"mensagem": "Aluno removido com sucesso"}, 200
    except Exception as e:
        db.session.rollback()
        return {"erro": str(e)}, 500