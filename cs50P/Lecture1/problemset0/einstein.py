def square(n):
    return n * n

def einstein_energy(mass):
    E = mass * square(300000000)
    return E

def main():
    mass = int(input("What's mass? In kilograms"))
    print("It is", einstein_energy(mass))
    
main()





