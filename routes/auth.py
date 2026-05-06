from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime, timedelta

from extensions import db
from models.usuario import Usuario
from services.auth_service import gerar_token_recuperacao, criptografar_senha, verificar_senha

import uuid


from flask import Blueprint

auth_bp = Blueprint(
    "auth",
    __name__
)

# =========================
# LOGIN
# =========================
@auth_bp.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")

        senha = request.form.get("senha")

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and verificar_senha(usuario.senha, senha):
            
            login_user(usuario)

            if usuario.tipo == "advogado":
                return redirect(url_for("home.home_advogado"))

            elif usuario.tipo == "cliente":
                return redirect(url_for("home.home_cliente"))

            elif usuario.tipo == "admin":
                return redirect(url_for("home.home_admin"))

        return redirect("/?erro=1")

    erro_login = request.args.get("erro")
    
    sucesso = request.args.get("sucesso")

    return render_template(
        "login.html",
        erro_login=erro_login,
        sucesso=sucesso
    )


# =========================
# CADASTRO
# =========================
@auth_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        nome = request.form.get("nome")

        cpf = request.form.get("cpf")

        data_nascimento = request.form.get("data_nascimento")

        tipo = request.form.get("tipo")

        email = request.form.get("email")

        senha = request.form.get("senha")
        senha_criptografada = criptografar_senha(senha)


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
# RECUPERAR SENHA
# =========================
@auth_bp.route("/recuperar_senha", methods=["GET", "POST"])
def recuperar_senha():

    if request.method == "POST":

        email = request.form.get("email")

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario:

            token = gerar_token_recuperacao(usuario) # Função construída no auth_service.py
            
            db.session.commit()

            print(f"""
LINK DE RECUPERAÇÃO:

http://127.0.0.1:5000/redefinir_senha/{token}
""")

        return render_template(
            "email_enviado.html",
            email=email
        )

    return render_template("recuperar_senha.html")


# =========================
# REDEFINIR SENHA
# =========================
@auth_bp.route("/redefinir_senha/<token>", methods=["GET", "POST"])
def redefinir_senha(token):

    usuario = Usuario.query.filter_by(
        token_recuperacao=token
    ).first()

    if not usuario:

        return render_template(
            "redefinir_senha.html",
            erro="Token inválido"
        )
    
    if datetime.utcnow() > usuario.token_expira_em:

        return render_template(
            "redefinir_senha.html",
            erro="Link expirado. Solicite uma nova recuperação."
        )

    if request.method == "POST":

        nova_senha = request.form.get("nova_senha")

        confirmar_senha = request.form.get("confirmar_senha")

        if nova_senha != confirmar_senha:

            return render_template(
                "redefinir_senha.html",
                erro="As senhas não coincidem"
            )

        senha_criptografada = criptografar_senha(nova_senha)

        usuario.senha = senha_criptografada

        usuario.token_recuperacao = None

        db.session.commit()

        return redirect("/?sucesso=1")

    return render_template(
        "redefinir_senha.html"
    )


# =========================
# DESLOGAR
# =========================
@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect("/")