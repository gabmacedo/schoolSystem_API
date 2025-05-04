from config import db
from datetime import date

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)
    disciplina = db.Column(db.String(100), nullable=False)
    salario = db.Column(db.Float, nullable=False)

    def calcular_idade(self):
        ano, mes, dia = map(int, self.data_nascimento.split('-'))
        hoje = date.today()
        idade = hoje.year - ano - ((hoje.month, hoje.day) < (mes, dia))
        return idade

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.calcular_idade(),
            "disciplina": self.disciplina,
            "salario": self.salario
        }
