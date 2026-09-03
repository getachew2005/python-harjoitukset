nimet = set()

while True:
    nimi = input("Syötä nimi: ")

    if nimi == "":
        break

    if nimi in nimet:
        print("Aiemmin annettu nimi")
    else:
        print("Uuden henkilön nimi")
        nimet.add(nimi)

print("Annetut nimet:")

for nimi in nimet:
    print(nimi)