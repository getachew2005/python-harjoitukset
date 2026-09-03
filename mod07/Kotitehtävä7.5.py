def karsi_parittomatluvut(numeroluvut):
    karsittu = []

    for numeroluku in numeroluvut:
        if numeroluku % 2 == 0:
            karsittu.append(numeroluku)

    return karsittu


numeroluvut = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

karsittu = karsi_parittomatluvut(numeroluvut)

print("Alkuperäinen lukulista:", numeroluvut)
print("Karsittu lukulista:", karsittu)