# Suppose that you’re in the habit of making a list of items you need from the grocery store.

# In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

def main():
    groceries = get_need()
    groceries.sort()
    print("List:", sep='\n')
    for i in range (len(groceries)):
        print(i+1, groceries[i], sep='. ')
        
def get_need():
    list = []
    while True:
        try:
            x = input("").upper()
            list.append(x)
        except EOFError:
            return list
            
main()