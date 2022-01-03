
zodiac = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep"]


year = int(input("Please enter a year: "))

if ((year%400 == 0) or ((year%4 ==0) and(year%100 !=0))):
    print(year, "is a Leap Year!")
else:
    print(year, "is not a Leap year!")

if year%12 == 0:
    print("Chinese zodaic sign is", zodiac[0])
elif year%12 == 1:
    print("Chinese zociac sign is", zodiac[1])
elif year%12 == 2:
    print("Chinese zociac sign is", zodiac[2])
elif year%12 == 3:
    print("Chinese zociac sign is", zodiac[3])
elif year%12 == 4:
    print("Chinese zociac sign is", zodiac[4])
elif year%12 == 5:
    print("Chinese zociac sign is", zodiac[5])
elif year%12 == 6:
    print("Chinese zociac sign is", zodiac[6])
elif year%12 == 7:
    print("Chinese zociac sign is", zodiac[7])
elif year%12 == 8:
    print("Chinese zociac sign is", zodiac[8])
elif year%12 == 9:
    print("Chinese zociac sign is", zodiac[9])
elif year%12 == 10:
    print("Chinese zociac sign is", zodiac[10])
else:
    print("Chinese zociac sign is", zodiac[11])