
komento = input("Anna lasku (plus, miinus, kerto, lopeta): ")
while komento != "lopeta":
    if komento == "virhe":
        break

    print("Suoritan toiminnon: " + komento)
    komento = input("Anna lasku (plus, miinus, kerto, lopeta): ")
else:
    print("Näkemiin.")
print("Toiminnot lopetettu.")




