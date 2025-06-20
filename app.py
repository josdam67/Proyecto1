

from classes.persona import Persona
from classes.pasaporte import Pasaporte

#Tenemos que crear una persona 
persona = Persona ("Jose", "Alvarez", "1994-09-21")
persona.save

#POsteriomente creamos lo que es el pasaporte 
pasaporte = Pasaporte ("FE123456", "Honduras", "2025-06-20", "2035-06-20", persona._id )
pasaporte.save()

print(f"ID Persona: {persona._id}, ID Pasaporte_id: {pasaporte._id}" )