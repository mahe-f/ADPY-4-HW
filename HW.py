import random
import string

print("Random Password Generator")

# combine all characters
characters = string.ascii_letters + string.digits + string.punctuation

# choose password length
length = 8

# generate password
password = ""
for i in range(length):
    password += random.choice(characters)

print("Your generated password is:", password)