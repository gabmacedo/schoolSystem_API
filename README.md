<h1 align="center">🏫 Gestão de Alunos, Professores e Turmas - API Flask</h1>
Este projeto é uma API RESTful desenvolvida com <strong>Flask</strong>, focada na gestão de alunos, professores e turmas. Ele implementa operações CRUD para cada entidade e segue os princípios do TDD (Test-Driven Development). Ideal para fins acadêmicos e prática de arquitetura MVC.

<h1>🚀 Funcionalidades</h1>
✅ Cadastro, listagem, busca, atualização e exclusão de alunos<br>
✅ Suporte a endpoints para professores e turmas<br>
✅ Organização no padrão MVC<br>
✅ Testes unitários com unittest<br>
✅ Documentação automática com Swagger<br>
✅ Banco de dados SQLite com SQLAlchemy<br>
✅ Deploy na plataforma Render<br>
✅ Suporte a Docker<br>

<h1>🛠 Tecnologias Utilizadas</h1>
<ul>
<li><strong>🐍 Python</strong><br></li>
<li><strong>🌐 Flask</strong><br></li>
<li><strong>🗃️ Flask SQLAlchemy</strong><br></li>
<li><strong>🧩 SQLite</strong><br></li>
<li><strong>📄 Swagger (flask-restx)</strong><br></li>
<li><strong>🐳 Docker</strong><br></li>
<li><strong>🚀 Render (Deploy)</strong><br></li>
<li><strong>🧪 unittest</strong><br></li>
<li><strong>📬 requests</strong><br></li>
</ul>
<h1>📁 Estrutura do Projeto</h1>
O projeto está organizado da seguinte forma:<br>
📂 SchoolSystem_DevAPI<br>
 ┣ 📂 aluno<br>
 ┃ ┣ 📄 aluno_controller.py<br>
 ┃ ┣ 📄 aluno_model.py<br>
 ┃ ┗ 📄 aluno_routes.py<br>
 ┣ 📂 professor<br>
 ┃ ┣ 📄 professor_controller.py<br>
 ┃ ┣ 📄 professor_model.py<br>
 ┃ ┗ 📄 professor_routes.py<br>
 ┣ 📂 turma<br>
 ┃ ┣📄 turma_controller.py<br>
 ┃ ┣📄 turma_model.py<br>
 ┃ ┗📄 turma_routes.py<br>
 ┣📄app.py<br>
 ┣📄config.py<br>
 ┣📄Dockerfile<br>
 ┣📄teste_app.py<br>
 ┣📄requirements.txt<br>

<h2>📚 Documentação Swagger</h2>
Acesse a documentação interativa:<br>
Local: <code>http://localhost:5050/apidocs</code><br>
Produção: <code>https://api-de-gestao-escolar.onrender.com/apidocs</code><br>

<h2>▶️ Executando a Aplicação</h2>
<strong>Via Docker:</strong>

<code>docker build -t school-system-api .</code><br> 
<code>docker run -p 5050:5050 school-system-api</code><br>

<strong>Sem Docker:</strong><br> 
<code>pip install -r requirements.txt</code><br> 
<code>python app.py</code><br>

<h2>🌐 Endpoints Principais</h2>

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

<h2>🎯 Observações</h2>
- Agora o projeto utiliza banco de dados SQLite, armazenado em <code>/instance/app.db</code><br>
- A aplicação está hospedada em produção com o Render.

 <h1>👥 Colaboradores</h1>
<ul>
  <li><a href="https://github.com/gabmacedo">Gabriel Aparecido de Macedo</a> | RA: 2401541</li>
  <li><a href="https://github.com/GuilhermePecorari">Guilherme Eduardo Moraes Pecorari</a> | RA: 2400086</li>
  <li><a href="https://github.com/Davibizerra">Davi de Moraes Bizerra</a> | RA: 2401072</li>
</ul>
