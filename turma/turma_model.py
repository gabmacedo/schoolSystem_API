dados = {
    "turmas": [
        {"id": 1, "nome": "1º Ano A", "turno": "Manhã", "professor_id": 1},
        {"id": 2, "nome": "2º Ano B", "turno": "Tarde", "professor_id": 2}
    ],
    "contador": {
        "turma_id": 3
    }
}

def get_turmas():
    return dados["turmas"]

def get_turma_id(turma_id):
    for turma in dados["turmas"]:
        if turma["id"] == turma_id:
            return turma
    return None

def post_turma(nova_turma):
    nova_turma["id"] = dados["contador"]["turma_id"]
    dados["turmas"].append(nova_turma)
    dados["contador"]["turma_id"] += 1
    return nova_turma

def delete_turma(turma_id):
    turma = get_turma_id(turma_id)
    if turma:
        dados["turmas"].remove(turma)
        return True
    return False

def put_turma(turma_id, novos_dados):
    turma = get_turma_id(turma_id)
    if turma is None:
        return None

    for campo in ["nome", "turno", "professor_id"]:
        if campo in novos_dados:
            turma[campo] = novos_dados[campo]

    return turma
