ch=''
while ch!='Q':
    def suppesp(texte):
        nouvtexte = ""
        for i in range(len(texte)):
            if i < len(texte) - 1 and texte[i] == " " and texte[i + 1] == " ":
                continue
            else:
                 nouvtexte += texte[i]
        return nouvtexte
    def phraseparphrase(texte):
        ch=[]
        phrase=''
        for i in range (len(texte)):
            if texte[i] in['A','Z','E','R','T','Y','U','I','O','P','Q','S','D','F','G','H','J','K','L','M','W','X','C','V','B','N']  or (texte[i] in ['A','Z','E','R','T','Y','U','I','O','P','Q','S','D','F','G','H','J','K','L','M','W','X','C','V','B','N'] and i == 0):
                for j in range(i, len(texte)):
                    phrase += texte[j]
                    if texte[j] in ['?', '.', '!']:
                        if len(phrase)>=25:
                            ch.append(phrase)
                        phrase = ''
                        break
        return ch
    def phrasedanstextenecontientpasedecaracterespec(texte):
        lettresmin=['a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n']
        lettresMAJ=['A','Z','E','R','T','Y','U','I','O','P','Q','S','D','F','G','H','J','K','L','M','W','X','C','V','B','N']
        lettresaccent=['é','è','ç','à','ô','û','ù',' ']
        chiffres=[1,2,3,4,5,6,7,8,9,0]
        carnorm=[',','?',';','.',':','/','!']
        apostrophe=['\'']
        ponctuations=['?', '.', '!']
        nouvtexte=[]
        caracteresacceptables=lettresmin+lettresMAJ+lettresaccent+chiffres+carnorm+apostrophe
        i=0
        for phrase in texte:
            valide=True
            for lettre in phrase:
                if lettre not in caracteresacceptables:
                    valide=False
                    break
            if valide==True:
                nouvtexte.append(phrase)
        return nouvtexte    
    def programmedefinitif(texte):
        return phrasedanstextenecontientpasedecaracterespec((phraseparphrase(suppesp(texte))))
    print('Veuillez entrer un texte, ou Q pour quitter le programme')
    ch=input()
    if len(ch)==0:
        print('La chaîne de saisie est obligatoire')
    else:
        print('Le texte corrigé est:', programmedefinitif(ch))


    


    

