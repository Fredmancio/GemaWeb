from flask import Flask, render_template
from models.profesor import Profesor
from routes.instrumentos import instrumentos
from routes.profesores import profesores
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    login_user,
    logout_user,
    UserMixin,
    login_required,
    LoginManager,
    current_user,
)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:abc28051987A@localhost/gemadb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SECRET_KEY"] = "bonditalagordita"

SQLAlchemy(app)

# -- Flask_Login necesario----------------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return Profesor.query.get(int(user_id))
#-------------------------------------------

app.register_blueprint(instrumentos)
app.register_blueprint(profesores)


@app.route("/login")
def login():
    return render_template("auth/login.html")
