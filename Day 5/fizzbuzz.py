for n in range(1, 101):
    if n % 3 == 0:
        if n % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif n % 5 == 0:
        if n % 3 == 0:
            print("FizzBuzz")
        else:
            print("Buzz")
    else:
        print(n)

for n in range(1, 101): #better solution
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")