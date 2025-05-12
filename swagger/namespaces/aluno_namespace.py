from flask_restx import Namespace, Resource, fields
from aluno.aluno_controller import listar_alunos, criar_aluno, buscar_aluno, atualizar_aluno, remover_aluno

alunos_ns = Namespace("alunos", description="Operações relacionadas aos alunos")

aluno_model = alunos_ns.model("Aluno", {
    "nome": fields.String(required=True),
    "data_nascimento": fields.String(required=True),
    "nota_primeiro_semestre": fields.Float(required=True),
    "nota_segundo_semestre": fields.Float(required=True),
    "turma_id": fields.Integer(required=True)
})

aluno_output_model = alunos_ns.inherit("AlunoOutput", aluno_model, {
    "id": fields.Integer(description='ID do aluno'),
    "nome": fields.String(description='Nome do aluno'),
    "idade": fields.Integer(description='Idade do aluno'),
    "data_nascimento": fields.String(description='Data de nascimento do aluno'),
    "nota_primeiro_semestre": fields.Float(description='Nota primeiro semestre'),
    "nota_segundo_semestre": fields.Float(description='Nota segundo semestre'),
    "media_final": fields.Float(description='Média do aluno'),
    "turma_id": fields.Integer(description='ID da turma')
})

@alunos_ns.route("/")
class AlunoResource(Resource):
    @alunos_ns.marshal_list_with(aluno_output_model)
    def get(self):
        """Lista todos os alunos"""
        alunos, _ = listar_alunos()
        return alunos

    @alunos_ns.expect(aluno_model)
    def post(self):
        """Cria um novo aluno"""
        dados = alunos_ns.payload
        response, status = criar_aluno(dados)
        return response, status

@alunos_ns.route("/<int:aluno_id>")
class AlunoIdResource(Resource):
    @alunos_ns.marshal_with(aluno_output_model)
    def get(self, aluno_id):
        """Busca aluno por ID"""
        return buscar_aluno(aluno_id)

    @alunos_ns.expect(aluno_model)
    def put(self, aluno_id):
        """Atualiza aluno por ID"""
        dados = alunos_ns.payload
        atualizar_aluno(aluno_id, dados)
        return buscar_aluno(aluno_id), 200

    def delete(self, aluno_id):
        """Deleta aluno por ID"""
        remover_aluno(aluno_id)
        return {"message": "Aluno excluido com sucesso!"}, 200 

