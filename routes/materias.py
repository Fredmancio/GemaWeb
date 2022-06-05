from flask import Blueprint, render_template, request
from flask_login import login_required
from models.materia import Materia
from utils.db import db

materias = Blueprint('materias', __name__)

@materias.route('/materias')
@login_required
def listar_materias():
    
    materias = Materia.query.all()
    return render_template('materias.html', materias=materias)