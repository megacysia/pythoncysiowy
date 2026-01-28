def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
    
def dollars_to_float(d):
    x = float(f"{d}".replace("$", ""))
    return round(x, 1)
    
def percent_to_float(p):
    x = float((f"{p}".replace("%", "")))
    return x / 100
    
main()