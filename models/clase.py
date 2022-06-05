from flask_login import UserMixin
from utils.db import db
from sqlalchemy import PrimaryKeyConstraint

class Clase(db.Model, UserMixin):
    profesor = db.Column(db.Integer)
    alumno = db.Column(db.Integer)
    horario = db.Column(db.Integer)
    deberes = db.Column(db.String(100), nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint(
        profesor,
        alumno,
        horario),
         {})

    

    def __init__(self, profesor, alumno, horario):
        self.profesor = profesor
        self.alumno = alumno
        self.horario = horario

