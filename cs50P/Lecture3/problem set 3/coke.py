#Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

#In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

def get_coin():
    y = 0
    while True:
        n = int(input("Coca-Cola costs 50 cents. Insert a coin - only 5/10/25 cents: "))
        if n == 5 or n == 10 or n ==25:
            y = y + n
            print("Money: ", y)
        if y >= 50:
            break
    return y

def liczenie(x):
        return x - 50

def main():
    n = get_coin()
    reszta = liczenie(n)
    print("Change: ", reszta)

main()