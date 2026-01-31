def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            pass # zamiast np: print("x is not an integer") - bo mozemy chciec po prostu zignorowac ze ktos wpisuje cos glupiego. Pass wtedy dziala tak ze znowu sie wykona to co bylo przed chwila w petli, ale z niej nie wyjdzie dopoki to wyzej sie nie zrobi dobrze. no.
    
main()

#TO JEST TO SAMO CO W NUMBER.PY ALE GIGA SKRÓCONE
