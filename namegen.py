#name generator
import random

boy_names = ("John", "Lou", "Jacob", "Joseph", "Caleb", "Arthur", "Daniel", "Luke", "Jeremy", "Steven", "Peter", "Simon", "Derek", "Dimitri", "Ron", "Robert", "Bobby", "Timothy")
girl_names = ("Anastasia", "Skye","Elizabeth", "Tiffany", "Felicia", "Debbie", "Hannah", "Mary", "Ann", "Christina", "Melody", "Bella", "Penelope", "Maria", "Ella", "Emma")


print("Welcome to the Name Generator")
input = input("Would you like a boy or girl name? ")

if input == "boy":
    print(random.choice(boy_names), random.choice(boy_names))
elif input == "girl": 
    print(random.choice(girl_names), random.choice(girl_names))
else:
    print("you have entered an invalid input, try again!")