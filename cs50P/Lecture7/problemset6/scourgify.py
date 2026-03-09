#In a file called scourgify.py, implement a program that:

#    Expects the user to provide two command-line arguments:
#        the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
#        the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
#    Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.

#If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

import sys
import csv

try:
    
    program = sys.argv[1]
    
    if len(sys.argv) == 3 and program.endswith(".csv"):
        
        try:
            
            ludzie = []
            
            with open(program) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    first, last = row["name"].split(" ")
                    ludzie.append({"first": first, "last": last, "house": row["house"]})   
        
        except FileNotFoundError:
            print("File not found")
            sys.exit()

    with open(sys.argv[2], "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for osoba in ludzie:
            writer.writerow(osoba)

except IndexError:
    print("zla ilosc argumentow")
    sys.exit()