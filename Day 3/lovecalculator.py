print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower1 = name1.lower()
lower2 = name2.lower()
# COULD ALSO COMBINE THE STRINGS AND THEN GET THE LETTER COUNTS
true = lower1.count("t") + lower1.count("r") + lower1.count("u") + lower1.count("e") + lower2.count("t") + lower2.count("r") + lower2.count("u") + lower2.count("e")
love = lower1.count("l") + lower1.count("o") + lower1.count("v") + lower1.count("e") + lower2.count("l") + lower2.count("o") + lower2.count("v") + lower2.count("e")

outcome = int(str(true) + str(love))

if outcome < 10 or outcome >= 90:
    print(f"Your score is {outcome}, you go together like coke and mentos.")
elif outcome > 40 and outcome < 50:
    print(f"Your score is {outcome}, you are alright together.")
else:
    print(f"Your score is {outcome}.")