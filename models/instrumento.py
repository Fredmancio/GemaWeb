from utils.db import db


class Instrumento(db.Model):
    
    nombre = db.Column(db.String(100), primary_key=True)
    familia = db.Column(db.String(100))

    def __init__(self, nombre, familia):
        self.nombre = nombre
        self.familia = familia
