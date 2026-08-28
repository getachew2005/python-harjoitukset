sukupuoli =input("Anna sukupuoli (nainen/mies): ")
hemoglobiini = int(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiinin arvo on alhainen.")
    elif hemoglobiini <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiinin arvo on korkea.")

if sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvo on matala.")
    elif hemoglobiini <= 195:
        print("Hemoglobiinin arvo on normaali.")
    else:
        print("Hemoglobiiniarvo on ylhäinen.")