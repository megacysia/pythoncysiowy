def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))

        except ValueError:
            print("x is not an integer")
            
        else: #tylko wtedy sie wykona jak try jest succeded
            break           #mogloby byc po prostu else: return x - WTEDY JEDNOCZESNIE wychodzi z loopa i zwraca x
    return x
    
main()

#RETURN ZWRACA Z FUNKCJI. BREAK WYCHODZI Z LOOPA