from flask import Flask
from aluno.aluno_routes import aluno_bp
#from professor.professor_routes import professor_bp
#from turmas.turmas_routes import turmas_bp 


app = Flask(__name__)


app.register_blueprint(aluno_bp, url_prefix='/alunos')
#app.register_blueprint(professor_bp, url_prefix='/professores')
#app.register_blueprint(turma_bp, url_prefix='/turmas')

if __name__ == '__main__':
    app.run(debug=True)