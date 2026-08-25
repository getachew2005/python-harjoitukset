import math

leviskat = input("Mikä on levisköjen massa")
naulat = input("Mikä on naulojen massa")
luodit = input("Mikä on luotimien massa")
kilo = leviskat + naulat + luodit
gramma = leviskat + naulat + luodit
print(("Leviskojen massa on", leviskat, "Naulojen massa on", naulat, "Luotimien massa on", luodit, "Massan keskiaikaisten mittojen mukaan: kilo on", kilo, "Massan keskiaikaisten mittojen mukaan: gramma on", gramma, f"Määrä kiloina ja grammoina: {kilo} kg {gramma} g"))
