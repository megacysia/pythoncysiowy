name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron": # te | to taki or
        print("Gryffindor")
    case "Draco":
        print("Slyherin")
    case _: # to jesli nie ma kogos w caseach
        print("Who?")