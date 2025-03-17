import unittest
import requests

class TestStringMethods(unittest.TestCase):

#============= TESTES PARA PROFESSOR ==============

    # 01. Criar professor com dados completos
    def teste_001_criar_professor_completo(self):
        response = requests.post(
            "http://127.0.0.1:5000/professores",
            json={
                "nome": "Maria",
                "data_nascimento": "1980-05-15",
                "disciplina": "História",
                "salario": 4500
            }
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())
        
    # 02. Criar professor sem dados
    def teste_002_criar_professor_sem_dados(self):
        response = requests.post("http://127.0.0.1:5000/professores", json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("erro", response.json())

    # 03. Listar todos os professores
    def teste_003_listar_professores(self):
        response = requests.get("http://127.0.0.1:5000/professores")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    # 04. Criar turma com professor válido
    def teste_004_criar_turma_com_professor_valido(self):
        response_professor = requests.post(
            "http://127.0.0.1:5000/professores",
            json={
                "nome": "Carlos",
                "data_nascimento": "1975-08-25",
                "disciplina": "Matemática",
                "salario": 5000
            }
        )
        professor_id = response_professor.json()["id"]

        response = requests.post(
            "http://127.0.0.1:5000/turmas",
            json={
                "nome": "Turma A",
                "turno": "Manhã",
                "professor_id": professor_id
            }
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())

#============= TESTES PARA TURMA ==============

    # 05. Criar turma sem professor
    def test_005_criar_turma_sem_professor(self):
        response = requests.post(
            "http://127.0.0.1:5000/turmas",
            json={
                "nome": "Turma A",
                "turno": "Manhã",
                "professor_id": 9999
            }
        )
        self.assertEqual(response.status_code, 404)
        self.assertIn("erro", response.json())

    # 06. Criar turma sem dados
    def test_006_criar_turma_sem_dados(self):
        response = requests.post("http://127.0.0.1:5000/turmas", json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("erro", response.json())

    # 07. Listar todas as turmas
    def test_007_listar_turmas(self):
        response = requests.get("http://127.0.0.1:5000/turmas")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

#============= TESTES PARA ALUNO ==============

    # 08. Criar aluno com dados completos
    def test_008_criar_aluno_completo(self):
        response_professor = requests.post(
        "http://127.0.0.1:5000/professores", 
        json={"nome": "Carlos", "data_nascimento": "1975-08-25", "disciplina": "Matemática", "salario": 5000})
        professor_id = response_professor.json()["id"]

        # Criar uma turma antes de criar o aluno
        response_turma = requests.post("http://127.0.0.1:5000/turmas",
        json={"nome": "Turma A", "turno": "Manhã", "professor_id": professor_id})
        turma_id = response_turma.json()["id"]

        # Criar aluno com a turma correta
        response = requests.post("http://127.0.0.1:5000/alunos", 
        json={"nome": "Gabriel", "data_nascimento": "2000-01-01", "nota_primeiro_semestre": 9.0, "nota_segundo_semestre": 8.5, "turma_id": turma_id})
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())
        response = requests.post(
            "http://127.0.0.1:5000/alunos",
            json={
                "nome": "Gabriel",
                "data_nascimento": "2000-01-01",
                "nota_primeiro_semestre": 9.0,
                "nota_segundo_semestre": 8.5,
                "turma_id": 1
            }
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())

    # 09. Criar aluno sem dados
    def test_009_criar_aluno_sem_dados(self):
        response = requests.post("http://127.0.0.1:5000/alunos", json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("erro", response.json())

    # 010. Listar todos os alunos
    def test_010_listar_alunos(self):
        response = requests.get("http://127.0.0.1:5000/alunos")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    # 011. Obter aluno por ID inexistente
    def test_011_obter_aluno_inexistente(self):
        response = requests.get("http://127.0.0.1:5000/alunos/99")
        self.assertEqual(response.status_code, 404)
        self.assertIn("erro", response.json())

    # 012. Atualizar aluno inexistente
    def test_012_atualizar_aluno_inexistente(self):
        response = requests.put(
            "http://127.0.0.1:5000/alunos/99",
            json={"nome": "Atualizado"}
        )
        self.assertEqual(response.status_code, 404)
        self.assertIn("erro", response.json())

    # 013. Excluir aluno inexistente
    def test_013_excluir_aluno_inexistente(self):
        response = requests.delete("http://127.0.0.1:5000/alunos/99")
        self.assertEqual(response.status_code, 404)
        self.assertIn("erro", response.json())

    # 014. Atualizar turma existente
    def test_015_atualizar_turma_existente(self):
        # Cria um professor primeiro
        response_professor = requests.post(
            "http://127.0.0.1:5000/professores",
            json={"nome": "Carlos", "data_nascimento": "1975-08-25", "disciplina": "Matemática", "salario": 5000}
        )
        professor_id = response_professor.json()["id"]

        # Cria uma turma
        response_turma = requests.post(
            "http://127.0.0.1:5000/turmas",
            json={"nome": "Turma A", "turno": "Manhã", "professor_id": professor_id}
        )
        turma_id = response_turma.json()["id"]

        # Atualiza a turma
        response_atualizacao = requests.put(
            f"http://127.0.0.1:5000/turmas/{turma_id}",
            json={"nome": "Turma Atualizada", "turno": "Tarde", "professor_id": professor_id}
        )
        self.assertEqual(response_atualizacao.status_code, 200)
        self.assertEqual(response_atualizacao.json()["nome"], "Turma Atualizada")
        self.assertEqual(response_atualizacao.json()["turno"], "Tarde")

    # 015. Excluir aluno existente
    def test_014_excluir_aluno_existente(self):
        # Cria um professor
        response_professor = requests.post(
            "http://127.0.0.1:5000/professores",
            json={"nome": "Carlos", "data_nascimento": "1975-08-25", "disciplina": "Matemática", "salario": 5000}
        )
        professor_id = response_professor.json()["id"]

        # Cria uma turma
        response_turma = requests.post(
            "http://127.0.0.1:5000/turmas",
            json={"nome": "Turma A", "turno": "Manhã", "professor_id": professor_id}
        )
        turma_id = response_turma.json()["id"]
        
        # Cria um aluno 
        response_aluno = requests.post(
            "http://127.0.0.1:5000/alunos",
            json={"nome": "Gabriel", "data_nascimento": "2000-01-01", "nota_primeiro_semestre": 9.0, "nota_segundo_semestre": 8.5, "turma_id": turma_id}
        )
        aluno_id = response_aluno.json()["id"]

if __name__ == "__main__":
    unittest.main()