def gallona_litroina(gallona):
    return gallona * 3.785


while True:
    gallona = float(input("Syötä gallonmäärä:"))

    if gallona < 0:
        break

    litrat = gallona_litroina(gallona)
    print(f"{litrat:.2f} l")

