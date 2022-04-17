from flask import Blueprint, render_template, request, session
from models.profesor import Profesor
from models.instrumento import Instrumento
from utils.db import db

profesores = Blueprint("profesores", __name__)


@profesores.route("/profesores")
def listar_profesores():


    instrumentos = Instrumento.query.all()
    profesores = Profesor.query.all()
    return render_template("profesores.html", profesores=profesores, instrumentos=instrumentos)
