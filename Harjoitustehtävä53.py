def tervehdi(tervehdys="Hei", kerrat=1):
    for i in range(kerrat):
        print(tervehdys + " " + str(i+1) + ". kerran")
    return

tervehdi()
tervehdi("Terve", 4)
tervehdi(kerrat=6, tervehdys="Moro")