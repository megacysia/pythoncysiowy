def ify(first, second, last):
    try:
        if second == "+":
            xyz = int(first) + int(last)
        elif second == "-":
            xyz = int(first) - int(last)
        elif second == "*":
            xyz = int(first) * int(last)
        elif second == "/" and last != 0:
            xyz = int(first) / int(last)
        return xyz
    except ZeroDivisionError:
        return None
    
def main():
    dzialanie = input("Działanie: ")
    first, second, last = dzialanie.split(" ")
    xyz = ify(first, second, last)
    if xyz is None:
        print("Can't divide by 0")
    else:
        print(f"Wynik: {xyz:.1f}")
    
main()