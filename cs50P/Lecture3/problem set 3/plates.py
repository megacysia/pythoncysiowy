#In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

 #   “All vanity plates must start with at least two letters.”
 #   “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
 #   “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
 #   “No periods, spaces, or punctuation marks are allowed.”

#In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s): 
    if two_to_six_chars(s) and first_two_letters(s) and finding_numbers(s) and zero_not_first(s) and no_punctuation(s):
        return True
    return False
    
def two_to_six_chars(s:str): 
    x = len(s)
    if x >= 2 and x <= 6:
        return True
    return False

def first_two_letters(s): 
    for i in range(2):
        if not s[i].isupper():
            return False
    return True 

def finding_numbers(s:str): 
    y = len(s)
    for i in range(y-1):
        first = s[i]
        second = s[i+1]
        if first.isnumeric() and not second.isnumeric():
            return False     
    return True

def zero_not_first(s:str): 
    y = len(s)
    for i in range(y):
        pierwsze = s[i]
        if pierwsze.isnumeric() and not pierwsze == "0":
            return True
        elif pierwsze.isnumeric() and pierwsze == "0":
            return False        
    return True
        
def no_punctuation(s:str): 
    if s.__contains__("."):
        return False
    return True


main()

