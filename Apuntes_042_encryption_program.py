import random
import string

# string.whitespace

chars = " " + string.punctuation + string.digits + string.ascii_letters + "á" + "é" + "í" + "ó" + "ú"
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"Chars: {chars}")
# print(f"Key: {key}")

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# DECRYPT
cipher_text = input("Enter a message to desencrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message: {cipher_text}")
print(f"Original message: {plain_text}")