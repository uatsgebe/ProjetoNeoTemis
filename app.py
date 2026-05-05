from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)

app.secret_key = "neotemis_secret"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"

db = SQLAlchemy(app)

login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = "login"

# =========================
# TABELA DE USUÁRIOS
# =========================
class Usuario(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(100), nullable=False)

    cpf = db.Column(db.String(14), unique=True, nullable=False)

    data_nascimento = db.Column(db.String(20), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    senha = db.Column(db.String(200), nullable=False)

    tipo = db.Column(db.String(20), nullable=False)

@login_manager.user_loader
def load_user(user_id):

    return Usuario.query.get(int(user_id))

# =========================
# LOGIN
# =========================
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")

        senha = request.form.get("senha")

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and check_password_hash(usuario.senha, senha):
            
            login_user(usuario)

            if usuario.tipo == "advogado":
                return redirect("/home_advogado")

            elif usuario.tipo == "cliente":
                return redirect("/home_cliente")

            elif usuario.tipo == "admin":
                return redirect("/home_admin")

        return "Email ou senha inválidos"

    return render_template("login.html")

@app.route("/home_advogado")
@login_required
def home_advogado():

    if current_user.tipo != "advogado":
        return redirect("/")

    return render_template("home_advogado.html")


@app.route("/home_cliente")
@login_required
def home_cliente():

    if current_user.tipo != "cliente":
        return redirect("/")

    return render_template("home_cliente.html")


@app.route("/home_admin")
@login_required
def home_admin():

    if current_user.tipo != "admin":
        return redirect("/")

    return render_template("home_admin.html")


# =========================
# CADASTRO
# =========================
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        nome = request.form.get("nome")

        cpf = request.form.get("cpf")

        data_nascimento = request.form.get("data_nascimento")

        tipo = request.form.get("tipo")

        email = request.form.get("email")

        senha = request.form.get("senha")
        senha_criptografada = generate_password_hash(senha)


        novo_usuario = Usuario(

            nome=nome,

            cpf=cpf,

            data_nascimento=data_nascimento,

            email=email,

            senha=senha_criptografada,

            tipo=tipo
        )

        db.session.add(novo_usuario)

        db.session.commit()

        return redirect("/")

    return render_template("cadastro.html")

# =========================
# DESLOGAR
# =========================
@app.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect("/")


# =========================
# EXECUTAR SERVIDOR
# =========================
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)