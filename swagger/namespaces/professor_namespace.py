from flask_restx import Namespace, Resource, fields
from professor.professor_controller import listar_professores, criar_professor, buscar_professor, atualizar_professor, remover_professor

professores_ns = Namespace("professores", description="Operações relacionadas aos professores")

professor_model = professores_ns.model("Professor", {
    "nome": fields.String(required=True, description="Nome do professor"),
    "data_nascimento": fields.String(required=True, description="Data de nascimento (YYYY-MM-DD)"),
    "disciplina": fields.String(required=True, description="Disciplina ensinada"),
    "salario": fields.Float(required=True, description="Salário")
})

professor_output_model = professores_ns.model("ProfessorOutput", {
    "id": fields.Integer(description="ID do professor"),
    "nome": fields.String(description="Nome do professor"),
    "idade": fields.Integer(description="Idade do professor"),
    "disciplina": fields.String(description="Disciplina"),
    "salario": fields.Float(description="Salário")
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
        data = professores_ns.payload
        return criar_professor(data)
    
@professores_ns.route("/<int:id_professor>")    
class ProfessorIdResource(Resource):
    @professores_ns.marshal_with(professor_output_model)
    def get(self, id_professor):
        """Busca um professor por ID"""
        return buscar_professor(id_professor)
    
    @professores_ns.expect(professor_model)
    def put(self, id_professor):
        """Atualiza um professo"""
        data = professores_ns.payload
        atualizar_professor(id_professor, data)
        return buscar_professor(id_professor), 200
    
    def delete(self, id_professor):
        """Deleta um professor"""
        remover_professor(id_professor)
        return {"message": "Professor excluido com sucesso"}, 200