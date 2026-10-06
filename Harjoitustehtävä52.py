def tervehdi(tervehdys, kerrat):
    for i in range(kerrat):
        print(tervehdys + " " + str(i+1) + ". kerran")
    return

tervehdi("Moi", 5)
tervehdi("Hyvää päivää", 4)