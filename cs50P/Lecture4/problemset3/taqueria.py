#One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, which offers a menu of entrees, per the dict below, wherein the value of each key is a price in dollars:

# {
#     "Baja Taco": 4.25,
#     "Burrito": 7.50,
#     "Bowl": 8.50,
#     "Nachos": 11.00,
#     "Quesadilla": 8.50,
#     "Super Burrito": 8.50,
#     "Super Quesadilla": 9.50,
#     "Taco": 3.00,
#     "Tortilla Salad": 8.00
# }

# In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.

def main():
    food = get_food()
    print(food)
    
    
def get_food():
    entrees = [
     {"name": "Baja Taco", "price": 4.25},
     {"name": "Burrito", "price": 7.50},
     {"name": "Bowl", "price": 8.50},
     {"name": "Nachos", "price": 11.00},
     {"name": "Quesadilla", "price": 8.50},
     {"name": "Super Burrito", "price": 8.50},
     {"name": "Super Quesadilla", "price": 9.50},
     {"name": "Taco", "price": 3.00},
     {"name": "Tortilla Salad", "price": 8.00},
    ]
    hajs = 0
    while True:
        try:
            zamowienie = input("order: ").lower().capitalize()
            for pozycja in entrees:
                if pozycja["name"] == zamowienie:
                    hajs = float(hajs + pozycja["price"])
                    print("price so far: ", end="")
                    print("$", end ="")
                    print(hajs)
                else:
                    pass
        except EOFError:
            print("Total: ", end="")
            print("$", end ="")
            print(hajs)
    
main()