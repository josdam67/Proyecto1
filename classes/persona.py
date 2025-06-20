
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


client = MongoClient(os.getenv("MONGO_URI"))
db = client['Proyecto1_db']
persona_colletion = db['personas']

class Persona:
    def __init__(self, nombre, apellido, fecha_nacimiento):
        self._id =None
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.pasaporte_id = None

    def save (self):
        data = {
            "nombre: " :self.nombre,
            "apellido: " : self.apellido,
            "Fecha de Nacimiento": self.fecha_nacimiento,
            "ID Pasaporte":self.pasaporte_id
        }

        resultado = persona_colletion.insert_one(data)
        self._id = resultado.inserted_id
