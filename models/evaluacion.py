from flask_login import UserMixin
from utils.db import db
from sqlalchemy import PrimaryKeyConstraint

class Evaluacion(db.Model, UserMixin):
    profesor = db.Column(db.Integer)
    alumno = db.Column(db.Integer)
    trimestre= db.Column(db.Integer)
    nota_final = db.Column(db.String(2))
    fecha = db.Column(db.Date)
    comportamiento = db.Column(db.String(2))
    sonido = db.Column(db.String(2))
    lectura = db.Column(db.String(2))
    precision = db.Column(db.String(2))
    tecnica = db.Column(db.String(2))
    programa = db.Column(db.String(2))
    estudio = db.Column(db.String(2)) 
    comentarios = db.Column(db.String(100))

    __table_args__ = (
        PrimaryKeyConstraint(
        profesor,
        alumno,
        trimestre),
         {})

    

    def __init__(self, profesor, alumno, trimestre, nota_final, fecha, comportamiento, sonido, lectura, precision, tecnica, programa, estudio, comentarios):
        self.profesor = profesor
        self.alumno = alumno
        self.trimestre = trimestre
        self.nota_final = nota_final
        self.fecha = fecha
        self.comportamiento = comportamiento
        self.sonido = sonido
        self.lectura = lectura
        self.precision = precision
        self.tecnica = tecnica
        self.programa = programa
        self.estudio = estudio
        self.comentarios = comentarios