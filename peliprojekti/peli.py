kayttaja = input("Anna nimesi: ")
ika = int(input("Anna ikä: "))

if ika < 12:
    print("Olet todella nuori pelaamaan.")
else:
    print("Tervettuloa The Incredible Flash-peliin", kayttaja, "!")

    while True:
        print("\nPÄÄVALIKKO")
        print("1 - Aloita peli")
        print("2 - Ohjeet")
        print("3 - Tervehdys")
        print("lopeta - Lopeta peli")

        komento = input("Anna komento: ")

        if komento == "1":
            print("The Incredible Flash-peli alkaa!")

        elif komento == "2":
            print("Tässä pelissä sinun tehtäväsi on selviytyä.")

        elif komento == "3":
            print("Mukavaa pelipäivää!")

        elif komento == "lopeta":
            print("Peli lopetetaan.")
            break

        else:
            print("Tuntematon komento.")


