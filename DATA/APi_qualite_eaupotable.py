import requests
from pymongo import MongoClient

# URL de l'API
url_qlt_eau = "https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/resultats_dis"

codes_dict = [
    {"code": "1302", "name": "PH"},
    {"code": "1340", "name": "Nitrate"},
    {"code": "1345", "name": "Durete_eau"}
]

result_dict = {}

for c in codes_dict:

    # Paramètres de la requête
    param = {
        "nom_commune": "vichy",
        "code_parametre": c["code"],
        "size": "5"
    }

    # Envoi de la requête HTTP GET
    response = requests.get(url_qlt_eau, params=param)

    # Vérification du code de statut HTTP
    if response.status_code == 200 or response.status_code == 206:

        # Traitement de la réponse JSON
        data = response.json()
        if 'data' in data and len(data['data']) > 0:
            for d in data['data']:

                # Création du dictionnaire pour chaque paramètre
                param_dict = {
                    'valeur': d['resultat_numerique'],
                    'libelle_unite': d['libelle_unite'],
                    'reference_qualite_parametre': d['reference_qualite_parametre'],
                    'date_prelevement': d['date_prelevement'],
                    'conclusion_conformite_prelevement': d['conclusion_conformite_prelevement'],
                    'conformite_limites_bact_prelevement': d['conformite_limites_bact_prelevement'],
                    'conformite_limites_pc_prelevement': d['conformite_limites_pc_prelevement'],
                    'conformite_references_bact_prelevement': d['conformite_references_bact_prelevement'],
                    'conformite_references_pc_prelevement': d['conformite_references_pc_prelevement']
                }

                # Récupération du nom de la commune
                nom_commune = d['nom_commune']

                # Ajout des données dans le dictionnaire final
                if nom_commune not in result_dict:
                    result_dict[nom_commune] = {}
                result_dict[nom_commune].setdefault(c['name'], {})
                result_dict[nom_commune][c['name']][d['date_prelevement']] = param_dict

    else:
        print("Erreur HTTP : %d" % response.status_code)

# Connexion à la base de données MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Création d'une collection "tbl_qualite_eaupotable" dans la base de données "TEZEAU"
db = client['TEZEAU']
tbl_qualite_eaupotable = db['tbl_qualite_eaupotable']

# Insertion des données dans la collection "tbl_qualite_eaupotable"
# Parcours du dictionnaire final pour l'insertion dans la base de données
for commune, data in result_dict.items():
    for param, values in data.items():
        for date, params_dict in values.items():
            # Création d'un document pour l'insertion
            document = {
                "commune": commune,
                "param": param,
                "date": date,
                "valeur": params_dict['valeur'],
                "libelle_unite": params_dict['libelle_unite'],
                "reference_qualite_parametre": params_dict['reference_qualite_parametre'],
                "conclusion_conformite_prelevement": params_dict['conclusion_conformite_prelevement'],
                "conformite_limites_bact_prelevement": params_dict['conformite_limites_bact_prelevement'],
                "conformite_limites_pc_prelevement": params_dict['conformite_limites_pc_prelevement'],
                "conformite_references_bact_prelevement": params_dict['conformite_references_bact_prelevement'],
                "conformite_references_pc_prelevement": params_dict['conformite_references_pc_prelevement']
            }
            # Insertion du document dans la table
            tbl_qualite_eaupotable.insert_one(document)

# Affichage de la première ligne de la table
print(tbl_qualite_eaupotable.find_one())