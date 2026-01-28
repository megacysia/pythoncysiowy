#students = ["Hermione", "Harry", "Ron"]

#print(students[0]) #to nam wydrukuje hermione, bo te kwadratowe nawiasy wchodzą do listy i wybierają ten element, który potrzebuje
#print(students[1]) #a to wydrukuje Harrego

#ale mozna zrobic to mądrzej - for loop moze przechodzic nie tylko przez inty ale tez stringi

#2 sposób:

#students = ["Hermione", "Harry", "Ron"]

#for student in students: #nie musze w pythonie deklarowac zmiennej - python wie ze jak byla lista i w niej zmiennej to ze ten student tu to bedzie student z listy. Mogłabym tez napisac ,,xyz" i tez by wiedzial ze to student#
#    print(student)
    
#to co teraz napisałam wydrukuje wszystkich studentów z listy 

#3 sposób:

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)): #len zwraca wielkość listy i zwraca to jako argument do range
    print(i, students[i]) #to ,,i'' nie jest konieczne, ale mozna je dac i wtedy wydrukuje oprocz imienia studenta takze jego numer w liscie, czyli np 0 Hermione. Jkby sie chcialo
    #zeby nie drukowalo od 0 tylko od 1, to piszemy po prostu i + 1, students[i]