from flask_login import UserMixin
from utils.db import db

class Partitura(db.Model, UserMixin):
    codigo = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    datos = db.Column(db.LargeBinary)
    profesor = db.Column(db.Integer)

    def __init__(self, nombre, datos, profesor):
        self.nombre = nombre
        self.datos = datos
        self.profesor = profesor

    
    def get_id(self):
           return (self.codigo)