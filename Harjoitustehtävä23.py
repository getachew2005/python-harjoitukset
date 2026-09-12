pelit = []

peli = input("Anna ensimmäinen peli tai lopeta painamalla Enter: ")
while peli != "":
    pelit.append(peli)
    peli = input("Anna seuraava peli tai lopeta painamalla Enter: ")

print(pelit)