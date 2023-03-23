def recupmotsnew(phrase):
    mots=''
    for i in range (len(phrase)):
        if phrase[i]==" " and phrase[i+1]==" ":
            continue
        else:
            mots+=phrase[i]
    return mots
