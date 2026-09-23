import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False

    def tulosta_tilanne(self):
        for auto in self.autot:
            print(auto.rekisteritunnus,
                  auto.huippunopeus,
                  auto.nopeus,
                  auto.kuljettu_matka)


autot = []

for i in range(1, 11):
    autot.append(Auto(f"ABC-{i}", random.randint(100, 200)))


kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1

    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()