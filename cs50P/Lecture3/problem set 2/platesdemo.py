def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s): #returns True if s meets all requirements and False if not. Assume that s will be a str
    if two_to_six_chars(s) and first_two_letters(s) and finding_numbers(s) and zero_not_first(s) and no_punctuation(s):
        return True
    return False
    
def two_to_six_chars(s:str): #2-6 characters
    x = len(s)
    if x >= 2 and x <= 6:
        return True
    return False

def first_two_letters(s): #start with at least two letters
    for i in range(2):
        if not s[i].isupper():
            return False
    return True 
    
#Numbers cannot be used in the middle of a plate; they must come at the end
# invalid: AA1D34
#Valid: AAD134
    
def finding_numbers(s:str): 
    y = len(s)
    for i in range(y-1):
        first = s[i]
        second = s[i+1]
        if first.isnumeric() and not second.isnumeric():
            return False     
    return True

def zero_not_first(s:str): #The first number used cannot be a ‘0’
    y = len(s)
    for i in range(y):
        pierwsze = s[i]
        if pierwsze.isnumeric() and not pierwsze == "0":
            return True
        elif pierwsze.isnumeric() and pierwsze == "0":
            return False        
    return True
        
def no_punctuation(s:str):  #No periods, spaces, or punctuation marks are allowed
    if s.__contains__("."):
        return False
    return True


main()
