import sys

from pyfiglet import Figlet
from pyfiglet import FontNotFound

from random import choice

figlet = Figlet()
lista = figlet.getFonts()

losowa = choice(lista)

if len(sys.argv) == 1:
    cokolwiek = input("Input: ")
    figlet.setFont(font=losowa)
    print(figlet.renderText(cokolwiek))
    
elif len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("invalid arguments")

elif sys.argv[1] != "-f" and sys.argv[1] != "--font":
    sys.exit("invalid arguments!!")

elif len(sys.argv) == 3:
    czcionka = sys.argv[2]
    cokolwiek = input("tekst: ")
    while True:
        try:
            figlet.setFont(font=czcionka)
            print(figlet.renderText(cokolwiek))
            break
        except FontNotFound:
            print("Nie ma takiej czcionki. Wybierz z listy: ")
            print(lista)
            czcionka = input("czcionka: ")
            
    
    

    