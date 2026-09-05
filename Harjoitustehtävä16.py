kokonaisluku = int(input("Syötä kokonaisluku:"))
kokonaisluku_2 = int(input("Anna luku: "))
if kokonaisluku > kokonaisluku_2:
    print("Ensimmäinen kokonaisluku on suurempi kuin toinen kokonaisluku.")
elif kokonaisluku < kokonaisluku_2:
    print("Toinen syöttämä kokonaisluku on suurempi kuin ensimmäinen syöttämä kokonaisluku.")
elif kokonaisluku == kokonaisluku_2:
    print("Luvut ovat yhtäsuuret.")