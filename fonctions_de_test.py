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

def invalidernum(data):
    raison='  numero invalide   '
    raison2='  numéro non alphanumérique   '
    raison3='  numéro contient lettre minuscule   '
    raison_invalidite={}
    invalid_data={}
    for key, value in data.items():
        try:
            if len(key) != 7:        
                invalid_data.update({key: value})
        except TypeError:
            invalid_data.update({key: value})
            try:
                if raison not in value:
                    raison_invalidite[key]+=(raison)
            except:
                raison_invalidite.update({key: raison})
        try:
            if not key.isalnum():
                invalid_data.update({key: value})
        except AttributeError:
            invalid_data.update({key: value})
            try:
                if raison2 not in value:
                    raison_invalidite[key]+=(raison2)
            except:
                raison_invalidite.update({key: raison2})
        try:
            for i in range(len(key)):
                if key[i].islower():
                    invalid_data.update({key: value})
                    try:
                        if raison3 not in value:
                            raison_invalidite[key]+=(raison3)
                    except:
                        raison_invalidite.update({key: raison3})     
        except:
            invalid_data.update({key: value})
            try:
                if raison3 not in value:
                        raison_invalidite[key]+=('liste vide')
            except:
                raison_invalidite.update({key: 'liste vide'})   
    return invalid_data, raison_invalidite


def invalider_nom_et_prénom(data):
    raison_invalidite={}
    invalid_data={}
    raison='   nom invalide   '
    raison2='   prénom invalide   '
    try:
        for key, value in data.items():
            if len(value[0]) < 2 or not value[0][0].isalpha():
                invalid_data.update({key: value})
                try:
                    if raison not in value:
                        raison_invalidite[key]+=(raison)
                except:
                    raison_invalidite.update({key: raison})
            if len(value[1]) < 3 or not value[1][0].isalpha():
                invalid_data.update({key: value})
                try:
                    if raison2 not in value:
                        raison_invalidite[key]+=(raison2)
                except:
                    raison_invalidite.update({key: raison2})
    except:
        invalid_data.update({key: value})
        try:
            if raison2 not in value:
                raison_invalidite[key]+=(raison2)
        except:
            raison_invalidite.update({key: raison2})
    return invalid_data, raison_invalidite

def invalider_notes(data):
    raison_invalidite={}
    invalid_data={}
    raison='   pas de note d\'examen   '
    raison2='  note d\'examen invalide  '
    for key, value in data.items():
        try:
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
                                invalid_data.update({key: value})
                                try:
                                    if raison not in value:
                                        raison_invalidite[key]+=(raison)
                                    else:
                                        pass
                                except:
                                    raison_invalidite.update({key: raison})
                            if float(notexamen)<0 or float(notexamen)>20:
                                invalid_data.update({key: value})
                                try:
                                    if raison2 not in value:
                                        raison_invalidite[key]+=(raison2)
                                    else:
                                        pass
                                except:
                                    raison_invalidite.update({key: raison2})
        except:
            invalid_data.update({key: value})
            try:
                if '  champ vide  ' not in value:
                    raison_invalidite[key]+=('  champ vide  ')
                else:
                    pass
            except:
                raison_invalidite.update({key: '  champ vide  '})
    return invalid_data, raison_invalidite
def invalider_classe(data):
    raison_invalidite={}
    invalid_data={}
    raison='   Classe vide   '
    raison2='   Format de classe invalide   '
    for key, value in data.items():
        try:
            class_level=value[3]
            class_level=class_level.replace(" ", "")
            if (len(class_level))>0:
                if class_level[0] not in ['6','5','4','3']:
                    invalid_data.update({key: value})
                    try:
                        raison_invalidite[key]+=(raison2)
                    except:
                        raison_invalidite.update({key: raison2})
                if class_level[-1] not in ['A','B']:
                    invalid_data.update({key: value})
                    try:
                        raison_invalidite[key]+=(raison2)
                    except:
                        raison_invalidite.update({key: raison2})
            else:
                try:
                    raison_invalidite[key]+=(raison)
                except:
                    raison_invalidite.update({key: raison})
        except:
            invalid_data.update({key: value})
            try:
                raison_invalidite[key]+=('  champ vide  ')
            except:
                raison_invalidite.update({key: '  champ vide  '})
    return invalid_data, raison_invalidite

def changer_formats_dates(valid_data):
    for key, value in valid_data.items():
        for char in value[2]:
            if not char.isnumeric():
                value[2]=value[2].replace(char, '/')
        if value[2][-4:].isalnum():
            value[2]=value[2][:-4]+value[2][-2:]


def changer_formats_devoirs(valid_data):
    for key, value in valid_data.items():
        for char in value[4]:
            if char=='[':
                value[4]=value[4].replace(char, ' Devoir(s) = ')


def changer_formats_notes(valid_data):
    for key, value in valid_data.items():
        for char in value[4]:
            if char in ['|',']','#']:
                value[4]=value[4].replace(char, ' ')


def changer_formats_examens(valid_data):
    for key, value in valid_data.items():
        for char in value[4]:
             if char==':':
                value[4]=value[4].replace(char, ' Examen = ')


def changer_formats_classes(valid_data):
    for key, value in valid_data.items():
        for char in value[3]:
            if char==' ':
                value[3]=value[3].replace(char, '')
        value[3]=value[3][0]+'eme'+value[3][-1]

def afficher_tout(toprint):
    for key, value in toprint.items():
        value_str = ', '.join(str(x) for x in value)
        print("{}: {}".format(key, value_str))
        print()

def afficher_informations_selon_numero(toprint, num):
    for key, value in toprint.items():
        if key == num:
            print(key, value)
            return
    print("Data not found")
def affichage_simple(toprint):
    for key, value in toprint.items():
        print(key, value)
    
def afficher_les_cinq_premiers(garder_les_notes):
    notes_classees={}
    notes_classees=sorted(garder_les_notes.items(),
                          key=lambda kv: kv[1]['moyenne générale'],
                          reverse=True)
    for i in range (5):
        print(notes_classees[i])

