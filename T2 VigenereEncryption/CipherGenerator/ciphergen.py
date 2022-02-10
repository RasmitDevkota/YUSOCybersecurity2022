import random

def main():
    generator()

def generator():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    test_case_counter = 0
    test_cases_needed = 2880

    for i in range(16, 256):
        for j in range(4, 16):
            plaintext_list = [random.randrange(0, 26) for k in range(i)]

            key_list = [random.randrange(0, 26) for k in range(j)]

            ciphertext_list = [(plaintext_list[p] + key_list[p % j]) % 26 for p in range(len(plaintext_list))]

            plaintext = "".join([alphabet[k] for k in plaintext_list])

            key = "".join([alphabet[k] for k in key_list])

            ciphertext = "".join([alphabet[k] for k in ciphertext_list])

            test_case_number = str(test_case_counter).zfill(4)

            input_file = open("../Ciphers/vigenereencryption_test_cases/input/input{}.txt".format(test_case_number), "w")

            input_file.writelines([plaintext, "\n", key])

            output_file = open("../Ciphers/vigenereencryption_test_cases/output/output{}.txt".format(test_case_number), "w")

            output_file.write(ciphertext)

            test_case_counter += 1

            print(str(test_case_counter) + "/2880 test cases generated")

def generator_mass():
    return

def generator_cmd():
    return

main()
