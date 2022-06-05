from flask_login import UserMixin
from utils.db import db
from werkzeug.security import check_password_hash

class Alumno(db.Model, UserMixin):
    codigo = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido_1 = db.Column(db.String(100))
    apellido_2 = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(102))

    def __init__(self, nombre, apellido_1, apellido_2, email, password):
        self.nombre = nombre
        self.apellido_1 = apellido_1
        self.apellido_2 = apellido_2
        self.email = email
        self.password = password

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)   
    
    def get_id(self):
           return (self.codigo)

