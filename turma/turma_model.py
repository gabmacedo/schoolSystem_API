from config import db

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    materia = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'materia': self.materia,
            'descricao': self.descricao,
            'ativo': self.ativo,
            'professor_id': self.professor_id
        }