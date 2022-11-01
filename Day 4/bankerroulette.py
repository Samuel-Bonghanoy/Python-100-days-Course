import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

unluckyperson = random.randint(0, (len(names) - 1))

print(f"{names[unluckyperson]} is going to buy the meal today!")

luckyperson = random.choice(names)
print(luckyperson + " is going to buy the meal today!")

