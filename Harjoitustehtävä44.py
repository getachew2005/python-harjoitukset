class Simkortti:
    def __init__(self, puhelinnumero):
        self.puhelinnumero = puhelinnumero


class Puhelin:
    def __init__(self, merkki, malli):
        self.merkki = merkki
        self.malli = malli
        self.simkortti = None

    def aseta_simkortti(self, simkortti):
        self.simkortti = simkortti


puhelin = Puhelin("Honor", "Magic 7 lite")
simkortti = Simkortti("+358452347569")

puhelin.aseta_simkortti(simkortti)

print(puhelin.merkki)
print(puhelin.malli)
print(puhelin.simkortti.puhelinnumero)