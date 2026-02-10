import random

def main():
    prompt = get_number()
    guessing(prompt)
        
        
def get_number():
    while True:
            try:
                x = int(input("random number: "))
                if x > 0:
                    return x
                else:
                    pass
            except ValueError:
                pass
    
def guessing(x):
    random_number = random.randint(1, x)
    while True:
        try:
            guess = int(input("Now you guess my choice! "))
            if guess < 0:
                pass
            elif guess > random_number:
                print("Too large!")
            elif guess < random_number and guess > 0:
                print("Too small!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass       

main()