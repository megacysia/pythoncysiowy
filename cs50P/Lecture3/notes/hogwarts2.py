#students = ["Hermione", "Ron", "Draco"]
#houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

#No mozna by tak bylo to powypisywac ale to jest szybko błędogenne, i lepiej uzyc dictionary - takiej two-dimensional listy:

#students = {"Hermione": "Gryffindor", "Harry": "Gryffindor", "Ron": "Gryffindor", "Draco": "Slytherin"}  --> mozna tak ale tak jest brzydko. lepiej tak:

students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin",
}

#print(students["Hermione"]) #w odroznieniu od list, dictionaries nie potrzebuja wartosci liczbowej - tutaj mamy key i value - wiec to co teraz robimy, to: wejdz do studentów, znajdz hermione, i wydrukuj mi jej value (czyli tu Gryffindor)

#ale jak to polepszyć i skrócić? no bo to moze wydrukowac tylko jedno. a jakbysmy chcieli wiecej?:

#for student in students:
 #   print(student) #jak tak zrobimy, ze uzyjemy for loopa zeby przeszedl przez dictionary, to on przeszukuje by design tylko keys, wiec wydrukuje w tym przypadku tylko imiona studentów - a co jak chcemy calosc?:
 
for student in students:
    print(student, students[student], sep=", ") #jesli student to key w tym dictionary, a tak jest, to students[student] pojdzie do lokalizacji hermiony i zwroci jej dom
    
#a co jak będzie jeszcze więcej danych w dictionary? Np. numer, imię, dom i jeszcze np patronus? to juz w nastepnym pliku