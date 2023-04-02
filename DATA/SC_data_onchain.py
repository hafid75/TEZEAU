import pymongo
import smartpy as sp
import pytezos as tz
import pandas as pd

# Se connecter à la base MongoDB
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["TEZEAU"]
mongo_collection = mongo_db["tbl_piezometrie"]





# Récupération des collections
piezometrie = db.tbl_piezometrie
referentiel_stations = db.tbl_referentiel_stations

# Parcours des documents de la collection piezometrie
for document in piezometrie.find():
    # Récupération du code_bss
    code_bss = document['code_bss']

    # Recherche du document correspondant dans la collection referentiel_stations
    ref_station = referentiel_stations.find_one({'code_bss': code_bss})

    # Si un document correspondant est trouvé, récupération du nom de la commune
    if ref_station is not None:
        nom_commune = ref_station['nom_commune']

        # Ajout de l'information nom_commune dans le document de la collection piezometrie
        piezometrie.update_one({'_id': document['_id']}, {'$set': {'nom_commune': nom_commune}})






# Se connecter au noeud Tezos
pytezos_node = tz.node.Node()

# Se connecter au contrat Tezos
contract_address = '0x123456789ABCDEF...' # Mettre l'adresse de votre contrat ici
contract = pytezos_node.contract(contract_address)

# Récupérer les données depuis la base MongoDB et les stocker sur la blockchain Tezos
for data in mongo_collection.find():
    contract.store_data(sp.bytes(data['key']), sp.bytes(data['value'])).operation_group.sign().inject()
