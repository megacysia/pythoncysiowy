#Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

#In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

#If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

def main():
    x = get_int()
    y = give_percent(x)
    if y <= 1:
        print("Fuel is empty!")
    elif y >= 99:
        print("Fuel is full!")
    else:
        print(f"fuel is {y}%")


def give_percent(wynik):
    procenty = wynik * 100
    return round(procenty) 


def get_int():
    while True:
        try:
            x = input("What's fuel fraction? ")
            first, second = x.split("/")
            liczebnik = int(first)
            mianownik = int(second)
            
            if liczebnik >= 0 and mianownik >= 0 and liczebnik < mianownik:
                return liczebnik / mianownik
            if liczebnik > mianownik:
                raise Exception("too much")
            
        except Exception:
            print("You can't have THAT much! :D ")
        
        except ZeroDivisionError:
            print("Can't divide by 0")

        except ValueError:
            print("It is not a fraction format")
            
        else: 
            break
    
main()