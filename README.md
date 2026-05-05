//pra baixar o flask digite no terminal:

pip install flask

//depois execute o SQLAlchemy (banco de dados):

pip install flask_sqlalchemy

//depois instale o sistema de login/sessao

pip install flask_login

//depois que baixou tudo, abrir terminal com 

python app.py

//obs: toda vez que fechar e abrir o VS code,
abrir o terminal e executar esse código ^

=======================================

// Organização

models/: Tabelas do banco.
    Exemplo:
    class Usuario(db.Model)

routes/: Rotas Flask.
    Exemplo:
    @app.route("/")

services/: Lógica do sistema
    Exemplo:
    login, token, email, regras

static/: Arquivos enviados diretamente ao navegador
    Exemplo:
    Javascript, CSS e imagens

templates/: Arquivos de estrutura visual
    Exemplos:
    Pagina Login, Cadastro, Pagina Inicial

=======================================

// Baixar, caso precise

Flask Migrate:

pip install flask-migrate


.env:

pip install python-dotenv