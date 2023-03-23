chainebrute=''
while chainebrute!='Q':    
    def chainesansespaces(chainebrute):
        nouvchainebrute=''
        for caractere in range (len(chainebrute)):
            if chainebrute[caractere]==" ":
                continue
            else:
                nouvchainebrute+=chainebrute[caractere]
        return nouvchainebrute
    def numeroparnumero(chainebrute):
        caractèresvalides=['1','2','3','4','5','6','7','8','9','0',' ']
        chainedecoupee = []
        tmp = ''
        for caractère in chainebrute:
           if caractère not in caractèresvalides:
               chainedecoupee.append(tmp)
               tmp = ''
           else:
               tmp += caractère
        if len(tmp)!=0:
           chainedecoupee.append(tmp)

        return(chainedecoupee)
    def filtrerpuiscompteroperateurs(chainedecoupee):
        numvalide=[]
        numinvalide=[]
        numapriorivalide=[]
        nborange=0
        nbfree=0
        nbexpresso=0
        nbpromobile=0
        for numero in chainedecoupee:
            if len(numero)==9:
                numapriorivalide.append(numero)
            elif len(numero)==0:
                pass
            else:
                numinvalide.append(numero)
        for numeroavalider in numapriorivalide:
            if numeroavalider[0]!='7'or numeroavalider[1] not in ['7','8','6','0','5']:
                    numinvalide.append(numeroavalider)
            else:
                    numvalide.append(numeroavalider)
        for numero in numvalide:
            if numero[1] in ['7','8']:
                nborange+=1
            if numero[1]=='6':
                nbfree+=1
            if numero[1]=='0':
                nbexpresso+=1
            if numero[1]=='5':
                nbpromobile+=1
        #return numvalide, numinvalide, nborange, nbfree, nbexpresso, nbpromobile
        print(f"Orange a {nborange} numeros")
        print(f"Free a {nbfree} numeros")
        print(f"Expresso a {nbexpresso} numeros")
        print(f"Promobile a {nbpromobile} numeros")
        print(end='')
        if len(numvalide)>len(numinvalide):
            for i in range (len(numvalide)-len(numinvalide)):
                numinvalide.append(' ')
        elif len(numvalide)<len(numinvalide):
            for i in range(len(numinvalide)-len(numvalide)):
                numvalide.append(' '*9)
        print("Les numéros valides sont:      les numeros invalides sont:")
        for i in range (len(numvalide)):
            print(numvalide[i]+' '*22+numinvalide[i])
    print('Veuillez entrer une chaine de numéros\n en les séparant par un caractère différent d\'un espace, ou Q pour quitter')
    chainebrute=input()
    if len(chainebrute)==0:
        print('La chaine de saisie est obligatoire')
    else:
        filtrerpuiscompteroperateurs(numeroparnumero(chainesansespaces(chainebrute)))
