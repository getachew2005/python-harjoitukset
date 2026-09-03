import random

def noppa(nopan_tahkot):
    return random.randint(1, nopan_tahkot)

max = int(input("Anna tahkojen määrä:"))

while True:
    nopan_silmäluku = noppa(max)
    print(nopan_silmäluku)

    if nopan_silmäluku == max:
        break