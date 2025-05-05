from config import db
from datetime import date

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    materia = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.String(255), nullable=True)
    idade = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "materia": self.materia,
            "observacoes": self.observacoes,
            "idade": self.idade
        }
