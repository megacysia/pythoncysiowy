def main():
    greeting = input("Greet me!").strip().lower()
    print(f"$ {value(greeting)}")

def value(x:str):
    x = x.lower()
    if x.startswith("hello"):
        return 0
    elif x.startswith("h") and x != "hello":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()