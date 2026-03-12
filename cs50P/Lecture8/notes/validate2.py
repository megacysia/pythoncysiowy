import re

email = input("What's your email? ").strip()

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email): 
# else:
#     print("Invalid")

if re.search(r"^\w+@\w+\.edu$", email): #ten \w to litery i numery
    print("Valid")
else:
    print("Invalid")
    
# \d decimal digit
# \D not a decimal digit
# \s whitespace characters
# \S not a whitespace character
# \w word character... as well as numbers and the underscore
# \W not a word character