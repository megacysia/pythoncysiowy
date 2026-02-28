#with open("names.txt", "r") as file:
#    lines = file.readlines()
#    
#for line in lines:
#    print("hello,", line.rstrip())

#ALBO:

#with open("names.txt", "r") as file:
#    for line in file: #ogólnie python slodziak
#        print("hello,", line.rstrip())

#ale problem jest tak, ze jakbym chciala posortowac liste, to sie tak z tym with open nie da bo nie ma jak, wiec:

names = []

with open("names.txt") as file: #r nie jest konieczne bo jesst domyslene 
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
    
#czyli ogolnie dzieje sie tu to, ze najpierw tworzymy pusta liste, i ta funkcja with otwieramy plik, w kazdej nowej linijce aktualizujemy plik o nowe imie, a potem dla kazdego name w posortowanej wlasnie liscie, drukujemy przywianie