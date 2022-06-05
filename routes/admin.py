from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models.profesor import Profesor
from models.materia import Materia
from models.alumno import Alumno
from models.horario import Horario_plantilla
from models.clase import Clase
from utils.db import db, pending, integrity
from werkzeug.security import check_password_hash, generate_password_hash
from utils.passwords import generate_random_password
from sqlalchemy.sql import text
from sqlalchemy import select

admin = Blueprint("admin", __name__)

# ---------Rutas gestión profesores-----------------


@admin.route("/gestion_profesores")
@login_required
def gestion_profesores():
    id = current_user.codigo
    if id == 1:
        # -- Template de profesores
        materias = Materia.query.all()
        profesores = Profesor.query.all()
        password = generate_random_password()
        return render_template(
            "admin/gestion_profesores.html",
            profesores=profesores,
            materias=materias,
            password=password,
        )
    else:
        flash("Debes ser administrador para acceder a esta página")
        return redirect("/home")


@admin.route("/gestion_profesores/new_profesor", methods=["POST"])
@login_required
def guardar_profesor():

    nombre = request.form["nombreProfesor"]
    apellido_1 = request.form["apellido1"]
    apellido_2 = request.form["apellido2"]
    email = request.form["email"]
    password = request.form["password"]
    materia = request.form.get("materia")

    password_hash = generate_password_hash(password)

    nuevo_profesor = Profesor(
        nombre, apellido_1, apellido_2, email, password_hash, materia
    )
    db.session.add(nuevo_profesor)
    db.session.commit()
    flash("Profesor Creado")

    return redirect("/gestion_profesores")


@admin.route("/gestion_profesores/delete_profesor/<int:id>")
@login_required
def borrar_profesor(id):
    profesor_to_delete = Profesor.query.get_or_404(id)

    try:
        db.session.delete(profesor_to_delete)
        db.session.commit()
        flash("Profesor borrado correctamente")
        return redirect("/gestion_profesores")

    except integrity:
        db.session.rollback()
        flash("Para eliminar un profesor no debe tener alumnos asignados")
        return redirect("/gestion_profesores")
    except pending:
        db.session.rollback()
        flash("Para eliminar un profesor no debe tener alumnos asignados")
        return redirect("/gestion_profesores")


@admin.route(
    "/gestion_profesores/formulario_update_profesor/<int:id>", methods=["GET", "POST"]
)
@login_required
def formulario_update_profesor(id):
    profesor_to_update = Profesor.query.get_or_404(id)
    materias = Materia.query.all()
    if request.method == "POST":
        profesor_to_update.nombre = request.form["nombreProfesor"]
        profesor_to_update.apellido_1 = request.form["apellido1"]
        profesor_to_update.apellido_2 = request.form["apellido2"]
        profesor_to_update.email = request.form["email"]
        profesor_to_update.password = request.form["password"]
        profesor_to_update.materia = request.form.get("materia")
        try:
            db.session.commit()
            flash("Profesor modificado correctamente")
            return redirect("/gestion_profesores")
        except:
            flash("El profesor no existe")
            return redirect("/gestion_profesores")
    else:
        return render_template(
            "admin/update_profesor.html",
            profesor_to_update=profesor_to_update,
            materias=materias,
        )


# ------------Rutas gestión alumnos--------------


@admin.route("/gestion_alumnos")
@login_required
def gestion_alumnos():
    # -- Template de alumnos
    materias = Materia.query.all()
    alumnos = Alumno.query.all()
    password = generate_random_password()
    return render_template(
        "admin/gestion_alumnos.html",
        materias=materias,
        alumnos=alumnos,
        password=password,
    )


@admin.route("/gestion_alumnos/new_alumno", methods=["POST"])
@login_required
def guardar_alumno():

    nombre = request.form["nombreAlumno"]
    apellido_1 = request.form["apellido1"]
    apellido_2 = request.form["apellido2"]
    email = request.form["email"]
    password = request.form["password"]

    password_hash = generate_password_hash(password)

    nuevo_alumno = Alumno(
        nombre, apellido_1, apellido_2, email, password_hash
    )
    db.session.add(nuevo_alumno)
    db.session.commit()
    flash("Alumno Creado")

    return redirect("/gestion_alumnos")


@admin.route("/gestion_alumnos/delete_alumno/<int:id>")
@login_required
def borrar_alumno(id):
    alumno_to_delete = Alumno.query.get_or_404(id)
    print(alumno_to_delete)
    try:
        db.session.delete(alumno_to_delete)
        db.session.commit()
        flash("Alumno borrado correctamente")
        return redirect("/gestion_alumnos")

    except integrity:
        db.session.rollback()
        flash("Para eliminar un profesor no debe tener alumnos asignados")
        return redirect("/gestion_alumnos")
    except pending:
        db.session.rollback()
        flash("Para eliminar un profesor no debe tener alumnos asignados")
        return redirect("/gestion_alumnos")


@admin.route(
    "/gestion_alumnos/formulario_update_alumno/<int:id>", methods=["GET", "POST"]
)
@login_required
def formulario_update_alumno(id):
    alumno_to_update = Alumno.query.get_or_404(id)
    if request.method == "POST":
        alumno_to_update.nombre = request.form["nombreAlumno"]
        alumno_to_update.apellido_1 = request.form["apellido1"]
        alumno_to_update.apellido_2 = request.form["apellido2"]
        alumno_to_update.email = request.form["email"]
        alumno_to_update.password = request.form["password"]
        try:
            db.session.commit()
            flash("Alumno modificado correctamente")
            return redirect("/gestion_alumnos")
        except:
            flash("El alumno no existe")
            return redirect("/gestion_alumnos")
    else:
        return render_template(
            "admin/update_alumno.html",
            alumno_to_update=alumno_to_update,
        )

#---------Rutas Gestión Clases-------------
@admin.route("/gestion_clases")
@login_required
def listar_clases():
    query_clases = text("""SELECT
                CONCAT(p.nombre, ' ', p.apellido_1) AS profesor,
                p.codigo AS codigo_profesor,
                h.dia_semana AS dia,
                h.hora AS hora,
                CONCAT(a.nombre, ' ', a.apellido_1) AS alumno,
                a.codigo AS codigo_alumno,
                h.codigo AS codigo_horario
                FROM profesor p
                INNER JOIN clase c
                    ON p.codigo = c.profesor
                INNER JOIN (horario_plantilla h, alumno a)
                    ON c.horario = h.codigo AND c.alumno = a.codigo
                ORDER BY 1, 2 ASC;""")
    clases = db.session.execute(query_clases)
    return render_template("admin/gestion_clases.html", clases=clases)

@admin.route("/gestion_clases/delete_clase/<idprofe>/<idalumno>/<idhorario>")
@login_required
def borrar_clase(idprofe, idalumno,idhorario):
    clase_to_delete = Clase.query.get_or_404((idprofe, idalumno,idhorario))
    try:
        db.session.delete(clase_to_delete)
        print("Clase to delete")
        db.session.commit()
        flash("Clase eliminada correctamente")
        return redirect("/gestion_clases")
    except integrity:
        db.session.rollback()
        flash("Error")
        return redirect("/gestion_clases")
    except pending:
        db.session.rollback()
        flash("Error")
        return redirect("/gestion_clases")
    return redirect("/gestion_clases")

# --------perfiles---------------------


@admin.route("/perfil_profesor/<int:id>", methods=["GET", "POST"])
@login_required
def mostrar_perfil_profesor(id):
    profesor_to_show = Profesor.query.get_or_404(id)
    materia = Materia.query.get_or_404(profesor_to_show.materia).nombre
    query_alumnos = text("""SELECT codigo, nombre from alumno where codigo not in (select alumno from clase)""")
    alumnos = db.session.execute(query_alumnos)
    consulta_horarios = """SELECT codigo as codigo, dia_semana as dia_semana, hora as hora from horario_plantilla
                        where codigo not in(select horario from clase where profesor = """ + str(id) + """);"""
    query_horarios = text(consulta_horarios)
    horarios = db.session.execute(query_horarios)
    ruta_volver = "/perfil_profesor/" + str(id)
    consulta_clases = """SELECT
                    CONCAT(p.nombre, ' ', p.apellido_1) AS nombre_completo,
                    h.dia_semana AS dia,
                    h.hora AS hora,
                    a.nombre AS nombre_alumno
                    FROM profesor p
                    INNER JOIN clase c
                    ON p.codigo = c.profesor
                    INNER JOIN (horario_plantilla h, alumno a)
                    ON c.horario = h.codigo AND c.alumno = a.codigo
                    WHERE p.codigo = """ + str(id)+ """
                    ORDER BY 2, 3 ASC;"""
    query_clases = text(consulta_clases)
    clases = db.session.execute(query_clases)  
    print(query_clases)
    if request.method == "POST":
        alumno = request.form.get("alumno")
        horario = request.form.get("horario")
        try:
            nueva_clase = Clase(profesor_to_show.codigo, alumno, horario)
            db.session.add(nueva_clase)
            db.session.commit()
            flash("Clase creada")
            return redirect(ruta_volver)
            
        except integrity:
            db.session.rollback()
            flash("Para eliminar un profesor no debe tener alumnos asignados")
            return redirect("/gestion_profesores")
        except pending:
            db.session.rollback()
            flash("Para eliminar un profesor no debe tener alumnos asignados")
            return redirect("/gestion_profesores")
    else:
        return render_template(
            "admin/perfil_profesor.html",
            profesor_to_show=profesor_to_show,
            materia = materia,
            alumnos = alumnos,
            horarios = horarios,
            clases = clases
            #numero_alumnos=numero_alumnos,
    )


@admin.route("/perfil_alumno/<int:id>")
@login_required
def mostrar_perfil_alumno(id):
    alumno_to_show = Alumno.query.get_or_404(id)
    return render_template(
        "admin/perfil_alumno.html", alumno_to_show=alumno_to_show
    )


# --------listas-----------------------


@admin.route("/lista_profesores")
@login_required
def listar_profesores():
    profesores = Profesor.query.all()
    return render_template("/admin/tabla_profesores.html", profesores=profesores)
