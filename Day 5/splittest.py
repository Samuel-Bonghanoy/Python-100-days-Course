from random import random


import random

members = input("Enter the names of the club members: ").split(", ")

print(members)
print(type(members))

members.extend(["Dexter", "Ash", "Darwin"])
print(members)

members.append("Katrina")
print(members)
print(len(members))

i = random.randint(0, (len(members) - 1))

print(f"The representative chosen for today will be {members[i]}!")