numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "samuel"
letters_list = [letter for letter in name]
print(letters_list)


range_list = [number * 2 for number in range(1,6)]
print(range_list)

range_list = [number * 2 for number in range(1,6) if number % 2 < 1]
print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elearnor", "Freddie"]
cap_names = [name.upper() for name in names if len(name) > 5]
print(cap_names)