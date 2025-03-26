from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados em listas
alunos = []
professores = []
turmas = []

# Contadores para ID
aluno_id_counter = 1
professor_id_counter = 1
turma_id_counter = 1

#======================Aluno===============================
@app.route('/alunos', methods=['POST'])
def criar_aluno():
    global aluno_id_counter
    dados = request.get_json()
    if not all(k in dados for k in ("nome", "data_nascimento", "nota_primeiro_semestre", "nota_segundo_semestre", "turma_id")):
        return jsonify({"erro": "Dados incompletos"}), 400
    if not any(t["id"] == dados["turma_id"] for t in turmas):
        return jsonify({"erro": "Turma não encontrada"}), 404
    aluno = {
        "id": aluno_id_counter,
        "nome": dados["nome"],
        "data_nascimento": dados["data_nascimento"],
        "nota_primeiro_semestre": dados["nota_primeiro_semestre"],
        "nota_segundo_semestre": dados["nota_segundo_semestre"],
        "turma_id": dados["turma_id"],
        "media_final": (dados["nota_primeiro_semestre"] + dados["nota_segundo_semestre"]) / 2
    }
    alunos.append(aluno)
    aluno_id_counter += 1
    return jsonify(aluno), 201

@app.route('/alunos', methods=['GET'])
def listar_alunos():
    return jsonify(alunos)

@app.route('/alunos/<int:aluno_id>', methods=['GET'])
def obter_aluno(aluno_id):
    aluno = next((a for a in alunos if a["id"] == aluno_id), None)
    if aluno is None:
        return jsonify({"erro": "Aluno não encontrado"}), 404
    return jsonify(aluno)

@app.route('/alunos/<int:aluno_id>', methods=['PUT'])
def atualizar_aluno(aluno_id):
    dados = request.get_json()
    aluno = next((a for a in alunos if a["id"] == aluno_id), None)
    if aluno is None:
        return jsonify({"erro": "Aluno não encontrado"}), 404
    for key in ["nome", "data_nascimento", "nota_primeiro_semestre", "nota_segundo_semestre", "turma_id"]:
        if key in dados:
            aluno[key] = dados[key]
    aluno["media_final"] = (aluno["nota_primeiro_semestre"] + aluno["nota_segundo_semestre"]) / 2
    return jsonify(aluno)

@app.route('/alunos/<int:aluno_id>', methods=['DELETE'])
def excluir_aluno(aluno_id):
    global alunos
    aluno = next((a for a in alunos if a["id"] == aluno_id), None)
    if aluno is None:
        return jsonify({"erro": "Aluno não encontrado"}), 404
    alunos = [a for a in alunos if a["id"] != aluno_id]
    return jsonify({"mensagem": "Aluno excluído"}), 200

#======================Professor===============================
@app.route('/professores', methods=['POST'])
def criar_professor():
    global professor_id_counter
    dados = request.get_json()
    if not all(k in dados for k in ("nome", "data_nascimento", "disciplina", "salario")):
        return jsonify({"erro": "Dados incompletos"}), 400
    professor = {
        "id": professor_id_counter,
        "nome": dados["nome"],
        "data_nascimento": dados["data_nascimento"],
        "disciplina": dados["disciplina"],
        "salario": dados["salario"]
    }
    professores.append(professor)
    professor_id_counter += 1
    return jsonify(professor), 201

@app.route('/professores', methods=['GET'])
def listar_professores():
    return jsonify(professores)

@app.route('/professores/<int:professor_id>', methods=['GET'])
def obter_professor(professor_id):
    professor = next((p for p in professores 
                      if p["id"] == professor_id), None)
    
    if professor is None:
        return jsonify({"erro": "Professor não encontrado"}), 404
    return jsonify(professor)

@app.route('/professores/<int:professor_id>', methods=['PUT'])
def atualizar_professor(professor_id):
    dados = request.get_json()
    professor = next((p for p in professores if p["id"] == professor_id), None)

    if professor is None:
        return jsonify

    if "nome" in dados:
        professor["nome"] = dados["nome"]
    if "data_nascimento" in dados:
        professor["data_nascimento"] = dados["data_nascimento"]
    if "disciplina" in dados:
        professor["disciplina"] = dados["disciplina"]
    if "salario" in dados:
        try:
            professor["salario"] = float(dados["salario"])
        except ValueError:
            return jsonify({"erro": "O salario deve ser um número"}), 400
        
    return jsonify(professor), 200

@app.route('/professores/<int:professor_id>', methods=['DELETE'])
def excluir_professor(professor_id):
    global professores
    professor = next((p for p in professores 
                      if p["id"] == professor_id), None)
    
    if professor is None:
        return jsonify({"erro": "Professor não encontrado"}), 404
    
    professores = [p for p in professores
                   if p["id"] != professor_id]
    
    for turma in turmas:
        if turma["professor_id"] == professor_id:
            turma["professor_id"] = None

    return jsonify({"mensagem": "Professor excluido com sucesso"}), 200
    
#======================Turma===============================
@app.route('/turmas', methods=['POST'])
def criar_turma():
    global turma_id_counter
    dados = request.get_json()

    if not all(k in dados for k in ("nome", "turno", "professor_id")):
        return jsonify({"erro": "Dados incompletos"}), 400
    
    if not any(p["id"] == dados["professor_id"] for p in professores):
        return jsonify({"erro": "Professor não encontrado"}), 404
    
    turma = {
        "id": turma_id_counter,
        "nome": dados["nome"],
        "turno": dados["turno"],
        "professor_id": dados["professor_id"]
    }
    
    turmas.append(turma)
    turma_id_counter += 1
    
    return jsonify(turma), 201

@app.route('/turmas', methods=['GET'])
def listar_turmas():
    return jsonify(turmas)

@app.route("/turmas/<int:turma_id>", methods=['GET'])
def obter_turmas(turma_id):
    turma = next((t for t in turmas if t["id"] == turma_id), None)
    if turma is None:
        return jsonify({"erro": "Turma não encontrada"}), 404
    return jsonify(turma)

@app.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    dados = request.get_json()
    turma = next((t for t in turmas if t["id"] == id), None)
    if turma is None:
        return jsonify({"erro": "Turma não encontrada"}), 404

    if "nome" in dados:
        turma["nome"] = dados["nome"]
    if "turno" in dados:
        turma["turno"] = dados["turno"]
    if "professor_id" in dados:
        turma["professor_id"] = dados["professor_id"]

    return jsonify(turma), 200

@app.route('/turmas/<int:id>', methods=['DELETE'])
def excluir_turma(id):
    global turmas
    turma = next((t for t in turmas if t["id"] == id), None)
    if turma is None:
        return jsonify({"erro": "Turma não encontrada"}), 404
    turmas = [t for t in turmas if t["id"] != id]
    return jsonify({"mensagem": "Turma excluída com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)
