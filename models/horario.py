from flask_login import UserMixin
from utils.db import db

class Horario_plantilla(db.Model, UserMixin):
    codigo = db.Column(db.Integer, primary_key=True)
    dia_semana = db.Column(db.String(10))
    hora = db.Column(db.Time)

    
    def get_id(self):
           return (self.codigo)