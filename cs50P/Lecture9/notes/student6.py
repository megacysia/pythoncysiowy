class Student: 
    def __init__(self, name, house): #gdyby house np mial byc opcjonalny to house=None
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclav", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = self.name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()
    
#attributes (.)