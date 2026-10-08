print("------------------------")
with open ("peliprojekti/intro.txt", "r", encoding='utf') as tiedosto:
    print(tiedosto.read())
print("------------------------")

esineet = []


def lisaa_esine():
    esine = input("Syötä pelissä oleva esine:")
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
    vihollinen = input("Laita The Incredible Flashissa oleva vihollinen: ")
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
        print("Hyvä pistemää. Voitit tason.")

    elif 149 < piste:
        print("Heikko pistemäärä. Hävisit tason.")


    print("----------------------------------------------------------------")
    print("Pelasit ensimmäistä tasoa ajoissa, ja pistemääräsi on 161/200.")
    print("----------------------------------------------------------------")


    muokkaus = input("Koska olet kerännyt vähintään 160 pistettä, pääset vapaaehtoisesti muokkaamaan Flashin puvun väriä. Värejä on vain kuusi. Valitse väri: ")
    if muokkaus == "sininen":
        print("Flashin punainen puku on vaihdettu siniseen pukuun.")

    elif muokkaus == "vihreä":
        print("Pelihahmo Flashin puku on muokattu vihreään pukuun.")

    elif muokkaus == "keltainen":
        print("Flashin punainen puku on vaihdettu keltaiseen pukuun.")

    elif muokkaus == "violetti":
        print("Pelihahmo Flashin puku on muokattu violettiin pukuun.")

    elif muokkaus == "oranssi":
        print("Flashin punainen puku on vaihdettu oransiin pukuun.")


    piste = int(input("Valitse The Incredible Flash-pelissä keräämä pistemäärä: "))
    if 200 > piste >= 150 or (piste == 200):
        print("Hyvä pistemää.")
    
    elif 149 < piste:
        print("Heikko pistemäärä.")


    print("----------------------------------------------------------------")
    print("Pelasit toista tasoa ajoissa, ja pistesi on 171/200.")
    print("----------------------------------------------------------------")


    päivitys = input("Olet kerännyt vähintään 170 pistettä, mitä haluat päivittää hahmosta: ")
    if päivitys == "voima":
        print("Olet päivittänyt pelihahmo Flashin voiman tasoa.")

    elif päivitys == "kestävyys":
        print("Olet päivittänyt Fashin kestävyyttä.")

    elif päivitys == "nopeus":
        print("Olet päivittänyt pelihahmon nopeutta.")


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
    print("Tervettuloa The Incredible Flash-peliin " + kayttaja + "!")

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