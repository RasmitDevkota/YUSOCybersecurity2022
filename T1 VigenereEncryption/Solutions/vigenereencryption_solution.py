plaintext = input()
key = input()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

plaintext_indices = [alphabet.index(pt) for pt in plaintext]
key_indices = [alphabet.index(k) for k in key]
key_len = len(key)

ciphertext = ""

for i in range(len(plaintext_indices)):
    ciphertext_index = plaintext_indices[i] + key_indices[i % key_len] % 26

    ciphertext_character = alphabet[ciphertext_index]

    ciphertext += ciphertext_character

print(ciphertext)