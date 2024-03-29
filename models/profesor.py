from flask_login import UserMixin
from utils.db import db
from werkzeug.security import check_password_hash

class Profesor(db.Model, UserMixin):
    codigo = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido_1 = db.Column(db.String(100))
    apellido_2 = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(102))
    materia = db.Column(db.String(100))

    def __init__(self, nombre, apellido_1, apellido_2, email, password, materia):
        self.nombre = nombre
        self.apellido_1 = apellido_1
        self.apellido_2 = apellido_2
        self.email = email
        self.password = password
        self.materia = materia

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)   
    
    def get_id(self):
           return (self.codigo)

