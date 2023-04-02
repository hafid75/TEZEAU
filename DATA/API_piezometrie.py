import requests
from pymongo import MongoClient
import time
# URL de l'API
url_pzmtr_eau = "https://hubeau.eaufrance.fr/api/v1/niveaux_nappes/chroniques_tr"
client = MongoClient('localhost', 27017)
db = client.TEZEAU
collection = db.tbl_piezometrie
dict_ref={}




# Faire une requête API
response = requests.get(url_pzmtr_eau)

if response.status_code == 200 or response.status_code == 206:
    data = response.json()

    # Insérer les données dans MongoDB
    collection.insert_many(data['data'])

# Attendre 30 minutes avant la prochaine requête