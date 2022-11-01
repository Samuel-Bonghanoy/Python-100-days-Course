import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

rand_letters = ""
rand_symbols = ""
rand_numbers = ""
#password_list - [] - use this to initialize a list

for n in range(1, (nr_letters + 1)):
    rand_letters += letters[random.randint(0, (len(letters) - 1))] #THERE IS SUCH A THING AS random.choice(letters) TO GET A RANDOM ELEMENT IN THE LIST

for n in range(1, (nr_symbols + 1)):
    rand_symbols += symbols[random.randint(0, (len(symbols) - 1))]

for n in range(1, (nr_numbers + 1)):
    rand_numbers += numbers[random.randint(0, (len(numbers) - 1))]

password = rand_letters + rand_symbols + rand_numbers
shuffledpw = list(password)
random.shuffle(shuffledpw)
randpass = ""
for element in shuffledpw:
    randpass += element
print(randpass)
