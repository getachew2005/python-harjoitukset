kuha = float(input("Mikä on kuhan pituus senttimetreinä: "))
alamitta = 37
if kuha < alamitta:
    puuttuu = alamitta - kuha
    print("Laske kuha takasin järveen, ")
    print(f"{puuttuu:.1f} puuttuu cm")
else:
    print("Oikea kuhan pituus!")

