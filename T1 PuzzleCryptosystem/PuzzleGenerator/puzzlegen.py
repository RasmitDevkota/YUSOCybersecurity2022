import random
import numpy as np

def generator(prompt):
    m = 0
    n = 0
    c = 0

    if prompt["method"] == "rowcolumn":
        m = prompt["rows"]
        n = prompt["columns"]

        c = random.randint(0, m * n - m - n)
    elif prompt["method"] == "piececount":
        c = prompt["count"]

    print("Generating puzzle with " + m + " rows, " + n + " columns, and " + c + " puzzle pieces")

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    word = ""

    for i in range(c):
        word += alphabet[random.randint(0, 25)]

    return

def generator_mass():

    return

def generator_cmd():
    print("Welcome to the Puzzle Generator Command Prompt!")

    gen_method = input("Would you like to generator a puzzle using the number or rows and columns (type \"1\") or the number of puzzle pieces (type \"2\")?")

    if gen_method == "1":
        prompt = {
            "method": "rowcolumn",
            "rows": int(input("Please enter the number of rows in the puzzle")),
            "columns": int(input("Please enter the number of columns in the puzzle"))
        }

        generator(prompt)
    elif gen_method == "2":
        prompt = {
            "method": "piececount",
            "count": int(input("Please enter the number of puzzle pieces to include in the puzzle (note: this must be a non-prime number greater than 9 but less than or equal to 1024"))
        }

        generator(prompt)
    else:
        print("Sorry, you entered an invalid generation method ID, please rerun the script to try again!")

    return