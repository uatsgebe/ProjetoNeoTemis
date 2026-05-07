from extensions import db

# =========================
# TABELA DE ESCRITÓRIOS
# =========================
class Escritorio(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(120), nullable=False)

    imagem = db.Column(db.String(200))

    data_fundacao = db.Column(db.String(20))

    descricao = db.Column(db.Text)

    telefone = db.Column(db.String(20))

    email = db.Column(db.String(120))

    endereco = db.Column(db.String(200))

    gestor_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    






