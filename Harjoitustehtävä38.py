class Elokuva:
    def __init__(self, nimi, valmistumisvuosi, lausahdus="Wakanda forever"):
        self.nimi = nimi
        self.valmistumisvuosi = valmistumisvuosi
        self.lausahdus = lausahdus

    def sano(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " sanoo: " + self.lausahdus)
        return

class Elokuvateatteri:
    def __init__(self):
        self.elokuvat = []

    def elokuva_julkaistaan(self, elokuva):
        self.elokuvat.append(elokuva)
        print(elokuva.nimi + " lisätty elokuvateatteriin")
        return

    def elokuva_poistetaan(self, elokuva):
        self.elokuvat.remove(elokuva)
        print(elokuva.nimi + " poistettu teatterista")
        return

    def hyvästele_elokuvia(self):
        for elokuva in self.elokuvat:
            elokuva.sano(1)

# Pääohjelma

elokuva1 = Elokuva("Avengers Infinity War", 2018)
elokuva2 = Elokuva("Avengers Endgame", 2019, "I am Iron Man")

elokuvateatteri = Elokuvateatteri()

elokuvateatteri.elokuva_julkaistaan(elokuva1)
elokuvateatteri.elokuva_julkaistaan(elokuva2)
elokuvateatteri.hyvästele_elokuvia()

elokuvateatteri.elokuva_poistetaan(elokuva1)
elokuvateatteri.hyvästele_elokuvia()