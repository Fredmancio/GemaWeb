from flask import Flask, redirect, render_template, url_for, request
from models.profesor import *
from routes.instrumentos import instrumentos
from routes.profesores import profesores
from flask_sqlalchemy import SQLAlchemy
from utils.db import db
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


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form['usuario'])
        print(request.form['password'])
        user = Profesor.query.filter_by(email = request.form['usuario']).first()
        print(user)
        if user:
            print("llego aqui")
            if check_password_hash(user.password, request.form['password']):
                login_user(user)
                return redirect(url_for('home'))
            else:
                print("no hay usuario")
    return render_template("auth/login.html")

@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('/home.html')
