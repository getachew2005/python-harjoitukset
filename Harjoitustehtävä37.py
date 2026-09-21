class Elokuva:
    def __init__(self, nimi, valmistumisvuosi):
        self.nimi = nimi
        self.valmistumisvuosi = valmistumisvuosi

elokuva = Elokuva("Avengers Infinity War", 2018)

print(f"Elokuva {elokuva.nimi} julkaistiin vuonna {elokuva.valmistumisvuosi}.")