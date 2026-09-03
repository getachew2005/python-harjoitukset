import math 
def yksiköllinen_hinta(halkaisija, hinta):
    pinta_ala_A = math.pi * (halkaisija / 2) ** 2
    return hinta / (pinta_ala_A / 10000)


d1 = float(input("Syötä ensimmäinen pizzan halkaisija:"))
h1 = float(input("Anna ensimäisen pizzaan kuuluva hinta:"))

d2 = float(input("Syötä toisen pizzan halkaisija:"))
h2 = float(input("Anna toisen pizzaan kuuluva hinta:"))

p1 = yksiköllinen_hinta(d1, h1)
p2 = yksiköllinen_hinta(d2, h2)

if p1 < p2:
    print("Ensimmäinen pizza on parempi.")
else:
    print("Toinen pizza on hyvempi.")