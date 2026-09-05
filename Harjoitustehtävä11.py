ikä = int(input("Anna ikäsi:"))
if 15 <= ikä < 18:
    vuosi = float(input("Syötä vuosi:"))
if ikä >= 18 or (ikä >= 15 and vuosi >= 2005):
    print("Voit pelata peliä nimeltään The Incredible Flash.")
else:
    print("Et voi pelata The Incredible Flash.")