numerot = {"Ratchet": "050-1234567",
           "Clank": "040-1112223",
           "Qwark": "050-7654321"}

numerot["Jak"] = "050-1011012"
numerot["Daxter"] = "0401-2132139"

print(numerot)

nimi = input("Anna nimi: ")
if nimi in numerot:
    print(f"Henkilön {nimi} puhelinnumero on {numerot[nimi]}.")