number = int(input("Which number do you want to check? "))

check = number % 2

if check > 0: #could also do if number % 2 == 0:
    print("This is an odd number.")
else:
    print("This is an even number.")