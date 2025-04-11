dados = {
    "alunos": [
        {"id": 1, "nome": "Gabriel", "idade": 14, "turma_id": 1, "data_nascimento": "2010-05-14", "nt_prim_sem": 8.5, "nt_seg_sem": 9.0, "media_final": 8.75},
        {"id": 2, "nome": "Guilherme", "idade": 15, "turma_id": 2, "data_nascimento": "2009-08-22", "nt_prim_sem": 7.0, "nt_seg_sem": 6.5, "media_final": 6.75},
        {"id": 3, "nome": "Davi", "idade": 14, "turma_id": 1, "data_nascimento": "2010-08-09", "nt_prim_sem": 8.0, "nt_seg_sem": 7.5, "media_final": 7.75},
    ],
    "contador": {
        "aluno_id": 4
    }
    
}


def get_alunos():
    return dados["alunos"]

def get_alunos_id(aluno_id):
    for aluno in dados["alunos"]:
        if aluno["id"] == aluno_id:
            return aluno
    return None

def post_aluno(novo_aluno):
    novo_aluno["id"] = dados["contador"]["aluno_id"]
    novo_aluno["media_final"] = (novo_aluno["nt_prim_sem"] + novo_aluno["nt_seg_sem"]) / 2
    dados["alunos"].append(novo_aluno)
    dados["contador"]["aluno_id"] += 1
    return novo_aluno

def delete_aluno(aluno_id):
    aluno = get_alunos_id(aluno_id)
    if aluno:
        dados["alunos"].remove(aluno)
        return True
    return False

def put_aluno(aluno_id, novos_dados):
    aluno = get_alunos_id(aluno_id)
    if aluno is None:
        return None
    
    for campo in ["nome", "idade", "data_nascimento," "nt_prim_sem", "nt_seg_sem", "turma_id" ]:
        if campo in novos_dados:
            aluno[campo] = novos_dados[campo]

    if "nt_prim_sem" in novos_dados or "nt_seg_sem" in novos_dados:
        aluno["media_final"] = (aluno["nt_prim_sem"] + aluno["nt_seg_sem"]) / 2

    return aluno

    