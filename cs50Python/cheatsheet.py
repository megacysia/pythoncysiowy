names = ["Asia", "Basia", "Kuba"] #robimy tablicę ze stringami która zawiera dane imiona

name = input("Name: ") #bierzemy input od uzytkownika, jakiego imienia szukamy

for n in names: #jeśli zmienna n jest w tablicy z names
    if name == n: #jeśli to co wpisał uzytkownik jest takie jak któryś element (n) w tablicy names
        print("Found")
        break #jeśli nie znajdzie w tablicy names imienia ktore wpisal uzytkownik to wychodzi z petli
else: #a poniewaz jak nie znajdzie tego imienia to tylko wychodzi z petli, to jesli nie znajdzie to
    print("Not found")
    
#inaczej mozna tak:
#people = [
#   {"name": "Asia", "number": 123456789"},
#   {"name": "Basia", "number": "012345678"},   TO JEST PYTHONOWA LISTA Z WARTOSCIAMI i key value
#   {"name": "Kuba", "number": "123456780"},
#]
#name = input("Name: ")
#for person in people:
    #if person["name"] == name:
    #   number = person["number"]   --> person tutaj to input od uzytkownika - znajdz numer danego person
    #   print(f"Found: {number}")
    #   break
#else:
#   print("Not found")
