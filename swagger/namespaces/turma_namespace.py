from flask_restx import Namespace, Resource, fields
from turma.turma_controller import listar_turmas, criar_turma, buscar_turma, atualizar_turma, remover_turma

turma_ns = Namespace("turmas", description="Operações relacionadas as turmas")

turma_model = turma_ns.model("Turma", {
    "nome": fields.String(required=True, description="Nome da turma"),
    "materia": fields.String(description="Materia da turma"),
    "descricao": fields.String(required=True, description="Descrição da Turma"),
    "ativo": fields.Boolean(required=True, description="Status da Turma"),
    "professor_id": fields.Integer(required=True, description="ID do professor pertencente a turma")
})


turma_output_model = turma_ns.model("TurmaOutput", {
    "id": fields.Integer(description="ID da turma"),
    "nome": fields.String(description="Nome da turma"),
    "materia": fields.String(description="Materia da turma"),
    "descricao": fields.String(description="Descrição da Turma"),
    "ativo": fields.Boolean(description="Status da Turma"),
    "professor_id": fields.Integer(description="ID do professor pertencente a turma")
})

@turma_ns.route("/")
class TurmaResource(Resource):
    @turma_ns.marshal_list_with(turma_output_model)
    def get(self):
        """Lista todas as turmas"""
        return listar_turmas()
    
    @turma_ns.expect(turma_model)
    def post(self):
        """Cria uma turma"""
        dados = turma_ns.payload
        return criar_turma(dados)
    
@turma_ns.route("/<int:id_turma>")
class TurmaIdResource(Resource):
    @turma_ns.marshal_with(turma_output_model)
    def get(self, id_turma):
        """Busca turma pelo ID"""
        return buscar_turma(id_turma)

    @turma_ns.expect(turma_model)
    def put(self, id_turma):
        """Atualiza turma por ID"""
        dados = turma_ns.payload
        return atualizar_turma(id_turma, dados)

    def delete(self, id_turma):
        """Deleta turma por ID"""
        remover_turma(id_turma)
        return {"message": "Turma excluida com sucesso!"}, 200