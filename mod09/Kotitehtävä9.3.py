class Auto:
    def __int__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.tamanhetkinen_nopeus += muutos

        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus

        if self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.tämänhetkinen_nopeus * tunnit


# Pääohjelma 
auto = Auto("ABC-123", 180)

auto.tämänhetkinen_nopeus = 60
auto.kuljettu_matka = 2000

auto.kulje(1.5)

print("Auton kuljettumatka:", auto.kuljettu_matka, "km")