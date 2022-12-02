import pandas

phonetic_data = pandas.read_csv("nato_phonetic_value.csv")

phonetic_dict = {row.letter: row.code for (index, row) in phonetic_data.iterrows()}

message = input("Enter a word: ").upper()

# for letter in list(message):
#     coded_message.append(phonetic_dict[letter])

# better way: coded_message = [phonetic_dict[letter] for letter in message]

coded_message = [phonetic_dict[letter] for letter in message]

print(coded_message)
