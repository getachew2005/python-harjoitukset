import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        self.nopeus = max(0, min(self.nopeus, self.huippunopeus))

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


autot = []
for i in range(1, 11):
    autot.append(Auto(f"ABC-{i}", random.randint(100, 200)))


while max(auto.kuljettu_matka for auto in autot) < 10000:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)


print("Rekisteri   Huippunopeus   Nopeus   Matka")
for auto in autot:
    print(auto.rekisteritunnus, auto.huippunopeus,
          auto.nopeus, auto.kuljettu_matka)
