name  = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

#with automatycznie otwiera zapisuje i zamyka