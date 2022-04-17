from utils.db import db


class Instrumento(db.Model):
    idinstrumento = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    familia = db.Column(db.String(100))

    def __init__(self, nombre, familia):
        self.nombre = nombre
        self.familia = familia
