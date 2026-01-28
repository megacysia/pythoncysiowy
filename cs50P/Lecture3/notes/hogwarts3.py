students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slyherin", "patronus": "None"}, #bo ogolnie istnieje none
]

#zrobilismy tu listę. Listę czegoś - bo mamy []. Potem mamy {} więc to znaczy, ze mamy dictionary. Czyli listę dictionaries. Kazda ma po 3 keys i 3 values. no. 

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")