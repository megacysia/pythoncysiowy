def main():
    long = input("Word: ")
    print (shorten(long))
    
    
    
def shorten(x:str):
    y = len(x)
    slowo = ""
    for i in range(y):
        litera = x[i]
        litera = litera.lower()
        if litera == "a" or litera == "e" or litera == "i" or litera == "o" or litera == "u":
            litera = litera.replace("a", "").replace("e", "").replace("i",  "").replace("o", "").replace("u", "")
        slowo = slowo + litera
    
    return slowo

if __name__ == "__main__":
    main()