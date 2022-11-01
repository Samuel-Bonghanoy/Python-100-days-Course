print("Welcome to the tip calculator")
total = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

overall = total + ((percent / 100) * total)
individual = overall / people

formattt = "{:.2f}".format(individual)
print(f"Each person should pay: ${formattt}")
print(f"Each person should pay: ${round(individual, 2)}")