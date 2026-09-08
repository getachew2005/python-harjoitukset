komento = input("Syötä komento:")
while komento != "lopeta":
    if komento == "STOP":
        break
    print("Suoritan toiminnon: " + komento)
    komento = input("Anna jokin komento: ")
else:
    print("Näkemiin.")
print("Toiminnot lopetettu.")