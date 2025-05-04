# 🏫 Gestão de Alunos, Professores e Turmas - API Flask

Este projeto é uma API RESTful desenvolvida com **Flask**, focada na gestão de alunos, professores e turmas. Ele implementa operações CRUD para cada entidade e segue os princípios do TDD (Test-Driven Development). Ideal para fins acadêmicos e prática de arquitetura MVC.

## 🚀 Funcionalidades

✅ Cadastro, listagem, busca, atualização e exclusão de alunos  
✅ Suporte a endpoints para professores e turmas  
✅ Organização no padrão MVC  
✅ Testes unitários com unittest  
✅ Documentação automática com Swagger  
✅ Banco de dados SQLite com SQLAlchemy  
✅ Deploy na plataforma Render  
✅ Suporte a Docker  

## 🛠 Tecnologias Utilizadas

- **🐍 Python**
- **🌐 Flask**
- **🗃️ Flask SQLAlchemy**
- **🧩 SQLite**
- **📄 Swagger (flask-restx)**
- **🐳 Docker**
- **🚀 Render (Deploy)**
- **🧪 unittest**
- **📬 requests**

## 📁 Estrutura do Projeto
O projeto está organizado da seguinte forma:  
📂 SchoolSystem_DevAPI  
 ┣ 📂 aluno  
 ┃ ┣ 📄 aluno_controller.py  
 ┃ ┣ 📄 aluno_model.py  
 ┃ ┗ 📄 aluno_routes.py  
 ┣ 📂 professor  
 ┃ ┣ 📄 professor_controller.py  
 ┃ ┣ 📄 professor_model.py  
 ┃ ┗ 📄 professor_routes.py  
 ┣ 📂 turma  
 ┃ ┣📄 turma_controller.py  
 ┃ ┣📄 turma_model.py  
 ┃ ┗📄 turma_routes.py  
 ┣📄app.py  
 ┣📄config.py  
 ┣📄Dockerfile  
 ┣📄teste_app.py  
 ┣📄requirements.txt

## 📚 Documentação Swagger
Acesse a documentação interativa:

- Local:  
  http://localhost:5050/apidocs

- Render:  
  https://api-de-gestao-escolar.onrender.com/apidocs

## ▶️ Executando a Aplicação
Via Docker:
```bash
docker build -t school-system-api .
docker run -p 5050:5050 school-system-api
```

Sem Docker:
```bash
pip install -r requirements.txt
python app.py
```
## 🌐 Endpoints Principais

<b>Alunos</b><br>
<ul>
<li>POST /alunos<br></li>
<li>GET /alunos<br></li>
<li>PUT /alunos/<id><br></li>
<li>DELETE /alunos/<id><br></li>
</ul>

<b>Turmas</b><br>
<ul>
<li>POST /turmas<br></li>
<li>GET /turmas<br></li>
<li>PUT /turmas/<id><br></li>
<li>DELETE /turmas/<id><br></li>
</ul>

<b>Professores</b><br>
<ul>
<li>POST /professores<br></li>
<li>GET /professores<br></li>
<li>PUT /professores/<id><br></li>
<li>DELETE /professores/<id><br></li>
</ul>

## 🎯 Observações
- Agora o projeto utiliza banco de dados SQLite, armazenado em <code>/instance/app.db</code><br>
- A aplicação está hospedada em produção com o Render.

 <h1>👥 Colaboradores</h1>

- <a href="https://github.com/gabmacedo">Gabriel Aparecido de Macedo</a> | RA: 2401541  
- <a href="https://github.com/GuilhermePecorari">Guilherme Eduardo Moraes Pecorari</a> | RA: 2400086  
- <a href="https://github.com/Davibizerra">Davi de Moraes Bizerra</a> | RA: 2401072  

