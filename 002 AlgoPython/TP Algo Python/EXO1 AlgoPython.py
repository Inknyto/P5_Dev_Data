lesMois=["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"];
theMonthes=["January","February","March","April", "May","June","July","August","September","October","November", "December"]
def cmptr(lesMois):
    cpt=0
    for i in range (len(lesMois)):
        cpt+=1
    return cpt

print("********************************************************")
print("********************* MENU ***************************")
print("1. Tapez 1 pour le francais")
print("2. Tapez 2 pour l'anglais ")
print("3. Tapez 3 pour quitter")
print("********************************************************")
choix=int(input())
if choix==1:
    print(11*4*"_")
    print(end='|')
    for i in range (0,12,3):
        x=cmptr(lesMois[i])
        if x<10:
            mult=10-x
        print(lesMois[i]+mult*" ", end="|")
    print(end="\n")
    print(11*4*"_")
    print(end='|')
    
    for j in range (1,12,3):
        x=cmptr(lesMois[j])
        if x<10:
            mult=10-x
        print (lesMois[j]+mult*" ", end="|")
    print(end="\n")
    print(11*4*"_")
    print(end='|')
    
   
    
    for k in range (2,12,3):
        x=cmptr(lesMois[k])
        if x<10:
            mult=10-x
        print(lesMois[k]+mult*" ", end="|")
    print(end="\n")
    print(11*4*"_")
elif choix==2:
    print(11*4*"_")
    print(end='|')
    for i in range (0,12,3):
        x=cmptr(theMonthes[i])
        if x<10:
            mult=10-x
        
        print(theMonthes[i]+mult*" ", end="|")
    print(end="\n")
    print(11*4*"_")
    print(end='|')
    
    for j in range (1,12,3):
        x=cmptr(theMonthes[j])
        if x<10:
            mult=10-x
        print(theMonthes[j]+mult*" ", end="|")
    print(end="\n")
    print(11*4*"_")
    print(end='|')
    
    
    for k in range (2,12,3):
        x=cmptr(theMonthes[k])
        if x<10:
            mult=10-x
        print(theMonthes[k]+mult*" ", end="|")
    print(end="\n")
    print(11*4*"_")
    
elif choix==3:
    quit()
else:
    for i in range (0,12,3):
        print(lesMois[i], end=" ")
    print(end="\n")
    for j in range (1,12,3):
        print(lesMois[j], end=" ")
    print(end="\n")
    for j in range (2,12,3):
        print(lesMois[j], end=" ")
    print(end="\n")
