import random

kerrat = int(input("Montako kertaa on jaollisia lukuja: "))
x = random.randint(1, 1000)
tehdyt = 0
while tehdyt < kerrat:
    print(x)
    tehdyt = tehdyt / 3