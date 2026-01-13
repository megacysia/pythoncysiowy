def najwiekszywydatek(xyz):
    print(f"Najwiekszy wydatek: {max(xyz)}")

def najmniejszyszywydatek(xyz):
    print(f"Najmniejszy wydatek: {min(xyz)}")

def sumawydatków(xyz):
    print(f"Suma wydatków: {sum(xyz)}")


wydatki = []

while True:
    try:
        for i in range (7):
            koszt = int(input("Koszt: "))
            wydatki.append(koszt)
        break
    except ValueError:
        print("Wprowadzaj tylko liczby. Wprowadz wydatki jeszcze raz")


srednikoszt = sum(wydatki) / len(wydatki)
print(f"Średni wydatek: {srednikoszt}")

najwiekszywydatek(wydatki)

najmniejszyszywydatek(wydatki)

sumawydatków(wydatki)
