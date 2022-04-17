

from flask import Blueprint, render_template, request
from models.profesor import Profesor
from models.instrumento import Instrumento
from utils.db import db

profesores = Blueprint("profesores", __name__)


@profesores.route("/profesores")
def home_profesores():
#-- Template de profesores
    instrumentos = Instrumento.query.all()
    profesores = Profesor.query.all()
    return render_template("profesores/profesores.html", profesores=profesores, instrumentos=instrumentos)

@profesores.route("/profesores/new", methods=['POST'])
def guardar_profesor():
    
    nombre = request.form['nombreProfesor']
    apellido_1 = request.form['apellido1']
    apellido_2 = request.form['apellido2']
    email = request.form['email']
    password = request.form['password']
    instrumento = request.form.get('instrumento')

    nuevo_profesor = Profesor(nombre, apellido_1, apellido_2, email, password, instrumento)
    db.session.add(nuevo_profesor)
    db.session.commit()
    

    return render_template("profesores/new_profesor.html", profesores=profesores)