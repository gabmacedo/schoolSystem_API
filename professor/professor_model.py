dados = {
    "professores": [
        {"id": 1, "nome": "Carlos", "idade": 40, "disciplina": "Matemática", "data_admissao": "2010-03-15", "turma_id": 1},
        {"id": 2, "nome": "Ana", "idade": 35, "disciplina": "Português", "data_admissao": "2012-07-10", "turma_id": 2},
    ],
    "contador": {
        "professor_id": 3
    }
}

def get_professores():
    return dados["professores"]

def get_professor_id(professor_id):
    for professor in dados["professores"]:
        if professor["id"] == professor_id:
            return professor
    return None

def post_professor(novo_professor):
    novo_professor["id"] = dados["contador"]["professor_id"]
    dados["professores"].append(novo_professor)
    dados["contador"]["professor_id"] += 1
    return novo_professor

def delete_professor(professor_id):
    professor = get_professor_id(professor_id)
    if professor:
        dados["professores"].remove(professor)
        return True
    return False

def put_professor(professor_id, novos_dados):
    professor = get_professor_id(professor_id)
    if professor is None:
        return None

    for campo in ["nome", "idade", "disciplina", "data_admissao", "turma_id"]:
        if campo in novos_dados:
            professor[campo] = novos_dados[campo]

    return professor
