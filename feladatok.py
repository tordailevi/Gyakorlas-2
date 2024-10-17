import random
'''Adott egy lista
lista= [12, 21, 56, 32, -5, -23, 35]'''
'''Paraméterként a fenti listát!'''
'''
1. Hány pozitív szám?
2. Mennyi a negatív számok összege?
3. Mennyi az öttel osztható számok átlaga? 
'''


def poz_szamok_szama(lista):
    i:int=0
    db:int=0

    while(i < len(lista)):
        if (lista[i] > 0):
            db += 1
        i += 1

    return db



def negativ_szamok_osszege(lista):
    i:int=0
    szam:int=0

    while(i < len(lista)):
        if (lista[i] < 0):
            szam += lista [i]
        i +=1

    return szam

def otteloszthato(lista):
    i:int=0
    osszeg:int=0
    db:int=0
    while(i < len(lista)):
        if (lista[i]%5==0):
            osszeg += lista[i]
            db += 1
        i += 1
    atlag:float = osszeg / db

    return atlag
    
'''Függvény: éremdobás-10db fej vagy írás, eredményt eltárolja egy listában
A függvény térjen vissza a listával.'''

def eremdobas():
    eredmenyek_lista=[]
    i:int=0
    while(i <10):
        erem:int=int(random.random() * 2) +1
        if(erem==1):
            eredmenyek_lista.append("fej")
        elif(erem==2):
            eredmenyek_lista.append("iras")
        i += 1
    return eredmenyek_lista

def fej_dobasok(eredmenyek_lista):
    i:int=0
    fej:int=0
    

    while (i < len(eredmenyek_lista)):
        
        if (eredmenyek_lista[i] == "fej"):
            fej += 1
        i += 1
    return fej

def kockadobas():
    kockadobasok=[]
    i=0
    while(i<200):
        dobas:int=int(random.random()*7)+1
        if(dobas ==1):
            kockadobasok.append(dobas)
            i += 1
        elif(dobas ==2):
            kockadobasok.append(dobas)
            i += 1
        elif(dobas ==3):
            kockadobasok.append(dobas)
            i += 1
        elif(dobas ==4):
            kockadobasok.append(dobas)
            i += 1
        elif(dobas ==5):
            kockadobasok.append(dobas)
            i += 1
        elif(dobas ==6):
            kockadobasok.append(dobas)
            i += 1
    return kockadobasok, dobas


def kockadobas_szamolo(kockadobasok, dobas):
    i:int=0
    egyes:int=0
    kettes:int=0
    harmas:int=0
    negyes:int=0
    otos:int=0
    hatos:int=0
    while (i < len(kockadobasok)):
        if (dobas == 1):
            egyes += 1
            i += 1

        elif (dobas == 2):
            kettes += 1
            i += 1

        elif (dobas == 3):
            harmas += 1
            i += 1

        elif (dobas == 4):
            negyes += 1
            i += 1

        elif (dobas == 5):
            otos += 1
            i += 1

        elif (dobas == 6):
            hatos += 1
            i += 1
    i += 1
    return egyes, kettes, harmas, negyes, otos, hatos

def cinkeltkocka():
    cinkelt_lista=[1, 2, 3, 4, 5, 6, 6, 6]
    dobas:int=int(random.random()(cinkelt_lista)*20)
    print(f"{dobas}")