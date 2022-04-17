from flask import Flask, render_template
from routes.instrumentos import instrumentos
from routes.profesores import profesores
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] ='mysql://root:abc28051987A@localhost/gemadb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

SQLAlchemy(app)

app.register_blueprint(instrumentos)
app.register_blueprint(profesores)

@app.route('/login')
def login():
    return render_template('auth/login.html')


