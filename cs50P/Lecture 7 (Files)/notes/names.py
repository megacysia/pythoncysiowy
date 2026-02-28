names = [] #give me an empty list, that we can add things to later

for _ in range(3):
    #name = input("What's your name? ")
    #names.append(name)
    #albo ładniej:
    names.append(input("What's your name? "))
    
for name in sorted(names):
    print(f"hello, {name}")