pistemäärä = int(input("Syötä kokeen pistemäärä 0-100:"))
if 90 <= pistemäärä < 100 or (pistemäärä == 100):
    print("5")
elif 80 <= pistemäärä < 89 or (pistemäärä == 89):
    print("4")
elif 70 <= pistemäärä < 79 or (pistemäärä == 79):
    print("3")
elif 60 <= pistemäärä < 69 or (pistemäärä == 69):
    print("2")
elif 50 <= pistemäärä < 59 or (pistemäärä == 59):
    print("1")
elif pistemäärä < 50:
    print("Hylätty")