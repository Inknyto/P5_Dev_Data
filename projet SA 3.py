from lect_fichiers import*
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

data=ouvrir_et_lire_xml()
libelles={'mat':'MATH','fr':'FR','hg':'HG','ang':'ANG','pc':'PC','sv':'SVT'}
for key, value in data.items():
    data[key]={'Nom': value[0],
    'Prenom': value[1],
    'Date_de_Naissance':value[2],
    'Classe':value[3],
    'Notes':value[4]}
for key, value in data.items():
    notes={}
    if not value['Notes']==None:
        value['Notes']=value['Notes'].split('#')
        for matiere in value['Notes']:
             for i in range(len(matiere)):
                for j in range(len(matiere)):
                    if matiere[i]=='[' and matiere[j]==']':
                        libellé=matiere[:i]
                        serienotes=matiere[i+1:j]
                        try:
                            notesdevoir, notexamen=serienotes.split(':')
                        except ValueError:
                            notexamen='pas de note d\'examen'
                        tabn=list(notesdevoir.split('|'))
                        while len(libellé) > 0 and not libellé[0].isalnum():
                            libellé = libellé[1:]
                        for clef, valeur in libelles.items():    
                            if libellé.lower().startswith(clef):
                                libellé=valeur
                        dico={libellé:{'notes devoir':tabn,
                        'note d\'examen':notexamen}}   
             notes.update(dico)
    value['Notes']=notes
    

from datetime import datetime    
class SubjectClass:
    def __init__(self, *args):
        for i, subject_values in enumerate(args):
            setattr(self, f"Subject_{i+1}", subject_values)

class Dict2Class:
    def __init__(self, my_dict):
        for key, value in my_dict.items():
                setattr(self, key, value)
    def invalidname(self):
        if self.Nom!=None:
            if len(self.Nom) < 2 or not self.Nom.isalpha():
                self.invalide = True
                try:
                    self.raison+=' Nom invalide '
                except AttributeError:
                    self.raison=' Nom invalide '
            if len(self.Prenom) < 3 or not self.Prenom.isalpha():
                self.invalide=True
                try:
                    self.raison+=' Prénom invalide '
                except AttributeError:
                    self.raison=' Prénom invalide '
            
    def changer_formats_dates(self):
        try:
            for char in self.Date_de_Naissance:
                if not char.isnumeric():
                    self.Date_de_Naissance=self.Date_de_Naissance.replace(char, '/')
                if self.Date_de_Naissance[-4:].isalnum():
                    self.Date_de_Naissance=self.Date_de_Naissance[:-4]+self.Date_de_Naissance[-2:]
                while len(self.Date_de_Naissance) > 0 and not self.Date_de_Naissance[0].isalnum():
                    self.Date_de_Naissance = self.Date_de_Naissance[1:]
        except TypeError:
            return
    def invaliddate(self):
        invalide=False
        try:
            if not str(type(self.Date_de_Naissance))=="<class 'datetime.date'>" and not self.Date_de_Naissance==None:
                self.Date_de_Naissance = datetime.strptime(self.Date_de_Naissance, '%d/%m/%y').date()
        except ValueError:
            invalide=True
        if invalide==True:
            self.invalide=True
            try:
                self.raison+=' Date invalide '
            except AttributeError:
                self.raison=' Date invalide '
    def invalidernotes(self):
        invalide=False
        for key, value in vars(self).items():
            if len(value['notes devoir'])==0 or value['note d\'examen']=="pas de note d'examen" or float(value['note d\'examen'])>20 or float(value['note d\'examen'])<0:
                invalide=True
        if invalide==True:
            self.invalide=True
            try:
                self.raison+=' Note invalide '
            except AttributeError:
                self.raison=' Note invalide '
    def invaliderclasse(self):
        inv=False
        try:
            self.Classe=self.Classe.replace(' ', '')
        except AttributeError:
            self.Classe=self.Classe
        finally:
            try:
                if len(self.Classe)>0:
                    if self.Classe[0] not in ['6','5','4','3']:
                        self.invalide=True
                        inv=True
                    if self.Classe[-1] not in ['A','B']:
                        self.invalide=True
                        inv=True
            except TypeError:
                self.invalide=True
                inv=True
            else:
                self.Classe=self.Classe[0]+' eme '+self.Classe[-1]
        if inv==True:
            try:
                if ' Classe invalide ' not in self.raison:
                    self.raison+=' Classe invalide '
            except AttributeError:
                self.raison=' Classe invalide '
    def calculermoyenne(self):
        tabmoygen=[]
        sommoygen=0
        if not hasattr(self, 'invalide'):
            for key, value in vars(self).items():
                tabdev=[]
                somdev=0
                for d in value['notes devoir']:
                    d=d.replace(',', '.')
                    if not isfloat(d):
                        continue
                    d=float(d)
                    tabdev.append(d)
                    somdev=sum(tabdev)
                    moydev=somdev/len(tabdev)
                value['note d\'examen']=float(value['note d\'examen'])
                moyenne=(moydev+(2*value['note d\'examen']))/3
                moyenne=round(moyenne, 2)
                value.update({'moyenne':moyenne})
                tabmoygen.append(value['moyenne'])
            sommoygen=sum(tabmoygen)
            moygen=sommoygen/len(tabmoygen)
            self.moyennegenerale=moygen
   
def creation():
    for key,value in data.items():
        try:
            data[key]['Notes']=Dict2Class(data[key]['Notes'])  
            data[key]=Dict2Class(data[key])
        except TypeError:
            continue
creation()
def validation():
    for key, value in data.items():
        value.invaliderclasse()
        value.invalidname()
        value.changer_formats_dates()
        value.invaliddate()
        value.Notes.invalidernotes()
        
validation()
dictinvalide={key:value for key, value in data.items() if hasattr(value, 'invalide') or hasattr(value.Notes, 'invalide')}
dictvalide={key:value for key, value in data.items() if value not in dictinvalide.values()}
for key, value in dictvalide.items():    
    value.Notes.calculermoyenne()
