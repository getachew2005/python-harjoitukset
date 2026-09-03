import random

def noppa():
    return random.randint(1, 6)

while True:
    nopan_silmäluku = noppa()
    print(nopan_silmäluku)

    if nopan_silmäluku == 6:
        break
