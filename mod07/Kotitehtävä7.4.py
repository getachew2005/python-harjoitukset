def summa(numeroluvut):
    yhteensa = 0

    for numeroluku in numeroluvut:
        yhteensa += numeroluku

    return yhteensa


numeroluvut = [4, 8, 2, 7, 12]

tulos = summa(numeroluvut)

print("Numerolukujen summa on:", tulos)

