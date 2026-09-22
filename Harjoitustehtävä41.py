class Pelihahmo:
    def __init__(self, nimi, taso):
        self.nimi = nimi
        self.taso = taso

class Pelaaja:
    def __init__(self, nimi):
        self.nimi = nimi
        self.hahmo = None    

    def aseta_hahmo(self, hahmo):
        self.hahmo = hahmo

pelaaja = Pelaaja("Bruce")
hahmo = Pelihahmo("Sonic", 40)

pelaaja.aseta_hahmo(hahmo)

print(pelaaja.nimi)
print(pelaaja.hahmo.nimi)
print(pelaaja.hahmo.taso)