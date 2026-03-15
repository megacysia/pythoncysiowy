import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
        print("Valid")
else:
    print("Invalid")
    
    
# re.match(pattern, string, flag=0)
# re.fullmatch(pattern, string, flag=0)