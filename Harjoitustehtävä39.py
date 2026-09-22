class Lentokone:
    def __init__(self, nimi, väri):
        self.nimi = nimi
        self.väri = väri

class Maalaamo:
    def maalaa(self, lentokone, väri):
        lentokone.väri = väri

maalaamo = Maalaamo()
lentokone = Lentokone("ABC-123", "sininen")
print("Lentokone on " + lentokone.väri)
maalaamo.maalaa(lentokone, "punainen")
print("Kone on nyt " + lentokone.väri)