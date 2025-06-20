

from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client['Proyecto1_db']
pasaporte_collection = db['pasaportes']
persona_colletion = db['personas']


class Pasaporte:
    def __init__(self, numero_pasaporte, pais_emision, fecha_emision, fecha_expiracion, persona_id):
        self._id = None
        self.numero_pasaporte =numero_pasaporte
        self.pais_emision = pais_emision
        self.fecha_emision = fecha_emision
        self.fecha_expiracion = fecha_expiracion
        self.persona_id = persona_id

    def save (self):
        data = {
            "Numero Pasaporte": self.numero_pasaporte,
            "Pais de Emision" : self.pais_emision,
            "Fecha de Emision" : self.fecha_emision,
            "Fecha de Expiracion": self.fecha_expiracion,
            "ID Persona" : self.persona_id

        }

        resultado = pasaporte_collection.insert_one(data)
        self._id = resultado.inserted_id
