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
    "id": fields.Integer(),
    "idade": fields.Integer(),
    "media_final": fields.Float()
})

@alunos_ns.route("/")
class AlunoList(Resource):
    @alunos_ns.marshal_list_with(aluno_output_model)
    def get(self):
        """Lista todos os alunos"""
        alunos, _ = listar_alunos()
        return alunos

    @alunos_ns.expect(aluno_model)
    def post(self):
        """Cria um novo aluno"""
        data = alunos_ns.payload
        response, status = criar_aluno(data)
        return response, status

@alunos_ns.route("/<int:aluno_id>")
class AlunoDetail(Resource):
    @alunos_ns.marshal_with(aluno_output_model)
    def get(self, aluno_id):
        """Busca aluno por ID"""
        return buscar_aluno(aluno_id)

    @alunos_ns.expect(aluno_model)
    def put(self, aluno_id):
        """Atualiza aluno"""
        data = alunos_ns.payload
        return atualizar_aluno(aluno_id)

    def delete(self, aluno_id):
        """Deleta aluno"""
        return remover_aluno(aluno_id)
