import os
while True:
        tiedoston_nimi = int(input("Tiedoston nimi: "))
        try:
                with open (tiedoston_nimi, "r") as tiedosto:
                        data = tiedosto.read()
                        print(data)
                        break
        except FileNotFoundError:
                print("tiedostoa ei löydy:/")