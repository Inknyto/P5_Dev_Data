import csv
import json
import xml.etree.ElementTree as ET

def ouvrir_et_lire_json():
    dico_data_json={}
    value=[]
    values=[]
    keys=[]
    with open('/home/nyto/Documents/projet S.A/Donnees_projet_data_p5.json') as jsonfile:
        donnees_json = json.load(jsonfile)
    dicos_from_json=json.loads(donnees_json)
    for dico in dicos_from_json:
        if 'Numero' in dico:
            keys.append(dico['Numero'])
    for dico in dicos_from_json:
        for x, y in dico.items():
            value.append(y)
        values.append(value[2:])
        value=[]
    dico_data_json=dict(zip(keys, values))
    return dico_data_json


def ouvrir_et_lire_xml():
    tree = ET.parse('/home/nyto/Documents/projet S.A/Donnees_projet_data.xml') 
    root = tree.getroot() 
    keys=[]
    value=[]
    values=[]
    for i in range(len(root)):    
        keys.append(root[i][1].text)
    for j in range(len(root)):
        for i in range (2, 7):
            value.append(root[j][i].text)
        values.append(value)
        value=[]
    dico_data_xml=dict(zip(keys, values))
    return dico_data_xml


def ouvrir_et_lire_csv():
    with open('/home/nyto/Téléchargements/Donnees_Projet_Python_DataC5.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # get the header row
        dico_data_csv = {}
        for row in reader:
            key = row[1]
            values = row[2:]
            dico_data_csv[key] = values
        return dico_data_csv    

