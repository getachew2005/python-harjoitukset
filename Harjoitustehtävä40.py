class Reppu:
    def __init__(self, merkki):
        self.merkki = merkki


class Opiskelija:
    def __init__(self, nimi):
        self.nimi = nimi
        self.reppu = None

    def aseta_reppu(self, reppu):
        self.reppu = reppu


opiskelija = Opiskelija("Eddie")
reppu = Reppu("Puuma")

opiskelija.aseta_reppu(reppu)

print(opiskelija.nimi)
print(opiskelija.reppu.merkki)