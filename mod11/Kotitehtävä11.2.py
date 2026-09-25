class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matkamittari = 0

    def aja(self, tunnit):
        self.matkamittari += self.nopeus * tunnit


class Sähköauto:
    def __init__(self, rekisteri, huippunopeus, akku):
        super().__init__(self, rekisteri, huippunopeus)
        self.akku = akku


class Polttomoottoriauto:
    def __init__(self, rekisteri, huippunopeus, tankki):
        super().__init__(self, rekisteri, huippunopeus)
        self. tankki = tankki


sähkö = Sähköauto("ABC-15", 180, 52.5)
bensa = Polttomoottoriauto("ACD-123", 165, 32.3)

sähkö.nopeus = 100
bensa.nopeus = 100

sähkö.aja(3)
sähkö.aja(3)

print(sähkö.matkamittari)
print(bensa.matkamittari)