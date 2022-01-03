#Dice simulator

#import random module
import random

#user input
yesorno = input("Care to roll the dice? ")
yesorno = str(yesorno)

#main 
if yesorno == ("yes"): 
    print("Rolling dice....The sum of the dice is ", random.randint(2,12))
elif yesorno == str("no"):
    print("The dice awaits.....")
else: 
    print("Enter a valid yes or no")
    
    
