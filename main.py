import feladatok
lista = [12, 21, 56, 32, -5, -23, 35]

print("1. feladat")
db:int=feladatok.poz_szamok_szama(lista)
print(f"A pozitív számok száma: {db}")


print("2.feladat")
szam:int=feladatok.negativ_szamok_osszege(lista)
print(f"A negatív számok összege: {szam}")

print("3. feladat")
atlag:float=feladatok.otteloszthato(lista)
print(f"Az öttel osztható számok átlaga: {atlag}")