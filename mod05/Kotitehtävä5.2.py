while True:
    tuuma = float(input("Anna tuumamäärä: "))

    if tuuma < 0:
        break

    senttimetri = tuuma * 2.54
    print(f"{tuuma} tumaa = {senttimetri} cm")


    