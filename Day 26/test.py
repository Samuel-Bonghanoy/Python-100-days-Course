# with open("file1.txt") as number_file:
#     numbers = number_file.readlines()
#     numbers_list_1 = [number.strip() for number in numbers]

# with open("file2.txt") as number_file:
#     numbers = number_file.readlines()
#     numbers_list_2 = [number.strip() for number in numbers]

# result = [int(number) for number in numbers_list_1 if number in numbers_list_2]

# print(result)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

sentence_list = sentence.split()
print(sentence_list)