from professor.professor_model import get_professores, get_professor_id, post_professor, delete_professor, put_professor

def listar_professores():
    return get_professores()

def buscar_professor(professor_id):
    return get_professor_id(professor_id)

def criar_professor(dados):
    if not all(k in dados for k in ("nome", "data_nascimento", "disciplina", "salario")):
        return {"erro": "Dados incompletos"}, 400
    return post_professor(dados), 201

def remover_professor(professor_id):
    if delete_professor(professor_id):
        return {"mensagem": "Professor removido"}, 200
    return {"erro": "Professor não encontrado"}, 404

def atualizar_professor(professor_id, dados):
    professor_atualizado = put_professor(professor_id, dados)
    if professor_atualizado:
        return professor_atualizado, 200
    return {"erro": "Professor não encontrado"}, 404
