# email = input("What's ypur email? ").strip()
# #i teraz albo łatwa wersja:
# # if "@" in email and "." in email:
# #     print("Valid")
# # else:
# #     print("Invalid")

# #albo trudniejsza:

# username, domain = email.split("@")

# #if username: #if username da True, czyli tak naprawdę jesli username ma więcej ni jeden char
# #ale potrzebujemy więcej więc:
# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")
    
#re.search(pattern, string, flags=0)
#pattern to to czego szukamy w tym co jest wpisane, czyli np string od uzytk
#string w tym to w czym szukamy patternu
#flag to parametr który mona przekazać funkcji eby coś zmodyfikować w funkcji ale nie będziemy teraz tego uzywac

import re

email = input("What's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email): #r #jakbym faktycznie chciała $ na końcu to tak samo, \$ trzeba i tyle
    print("Valid")
else:
    print("Invalid")
    
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetition
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end of the string or just before the newline at the and of the string
# [] set of characters
# [^] complementing the set