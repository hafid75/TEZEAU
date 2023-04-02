import requests
from pymongo import MongoClient

# Connexion à la base de données
client = MongoClient('localhost', 27017)
db = client.TEZEAU
collection = db.tbl_referentiel_stations

# URL de l'API
url_communes = "https://hubeau.eaufrance.fr/api/v1/niveaux_nappes/stations"

# Envoi de la requête HTTP GET
response = requests.get(url_communes)

if response.status_code == 200 or response.status_code == 206:
    # Traitement de la réponse JSON
    data = response.json()
    for a in data['data']:
        # Insertion des données dans la collection
        collection.insert_one(a)
else:
    print("Erreur HTTP : %d" % response.status_code)

# Fermeture de la connexion à la base de données
client.close()
