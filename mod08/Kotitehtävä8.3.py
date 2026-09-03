lentokentat = {}

while True:
    print("\n1 - Anna uusi lentokenttä")
    print("2 - Hae lentokone asema")
    print("3 - Lopeta")

    valinta = input("Valitse jokin toiminto: ")

    if valinta == "1":
        icao = input("Syötä ICAO-koodi: ")
        nimi = input("Anna lentokentän nimi: ")

        lentokentat[icao] = nimi
        print("Lentokenttä tallennettu.")

    elif valinta == "2":
        icao = input("Syötä ICAO-koodi: ")

        if icao in lentokentat:
            print(lentokentat[icao])
        else:
            print("Lentokone asema ei löytynyt.")

    elif valinta == "3":
        break

    else:
        print("Virheellinen valitsema valinta.")