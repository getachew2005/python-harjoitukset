class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäära):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäära = sivumäära

    def tulosta_tiedot(self):
        print(self.nimi, self.kirjoittaja, self.sivumäära)


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(self.nimi, self.päätoimittaja)


aku = Lehti("Aku Ankka", "Aki Hyyppää")
hytti = Kirja ("Hytti n:o 6", "Rosa Liksom", 200)

aku.tulosta_tiedot()
hytti.tulosta_tiedot()