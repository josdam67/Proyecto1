
import unittest
from classes.persona import Persona
from classes.pasaporte import Pasaporte
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client ['Protecto1_db']
persona_colletion = db['personas']
pasaporte_colletion = db['pasaportes']

class TestModelo (unittest.TestCase):
    def setUp(self):
        #segun investigacion nos ayudara a limpiar las colecciones antes de inciar cada prueba a realizar 
        persona_colletion.delete_many({})
        pasaporte_colletion.delete_many({})

    def test_creacion_de_instancias(self):
        persona = Persona("Arely", "Zuniga", "1997-03-29")
        persona.save()

        pasaporte = Pasaporte("XY897654", "Honduras", "2025-06-20", "2035-06-20", persona._id) 
        pasaporte.save()


        persona_db = persona_colletion.find_one({"_id": persona._id})
        pasaporte_db = pasaporte_colletion.find_one({"_id": pasaporte._id})

        self.assertIsNotNone(persona_db)
        self.assertIsNotNone(pasaporte_db)
        self.assertEqual(pasaporte_db["ID Persona"], persona._id)

    def test_actualizacion_persona_con_pasaporte(self):
        persona = Persona("Alberto", "Zuniga", "1987-03-29")
        persona.save()

        pasaporte = Pasaporte("XY657463", "Honduras", "2025-06-20", "2035-06-20", persona._id) 
        pasaporte.save()

        persona_db = persona_colletion.find_one({"_id": persona._id})
        self.assertEqual(persona_db["ID Persona"], pasaporte._id)

if __name__ == '__main__':
    unittest.main()


        
