class Elokuva:
    def __init__(self, nimi, elokuvan_valmistumisvuosi):
        self.nimi = nimi
        self.elokuvan_valmistumisvuosi = elokuvan_valmistumisvuosi

elokuva = Elokuva("Avengers Endgame", 2019)

print(f"{elokuva.nimi} on julkaistu vuonna {elokuva.elokuvan_valmistumisvuosi}.")