import re

email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9_ ]+@\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
        print("Valid")
else:
    print("Invalid")
    
# re.IGNORECASE
# re.MULTILINE
# re.DOTALL