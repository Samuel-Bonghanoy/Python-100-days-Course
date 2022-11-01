def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
)

operations = {
   "+": add,
   "-": subtract,
   "*": multiply,
   "/": divide,
}

def calculator():
    num1 = float(input("What is the first number?: "))
    for operation in operations:
        print(operation)
    restart = True

    while restart:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number? "))
        operation = operations[operation_symbol]
        answer = operation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        restart_choice = input("Do you want to continue? Type 'y' for yes or 'n' to start a new calculation: ").lower()
        if restart_choice == "y":
            num1 = answer
            restart = True
        else:
            print("Goodbye")
            restart = False 
            calculator()

#if input(f"type y to continue calculating with {answer})
