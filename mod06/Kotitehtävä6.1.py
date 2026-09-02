import random

lukumaara = int(input("Anna arpakuutioiden määrä: "))

summa = 0

for i in range(lukumaara):
    silmaluku = random.randint(1, 6)
    summa += silmaluku

print("Silmälukujen lukusumma on:", summa)