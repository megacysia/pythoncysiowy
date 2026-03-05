import csv

name = input("What's your name? ")
house = input("Where's your house? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, house])