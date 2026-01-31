#The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”

#In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.
def main():
    fruits = [
    {"name": "apple", "calories": 130},
    {"name": "avocado", "calories": 50},
    {"name": "banana", "calories": 110},
    {"name": "cantaloupe", "calories": 50}, 
    {"name": "grapefruit", "calories": 60}, 
    {"name": "grapes", "calories": 90}, 
    {"name": "honeydew melon", "calories": 50}, 
    {"name": "kiwifruit", "calories": 90}, 
    {"name": "lemon", "calories": 15}, 
    {"name": "lime", "calories": 20}, 
    {"name": "nectarine", "calories": 60}, 
    {"name": "orange", "calories": 80}, 
    {"name": "peach", "calories": 60}, 
    {"name": "pear", "calories": 100}, 
    {"name": "pineapple", "calories": 50}, 
    {"name": "plums", "calories": 70}, 
    {"name": "strawberries", "calories": 50}, 
    {"name": "sweet cherries", "calories": 100}, 
    {"name": "tangerine", "calories": 50}, 
    {"name": "watermelon", "calories": 80}, 
    ]

    while True:
        owoc = input("owoc: ").lower()
        for fruit in fruits:
            if fruit["name"] == owoc:
                print("calories: ", fruit["calories"])
            return
            

main()