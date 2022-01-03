import random
import string


input = input("Generate new password? (y or n) ").lower()
length=8

if input == "y":
    password = "".join(random.choices(string.ascii_letters, k = length))
    print("Your new password is: " + str(password))
else:
    print("If you need a password please enter in y")