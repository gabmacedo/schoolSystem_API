from flask import Flask
from config import db
from aluno.aluno_routes import aluno_bp
from professor.professor_routes import professor_bp
from turma.turma_routes import turma_bp
from swagger.swagger_config import configure_swagger
import os

app = Flask(__name__)

# Configuração do Flask
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 5050
app.config['DEBUG'] = True

# Inicializa o db com a app configurada
db.init_app(app)
configure_swagger(app)

# Registrando Blueprints
app.register_blueprint(aluno_bp, url_prefix='/alunos')
app.register_blueprint(professor_bp, url_prefix='/professores')
app.register_blueprint(turma_bp, url_prefix='/turmas')

# Criando as tabelas
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])
