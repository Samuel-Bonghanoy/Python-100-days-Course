age = input("What is your current age?")
timeleft = 90 - int(age)
months = timeleft * 12
weeks = timeleft * 52
days = timeleft * 365
print(f"You have {days} days, {weeks} weeks, and {months} months left.")

message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)