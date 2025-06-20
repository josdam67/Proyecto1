from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # Carga variables del .env

uri = os.getenv("MONGO_URI")
print("URI:", uri)

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("✅ Conectado a MongoDB Atlas")
except Exception as e:
    print("❌ Error de conexión:", e)
