from flask_restx import Namespace, Resource, fields
from professor.professor_controller import listar_professores, criar_professor, buscar_professor, atualizar_professor, remover_professor

professores_ns = Namespace("professores", description="Operações relacionadas aos professores")

professor_model = professores_ns.model("Professor", {
    "nome": fields.String(required=True, description="Nome do professor"),
    "materia": fields.String(required=True, description="Materia do professor"),
    "observacoes": fields.String(required=True, description="Observações sobre o professor"),
    "idade": fields.Integer(required=True, description="Idade do professor")
})

professor_output_model = professores_ns.model("ProfessorOutput", {
    "id": fields.Integer(description="ID do professor"),
    "nome": fields.String(description="Nome do professor"),
    "materia": fields.String(description="Matéria lecionada"),
    "observacoes": fields.String(description="Observações sobre o professor"),
    "idade": fields.Integer(description="Idade do professor")
})

@professores_ns.route("/")
class ProfessoresResource(Resource):
    @professores_ns.marshal_list_with(professor_output_model)
    def get(self):
        """Lista todos os professores"""
        return listar_professores()
    
    @professores_ns.expect(professor_model)
    def post(self):
        """Cria um professor"""
        dados = professores_ns.payload
        return criar_professor(dados)
    
@professores_ns.route("/<int:id_professor>")    
class ProfessorIdResource(Resource):
    @professores_ns.marshal_with(professor_output_model)
    def get(self, id_professor):
        """Busca professor por ID"""
        return buscar_professor(id_professor)
    
    @professores_ns.expect(professor_model)
    def put(self, id_professor):
        """Atualiza professor por ID"""
        dados = professores_ns.payload
        atualizar_professor(id_professor, dados)
        return buscar_professor(id_professor), 200
    
    def delete(self, id_professor):
        """Deleta professor por ID"""
        remover_professor(id_professor)
        return {"message": "Professor excluido com sucesso!"}, 200