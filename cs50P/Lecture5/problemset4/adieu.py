import inflect

def main():
    p = inflect.engine()
    imiona = get_names()
    imiona = p.join((imiona), final_sep="")
    print("Adieu, adieu, to", end=" ")
    print(imiona)

def get_names():
    list = []
    while True:
        try:
            x = input("Imie: ")
            list.append(x)
        except EOFError:
            print("")
            return list
        
main()