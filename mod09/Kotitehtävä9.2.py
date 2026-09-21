class Auto:
    def __int__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.tamanhetkinen_nopeus += muutos

        # Nopeus ei voi ylittää huippunopeutta
        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus

        # Auton nopeus ei voi olla alle 0
        if self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0


# Pääohjelma 
auto = Auto("ABC-123", 180)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

print("Auton tämänhetkinen nopeus:", auto.tämänhetkinen_nopeus, "km/h")

auto.kiihdytä(-200)

print("Auton nopeus hätäjarrutuksen jälkeen:", auto.tämänhetkinen_nopeus, "km/h")