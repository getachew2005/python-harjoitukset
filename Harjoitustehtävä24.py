pelit = []

kokonimi = input("Anna ensimmäinen pelin nimi tai lopeta painamalla Enter: ")
while kokonimi != "":
    pelit.append(kokonimi)
    kokonimi = input("Anna seuraava pelin nimni tai lopeta painamalla Enter: ")

for peli in pelit:
    print(f"Pelaa peliä {peli}!")