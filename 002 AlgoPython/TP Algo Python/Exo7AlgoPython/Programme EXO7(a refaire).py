def letter_to_numbers(letter):
    dictionary = {"abc":'2',"def":'3',"ghi":'4',"jkl":'5',"mno":'6',"pqrs":'7',"tuv":'8',"wxyz":'9'}
    number=""
    for Key, Value in dictionary.items():
        for i in range (len(Key)):
            if Key[i]==letter:
                number=Value*(i+1)
            else:
                continue
        continue
    return number
def numbers_to_letters(letter):
    dictionary = {'a':"0",'b':"1",'c':"2",'d':"3",'e':"4",'f':"5",'g':"6","h":'7','i':"8",'j':"9"}
    number=""
    for Key, Value in dictionary.items():
        if Key==letter:
            number=Value
        else:
            continue
    return number
def spacestozeros(chaine):
    for char in chaine:
        if char==" ":
            char="00"
        else:
            continue
    return char
def charsuccessifs(chaine):
    nouvchaine=[]
    for i in range (len(chaine)):
        if chaine[i]==chaine[i+i]and i<len(chaine):
            nouvchaine=chaine[0:i]
            nouvchaine+='0'
            nouvchaine=chaine[i+1:]
        else:
            continue
    return nouvchaine
phrase=input("Entrez une phrase")
chaine=[]
chaine+=phrase
nouvchaine=charsuccessifs(chaine)
nouvchaine=spacestozeros(chaine)
nouvchaine=letter_to_numbers(letter)
nouvchaine=numbers_to_letters(letter)
print:('La phrase corrigée est: ', nouvchaine)
