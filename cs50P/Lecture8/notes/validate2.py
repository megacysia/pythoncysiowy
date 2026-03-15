import re

email = input("What's your email? ").strip()

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email): 
# else:
#     print("Invalid")

if re.search(r"^[a-zA-Z0-9_ ]+@\w+\.(com|edu|gov|net|org)$", email): #ten \w to litery i numery ; zamiast [a-zA-Z0-9_ ] zby miec spacje mozna tez (\w|\s), bo \s to whitespace
    print("Valid")
else:
    print("Invalid")
    
# \d decimal digit
# \D not a decimal digit
# \s whitespace characters
# \S not a whitespace character
# \w word character... as well as numbers and the underscore
# \W not a word character
# A|B either A or B
# (...) a group
# (?:...) non-capturing version