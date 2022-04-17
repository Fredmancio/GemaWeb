from utils.db import db

class Profesor(db.Model):
    idprofesor = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido_1 = db.Column(db.String(100))
    apellido_2 = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(102))
    instrumento = db.Column(db.Integer)

    def __init__(self, nombre, apellido_1, apellido_2, email, password, instrumento):
        self.nombre = nombre
        self.apellido_1 = apellido_1
        self.apellido_2 = apellido_2
        self.email = email
        self.password = password
        self.instrumento = instrumento

