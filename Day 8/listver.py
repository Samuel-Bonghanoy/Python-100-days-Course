alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
  list_ver = list(text)
  n = 0
  for letter in list_ver:
    list_ver[n] = alphabet[alphabet.index(letter) + shift]
    n += 1
  print(f"The econded text is {''.join(list_ver)}.")

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypt(text, shift)