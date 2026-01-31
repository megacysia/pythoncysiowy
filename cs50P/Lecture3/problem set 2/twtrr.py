#When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

def main():
    long = input("Word: ")
    print (saving(long))
    
    
    
def saving(x:str):
    y = len(x)
    slowo = ""
    for i in range(y):
        litera = x[i]
        if litera == "a" or litera == "e" or litera == "i" or litera == "o" or litera == "u":
            litera = litera.replace("a", "").replace("e", "").replace("i",  "").replace("o", "").replace("u", "")
        slowo = slowo + litera
    
    return slowo




main()