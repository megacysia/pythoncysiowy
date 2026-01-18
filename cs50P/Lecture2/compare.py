x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y: # "x < y" to boolean expression (bool) - pytanie na ktore odp to tak albo nie / true / false
    print("x is less than y") #to ze tu sa te spacje po lewej znaczy dla programu, ze linijka 5 ma byc wykonana tylko jesli warunek z 4 jest spelniony
    
elif x > y:
    print("x is greater than y")
    
else:
    print("x is equal to y")
    
