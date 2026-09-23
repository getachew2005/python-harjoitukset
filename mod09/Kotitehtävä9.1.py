class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0


# Pääohjelma
auto = Auto("ABC-123", 142)

print("Rekisteritunnus:", auto.rekisteritunnus)
print("Huippunopeus:", auto.huippunopeus, "km/h")
print("Nopeus:", auto.nopeus, "km/h")
print("Kuljettu matka:", auto.kuljettu_matka, "km")         





        
   

auto1 = Auto("ABC-123",142)
print(f"Rekisteritunnus {auto1.rekisteritunnus} nopeus {auto1.huippunopeus} tämänhetkinen nopeus {auto1.tamanhetkinen_nopeus} kuljettu matka {auto1.kuljettu_matka}")