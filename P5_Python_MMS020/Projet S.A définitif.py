import csv
import re
from datetime import datetime
valid_data={}
invalid_data={}
raison_invalidite={}
garder_les_notes = {}
gn={}

def isfloat(num):
    if not num.isnumeric():
        try:    
            a, b=num.split('.')

            if a.isnumeric() and b.isnumeric():
                return True
            else:
                return False
        except:
            return False
    else:
        return True
    
def read_file():
    with open('/home/nyto/Téléchargements/Donnees_Projet_Python_DataC5.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # get the header row
        data = {}
        for row in reader:
            key = row[1]
            values = row[2:]
            data[key] = values
        return data
data=read_file()

def validernum(data):
    raison='  numero invalide   '
    raison2='  numéro non alphanumérique   '
    raison3='  numéro contient lettre minuscule   '
    for key, value in data.items():
        if len(key) != 7:        
            invalid={key: value}
            invalid_data.update(invalid)
            try:
                if raison not in value:
                    raison_invalidite[key]+=(raison)
            except:
                r={key: raison}
                raison_invalidite.update(r)
        if not key.isalnum():
            invalid={key: value}
            invalid_data.update(invalid)
            try:
                if raison2 not in value:
                    raison_invalidite[key]+=(raison2)
            except:
                r={key: raison2}
                raison_invalidite.update(r)
        for i in range(len(key)):
            if key[i].islower():
                invalid={key: value}
                invalid_data.update(invalid)
                try:
                    if raison3 not in value:
                        raison_invalidite[key]+=(raison3)
                except:
                    r={key: raison3}
                    raison_invalidite.update(r)                    
validernum(data)

def valider_nom_et_prénom(data):
    raison='   nom invalide   '
    raison2='   prénom invalide   '
    for key, value in data.items():
        if len(value[0]) < 2 or not value[0][0].isalpha():
            invalid={key: value}
            invalid_data.update(invalid)
            try:
                if raison not in value:
                    raison_invalidite[key]+=(raison)
            except:
                r={key: raison}
                raison_invalidite.update(r)
        if len(value[1]) < 3 or not value[1][0].isalpha():
            invalid={key: value}
            invalid_data.update(invalid)
            try:
                if raison2 not in value:
                    raison_invalidite[key]+=(raison2)
            except:
                r={key: raison2}
                raison_invalidite.update(r)
valider_nom_et_prénom(data)       

def valider_notes(data):
    raison='   pas de note d\'examen   '
    raison2='  note d\'examen invalide  '
    for key, value in data.items():
        notes=value[4]
        notes=notes.split('#')
        for matiere in notes:
            for i in range(len(matiere)):
                for j in range(len(matiere)):
                    if matiere[i]=='[' and matiere[j]==']':
                        libellé=matiere[:i]
                        serienotes=matiere[i+1:j]
                        try:
                            notesdevoir, notexamen=serienotes.split(':')
                        except:
                            invalid={key: value}
                            invalid_data.update(invalid)
                            try:
                                if raison not in value:
                                    raison_invalidite[key]+=(raison)
                                else:
                                    pass
                            except:
                                r={key: raison}
                                raison_invalidite.update(r)
                        if float(notexamen)<0 or float(notexamen)>20:
                            invalid={key: value}
                            invalid_data.update(invalid)
                            try:
                                if raison2 not in value:
                                    raison_invalidite[key]+=(raison2)
                                else:
                                    pass
                            except:
                                r={key: raison2}
                                raison_invalidite.update(r)

valider_notes(data)

def valider_classe(data):
    raison='   Classe vide   '
    raison2='   Format de classe invalide   '
    for key, value in data.items():
        class_level=value[3]
        class_level=class_level.replace(" ", "")
        if (len(class_level))>0:
            if class_level[0] not in ['6','5','4','3']:
                invalid={key: value}
                invalid_data.update(invalid)
                try:
                    raison_invalidite[key]+=(raison2)
                except:
                    r={key: raison2}
                    raison_invalidite.update(r)
            if class_level[-1] not in ['A','B']:
                invalid={key: value}
                invalid_data.update(invalid)
                try:
                    raison_invalidite[key]+=(raison2)
                except:
                    r={key: raison2}
                    raison_invalidite.update(r)
        else:
            try:
                raison_invalidite[key]+=(raison)
            except:
                r={key: raison}
                raison_invalidite.update(r)
valider_classe(data)

def valider_dates(data):
    raison='   Date invalide   '
    for key, value in data.items():
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
            invalid={key: value}
            invalid_data.update(invalid)
            try:
                raison_invalidite[key]+=(raison)
            except:
                r={key: raison}
                raison_invalidite.update(r)
valider_dates(data)

def valider_donnees(data):
    for key, value in data.items(): 
        if key not in invalid_data:
            valid={key: value}
            valid_data.update(valid)
valider_donnees(data)

def calculer_moyenne_et_garder_notes(valid_data):
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
calculer_moyenne_et_garder_notes(valid_data)
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
                    print(f"Error: '{unenote}' is not a valid float")
            else:
                print(f"Error: '{notes}' is not a dictionary or does not have a 'moyenne' key")
        somme_moyennes = sum(tab_moyennes)
        moyenne_generale = somme_moyennes / len(petit_dict)
        moyenne_generale=round(moyenne_generale, 2)
        enregistrer_moyenne = {'moyenne générale': moyenne_generale}
        petit_dict.update(enregistrer_moyenne)
calculer_moyenne_generale()
def changer_formats_dates(valid_data):
    for key, value in valid_data.items():
        for char in value[2]:
            if not char.isnumeric():
                value[2]=value[2].replace(char, '/')
        if value[2][-4:].isalnum():
            value[2]=value[2][:-4]+value[2][-2:]
changer_formats_dates(valid_data)

def changer_formats_classes(valid_data):
    for key, value in valid_data.items():
        for char in value[3]:
            if char==' ':
                value[3]=value[3].replace(char, '')
        value[3]=value[3][0]+'eme'+value[3][-1]
changer_formats_classes(valid_data)

def afficher_tout(toprint):
    for key, value in toprint.items():
        value_str = ', '.join(str(x) for x in value)
        print("{}: {}".format(key, value_str))
        print()

def afficher_informations_selon_numero(toprint):
    for key, value in toprint.items():
        if key == num:
            print(key, value)
            return
    print("Data not found")
def affichage_simple(toprint):
    for key, value in toprint.items():
        print(key, value)
    
def afficher_les_cinq_premiers():
    notes_classees={}
    notes_classees=sorted(garder_les_notes.items(), key=lambda kv: kv[1]['moyenne générale'], reverse=True)
    for i in range (5):
        print(notes_classees[i])

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


while True:
    print("Menu:")
    print("1. Afficher les informations valides")
    print("2. Afficher les informations invalides")
    print("3. Afficher les raisons d'invalidité")
    print("4. Afficher par numéros")
    print("5. Afficher les cinq premiers")
    print("6. Ajouter des données")
    print("7. Modifier des données")
    print("8. Quitter")
    choice = input("Entrez un choix: ")

    if choice == '1':
        afficher_tout(valid_data)
    elif choice == '2':
        afficher_tout(invalid_data)
    elif choice == '3':
        affichage_simple(raison_invalidite)
    elif choice=='4':
        num = input("Entrez le numero: ")
        afficher_informations_selon_numero(valid_data)
    elif choice == '5':
        afficher_les_cinq_premiers()
    elif choice == '6':
        new_data = input("Entrez les nouvelles données (code, numero, nom, prénom , date de naissance, classe, notes): ")
        ajouter_données(data, new_data)
    elif choice == '7':
        new_data = input("Entrez les nouvelles données (code, numero, nom, prénom , date de naissance, classe, notes): ")
        modifier_données(invalid_data, new_data)
    elif choice == '8':
        break
    else:
        print("Choix invalide")
