class Auto:
    def __int__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = huippunopeus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0
    def kiihdyta(self, muutos):
        if self.tamanhetkinen_nopeus - muutos <= 0:
            self.tamanhetkinen_nopeus = 0
        elif self.tamanhetkinen_nopeus + muutos >= self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        else:
            self.tamanhetkinen_nopeus += muutos

auto1 = Auto("ABC-123", 142)
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
print(f"Auton nopeus nyt: {auto1.tamanhetkinen_nopeus}")
auto1.kiihdyta
print(f"Auton nopeus nyt: {auto1.tamanhetkinen_nopeus}")
            





        
   

auto1 = Auto("ABC-123",142)
print(f"Rekisteritunnus {auto1.rekisteritunnus} nopeus {auto1.huippunopeus} tämänhetkinen nopeus {auto1.tamanhetkinen_nopeus} kuljettu matka {auto1.kuljettu_matka}")