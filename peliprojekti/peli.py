esineet = []


def lisaa_esine():
    esine = input("Syötä jokin esine:")
    esineet.append(esine)
    print("Esinettä on lisätty.")


def nayta_esine():
    print("Tavarat:")

    for esine in esineet:
        print(esine)


def tervehdys():
    print("Tervetuloa peliin, nimeltään The Incredible-Flash-peliin!")


kayttaja = input("Anna nimesi: ")
ikä = int(input("Anna ikä: "))

if ikä < 12:
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