import uuid

from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash


def gerar_token_recuperacao(usuario):

    token = str(uuid.uuid4())

    usuario.token_recuperacao = token

    usuario.token_expira_em = (
        datetime.utcnow() + timedelta(minutes=15)
    )

    return token

def criptografar_senha(senha):

    return generate_password_hash(senha)


def verificar_senha(senha_hash, senha_digitada):

    return check_password_hash(
        senha_hash,
        senha_digitada
    )