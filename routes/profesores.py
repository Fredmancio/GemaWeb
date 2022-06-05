from flask import Blueprint, flash, render_template, request, redirect, url_for, send_file
from flask_login import login_required, current_user
from models.alumno import Alumno
from models.clase import Clase
from models.evaluacion import Evaluacion
from models.partitura import Partitura
from utils.db import db, pending, integrity
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from utils.passwords import generate_random_password
from sqlalchemy.sql import text
from sqlalchemy import select
from datetime import date
from io import BytesIO

profesores = Blueprint("profesores", __name__)

@profesores.route("/horario")
@login_required
def ver_horario():
    consulta_clases = """SELECT
                    p.codigo AS codigo_profesor,
                    h.dia_semana AS dia,
                    h.hora AS hora,
                    CONCAT(a.nombre, ' ', a.apellido_1) AS alumno,
                    a.codigo AS codigo_alumno,
                    h.codigo AS codigo_horario,
                    c.deberes AS deberes
                    FROM profesor p
                    INNER JOIN clase c
                        ON p.codigo = c.profesor
                    INNER JOIN (horario_plantilla h, alumno a)
                        ON c.horario = h.codigo AND c.alumno = a.codigo
                    WHERE p.codigo = """ + str(current_user.codigo) +"""
                    ORDER BY 1, 2 DESC;"""
    query_clases = text(consulta_clases)
    try:
        clases = db.session.execute(query_clases)
    finally:
        db.session.close()
    return render_template("profesores/horario.html", clases = clases)

@profesores.route("/horario/deberes/<idprofe>/<idalumno>/<idhorario>", methods=["GET", "POST"])
@login_required
def poner_deberes(idprofe, idalumno,idhorario):
    clase_deberes = Clase.query.get_or_404((idprofe, idalumno,idhorario))
    if request.method == "POST":
        clase_deberes.deberes = request.form['deberes']
        try:
            db.session.commit()
            flash("Deberes asignados")
            return redirect("/horario")
        except:
            flash("No se pudieron poner los deberes")
            return redirect("/horario")
    else:
        return render_template("profesores/horario.html")

@profesores.route("/primera_evaluacion/<int:idalumno>")
@login_required
def mostrar_primera_evaluacion(idalumno):
    alumno = Alumno.query.get_or_404(idalumno)
    evaluacion = "Primera Evaluación"
    fecha = date.today()
    format_fecha = fecha.strftime('%d/%b/%Y')
    trimestre = 1
    profesor = current_user.codigo
    return render_template("profesores/evaluacion.html", evaluacion = evaluacion, alumno = alumno, format_fecha = format_fecha, trimestre = trimestre, profesor = profesor)

@profesores.route("/segunda_evaluacion/<int:idalumno>")
@login_required
def mostrar_segunda_evaluacion(idalumno):
    alumno = Alumno.query.get_or_404(idalumno)
    evaluacion = "Segunda Evaluación"
    fecha = date.today()
    format_fecha = fecha.strftime('%d/%b/%Y')
    trimestre = 2
    profesor = current_user.codigo
    return render_template("profesores/evaluacion.html", evaluacion = evaluacion, alumno = alumno, format_fecha = format_fecha, trimestre = trimestre, profesor = profesor)


@profesores.route("/tercera_evaluacion/<int:idalumno>")
@login_required
def mostrar_tercera_evaluacion(idalumno):
    alumno = Alumno.query.get_or_404(idalumno)
    evaluacion = "Tercera Evaluación"
    fecha = date.today()
    format_fecha = fecha.strftime('%d/%b/%Y')
    trimestre = 3
    profesor = current_user.codigo
    return render_template("profesores/evaluacion.html", evaluacion = evaluacion, alumno = alumno, format_fecha = format_fecha, trimestre = trimestre, profesor = profesor)


@profesores.route("/guardar_evaluacion/<int:idprofe>/<int:idalumno>/<int:idtrimestre>", methods=["GET", "POST"])
@login_required
def guardar_evaluacion(idprofe, idalumno, idtrimestre):
    evaluacion = Evaluacion.query.get_or_404((idprofe, idalumno,idtrimestre))
    if request.method == "POST":
        evaluacion.fecha = date.today()
        evaluacion.comportamiento = request.form['comportamiento']
        evaluacion.sonido = request.form['sonido']
        evaluacion.lectura = request.form['lectura']
        evaluacion.precision = request.form['precision']
        evaluacion.tecnica = request.form['tecnica']
        evaluacion.programa = request.form['programa']
        evaluacion.estudio = request.form['estudio']
        evaluacion.comentarios = request.form['comentarios']
        try:
            db.session.commit()
            flash("Evaluación realizada")
            return redirect("/horario")
        except:
            flash("No se pudo realizar la evaluación")
            return redirect("/horario")
    else:
        return render_template("profesores/horario.html")

@profesores.route("/evaluaciones")
@login_required
def ver_evaluaciones():
    consulta_primera_evaluacion = """SELECT
                                concat(a.nombre, ' ', a.apellido_1) AS alumno,
                                fecha, comportamiento, sonido, lectura, e.precision as preci, tecnica, programa, estudio, comentarios
                                FROM evaluacion e
                                INNER JOIN (alumno a, profesor p)
                                    ON e.alumno = a.codigo AND e.profesor = """ + str(current_user.codigo) + """
                                WHERE e.trimestre = 1
                                ORDER BY 1;"""
    consulta_segunda_evaluacion = """SELECT
                                concat(a.nombre, ' ', a.apellido_1) AS alumno,
                                fecha, comportamiento, sonido, lectura, e.precision as preci, tecnica, programa, estudio, comentarios
                                FROM evaluacion e
                                INNER JOIN (alumno a, profesor p)
                                    ON e.alumno = a.codigo AND e.profesor = """ + str(current_user.codigo) + """
                                WHERE e.trimestre = 2
                                ORDER BY 1;"""
    consulta_tercera_evaluacion = """SELECT
                                concat(a.nombre, ' ', a.apellido_1) AS alumno,
                                fecha, comportamiento, sonido, lectura, e.precision as preci, tecnica, programa, estudio, comentarios
                                FROM evaluacion e
                                INNER JOIN (alumno a, profesor p)
                                    ON e.alumno = a.codigo AND e.profesor = """ + str(current_user.codigo) + """
                                WHERE e.trimestre = 3
                                ORDER BY 1;"""
    query_primera_evaluacion =  text(consulta_primera_evaluacion)
    query_segunda_evaluacion = text(consulta_segunda_evaluacion)
    query_tercera_evaluacion = text(consulta_tercera_evaluacion)
    try:
        primera_evaluacion = db.session.execute(query_primera_evaluacion).unique()
        segunda_evaluacion = db.session.execute(query_segunda_evaluacion).unique()
        tercera_evaluacion = db.session.execute(query_tercera_evaluacion).unique()
    finally:
        db.session.close()
    return render_template("profesores/lista_evaluaciones.html", primera_evaluacion= primera_evaluacion, segunda_evaluacion = segunda_evaluacion, tercera_evaluacion = tercera_evaluacion)


@profesores.route('/partituras', methods=['GET','POST'])
@login_required
def subir_partituras():
    
    if request.method == 'POST':
        try:
            file = request.files['file']
            nombre = secure_filename(file.filename)
            datos = file.read()
            profesor = current_user.codigo
            partitura = Partitura(nombre, datos, profesor)
            db.session.add(partitura)
            db.session.commit()
        finally:
            db.session.close()
            flash("Partitura Subida")

        return redirect('/partituras')
    else:
        consulta_partitura = """select * from partitura where profesor =""" + str(current_user.codigo) + """;"""
        query_partitura = text(consulta_partitura)
        try:
            partituras = db.session.execute(query_partitura)
        finally:
            db.session.close()
        return render_template('profesores/partituras.html', partituras=partituras)

@profesores.route('/descargar/<int:idpartitura>')
def descargar_partitura(idpartitura):
    partitura = Partitura.query.get_or_404(idpartitura)
    return send_file(BytesIO(partitura.datos), attachment_filename=partitura.nombre, as_attachment=True)