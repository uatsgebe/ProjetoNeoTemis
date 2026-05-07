from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from extensions import db
from models.escritorio import Escritorio
from models.usuario import Usuario


home_bp = Blueprint("home", __name__)

# =========================
# DASHBOARD (PAGINA INICIAL)
# =========================
@home_bp.route("/dashboard")
@login_required
def dashboard():
    if current_user.tipo == "admin":
        return render_template("dashboard_admin.html")
    
    if current_user.tipo == "cliente":
        return render_template("dashboard_cliente.html")
    
    if current_user.tipo == "advogado":
        
        if current_user.papel_escritorio == "gestor":    
            return render_template("dashboard_gestor.html")
        
        if current_user.papel_escritorio == "estagiario":    
            return render_template("dashboard_estagiario.html")
        
        return render_template("dashboard_advogado.html")
    
    return redirect(url_for("auth.login"))

# =========================
# CRIAR ESCRITÓRIO
# =========================
@home_bp.route("/criar_escritorio", methods=["GET", "POST"])
@login_required
def criar_escritorio():

    if current_user.tipo != "advogado":
        return redirect(url_for("home.dashboard"))

    if request.method == "POST":

        nome = request.form.get("nome")

        data_fundacao = request.form.get("data_fundacao")

        descricao = request.form.get("descricao")

        telefone = request.form.get("telefone")

        email = request.form.get("email")

        endereco = request.form.get("endereco")

        if not nome:
            return render_template(
                "criar_escritorio.html",
                erro="O nome do escritório é obrigatório."
            )

        novo_escritorio = Escritorio(

            nome=nome,

            data_fundacao=data_fundacao,

            descricao=descricao,

            telefone=telefone,

            email=email,

            endereco=endereco,

            gestor_id=current_user.id
        )

        db.session.add(novo_escritorio)
        db.session.commit()

        current_user.escritorio_id = novo_escritorio.id
        current_user.papel_escritorio = "gestor"

        db.session.commit()

        return redirect(url_for("home.dashboard"))

    return render_template("criar_escritorio.html")

# =========================
# ESCRITÓRIO
# =========================
@home_bp.route("/escritorio")
@login_required
def escritorio():

    if current_user.tipo != "advogado":
        return redirect(url_for("home.dashboard"))

    escritorio = None                               # Se ele for autônomo ele vai pro dashboard (porque "nao tem" a opção escritório, só criar escritorio)

    if current_user.escritorio_id:

        escritorio = Escritorio.query.get(
            current_user.escritorio_id
        )

    return render_template(                         # Se ele estiver em um escritório, ele tem a opção de ver o escritório
        "escritorio.html",
        escritorio=escritorio
    )

# =========================
# EQUIPE
# =========================
@home_bp.route("/equipe")
@login_required
def equipe():

    if current_user.tipo != "advogado":
        return redirect(url_for("home.dashboard"))

    if not current_user.escritorio_id:
        return redirect(url_for("home.escritorio"))

    membros = Usuario.query.filter_by(
        escritorio_id=current_user.escritorio_id
    ).all()

    return render_template(
        "equipe.html",
        membros=membros
    )

# =========================
# NOVO MEMBRO
# =========================
@home_bp.route("/novo_membro", methods=["GET", "POST"])
@login_required
def novo_membro():

    if current_user.tipo != "advogado":
        return redirect(url_for("home.dashboard"))

    if current_user.papel_escritorio != "gestor":
        return redirect(url_for("home.equipe"))

    if request.method == "POST":

        email = request.form.get("email")

        papel = request.form.get("papel")

        usuario = Usuario.query.filter_by(email=email).first()

        if not usuario:
            return render_template(
                "novo_membro.html",
                erro="Usuário não encontrado."
            )

        usuario.escritorio_id = current_user.escritorio_id
        usuario.papel_escritorio = papel

        db.session.commit()

        return redirect(url_for("home.equipe"))

    return render_template("novo_membro.html")