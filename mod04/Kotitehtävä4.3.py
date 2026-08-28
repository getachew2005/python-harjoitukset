arvo =input("Anna biologinen sukupuoli: ")
if arvo < 117:
    print("Hemoglobiininarvo on alhainen.")
elif arvo == 125:
    print("Hemoglobiininarvo on normaali.")
elif arvo > 175:
    print("Hemoglobiininarvo on korkea.")
else:
    print(f"Määrä gramma/litra: {gramma} g {litra} l")