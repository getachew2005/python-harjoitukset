class Esine:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino


class Pelaaja:
    def __init__(self, nimi, kultaiset_kengät, sijainti):
        self.nimi = nimi
        self.kultaiset_kengät = kultaiset_kengät
        self.sijainti = sijainti
        self.esine = None

    def liiku_ja_kerää_esinettä(self, esine):
            self.esine = esine


class Paikka:
    def __init__(self, nimi, esine):
        self.nimi = nimi
        self.esine = None


pelaaja = Pelaaja("Liul Getachew", "kultaiset kengät", "Last Vegas")
esine = Esine("Kutltaiset kengät", 2)
paikka = Paikka("Last Vegas", "kultaiset kengät")

pelaaja.liiku_ja_kerää_esinettä(esine)

print(pelaaja.nimi)
print(pelaaja.kultaiset_kengät)
print(pelaaja.sijainti)
print(pelaaja.esine.nimi)
print(pelaaja.esine.paino)