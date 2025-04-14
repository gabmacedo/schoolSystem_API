dados = {
    "alunos": [
        {"id": 1, "nome": "Gabriel", "turma_id": 1, "data_nascimento": "2010-05-14", "nota_primeiro_semestre": 8.5, "nota_segundo_semestre": 9.0, "media_final": 8.75},
        {"id": 2, "nome": "Guilherme", "turma_id": 2, "data_nascimento": "2009-08-22", "nota_primeiro_semestre": 7.0, "nota_segundo_semestre": 6.5, "media_final": 6.75},
        {"id": 3, "nome": "Davi", "turma_id": 1, "data_nascimento": "2010-08-09", "nota_primeiro_semestre": 8.0, "nota_segundo_semestre": 7.5, "media_final": 7.75},
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
    novo_aluno["media_final"] = (novo_aluno["nota_primeiro_semestre"] + novo_aluno["nota_segundo_semestre"]) / 2
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
    
    for campo in ["nome", "idade", "data_nascimento," "nota_primeiro_semestre", "nota_segundo_semestre", "turma_id" ]:
        if campo in novos_dados:
            aluno[campo] = novos_dados[campo]

    if "nt_prim_sem" in novos_dados or "nt_seg_sem" in novos_dados:
        aluno["media_final"] = (aluno["nota_primeiro_semestre"] + aluno["nota_segundo_semestre"]) / 2

    return aluno

    