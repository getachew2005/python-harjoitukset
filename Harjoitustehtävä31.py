numeron_arvosanat = [8, 5, 10, 7, 9, 6, 4, 10]

for numeron_arvosana in numeron_arvosanat:
    if numeron_arvosana >= 8:
        print("Hyvä")
    elif 6 <= numeron_arvosana < 7 or (numeron_arvosana == 7):
        print("Kohtalainen")
    elif numeron_arvosana < 6:
        print("Heikko")