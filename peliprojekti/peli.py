print("------------------------")
with open ("peliprojekti/intro.txt", "r", encoding='utf') as tiedosto:
    print(tiedosto.read())
print("------------------------")

esineet = []


def lisaa_esine():
    esine = input("Syötä jokin esine:")
    esineet.append(esine)
    print("Esinettä on lisätty.")


def nayta_esine():
    print("Tavarat:")

    for esine in esineet:
        print(esine)

pisteet = []

def keraa_pisteita():
    piste = input("Syötä pistemäärä: ")
    pisteet.append(piste)
    print("Piste lisätty.")



viholliset = []

def vaista_vihollisia():
    vihollinen = input("Laita jokin vihollinen: ")
    viholliset.append(vihollinen)
    print("Vihollinen lisätty.")

    nopeus = int(input("Valitse juoksunopeus: "))
    if 500 > nopeus >= 400 or (nopeus == 500):
        print("Olet riittävän nopea.")

    elif 399 > nopeus >= 200 or (nopeus == 399):
        print("Olet nopea mutta et riittävästi.")

    elif 199 < nopeus:
        print("Olet hidas tälle pelille.")

    komento = input("Mitä Flash tekee, kun hän kohtaa vihollisen edessään: ")
    print("Flash hahmo " + komento + " edessä olevan vihollisen.")

    piste = int(input("Valitse pelissä keräämä pistemäärä: "))
    if 200 > piste >= 150 or (piste == 200):
        print("Hyvä pistemää.")

    elif 149 < nopeus:
        print("Heikko pistemäärä.")


def tervehdys():
    print("Tervetuloa peliin, nimeltään The Incredible-Flash-peliin!")

def peli():
    print("")
    lisaa_esine()
    nayta_esine()
    keraa_pisteita()
    vaista_vihollisia()


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
            peli()

        elif komento == "2":
            print("------------------------")
            with open ("peliprojekti/ohjeet.txt", "r", encoding='utf') as tiedosto:
                print(tiedosto.read())
            print("------------------------")

        elif komento == "3":
            print("Mukavaa pelipäivää!")

        elif komento == "lopeta":
            print("Peli lopetetaan.")
            break

        else:
            print("Tuntematon komento.")