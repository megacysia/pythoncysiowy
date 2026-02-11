import random


def main():
    
    poziom = get_level()
    score = 0
    
    for _ in range(10):
        wygenerowana_liczba = generate_integer(poziom)
        druga_liczba = (generate_integer(poziom))
        prawidlowa_odp = wygenerowana_liczba + druga_liczba
        proba = 0
        prawidlowo = False
        
        while proba < 3:
            try:
                wynik = int(input(f"{wygenerowana_liczba} + {druga_liczba} = "))
                if wynik == prawidlowa_odp:
                    score += 1
                    prawidlowo = True
                    break
                else:
                    print("EEE")
                    proba += 1
            except ValueError:
                print("EEE")
                proba += 0
        if not prawidlowo:
            print(prawidlowa_odp)
        
    print("Score: ", score)
        
def get_level():
    while True:
            try:
                x = int(input("Level: "))
                if x == 1 or x == 2 or x == 3:
                    return x
                else:
                    pass
            except ValueError:
                pass


def generate_integer(level):
    if level == 1:
        random_number = random.randint(0, 9)
    elif level == 2:
        random_number = random.randint(10, 99)
    elif level == 3:
        random_number = random.randint(100, 999)
    
    return random_number
    


if __name__ == "__main__":
    main()
