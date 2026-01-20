#in meal.py, implement a program that prompts the user for a time 
#and outputs whether it’s breakfast time, lunch time, or dinner time. 
# If it’s not time for a meal, don’t output anything at all. 
# 
# Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. 
# And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

#Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

def main():
    time = input("What time is it? ")
    hours = convert(time)
    posilek = meal(hours)


def convert(n):
    hours, minutes = n.split(":")
    return int(hours) + int(minutes) / 60

def meal(n):
    if n >= 7 and n < 9.99:
        print("It is breakfast time!")
    elif n >= 13 and n < 16:
        print("It is dinner time!")
    elif n >= 18 and n < 20:
        print("It is supper time!") 

if __name__ == "__main__":
    main()
