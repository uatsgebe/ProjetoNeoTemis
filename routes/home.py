from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user

home_bp = Blueprint("home", __name__)

@home_bp.route("/home_advogado")
@login_required
def home_advogado():

    if current_user.tipo != "advogado":
        return redirect("/")

    return render_template("home_advogado.html")


@home_bp.route("/home_cliente")
@login_required
def home_cliente():

    if current_user.tipo != "cliente":
        return redirect("/")

    return render_template("home_cliente.html")


@home_bp.route("/home_admin")
@login_required
def home_admin():

    if current_user.tipo != "admin":
        return redirect("/")

    return render_template("home_admin.html")