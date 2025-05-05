from flask import request, jsonify
from config import db
from turma.turma_model import Turma
from professor.professor_model import Professor

def listar_turmas():
    turmas = Turma.query.all()
    return jsonify([t.to_dict() for t in turmas]), 200

def buscar_turma(turma_id):
    turma = Turma.query.get(turma_id)
    if turma:
        return jsonify(turma.to_dict()), 200
    return jsonify({"erro": "Turma não encontrada"}), 404

def criar_turma():
    dados = request.get_json()  # <-- agora ela busca os dados internamente
    campos_obrigatorios = ['nome', 'descricao', 'ativo', 'professor_id']
    for campo in campos_obrigatorios:
        if campo not in dados:
            return {"erro": f"Campo obrigatório '{campo}' não enviado"}, 400

    professor = Professor.query.get(dados['professor_id'])
    if not professor:
        return {"erro": "Professor não encontrado"}, 404

    try:
        print("Dados recebidos para criar a turma:", dados)

        nova_turma = Turma(
            nome=dados['nome'],
            descricao=dados['descricao'],
            ativo=dados['ativo'],
            professor_id=dados['professor_id']
        )

        db.session.add(nova_turma)
        db.session.commit()

        turma_salva = Turma.query.get(nova_turma.id)
        print("Turma salva no banco após commit:", turma_salva.to_dict())

        return turma_salva.to_dict(), 201
    except Exception as e:
        db.session.rollback()
        return {"erro": str(e)}, 500

def atualizar_turma(turma_id):
    turma = Turma.query.get(turma_id)
    if not turma:
        return jsonify({"erro": "Turma não encontrada"}), 404

    dados = request.get_json()

    try:
        if 'nome' in dados:
            turma.nome = dados['nome']
        if 'descricao' in dados:
            turma.descricao = dados['descricao']
        if 'ativo' in dados:
            turma.ativo = dados['ativo']
        if 'professor_id' in dados:
            turma.professor_id = dados['professor_id']

        db.session.commit()
        return jsonify(turma.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500

def remover_turma(turma_id):
    turma = Turma.query.get(turma_id)
    if not turma:
        return jsonify({"erro": "Turma não encontrada"}), 404

    try:
        db.session.delete(turma)
        db.session.commit()
        return jsonify({"mensagem": "Turma removida com sucesso"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500
