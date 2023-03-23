def choixutilisateur():
    ordre=0
    couleur=0
    choix=0
    choices=[]
    while True:
        print('Veuillez entrer l\'ordre de la matrice\n qui devra être supérieur à 5')
        ordre=int(input())
        if ordre>5:
            choices.append(ordre)
            print('Veuillez choisir 1 pour la couleur Rouge ou 2 Pour la couleur Bleue')
            couleur=int(input())
            if couleur==1 or couleur ==2:
                choices.append(couleur)
                print('Où voulez-vous mettre la couleur Bleue? Tapez 1 pour la mettre en haut, ou 2 pour la mettre en bas.')
                choix=int(input())
                if choix==1 or choix==2:
                    choices.append(choix)
                    return choices
                
    return False

def runmatrice(choices):
    ordre=choices[0]
    couleur=choices[1]
    choix=choices[2]
    matrice=[]
    tmp=''
    liste=[]
    for i in range (ordre):
        for j in range (ordre):
            if i==j:
                tmp='o'
            elif i>j:
                if choix==1:
                    tmp="\033[0;31mo\033[00m"
                if choix==2:
                    tmp="\033[34mo\033[0m"
            else:
                if choix==1:
                    tmp="\033[34mo\033[0m"
                if choix==2:
                    tmp="\033[0;31mo\033[00m"
            liste.append(tmp)
        matrice.append(liste)
        liste=[]
    for liste in matrice:
        for valeur in liste:
            print(valeur, end='  ')
        print()

runmatrice(choixutilisateur())
