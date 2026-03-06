#in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

#Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.

import sys

program = sys.argv[1]

if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
    try:
        with open(sys.argv[1]) as file:
            x = 0
            for row in file:
                row = row.replace(" ", "")
                if not row.startswith('#') and row != '\n':
                    x = x + 1
            print(x)
    except FileNotFoundError:
        print("Nie ma takiego pliku")
        sys.exit()
else:
    print("wpisz tylko nazwę programu")
    sys.exit()