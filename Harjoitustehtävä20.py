komento = input("Syötä komento:")
while komento != "lopeta":
    if komento == "STOP":
        break
    print("Suoritan komennon: " + komento)
    komento = input("Syötä komento: ")
print("Toiminto lopetettu.")
