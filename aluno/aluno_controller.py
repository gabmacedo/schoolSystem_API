from .aluno_model import get_alunos, get_alunos_id, post_aluno, delete_aluno, put_aluno

def listar_alunos():
    return get_alunos()

def buscar_aluno(aluno_id):
    return get_alunos_id(aluno_id)

def criar_aluno(dados):
    if not all(k in dados for k in ("nome", "idade", "data_nascimento", "nt_prim_sem", "nt_seg_sem", "turma_id")):
        return {"erro": "Dados incompletos"}, 400
    return post_aluno(dados), 201

def remover_aluno(aluno_id):
    if delete_aluno(aluno_id):
        return {"mensagem": "Aluno removido"}, 200
    return {"erro": "Aaluno não encontrado"}, 404

def atualizar_aluno(aluno_id, dados):
    aluno_atualizado = put_aluno(aluno_id, dados)
    if aluno_atualizado:
        return aluno_atualizado, 200
    return {"erro": "Aluno não encontrado"}, 404