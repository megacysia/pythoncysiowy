#name = input("What's your name?  "). --> demo

#name = name.strip() #to name.strip() usuwa whitespacey ze stringa jakby ktos wpisal za duzo spacji --> ale tylko od lewej i prawej, nie pomiedzy stringami - jest jeszcze funkcja L strip i R strip jakbysmy chcieli tylko z 1 strony usunaac whitespacey
#jezeli w pythonie chcemy dodac funkcje jako metode, to piszemy nazwe stringu, potem kropke, i potem nazwe funkcji - bo to strip to jest funkcja pythona. i potem nawiasy, tutaj puste akurat bo nie potrzebujemy zeby cos zwracala
#a przypisujemy = bo to bierze ten input od uzytk, przypisuje do name, a potem przypisujemy ten input do metody i zwraca nam bez whitespaceow
#to idzie OD PRAWEJ DO LEWEJ

#name = name.capitalize() --> #to robi duza litere ale tylko pierwsza w stringu
#więc uzyjemy innej metody / funkcji:

#name = name.title() #to zrobi duza litere wszystkich pierwszych liter w kazdym slowie w stringu

#name = name.strip().title() #bo mozna laczyc te metody / funkcje w jednym

name = input("What's your name?  ").strip().title()

#podziel imie usera na imie i nazwisko:
first, last = name.split(" ")

#print(f"Hello, {name}") #mozna tez zamiast {name} napisac + name i zadziala tak samo ALBO , name i tez

#ale podzielilismy na imie i nazwisko wiec:
print(f"hello, {first}")
#i dizeki temu wydrukuje tylko 1 imie

#zeby nie zaczynac w nowej linijce -> end=''

#print(*objects, sep=' ', end='\n')

#print("hello, \"friend\"") --> te backslashe jakby informuja komputer ze to co teraz zobaczy to nie to co mysli i ze ma zignorowac




