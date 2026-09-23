class Rengassarja:
    def __init__(self, merkki, koko):
        self.merkki = merkki
        self.koko = koko


class Auto:
    def __init__(self, rekisterinumero):
        self.rekisterinumero = rekisterinumero
        self.rengassarja = None

    def vaihda_renkaat(self, rengassarja):
        self.rengassarja = rengassarja


auto = Auto("ABC-123")
rengassarja = Rengassarja("Nokian", 18)

auto.vaihda_renkaat(rengassarja)

print(auto.rekisterinumero)
print(auto.rengassarja.merkki)
print(auto.rengassarja.koko)