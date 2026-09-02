ika = int(input("Anna ikäsi:"))
if 15 <= ika < 18:
    vuosi = float(input("Syötä vuosi:"))
if ika >= 18 or (ika >= 15 and vuosi >= 2005):
    print("Voit pelata peliä nimeltään The Incredible Flash.")