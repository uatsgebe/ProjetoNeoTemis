from extensions import db
from flask_login import UserMixin

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

    token_recuperacao = db.Column(db.String(200))

    token_expira_em = db.Column(db.DateTime)