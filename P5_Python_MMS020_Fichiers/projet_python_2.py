import csv
import json
import xml.etree.ElementTree as ET
import re
from datetime import datetime
from lect_fichiers import*
from fonctions_de_test import*
valid_data={}
invalid_data={}
raison_invalidite={}
garder_les_notes = {}
gn={}
data={}
def invalider_dates(data):
    raison_invalidite={}
    invalid_data={}
    raison='   Date invalide   '
    for key, value in data.items():
        try:
            birthdate=value[2]
            birthdate = birthdate.replace(" ", "/").replace("-", "/").replace("|", "/")
            birthdate = birthdate.replace(".", "/").replace("_", "/")
            birthdate = birthdate.replace(",", "/").replace(":", "/")
    
            while len(birthdate) > 0 and not birthdate[0].isalnum():
                birthdate = birthdate[1:]
            if birthdate[-4:].isalnum():
                birthdate=birthdate[:-4]+birthdate[-2:]
    
            try:
                birthdate = datetime.strptime(birthdate, '%d/%m/%y').date()
            except ValueError:
                invalid_data.update({key: value})
                try:
                    raison_invalidite[key]+=(raison)
                except:
                    raison_invalidite.update({key: raison})
        except:
            invalid_data.update({key: value})
            try:
                raison_invalidite[key]+=(raison)
            except:
                raison_invalidite.update({key: '  champ vide  '})
    return invalid_data, raison_invalidite
def valider_donnees(data):
    for key, value in data.items(): 
        if key not in invalid_data:
            valid_data.update({key: value})


        
def calculer_moyenne_et_garder_notes(valid_data):
    garder_les_notes={}
    dictparnote={}
    listededict=[]
    for key, value in valid_data.items():
        notes=value[4]
        notes=notes.split('#')
        for matiere in notes:
            for i in range(len(matiere)):
                for j in range(len(matiere)):
                    if matiere[i]=='[' and matiere[j]==']':
                        libellé=matiere[:i]
                        serienotes=matiere[i+1:j]
                        notesdevoir, notexamen=serienotes.split(':')

                        try:
                            notesdevoir=notesdevoir.replace(',', '.')
                            notesdevoir=notesdevoir.split('|')
                        except:
                            notesdevoir=str(notesdevoir)
                        tabn=[]

                        for num in notesdevoir:
                            if isfloat(num):
                                notesdevoir=float(num)
                                tabn.append(notesdevoir)
                        nombredevoir=len(tabn)
                        sommedevoir=sum(tabn)
                        notexamen=float(notexamen) #mettre structure de controle
                        moyennedevoir=sommedevoir/nombredevoir
                        moyenne=(moyennedevoir+notexamen)/2
                        moyenne=round(moyenne, 2)
                       # print('numero=', key, libellé, 'notesdevoir=',tabn, notexamen, 'moyenne=', moyenne)
                        dictparnote={'numero':key, 'matiere':libellé, 'notes devoir': tabn,
                                    'note examen': notexamen, 'moyenne ': moyenne}

            listededict.append(dictparnote)
    temp_list = []
    for i in listededict:
        if i not in temp_list:
            temp_list.append(i)
    listededict = temp_list
    for dico in listededict:
        if dico['numero'] not in garder_les_notes:
            garder_les_notes[dico['numero']] = {}

        garder_les_notes[dico['numero']].setdefault(dico['matiere'], {
            'notes devoir': [],
            'note examen': 0,
            'moyenne': 0
        })
        garder_les_notes[dico['numero']][dico['matiere']]['notes devoir']+=(dico['notes devoir'])
        garder_les_notes[dico['numero']][dico['matiere']]['note examen']+=(dico['note examen'])
        garder_les_notes[dico['numero']][dico['matiere']]['moyenne']+=(dico['moyenne '])
    return garder_les_notes
def calculer_moyenne_generale():
    for numero, petit_dict in garder_les_notes.items():
        moyenne_generale = 0
        tab_moyennes = []
        somme_moyennes = 0
        unenote = 0
        for libelle, notes in petit_dict.items():
            if isinstance(notes, dict) and 'moyenne' in notes:
                unenote = notes['moyenne']
                try:
                    tab_moyennes.append(float(unenote))
                except ValueError:
                    pass
            else:
                pass
        somme_moyennes = sum(tab_moyennes)
        moyenne_generale = somme_moyennes / len(petit_dict)
        moyenne_generale=round(moyenne_generale, 2)
        petit_dict.update({'moyenne générale': moyenne_generale})



def ajouter_données(data, new_data):
    if not validate_data(new_data):
        print("Invalid data")
        return
    data.append(new_data)

def modifier_données(invalid_data, new_data):
    if not validate_data(new_data):
        print("Invalid data")
        return
    for i, row in enumerate(invalid_data):
        if row[0] == new_data[0]:
            invalid_data.pop(i)
            break
    return new_data

def afficher_les_notes():
    for numero, notes in garder_les_notes.items():    
        print(numero, '  ')
        print()
        for libelle, note in notes.items():
            print(libelle)
            print()
            try:
                for nom, n in note.items():
                    print(nom,' ',end='')
                    try:
                        for i in n:
                            if isinstance(n, list):
                                print(i,' ', end='')
                    except:
                        print(n,' ')
            except AttributeError:
                print(note)
            print()
def invalider_les_donnees(data):
    invnum, rnum=invalidernum(data)
    invalid_data.update(invnum)
    raison_invalidite.update({'Numero invalide':rnum})
    invnom, rnom=invalider_nom_et_prénom(data)
    invalid_data.update(invnom)
    raison_invalidite.update({'Nom ou prénom invalide':rnom})
    invdates, rdates=invalider_dates(data)
    invalid_data.update(invdates)
    raison_invalidite.update({'Date invalide':rdates})
    invclasse, rclasse=invalider_classe(data)
    invalid_data.update(invclasse)
    raison_invalidite.update({'Classe invalide':rclasse})
    invnotes, rnotes=invalider_notes(data)
    invalid_data.update(invnotes)
    raison_invalidite.update({'Notes invalide':rnotes})
    
def operations_suivantes():
    garder_les_notes.update(calculer_moyenne_et_garder_notes(valid_data))
    calculer_moyenne_generale()
    changer_formats_dates(valid_data)
    changer_formats_devoirs(valid_data)
    changer_formats_notes(valid_data)
    changer_formats_classes(valid_data)
    changer_formats_examens(valid_data)
    
def operation_intermediaire(data):
    invalider_les_donnees(data)
    valider_donnees(data)
    operations_suivantes()
def menu_2():
    print("Menu 2:")
    print("1. Afficher les informations valides")
    print("2. Afficher les informations invalides")
    print("3. Afficher les raisons d'invalidité")
    print("4. Afficher les notes")
    print("5. Afficher par numéros")
    print("6. Afficher les cinq premiers")
    print("7. Ajouter des données")
    print("8. Modifier des données")
    print("9. Retour")
    choice = input("Entrez un choix: ")
    while True:
        if choice == '1':
            afficher_tout(valid_data)
            break
        elif choice == '2':
            afficher_tout(invalid_data)
            break
        elif choice == '3':
            affichage_simple(raison_invalidite)
            break
        elif choice=='4':
            afficher_les_notes()
            break
        elif choice == '5':   
            num = input("Entrez le numero: ")
            afficher_informations_selon_numero(valid_data, num)
            break
        elif choice == '6':
            afficher_les_cinq_premiers(garder_les_notes)
            break
        elif choice == '7':
            new_data = input("Entrez les nouvelles données (code, numero, nom, prénom , date de naissance, classe, notes): ")
            ajouter_données(data, new_data)
            break
        elif choice == '8':
            new_data = input("Entrez les nouvelles données (code, numero, nom, prénom , date de naissance, classe, notes): ")
            modifier_données(invalid_data, new_data)
            break
        elif choice=='9':
            return
        else:
            print('Choix invalide')
            break
    menu_2()
while True:
    xml=False
    csv=False
    json=False
    print("Menu:")
    print("Quel format de fichier voulez-vous lire?")
    print("1. Pour XML")
    print("2. Pour CSV")
    print("3. Pour JSON")
    print("4. Quitter")
    choice = input()
    if choice == '1':
        data=ouvrir_et_lire_xml()
        xml=True
        operation_intermediaire(data)
        menu_2()
    elif choice == '2':
        data=ouvrir_et_lire_csv()
        csv=True
        operation_intermediaire(data)
        menu_2()
    elif choice == '3':
        data=ouvrir_et_lire_json()
        json=True
        operation_intermediaire(data)
        menu_2()
    elif choice == '4':
        break
    else:
        print("Choix invalide")
