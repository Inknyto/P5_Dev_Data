{data=read.csv("/home/nyto/Téléchargements/Donnees_Projet_Python_DataC5.csv")
library(validate)
library("stringr")
L <- 'AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn'}
#valider numero
{validnum<- validator(nchar(Numero)==7,
                     toupper(Numero)==Numero)
out<- confront(data, validnum)
invnum=violating(data, out)}

{isvalideprenom<-nchar(data$Prénom) >= 3 & grepl(substr(data$Prénom, 1, 1), L)
isvalidenom<-nchar(data$Nom) >= 2 & grepl(substr(data$Nom, 1, 1), L)
datatest=data
datatest$Prenom_valide<-isvalideprenom
datatest$Nom_valide<-isvalidenom}
#valider nom prénoml
{validname <- validator( Prenom_valide==TRUE,
                        Nom_valide==TRUE)
output <- confront(datatest, validname)
invname <- violating(datatest, output)
invname<-(within(invname, rm(Prenom_valide, Nom_valide))  )}
#changer formats dates
i=1
for (line in data$Date.de.naissance){
  line=gsub("-", "/", line)
  line=gsub(" ", "/", line) 
  line=gsub("[|]", "/", line)
  line=gsub("[.]", "/", line)
  line=gsub("_", "/", line)
  line=gsub(",", "/", line)
  line=gsub(":", "/", line)
 
  if (!is.na(as.numeric((substr(line, nchar(line) - 3, nchar(line))))))
  {line <- paste(substr(line, 1, nchar(line) - 4) , substr(line, nchar(line) - 1, nchar(line)), sep='')}
  
  while (nchar(line) > 0 & substr(line,1,1)=='/') {line <- substr(line, 2, nchar(line))}
  
  if(grepl('[A-Za-z]', line))  {moisenchar=str_split_i(line, '/', 2)
  if (startsWith(moisenchar, 'mar'))      {line=gsub(moisenchar, "03", line)}
  else if (startsWith(moisenchar, 'de')) {line=gsub(moisenchar, "12", line)}
  else if (startsWith(moisenchar, 'fe')) {line=gsub(moisenchar, "02", line)}}
  
  data$Date.de.naissance[i]=line
  i=i+1
}
#valider dates
{validdate<- validator(
  !is.na(as.Date(Date.de.naissance, "%d/%m/%y")),
  Date.de.naissance!='07/06/199Ç'
)
out<-confront(data, validdate)
invdate=violating(data, out)}
#changer formats classes
{firstchar='6543'
lastchar='AB'
i=0}
for (line in data$Classe){line=gsub(' ', "", line)
i=i+1
if(grepl(substr(line, 1, 1), firstchar) & grepl(substr(line, nchar(line) , nchar(line)  ), lastchar))
{data$Classe[i]=paste(substr(line, 1, 1), substr(line, nchar(line), nchar(line)), sep=' eme ')}}
data
#invalider classe
{firstchar='6543'
lastchar='AB'
v=vector()}
for (line in data$Classe){
  a=grepl(paste0('[',substr(line, 1, 1),']'), firstchar)
  b=grepl(paste0('[',substr(line, nchar(line), nchar(line)),']'), lastchar)
  g<-a*b
  g=c(g)
  v <- append(v, as.logical(g))
}

{datatest=data
datatest$isclassevalide=v
validtest<- validator(isclassevalide==TRUE)
out<- confront(datatest, validtest)
invtest=violating(datatest, out)
invclasse=within(invtest, rm(isclassevalide))}

#invalider notes
i=0
notescalculees=vector()
for(line in data$Note){
  line=strsplit(line, split='#')
  notes=vector()
  for (chainenotes in line){
    for (matiere in chainenotes){
      for (i in 1:nchar(matiere)){
        for (j in 1:nchar(matiere)){
          
          if (substr(matiere, i, i)=='[' & substr(matiere, j, j)==']')
          {
            libelle<-(substr(matiere, 1, i-1))
            serienotes<-(substr (matiere, i+1, j-1))
            notesdevoirs<-str_split_i(serienotes, ':', 1)
            notexamen<-str_split_i(serienotes, ':', 2)
            tabdevoir<-strsplit(notesdevoirs, split='[|]')
            tabdevoir<-tabdevoir[[1]]
            tabdevoir<-gsub('[,]','.',tabdevoir)
            notexamen<-gsub('[,]','.',notexamen)
            tabdevoir<-as.numeric(tabdevoir)
            notexamen=as.numeric(notexamen)
            sommedevoir<-sum(tabdevoir)
            moydevoir<-sommedevoir/length(tabdevoir)
            moyenne<-(moydevoir+2*notexamen)/3
            moyenne<-round(moyenne, digits = 2)
            notesdefinitif<-c('matiere'=libelle, 'notes devoir'=tabdevoir , 'note examen'=notexamen, 'moyenne'=moyenne )
          }
        }
      }
      notes<-append(notes, notesdefinitif)
    }
  }
  notescalculees<-append(notescalculees, list(notes))
}
{datatest=data
data$Notes_calculees<-datatest$Notes_Calculees
datatest <- subset(datatest, select = -c(Note))
datatest$Notes_Calculees=notescalculees

v<-vector()}
for (note in notescalculees){v<-append(v, NA %in% note)}
{datatest$Noteinvalide<-v

validnote<- validator(Noteinvalide==FALSE)
out<- confront(datatest, validnote)
invtest=violating(datatest, out)
invnote<-within(invtest, rm(Noteinvalide))


invname<-as.data.frame(invname)
invdate<-as.data.frame(invdate)
invnote<-as.data.frame(invnote)
invclas<-as.data.frame(invclasse)
numinvalide<- c(invname$Numero,invdate$Numero,invnote$Numero,invclas$Numero)

invalid_data=data.frame(matrix(nrow = 0, ncol = 6))
valid_data=data.frame(matrix(nrow = 0, ncol = 6))
colnames(valid_data) = c( 'CODE','Numero','Nom','Prénom Date.de.naissance','Classe','Note')
colnames(invalid_data)<-colnames(valid_data)
names(invalid_data)<-names(valid_data)}
#invalider donnees
for (i in  1:nrow(data)){
  if (data[i,2]%in% numinvalide){
    invalid_data<- rbind(invalid_data, data[i,])
  }
}
#valioder données
{data$Notes_calculees<-notescalculees
data<-within(data, rm(Note))
data}
for (i in  1:nrow(data)){
  if (!(data[i,2] %in% numinvalide)){
    valid_data<- rbind(valid_data, data[i,])
  }
}
#Afficher
while (TRUE){
  print('1 Pour afficher les données valide')
  print('2 Pour afficher les données invalide')
  print('3 Pour afficher par raison d\'invalidité')
  print('4 Pour quitter')
  choix<-readline("")
  if(choix=='1'){View(valid_data)}
  else if(choix=='2'){View(invalid_data)}
  else if(choix=='3'){
    print('1 Pour afficher les numéros invalides') 
    print('2 Pour afficher les noms ou prénoms invalides') 
    print('3 Pour afficher les dates de naissance invalides')
    print('4 Pour afficher les classes invalides')
    print('5 Pour afficher les notes invalides')
    print('6 Pour quitter')
    choix2<-readline("")
    
    if (choix2=='1'){
      View(invnum)
    }
    else if (choix2=='2'){
      View(invname)
    }
    else if (choix2=='3'){
      View(invdate)
    }
    else if (choix2=='4'){
      View(invclas)
    }
    else if (choix2=='5'){
      View(invnote)
    }
    else if (choix2=='6'){
      break
    }
    else{
      print('Choix invalide')
    }
  }
  else if(choix=='4'){
    break
  }
  else{print('Choix invalide')}
}
