import random
noppa1 = noppa2 = heitot = 0
while (noppa1 != 4 or noppa2 != 4):
    noppa1 = random.randint(1,4)
    noppa2 = random.randint(1,4)
    heitot = heitot + 1
print(f"Tarvittiin {heitot:d} heittoa.")