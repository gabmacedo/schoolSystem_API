import unittest
import requests

class TestStringMethods(unittest.TestCase):

    #============= TESTES PARA PROFESSOR ==============

    # 01. Criar professor com dados completos
    def test_001_criar_professor_completo(self):
        response = requests.post(
            "http://127.0.0.1:5050/professores",
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
    def test_002_criar_professor_sem_dados(self):
        response = requests.post("http://127.0.0.1:5050/professores", json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("erro", response.json())

    # 03. Listar todos os professores
    def test_003_listar_professores(self):
        response = requests.get("http://127.0.0.1:5050/professores")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    # 04. Criar turma com professor válido
    def test_004_criar_turma_com_professor_valido(self):
        response_professor = requests.post(
            "http://127.0.0.1:5050/professores",
            json={
                    "nome": "Caio",
                    "materia": "Desenvolvimento de API's",
                    "observacoes": "Professor experiente",
                    "idade": 25
                }
        )
        self.assertEqual(response_professor.status_code, 201)
        professor_id = response_professor.json().get("id")
        self.assertIsNotNone(professor_id)

        response = requests.post(
            "http://127.0.0.1:5050/turmas",
            json={
                    "nome": "Turma de S.I",
                    "materia": "Desenvolvimento de API's",
                    "descricao": "Turma do primeiro semestre",
                    "ativo": True,
                    "professor_id": 1
                }
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())

    # 05. Atualizar professor existente
    def test_005_atualizar_professor_existente(self):
        response_professor = requests.post(
            "http://127.0.0.1:5050/professores",
            json={
                    "nome": "Caio",
                    "materia": "Desenvolvimento de API's",
                    "observacoes": "Professor experiente",
                    "idade": 25
                }
        )
        professor_id = response_professor.json()["id"]

        # Atualizar professor
        response_atualizacao = requests.put(
            f"http://127.0.0.1:5050/professores/{professor_id}",
            json={
                "nome": "Caio Prado", 
                "disciplina": "Desenvolvimento Web", 
                }
        )
        self.assertEqual(response_atualizacao.status_code, 200)
        self.assertEqual(response_atualizacao.json()["nome"], "Caio Prado")
        self.assertEqual(response_atualizacao.json()["disciplina"], "Desenvolvimento Web")

    # 06. Excluir professor existente
    def test_006_excluir_professor_existente(self):
        response_professor = requests.post(
            "http://127.0.0.1:5050/professores",
            json={
                    "nome": "Caio",
                    "materia": "Desenvolvimento de API's",
                    "observacoes": "Professor experiente",
                    "idade": 25
                }
        )
        professor_id = response_professor.json()["id"]

        response_delete = requests.delete(f"http://127.0.0.1:5050/professores/{professor_id}")
        self.assertEqual(response_delete.status_code, 200)

        response_get = requests.get(f"http://127.0.0.1:5050/professores/{professor_id}")
        self.assertEqual(response_get.status_code, 404)

    #============= TESTES PARA TURMA ==============

    # 07. Criar turma sem professor
    def test_007_criar_turma_sem_professor(self):
        response = requests.post(
            "http://127.0.0.1:5050/turmas",
            json={
                    "nome": "Turma de A.D.S",
                    "materia": "DevOps",
                    "descricao": "Turma do segundo semestre",
                    "ativo": True,
                    "professor_id": 99
                }
        )
        self.assertEqual(response.status_code, 404)
        self.assertIn("erro", response.json())

    # 08. Criar turma sem dados
    def test_008_criar_turma_sem_dados(self):
        response = requests.post("http://127.0.0.1:5050/turmas", json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("erro", response.json())

    # 09. Listar todas as turmas
    def test_009_listar_turmas(self):
        response = requests.get("http://127.0.0.1:5050/turmas")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    # 10. Atualizar turma existente
    def test_010_atualizar_turma_existente(self):
        response_professor = requests.post(
            "http://127.0.0.1:5050/professores",
            json={
                    "nome": "Hebert",
                    "materia": "DevOps",
                    "observacoes": "Afastado em viagem.",
                    "idade": 31
                }

        )
        professor_id = response_professor.json()["id"]

        response_turma = requests.post(
            "http://127.0.0.1:5050/turmas",
            json={
                    "nome": "Turma de S.I",
                    "materia": "DevOps",
                    "descricao": "Turma do primeiro semestre",
                    "ativo": True,
                    "professor_id": 1
                }
        )
        turma_id = response_turma.json()["id"]

        response_atualizacao = requests.put(
            f"http://127.0.0.1:5050/turmas/{turma_id}",
            json={
                    "nome": "Turma de S.I",
                    "materia": "DevOps",
                    "descricao": "Turma do segundo semestre",
                    "ativo": True,
                    "professor_id": 1
                }
        )
        self.assertEqual(response_atualizacao.status_code, 200)
        self.assertEqual(response_atualizacao.json()["descricao"], "Turma do segundo semestre")

    # 11. Excluir turma existente
    def test_011_excluir_turma_existente(self):
        # Criar professor
        response_professor = requests.post(
            "http://127.0.0.1:5050/professores",
            json={
                    "nome": "Hebert",
                    "materia": "DevOps",
                    "observacoes": "Afastado em viagem.",
                    "idade": 31
                }
        )
        professor_id = response_professor.json()["id"]

        # Criar turma
        response_turma = requests.post(
            "http://127.0.0.1:5050/turmas",
            json={
                    "nome": "Turma de S.I",
                    "materia": "Desenvolvimento de API's",
                    "descricao": "Turma do primeiro semestre",
                    "ativo": True,
                    "professor_id": 1
                }
        )
        turma_id = response_turma.json()["id"]

        # Excluir turma
        response_delete = requests.delete(f"http://127.0.0.1:5050/turmas/{turma_id}")
        self.assertEqual(response_delete.status_code, 200)

        response_get = requests.get(f"http://127.0.0.1:5050/turmas/{turma_id}")
        self.assertEqual(response_get.status_code, 404)

    #============= TESTES PARA ALUNO ==============

    # 12. Criar aluno com dados completos
    def test_012_criar_aluno_completo(self):
        response_professor = requests.post(
            "http://127.0.0.1:5050/professores",
            json={
                    "nome": "Caio",
                    "materia": "Desenvolvimento de API's",
                    "observacoes": "Professor experiente",
                    "idade": 25
                }
        )

        # Criar uma turma antes de criar o aluno
        response_turma = requests.post(
            "http://127.0.0.1:5050/turmas",
            json={
                "nome": "Turma de S.I",
                "materia": "Desenvolvimento de API's",
                "descricao": "Turma do primeiro semestre",
                "ativo": True,
                "professor_id": 1
            }
        )

        # Criar aluno com a turma correta
        response = requests.post(
            "http://127.0.0.1:5050/alunos",
            json={
                    "nome": "Gabriel Macedo",
                    "data_nascimento": "2005-08-28",
                    "nota_primeiro_semestre": 9,
                    "nota_segundo_semestre": 7.5,
                    "turma_id": 1
                }
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())

    # 13. Criar aluno sem dados
    def test_013_criar_aluno_sem_dados(self):
        response = requests.post("http://127.0.0.1:5050/alunos", json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("erro", response.json())

    # 14. Listar todos os alunos
    def test_014_listar_alunos(self):
        response = requests.get("http://127.0.0.1:5050/alunos")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    # 15. Obter aluno por ID inexistente
    def test_015_obter_aluno_inexistente(self):
        response = requests.get("http://127.0.0.1:5050/alunos/99")
        self.assertEqual(response.status_code, 404)
        self.assertIn("erro", response.json())

    # 16. Atualizar aluno inexistente
    def test_016_atualizar_aluno_inexistente(self):
        response = requests.put(
            "http://127.0.0.1:5050/alunos/99",
            json={"nome": "Atualizado"}
        )
        self.assertEqual(response.status_code, 404)
        self.assertIn("erro", response.json())

if __name__ == '__main__':
    unittest.main()
