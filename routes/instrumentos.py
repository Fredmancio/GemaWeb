from flask import Blueprint, render_template, request
from models.instrumento import Instrumento
from utils.db import db

instrumentos = Blueprint('instrumentos', __name__)

@instrumentos.route('/instrumentos')
def listar_instrumentos():
    
    instrumentos = Instrumento.query.all()
    return render_template('instrumentos.html', instrumentos=instrumentos)