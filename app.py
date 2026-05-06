import uuid

from config import Config

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_migrate import Migrate

from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime, timedelta

app = Flask(__name__)

app.config.from_object(Config)

from extensions import db, login_manager

db.init_app(app)

migrate = Migrate(app, db)

login_manager.init_app(app)

login_manager.login_view = "login"

from models.usuario import Usuario

@login_manager.user_loader
def load_user(user_id):

    return Usuario.query.get(int(user_id))

from routes.auth import auth_bp
from routes.home import home_bp

app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)

# =========================
# EXECUTAR SERVIDOR
# =========================
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)