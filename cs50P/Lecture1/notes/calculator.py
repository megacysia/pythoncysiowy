x = float(input("What's x? ")) #bierze input i od razu zmienia go na inta - tak samo jak napiszemy float
y = float(input("What's y? "))

#mozna tez zamiast int(input.... zrobic float(input... i tez jest git

#jest funkcja która zaokrągla:
# round(number[, ndigits])

z = round(x + y)

print(f"{z:,}") 

#ten :, powoduje, ze jak mamy jakas duza liczbe jak np 1000 to program da przecinek po drodze dla czytelnosci

#z = x + y --> jak tak sie zrobi to polaczy po prostu te 2 inputy bo to sa stringi nawet jak wygladaja jak inty wiec trzeba uzyc funkcji ktora zmieni typ zmiennej:

#z = int(x) + int(y) #teraz zmieni stringa na inta. bo int to nie tylko typ zmiennej, ale tez funkcja zmieniajaca inne typy na inta - ale zmienilam to i tak od razu w linijce z inputami u gory

#print(x + y) #poniewaz zmienilismy juz stringa na inta to teraz juz mozna dac +