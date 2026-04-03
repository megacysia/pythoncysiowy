class Student:  #1tu się tworzy klasę
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}") #3tu się DOSTAJEMY do tych attributes
    
    
def get_student():
    student = Student()
    student.name = input("Name: ") #2to .name, .house to przechowywanie attributes W KLASIE 
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()
    
#attributes (.)
#klasy są o tyle lepsze, e nie trzeba się bawić w tuple, listy, ani dictionaries, bo po prostu od razu tworzę klasę, czyli odrębny typ danych, jak np. właśnie Student, który zawiera w sobie imię, i dom, i mogę 