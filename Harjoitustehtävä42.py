class Osoite:
    def __init__(self, katu, postinumero, kaupunki):
        self.katu = katu
        self.postinumero = postinumero
        self.kaupunki = kaupunki

class Henkilö:
    def __init__(self, nimi):
        self.nimi = nimi
        self.osoite = None

    def aseta_osoite(self, osoite):
        self.osoite = osoite

henkilö = Henkilö("Toby")
osoite = Osoite("Takomotie 27", "00380", "Helsinki")

henkilö.aseta_osoite(osoite)

print(henkilö.nimi)
print(henkilö.osoite.katu)
print(henkilö.osoite.postinumero)
print(henkilö.osoite.kaupunki)






