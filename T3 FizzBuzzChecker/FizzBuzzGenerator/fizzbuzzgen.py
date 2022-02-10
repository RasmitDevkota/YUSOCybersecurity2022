import json
import random
from time import time

def main():
    generator()

def generator():
    quotes_file = open("quotes.json", "r")
    quotes_content = quotes_file.read()
    quotes = json.loads(quotes_content)

    test_case_counter = 0

    for quote in quotes:
        message = quote["text"]

        fizzbuzzes = [[0 for _ in range(32, 128)] for _ in message]

        for i in range(len(message)):
            character = message[i]
            ascii_character = str(ord(character))

            for j in range(32, 128):
                fizzbuzz_result = ascii_character

                if j % 3 == 0:
                    fizzbuzz_result = fizzbuzz_result.lstrip(ascii_character)

                    fizzbuzz_result += "fizz"

                if j % 5 == 0:
                    fizzbuzz_result = fizzbuzz_result.lstrip(ascii_character)

                    fizzbuzz_result += "buzz"

                if j == int(ascii_character):
                    options = [ascii_character, "fizz", "buzz", "fizzbuzz"]
                    options.remove(fizzbuzz_result)

                    fizzbuzzes[i][j - 32] = str(options[random.randrange(0, 3)])
                else:
                    fizzbuzzes[i][j - 32] = str(fizzbuzz_result)

        # return
        test_case_number = str(test_case_counter).zfill(4)

        input_file = open("../FizzBuzzes/fizzbuzzchecker_test_cases/input/input{}.txt".format(test_case_number), "w")

        fizzbuzzes = [" ".join(row) for row in fizzbuzzes]

        input_file.writelines("\n".join(fizzbuzzes))

        output_file = open("../FizzBuzzes/fizzbuzzchecker_test_cases/output/output{}.txt".format(test_case_number), "w")

        output_file.writelines(message)

        test_case_counter += 1

        print(str(test_case_counter) + "/1622 test cases generated")

    return

def generator_mass():
    return

def generator_cmd():
    return

main()
