numeroluku = int(input("Anna jokin kokonaisluku: "))

if numeroluku < 2:
    print("Numeroluku ei ole alkuluku.")
else:
    alkuluku = True

    for jakaja in range(2, numeroluku):
        if numeroluku % jakaja == 0:
            alkuluku = False
            break

    if alkuluku:
        print("Antama luku on alkuluku")
    else:
        print("Numeroluku ei ole alkuluku")