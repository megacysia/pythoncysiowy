def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
        

def is_even(n):
#   if n % 2 == 0:
#      return True
#   else:
#        return False
#albo pythonowo:
#    return True if n % 2 == 0 else False
#albo jeszcze lepiej:
    return n % 2 == 0 #to zwraca prawde jesli ten warunek stad jest spelniony 

main()
