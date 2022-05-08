from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import login_required
from models.profesor import Profesor
from models.instrumento import Instrumento
from utils.db import db
from werkzeug.security import check_password_hash, generate_password_hash

admin = Blueprint("admin", __name__)


@admin.route("/gestion_profesores")
@login_required
def gestion_profesores():
#-- Template de profesores
    instrumentos = Instrumento.query.all()
    profesores = Profesor.query.all()
    return render_template("admin/gestion_profesores.html", profesores=profesores, instrumentos=instrumentos)

@admin.route("/gestion_profesores/new_profesor", methods=['POST'])
@login_required
def guardar_profesor():
    
    nombre = request.form['nombreProfesor']
    apellido_1 = request.form['apellido1']
    apellido_2 = request.form['apellido2']
    email = request.form['email']
    password = request.form['password']
    instrumento = request.form.get('instrumento')

    password_hash = generate_password_hash(password)

    nuevo_profesor = Profesor(nombre, apellido_1, apellido_2, email, password_hash, instrumento)
    db.session.add(nuevo_profesor)
    db.session.commit()
    flash("Profesor Creado")
    
    return redirect('/gestion_profesores')