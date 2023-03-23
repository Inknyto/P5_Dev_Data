def choixutilisateur():
    ordre = 0
    couleur = 0
    choix = 0
    choices = []
    while True:
        print('Veuillez entrer l\'ordre de la matrice\n qui devra être supérieur à 5')
        ordre = int(input())
        if ordre > 5:
            choices.append(ordre)
            print('Veuillez choisir une couleur: 1 pour Rouge, 2 pour Bleue, 3 pour Vert, 4 pour Jaune, 5 pour Rose, 6 pour Noir')
            couleur = int(input())
            if couleur in range(1, 7):
                choices.append(couleur)
                print('Où voulez-vous mettre la couleur? Tapez 1 pour la mettre en haut, ou 2 pour la mettre en bas.')
                choix = int(input())
                if choix in [1, 2]:
                    choices.append(choix)
                    return choices
            return False
def runmatrice(choices):
    ordre = choices[0]
    couleur = choices[1]
    choix = choices[2]
    matrice = []
    tmp = ''
    liste = []
    color_dict = {
        1: "\033[0;31mo\033[00m",
        2: "\033[34mo\033[0m",
        3: "\033[0;32mo\033[00m",
        4: "\033[0;33mo\033[00m",
        5: "\033[0;35mo\033[00m",
        6: "\033[0;30mo\033[00m"
    }

    for i in range(ordre):
        for j in range(ordre):
            if i == j:
                tmp = 'o'
            elif i > j:
                if choix == 1:
                    tmp = color_dict[couleur]
                if choix == 2:
                    tmp = color_dict[couleur]
            else:
                if choix == 1:
                    tmp = color_dict[couleur]
                if choix == 2:
                    tmp = color_dict[couleur]
            liste.append(tmp)
        matrice.append(liste)
        liste = []

    for liste in matrice:
        for valeur in liste:
            print(valeur, end='  ')
        print()
    runmatrice(choixutilisateur())




