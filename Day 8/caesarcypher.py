import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# # def encrypt(text, shift):
# #   cipher = ""
# #   for letter in text:
# #     position = alphabet.index(letter)
# #     new_position = position + shift
# #     new_letter = alphabet[new_position]
# #     cipher += new_letter
# #   print(f"The encoded text is {cipher}")

# # def decrypt(text, shift):
# #   cipher = ""
# #   for letter in text:
# #     position = alphabet.index(letter)
# #     new_position = position - shift
# #     new_letter = alphabet[new_position]
# #     cipher += new_letter
# #   print(f"The decoded text is {cipher}")

def caesar(direction, text, shift):
  shift %= 26
  if direction == "encode":
    list_ver = list(text)
    n = 0
    for char in list_ver:
      if char in alphabet:
        list_ver[n] = alphabet[alphabet.index(char) + shift]
        n += 1
    print(f"The encoded text is {''.join(list_ver)}.")
  elif direction == "decode":
    list_ver = list(text)
    n = 0
    for char in list_ver:
      if char in alphabet:
        list_ver[n] = alphabet[alphabet.index(char) - shift]
        n += 1
    print(f"The decoded text is {''.join(list_ver)}.")

restart = True
while restart:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(direction = direction, text = text, shift = shift)
  choice = input("Type 'yes' if you want to go again. Otherwise type 'no'. " ).lower()
  if choice == "no":
    restart = False
    print("Goodbye")


