import random
import hangmanwords

print(hangmanwords.logo)
word = random.choice(hangmanwords.word_list)
display = []
repeated = []

for n in range(0, len(word)):
  display += "_"

list_ver = list(word)
lives = 6
ctr = 0

while not display == list_ver and not lives == 0: #
  if not list_ver == display:
    guess = input("Guess a letter: ").lower()
    ctr = 0
    if guess in repeated:
      print(f"You've already guessed {guess}")
    else:
      if guess in list_ver:
        for letter in word:
          if letter == guess:
            display[ctr] = guess
          ctr += 1
      else:
        lives -= 1
        print(f"You guessed {guess}. That is not in the word. You lose a life.")
  repeated += guess
  print(f"{' '.join(display)}")
  print(hangmanwords.stages[lives]) 

print(f"{' '.join(display)}")

if display == list_ver:
  print("You win!")
else:
  print("You lose!")
 
