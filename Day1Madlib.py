#Mad libs generator (Day 1 of 100 days to code)
print("Welcome to Mad libs!")

#User input 
adj = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
verb_ing = input("Enter a verb ending in -ing: ")
pofbody = input("Enter part of body: ")

#madlib message
madlib = str("It was a " + adj + ", cold November day. I woke up to " + noun + " falling down the stairs. They " + verb + " their " + pofbody + " when they fell down the stairs. I asked them why they fell, to which they replied that they were " + verb_ing + "!")

#print madlib
print(madlib)
