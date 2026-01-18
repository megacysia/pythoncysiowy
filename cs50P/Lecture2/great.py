score = int(input("Score: "))

if score >= 90: #albo "if 90 <= score <= 100:"" # albo najprosciej: "if score >= 90 and score <= 100: "" #albo "if 90 <= score and score <= 100"   --> wtedy jest prosciej a wychodzi na to samo 
    print("Grade: A")
    
elif score >= 80:
    print("Grade: B")
    
elif score >= 70:
    print("Grade: C")
    
elif score >= 60:
    print("Grade: D")
    
else:
    print("Grade: F")