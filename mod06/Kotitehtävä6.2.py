numeroluvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")

    if syote == "":
        break

    numeroluvut.append(int(syote))

numeroluvut.sort(reverse=True)

print("Viisi suurinta numerolukua:")

for numeroluku in numeroluvut [5:]:
    print(numeroluku)





